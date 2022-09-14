---
description: The performance data contains index values that you use to locate the names and help text for each registered object and counter.
ms.assetid: 9ddd1672-61cf-41c2-bec0-0d2b775bf970
title: Retrieving Counter Names and Help Text
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving Counter Names and Help Text

The performance data contains index values that you use to locate the names and help text for each registered object and counter. The **ObjectNameTitleIndex** and **ObjectHelpTitleIndex** members of the [**PERF\_OBJECT\_TYPE**](/windows/desktop/api/Winperf/ns-winperf-perf_object_type) structure contain the index values to the object name and help text, respectively, and the **CounterNameTitleIndex** and **CounterHelpTitleIndex** members of the [**PERF\_COUNTER\_DEFINITION**](/windows/desktop/api/Winperf/ns-winperf-perf_counter_definition) structure contain the index values to the counter name and help text, respectively.

To retrieve the names or help text, call the [**RegQueryValueEx**](/windows/desktop/api/winreg/nf-winreg-regqueryvalueexa) function. Set the *hKey* parameter to one of the following predefined keys. Typically, you would use the **HKEY\_PERFORMANCE\_NLSTEXT** key, so you do not have to determine the user's language identifier.



| Key                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **HKEY\_PERFORMANCE\_DATA**    | Query strings based on the language identifier value that you specify in the *lpValueName* parameter. Set *lpValueName* parameter to either "Counter &lt;langid&gt;" or "Help &lt;langid&gt;" to retrieve the names or help text, respectively, where "&lt;langid&gt;" is the system language identifier formatted as **zero-padded 3-digit hex number**. The language identifier is optional. If you do not specify a language identifier, the function returns English strings. Check the `HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Perflib` registry key for the list of languages available on your system.<br/>To retrieve text in most languages, specify the primary language identifier only. For example, to retrieve English strings, specify the language identifier as 009, not 1033 for English-US.<br/>To retrieve Chinese and Portuguese text, specify both the primary and sublanguage identifiers.<br/>**Windows Server 2003 and Windows XP:** Specify only the primary language identifier for Portuguese.<br/>**Windows 10**: "Help &lt;langid&gt;" text with custom language identifier always returns strings in English, although localized value can still be retrieved from the registry using the aforementioned key.<br/><br/> |
| **HKEY\_PERFORMANCE\_NLSTEXT** | Query strings based on the default UI language of the current user. Set the *lpValueName* parameter to either "Counter" or "Help" to retrieve the names or help text, respectively.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **HKEY\_PERFORMANCE\_TEXT**    | Query English strings. Set the *lpValueName* parameter to either "Counter" or "Help" to retrieve the names or help text, respectively.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |





The function returns the data as a list of strings. Each string is null-terminated. The last string is followed by an additional null terminator. The strings are listed in pairs. The first string of each pair is the index, and the second string is the text associated with the index. The counter data uses only even-numbered indexes, while the help data uses odd-numbered indexes. The pairs are returned in increasing index order.

The following lists show examples of counter and help data. Incrementing a given counter's index value by one gives you the index to the counter's help text. For example, 7 is the help index associated with counter index 6.

Counter data pairs.

<dl> 2 System
4 Memory
6 % Processor Time
</dl>

Help data pairs.

<dl> 3 The System object type includes those counters that ...
5 The Memory object type includes those counters that ...
7 Processor Time is expressed as a percentage of the ...
</dl>

Note that the first pair of strings in the counter data do not identify a counter name and can be ignored. The index number of the first pair is 1 and the string is a numeric string that represents the maximum index value for system counters.

For information on how a provider loads the name and help text, see [Adding Counter Names and Descriptions to the Registry](adding-counter-names-and-descriptions-to-the-registry.md).

There is no information in the text that indicates if the text identifies a counter or performance object. The only way to determine this, or the relationship between counters and objects, is to query the performance data itself. For example, if you want to display a list of objects and their counters in a user interface, you must retrieve the performance data, and then use the index values to parse the text data for the strings. For an example that does this, see [Displaying Object, Instance, and Counter Names](displaying-object-instance-and-counter-names.md).

