---
Description: The following are the registry functions.
ms.assetid: a490b748-42e8-462b-9a7f-a8b21438ea79
title: Registry Functions
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Registry Functions

The following are the registry functions.



| Function                                                           | Description                                                                                                                                    |
|--------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetSystemRegistryQuota**](/windows/desktop/api/Winbase/nf-winbase-getsystemregistryquota)           | Retrieves the current size of the registry and the maximum size that the registry is allowed to attain on the system.                          |
| [**RegCloseKey**](/windows/desktop/api/Winreg/nf-winreg-regclosekey)                                 | Closes a handle to the specified registry key.                                                                                                 |
| [**RegConnectRegistry**](/windows/desktop/api/Winreg/nf-winreg-regconnectregistrya)                   | Establishes a connection to a predefined registry handle on another computer.                                                                  |
| [**RegCopyTree**](/windows/desktop/api/Winreg/nf-winreg-regcopytreea)                                 | Copies the specified registry key, along with its values and subkeys, to the specified destination key.                                        |
| [**RegCreateKeyEx**](/windows/desktop/api/Winreg/nf-winreg-regcreatekeyexa)                           | Creates the specified registry key.                                                                                                            |
| [**RegCreateKeyTransacted**](/windows/desktop/api/Winreg/nf-winreg-regcreatekeytransacteda)           | Creates the specified registry key and associates it with a transaction.                                                                       |
| [**RegDeleteKey**](/windows/desktop/api/Winreg/nf-winreg-regdeletekeya)                               | Deletes a subkey and its values.                                                                                                               |
| [**RegDeleteKeyEx**](/windows/desktop/api/Winreg/nf-winreg-regdeletekeyexa)                           | Deletes a subkey and its values from the specified platform-specific view of the registry.                                                     |
| [**RegDeleteKeyTransacted**](/windows/desktop/api/Winreg/nf-winreg-regdeletekeytransacteda)           | Deletes a subkey and its values from the specified platform-specific view of the registry as a transacted operation.                           |
| [**RegDeleteKeyValue**](/windows/desktop/api/Winreg/nf-winreg-regdeletekeyvaluea)                     | Removes the specified value from the specified registry key and subkey.                                                                        |
| [**RegDeleteTree**](/windows/desktop/api/Winreg/nf-winreg-regdeletetreea)                             | Deletes the subkeys and values of the specified key recursively.                                                                               |
| [**RegDeleteValue**](/windows/desktop/api/Winreg/nf-winreg-regdeletevaluea)                           | Removes a named value from the specified registry key.                                                                                         |
| [**RegDisablePredefinedCache**](/windows/desktop/api/Winreg/nf-winreg-regdisablepredefinedcache)     | Disables handle caching for the predefined registry handle for **HKEY\_CURRENT\_USER** for the current process.                                |
| [**RegDisablePredefinedCacheEx**](/windows/desktop/api/Winreg/nf-winreg-regdisablepredefinedcacheex) | Disables handle caching for all predefined registry handles for the current process.                                                           |
| [**RegDisableReflectionKey**](/windows/desktop/api/Winreg/nf-winreg-regdisablereflectionkey)         | Disables registry reflection for the specified key.                                                                                            |
| [**RegEnableReflectionKey**](/windows/desktop/api/Winreg/nf-winreg-regenablereflectionkey)           | Enables registry reflection for the specified disabled key.                                                                                    |
| [**RegEnumKeyEx**](/windows/desktop/api/Winreg/nf-winreg-regenumkeyexa)                               | Enumerates the subkeys of the specified open registry key.                                                                                     |
| [**RegEnumValue**](/windows/desktop/api/Winreg/nf-winreg-regenumvaluea)                               | Enumerates the values for the specified open registry key.                                                                                     |
| [**RegFlushKey**](/windows/desktop/api/Winreg/nf-winreg-regflushkey)                                 | Writes all attributes of the specified open registry key into the registry.                                                                    |
| [**RegGetKeySecurity**](https://msdn.microsoft.com/library/windows/desktop/aa379313)                | Retrieves a copy of the security descriptor protecting the specified open registry key.                                                        |
| [**RegGetValue**](/windows/desktop/api/Winreg/nf-winreg-reggetvaluea)                                 | Retrieves the type and data for the specified registry value.                                                                                  |
| [**RegLoadKey**](/windows/desktop/api/Winreg/nf-winreg-regloadkeya)                                   | Creates a subkey under **HKEY\_USERS** or **HKEY\_LOCAL\_MACHINE** and stores registration information from a specified file into that subkey. |
| [**RegLoadMUIString**](/windows/desktop/api/Winreg/nf-winreg-regloadmuistringa)                       | Loads the specified string from the specified key and subkey.                                                                                  |
| [**RegNotifyChangeKeyValue**](/windows/desktop/api/Winreg/nf-winreg-regnotifychangekeyvalue)         | Notifies the caller about changes to the attributes or contents of a specified registry key.                                                   |
| [**RegOpenCurrentUser**](/windows/desktop/api/Winreg/nf-winreg-regopencurrentuser)                   | Retrieves a handle to the **HKEY\_CURRENT\_USER** key for the user the current thread is impersonating.                                        |
| [**RegOpenKeyEx**](/windows/desktop/api/Winreg/nf-winreg-regopenkeyexa)                               | Opens the specified registry key.                                                                                                              |
| [**RegOpenKeyTransacted**](/windows/desktop/api/Winreg/nf-winreg-regopenkeytransacteda)               | Opens the specified registry key and associates it with a transaction.                                                                         |
| [**RegOpenUserClassesRoot**](/windows/desktop/api/Winreg/nf-winreg-regopenuserclassesroot)           | Retrieves a handle to the **HKEY\_CLASSES\_ROOT** key for the specified user.                                                                  |
| [**RegOverridePredefKey**](/windows/desktop/api/Winreg/nf-winreg-regoverridepredefkey)               | Maps a predefined registry key to a specified registry key.                                                                                    |
| [**RegQueryInfoKey**](/windows/desktop/api/Winreg/nf-winreg-regqueryinfokeya)                         | Retrieves information about the specified registry key.                                                                                        |
| [**RegQueryMultipleValues**](/windows/desktop/api/Winreg/nf-winreg-regquerymultiplevaluesa)           | Retrieves the type and data for a list of value names associated with an open registry key.                                                    |
| [**RegQueryReflectionKey**](/windows/desktop/api/WinReg/nf-winreg-regqueryreflectionkey)             | Determines whether reflection has been disabled or enabled for the specified key.                                                              |
| [**RegQueryValueEx**](/windows/desktop/api/Winreg/nf-winreg-regqueryvalueexa)                         | Retrieves the type and data for a specified value name associated with an open registry key.                                                   |
| [**RegReplaceKey**](/windows/desktop/api/Winreg/nf-winreg-regreplacekeya)                             | Replaces the file backing a registry key and all its subkeys with another file.                                                                |
| [**RegRestoreKey**](/windows/desktop/api/Winreg/nf-winreg-regrestorekeya)                             | Reads the registry information in a specified file and copies it over the specified key.                                                       |
| [**RegSaveKey**](/windows/desktop/api/Winreg/nf-winreg-regsavekeya)                                   | Saves the specified key and all of its subkeys and values to a new file.                                                                       |
| [**RegSaveKeyEx**](/windows/desktop/api/Winreg/nf-winreg-regsavekeyexa)                               | Saves the specified key and all of its subkeys and values to a new file. You can specify the format for the saved key or hive.                 |
| [**RegSetKeyValue**](/windows/desktop/api/Winreg/nf-winreg-regsetkeyvaluea)                           | Sets the data for the specified value in the specified registry key and subkey.                                                                |
| [**RegSetKeySecurity**](https://msdn.microsoft.com/library/windows/desktop/aa379314)                | Sets the security of an open registry key.                                                                                                     |
| [**RegSetValueEx**](/windows/desktop/api/Winreg/nf-winreg-regsetvalueexa)                             | Sets the data and type of a specified value under a registry key.                                                                              |
| [**RegUnLoadKey**](/windows/desktop/api/Winreg/nf-winreg-regunloadkeya)                               | Unloads the specified registry key and its subkeys from the registry.                                                                          |



 

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
| [**GetPrivateProfileInt**](/windows/desktop/api/Winbase/nf-winbase-getprivateprofileint)                   | Retrieves an integer associated with a key in the specified section of an initialization file.     |
| [**GetPrivateProfileSection**](/windows/desktop/api/Winbase/nf-winbase-getprivateprofilesection)           | Retrieves all the keys and values for the specified section of an initialization file.             |
| [**GetPrivateProfileSectionNames**](/windows/desktop/api/Winbase/nf-winbase-getprivateprofilesectionnames) | Retrieves the names of all sections in an initialization file.                                     |
| [**GetPrivateProfileString**](/windows/desktop/api/Winbase/nf-winbase-getprivateprofilestring)             | Retrieves a string from the specified section in an initialization file.                           |
| [**GetPrivateProfileStruct**](/windows/desktop/api/Winbase/nf-winbase-getprivateprofilestruct)             | Retrieves the data associated with a key in the specified section of an initialization file.       |
| [**GetProfileInt**](/windows/desktop/api/Winbase/nf-winbase-getprofileinta)                                 | Retrieves an integer from a key in the specified section of the Win.ini file.                      |
| [**GetProfileSection**](/windows/desktop/api/Winbase/nf-winbase-getprofilesectiona)                         | Retrieves all the keys and values for the specified section of the Win.ini file.                   |
| [**GetProfileString**](/windows/desktop/api/Winbase/nf-winbase-getprofilestringa)                           | Retrieves the string associated with a key in the specified section of the Win.ini file.           |
| [**WritePrivateProfileSection**](/windows/desktop/api/Winbase/nf-winbase-writeprivateprofilesectiona)       | Replaces the keys and values for the specified section in an initialization file.                  |
| [**WritePrivateProfileString**](/windows/desktop/api/Winbase/nf-winbase-writeprivateprofilestringa)         | Copies a string into the specified section of an initialization file.                              |
| [**WritePrivateProfileStruct**](/windows/desktop/api/Winbase/nf-winbase-writeprivateprofilestructa)         | Copies data into a key in the specified section of an initialization file.                         |
| [**WriteProfileSection**](/windows/desktop/api/Winbase/nf-winbase-writeprofilesectiona)                     | Replaces the contents of the specified section in the Win.ini file with specified keys and values. |
| [**WriteProfileString**](/windows/desktop/api/Winbase/nf-winbase-writeprofilestringa)                       | Copies a string into the specified section of the Win.ini file.                                    |



 

## Obsolete Functions

These functions are provided only for compatibility with 16-bit versions of Windows:

-   [**RegCreateKey**](/windows/desktop/api/Winreg/nf-winreg-regcreatekeya)
-   [**RegEnumKey**](/windows/desktop/api/Winreg/nf-winreg-regenumkeya)
-   [**RegOpenKey**](/windows/desktop/api/Winreg/nf-winreg-regopenkeya)
-   [**RegQueryValue**](/windows/desktop/api/Winreg/nf-winreg-regqueryvaluea)
-   [**RegSetValue**](/windows/desktop/api/Winreg/nf-winreg-regsetvaluea)

 

 



