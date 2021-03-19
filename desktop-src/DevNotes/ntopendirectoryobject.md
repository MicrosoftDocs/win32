---
description: Opens an existing directory object.
ms.assetid: 7313fb32-976b-4c73-b9ba-09fb8ad7faf1
title: NtOpenDirectoryObject function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- NtOpenDirectoryObject
api_type: 
- DllExport
api_location: 
- Ntdll.dll
---

# NtOpenDirectoryObject function

\[This function may be altered or unavailable in the future.\]

Opens an existing directory object.

## Syntax


```C++
NTSTATUS WINAPI NtOpenDirectoryObject(
  _Out_ PHANDLE            DirectoryHandle,
  _In_  ACCESS_MASK        DesiredAccess,
  _In_  POBJECT_ATTRIBUTES ObjectAttributes
);
```



## Parameters

<dl> <dt>

*DirectoryHandle* \[out\]
</dt> <dd>

A handle to the newly opened directory object.

</dd> <dt>

*DesiredAccess* \[in\]
</dt> <dd>

An [**ACCESS\_MASK**](../secauthz/access-mask.md) that specifies the requested access to the directory object. This parameter can be one or more of the following values.



| Value                                                                                                                                                                                                                                                                      | Meaning                                                                     |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| <span id="DIRECTORY_QUERY"></span><span id="directory_query"></span><dl> <dt>**DIRECTORY\_QUERY**</dt> <dt>0x0001</dt> </dl>                                            | Query access to the directory object.<br/>                            |
| <span id="DIRECTORY_TRAVERSE"></span><span id="directory_traverse"></span><dl> <dt>**DIRECTORY\_TRAVERSE**</dt> <dt>0x0002</dt> </dl>                                   | Name-lookup access to the directory object.<br/>                      |
| <span id="DIRECTORY_CREATE_OBJECT"></span><span id="directory_create_object"></span><dl> <dt>**DIRECTORY\_CREATE\_OBJECT**</dt> <dt>0x0004</dt> </dl>                   | Name-creation access to the directory object.<br/>                    |
| <span id="DIRECTORY_CREATE_SUBDIRECTORY"></span><span id="directory_create_subdirectory"></span><dl> <dt>**DIRECTORY\_CREATE\_SUBDIRECTORY**</dt> <dt>0x0008</dt> </dl> | Subdirectory-creation access to the directory object.<br/>            |
| <span id="DIRECTORY_ALL_ACCESS"></span><span id="directory_all_access"></span><dl> <dt>**DIRECTORY\_ALL\_ACCESS**</dt> <dt>STANDARD\_RIGHTS\_REQUIRED \| 0xF</dt> </dl> | All of the preceding rights plus **STANDARD\_RIGHTS\_REQUIRED**.<br/> |



 

</dd> <dt>

*ObjectAttributes* \[in\]
</dt> <dd>

The attributes for the directory object. To initialize the **OBJECT\_ATTRIBUTES** structure, use the **InitializeObjectAttributes** macro. For more information, see the documentation for these items in the documentation for the WDK.

</dd> </dl>

## Return value

The function returns STATUS\_SUCCESS or an error status. The possible status codes include the following.



| Return code                                                                                                       | Description                                                                                                                                                                                                                                                                                               |
|-------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**STATUS\_INSUFFICIENT\_RESOURCES**</dt> </dl>    | A temporary buffer required by this function could not be allocated.<br/>                                                                                                                                                                                                                           |
| <dl> <dt>**STATUS\_INVALID\_PARAMETER**</dt> </dl>         | The specified ObjectAttributes parameter was a **NULL** pointer, not a valid pointer to an **OBJECT\_ATTRIBUTES** structure, or some of the members specified in the **OBJECT\_ATTRIBUTES** structure were not valid.<br/>                                                                          |
| <dl> <dt>**STATUS\_OBJECT\_NAME\_INVALID**</dt> </dl>      | The *ObjectAttributes* parameter contained an **ObjectName** member in the **OBJECT\_ATTRIBUTES** structure that was not valid because an empty string was found after the **OBJECT\_NAME\_PATH\_SEPARATOR** character.<br/>                                                                        |
| <dl> <dt>**STATUS\_OBJECT\_NAME\_NOT\_FOUND**</dt> </dl>   | The *ObjectAttributes* parameter contained an **ObjectName** member in the **OBJECT\_ATTRIBUTES** structure that could not be found.<br/>                                                                                                                                                           |
| <dl> <dt>**STATUS\_OBJECT\_PATH\_NOT\_FOUND**</dt> </dl>   | The *ObjectAttributes* parameter contained an **ObjectName** member in the **OBJECT\_ATTRIBUTES** structure with an object path that could not be found. <br/>                                                                                                                                      |
| <dl> <dt>**STATUS\_OBJECT\_PATH\_SYNTAX\_BAD** </dt> </dl> | The *ObjectAttributes* parameter did not contain a **RootDirectory** member, but the **ObjectName** member in the **OBJECT\_ATTRIBUTES** structure was an empty string or did not contain an **OBJECT\_NAME\_PATH\_SEPARATOR** character. This indicates incorrect syntax for the object path.<br/> |



 

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions.

## Requirements



| Requirement | Value |
|----------------|--------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Ntdll.dll</dt> </dl> |



## See also

<dl> <dt>

[**NtQueryDirectoryObject**](ntquerydirectoryobject.md)
</dt> </dl>

 

 
