---
description: This section describes the Windows Shell registry handling functions. The programming elements explained in this documentation are exported by Shlwapi.dll and defined in Shlwapi.h and Shlwapi.lib.
title: Shell Registry Handling Functions
ms.topic: article
ms.date: 05/31/2018
ms.assetid: 12182f56-5bb3-4f70-ae6a-2ef7366287b9
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# Shell Registry Handling Functions

This section describes the Windows Shell registry handling functions. The programming elements explained in this documentation are exported by Shlwapi.dll and defined in Shlwapi.h and Shlwapi.lib.

## In this section



| Topic                                                             | Description                                                                                                                                                                         |
|-------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AssocCreate**](/windows/desktop/api/Shlwapi/nf-shlwapi-assoccreate)<br/>                     | Returns a pointer to an [**IQueryAssociations**](/windows/win32/api/shlwapi/nn-shlwapi-iqueryassociations) object.<br/>                                                                                         |
| [**AssocGetPerceivedType**](/windows/desktop/api/Shlwapi/nf-shlwapi-assocgetperceivedtype)<br/> | Retrieves a file's perceived type based on its extension.<br/>                                                                                                                |
| [**AssocIsDangerous**](/windows/desktop/api/Shlwapi/nf-shlwapi-associsdangerous)<br/>           | Determines whether a file type is considered a potential security risk.<br/>                                                                                                  |
| [**AssocQueryKey**](/windows/desktop/api/Shlwapi/nf-shlwapi-assocquerykeya)<br/>                 | Searches for and retrieves a key related to a file or protocol association from the registry.<br/>                                                                            |
| [**AssocQueryString**](/windows/desktop/api/Shlwapi/nf-shlwapi-assocquerystringa)<br/>           | Searches for and retrieves a file or protocol association-related string from the registry.<br/>                                                                              |
| [**AssocQueryStringByKey**](/windows/desktop/api/Shlwapi/nf-shlwapi-assocquerystringbykeya)<br/> | Searches for and retrieves a file association-related string from the registry starting from a specified key.<br/>                                                            |
| [**SHCopyKey**](/windows/desktop/api/Shlwapi/nf-shlwapi-shcopykeya)<br/>                         | Recursively copies the subkeys and values of the source subkey to the destination key. [**SHCopyKey**](/windows/desktop/api/Shlwapi/nf-shlwapi-shcopykeya) does not copy the security attributes of the keys.<br/> |
| [**SHDeleteEmptyKey**](/windows/desktop/api/Shlwapi/nf-shlwapi-shdeleteemptykeya)<br/>           | Deletes an empty key.<br/>                                                                                                                                                    |
| [**SHDeleteKey**](/windows/desktop/api/Shlwapi/nf-shlwapi-shdeletekeya)<br/>                     | Deletes a subkey and all its descendants. This function removes the key and all the key's values from the registry.<br/>                                                      |
| [**SHDeleteValue**](/windows/desktop/api/Shlwapi/nf-shlwapi-shdeletevaluea)<br/>                 | Deletes a named value from the specified registry key.<br/>                                                                                                                   |
| [**SHEnumKeyEx**](/windows/desktop/api/Shlwapi/nf-shlwapi-shenumkeyexa)<br/>                     | Enumerates the subkeys of the specified open registry key.<br/>                                                                                                               |
| [**SHEnumValue**](/windows/desktop/api/Shlwapi/nf-shlwapi-shenumvaluea)<br/>                     | Enumerates the values of the specified open registry key.<br/>                                                                                                                |
| [**SHGetAssocKeys**](/windows/desktop/api/Shlwapi/nf-shlwapi-shgetassockeys)<br/>               | Retrieves an array of class subkeys associated with an [**IQueryAssociations**](/windows/win32/api/shlwapi/nn-shlwapi-iqueryassociations) object.<br/>                                                          |
| [**SHGetValue**](/windows/desktop/api/Shlwapi/nf-shlwapi-shgetvaluea)<br/>                       | Retrieves a registry value.<br/>                                                                                                                                              |
| [**SHOpenRegStream2**](/windows/desktop/api/Shlwapi/nf-shlwapi-shopenregstream2a)<br/>           | Opens a registry value and supplies a stream that can be used to read from or write to the value. This function supersedes [**SHOpenRegStream**](/windows/desktop/api/Shlwapi/nf-shlwapi-shopenregstreama).<br/>   |
| [**SHQueryInfoKey**](/windows/desktop/api/Shlwapi/nf-shlwapi-shqueryinfokeya)<br/>               | Retrieves information about a specified registry key.<br/>                                                                                                                    |
| [**SHQueryValueEx**](/windows/desktop/api/Shlwapi/nf-shlwapi-shqueryvalueexa)<br/>               | Opens a registry key and queries it for a specific value.<br/>                                                                                                                |
| [**SHRegCloseUSKey**](/windows/desktop/api/Shlwapi/nf-shlwapi-shregcloseuskey)<br/>             | Closes a handle to a user-specific registry subkey in a user-specific subtree (HKEY\_CURRENT\_USER or HKEY\_LOCAL\_MACHINE).<br/>                                             |
| [**SHRegCreateUSKey**](/windows/desktop/api/Shlwapi/nf-shlwapi-shregcreateuskeya)<br/>           | Creates or opens a registry subkey in a user-specific subtree (HKEY\_CURRENT\_USER or HKEY\_LOCAL\_MACHINE).<br/>                                                             |
| [**SHRegDeleteEmptyUSKey**](/windows/desktop/api/Shlwapi/nf-shlwapi-shregdeleteemptyuskeya)<br/> | Deletes an empty registry subkey in a user-specific subtree (HKEY\_CURRENT\_USER or HKEY\_LOCAL\_MACHINE).<br/>                                                               |
| [**SHRegDeleteUSValue**](/windows/desktop/api/Shlwapi/nf-shlwapi-shregdeleteusvaluea)<br/>       | Deletes a registry subkey value in a user-specific subtree (HKEY\_CURRENT\_USER or HKEY\_LOCAL\_MACHINE).<br/>                                                                |
| [**SHRegDuplicateHKey**](/windows/desktop/api/Shlwapi/nf-shlwapi-shregduplicatehkey)<br/>       | Duplicates a registry key's HKEY handle.<br/>                                                                                                                                 |
| [**SHRegEnumUSKey**](/windows/desktop/api/Shlwapi/nf-shlwapi-shregenumuskeya)<br/>               | Enumerates the subkeys of a registry subkey in a user-specific subtree (HKEY\_CURRENT\_USER or HKEY\_LOCAL\_MACHINE).<br/>                                                    |
| [**SHRegEnumUSValue**](/windows/desktop/api/Shlwapi/nf-shlwapi-shregenumusvaluea)<br/>           | Enumerates the values of the specified registry subkey in a user-specific subtree (HKEY\_CURRENT\_USER or HKEY\_LOCAL\_MACHINE).<br/>                                         |
| [**SHRegGetBoolUSValue**](/windows/desktop/api/Shlwapi/nf-shlwapi-shreggetboolusvaluea)<br/>     | Retrieves a Boolean value from a registry subkey in a user-specific subtree (HKEY\_CURRENT\_USER or HKEY\_LOCAL\_MACHINE).<br/>                                               |
| [**SHRegGetIntW**](/windows/desktop/api/Shlwapi/nf-shlwapi-shreggetintw)<br/>                    | Reads a numeric string value from the registry and converts it to an integer.<br/>                                                                                            |
| [**SHRegGetPath**](/windows/desktop/api/Shlwapi/nf-shlwapi-shreggetpatha)<br/>                   | Retrieves a file path from the registry, expanding environment variables as needed.<br/>                                                                                      |
| [**SHRegGetUSValue**](/windows/desktop/api/Shlwapi/nf-shlwapi-shreggetusvaluea)<br/>             | Retrieves a value from a registry subkey in a user-specific subtree (HKEY\_CURRENT\_USER or HKEY\_LOCAL\_MACHINE).<br/>                                                       |
| [**SHRegOpenUSKey**](/windows/desktop/api/Shlwapi/nf-shlwapi-shregopenuskeya)<br/>               | Opens a registry subkey in a user-specific subtree (HKEY\_CURRENT\_USER or HKEY\_LOCAL\_MACHINE).<br/>                                                                        |
| [**SHRegQueryInfoUSKey**](/windows/desktop/api/Shlwapi/nf-shlwapi-shregqueryinfouskeya)<br/>     | Retrieves information about a specified registry subkey in a user-specific subtree (HKEY\_CURRENT\_USER or HKEY\_LOCAL\_MACHINE).<br/>                                        |
| [**SHRegQueryUSValue**](/windows/desktop/api/Shlwapi/nf-shlwapi-shregqueryusvaluea)<br/>         | Retrieves the type and data for a specified name associated with an open registry subkey in a user-specific subtree (HKEY\_CURRENT\_USER or HKEY\_LOCAL\_MACHINE).<br/>       |
| [**SHRegSetPath**](/windows/desktop/api/Shlwapi/nf-shlwapi-shregsetpatha)<br/>                   | Takes a file path, replaces folder names with environment strings, and places the resulting string in the registry.<br/>                                                      |
| [**SHRegSetUSValue**](/windows/desktop/api/Shlwapi/nf-shlwapi-shregsetusvaluea)<br/>             | Sets a registry subkey value in a user-specific subtree (HKEY\_CURRENT\_USER or HKEY\_LOCAL\_MACHINE).<br/>                                                                   |
| [**SHRegSetValue**](/windows/desktop/api/shlwapi/nf-shlwapi-shregsetvalue)<br/>                 | Sets a registry value.<br/> Use [**RegSetValue**](/windows/win32/api/winreg/nf-winreg-regsetvaluea) in its place.<br/>                                                                                  |
| [**SHRegWriteUSValue**](/windows/desktop/api/Shlwapi/nf-shlwapi-shregwriteusvaluea)<br/>         | Writes a value to a registry subkey in a user-specific subtree (HKEY\_CURRENT\_USER or HKEY\_LOCAL\_MACHINE).<br/>                                                            |
| [**SHSetValue**](/windows/desktop/api/Shlwapi/nf-shlwapi-shsetvaluea)<br/>                       | Sets the value of a registry key.<br/>                                                                                                                                        |



 

 

 
