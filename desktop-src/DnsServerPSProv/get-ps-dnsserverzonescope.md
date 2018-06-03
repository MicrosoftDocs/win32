---
title: Get method of the PS\_DnsServerZoneScope class
description: Retrieves a zone scope from a DNS zone.
audience: developer
ms.assetid: 9398ae8f-8f52-4997-becc-25662a7e8b02
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_DnsServerZoneScope class
- PS_DnsServerZoneScope class, Get method
topic_type:
- apiref
api_name:
- PS_DnsServerZoneScope.Get
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Get method of the PS\_DnsServerZoneScope class

Retrieves a zone scope from a DNS zone.

## Syntax


```mof
uint32 Get(
  [in]  string       ZoneName,
  [in]  string       ComputerName,
  [in]  string       Name,
  [out] DnsZoneScope cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ZoneName* \[in\]
</dt> <dd>

The name of the zone that contains the zone scopes.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

The computer name of the machine that hosts the DNS zone.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

The name of the zone scope to retrieve.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An array that contains the [**DnsZoneScope**](dnszonescope.md) objects that receives the zone scopes retrieved from the DNS zone.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServerZoneScope**](ps-dnsserverzonescope.md)
</dt> </dl>

 

 





