---
title: IsLSinTSLSGroup method of the Win32_TSLicenseServer class
description: Retrieves whether the Remote Desktop license server is a member of the Remote Desktop license server group on a domain controller in a given domain.
ms.assetid: a6ad7f09-8972-47d4-8b3b-cd129b400ea8
ms.tgt_platform: multiple
keywords:
- IsLSinTSLSGroup method Remote Desktop Services
- IsLSinTSLSGroup method Remote Desktop Services , Win32_TSLicenseServer class
- Win32_TSLicenseServer class Remote Desktop Services , IsLSinTSLSGroup method
topic_type:
- apiref
api_name:
- Win32_TSLicenseServer.IsLSinTSLSGroup
api_location:
- TlsWmiProv.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IsLSinTSLSGroup method of the Win32\_TSLicenseServer class

Retrieves whether the Remote Desktop license server is a member of the Remote Desktop license server group on a domain controller in a given domain.

## Syntax


```mof
uint32 IsLSinTSLSGroup(
  [in]  string  Domain,
  [out] boolean IsMember
);
```



## Parameters

<dl> <dt>

*Domain* \[in\]
</dt> <dd>

The domain name.

</dd> <dt>

*IsMember* \[out\]
</dt> <dd>

Boolean value that indicates whether the license server is a member of the Remote Desktop license server group in the domain.

</dd> </dl>

## Return value

If the method succeeds, it returns zero. If the method is unsuccessful, it returns a nonzero value. For a list of error codes, see [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md).

## Remarks

You must be a member of the Administrators group to call this method.

If no domain name is provided, a domain controller in the same domain as the license server is queried.

The license server should be a member of the Remote Desktop license server group if the server is configured to use the domain or forest discovery scope. If the license server is not a member of this group, per-user license tracking and reporting will not work.

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
</dt> <dt>

[**AddLStoTSLSGroup**](addlstotslsgroup-win32-tslicenseserver.md)
</dt> <dt>

[**RemoveLSfromTSLSGroup**](removelsfromtslsgroup-win32-tslicenseserver.md)
</dt> </dl>

 

