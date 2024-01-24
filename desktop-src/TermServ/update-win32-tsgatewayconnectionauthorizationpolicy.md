---
title: Update method of the Win32_TSGatewayConnectionAuthorizationPolicy class
description: Updates the current Remote Desktop connection authorization policy (RD \ 160;CAP).
ms.assetid: 6d13d1b7-1c7d-4d22-b42c-36e0f4446e86
ms.tgt_platform: multiple
keywords:
- Update method Remote Desktop Services
- Update method Remote Desktop Services , Win32_TSGatewayConnectionAuthorizationPolicy class
- Win32_TSGatewayConnectionAuthorizationPolicy class Remote Desktop Services , Update method
topic_type:
- apiref
api_name:
- Win32_TSGatewayConnectionAuthorizationPolicy.Update
api_location:
- AagWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Update method of the Win32\_TSGatewayConnectionAuthorizationPolicy class

Updates the current Remote Desktop connection authorization policy (RD CAP).

## Syntax


```mof
uint32 Update(
  [in] string  Name,
  [in] string  UserGroupNames,
  [in] string  ComputerGroupNames,
  [in] boolean SmartCard,
  [in] boolean Password,
  [in] boolean SecureId,
  [in] boolean Enabled,
  [in] uint32  DeviceRedirectionType,
  [in] boolean DiskDrivesDisabled,
  [in] boolean PrintersDisabled,
  [in] boolean SerialPortsDisabled,
  [in] boolean ClipboardDisabled,
  [in] boolean PlugAndPlayDevicesDisabled,
  [in] uint32  IdleTimeout,
  [in] uint32  SessionTimeout,
  [in] uint32  SessionTimeoutAction,
  [in] boolean AllowOnlySDRServers,
  [in] boolean CookieAuthentication
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

Name of the RD CAP. The name must be 64 characters or less, unique (case is ignored), and cannot contain the following reserved characters:

<> : ; " / \\ \| ? \* \[TAB\]

</dd> <dt>

*UserGroupNames* \[in\]
</dt> <dd>

List of semicolon-separated user group names. The names are of the format *Domain\\UserGroupName*. If the user belongs to any one of these user groups, the user will be permitted access to the RD Gateway server.

</dd> <dt>

*ComputerGroupNames* \[in\]
</dt> <dd>

List of semicolon-separated machine group names. This value can be empty. The names are of the format *Domain\\ComputerGroupName*. If a value is specified, the client computer must belong to one of these computer groups for the user to access the RD Gateway server.

</dd> <dt>

*SmartCard* \[in\]
</dt> <dd>

Specifies whether smart cards can be used to authenticate with the RD Gateway server.

</dd> <dt>

*Password* \[in\]
</dt> <dd>

Specifies whether passwords can be used to authenticate with the RD Gateway server.

</dd> <dt>

*SecureId* \[in\]
</dt> <dd>

This parameter is reserved for future use.

</dd> <dt>

*Enabled* \[in\]
</dt> <dd>

Specifies whether this RD CAP is enabled.

</dd> <dt>

*DeviceRedirectionType* \[in\]
</dt> <dd>

Specifies which device types will be redirected.

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

Specified devices will not be redirected. The *DiskDrivesDisabled*, *PrintersDisabled*, *SerialPortsDisabled*, *ClipboardDisabled*, and *PlugAndPlayDevicesDisabled* parameters control which devices will not be redirected.

</dd> </dl> </dd> <dt>

*DiskDrivesDisabled* \[in\]
</dt> <dd>

Specifies whether to disable disk drive redirection if the *DeviceRedirectionType* parameter is "2".

</dd> <dt>

*PrintersDisabled* \[in\]
</dt> <dd>

Specifies whether to disable printer redirection if the *DeviceRedirectionType* parameter is "2".

</dd> <dt>

*SerialPortsDisabled* \[in\]
</dt> <dd>

Specifies whether to disable serial port redirection if the *DeviceRedirectionType* parameter is "2".

</dd> <dt>

*ClipboardDisabled* \[in\]
</dt> <dd>

Specifies whether to disable clipboard redirection if the *DeviceRedirectionType* parameter is "2".

</dd> <dt>

*PlugAndPlayDevicesDisabled* \[in\]
</dt> <dd>

Specifies whether to disable redirection of Plug and Play devices if the *DeviceRedirectionType* parameter is "2".

</dd> <dt>

*IdleTimeout* \[in\]
</dt> <dd>

Idle timeout value in minutes

</dd> <dt>

*SessionTimeout* \[in\]
</dt> <dd>

Session timeout value in minutes

</dd> <dt>

*SessionTimeoutAction* \[in\]
</dt> <dd>

Session timeout action in minutes

</dd> <dt>

*AllowOnlySDRServers* \[in\]
</dt> <dd>

Whether connections allowed only to SDR TS servers

</dd> <dt>

*CookieAuthentication* \[in\]
</dt> <dd>

Indicates whether cookie authentication can be used to connect to TS Gateway server

</dd> </dl>

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

 

