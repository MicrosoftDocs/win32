---
description: The following example uses the RegQueryInfoKey, RegEnumKeyEx, and RegEnumValue functions to enumerate the subkeys of the specified key.
ms.assetid: 3730180a-52bc-4382-83ca-39f162273ba5
title: Enumerating Registry Subkeys
ms.topic: concept-article
ms.date: 05/31/2018
---

# Enumerating Registry Subkeys

The following example uses the [**RegQueryInfoKey**](/windows/desktop/api/Winreg/nf-winreg-regqueryinfokeya), [**RegEnumKeyEx**](/windows/desktop/api/Winreg/nf-winreg-regenumkeyexa), and [**RegEnumValue**](/windows/desktop/api/Winreg/nf-winreg-regenumvaluea) functions to enumerate the subkeys of the specified key. The hKey parameter passed to each function is a handle to an open key. This key must be opened before the function call and closed afterward.


```C++
// QueryKey - Enumerates the subkeys of key and its associated values.
//     hKey - Key whose subkeys and values are to be enumerated.

#include <windows.h>
#include <stdio.h>
#include <tchar.h>

#define MAX_KEY_LENGTH 255
#define MAX_VALUE_NAME 16383

void QueryKey(HKEY hKey)
{
    TCHAR    achKey[MAX_KEY_LENGTH];   // buffer for subkey name
    DWORD    cbName = 0;                   // size of name string 
    TCHAR    achClass[MAX_PATH] = TEXT("");  // buffer for class name 
    DWORD    cchClassName = MAX_PATH;  // size of class string 
    DWORD    cSubKeys = 0;               // number of subkeys 
    DWORD    cbMaxSubKey = 0;              // longest subkey size 
    DWORD    cchMaxClass = 0;              // longest class string 
    DWORD    cValues = 0;              // number of values for key 
    DWORD    cchMaxValue = 0;          // longest value name 
    DWORD    cbMaxValueData = 0;       // longest value data 
    DWORD    cbSecurityDescriptor = 0; // size of security descriptor 
    FILETIME ftLastWriteTime;      // last write time 

    DWORD i = 0, j = 0, retCode = 0;

    TCHAR  achValue[MAX_VALUE_NAME] = {'\0'};
    DWORD cchValue = MAX_VALUE_NAME;

    // Get the class name and the value count. 
    retCode = ::RegQueryInfoKey(
        hKey,                    // key handle 
        achClass,                // buffer for class name 
        &cchClassName,           // size of class string 
        NULL,                    // reserved 
        &cSubKeys,               // number of subkeys 
        &cbMaxSubKey,            // longest subkey size 
        &cchMaxClass,            // longest class string 
        &cValues,                // number of values for this key 
        &cchMaxValue,            // longest value name 
        &cbMaxValueData,         // longest value data 
        &cbSecurityDescriptor,   // security descriptor 
        &ftLastWriteTime);       // last write time 



    // Enumerate the subkeys, until RegEnumKeyEx fails.

    if (cSubKeys)
    {
        printf("\nNumber of subkeys: %d\n", cSubKeys);

        for (i = 0; i < cSubKeys; i++)
        {
            cbName = MAX_KEY_LENGTH;
            retCode = ::RegEnumKeyEx(hKey, i,
                achKey,
                &cbName,
                NULL,
                NULL,
                NULL,
                &ftLastWriteTime);

            if (retCode == ERROR_SUCCESS)
            {
                _tprintf(TEXT("(%d) %s\n"), i + 1, achKey);
            }
        }
    }

    // Enumerate the key values. 

    if (cValues)
    {
        printf("\nNumber of values: %d\n", cValues);

        for (i = 0; i < cValues; i++)
        {
            cchValue = MAX_VALUE_NAME;
            achValue[0] = '\0';
            retCode = ::RegEnumValue(hKey, i,
                achValue,
                &cchValue,
                NULL,
                NULL,
                NULL,
                NULL);

            if (retCode == ERROR_SUCCESS)
            {
                _tprintf(TEXT("(%d) %s\n"), i + 1, achValue);
            }
        }
    }
}

int __cdecl _tmain()
{
    HKEY hTestKey = 0;

    if (::RegOpenKeyEx(HKEY_CURRENT_USER,
        TEXT("SOFTWARE\\Microsoft"),
        0,
        KEY_READ,
        &hTestKey) == ERROR_SUCCESS
        )
    {
        QueryKey(hTestKey);
    }

    ::RegCloseKey(hTestKey);

    return 0;
}
```



 

 



