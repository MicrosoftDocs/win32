---
Description: 'This section describes the Windows Shell registry handling functions. The programming elements explained in this documentation are exported by Shlwapi.dll and defined in Shlwapi.h and Shlwapi.lib.'
title: Shell Registry Handling Functions
---

# Shell Registry Handling Functions

This section describes the Windows Shell registry handling functions. The programming elements explained in this documentation are exported by Shlwapi.dll and defined in Shlwapi.h and Shlwapi.lib.

## In this section



| Topic                                                             | Description                                                                                                                                                                         |
|-------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AssocCreate**](assoccreate.md)<br/>                     | Returns a pointer to an [**IQueryAssociations**](iqueryassociations.md) object.<br/>                                                                                         |
| [**AssocGetPerceivedType**](assocgetperceivedtype.md)<br/> | Retrieves a file's perceived type based on its extension.<br/>                                                                                                                |
| [**AssocIsDangerous**](associsdangerous.md)<br/>           | Determines whether a file type is considered a potential security risk.<br/>                                                                                                  |
| [**AssocQueryKey**](assocquerykey.md)<br/>                 | Searches for and retrieves a key related to a file or protocol association from the registry.<br/>                                                                            |
| [**AssocQueryString**](assocquerystring.md)<br/>           | Searches for and retrieves a file or protocol association-related string from the registry.<br/>                                                                              |
| [**AssocQueryStringByKey**](assocquerystringbykey.md)<br/> | Searches for and retrieves a file association-related string from the registry starting from a specified key.<br/>                                                            |
| [**SHCopyKey**](shcopykey.md)<br/>                         | Recursively copies the subkeys and values of the source subkey to the destination key. [**SHCopyKey**](shcopykey.md) does not copy the security attributes of the keys.<br/> |
| [**SHDeleteEmptyKey**](shdeleteemptykey.md)<br/>           | Deletes an empty key.<br/>                                                                                                                                                    |
| [**SHDeleteKey**](shdeletekey.md)<br/>                     | Deletes a subkey and all its descendants. This function removes the key and all the key's values from the registry.<br/>                                                      |
| [**SHDeleteValue**](shdeletevalue.md)<br/>                 | Deletes a named value from the specified registry key.<br/>                                                                                                                   |
| [**SHEnumKeyEx**](shenumkeyex.md)<br/>                     | Enumerates the subkeys of the specified open registry key.<br/>                                                                                                               |
| [**SHEnumValue**](shenumvalue.md)<br/>                     | Enumerates the values of the specified open registry key.<br/>                                                                                                                |
| [**SHGetAssocKeys**](shgetassockeys.md)<br/>               | Retrieves an array of class subkeys associated with an [**IQueryAssociations**](iqueryassociations.md) object.<br/>                                                          |
| [**SHGetValue**](shgetvalue.md)<br/>                       | Retrieves a registry value.<br/>                                                                                                                                              |
| [**SHOpenRegStream2**](shopenregstream2.md)<br/>           | Opens a registry value and supplies a stream that can be used to read from or write to the value. This function supersedes [**SHOpenRegStream**](shopenregstream.md).<br/>   |
| [**SHQueryInfoKey**](shqueryinfokey.md)<br/>               | Retrieves information about a specified registry key.<br/>                                                                                                                    |
| [**SHQueryValueEx**](shqueryvalueex.md)<br/>               | Opens a registry key and queries it for a specific value.<br/>                                                                                                                |
| [**SHRegCloseUSKey**](shregcloseuskey.md)<br/>             | Closes a handle to a user-specific registry subkey in a user-specific subtree (HKEY\_CURRENT\_USER or HKEY\_LOCAL\_MACHINE).<br/>                                             |
| [**SHRegCreateUSKey**](shregcreateuskey.md)<br/>           | Creates or opens a registry subkey in a user-specific subtree (HKEY\_CURRENT\_USER or HKEY\_LOCAL\_MACHINE).<br/>                                                             |
| [**SHRegDeleteEmptyUSKey**](shregdeleteemptyuskey.md)<br/> | Deletes an empty registry subkey in a user-specific subtree (HKEY\_CURRENT\_USER or HKEY\_LOCAL\_MACHINE).<br/>                                                               |
| [**SHRegDeleteUSValue**](shregdeleteusvalue.md)<br/>       | Deletes a registry subkey value in a user-specific subtree (HKEY\_CURRENT\_USER or HKEY\_LOCAL\_MACHINE).<br/>                                                                |
| [**SHRegDuplicateHKey**](shregduplicatehkey.md)<br/>       | Duplicates a registry key's HKEY handle.<br/>                                                                                                                                 |
| [**SHRegEnumUSKey**](shregenumuskey.md)<br/>               | Enumerates the subkeys of a registry subkey in a user-specific subtree (HKEY\_CURRENT\_USER or HKEY\_LOCAL\_MACHINE).<br/>                                                    |
| [**SHRegEnumUSValue**](shregenumusvalue.md)<br/>           | Enumerates the values of the specified registry subkey in a user-specific subtree (HKEY\_CURRENT\_USER or HKEY\_LOCAL\_MACHINE).<br/>                                         |
| [**SHRegGetBoolUSValue**](shreggetboolusvalue.md)<br/>     | Retrieves a Boolean value from a registry subkey in a user-specific subtree (HKEY\_CURRENT\_USER or HKEY\_LOCAL\_MACHINE).<br/>                                               |
| [**SHRegGetIntW**](shreggetint.md)<br/>                    | Reads a numeric string value from the registry and converts it to an integer.<br/>                                                                                            |
| [**SHRegGetPath**](shreggetpath.md)<br/>                   | Retrieves a file path from the registry, expanding environment variables as needed.<br/>                                                                                      |
| [**SHRegGetUSValue**](shreggetusvalue.md)<br/>             | Retrieves a value from a registry subkey in a user-specific subtree (HKEY\_CURRENT\_USER or HKEY\_LOCAL\_MACHINE).<br/>                                                       |
| [**SHRegOpenUSKey**](shregopenuskey.md)<br/>               | Opens a registry subkey in a user-specific subtree (HKEY\_CURRENT\_USER or HKEY\_LOCAL\_MACHINE).<br/>                                                                        |
| [**SHRegQueryInfoUSKey**](shregqueryinfouskey.md)<br/>     | Retrieves information about a specified registry subkey in a user-specific subtree (HKEY\_CURRENT\_USER or HKEY\_LOCAL\_MACHINE).<br/>                                        |
| [**SHRegQueryUSValue**](shregqueryusvalue.md)<br/>         | Retrieves the type and data for a specified name associated with an open registry subkey in a user-specific subtree (HKEY\_CURRENT\_USER or HKEY\_LOCAL\_MACHINE).<br/>       |
| [**SHRegSetPath**](shregsetpath.md)<br/>                   | Takes a file path, replaces folder names with environment strings, and places the resulting string in the registry.<br/>                                                      |
| [**SHRegSetUSValue**](shregsetusvalue.md)<br/>             | Sets a registry subkey value in a user-specific subtree (HKEY\_CURRENT\_USER or HKEY\_LOCAL\_MACHINE).<br/>                                                                   |
| [**SHRegSetValue**](shregsetvalue.md)<br/>                 | Sets a registry value.<br/> Use [**RegSetValue**](base.regsetvalue) in its place.<br/>                                                                                  |
| [**SHRegWriteUSValue**](shregwriteusvalue.md)<br/>         | Writes a value to a registry subkey in a user-specific subtree (HKEY\_CURRENT\_USER or HKEY\_LOCAL\_MACHINE).<br/>                                                            |
| [**SHSetValue**](shsetvalue.md)<br/>                       | Sets the value of a registry key.<br/>                                                                                                                                        |



 

 

 




