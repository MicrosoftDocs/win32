---
Description: The following example uses the RegQueryInfoKey, RegEnumKeyEx, and RegEnumValue functions to enumerate the subkeys of the specified key.
ms.assetid: 3730180a-52bc-4382-83ca-39f162273ba5
title: Enumerating Registry Subkeys
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Enumerating Registry Subkeys

The following example uses the [**RegQueryInfoKey**](/windows/win32/Winreg/nf-winreg-regqueryinfokeya?branch=master), [**RegEnumKeyEx**](/windows/win32/Winreg/nf-winreg-regenumkeyexa?branch=master), and [**RegEnumValue**](/windows/win32/Winreg/nf-winreg-regenumvaluea?branch=master) functions to enumerate the subkeys of the specified key. The hKey parameter passed to each function is a handle to an open key. This key must be opened before the function call and closed afterward.


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
    DWORD    cbName;                   // size of name string 
    TCHAR    achClass[MAX_PATH] = TEXT("");  // buffer for class name 
    DWORD    cchClassName = MAX_PATH;  // size of class string 
    DWORD    cSubKeys=0;               // number of subkeys 
    DWORD    cbMaxSubKey;              // longest subkey size 
    DWORD    cchMaxClass;              // longest class string 
    DWORD    cValues;              // number of values for key 
    DWORD    cchMaxValue;          // longest value name 
    DWORD    cbMaxValueData;       // longest value data 
    DWORD    cbSecurityDescriptor; // size of security descriptor 
    FILETIME ftLastWriteTime;      // last write time 
 
    DWORD i, retCode; 
 
    TCHAR  achValue[MAX_VALUE_NAME]; 
    DWORD cchValue = MAX_VALUE_NAME; 
 
    // Get the class name and the value count. 
    retCode = RegQueryInfoKey(
        hKey,                    // key handle 
        achClass,                // buffer for class name 
        &amp;cchClassName,           // size of class string 
        NULL,                    // reserved 
        &amp;cSubKeys,               // number of subkeys 
        &amp;cbMaxSubKey,            // longest subkey size 
        &amp;cchMaxClass,            // longest class string 
        &amp;cValues,                // number of values for this key 
        &amp;cchMaxValue,            // longest value name 
        &amp;cbMaxValueData,         // longest value data 
        &amp;cbSecurityDescriptor,   // security descriptor 
        &amp;ftLastWriteTime);       // last write time 
 
    // Enumerate the subkeys, until RegEnumKeyEx fails.
    
    if (cSubKeys)
    {
        printf( "\nNumber of subkeys: %d\n", cSubKeys);

        for (i=0; i<cSubKeys; i++) 
        { 
            cbName = MAX_KEY_LENGTH;
            retCode = RegEnumKeyEx(hKey, i,
                     achKey, 
                     &amp;cbName, 
                     NULL, 
                     NULL, 
                     NULL, 
                     &amp;ftLastWriteTime); 
            if (retCode == ERROR_SUCCESS) 
            {
                _tprintf(TEXT("(%d) %s\n"), i+1, achKey);
            }
        }
    } 
 
    // Enumerate the key values. 

    if (cValues) 
    {
        printf( "\nNumber of values: %d\n", cValues);

        for (i=0, retCode=ERROR_SUCCESS; i<cValues; i++) 
        { 
            cchValue = MAX_VALUE_NAME; 
            achValue[0] = '\0'; 
            retCode = RegEnumValue(hKey, i, 
                achValue, 
                &amp;cchValue, 
                NULL, 
                NULL,
                NULL,
                NULL);
 
            if (retCode == ERROR_SUCCESS ) 
            { 
                _tprintf(TEXT("(%d) %s\n"), i+1, achValue); 
            } 
        }
    }
}

void __cdecl _tmain(void)
{
   HKEY hTestKey;

   if( RegOpenKeyEx( HKEY_CURRENT_USER,
        TEXT("SOFTWARE\\Microsoft"),
        0,
        KEY_READ,
        &amp;hTestKey) == ERROR_SUCCESS
      )
   {
      QueryKey(hTestKey);
   }
   
   RegCloseKey(hTestKey);
}
```



 

 



