---
title: SetDeviceRedirectionType method of the Win32_TSGatewayConnectionAuthorizationPolicy class
description: Sets the DeviceRedirectionType property, which controls which devices will be redirected.
ms.assetid: d97a0a7d-a08e-4703-b0f0-ba5d20688dc8
ms.tgt_platform: multiple
keywords:
- SetDeviceRedirectionType method Remote Desktop Services
- SetDeviceRedirectionType method Remote Desktop Services , Win32_TSGatewayConnectionAuthorizationPolicy class
- Win32_TSGatewayConnectionAuthorizationPolicy class Remote Desktop Services , SetDeviceRedirectionType method
topic_type:
- apiref
api_name:
- Win32_TSGatewayConnectionAuthorizationPolicy.SetDeviceRedirectionType
api_location:
- AagWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SetDeviceRedirectionType method of the Win32\_TSGatewayConnectionAuthorizationPolicy class

Sets the **DeviceRedirectionType** property, which controls which devices will be redirected.

## Syntax


```mof
uint32 SetDeviceRedirectionType(
  [in] uint32 DeviceRedirectionType
);
```



## Parameters

<dl> <dt>

*DeviceRedirectionType* \[in\]
</dt> <dd>

The device redirection type.

<dt>

0
</dt> <dd>

All devices will be redirected.

</dd> <dt>

1
</dt> <dd>

No devices will be redirected.

</dd> <dt>

2
</dt> <dd>

Specified devices will not be redirected. The **DiskDrivesDisabled**, **PrintersDisabled**, **SerialPortsDisabled**, **ClipboardDisabled**, and **PlugAndPlayDevicesDisabled** properties control which devices will not be redirected.

</dd> </dl> </dd> </dl>

## Return value

If the method succeeds, it returns zero. If the method is unsuccessful, it returns a nonzero value. For a list of error codes, see [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md).

## Remarks

You must be a member of the Administrators group to call this method.

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Microsoft Windows Software Development Kit (SDK). They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](/windows/desktop/WmiSdk/managed-object-format--mof-).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                           |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                 |
| MOF<br/>                      | <dl> <dt>TSGateway.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AagWmi.dll</dt> </dl>    |



## See also

<dl> <dt>

[**Win32\_TSGatewayConnectionAuthorizationPolicy**](win32-tsgatewayconnectionauthorizationpolicy.md)
</dt> </dl>

 

