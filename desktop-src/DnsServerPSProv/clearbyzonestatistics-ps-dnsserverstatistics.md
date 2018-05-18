---
title: ClearByZoneStatistics method of the PS\_DnsServerStatistics class
description: Clear DNS server statistics.
audience: developer
ms.assetid: 'd256df31-22cd-4935-8722-9b5df5cf026b'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["ClearByZoneStatistics method", "ClearByZoneStatistics method, PS_DnsServerStatistics class", "PS_DnsServerStatistics class, ClearByZoneStatistics method"]
topic_type:
- apiref
api_name:
- PS_DnsServerStatistics.ClearByZoneStatistics
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# ClearByZoneStatistics method of the PS\_DnsServerStatistics class

Clear DNS server statistics.

## Syntax


```mof
uint32 ClearByZoneStatistics(
  [in] boolean Force,
  [in] string  ZoneName[],
  [in] string  ComputerName
);
```



## Parameters

<dl> <dt>

*Force* \[in\]
</dt> <dd>

If specified, overrides the default confirmation before performing the operation.

</dd> <dt>

*ZoneName* \[in\]
</dt> <dd>

Specifies zone name(s) for which statistics need to be cleared.

If *ZoneName* is specified, clear statistics for the specified zone(s). If *ZoneName* is not specified, aggregated server level statistics are cleared. Zone level statistics are not cleared in this case.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command

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

 

 





