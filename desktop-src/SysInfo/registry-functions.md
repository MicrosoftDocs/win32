---
Description: 'The following are the registry functions.'
ms.assetid: 'a490b748-42e8-462b-9a7f-a8b21438ea79'
title: Registry Functions
---

# Registry Functions

The following are the registry functions.



| Function                                                           | Description                                                                                                                                    |
|--------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetSystemRegistryQuota**](getsystemregistryquota.md)           | Retrieves the current size of the registry and the maximum size that the registry is allowed to attain on the system.                          |
| [**RegCloseKey**](regclosekey.md)                                 | Closes a handle to the specified registry key.                                                                                                 |
| [**RegConnectRegistry**](regconnectregistry.md)                   | Establishes a connection to a predefined registry handle on another computer.                                                                  |
| [**RegCopyTree**](regcopytree.md)                                 | Copies the specified registry key, along with its values and subkeys, to the specified destination key.                                        |
| [**RegCreateKeyEx**](regcreatekeyex.md)                           | Creates the specified registry key.                                                                                                            |
| [**RegCreateKeyTransacted**](regcreatekeytransacted.md)           | Creates the specified registry key and associates it with a transaction.                                                                       |
| [**RegDeleteKey**](regdeletekey.md)                               | Deletes a subkey and its values.                                                                                                               |
| [**RegDeleteKeyEx**](regdeletekeyex.md)                           | Deletes a subkey and its values from the specified platform-specific view of the registry.                                                     |
| [**RegDeleteKeyTransacted**](regdeletekeytransacted.md)           | Deletes a subkey and its values from the specified platform-specific view of the registry as a transacted operation.                           |
| [**RegDeleteKeyValue**](regdeletekeyvalue.md)                     | Removes the specified value from the specified registry key and subkey.                                                                        |
| [**RegDeleteTree**](regdeletetree.md)                             | Deletes the subkeys and values of the specified key recursively.                                                                               |
| [**RegDeleteValue**](regdeletevalue.md)                           | Removes a named value from the specified registry key.                                                                                         |
| [**RegDisablePredefinedCache**](regdisablepredefinedcache.md)     | Disables handle caching for the predefined registry handle for **HKEY\_CURRENT\_USER** for the current process.                                |
| [**RegDisablePredefinedCacheEx**](regdisablepredefinedcacheex.md) | Disables handle caching for all predefined registry handles for the current process.                                                           |
| [**RegDisableReflectionKey**](regdisablereflectionkey.md)         | Disables registry reflection for the specified key.                                                                                            |
| [**RegEnableReflectionKey**](regenablereflectionkey.md)           | Enables registry reflection for the specified disabled key.                                                                                    |
| [**RegEnumKeyEx**](regenumkeyex.md)                               | Enumerates the subkeys of the specified open registry key.                                                                                     |
| [**RegEnumValue**](regenumvalue.md)                               | Enumerates the values for the specified open registry key.                                                                                     |
| [**RegFlushKey**](regflushkey.md)                                 | Writes all attributes of the specified open registry key into the registry.                                                                    |
| [**RegGetKeySecurity**](https://msdn.microsoft.com/library/windows/desktop/aa379313)                | Retrieves a copy of the security descriptor protecting the specified open registry key.                                                        |
| [**RegGetValue**](reggetvalue.md)                                 | Retrieves the type and data for the specified registry value.                                                                                  |
| [**RegLoadKey**](regloadkey.md)                                   | Creates a subkey under **HKEY\_USERS** or **HKEY\_LOCAL\_MACHINE** and stores registration information from a specified file into that subkey. |
| [**RegLoadMUIString**](regloadmuistring.md)                       | Loads the specified string from the specified key and subkey.                                                                                  |
| [**RegNotifyChangeKeyValue**](regnotifychangekeyvalue.md)         | Notifies the caller about changes to the attributes or contents of a specified registry key.                                                   |
| [**RegOpenCurrentUser**](regopencurrentuser.md)                   | Retrieves a handle to the **HKEY\_CURRENT\_USER** key for the user the current thread is impersonating.                                        |
| [**RegOpenKeyEx**](regopenkeyex.md)                               | Opens the specified registry key.                                                                                                              |
| [**RegOpenKeyTransacted**](regopenkeytransacted.md)               | Opens the specified registry key and associates it with a transaction.                                                                         |
| [**RegOpenUserClassesRoot**](regopenuserclassesroot.md)           | Retrieves a handle to the **HKEY\_CLASSES\_ROOT** key for the specified user.                                                                  |
| [**RegOverridePredefKey**](regoverridepredefkey.md)               | Maps a predefined registry key to a specified registry key.                                                                                    |
| [**RegQueryInfoKey**](regqueryinfokey.md)                         | Retrieves information about the specified registry key.                                                                                        |
| [**RegQueryMultipleValues**](regquerymultiplevalues.md)           | Retrieves the type and data for a list of value names associated with an open registry key.                                                    |
| [**RegQueryReflectionKey**](regqueryreflectionkey.md)             | Determines whether reflection has been disabled or enabled for the specified key.                                                              |
| [**RegQueryValueEx**](regqueryvalueex.md)                         | Retrieves the type and data for a specified value name associated with an open registry key.                                                   |
| [**RegReplaceKey**](regreplacekey.md)                             | Replaces the file backing a registry key and all its subkeys with another file.                                                                |
| [**RegRestoreKey**](regrestorekey.md)                             | Reads the registry information in a specified file and copies it over the specified key.                                                       |
| [**RegSaveKey**](regsavekey.md)                                   | Saves the specified key and all of its subkeys and values to a new file.                                                                       |
| [**RegSaveKeyEx**](regsavekeyex.md)                               | Saves the specified key and all of its subkeys and values to a new file. You can specify the format for the saved key or hive.                 |
| [**RegSetKeyValue**](regsetkeyvalue.md)                           | Sets the data for the specified value in the specified registry key and subkey.                                                                |
| [**RegSetKeySecurity**](https://msdn.microsoft.com/library/windows/desktop/aa379314)                | Sets the security of an open registry key.                                                                                                     |
| [**RegSetValueEx**](regsetvalueex.md)                             | Sets the data and type of a specified value under a registry key.                                                                              |
| [**RegUnLoadKey**](regunloadkey.md)                               | Unloads the specified registry key and its subkeys from the registry.                                                                          |



 

The following shell functions can be used with the registry:

-   [**AssocCreate**](https://msdn.microsoft.com/library/windows/desktop/bb773460)
-   [**AssocQueryKey**](https://msdn.microsoft.com/library/windows/desktop/bb773468)
-   [**AssocQueryString**](https://msdn.microsoft.com/library/windows/desktop/bb773471)
-   [**AssocQueryStringByKey**](https://msdn.microsoft.com/library/windows/desktop/bb773473)
-   [**SHCopyKey**](https://msdn.microsoft.com/library/windows/desktop/bb773482)
-   [**SHDeleteEmptyKey**](https://msdn.microsoft.com/library/windows/desktop/bb773485)
-   [**SHDeleteKey**](https://msdn.microsoft.com/library/windows/desktop/bb773486)
-   [**SHDeleteValue**](https://msdn.microsoft.com/library/windows/desktop/bb773489)
-   [**SHEnumKeyEx**](https://msdn.microsoft.com/library/windows/desktop/bb773491)
-   [**SHEnumValue**](https://msdn.microsoft.com/library/windows/desktop/bb773494)
-   [**SHGetValue**](https://msdn.microsoft.com/library/windows/desktop/bb773495)
-   [**SHQueryInfoKey**](https://msdn.microsoft.com/library/windows/desktop/bb773501)
-   [**SHQueryValueEx**](https://msdn.microsoft.com/library/windows/desktop/bb773502)
-   [**SHRegCloseUSKey**](https://msdn.microsoft.com/library/windows/desktop/bb773505)
-   [**SHRegCreateUSKey**](https://msdn.microsoft.com/library/windows/desktop/bb773507)
-   [**SHRegDeleteEmptyUSKey**](https://msdn.microsoft.com/library/windows/desktop/bb773510)
-   [**SHRegDeleteUSValue**](https://msdn.microsoft.com/library/windows/desktop/bb773511)
-   [**SHRegDuplicateHKey**](https://msdn.microsoft.com/library/windows/desktop/bb773516)
-   [**SHRegEnumUSKey**](https://msdn.microsoft.com/library/windows/desktop/bb773519)
-   [**SHRegEnumUSValue**](https://msdn.microsoft.com/library/windows/desktop/bb773520)
-   [**SHRegGetBoolUSValue**](https://msdn.microsoft.com/library/windows/desktop/bb773524)
-   [**SHRegGetIntW**](https://msdn.microsoft.com/library/windows/desktop/bb773529)
-   [**SHRegGetPath**](https://msdn.microsoft.com/library/windows/desktop/bb773532)
-   [**SHRegGetUSValue**](https://msdn.microsoft.com/library/windows/desktop/bb773534)
-   [**SHRegOpenUSKey**](https://msdn.microsoft.com/library/windows/desktop/bb773541)
-   [**SHRegQueryInfoUSKey**](https://msdn.microsoft.com/library/windows/desktop/bb773542)
-   [**SHRegQueryUSValue**](https://msdn.microsoft.com/library/windows/desktop/bb773545)
-   [**SHRegSetPath**](https://msdn.microsoft.com/library/windows/desktop/bb773548)
-   [**SHRegSetUSValue**](https://msdn.microsoft.com/library/windows/desktop/bb773549)
-   [**SHRegWriteUSValue**](https://msdn.microsoft.com/library/windows/desktop/bb773556)
-   [**SHSetValue**](https://msdn.microsoft.com/library/windows/desktop/bb773557)

The following are the initialization-file functions. They retrieve information from and copy information to a system- or application-defined initialization file. These functions are provided only for compatibility with 16-bit versions of Windows. New applications should use the registry.



| Function                                                               | Description                                                                                        |
|------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| [**GetPrivateProfileInt**](getprivateprofileint.md)                   | Retrieves an integer associated with a key in the specified section of an initialization file.     |
| [**GetPrivateProfileSection**](getprivateprofilesection.md)           | Retrieves all the keys and values for the specified section of an initialization file.             |
| [**GetPrivateProfileSectionNames**](getprivateprofilesectionnames.md) | Retrieves the names of all sections in an initialization file.                                     |
| [**GetPrivateProfileString**](getprivateprofilestring.md)             | Retrieves a string from the specified section in an initialization file.                           |
| [**GetPrivateProfileStruct**](getprivateprofilestruct.md)             | Retrieves the data associated with a key in the specified section of an initialization file.       |
| [**GetProfileInt**](getprofileint.md)                                 | Retrieves an integer from a key in the specified section of the Win.ini file.                      |
| [**GetProfileSection**](getprofilesection.md)                         | Retrieves all the keys and values for the specified section of the Win.ini file.                   |
| [**GetProfileString**](getprofilestring.md)                           | Retrieves the string associated with a key in the specified section of the Win.ini file.           |
| [**WritePrivateProfileSection**](writeprivateprofilesection.md)       | Replaces the keys and values for the specified section in an initialization file.                  |
| [**WritePrivateProfileString**](writeprivateprofilestring.md)         | Copies a string into the specified section of an initialization file.                              |
| [**WritePrivateProfileStruct**](writeprivateprofilestruct.md)         | Copies data into a key in the specified section of an initialization file.                         |
| [**WriteProfileSection**](writeprofilesection.md)                     | Replaces the contents of the specified section in the Win.ini file with specified keys and values. |
| [**WriteProfileString**](writeprofilestring.md)                       | Copies a string into the specified section of the Win.ini file.                                    |



 

## Obsolete Functions

These functions are provided only for compatibility with 16-bit versions of Windows:

-   [**RegCreateKey**](regcreatekey.md)
-   [**RegEnumKey**](regenumkey.md)
-   [**RegOpenKey**](regopenkey.md)
-   [**RegQueryValue**](regqueryvalue.md)
-   [**RegSetValue**](regsetvalue.md)

 

 



