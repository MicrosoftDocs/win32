---
title: EnableAllowOnlySDRServers method of the Win32_TSGatewayConnectionAuthorizationPolicy class
description: Used to toggle the AllowOnlySDRServers property.
ms.assetid: ec7f22bc-4e80-4ece-9567-5f405207480e
ms.tgt_platform: multiple
keywords:
- EnableAllowOnlySDRServers method Remote Desktop Services
- EnableAllowOnlySDRServers method Remote Desktop Services , Win32_TSGatewayConnectionAuthorizationPolicy class
- Win32_TSGatewayConnectionAuthorizationPolicy class Remote Desktop Services , EnableAllowOnlySDRServers method
topic_type:
- apiref
api_name:
- Win32_TSGatewayConnectionAuthorizationPolicy.EnableAllowOnlySDRServers
api_location:
- AagWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# EnableAllowOnlySDRServers method of the Win32\_TSGatewayConnectionAuthorizationPolicy class

Used to toggle the **AllowOnlySDRServers** property.

## Syntax


```mof
uint32 EnableAllowOnlySDRServers(
  [in] boolean AllowOnlySDRServers
);
```



## Parameters

<dl> <dt>

*AllowOnlySDRServers* \[in\]
</dt> <dd>

If set to **True**, connections will be allowed only to secure device redirection (SDR) RDS servers. If set to **False**, connections will be allowed to older RDS servers also

</dd> </dl>

## Return value

If the method succeeds, it returns zero. If the method is unsuccessful, it returns a nonzero value. For a list of error codes, see [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                        |
| Namespace<br/>                | ROOT\\cimv2\\TerminalServices<br/>                                                 |
| MOF<br/>                      | <dl> <dt>TsGateway.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AagWmi.dll</dt> </dl>    |



## See also

<dl> <dt>

[**Win32\_TSGatewayConnectionAuthorizationPolicy**](win32-tsgatewayconnectionauthorizationpolicy.md)
</dt> </dl>

 

 





