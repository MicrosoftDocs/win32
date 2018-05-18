---
title: ExportByDsKey method of the PS\_DnsServerDnsSecPublicKey class
description: Exports DS or DNSKEY information of a DNSSEC signed zone.
audience: developer
ms.assetid: '1348d6b2-3a53-4eb6-bd38-916f041e3370'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["ExportByDsKey method", "ExportByDsKey method, PS_DnsServerDnsSecPublicKey class", "PS_DnsServerDnsSecPublicKey class, ExportByDsKey method"]
topic_type:
- apiref
api_name:
- PS_DnsServerDnsSecPublicKey.ExportByDsKey
api_location:
- DNSServerPSProvider.dll
api_type:
- COM
---

# ExportByDsKey method of the PS\_DnsServerDnsSecPublicKey class

Exports DS or DNSKEY information of a DNSSEC signed zone.

## Syntax


```mof
uint32 ExportByDsKey(
  [in]  string                  ZoneName,
  [in]  boolean                 UnAuthenticated,
  [in]  string                  ComputerName,
  [in]  boolean                 Force,
  [in]  boolean                 NoClobber,
  [in]  boolean                 PassThru,
  [in]  string                  Path,
  [in]  string                  DigestType[],
  [out] DnsServerResourceRecord cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ZoneName* \[in\]
</dt> <dd>

Name of the primary zone from which DnsSec public keys will be exported.

</dd> <dt>

*UnAuthenticated* \[in\]
</dt> <dd>

If specified, even if the admin does not have permissions to run the cmdlets on the remote server, the provider would query for DNSKEY and export the required data.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS server name which is authoritative for the Signed zone.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

If specified, overrides default confirmation before performing the operation.

</dd> <dt>

*NoClobber* \[in\]
</dt> <dd>

If specified, does not overwrite if the file already exists.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If specified, returns the object or objects on which the operation was done.

</dd> <dt>

*Path* \[in\]
</dt> <dd>

Absolute path used to place the keyset file, the file name will be automatically created according to the zone name.

</dd> <dt>

*DigestType* \[in\]
</dt> <dd>

Algorithm used to create the DS record.

The possible values are.

<dt>

<span id="Sha1"></span><span id="sha1"></span><span id="SHA1"></span>

**Sha1** ("Sha1")


</dt> <dd></dd> <dt>

<span id="Sha256"></span><span id="sha256"></span><span id="SHA256"></span>

**Sha256** ("Sha256")


</dt> <dd></dd> <dt>

<span id="Sha384"></span><span id="sha384"></span><span id="SHA384"></span>

**Sha384** ("Sha384")


</dt> <dd></dd> </dl> </dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

A [**DnsServerResourceRecord**](dnsserverresourcerecord.md) that contains the exported information.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DNSServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServerDnsSecPublicKey**](ps-dnsserverdnssecpublickey.md)
</dt> </dl>

 

 





