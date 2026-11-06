package com.example.yevmiye.data

import android.content.Context
import androidx.datastore.preferences.core.Preferences
import androidx.datastore.preferences.core.edit
import androidx.datastore.preferences.core.stringPreferencesKey
import androidx.datastore.preferences.preferencesDataStore
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.map
import org.json.JSONArray
import org.json.JSONObject

private val Context.dataStore by preferencesDataStore(name = "yevmiye_prefs")

data class YevmiyeEntry(
    val id: String,
    val date: String,
    val description: String,
    val amount: Double
)

class YevmiyeRepository(private val context: Context) {
    
    private val ENTRIES_KEY = stringPreferencesKey("yevmiye_entries")
    
    val entriesFlow: Flow<List<YevmiyeEntry>> = context.dataStore.data.map { preferences ->
        val jsonStr = preferences[ENTRIES_KEY] ?: "[]"
        parseEntries(jsonStr)
    }
    
    suspend fun addEntry(entry: YevmiyeEntry) {
        context.dataStore.edit { preferences ->
            val currentList = parseEntries(preferences[ENTRIES_KEY] ?: "[]").toMutableList()
            currentList.add(0, entry)
            preferences[ENTRIES_KEY] = serializeEntries(currentList)
        }
    }
    
    suspend fun deleteEntry(id: String) {
        context.dataStore.edit { preferences ->
            val currentList = parseEntries(preferences[ENTRIES_KEY] ?: "[]").toMutableList()
            currentList.removeAll { it.id == id }
            preferences[ENTRIES_KEY] = serializeEntries(currentList)
        }
    }
    
    private fun parseEntries(jsonStr: String): List<YevmiyeEntry> {
        val list = mutableListOf<YevmiyeEntry>()
        try {
            val jsonArray = JSONArray(jsonStr)
            for (i in 0 until jsonArray.length()) {
                val obj = jsonArray.getJSONObject(i)
                list.add(
                    YevmiyeEntry(
                        id = obj.getString("id"),
                        date = obj.getString("date"),
                        description = obj.getString("description"),
                        amount = obj.getDouble("amount")
                    )
                )
            }
        } catch (e: Exception) {
            e.printStackTrace()
        }
        return list
    }
    
    private fun serializeEntries(entries: List<YevmiyeEntry>): String {
        val jsonArray = JSONArray()
        entries.forEach { entry ->
            val obj = JSONObject().apply {
                put("id", entry.id)
                put("date", entry.date)
                put("description", entry.description)
                put("amount", entry.amount)
            }
            jsonArray.put(obj)
        }
        return jsonArray.toString()
    }
}
