---
Description: The following are the registry functions.
ms.assetid: a490b748-42e8-462b-9a7f-a8b21438ea79
title: Registry Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Registry Functions

The following are the registry functions.



| Function                                                           | Description                                                                                                                                    |
|--------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetSystemRegistryQuota**](/windows/win32/Winbase/nf-winbase-getsystemregistryquota?branch=master)           | Retrieves the current size of the registry and the maximum size that the registry is allowed to attain on the system.                          |
| [**RegCloseKey**](/windows/win32/Winreg/nf-winreg-regclosekey?branch=master)                                 | Closes a handle to the specified registry key.                                                                                                 |
| [**RegConnectRegistry**](/windows/win32/Winreg/nf-winreg-regconnectregistrya?branch=master)                   | Establishes a connection to a predefined registry handle on another computer.                                                                  |
| [**RegCopyTree**](/windows/win32/Winreg/nf-winreg-regcopytreea?branch=master)                                 | Copies the specified registry key, along with its values and subkeys, to the specified destination key.                                        |
| [**RegCreateKeyEx**](/windows/win32/Winreg/nf-winreg-regcreatekeyexa?branch=master)                           | Creates the specified registry key.                                                                                                            |
| [**RegCreateKeyTransacted**](/windows/win32/Winreg/nf-winreg-regcreatekeytransacteda?branch=master)           | Creates the specified registry key and associates it with a transaction.                                                                       |
| [**RegDeleteKey**](/windows/win32/Winreg/nf-winreg-regdeletekeya?branch=master)                               | Deletes a subkey and its values.                                                                                                               |
| [**RegDeleteKeyEx**](/windows/win32/Winreg/nf-winreg-regdeletekeyexa?branch=master)                           | Deletes a subkey and its values from the specified platform-specific view of the registry.                                                     |
| [**RegDeleteKeyTransacted**](/windows/win32/Winreg/nf-winreg-regdeletekeytransacteda?branch=master)           | Deletes a subkey and its values from the specified platform-specific view of the registry as a transacted operation.                           |
| [**RegDeleteKeyValue**](/windows/win32/Winreg/nf-winreg-regdeletekeyvaluea?branch=master)                     | Removes the specified value from the specified registry key and subkey.                                                                        |
| [**RegDeleteTree**](/windows/win32/Winreg/nf-winreg-regdeletetreea?branch=master)                             | Deletes the subkeys and values of the specified key recursively.                                                                               |
| [**RegDeleteValue**](/windows/win32/Winreg/nf-winreg-regdeletevaluea?branch=master)                           | Removes a named value from the specified registry key.                                                                                         |
| [**RegDisablePredefinedCache**](/windows/win32/Winreg/nf-winreg-regdisablepredefinedcache?branch=master)     | Disables handle caching for the predefined registry handle for **HKEY\_CURRENT\_USER** for the current process.                                |
| [**RegDisablePredefinedCacheEx**](/windows/win32/Winreg/nf-winreg-regdisablepredefinedcacheex?branch=master) | Disables handle caching for all predefined registry handles for the current process.                                                           |
| [**RegDisableReflectionKey**](/windows/win32/Winreg/nf-winreg-regdisablereflectionkey?branch=master)         | Disables registry reflection for the specified key.                                                                                            |
| [**RegEnableReflectionKey**](/windows/win32/Winreg/nf-winreg-regenablereflectionkey?branch=master)           | Enables registry reflection for the specified disabled key.                                                                                    |
| [**RegEnumKeyEx**](/windows/win32/Winreg/nf-winreg-regenumkeyexa?branch=master)                               | Enumerates the subkeys of the specified open registry key.                                                                                     |
| [**RegEnumValue**](/windows/win32/Winreg/nf-winreg-regenumvaluea?branch=master)                               | Enumerates the values for the specified open registry key.                                                                                     |
| [**RegFlushKey**](/windows/win32/Winreg/nf-winreg-regflushkey?branch=master)                                 | Writes all attributes of the specified open registry key into the registry.                                                                    |
| [**RegGetKeySecurity**](https://msdn.microsoft.com/library/windows/desktop/aa379313)                | Retrieves a copy of the security descriptor protecting the specified open registry key.                                                        |
| [**RegGetValue**](/windows/win32/Winreg/nf-winreg-reggetvaluea?branch=master)                                 | Retrieves the type and data for the specified registry value.                                                                                  |
| [**RegLoadKey**](/windows/win32/Winreg/nf-winreg-regloadkeya?branch=master)                                   | Creates a subkey under **HKEY\_USERS** or **HKEY\_LOCAL\_MACHINE** and stores registration information from a specified file into that subkey. |
| [**RegLoadMUIString**](/windows/win32/Winreg/nf-winreg-regloadmuistringa?branch=master)                       | Loads the specified string from the specified key and subkey.                                                                                  |
| [**RegNotifyChangeKeyValue**](/windows/win32/Winreg/nf-winreg-regnotifychangekeyvalue?branch=master)         | Notifies the caller about changes to the attributes or contents of a specified registry key.                                                   |
| [**RegOpenCurrentUser**](/windows/win32/Winreg/nf-winreg-regopencurrentuser?branch=master)                   | Retrieves a handle to the **HKEY\_CURRENT\_USER** key for the user the current thread is impersonating.                                        |
| [**RegOpenKeyEx**](/windows/win32/Winreg/nf-winreg-regopenkeyexa?branch=master)                               | Opens the specified registry key.                                                                                                              |
| [**RegOpenKeyTransacted**](/windows/win32/Winreg/nf-winreg-regopenkeytransacteda?branch=master)               | Opens the specified registry key and associates it with a transaction.                                                                         |
| [**RegOpenUserClassesRoot**](/windows/win32/Winreg/nf-winreg-regopenuserclassesroot?branch=master)           | Retrieves a handle to the **HKEY\_CLASSES\_ROOT** key for the specified user.                                                                  |
| [**RegOverridePredefKey**](/windows/win32/Winreg/nf-winreg-regoverridepredefkey?branch=master)               | Maps a predefined registry key to a specified registry key.                                                                                    |
| [**RegQueryInfoKey**](/windows/win32/Winreg/nf-winreg-regqueryinfokeya?branch=master)                         | Retrieves information about the specified registry key.                                                                                        |
| [**RegQueryMultipleValues**](/windows/win32/Winreg/nf-winreg-regquerymultiplevaluesa?branch=master)           | Retrieves the type and data for a list of value names associated with an open registry key.                                                    |
| [**RegQueryReflectionKey**](/windows/win32/WinReg/nf-winreg-regqueryreflectionkey?branch=master)             | Determines whether reflection has been disabled or enabled for the specified key.                                                              |
| [**RegQueryValueEx**](/windows/win32/Winreg/nf-winreg-regqueryvalueexa?branch=master)                         | Retrieves the type and data for a specified value name associated with an open registry key.                                                   |
| [**RegReplaceKey**](/windows/win32/Winreg/nf-winreg-regreplacekeya?branch=master)                             | Replaces the file backing a registry key and all its subkeys with another file.                                                                |
| [**RegRestoreKey**](/windows/win32/Winreg/nf-winreg-regrestorekeya?branch=master)                             | Reads the registry information in a specified file and copies it over the specified key.                                                       |
| [**RegSaveKey**](/windows/win32/Winreg/nf-winreg-regsavekeya?branch=master)                                   | Saves the specified key and all of its subkeys and values to a new file.                                                                       |
| [**RegSaveKeyEx**](/windows/win32/Winreg/nf-winreg-regsavekeyexa?branch=master)                               | Saves the specified key and all of its subkeys and values to a new file. You can specify the format for the saved key or hive.                 |
| [**RegSetKeyValue**](/windows/win32/Winreg/nf-winreg-regsetkeyvaluea?branch=master)                           | Sets the data for the specified value in the specified registry key and subkey.                                                                |
| [**RegSetKeySecurity**](https://msdn.microsoft.com/library/windows/desktop/aa379314)                | Sets the security of an open registry key.                                                                                                     |
| [**RegSetValueEx**](/windows/win32/Winreg/nf-winreg-regsetvalueexa?branch=master)                             | Sets the data and type of a specified value under a registry key.                                                                              |
| [**RegUnLoadKey**](/windows/win32/Winreg/nf-winreg-regunloadkeya?branch=master)                               | Unloads the specified registry key and its subkeys from the registry.                                                                          |



 

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
| [**GetPrivateProfileInt**](/windows/win32/Winbase/nf-winbase-getprivateprofileint?branch=master)                   | Retrieves an integer associated with a key in the specified section of an initialization file.     |
| [**GetPrivateProfileSection**](/windows/win32/Winbase/nf-winbase-getprivateprofilesection?branch=master)           | Retrieves all the keys and values for the specified section of an initialization file.             |
| [**GetPrivateProfileSectionNames**](/windows/win32/Winbase/nf-winbase-getprivateprofilesectionnames?branch=master) | Retrieves the names of all sections in an initialization file.                                     |
| [**GetPrivateProfileString**](/windows/win32/Winbase/nf-winbase-getprivateprofilestring?branch=master)             | Retrieves a string from the specified section in an initialization file.                           |
| [**GetPrivateProfileStruct**](/windows/win32/Winbase/nf-winbase-getprivateprofilestruct?branch=master)             | Retrieves the data associated with a key in the specified section of an initialization file.       |
| [**GetProfileInt**](/windows/win32/Winbase/nf-winbase-getprofileinta?branch=master)                                 | Retrieves an integer from a key in the specified section of the Win.ini file.                      |
| [**GetProfileSection**](/windows/win32/Winbase/nf-winbase-getprofilesectiona?branch=master)                         | Retrieves all the keys and values for the specified section of the Win.ini file.                   |
| [**GetProfileString**](/windows/win32/Winbase/nf-winbase-getprofilestringa?branch=master)                           | Retrieves the string associated with a key in the specified section of the Win.ini file.           |
| [**WritePrivateProfileSection**](/windows/win32/Winbase/nf-winbase-writeprivateprofilesectiona?branch=master)       | Replaces the keys and values for the specified section in an initialization file.                  |
| [**WritePrivateProfileString**](/windows/win32/Winbase/nf-winbase-writeprivateprofilestringa?branch=master)         | Copies a string into the specified section of an initialization file.                              |
| [**WritePrivateProfileStruct**](/windows/win32/Winbase/nf-winbase-writeprivateprofilestructa?branch=master)         | Copies data into a key in the specified section of an initialization file.                         |
| [**WriteProfileSection**](/windows/win32/Winbase/nf-winbase-writeprofilesectiona?branch=master)                     | Replaces the contents of the specified section in the Win.ini file with specified keys and values. |
| [**WriteProfileString**](/windows/win32/Winbase/nf-winbase-writeprofilestringa?branch=master)                       | Copies a string into the specified section of the Win.ini file.                                    |



 

## Obsolete Functions

These functions are provided only for compatibility with 16-bit versions of Windows:

-   [**RegCreateKey**](/windows/win32/Winreg/nf-winreg-regcreatekeya?branch=master)
-   [**RegEnumKey**](/windows/win32/Winreg/nf-winreg-regenumkeya?branch=master)
-   [**RegOpenKey**](/windows/win32/Winreg/nf-winreg-regopenkeya?branch=master)
-   [**RegQueryValue**](/windows/win32/Winreg/nf-winreg-regqueryvaluea?branch=master)
-   [**RegSetValue**](/windows/win32/Winreg/nf-winreg-regsetvaluea?branch=master)

 

 



