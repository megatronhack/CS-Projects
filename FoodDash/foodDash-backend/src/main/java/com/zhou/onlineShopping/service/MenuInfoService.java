package com.zhou.onlineShopping.service;

import com.zhou.onlineShopping.dao.MenuInfoDao;
import com.zhou.onlineShopping.entity.MenuItem;
import com.zhou.onlineShopping.entity.Restaurant;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;

import java.util.List;

@Service
public class MenuInfoService {

    @Autowired
    private MenuInfoDao menuInfoDao;


    public List<Restaurant> getRestaurants() {
        return menuInfoDao.getRestaurants();
    }

    public List<MenuItem> getAllMenuItem(int restaurantId) {
        return menuInfoDao.getAllMenuItem(restaurantId);
    }

    public MenuItem getMenuItem(int id) {
        return menuInfoDao.getMenuItem(id);
    }
}





