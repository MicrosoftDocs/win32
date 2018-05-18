---
title: GetByZone method of the PS\_DnsServerQueryResolutionPolicy class
description: Enumerates the name resolution policies by zone.
audience: developer
ms.assetid: '3660aa91-2bd2-4669-bf48-248877a52708'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetByZone method", "GetByZone method, PS_DnsServerQueryResolutionPolicy class", "PS_DnsServerQueryResolutionPolicy class, GetByZone method"]
topic_type:
- apiref
api_name:
- PS_DnsServerQueryResolutionPolicy.GetByZone
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# GetByZone method of the PS\_DnsServerQueryResolutionPolicy class

Enumerates the name resolution policies by zone

## Syntax


```mof
uint32 GetByZone(
  [in]  string          Name,
  [in]  string          ComputerName,
  [in]  string          ZoneName,
  [out] DnsServerPolicy cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

Name of the policy to retrieve.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Optional DNS server name.

</dd> <dt>

*ZoneName* \[in\]
</dt> <dd>

Name of the zone.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On return, contains an array of [**DnsServerPolicy**](dnsserverpolicy.md). This parameter returns a value only if *PassThru* is set to **true.**

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServerQueryResolutionPolicy**](ps-dnsserverqueryresolutionpolicy.md)
</dt> </dl>

 

 





