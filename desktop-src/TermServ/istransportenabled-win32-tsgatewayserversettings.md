---
title: IsTransportEnabled method of the Win32_TSGatewayServerSettings class
description: Determines whether the specified transport is enabled.
ms.assetid: 3f08a206-5800-4088-a113-bb3f0cc826f2
ms.tgt_platform: multiple
keywords:
- IsTransportEnabled method Remote Desktop Services
- IsTransportEnabled method Remote Desktop Services , Win32_TSGatewayServerSettings class
- Win32_TSGatewayServerSettings class Remote Desktop Services , IsTransportEnabled method
topic_type:
- apiref
api_name:
- Win32_TSGatewayServerSettings.IsTransportEnabled
api_location:
- AagWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IsTransportEnabled method of the Win32\_TSGatewayServerSettings class

Determines whether the specified transport is enabled.

## Syntax


```mof
uint32 IsTransportEnabled(
  [in]  uint16  TransportType,
  [out] boolean Enabled
);
```



## Parameters

<dl> <dt>

*TransportType* \[in\]
</dt> <dd>

Specifies the transport type. This must be one of the following values.

<dt>

0
</dt> <dd>

RPC over HTTP transport.

</dd> <dt>

1
</dt> <dd>

HTTP transport.

</dd> <dt>

2
</dt> <dd>

UDP transport.

</dd> </dl> </dd> <dt>

*Enabled* \[out\]
</dt> <dd>

A **boolean** value that indicates whether the transport is enabled.

</dd> </dl>

## Return value

If the method succeeds, it returns zero. If the method is unsuccessful, it returns a nonzero value. For a list of error codes, see [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                           |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                 |
| MOF<br/>                      | <dl> <dt>TSGateway.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AagWmi.dll</dt> </dl>    |



## See also

<dl> <dt>

[**Win32\_TSGatewayServerSettings**](win32-tsgatewayserversettings.md)
</dt> </dl>

 

 





