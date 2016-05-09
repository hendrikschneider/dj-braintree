# from django.contrib.auth import get_user_model
# from django.test import TestCase
# from django.test.client import RequestFactory
#
# from djbraintree.models import Customer
#
# try:
#     import rest_framework
# except ImportError:
#     rest_framework = None
#
# if rest_framework:
#     from djbraintree.contrib.rest_framework.permissions import DJBraintreeSubscriptionPermission
#
#     class TestUserHasActiveSubscription(TestCase):
#
#         def setUp(self):
#             self.user = get_user_model().objects.create_user(username="pydanny",
#                                                              email="pydanny@gmail.com")
#             self.customer = Customer.objects.create(
#                 subscriber=self.user,
#                 stripe_id="cus_xxxxxxxxxxxxxxx",
#                 card_fingerprint="YYYYYYYY",
#                 card_last_4="2342",
#                 card_kind="Visa"
#             )
#
#         def test_no_user_in_request(self):
#             request = RequestFactory().get('djbraintree/')
#
#             self.assertFalse(DJBraintreeSubscriptionPermission().has_permission(request=request, view=None))
#
#         def test_user(self):
#             request = RequestFactory().get('djbraintree/')
#             request.user = self.user
#
#             self.assertFalse(DJBraintreeSubscriptionPermission().has_permission(request=request, view=None))
