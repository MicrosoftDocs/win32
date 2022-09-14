---
description: Writes the specified offline registry hive to a file.
ms.assetid: 26f2eed9-e6e0-4dc0-8b91-212cde072744
title: ORSaveHive function (Offreg.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ORSaveHive
api_type: 
- DllExport
api_location: 
- Offreg.dll
---

# ORSaveHive function

Writes the specified offline registry hive to a file.

## Syntax


```C++
DWORD ORSaveHive(
  _In_ ORHKEY Handle,
  _In_ PCWSTR lpHivePath,
  _In_ DWORD  dwOsMajorVersion,
  _In_ DWORD  dwOsMinorVersion
);
```



## Parameters

<dl> <dt>

*Handle* \[in\]
</dt> <dd>

A handle to the offline registry hive to save.

</dd> <dt>

*lpHivePath* \[in\]
</dt> <dd>

A pointer to a Unicode string that specifies the name of the registry hive file. This cannot be the name of an existing file.

</dd> <dt>

*dwOsMajorVersion* \[in\]
</dt> <dd>

The major version number of the operating system. This member can be one of the following values.



| Value                                                                        | Meaning                                                                                                                                                                                                                        |
|------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>5</dt> </dl> | If *dwOsMinorVersion* is 1, the operating system is Windows XP.<br/> If *dwOsMinorVersion* is 2, the operating system is Windows Server 2003 R2, Windows Server 2003, or Windows XP Professional x64 Edition.<br/> |
| <dl> <dt>6</dt> </dl> | If *dwOsMinorVersion* is 0, the operating system is Windows Server 2008 or Windows Vista.<br/> If *dwOsMinorVersion* is 1, the operating system is Windows Server 2008 R2 or Windows 7.<br/>                       |



 

</dd> <dt>

*dwOsMinorVersion* \[in\]
</dt> <dd>

The minor version number of the operating system. This member can be one of the following values.



| Value                                                                        | Meaning                                                                                                                                                                                                                                       |
|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>0</dt> </dl> | If *dwOsMajorVersion* is 6, the operating system is Windows Server 2008 or Windows Vista.<br/>                                                                                                                                          |
| <dl> <dt>1</dt> </dl> | If *dwOsMajorVersion* is 5, the operating system is Windows XP.<br/> If *dwOsMajorVersion* is 6, the operating system is Windows Server 2008 R2 or Windows 7.<br/>                                                                |
| <dl> <dt>2</dt> </dl> | If *dwOsMajorVersion* is 5, the operating system is Windows Server 2003 R2, Windows Server 2003, or Windows XP Professional x64 Edition. <br/> If *dwOsMajorVersion* is 6, the *dwOsMinorVersion* parameter must be 0 or 1. <br/> |



 

</dd> </dl>

## Return value

If the function succeeds, the return value is ERROR\_SUCCESS.

If the function fails, the return value is a nonzero error code defined in Winerror.h. You can use the [FormatMessage](/windows/win32/api/winbase/nf-winbase-formatmessage) function with the FORMAT\_MESSAGE\_FROM\_SYSTEM flag to get a generic description of the error. Possible error codes include the following:

-   If the caller does not have the necessary access rights to write the file, the function returns ERROR\_ACCESS\_DENIED.
-   If the specified file already exists, the function returns ERROR\_ALREADY\_EXISTS.

## Remarks

The **ORSaveHive** function must be used to save changes made to an offline registry hive. Changes are not preserved until **ORSaveHive** is called to save the hive to a file.

The *dwOsMajorVersion* and *dwOsMinorVersion* parameters together specify the target format of the registry hive file. The following table summarizes the most recent operating system version numbers.



| Operating system                    | Version number |
|-------------------------------------|----------------|
| Windows Server 2008 R2              | 6.1            |
| Windows 7                           | 6.1            |
| Windows Server 2008                 | 6.0            |
| Windows Vista                       | 6.0            |
| Windows Server 2003 R2              | 5.2            |
| Windows Server 2003                 | 5.2            |
| Windows XP Professional x64 Edition | 5.2            |
| Windows XP                          | 5.1            |



 

Use the [GetVersionEx](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getversionexa) function to retrieve information about the current operating system.

The **ORSaveHive** function locks the registry hive while it is writing the hive to the file, then closes the file and releases the lock. The registry hive remains in memory until it is closed by calling the [**ORCloseHive**](orclosehive.md) function. It is possible to make further changes to the registry hive while it is open; however, to preserve these changes the hive must be saved to a new file, because the **ORSaveHive** function will not overwrite an existing file.

The **ORSaveHive** function can be used to save part of the offline registry hive. The key specified in the *Handle* parameter becomes the root key of a hive that consists of the specified key and all of its subkeys.

## Requirements



| Requirement | Value |
|----------------------------|---------------------------------------------------------------------------------------|
| Redistributable<br/> | Windows Offline Registry library version 1.0 or later<br/>                      |
| Header<br/>          | <dl> <dt>Offreg.h</dt> </dl>   |
| DLL<br/>             | <dl> <dt>Offreg.dll</dt> </dl> |



## See also

<dl> <dt>

[GetVersionEx](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getversionexa)
</dt> <dt>

[**ORCloseHive**](orclosehive.md)
</dt> <dt>

[**OROpenHive**](oropenhive.md)
</dt> </dl>

 

 
