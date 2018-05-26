---
title: Add method of the PS\_DnsServerZoneScope class
description: Adds a zone scope to a DNS zone.
audience: developer
ms.assetid: 8245318b-d2b1-4ba5-b2b4-a91c69487f25
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Add method
- Add method, PS_DnsServerZoneScope class
- PS_DnsServerZoneScope class, Add method
topic_type:
- apiref
api_name:
- PS_DnsServerZoneScope.Add
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Add method of the PS\_DnsServerZoneScope class

Adds a zone scope to a DNS zone.

## Syntax


```mof
uint32 Add(
  [in]  string       ZoneName,
  [in]  string       Name,
  [in]  boolean      LoadExisting,
  [in]  boolean      PassThru,
  [in]  string       ComputerName,
  [out] DnsZoneScope cmdletOutput
);
```



## Parameters

<dl> <dt>

*ZoneName* \[in\]
</dt> <dd>

The name of the zone that receives the zone scope.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

The name of the zone scope to add.

</dd> <dt>

*LoadExisting* \[in\]
</dt> <dd>

Indicates whether to load the existing zone scope. **True** to load the zone scope; otherwise **false**.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Indicates whether the [**DnsZoneScope**](dnszonescope.md) parameter returns an object. **True** to return an object; otherwise **false**.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

The computer name of the machine that hosts the DNS zone.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The [**DnsZoneScope**](dnszonescope.md) object that receives the zone scope.

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

 

 





