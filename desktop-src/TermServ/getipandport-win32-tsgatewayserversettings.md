---
title: GetIPAndPort method of the Win32_TSGatewayServerSettings class
description: Obtains the listening IP address and port number for the specified transport.
ms.assetid: e12451c3-2641-49e1-bd35-f7cab37865ae
ms.tgt_platform: multiple
keywords:
- GetIPAndPort method Remote Desktop Services
- GetIPAndPort method Remote Desktop Services , Win32_TSGatewayServerSettings class
- Win32_TSGatewayServerSettings class Remote Desktop Services , GetIPAndPort method
topic_type:
- apiref
api_name:
- Win32_TSGatewayServerSettings.GetIPAndPort
api_location:
- AagWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# GetIPAndPort method of the Win32\_TSGatewayServerSettings class

Obtains the listening IP address and port number for the specified transport.

## Syntax


```mof
uint32 GetIPAndPort(
  [in]  uint16 TransportType,
  [out] string IPAddress,
  [out] uint16 Port
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

*IPAddress* \[out\]
</dt> <dd>

A string that receives the listening IP address, in octet form (for example, "192.168.1.1").

</dd> <dt>

*Port* \[out\]
</dt> <dd>

Specifies the listening port number.

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

 

 





