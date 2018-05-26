---
title: Get method of the PS\_DnsServerRecursion class
description: Retrieves DNS Server Recursion settings.
audience: developer
ms.assetid: 01ea1b2b-5925-468b-bddc-a3f477848edb
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_DnsServerRecursion class
- PS_DnsServerRecursion class, Get method
topic_type:
- apiref
api_name:
- PS_DnsServerRecursion.Get
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Get method of the PS\_DnsServerRecursion class

Retrieves DNS Server Recursion settings.

## Syntax


```mof
uint32 Get(
  [in]  string             ComputerName,
  [out] DnsServerRecursion cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on to execute the command

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DnsServerRecursion**](dnsserverrecursion.md) class.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServerRecursion**](ps-dnsserverrecursion.md)
</dt> </dl>

 

 





