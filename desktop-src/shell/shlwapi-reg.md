---
Description: This section describes the Windows Shell registry handling functions. The programming elements explained in this documentation are exported by Shlwapi.dll and defined in Shlwapi.h and Shlwapi.lib.
title: Shell Registry Handling Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Shell Registry Handling Functions

This section describes the Windows Shell registry handling functions. The programming elements explained in this documentation are exported by Shlwapi.dll and defined in Shlwapi.h and Shlwapi.lib.

## In this section



| Topic                                                             | Description                                                                                                                                                                         |
|-------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AssocCreate**](/windows/win32/Shlwapi/nf-shlwapi-assoccreate?branch=master)<br/>                     | Returns a pointer to an [**IQueryAssociations**](/windows/win32/Shlwapi/?branch=master) object.<br/>                                                                                         |
| [**AssocGetPerceivedType**](/windows/win32/Shlwapi/nf-shlwapi-assocgetperceivedtype?branch=master)<br/> | Retrieves a file's perceived type based on its extension.<br/>                                                                                                                |
| [**AssocIsDangerous**](/windows/win32/Shlwapi/nf-shlwapi-associsdangerous?branch=master)<br/>           | Determines whether a file type is considered a potential security risk.<br/>                                                                                                  |
| [**AssocQueryKey**](/windows/win32/Shlwapi/nf-shlwapi-assocquerykeya?branch=master)<br/>                 | Searches for and retrieves a key related to a file or protocol association from the registry.<br/>                                                                            |
| [**AssocQueryString**](/windows/win32/Shlwapi/nf-shlwapi-assocquerystringa?branch=master)<br/>           | Searches for and retrieves a file or protocol association-related string from the registry.<br/>                                                                              |
| [**AssocQueryStringByKey**](/windows/win32/Shlwapi/nf-shlwapi-assocquerystringbykeya?branch=master)<br/> | Searches for and retrieves a file association-related string from the registry starting from a specified key.<br/>                                                            |
| [**SHCopyKey**](/windows/win32/Shlwapi/nf-shlwapi-shcopykeya?branch=master)<br/>                         | Recursively copies the subkeys and values of the source subkey to the destination key. [**SHCopyKey**](/windows/win32/Shlwapi/nf-shlwapi-shcopykeya?branch=master) does not copy the security attributes of the keys.<br/> |
| [**SHDeleteEmptyKey**](/windows/win32/Shlwapi/nf-shlwapi-shdeleteemptykeya?branch=master)<br/>           | Deletes an empty key.<br/>                                                                                                                                                    |
| [**SHDeleteKey**](/windows/win32/Shlwapi/nf-shlwapi-shdeletekeya?branch=master)<br/>                     | Deletes a subkey and all its descendants. This function removes the key and all the key's values from the registry.<br/>                                                      |
| [**SHDeleteValue**](/windows/win32/Shlwapi/nf-shlwapi-shdeletevaluea?branch=master)<br/>                 | Deletes a named value from the specified registry key.<br/>                                                                                                                   |
| [**SHEnumKeyEx**](/windows/win32/Shlwapi/nf-shlwapi-shenumkeyexa?branch=master)<br/>                     | Enumerates the subkeys of the specified open registry key.<br/>                                                                                                               |
| [**SHEnumValue**](/windows/win32/Shlwapi/nf-shlwapi-shenumvaluea?branch=master)<br/>                     | Enumerates the values of the specified open registry key.<br/>                                                                                                                |
| [**SHGetAssocKeys**](/windows/win32/Shlwapi/nf-shlwapi-shgetassockeys?branch=master)<br/>               | Retrieves an array of class subkeys associated with an [**IQueryAssociations**](/windows/win32/Shlwapi/?branch=master) object.<br/>                                                          |
| [**SHGetValue**](/windows/win32/Shlwapi/nf-shlwapi-shgetvaluea?branch=master)<br/>                       | Retrieves a registry value.<br/>                                                                                                                                              |
| [**SHOpenRegStream2**](/windows/win32/Shlwapi/nf-shlwapi-shopenregstream2a?branch=master)<br/>           | Opens a registry value and supplies a stream that can be used to read from or write to the value. This function supersedes [**SHOpenRegStream**](/windows/win32/Shlwapi/nf-shlwapi-shopenregstreama?branch=master).<br/>   |
| [**SHQueryInfoKey**](/windows/win32/Shlwapi/nf-shlwapi-shqueryinfokeya?branch=master)<br/>               | Retrieves information about a specified registry key.<br/>                                                                                                                    |
| [**SHQueryValueEx**](/windows/win32/Shlwapi/nf-shlwapi-shqueryvalueexa?branch=master)<br/>               | Opens a registry key and queries it for a specific value.<br/>                                                                                                                |
| [**SHRegCloseUSKey**](/windows/win32/Shlwapi/nf-shlwapi-shregcloseuskey?branch=master)<br/>             | Closes a handle to a user-specific registry subkey in a user-specific subtree (HKEY\_CURRENT\_USER or HKEY\_LOCAL\_MACHINE).<br/>                                             |
| [**SHRegCreateUSKey**](/windows/win32/Shlwapi/nf-shlwapi-shregcreateuskeya?branch=master)<br/>           | Creates or opens a registry subkey in a user-specific subtree (HKEY\_CURRENT\_USER or HKEY\_LOCAL\_MACHINE).<br/>                                                             |
| [**SHRegDeleteEmptyUSKey**](/windows/win32/Shlwapi/nf-shlwapi-shregdeleteemptyuskeya?branch=master)<br/> | Deletes an empty registry subkey in a user-specific subtree (HKEY\_CURRENT\_USER or HKEY\_LOCAL\_MACHINE).<br/>                                                               |
| [**SHRegDeleteUSValue**](/windows/win32/Shlwapi/nf-shlwapi-shregdeleteusvaluea?branch=master)<br/>       | Deletes a registry subkey value in a user-specific subtree (HKEY\_CURRENT\_USER or HKEY\_LOCAL\_MACHINE).<br/>                                                                |
| [**SHRegDuplicateHKey**](/windows/win32/Shlwapi/nf-shlwapi-shregduplicatehkey?branch=master)<br/>       | Duplicates a registry key's HKEY handle.<br/>                                                                                                                                 |
| [**SHRegEnumUSKey**](/windows/win32/Shlwapi/nf-shlwapi-shregenumuskeya?branch=master)<br/>               | Enumerates the subkeys of a registry subkey in a user-specific subtree (HKEY\_CURRENT\_USER or HKEY\_LOCAL\_MACHINE).<br/>                                                    |
| [**SHRegEnumUSValue**](/windows/win32/Shlwapi/nf-shlwapi-shregenumusvaluea?branch=master)<br/>           | Enumerates the values of the specified registry subkey in a user-specific subtree (HKEY\_CURRENT\_USER or HKEY\_LOCAL\_MACHINE).<br/>                                         |
| [**SHRegGetBoolUSValue**](/windows/win32/Shlwapi/nf-shlwapi-shreggetboolusvaluea?branch=master)<br/>     | Retrieves a Boolean value from a registry subkey in a user-specific subtree (HKEY\_CURRENT\_USER or HKEY\_LOCAL\_MACHINE).<br/>                                               |
| [**SHRegGetIntW**](/windows/win32/Shlwapi/nf-shlwapi-shreggetintw?branch=master)<br/>                    | Reads a numeric string value from the registry and converts it to an integer.<br/>                                                                                            |
| [**SHRegGetPath**](/windows/win32/Shlwapi/nf-shlwapi-shreggetpatha?branch=master)<br/>                   | Retrieves a file path from the registry, expanding environment variables as needed.<br/>                                                                                      |
| [**SHRegGetUSValue**](/windows/win32/Shlwapi/nf-shlwapi-shreggetusvaluea?branch=master)<br/>             | Retrieves a value from a registry subkey in a user-specific subtree (HKEY\_CURRENT\_USER or HKEY\_LOCAL\_MACHINE).<br/>                                                       |
| [**SHRegOpenUSKey**](/windows/win32/Shlwapi/nf-shlwapi-shregopenuskeya?branch=master)<br/>               | Opens a registry subkey in a user-specific subtree (HKEY\_CURRENT\_USER or HKEY\_LOCAL\_MACHINE).<br/>                                                                        |
| [**SHRegQueryInfoUSKey**](/windows/win32/Shlwapi/nf-shlwapi-shregqueryinfouskeya?branch=master)<br/>     | Retrieves information about a specified registry subkey in a user-specific subtree (HKEY\_CURRENT\_USER or HKEY\_LOCAL\_MACHINE).<br/>                                        |
| [**SHRegQueryUSValue**](/windows/win32/Shlwapi/nf-shlwapi-shregqueryusvaluea?branch=master)<br/>         | Retrieves the type and data for a specified name associated with an open registry subkey in a user-specific subtree (HKEY\_CURRENT\_USER or HKEY\_LOCAL\_MACHINE).<br/>       |
| [**SHRegSetPath**](/windows/win32/Shlwapi/nf-shlwapi-shregsetpatha?branch=master)<br/>                   | Takes a file path, replaces folder names with environment strings, and places the resulting string in the registry.<br/>                                                      |
| [**SHRegSetUSValue**](/windows/win32/Shlwapi/nf-shlwapi-shregsetusvaluea?branch=master)<br/>             | Sets a registry subkey value in a user-specific subtree (HKEY\_CURRENT\_USER or HKEY\_LOCAL\_MACHINE).<br/>                                                                   |
| [**SHRegSetValue**](/windows/win32/shlwapi/nf-shlwapi-shregsetvalue?branch=master)<br/>                 | Sets a registry value.<br/> Use [**RegSetValue**](base.regsetvalue) in its place.<br/>                                                                                  |
| [**SHRegWriteUSValue**](/windows/win32/Shlwapi/nf-shlwapi-shregwriteusvaluea?branch=master)<br/>         | Writes a value to a registry subkey in a user-specific subtree (HKEY\_CURRENT\_USER or HKEY\_LOCAL\_MACHINE).<br/>                                                            |
| [**SHSetValue**](/windows/win32/Shlwapi/nf-shlwapi-shsetvaluea?branch=master)<br/>                       | Sets the value of a registry key.<br/>                                                                                                                                        |



 

 

 




