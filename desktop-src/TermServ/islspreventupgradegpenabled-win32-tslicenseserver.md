---
title: IsLSPreventUpgradeGPEnabled method of the Win32_TSLicenseServer class
description: Retrieves whether the \ 0034;prevent license upgrade \ 0034; group policy setting is enabled on the Remote Desktop license server.
ms.assetid: f78585b8-a50c-402b-ab20-f405eba0c079
ms.tgt_platform: multiple
keywords:
- IsLSPreventUpgradeGPEnabled method Remote Desktop Services
- IsLSPreventUpgradeGPEnabled method Remote Desktop Services , Win32_TSLicenseServer class
- Win32_TSLicenseServer class Remote Desktop Services , IsLSPreventUpgradeGPEnabled method
topic_type:
- apiref
api_name:
- Win32_TSLicenseServer.IsLSPreventUpgradeGPEnabled
api_location:
- TlsWmiProv.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IsLSPreventUpgradeGPEnabled method of the Win32\_TSLicenseServer class

Retrieves whether the "prevent license upgrade" group policy setting is enabled on the Remote Desktop license server.

## Syntax


```mof
uint32 IsLSPreventUpgradeGPEnabled(
  [out] boolean Enabled
);
```



## Parameters

<dl> <dt>

*Enabled* \[out\]
</dt> <dd>

Boolean value that indicates whether the "prevent license upgrade" policy setting is enabled.

</dd> </dl>

## Return value

If the method succeeds, it returns zero. If the method is unsuccessful, it returns a nonzero value. For a list of error codes, see [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md).

## Remarks

You must be a member of the Administrators group to call this method.

If the "prevent license upgrade" policy setting is enabled, the license server will only issue a temporary RDS CAL to the client if an appropriate RDS CAL for the Remote Desktop Session Host (RD Session Host) server is not available.

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

 

