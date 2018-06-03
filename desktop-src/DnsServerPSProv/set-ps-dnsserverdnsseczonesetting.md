---
title: Set method of the PS\_DnsServerDnsSecZoneSetting class
description: Specifies the NSEC/NSEC3 and other advanced DNSSEC settings for a zone.
audience: developer
ms.assetid: a6af48e9-5c46-4b31-9f83-8656ef659608
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Set method
- Set method, PS_DnsServerDnsSecZoneSetting class
- PS_DnsServerDnsSecZoneSetting class, Set method
topic_type:
- apiref
api_name:
- PS_DnsServerDnsSecZoneSetting.Set
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Set method of the PS\_DnsServerDnsSecZoneSetting class

Specifies the NSEC/NSEC3 and other advanced DNSSEC settings for a zone.

## Syntax


```mof
uint32 Set(
  [in]  string                     ZoneName,
  [in]  string                     DenialOfExistence,
  [in]  string                     NSec3HashAlgorithm,
  [in]  uint16                     NSec3Iterations,
  [in]  boolean                    NSec3OptOut,
  [in]  uint8                      NSec3RandomSaltLength,
  [in]  string                     NSec3UserSalt,
  [in]  string                     DistributeTrustAnchor[],
  [in]  boolean                    EnableRfc5011KeyRollover,
  [in]  string                     DSRecordGenerationAlgorithm[],
  [in]  datetime                   DSRecordSetTtl,
  [in]  datetime                   DnsKeyRecordSetTtl,
  [in]  datetime                   SignatureInceptionOffset,
  [in]  datetime                   SecureDelegationPollingPeriod,
  [in]  datetime                   PropagationTime,
  [in]  boolean                    ParentHasSecureDelegation,
  [in]  string                     ComputerName,
  [in]  boolean                    PassThru,
  [out] DnsServerDnsSecZoneSetting cmdletOutput
);
```



## Parameters

<dl> <dt>

*ZoneName* \[in\]
</dt> <dd>

Name of the zone on which DnsSec operations are performed.

</dd> <dt>

*DenialOfExistence* \[in\]
</dt> <dd>

This setting is used by the DNS server to provide a signed proof of unregistered name in the DNS database.

</dd> <dt>

*NSec3HashAlgorithm* \[in\]
</dt> <dd>

NSEC3 hash algorithm. Default value is always 1.

</dd> <dt>

*NSec3Iterations* \[in\]
</dt> <dd>

NSEC3 iterations. Default value is 50.

</dd> <dt>

*NSec3OptOut* \[in\]
</dt> <dd>

NSEC3 opt-out. Default value is FALSE.

</dd> <dt>

*NSec3RandomSaltLength* \[in\]
</dt> <dd>

Random salt length in octets. Default is 8.

</dd> <dt>

*NSec3UserSalt* \[in\]
</dt> <dd>

User salt string. Default is NULL or -.

</dd> <dt>

*DistributeTrustAnchor* \[in\]
</dt> <dd>

Specifies if trust anchors should be published. Default is None.

</dd> <dt>

*EnableRfc5011KeyRollover* \[in\]
</dt> <dd>

Specifies if RFC 5011 key rollover is enabled. Default is FALSE.

</dd> <dt>

*DSRecordGenerationAlgorithm* \[in\]
</dt> <dd>

DS record generation algorithm. Valid values are: Sha1, Sha256 and Sha384. Default is Sha1.

</dd> <dt>

*DSRecordSetTtl* \[in\]
</dt> <dd>

DS Record Set TTL. Default is same as zone TTL.

</dd> <dt>

*DnsKeyRecordSetTtl* \[in\]
</dt> <dd>

TTL of DNS Key Record.

</dd> <dt>

*SignatureInceptionOffset* \[in\]
</dt> <dd>

Signature inception. Default is 1 hour.

</dd> <dt>

*SecureDelegationPollingPeriod* \[in\]
</dt> <dd>

Delegation polling period. Default is 12 hours.

</dd> <dt>

*PropagationTime* \[in\]
</dt> <dd>

Propagation time. Default is 2 days.

</dd> <dt>

*ParentHasSecureDelegation* \[in\]
</dt> <dd>

If parent has secure delegation.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Optional DNS server name.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to return the current instance in the *CmdletOutput* parameter. The default is **false**.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On return, contains an instance of the current object. This parameter returns a value only if *PassThru* is set to **true.**

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServerDnsSecZoneSetting**](ps-dnsserverdnsseczonesetting.md)
</dt> </dl>

 

 





