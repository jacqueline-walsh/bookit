from django.test import TestCase
from order.models import Order, OrderItem

# Create your tests here.


class TestOrderModel(TestCase):

    def test_billing_address(self):
        billing_address = Order(billingName='Test Billing Name', billingAddress1='Test Address1',
                                billingCity="Test City", billingPostcode="Test Postcode", billingCountry="Test Country")
        self.assertEqual(billing_address.billingName, 'Test Billing Name')
        self.assertEqual(billing_address.billingAddress1, "Test Address1")
        self.assertEqual(billing_address.billingCity, "Test City")
        self.assertEqual(billing_address.billingPostcode, "Test Postcode")
        self.assertEqual(billing_address.billingCountry, "Test Country")

    def test_shipping_address(self):
        shipping_address = Order(shippingName='Test Billing Name', shippingAddress1='Test Address1',
                                shippingCity="Test City", shippingPostcode="Test Postcode", shippingCountry="Test Country")
        self.assertEqual(shipping_address.shippingName, 'Test Billing Name')
        self.assertEqual(shipping_address.shippingAddress1, "Test Address1")
        self.assertEqual(shipping_address.shippingCity, "Test City")
        self.assertEqual(shipping_address.shippingPostcode, "Test Postcode")
        self.assertEqual(shipping_address.shippingCountry, "Test Country")

    def test_place_order(self):
        order = Order(total=20.00, emailAddress="test@mail.com")
        order.save()
        self.assertEqual(order.total, 20.00)
        self.assertEqual(order.emailAddress, "test@mail.com")


class TestOrderItemModel(TestCase):

    def test_order_exists(self):
        order_id = Order(id=1, total=20.00)
        order_id.save()
        order_item = OrderItem(book="Test book title",
                                quantity=2, price=9.99, order=order_id)
        order_item.save()
        self.assertEqual(order_item.book, "Test book title")
        self.assertEqual(order_item.quantity, 2)
        self.assertEqual(order_item.price, 9.99)

    def test_sub_total(self):
        order_id = Order(id=1, total=9.99)
        order_id.save()        
        sub_total = OrderItem(quantity=2, price=9.99, order=order_id)
        sub_total.save()
        self.assertEqual(sub_total.quantity * sub_total.price, 19.98)

