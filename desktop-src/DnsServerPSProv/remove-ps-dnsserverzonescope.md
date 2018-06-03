---
title: Remove method of the PS\_DnsServerZoneScope class
description: Removes a zone scope from an existing DNS zone.
audience: developer
ms.assetid: 02e022ee-edfd-4100-b12c-828f5d589c0a
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Remove method
- Remove method, PS_DnsServerZoneScope class
- PS_DnsServerZoneScope class, Remove method
topic_type:
- apiref
api_name:
- PS_DnsServerZoneScope.Remove
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Remove method of the PS\_DnsServerZoneScope class

Removes a zone scope from an existing DNS zone.

## Syntax


```mof
uint32 Remove(
  [in]  string       ZoneName,
  [in]  string       Name,
  [in]  boolean      PassThru,
  [in]  boolean      Force,
  [in]  string       ComputerName,
  [out] DnsZoneScope cmdletOutput
);
```



## Parameters

<dl> <dt>

*ZoneName* \[in\]
</dt> <dd>

The name of the zone that contains the zone scope to remove.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

The name of the zone scope to remove.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Indicates whether the [**DnsZoneScope**](dnszonescope.md) parameter returns an object. **True** to return an object; otherwise **false**.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Indicates whether this method displays the default confirmation prompt to the user. **True** to displays the default confirmation prompt; otherwise **false**.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

The computer name of the machine that hosts the DNS zone.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The [**DnsZoneScope**](dnszonescope.md) object that receives the zone scope to remove.

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

 

 





