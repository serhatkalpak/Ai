package com.example.yevmiye

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.lifecycle.viewmodel.compose.viewModel
import androidx.lifecycle.ViewModel
import androidx.lifecycle.ViewModelProvider
import androidx.lifecycle.viewModelScope
import com.example.yevmiye.data.YevmiyeEntry
import com.example.yevmiye.data.YevmiyeRepository
import com.example.yevmiye.ui.screens.HomeScreen
import com.example.yevmiye.ui.theme.YevmiyeHesaplaTheme
import kotlinx.coroutines.flow.SharingStarted
import kotlinx.coroutines.flow.stateIn
import kotlinx.coroutines.launch

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        
        val repository = YevmiyeRepository(applicationContext)
        
        setContent {
            YevmiyeHesaplaTheme {
                val viewModel: YevmiyeViewModel = viewModel(
                    factory = YevmiyeViewModelFactory(repository)
                )
                val entries by viewModel.entries.collectAsState()
                
                HomeScreen(
                    entries = entries,
                    onAddEntry = { viewModel.addEntry(it) },
                    onDeleteEntry = { viewModel.deleteEntry(it) }
                )
            }
        }
    }
}

class YevmiyeViewModel(private val repository: YevmiyeRepository) : ViewModel() {
    
    val entries = repository.entriesFlow
        .stateIn(viewModelScope, SharingStarted.Lazily, emptyList())
    
    fun addEntry(entry: YevmiyeEntry) {
        viewModelScope.launch {
            repository.addEntry(entry)
        }
    }
    
    fun deleteEntry(id: String) {
        viewModelScope.launch {
            repository.deleteEntry(id)
        }
    }
}

class YevmiyeViewModelFactory(
    private val repository: YevmiyeRepository
) : ViewModelProvider.Factory {
    @Suppress("UNCHECKED_CAST")
    override fun <T : ViewModel> create(modelClass: Class<T>): T {
        if (modelClass.isAssignableFrom(YevmiyeViewModel::class.java)) {
            return YevmiyeViewModel(repository) as T
        }
        throw IllegalArgumentException("Unknown ViewModel class")
    }
}
