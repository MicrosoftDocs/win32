---
title: AddLStoTSLSGroup method of the Win32_TSLicenseServer class
description: Adds the Remote Desktop license server to the Remote Desktop Connection Broker (RD Connection Broker) License Servers group on a domain controller in the same domain as the Remote Desktop license server.
ms.assetid: 65c6b7cf-324a-44f1-8dfc-40e35ed45d4f
ms.tgt_platform: multiple
keywords:
- AddLStoTSLSGroup method Remote Desktop Services
- AddLStoTSLSGroup method Remote Desktop Services , Win32_TSLicenseServer class
- Win32_TSLicenseServer class Remote Desktop Services , AddLStoTSLSGroup method
topic_type:
- apiref
api_name:
- Win32_TSLicenseServer.AddLStoTSLSGroup
api_location:
- TlsWmiProv.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# AddLStoTSLSGroup method of the Win32\_TSLicenseServer class

Adds the Remote Desktop license server to the Remote Desktop Connection Broker (RD Connection Broker) License Servers group on a domain controller in the same domain as the Remote Desktop license server.

## Syntax


```mof
uint32 AddLStoTSLSGroup();
```



## Parameters

This method has no parameters.

## Return value

If the method succeeds, it returns zero. If the method is unsuccessful, it returns a nonzero value. For a list of error codes, see [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md).

## Remarks

You must be a member of the Domain Admins group to call this method.

The license server should be a member of the Remote Desktop license servers group if the server is configured to use the domain or forest discovery scope.

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

[**IsLSinTSLSGroup**](islsintslsgroup-win32-tslicenseserver.md)
</dt> </dl>

 

