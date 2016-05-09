# import datetime
# import decimal
#
# from django.contrib.auth import get_user_model
# from django.contrib.auth.models import AnonymousUser
# from django.core.exceptions import ImproperlyConfigured
# from django.http import HttpResponse
# from django.test import TestCase
# from django.test.client import RequestFactory
# from django.utils import timezone
#
# from unittest2 import TestCase as AssertWarnsEnabledTestCase
#
# from djbraintree.decorators import subscription_payment_required
# from djbraintree.models import Customer, CurrentSubscription
# from djbraintree.stripe_objects import stripe_temporary_api_key
#
#
# class TestDeprecationWarning(AssertWarnsEnabledTestCase):
#     """
#     Tests the deprecation warning set in the decorators file.
#     See https://docs.python.org/3.4/library/warnings.html#testing-warnings
#     """
#
#     def test_deprecation(self):
#         with self.assertWarns(DeprecationWarning):
#             from djbraintree.decorators import user_passes_pay_test
#
#             test_func = (lambda subscriber: True)
#             user_passes_pay_test(test_func=test_func)
#
#
# class TestTemporaryKey(TestCase):
#     def test_basic(self):
#         import stripe
#         key = stripe.api_key
#
#         with stripe_temporary_api_key("newkey"):
#             self.assertEqual(stripe.api_key, "newkey")
#
#         self.assertEqual(stripe.api_key, key)
#
#
# class TestSubscriptionPaymentRequired(TestCase):
#
#     def setUp(self):
#         self.settings(ROOT_URLCONF='tests.test_urls')
#         self.factory = RequestFactory()
#
#     def test_direct(self):
#         subscription_payment_required(function=None)
#
#     def test_anonymous(self):
#
#         @subscription_payment_required
#         def a_view(request):
#             return HttpResponse()
#
#         request = self.factory.get('/account/')
#         request.user = AnonymousUser()
#         self.assertRaises(ImproperlyConfigured, a_view, request)
#
#     def test_user_unpaid(self):
#         # create customer object with no subscription
#         user = get_user_model().objects.create_user(username="pydanny",
#                                                     email="pydanny@gmail.com")
#         Customer.objects.create(
#             subscriber=user,
#             stripe_id="cus_xxxxxxxxxxxxxxx",
#             card_fingerprint="YYYYYYYY",
#             card_last_4="2342",
#             card_kind="Visa"
#         )
#
#         @subscription_payment_required
#         def a_view(request):
#             return HttpResponse()
#
#         request = self.factory.get('/account/')
#         request.user = user
#
#         response = a_view(request)
#         self.assertEqual(response.status_code, 302)
#
#     def test_user_active_subscription(self):
#         period_start = datetime.datetime(2013, 4, 1, tzinfo=timezone.utc)
#         period_end = datetime.datetime(2030, 4, 30, tzinfo=timezone.utc)
#         start = datetime.datetime(2013, 1, 1, tzinfo=timezone.utc)
#         user = get_user_model().objects.create_user(username="pydanny",
#                                                     email="pydanny@gmail.com")
#
#         customer = Customer.objects.create(
#             subscriber=user,
#             stripe_id="cus_xxxxxxxxxxxxxxx",
#             card_fingerprint="YYYYYYYY",
#             card_last_4="2342",
#             card_kind="Visa"
#         )
#         CurrentSubscription.objects.create(
#             customer=customer,
#             plan="test",
#             current_period_start=period_start,
#             current_period_end=period_end,
#             amount=(500 / decimal.Decimal("100.0")),
#             status="active",
#             start=start,
#             quantity=1
#         )
#
#         @subscription_payment_required
#         def a_view(request):
#             return HttpResponse()
#
#         request = self.factory.get('/account/')
#         request.user = user
#         response = a_view(request)
#         self.assertEqual(response.status_code, 200)
