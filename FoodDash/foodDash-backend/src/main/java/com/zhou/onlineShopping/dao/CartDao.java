package com.zhou.onlineShopping.dao;

import com.zhou.onlineShopping.entity.Cart;
import com.zhou.onlineShopping.entity.OrderItem;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

@Repository
public class CartDao {

    @Autowired
    private SessionFactory sessionFactory;

    public void removeCartItem(int orderItemId) {
        Session session = null;
        try {
            session = sessionFactory.openSession();
            OrderItem cartItem = session.get(OrderItem.class, orderItemId);
            Cart cart = cartItem.getCart();
            cart.getOrderItemList().remove(cartItem);

            session.beginTransaction();
            session.delete(cartItem);
            session.getTransaction().commit();

        } catch (Exception ex) {
            ex.printStackTrace();
            if (session != null) {
                session.getTransaction().rollback();
            }
        } finally {
            if (session != null) {
                session.close();
            }
        }

    }

    public void removeAllCartItems(Cart cart) {
        for (OrderItem item : cart.getOrderItemList()) {
            removeCartItem(item.getId());
        }
    }
}
