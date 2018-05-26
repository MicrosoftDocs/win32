---
title: Get method of the PS\_DnsServerZoneAging class
description: Retrieves DNS Aging settings for a zone.
audience: developer
ms.assetid: 6faf6d59-fbf4-4492-9847-530afe85be5d
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_DnsServerZoneAging class
- PS_DnsServerZoneAging class, Get method
topic_type:
- apiref
api_name:
- PS_DnsServerZoneAging.Get
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Get method of the PS\_DnsServerZoneAging class

Retrieves DNS Aging settings for a zone.

## Syntax


```mof
uint32 Get(
  [in]  string             Name[],
  [in]  string             ComputerName,
  [out] DnsServerZoneAging cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

Specifies the name of the zone.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

One or more embedded instances of the [**DnsServerZoneAging**](dnsserverzoneaging.md) class.

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

[**PS\_DnsServerZoneAging**](ps-dnsserverzoneaging.md)
</dt> </dl>

 

 





