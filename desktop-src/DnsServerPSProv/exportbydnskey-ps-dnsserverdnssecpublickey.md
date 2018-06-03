---
title: ExportByDnsKey method of the PS\_DnsServerDnsSecPublicKey class
description: Exports DS or DNSKEY information of a DNSSEC signed zone.
audience: developer
ms.assetid: e1d10eb9-0e41-4a5e-92ec-f8589ffeed2e
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ExportByDnsKey method
- ExportByDnsKey method, PS_DnsServerDnsSecPublicKey class
- PS_DnsServerDnsSecPublicKey class, ExportByDnsKey method
topic_type:
- apiref
api_name:
- PS_DnsServerDnsSecPublicKey.ExportByDnsKey
api_location:
- DNSServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ExportByDnsKey method of the PS\_DnsServerDnsSecPublicKey class

Exports DS or DNSKEY information of a DNSSEC signed zone.

## Syntax


```mof
uint32 ExportByDnsKey(
  [in]  string                  ZoneName,
  [in]  string                  Path,
  [in]  boolean                 PassThru,
  [in]  boolean                 UnAuthenticated,
  [in]  boolean                 Force,
  [in]  boolean                 NoClobber,
  [in]  string                  ComputerName,
  [out] DnsServerResourceRecord cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ZoneName* \[in\]
</dt> <dd>

Name of the primary zone from which DnsSec public keys will be exported.

</dd> <dt>

*Path* \[in\]
</dt> <dd>

Absolute path used to place the keyset file, the file name will be automatically created according to the zone name

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If specified, returns the object or objects on which the operation was done.

</dd> <dt>

*UnAuthenticated* \[in\]
</dt> <dd>

If specified, even if the admin does not have permissions to run the cmdlets on the remote server, the provider would query for DNSKEY and export the required data.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

If specified, overrides default confirmation before performing the operation

</dd> <dt>

*NoClobber* \[in\]
</dt> <dd>

If specified, does not overwrite if the file already exists

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS server name which is authoritative for the Signed zone

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

DnsServerResourceRecord

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DNSServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServerDnsSecPublicKey**](ps-dnsserverdnssecpublickey.md)
</dt> </dl>

 

 





