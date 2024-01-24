---
title: RegisterLSToSCP method of the Win32_TSLicenseServer class
description: Registers the Remote Desktop license server as a service connection point in Active Directory Domain Services.
ms.assetid: F0519C8C-49A9-40B1-88DB-FD0419469E62
ms.tgt_platform: multiple
keywords:
- RegisterLSToSCP method Remote Desktop Services
- RegisterLSToSCP method Remote Desktop Services , Win32_TSLicenseServer class
- Win32_TSLicenseServer class Remote Desktop Services , RegisterLSToSCP method
topic_type:
- apiref
api_name:
- Win32_TSLicenseServer.RegisterLSToSCP
api_location:
- TlsWmiProv.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# RegisterLSToSCP method of the Win32\_TSLicenseServer class

Registers the Remote Desktop license server as a service connection point in Active Directory Domain Services.

## Syntax


```mof
uint32 RegisterLSToSCP();
```



## Parameters

This method has no parameters.

## Return value

If the method succeeds, it returns zero. If the method is unsuccessful, it returns a nonzero value. For a list of error codes, see [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md).

## Remarks

You must be a member of the Administrators group to call this method.

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Microsoft Windows Software Development Kit (SDK). They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](/windows/desktop/WmiSdk/managed-object-format--mof-).

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                         |
| Namespace<br/>                | Root\\CIMv2<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>TlsWmiProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>TlsWmiProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_TSLicenseServer**](win32-tslicenseserver.md)
</dt> </dl>

 

