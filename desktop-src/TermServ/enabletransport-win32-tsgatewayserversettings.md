---
title: EnableTransport method of the Win32_TSGatewayServerSettings class
description: Enables or disables the specified transport.
ms.assetid: 95c599d7-56c3-462a-9c7d-2ecf8fc55da1
ms.tgt_platform: multiple
keywords:
- EnableTransport method Remote Desktop Services
- EnableTransport method Remote Desktop Services , Win32_TSGatewayServerSettings class
- Win32_TSGatewayServerSettings class Remote Desktop Services , EnableTransport method
topic_type:
- apiref
api_name:
- Win32_TSGatewayServerSettings.EnableTransport
api_location:
- AagWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# EnableTransport method of the Win32\_TSGatewayServerSettings class

Enables or disables the specified transport.

## Syntax


```mof
uint32 EnableTransport(
  [in] uint16  TransportType,
  [in] boolean Enable
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

*Enable* \[in\]
</dt> <dd>

Specifies if the transport is enabled or disabled.

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

 

 





