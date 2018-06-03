---
title: RemoveByServer method of the PS\_DnsServerQueryResolutionPolicy class
description: Removes the name resolution policy from a DNS server by server.
audience: developer
ms.assetid: 0644696c-1207-49b3-b8bf-3139207af597
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoveByServer method
- RemoveByServer method, PS_DnsServerQueryResolutionPolicy class
- PS_DnsServerQueryResolutionPolicy class, RemoveByServer method
topic_type:
- apiref
api_name:
- PS_DnsServerQueryResolutionPolicy.RemoveByServer
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RemoveByServer method of the PS\_DnsServerQueryResolutionPolicy class

Removes the name resolution policy from a DNS server by server.

## Syntax


```mof
uint32 RemoveByServer(
  [in]  boolean         Force,
  [in]  string          ComputerName,
  [in]  boolean         PassThru,
  [in]  string          Name,
  [out] DnsServerPolicy cmdletOutput
);
```



## Parameters

<dl> <dt>

*Force* \[in\]
</dt> <dd>

**True** to not require user confirmation before continuing with the operation; **false** to require user confirmation. The default value is **false**.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Optional DNS server name.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to return the current instance in the *CmdletOutput* parameter. The default is **false**.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

The name of the policy to remove.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On return, contains a [**DnsServerPolicy**](dnsserverpolicy.md). This parameter returns a value only if *PassThru* is set to **true.**

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServerQueryResolutionPolicy**](ps-dnsserverqueryresolutionpolicy.md)
</dt> </dl>

 

 





