package com.laioffer.tinnews;

import androidx.annotation.NonNull;
import androidx.lifecycle.ViewModel;
import androidx.lifecycle.ViewModelProvider;

import com.laioffer.tinnews.repository.NewsRepository;
import com.laioffer.tinnews.ui.home.HomeViewModel;
import com.laioffer.tinnews.ui.save.SaveViewModel;
import com.laioffer.tinnews.ui.search.SearchViewModel;

public class NewsViewModelFactory implements ViewModelProvider.Factory {
    private final NewsRepository newsRepository;

    public NewsViewModelFactory(NewsRepository newsRepository) {
        this.newsRepository = newsRepository;
    }

    @NonNull
    @Override
    public <T extends ViewModel> T create(@NonNull Class<T> modelClass) {
        if (modelClass.isAssignableFrom(HomeViewModel.class)) {
            return (T) new HomeViewModel(newsRepository);
        } else if (modelClass.isAssignableFrom(SearchViewModel.class)) {
            return (T) new SearchViewModel(newsRepository);
        } else if (modelClass.isAssignableFrom(SaveViewModel.class)) {
            return (T) new SaveViewModel(newsRepository);
        } else {
            throw new IllegalStateException("Unknown ViewModel");
        }
    }
}
