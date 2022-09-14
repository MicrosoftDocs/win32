---
description: Creates a user certificate for use with NetMeeting conferencing.
ms.assetid: 22acdcbe-c9c9-4f1b-a62d-44a35e101eec
title: NmMakeCert function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- NmMakeCert
api_type: 
- DllExport
api_location: 
- Nmmkcert.dll
---

# NmMakeCert function

Creates a user certificate for use with NetMeeting conferencing.

## Syntax


```C++
void NmMakeCert(
   LPCSTR szFirstName,
   LPCSTR szLastName,
   LPCSTR szEmailName,
   LPCSTR szCity,
   LPCSTR szCountry,
   DWORD  dwFlags
);
```



## Parameters

<dl> <dt>

*szFirstName* 
</dt> <dd>

The user's first name.

</dd> <dt>

*szLastName* 
</dt> <dd>

The user's last name.

</dd> <dt>

*szEmailName* 
</dt> <dd>

The user's email name.

</dd> <dt>

*szCity* 
</dt> <dd>

The user's city.

</dd> <dt>

*szCountry* 
</dt> <dd>

The user's country/region.

</dd> <dt>

*dwFlags* 
</dt> <dd>

A value that indicates how the certificate should be created. Values can be any of the following.



| Value                                                                                                                                                                                                                                                            | Meaning                                                                       |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| <span id="NMMKCERT_F_CLEANUP_ONLY"></span><span id="nmmkcert_f_cleanup_only"></span><dl> <dt>**NMMKCERT\_F\_CLEANUP\_ONLY**</dt> <dt>0x00000004</dt> </dl>    | Delete the old certificate without creating a new one. <br/>            |
| <span id="NMMKCERT_F_DELETEOLDCERT"></span><span id="nmmkcert_f_deleteoldcert"></span><dl> <dt>**NMMKCERT\_F\_DELETEOLDCERT**</dt> <dt>0x00000001</dt> </dl>  | Delete the old certificate previously created with this function. <br/> |
| <span id="NMMKCERT_F_LOCAL_MACHINE"></span><span id="nmmkcert_f_local_machine"></span><dl> <dt>**NMMKCERT\_F\_LOCAL\_MACHINE**</dt> <dt>0x00000002</dt> </dl> | Create the certificate in the local machine certificate store. <br/>    |



 

</dd> </dl>

## Return value

Returns 1 if the function succeeds and –1 if the function fails.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions.

## Requirements



| Requirement | Value |
|----------------|-----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Nmmkcert.dll</dt> </dl> |



 

 
