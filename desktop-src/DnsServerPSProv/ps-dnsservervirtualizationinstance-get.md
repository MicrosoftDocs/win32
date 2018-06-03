---
title: Get method of the PS\_DnsServerVirtualizationInstance class
description: Gets a DNS server virtualization instance.
audience: developer
ms.assetid: 8922eede-29fb-4b98-8958-9dec9a48428e
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_DnsServerVirtualizationInstance class
- PS_DnsServerVirtualizationInstance class, Get method
topic_type:
- apiref
api_name:
- PS_DnsServerVirtualizationInstance.Get
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Get method of the PS\_DnsServerVirtualizationInstance class

Gets a DNS server virtualization instance.

## Syntax


```mof
uint32 Get(
  [in]  string                          ComputerName,
  [in]  string                          Name[],
  [out] DnsServerVirtualizationInstance cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Unique identifier of the virtualization instance.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

A [**DnsServerVirtualizationInstance**](dnsservervirtualizationinstance.md) that describes the specified instance.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServerVirtualizationInstance**](ps-dnsservervirtualizationinstance.md)
</dt> </dl>

 

 





