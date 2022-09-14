---
title: DsIsNTDSOnline function (Ntdsbcli.h)
description: Determines if Active Directory Domain Services are online on the specified server.
ms.assetid: 8f46e4d8-6d05-402c-a5b4-291fd2d6609b
ms.tgt_platform: multiple
keywords:
- DsIsNTDSOnline function Active Directory
topic_type:
- apiref
api_name:
- DsIsNTDSOnline
- DsIsNTDSOnlineA
- DsIsNTDSOnlineW
api_location:
- Ntdsbcli.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# DsIsNTDSOnline function

\[This function is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Beginning with Windows Vista, use [Volume Shadow Copy Service (VSS)](../vss/volume-shadow-copy-service-overview.md) instead.\]

The **DsIsNTDSOnline** function determines if Active Directory Domain Services are online on the specified server.

## Syntax


```C++
HRESULT DsIsNTDSOnline(
  _In_  LPCTSTR szServerName,
  _Out_ BOOL    *pfNTDSOnline
);
```



## Parameters

<dl> <dt>

*szServerName* \[in\]
</dt> <dd>

Pointer to a null-terminated string that contains the name of the server to test. Preceding backslashes are optional. The server must be the same computer that this function is called from. The server name cannot contain any underscore (\_) characters. An example of a server name is "\\\\server1".

</dd> <dt>

*pfNTDSOnline* \[out\]
</dt> <dd>

Pointer to **BOOL** value that receives the result. Receives **TRUE** if the directory service is online or **FALSE** if the directory service is offline.

</dd> </dl>

## Return value

Returns **S\_OK** if the function is successful or an error code otherwise. The following list lists possible error codes.

<dl> <dt>

**ERROR\_ACCESS\_DENIED**
</dt> <dd>

The caller does not have the proper access privileges to call this function. The [**DsSetAuthIdentity**](dssetauthidentity.md) function can be used to set the credentials to use for the backup and restore functions.

</dd> <dt>

**hrCouldNotConnect**
</dt> <dd>

The server in *szServerName* cannot be found, is not a domain controller, or *szServerName* is not formatted correctly. This value is defined in Ntdsbmsg.h.

</dd> <dt>

**RPC\_S\_INVALID\_BINDING**
</dt> <dd>

The [**DsIsNTDSOnline**](dsisntdsonline.md) function is being called remotely or the server in *szServerName* is not a domain controller.

</dd> </dl>

## Remarks

Call this function before calling any of the directory backup or restore functions. The directory must be online in order to perform a backup. The directory must by offline to perform a restore.

This function can only be called from a domain controller that is also the target server specified in *szServerName*. This function cannot be called remotely.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Ntdsbcli.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Ntdsbcli.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Ntdsbcli.dll</dt> </dl> |
| Unicode and ANSI names<br/>   | **DsIsNTDSOnlineW** (Unicode) and **DsIsNTDSOnlineA** (ANSI)<br/>                 |



## See also

<dl> <dt>

[**DsSetAuthIdentity**](dssetauthidentity.md)
</dt> <dt>

[Directory Backup Functions](directory-backup-functions.md)
</dt> <dt>

[Backing Up and Restoring an Active Directory Server](backing-up-and-restoring-an-active-directory-server.md)
</dt> </dl>

 

