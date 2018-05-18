---
title: Add method of the PS\_DnsServerResourceRecordDS class
description: Adds a DS resource record.
audience: developer
ms.assetid: '8b1dd534-5bd3-4e93-9cf3-92d8851177ed'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Add method", "Add method, PS_DnsServerResourceRecordDS class", "PS_DnsServerResourceRecordDS class, Add method"]
topic_type:
- apiref
api_name:
- PS_DnsServerResourceRecordDS.Add
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# Add method of the PS\_DnsServerResourceRecordDS class

Adds a DS resource record.

## Syntax


```mof
uint32 Add(
  [in]  string                  Name,
  [in]  string                  CryptoAlgorithm,
  [in]  datetime                TimeToLive,
  [in]  boolean                 AgeRecord,
  [in]  string                  Digest,
  [in]  string                  DigestType,
  [in]  uint16                  KeyTag,
  [in]  string                  ComputerName,
  [in]  string                  ZoneName,
  [in]  boolean                 PassThru,
  [in]  string                  ZoneScope,
  [out] DnsServerResourceRecord cmdletOutput
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

Specifies the name of the resource record that this method adds to the DNS server.

</dd> <dt>

*CryptoAlgorithm* \[in\]
</dt> <dd>

Specifies the cryptographic algorithm the server uses to generate keys. The acceptable values for this parameter are:

<dt>

<span id="RsaSha1"></span><span id="rsasha1"></span><span id="RSASHA1"></span>

**RsaSha1** (RsaSha1)


</dt> <dd></dd> <dt>

<span id="RsaSha256"></span><span id="rsasha256"></span><span id="RSASHA256"></span>

**RsaSha256** (RsaSha256)


</dt> <dd></dd> <dt>

<span id="RsaSha512"></span><span id="rsasha512"></span><span id="RSASHA512"></span>

**RsaSha512** (RsaSha512)


</dt> <dd></dd> <dt>

<span id="RsaSha1NSec3"></span><span id="rsasha1nsec3"></span><span id="RSASHA1NSEC3"></span>

**RsaSha1NSec3** (RsaSha1NSec3)


</dt> <dd></dd> <dt>

<span id="ECDsaP256Sha256"></span><span id="ecdsap256sha256"></span><span id="ECDSAP256SHA256"></span>

**ECDsaP256Sha256** (ECDsaP256Sha256)


</dt> <dd></dd> <dt>

<span id="ECDsaP384Sha384"></span><span id="ecdsap384sha384"></span><span id="ECDSAP384SHA384"></span>

**ECDsaP384Sha384** (ECDsaP384Sha384)


</dt> <dd></dd> </dl> </dd> <dt>

*TimeToLive* \[in\]
</dt> <dd>

Specifies the Time to Live (TTL) value, in seconds, for a resource record. Other DNS servers use this length of time to determine how long to cache a record.

</dd> <dt>

*AgeRecord* \[in\]
</dt> <dd>

Indicates that the DNS server uses a time stamp for the resource record that this method adds. A DNS server can scavenge resource records that have become stale based on a time stamp.

</dd> <dt>

*Digest* \[in\]
</dt> <dd>

The DS digest data.

</dd> <dt>

*DigestType* \[in\]
</dt> <dd>

Specifies the type of digest data. The acceptable values for this parameter are:

<dt>

<span id="Sha1"></span><span id="sha1"></span><span id="SHA1"></span>

**Sha1** (Sha1)


</dt> <dd></dd> <dt>

<span id="Sha256"></span><span id="sha256"></span><span id="SHA256"></span>

**Sha256** (Sha256)


</dt> <dd></dd> <dt>

<span id="Sha384"></span><span id="sha384"></span><span id="SHA384"></span>

**Sha384** (Sha384)


</dt> <dd></dd> </dl> </dd> <dt>

*KeyTag* \[in\]
</dt> <dd>

Specifies a key tag.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies a DNS server. If you do not specify this parameter, the command runs on the local system. You can specify an IP address or any value that resolves to an IP address, such as a fully qualified domain name (FQDN), host name, or NETBIOS name.

</dd> <dt>

*ZoneName* \[in\]
</dt> <dd>

Specifies the name of a DNS zone. The method adds the record to this zone.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to return the object that was modified by the method. By default, this method does not generate any output.

</dd> <dt>

*ZoneScope* \[in\]
</dt> <dd>

Name of the zone scope.

**Windows Server 2012:** Not supported.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Receives and embedded instance of the [**DnsServerResourceRecordDS**](dnsserverresourcerecordds.md) class.

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

[**PS\_DnsServerResourceRecordDS**](ps-dnsserverresourcerecordds.md)
</dt> </dl>

 

 





