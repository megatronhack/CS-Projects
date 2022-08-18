package com.zhou.onlineShopping;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.zhou.onlineShopping.entity.Customer;


import java.io.*;
import javax.servlet.http.*;
import javax.servlet.annotation.*;

@WebServlet(name = "helloServlet", value = "/hello-servlet")
public class HelloServlet extends HttpServlet {
    private String message;

    public void init() {
        message = "Hello World!";
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException {
        response.setContentType("application/json");
        ObjectMapper mapper = new ObjectMapper();
        Customer customer= new Customer();
        customer.setEmail("hellworld@gmail.com");
        customer.setPassword("123456");
        customer.setFirstName("bruce");
        customer.setLastName("wayne");
        customer.setEnabled(true);

        response.getWriter().print(mapper.writeValueAsString(customer));
    }



    public void destroy() {
    }
}