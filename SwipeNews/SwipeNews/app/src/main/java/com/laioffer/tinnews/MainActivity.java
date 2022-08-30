package com.laioffer.tinnews;

import static android.widget.LinearLayout.HORIZONTAL;

import androidx.appcompat.app.AppCompatActivity;
import androidx.navigation.NavController;
import androidx.navigation.fragment.NavHostFragment;
import androidx.navigation.ui.NavigationUI;

import android.graphics.drawable.GradientDrawable;
import android.os.Bundle;
import android.util.Log;
import android.widget.LinearLayout;
import android.widget.TextView;

import com.google.android.material.bottomnavigation.BottomNavigationView;
import com.laioffer.tinnews.model.NewsResponse;
import com.laioffer.tinnews.network.NewsApi;
import com.laioffer.tinnews.network.RetrofitClient;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class MainActivity extends AppCompatActivity {

    private NavController navController;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
//        LinearLayout linearLayout = new LinearLayout(this);
//        linearLayout.setOrientation(HORIZONTAL);
//        TextView textView = new TextView(this);
//        textView.setText("Hello world");
//        linearLayout.addView(textView);
//        TextView textView1 = new TextView(this);
//        textView1.setText("Yo");
//        linearLayout.addView(textView1);
        setContentView(R.layout.activity_main);

        NavHostFragment navHostFragment = (NavHostFragment) getSupportFragmentManager()
                .findFragmentById(R.id.nav_host_fragment);
        navController = navHostFragment.getNavController();

        BottomNavigationView navView = findViewById(R.id.nav_view);
        NavigationUI.setupWithNavController(navView, navController);
        NavigationUI.setupActionBarWithNavController(this, navController);
//
//        // sample on using retrofit
//        NewsApi api = RetrofitClient.newInstance().create(NewsApi.class);
//        // endpoint: baseUrl/top-headlines/?q=tesla&pageSize=10
//        Call<NewsResponse> responseCall = api.getTopHeadlines("tesla", 10);


        // new a task, make the call<NewsResponse>
        // add task to queue
        // while(true) { retrofit keep check the queue }
        // if queue has `task`, retrofit do task: call endpoint, parse json , etc
        // once retrofit finish the task
        // callback.onRsponse(response)
        // if (task success) newsResponseCallback.onResponse()
        // else newsResponseCallback.onFailure()
//        Callback<NewsResponse> newsResponseCallback = new Callback<NewsResponse>() {
//            @Override
//            public void onResponse(Call<NewsResponse> call, Response<NewsResponse> response) {
//                if (response.isSuccessful()) {
//                    NewsResponse news = response.body();
//                    Log.d("getTopHeadlines", news.toString());
//                } else {
//                    Log.d("getTopHeadlines", response.toString());
//                }
//            }
//
//            @Override
//            public void onFailure(Call<NewsResponse> call, Throwable t) {
//                Log.d("getTopHeadlines", t.toString());
//            }
//        };
//
//        responseCall.enqueue(newsResponseCallback);
    }

    @Override
    public boolean onSupportNavigateUp() {
        return navController.navigateUp();
    }
}