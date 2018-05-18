---
title: GetByZone method of the PS\_DnsServerZoneTransferPolicy class
description: Enumerates a zone transfer object by zone.
audience: developer
ms.assetid: '65830c40-4a49-48f6-bd06-07812fd6995f'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetByZone method", "GetByZone method, PS_DnsServerZoneTransferPolicy class", "PS_DnsServerZoneTransferPolicy class, GetByZone method"]
topic_type:
- apiref
api_name:
- PS_DnsServerZoneTransferPolicy.GetByZone
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# GetByZone method of the PS\_DnsServerZoneTransferPolicy class

Enumerates a zone transfer object by zone.

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

[**PS\_DnsServerZoneTransferPolicy**](ps-dnsserverzonetransferpolicy.md)
</dt> </dl>

 

 





