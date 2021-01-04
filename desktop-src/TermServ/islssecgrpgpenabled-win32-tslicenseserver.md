---
title: IsLSSecGrpGPEnabled method of the Win32_TSLicenseServer class
description: Retrieves whether the \ 0034;license server security group \ 0034; group policy setting is enabled on the Remote Desktop license server.
ms.assetid: 715b619b-f082-4fed-ac4c-70d5e286e37c
ms.tgt_platform: multiple
keywords:
- IsLSSecGrpGPEnabled method Remote Desktop Services
- IsLSSecGrpGPEnabled method Remote Desktop Services , Win32_TSLicenseServer class
- Win32_TSLicenseServer class Remote Desktop Services , IsLSSecGrpGPEnabled method
topic_type:
- apiref
api_name:
- Win32_TSLicenseServer.IsLSSecGrpGPEnabled
api_location:
- TlsWmiProv.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IsLSSecGrpGPEnabled method of the Win32\_TSLicenseServer class

Retrieves whether the "license server security group" group policy setting is enabled on the Remote Desktop license server.

## Syntax


```mof
uint32 IsLSSecGrpGPEnabled(
  [out] boolean Enabled
);
```



## Parameters

<dl> <dt>

*Enabled* \[out\]
</dt> <dd>

Boolean value that indicates whether the "license server security group" policy setting is enabled.

</dd> </dl>

## Return value

If the method succeeds, it returns zero. If the method is unsuccessful, it returns a nonzero value. For a list of error codes, see [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md).

## Remarks

You must be a member of the Administrators group to call this method.

The "license server security group" policy setting allows you to specify the Remote Desktop Session Host (RD Session Host) servers that are permitted to contact the license server to obtain Remote Desktop Services client access licenses (RDS CALs). If the policy setting is enabled on the license server, the server will only respond to RDS CAL requests from RD Session Host servers whose computer accounts are members of the Terminal Server Computers local group on the license server.

The policy setting is located in the following node of the local group policy editor:

Computer Configuration\\Administrative Templates\\Windows Components\\Terminal Services\\TS Licensing

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

 

