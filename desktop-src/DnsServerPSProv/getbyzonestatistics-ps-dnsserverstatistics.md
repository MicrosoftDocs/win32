---
title: GetByZoneStatistics method of the PS\_DnsServerStatistics class
description: Gets DNS server statistics.
audience: developer
ms.assetid: '0d45a849-e25d-4c1a-a352-35d76382eade'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetByZoneStatistics method", "GetByZoneStatistics method, PS_DnsServerStatistics class", "PS_DnsServerStatistics class, GetByZoneStatistics method"]
topic_type:
- apiref
api_name:
- PS_DnsServerStatistics.GetByZoneStatistics
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# GetByZoneStatistics method of the PS\_DnsServerStatistics class

Gets DNS server statistics. Aggregated server level statistics cannot be cleared using this cmdlet.

## Syntax


```mof
uint32 GetByZoneStatistics(
  [in]  boolean                 Clear,
  [in]  string                  ComputerName,
  [in]  string                  ZoneName[],
  [out] DnsServerZoneStatistics cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*Clear* \[in\]
</dt> <dd>

Specifies if zone statistics need to be cleared for specified zone(s).

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command

</dd> <dt>

*ZoneName* \[in\]
</dt> <dd>

Specifies zone name(s) for which statistics need to be retrieved.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DnsServerZoneStatistics**](dnsserverzonestatistics.md) class.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServerStatistics**](ps-dnsserverstatistics.md)
</dt> </dl>

 

 





