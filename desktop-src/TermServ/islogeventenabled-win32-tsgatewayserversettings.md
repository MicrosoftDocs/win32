---
title: IsLogEventEnabled method of the Win32_TSGatewayServerSettings class
description: Indicates whether the specified event log type is enabled.
ms.assetid: 4abfc56f-871a-44ef-9998-da88949a0a2d
ms.tgt_platform: multiple
keywords:
- IsLogEventEnabled method Remote Desktop Services
- IsLogEventEnabled method Remote Desktop Services , Win32_TSGatewayServerSettings class
- Win32_TSGatewayServerSettings class Remote Desktop Services , IsLogEventEnabled method
topic_type:
- apiref
api_name:
- Win32_TSGatewayServerSettings.IsLogEventEnabled
api_location:
- AagWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IsLogEventEnabled method of the Win32\_TSGatewayServerSettings class

Indicates whether the specified event log type is enabled.

## Syntax


```mof
uint32 IsLogEventEnabled(
  [in]  string  EventName,
  [out] boolean Enabled
);
```



## Parameters

<dl> <dt>

*EventName* \[in\]
</dt> <dd>

Name of the event log type. This value should be retrieved by using the [**GetLogEventName**](getlogeventname-win32-tsgatewayserversettings.md) method.

<dt>

LogChannelDisconnect
</dt> <dd>

User successfully disconnected from the resource.

</dd> <dt>

LogFailedChannelConnect
</dt> <dd>

User failed to connect to the resource.

</dd> <dt>

LogFailureNetworkAccessCheck
</dt> <dd>

User failed connection authorization.

</dd> <dt>

LogFailureResourceAccessCheck
</dt> <dd>

User failed resource authorization.

</dd> <dt>

LogSuccessChannelConnect
</dt> <dd>

User successfully connected to the resource.

</dd> <dt>

LogSuccessfulNetworkAccessCheck
</dt> <dd>

User successfully passed connection authorization.

</dd> <dt>

LogSuccessfulResourceAccessCheck
</dt> <dd>

User successfully passed resource authorization.

</dd> </dl> </dd> <dt>

*Enabled* \[out\]
</dt> <dd>

Indicates whether the specified event log type is enabled.

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

[**Win32\_TSGatewayServerSettings**](win32-tsgatewayserversettings.md)
</dt> <dt>

[**GetLogEventName**](getlogeventname-win32-tsgatewayserversettings.md)
</dt> </dl>

 

