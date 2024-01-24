---
title: DsSetAuthIdentity function (Ntdsbcli.h)
description: Sets the security context under which the directory backup APIs are called.
ms.assetid: bfa2f847-6fe3-4f9b-bafa-acf6a7c861d9
ms.tgt_platform: multiple
keywords:
- DsSetAuthIdentity function Active Directory
topic_type:
- apiref
api_name:
- DsSetAuthIdentity
- DsSetAuthIdentityA
- DsSetAuthIdentityW
api_location:
- Ntdsbcli.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# DsSetAuthIdentity function

\[This function is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Beginning with Windows Vista, use [Volume Shadow Copy Service (VSS)](../vss/volume-shadow-copy-service-overview.md) instead.\]

The **DsSetAuthIdentity** function sets the security context under which the directory backup APIs are called.

## Syntax


```C++
HRESULT DsSetAuthIdentity(
  _In_ LPCTSTR szUserName,
  _In_ LPCTSTR szDomainName,
  _In_ LPCTSTR szPassword
);
```



## Parameters

<dl> <dt>

*szUserName* \[in\]
</dt> <dd>

The null-terminated string that specifies the user name.

</dd> <dt>

*szDomainName* \[in\]
</dt> <dd>

The null-terminated string that specifies the name of the domain that the user belongs to.

</dd> <dt>

*szPassword* \[in\]
</dt> <dd>

The null-terminated string that specifies the password of the user in the specified domain.

</dd> </dl>

## Return value

If successful, returns a standard **HRESULT** success codes; otherwise, a failure code is returned.

## Remarks

If **DsSetAuthIdentity** is not called, security context of the current process is assumed.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Ntdsbcli.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Ntdsbcli.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Ntdsbcli.dll</dt> </dl> |
| Unicode and ANSI names<br/>   | **DsSetAuthIdentityW** (Unicode) and **DsSetAuthIdentityA** (ANSI)<br/>           |



## See also

<dl> <dt>

[Backing Up and Restoring an Active Directory Server](backing-up-and-restoring-an-active-directory-server.md)
</dt> <dt>

[Directory Backup Functions](directory-backup-functions.md)
</dt> </dl>

 

