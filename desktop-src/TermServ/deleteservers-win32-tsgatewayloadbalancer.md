---
title: DeleteServers method of the Win32_TSGatewayLoadBalancer class
description: Deletes servers from the Servers property.
ms.assetid: 5ef44725-82b6-464a-abab-a68cc8799669
ms.tgt_platform: multiple
keywords:
- DeleteServers method Remote Desktop Services
- DeleteServers method Remote Desktop Services , Win32_TSGatewayLoadBalancer class
- Win32_TSGatewayLoadBalancer class Remote Desktop Services , DeleteServers method
topic_type:
- apiref
api_name:
- Win32_TSGatewayLoadBalancer.DeleteServers
api_location:
- AagWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# DeleteServers method of the Win32\_TSGatewayLoadBalancer class

Deletes servers from the **Servers** property.

## Syntax


```mof
uint32 DeleteServers(
  [in] string Servers
);
```



## Parameters

<dl> <dt>

*Servers* \[in\]
</dt> <dd>

Semicolon-separated list of RD Gateway load-balancing servers to delete from the **Servers** property.

</dd> </dl>

## Return value

If the method succeeds, it returns zero. If the method is unsuccessful, it returns a nonzero value. For a list of error codes, see [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md).

## Remarks

If multiple servers are in the *Servers* parameter and one of the servers cannot be processed, none of the servers will be processed.

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

[**Win32\_TSGatewayLoadBalancer**](win32-tsgatewayloadbalancer.md)
</dt> </dl>

 

