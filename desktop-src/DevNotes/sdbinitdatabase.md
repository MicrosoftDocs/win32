---
description: Opens the shim database.
ms.assetid: ece1bd39-20a1-42e6-8e2b-1d38f7223d42
title: SdbInitDatabase function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SdbInitDatabase
api_type: 
- DllExport
api_location: 
- Apphelp.dll
---

# SdbInitDatabase function

Opens the shim database.

## Syntax


```C++
HSDB WINAPI SdbInitDatabase(
  _In_ DWORD   dwFlags,
  _In_ LPCTSTR pszDatabasePath
);
```



## Parameters

<dl> <dt>

*dwFlags* \[in\]
</dt> <dd>

This parameter specifies the format of the path in the *pszDatabasePath* parameter. It can be one of the following values.



| Value                                                                                                                                                                                                                                                      | Meaning                                                                                                |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| <span id="HID_DOS_PATHS"></span><span id="hid_dos_paths"></span><dl> <dt>**HID\_DOS\_PATHS**</dt> <dt>0x00000001</dt> </dl>                             | An MS-DOS style path.<br/>                                                                       |
| <span id="HID_DATABASE_FULLPATH"></span><span id="hid_database_fullpath"></span><dl> <dt>**HID\_DATABASE\_FULLPATH**</dt> <dt>0x00000002</dt> </dl>     | A full path.<br/>                                                                                |
| <span id="HID_NO_DATABASE"></span><span id="hid_no_database"></span><dl> <dt>**HID\_NO\_DATABASE**</dt> <dt>0x00000004</dt> </dl>                       | The *pszDatabasePath* parameter is ignored and no database is opened.<br/>                       |
| <span id="HID_DATABASE_TYPE_MASK"></span><span id="hid_database_type_mask"></span><dl> <dt>**HID\_DATABASE\_TYPE\_MASK**</dt> <dt>0xF00F0000</dt> </dl> | This parameter specifies a predefined database. The *pszDatabasePath* parameter is ignored.<br/> |



 

If *dwFlags* contains **HID\_DATA\_TYPE\_MASK**, this parameter can also include one of the following values.



| Value                                                                                                                                                                                                                                                               | Meaning                                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| <span id="SDB_DATABASE_MAIN_SHIM"></span><span id="sdb_database_main_shim"></span><dl> <dt>**SDB\_DATABASE\_MAIN\_SHIM**</dt> <dt>0x80030000</dt> </dl>          | Application shim database.<br/>         |
| <span id="SDB_DATABASE_MAIN_MSI"></span><span id="sdb_database_main_msi"></span><dl> <dt>**SDB\_DATABASE\_MAIN\_MSI**</dt> <dt>0x80020000</dt> </dl>             | MSI database.<br/>                      |
| <span id="SDB_DATABASE_MAIN_DRIVERS"></span><span id="sdb_database_main_drivers"></span><dl> <dt>**SDB\_DATABASE\_MAIN\_DRIVERS**</dt> <dt>0x80040000</dt> </dl> | Database of drivers to be blocked.<br/> |



 

</dd> <dt>

*pszDatabasePath* \[in\]
</dt> <dd>

The path to the database. This parameter can be **NULL** if the *dwFlags* parameter specifies a predefined database.

</dd> </dl>

## Return value

The function returns a handle to the opened database.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>Apphelp.dll</dt> </dl> |



## See also

<dl> <dt>

[**SdbGetAppPatchDir**](sdbgetapppatchdir.md)
</dt> <dt>

[**SdbGetMatchingExe**](sdbgetmatchingexe.md)
</dt> <dt>

[**SdbReleaseMatchingExe**](sdbreleasematchingexe.md)
</dt> <dt>

[**SdbTagRefToTagID**](sdbtagreftotagid.md)
</dt> </dl>

 

 




