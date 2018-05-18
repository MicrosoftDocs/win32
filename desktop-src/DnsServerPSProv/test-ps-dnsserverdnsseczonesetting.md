---
title: Test method of the PS\_DnsServerDnsSecZoneSetting class
description: Validates if the DNSSEC settings configured on the zone are valid.
audience: developer
ms.assetid: '9d8655ab-c278-4972-97a0-8ac923229eeb'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Test method", "Test method, PS_DnsServerDnsSecZoneSetting class", "PS_DnsServerDnsSecZoneSetting class, Test method"]
topic_type:
- apiref
api_name:
- PS_DnsServerDnsSecZoneSetting.Test
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# Test method of the PS\_DnsServerDnsSecZoneSetting class

Validates if the DNSSEC settings configured on the zone are valid.

## Syntax


```mof
uint32 Test(
  [in]  string                              ZoneName,
  [in]  string                              ComputerName,
  [out] DnsServerZoneDnsSecValidationResult cmdletOutput
);
```



## Parameters

<dl> <dt>

*ZoneName* \[in\]
</dt> <dd>

Name of the zone on which DnsSec operations are performed.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Optional DNS server name.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On return, contains an instance of the current object. This parameter returns a value only if *PassThru* is set to **true.**

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServerDnsSecZoneSetting**](ps-dnsserverdnsseczonesetting.md)
</dt> </dl>

 

 





