package com.zhou.onlineShopping.service;

import com.zhou.onlineShopping.dao.CustomerDao;
import com.zhou.onlineShopping.entity.Cart;
import com.zhou.onlineShopping.entity.Customer;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class CustomerService {

    @Autowired
    private CustomerDao customerDao;

    public void signUp(Customer customer) {
        Cart cart = new Cart();
        customer.setCart(cart);

        customer.setEnabled(true);
        customerDao.signUp(customer);

    }

    public Customer getCustomer(String email) {
        return customerDao.getCustomer(email);
    }

}