The following example shows how to use **HKEY\_PERFORMANCE\_NLSTEXT** to retrieve the counter and help text and build a table for subsequent access.


```C++
#include <windows.h>
#include <stdio.h>

#pragma comment(lib, "advapi32.lib")

LPWSTR GetText(LPWSTR pwszSource);
BOOL BuildTextTable(LPWSTR pCounterHead, LPWSTR pHelpHead, LPDWORD* pOffsetsHead, LPDWORD pNumberOfOffsets);
DWORD GetNumberOfTextEntries(LPWSTR pwszSource);
void PrintCounterAndHelpText(LPWSTR pCounterTextHead, LPWSTR pHelpTextHead, LPDWORD pTextOffsets, DWORD dwNumberOfOffsets);

void wmain(void)
{
    LPWSTR pCounterTextHead = NULL; // Head of the MULTI_SZ buffer that contains the Counter text.
    LPWSTR pHelpTextHead = NULL;    // Head of the MULTI_SZ buffer that contains the Help text.
    LPDWORD pTextOffsets = NULL;    // Array of DWORDS that contain the offsets to the text in
                                    // pCounterTextHead and pHelpTextHead. The text index
                                    // values mirror the array index.
    DWORD dwNumberOfOffsets = 0;    // Number of elements in the pTextOffsets array.


    pCounterTextHead = GetText(L"Counter");
    if (NULL == pCounterTextHead)
    {
        wprintf(L"GetText(L\"Counter\") failed.\n");
        goto cleanup;
    }

    pHelpTextHead = GetText(L"Help");
    if (NULL == pHelpTextHead)
    {
        wprintf(L"GetText(L\"Help\") failed.\n");
        goto cleanup;
    }

    if (BuildTextTable(pCounterTextHead, pHelpTextHead, &pTextOffsets, &dwNumberOfOffsets))
    {
        PrintCounterAndHelpText(pCounterTextHead, pHelpTextHead, pTextOffsets, dwNumberOfOffsets);
    }
    else
    {
        wprintf(L"BuildTextTable failed.\n");
    }

cleanup:

    if (pCounterTextHead)
        free(pCounterTextHead);

    if (pHelpTextHead)
        free(pHelpTextHead);

    if (pTextOffsets)
        free(pTextOffsets);

    // You do not need to call RegCloseKey if you are only
    // retrieving names and help text.
}


// Get the text based on the source value. This function uses the
// HKEY_PERFORMANCE_NLSTEXT key to get the strings.
LPWSTR GetText(LPWSTR pwszSource)
{
    LPWSTR pBuffer = NULL;
    DWORD dwBufferSize = 0;
    LONG status = ERROR_SUCCESS;

    // Query the size of the text data so you can allocate the buffer.
    status = RegQueryValueEx(HKEY_PERFORMANCE_NLSTEXT, pwszSource, NULL, NULL, NULL, &dwBufferSize);
    if (ERROR_SUCCESS != status)
    {
        wprintf(L"RegQueryValueEx failed getting required buffer size. Error is 0x%x.\n", status);
        goto cleanup;
    }

    // Allocate the text buffer and query the text.
    pBuffer = (LPWSTR)malloc(dwBufferSize);
    if (pBuffer)
    {
        status = RegQueryValueEx(HKEY_PERFORMANCE_NLSTEXT, pwszSource, NULL, NULL, (LPBYTE)pBuffer, &dwBufferSize);
        if (ERROR_SUCCESS != status)
        {
            wprintf(L"RegQueryValueEx failed with 0x%x.\n", status);
            free(pBuffer);
            pBuffer = NULL;
            goto cleanup;
        }
    }
    else
    {
        wprintf(L"malloc failed to allocate memory.\n");
    }

cleanup:

    return pBuffer;
}


// Build a table of offsets into the counter and help text buffers. Use the index
// values from the performance data queries to access the offsets.
BOOL BuildTextTable(LPWSTR pCounterHead, LPWSTR pHelpHead, LPDWORD* pOffsetsHead, LPDWORD pNumberOfOffsets)
{
    BOOL fSuccess = FALSE;
    LPWSTR pwszCounterText = NULL;  // Used to cycle through the Counter text
    LPWSTR pwszHelpText = NULL;     // Used to cycle through the Help text
    LPDWORD pOffsets = NULL;
    DWORD dwCounterIndex = 0;       // Index value of the Counter text
    DWORD dwHelpIndex = 0;          // Index value of the Help text
    DWORD dwSize = 0;               // Size of the block of memory that holds the offset array


    pwszCounterText = pCounterHead;
    pwszHelpText = pHelpHead;

    *pNumberOfOffsets = GetNumberOfTextEntries(L"Last Help");
    if (0 == *pNumberOfOffsets)
    {
        wprintf(L"GetNumberOfTextEntries failed; returned 0 for number of entries.\n");
        goto cleanup;
    }

    dwSize = sizeof(DWORD) * (*pNumberOfOffsets + 1);  // Add one to make the array one-based

    pOffsets = (LPDWORD)malloc(dwSize);
    if (pOffsets)
    {
        ZeroMemory(pOffsets, dwSize);
        *pOffsetsHead = pOffsets;

        // Bypass first record (pair) of the counter data - contains upper bounds of system counter index.
        pwszCounterText += (wcslen(pwszCounterText)+1);
        pwszCounterText += (wcslen(pwszCounterText)+1);

        for (; *pwszCounterText; pwszCounterText += (wcslen(pwszCounterText)+1))
        {
            dwCounterIndex = _wtoi(pwszCounterText);
            dwHelpIndex = _wtoi(pwszHelpText);

            // Use the counter's index value as an indexer into the pOffsets array.
            // Store the offset to the counter text in the array element.
            pwszCounterText += (wcslen(pwszCounterText)+1);  //Skip past index value
            pOffsets[dwCounterIndex] = (DWORD)(pwszCounterText - pCounterHead);

            // Some help indexes for system counters do not have a matching counter, so loop
            // until you find the matching help index or the index is greater than the corresponding
            // counter index. For example, if the indexes were as follows, you would loop
            // until the help index was 11.
            //
            // Counter index       Help Index
            //   2                    3
            //   4                    5
            //   6                    7
            //                        9   (skip because there is no matching Counter index)
            //   10                   11
            while (*pwszHelpText && dwHelpIndex < dwCounterIndex)
            {
                pwszHelpText += (wcslen(pwszHelpText)+1);  // Skip past index value
                pwszHelpText += (wcslen(pwszHelpText)+1);  // Skip past help text to the next index value
                dwHelpIndex = _wtoi(pwszHelpText);
            }

            // Use the Help index value as an indexer into the pOffsets array.
            // Store the offset to the help text in the array element.
            if (dwHelpIndex == (dwCounterIndex + 1))
            {
                pwszHelpText += (wcslen(pwszHelpText)+1);  //Skip past index value
                pOffsets[dwHelpIndex] = (DWORD)(pwszHelpText - pHelpHead);
                pwszHelpText += (wcslen(pwszHelpText)+1);  //Skip past help text to next index value
            }
        }

        fSuccess = TRUE;
    }

cleanup:

    return fSuccess;
}


// Retrieve the last help index used from the registry. Use this number
// to allocate an array of DWORDs. Note that index values are not contiguous.
DWORD GetNumberOfTextEntries(LPWSTR pwszSource)
{
    DWORD dwEntries = 0;
    LONG status = ERROR_SUCCESS;
    HKEY hkey = NULL;
    DWORD dwSize = sizeof(DWORD);
    LPWSTR pwszMessage = NULL;

    status = RegOpenKeyEx(HKEY_LOCAL_MACHINE,
        L"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Perflib",
        0,
        KEY_READ,
        &hkey);

    if (ERROR_SUCCESS != status)
    {
        wprintf(L"RegOpenKeyEx failed with 0x%x.\n", status);
        goto cleanup;
    }

    status = RegQueryValueEx(hkey, pwszSource, NULL, 0, (LPBYTE)&dwEntries, &dwSize);

    if (ERROR_SUCCESS != status)
    {
        wprintf(L"RegQueryValueEx failed with 0x%x.\n", status);
    }

cleanup:

    if (hkey)
        RegCloseKey(hkey);

    return dwEntries;
}


// Print the pairs of counter and help text.
void PrintCounterAndHelpText(LPWSTR pCounterTextHead, LPWSTR pHelpTextHead, LPDWORD pTextOffsets, DWORD dwNumberOfOffsets)
{    UNREFERENCED_PARAMETER(dwNumberOfOffsets);
    // Counter index values are even numbers that start at 2 so begin with
    // the second element of the array of offsets. Many array elements will
    // not contain offset values (index values are not contiguous).

    // There is typically a large number of counters, so this example prints
    // the first 10 counters and help text.
    //for (DWORD i = 2; i < (dwNumberOfOffsets+1); i++)

    for (DWORD i = 2; i < 22; i++)
    {
        if (pTextOffsets[i]) // If index offset is not zero
        {
            if (0 == (i % 2)) // Counter text index (even number)
                wprintf(L"%d %s\n", i, pCounterTextHead+pTextOffsets[i]);
            else
                wprintf(L"%d %s\n\n", i, pHelpTextHead+pTextOffsets[i]);
        }
    }
}
```



