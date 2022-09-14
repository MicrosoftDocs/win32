---
title: ChangeRole method of the Win32_TSLicenseServer class
description: Changes the discovery scope of the Remote Desktop license server. The discovery scope determines which Remote Desktop Session Host (RD Session Host) servers on the network can automatically discover the license server.
ms.assetid: 3d98fd8a-4ade-489f-8edd-5df1227f15cd
ms.tgt_platform: multiple
keywords:
- ChangeRole method Remote Desktop Services
- ChangeRole method Remote Desktop Services , Win32_TSLicenseServer class
- Win32_TSLicenseServer class Remote Desktop Services , ChangeRole method
topic_type:
- apiref
api_name:
- Win32_TSLicenseServer.ChangeRole
api_location:
- TlsWmiProv.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ChangeRole method of the Win32\_TSLicenseServer class

Changes the discovery scope of the Remote Desktop license server. The discovery scope determines which Remote Desktop Session Host (RD Session Host) servers on the network can automatically discover the license server.

## Syntax


```mof
uint32 ChangeRole(
  [in] uint32 ServerRole
);
```



## Parameters

<dl> <dt>

*ServerRole* \[in\]
</dt> <dd>

Discovery scope for the Remote Desktop license server. You can set one of the following values.

<dt>

0
</dt> <dd>

RD Session Host servers in the same workgroup can discover the license server.

</dd> <dt>

1
</dt> <dd>

RD Session Host servers in the same domain can discover the license server. You must be logged on as a domain administrator to set this value.

</dd> <dt>

2
</dt> <dd>

RD Session Host servers from multiple domains in the same forest can discover the license server. You must be logged on as an enterprise administrator to set this value.

</dd> </dl> </dd> </dl>

## Return value

If the method succeeds, it returns zero. If the method is unsuccessful, it returns a nonzero value. For a list of error codes, see [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md).

## Remarks

You must be a member of the Administrators group to call this method.

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Microsoft Windows Software Development Kit (SDK). They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](/windows/desktop/WmiSdk/managed-object-format--mof-).

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                            |
| Namespace<br/>                | Root\\CIMv2<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>TlsWmiProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>TlsWmiProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_TSLicenseServer**](win32-tslicenseserver.md)
</dt> </dl>

 