The following example shows how to use **HKEY\_PERFORMANCE\_DATA** to retrieve the counter text.


```C++
#include <windows.h>
#include <stdio.h>
#include <strsafe.h>

#pragma comment(lib, "advapi32.lib")

LPWSTR GetText(LPWSTR pwszSource);
BOOL BuildTextTable(LPWSTR pCounterHead, LPWSTR pHelpHead, LPDWORD* pOffsetsHead, LPDWORD pNumberOfOffsets);
DWORD GetNumberOfTextEntries(LPWSTR pwszSource);
void PrintCounterAndHelpText(LPWSTR pCounterTextHead, LPWSTR pHelpTextHead, LPDWORD pTextOffsets, DWORD dwNumberOfOffsets);
LANGID GetLanguageId();

void wmain(void)
{
    LPWSTR pCounterTextHead = NULL; // Head of the MULTI_SZ buffer that contains the Counter text.
    LPWSTR pHelpTextHead = NULL;    // Head of the MULTI_SZ buffer that contains the Help text.
    LPDWORD pTextOffsets = NULL;    // Array of DWORDS that contain the offsets to the text in
                                    // pCounterTextHead and pHelpTextHead. The text index
                                    // values mirror the array index.
    DWORD dwNumberOfOffsets = 0;    // Number of elements in the pTextOffsets array.

    pCounterTextHead = GetText(L"Counter");
    if (NULL == pCounterTextHead)
    {
        wprintf(L"GetText(L\"Counter\") failed.\n");
        goto cleanup;
    }

    pHelpTextHead = GetText(L"Help");
    if (NULL == pHelpTextHead)
    {
        wprintf(L"GetText(L\"Help\") failed.\n");
        goto cleanup;
    }

    if (BuildTextTable(pCounterTextHead, pHelpTextHead, &pTextOffsets, &dwNumberOfOffsets))
    {
        PrintCounterAndHelpText(pCounterTextHead, pHelpTextHead, pTextOffsets, dwNumberOfOffsets);
    }
    else
    {
        wprintf(L"BuildTextTable failed.\n");
    }

cleanup:

    if (pCounterTextHead)
        free(pCounterTextHead);

    if (pHelpTextHead)
        free(pHelpTextHead);

    if (pTextOffsets)
        free(pTextOffsets);

    // You do not need to call RegCloseKey if you are only
    // retrieving names and help text.
}


// Get the text based on the source value. This function uses the
// HKEY_PERFORMANCE_DATA key to get the strings.
LPWSTR GetText(LPWSTR pwszSource)
{
    LPWSTR pBuffer = NULL;
    DWORD dwBufferSize = 0;
    LONG status = ERROR_SUCCESS;
    LANGID langid = 0;
    WCHAR wszSourceAndLangId[15];   // Identifies the source of the text; either
                                    // "Counter <langid>" or "Help <langid>"


    // Create the lpValueName string for the registry query.
    langid = GetLanguageId();
    if (0 == langid)
    {
        wprintf(L"GetLanguageId failed to get the default language identifier.\n");
        goto cleanup;
    }

    StringCchPrintf(wszSourceAndLangId, 15, L"%s %03x", pwszSource, langid);

    // Query the size of the text data so you can allocate the buffer.
    status = RegQueryValueEx(HKEY_PERFORMANCE_DATA, wszSourceAndLangId, NULL, NULL, NULL, &dwBufferSize);
    if (ERROR_SUCCESS != status)
    {
        wprintf(L"RegQueryValueEx failed getting required buffer size. Error is 0x%x.\n", status);
        goto cleanup;
    }

    // Allocate the text buffer and query the text.
    pBuffer = (LPWSTR)malloc(dwBufferSize);
    if (pBuffer)
    {
        status = RegQueryValueEx(HKEY_PERFORMANCE_DATA, wszSourceAndLangId, NULL, NULL, (LPBYTE)pBuffer, &dwBufferSize);
        if (ERROR_SUCCESS != status)
        {
            wprintf(L"RegQueryValueEx failed with 0x%x.\n", status);
            free(pBuffer);
            pBuffer = NULL;
            goto cleanup;
        }
    }
    else
    {
        wprintf(L"malloc failed to allocate memory.\n");
    }

cleanup:

    return pBuffer;
}


// Retrieve the default language identifier of the current user. For most languages,
// you use the primary language identifier only to retrieve the text. In Windows XP and
// Windows Server 2003, you use the complete language identifier to retrieve Chinese
// text. In Windows Vista, you use the complete language identifier to retrieve Portuguese
// text.
LANGID GetLanguageId()
{
    LANGID langid = 0;  // Complete language identifier.
    WORD primary = 0;   // Primary language identifier.
    OSVERSIONINFO osvi;

    ZeroMemory(&osvi, sizeof(OSVERSIONINFO));
    osvi.dwOSVersionInfoSize = sizeof(OSVERSIONINFO);

    if (GetVersionEx(&osvi))
    {
        langid = GetUserDefaultUILanguage();
        primary = PRIMARYLANGID(langid);

        if ( (LANG_PORTUGUESE == primary && osvi.dwBuildNumber > 5) || // Windows Vista and later
             (LANG_CHINESE == primary && (osvi.dwMajorVersion == 5 && osvi.dwMinorVersion >= 1)) ) // XP and Windows Server 2003
        {
            ; //Use the complete language identifier.
        }
        else
        {
            langid = primary;
        }
    }
    else
    {
        wprintf(L"GetVersionEx failed with 0x%x.\n", GetLastError());
    }

    return langid;
}


// Build a table of offsets into the counter and help text buffers. Use the index
// values from the performance data queries to access the offsets.
BOOL BuildTextTable(LPWSTR pCounterHead, LPWSTR pHelpHead, LPDWORD* pOffsetsHead, LPDWORD pNumberOfOffsets)
{
    BOOL fSuccess = FALSE;
    LPWSTR pwszCounterText = NULL;  // Used to cycle through the Counter text
    LPWSTR pwszHelpText = NULL;     // Used to cycle through the Help text
    LPDWORD pOffsets = NULL;
    DWORD dwCounterIndex = 0;       // Index value of the Counter text
    DWORD dwHelpIndex = 0;          // Index value of the Help text
    DWORD dwSize = 0;               // Size of the block of memory that holds the offset array

    pwszCounterText = pCounterHead;
    pwszHelpText = pHelpHead;

    *pNumberOfOffsets = GetNumberOfTextEntries(L"Last Help");
    if (0 == *pNumberOfOffsets)
    {
        wprintf(L"GetNumberOfTextEntries failed; returned 0 for number of entries.\n");
        goto cleanup;
    }

    dwSize = sizeof(DWORD) * (*pNumberOfOffsets + 1);  // Add one to make the array one-based

    pOffsets = (LPDWORD)malloc(dwSize);
    if (pOffsets)
    {
        ZeroMemory(pOffsets, dwSize);
        *pOffsetsHead = pOffsets;

        // Bypass first record (pair) of the counter data - contains upper bounds of system counter index.
        pwszCounterText += (wcslen(pwszCounterText)+1);
        pwszCounterText += (wcslen(pwszCounterText)+1);

        for (; *pwszCounterText; pwszCounterText += (wcslen(pwszCounterText)+1))
        {
            dwCounterIndex = _wtoi(pwszCounterText);
            dwHelpIndex = _wtoi(pwszHelpText);

            // Use the counter's index value as an indexer into the pOffsets array.
            // Store the offset to the counter text in the array element.
            pwszCounterText += (wcslen(pwszCounterText)+1);  //Skip past index value
            pOffsets[dwCounterIndex] = (DWORD)(pwszCounterText - pCounterHead);

            // Some help indexes for system counters do not have a matching counter, so loop
            // until you find the matching help index or the index is greater than the corresponding
            // counter index. For example, if the indexes were as follows, you would loop
            // until the help index was 11.
            //
            // Counter index       Help Index
            //   2                    3
            //   4                    5
            //   6                    7
            //                        9   (skip because there is no matching Counter index)
            //   10                   11
            while (*pwszHelpText && dwHelpIndex < dwCounterIndex)
            {
                pwszHelpText += (wcslen(pwszHelpText)+1);  // Skip past index value
                pwszHelpText += (wcslen(pwszHelpText)+1);  // Skip past help text to the next index value
                dwHelpIndex = _wtoi(pwszHelpText);
            }

            // Use the Help index value as an indexer into the pOffsets array.
            // Store the offset to the help text in the array element.
            if (dwHelpIndex == (dwCounterIndex + 1))
            {
                pwszHelpText += (wcslen(pwszHelpText)+1);  //Skip past index value
                pOffsets[dwHelpIndex] = (DWORD)(pwszHelpText - pHelpHead);
                pwszHelpText += (wcslen(pwszHelpText)+1);  //Skip past help text to next index value
            }
        }

        fSuccess = TRUE;
    }

cleanup:

    return fSuccess;
}


// Retrieve the last help index used from the registry. Use this number
// to allocate an array of DWORDs. Note that index values are not contiguous.
DWORD GetNumberOfTextEntries(LPWSTR pwszSource)
{
    DWORD dwEntries = 0;
    LONG status = ERROR_SUCCESS;
    HKEY hkey = NULL;
    DWORD dwSize = sizeof(DWORD);
    LPWSTR pwszMessage = NULL;

    status = RegOpenKeyEx(HKEY_LOCAL_MACHINE,
        L"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Perflib",
        0,
        KEY_READ,
        &hkey);

    if (ERROR_SUCCESS != status)
    {
        wprintf(L"RegOpenKeyEx failed with 0x%x.\n", status);
        goto cleanup;
    }

    status = RegQueryValueEx(hkey, pwszSource, NULL, 0, (LPBYTE)&dwEntries, &dwSize);

    if (ERROR_SUCCESS != status)
    {
        wprintf(L"RegQueryValueEx failed with 0x%x.\n", status);
    }

cleanup:

    if (hkey)
        RegCloseKey(hkey);

    return dwEntries;
}


// Print the pairs of counter and help text.
void PrintCounterAndHelpText(LPWSTR pCounterTextHead, LPWSTR pHelpTextHead, LPDWORD pTextOffsets, DWORD dwNumberOfOffsets)
{   UNREFERENCED_PARAMETER(dwNumberOfOffsets);
    // Counter index values are even numbers that start at 2 so begin with
    // the second element of the array of offsets. Many array elements will
    // not contain offset values (index values are not contiguous).

    // There is typically a large number of counters, so this example prints
    // the first 10 counters and help text.
    //for (DWORD i = 2; i < (dwNumberOfOffsets+1); i++)

    for (DWORD i = 2; i < 22; i++)
    {
        if (pTextOffsets[i]) // If index offset is not zero
        {
            if (0 == (i % 2)) // Counter text index (even number)
                wprintf(L"%d %s\n", i, pCounterTextHead+pTextOffsets[i]);
            else
                wprintf(L"%d %s\n\n", i, pHelpTextHead+pTextOffsets[i]);
        }
    }
}
```
