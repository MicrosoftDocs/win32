---
title: DnsServerDnsSecZoneSetting class
description: Represents Domain Name System Security Extensions (DNSSEC) settings for a DNS zone.
audience: developer
ms.assetid: 0c783b89-6b5f-466c-9589-2efc412dd810
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerDnsSecZoneSetting class
- DnsServerDnsSecZoneSetting class, described
topic_type:
- apiref
api_name:
- DnsServerDnsSecZoneSetting
- DnsServerDnsSecZoneSetting.ZoneName
- DnsServerDnsSecZoneSetting.DenialOfExistence
- DnsServerDnsSecZoneSetting.NSec3HashAlgorithm
- DnsServerDnsSecZoneSetting.NSec3Iterations
- DnsServerDnsSecZoneSetting.NSec3OptOut
- DnsServerDnsSecZoneSetting.NSec3RandomSaltLength
- DnsServerDnsSecZoneSetting.NSec3UserSalt
- DnsServerDnsSecZoneSetting.DistributeTrustAnchor
- DnsServerDnsSecZoneSetting.EnableRfc5011KeyRollover
- DnsServerDnsSecZoneSetting.DSRecordGenerationAlgorithm
- DnsServerDnsSecZoneSetting.DSRecordSetTtl
- DnsServerDnsSecZoneSetting.DnsKeyRecordSetTtl
- DnsServerDnsSecZoneSetting.SignatureInceptionOffset
- DnsServerDnsSecZoneSetting.SecureDelegationPollingPeriod
- DnsServerDnsSecZoneSetting.PropagationTime
- DnsServerDnsSecZoneSetting.ParentHasSecureDelegation
- DnsServerDnsSecZoneSetting.IsKeyMasterServer
- DnsServerDnsSecZoneSetting.KeyMasterServer
- DnsServerDnsSecZoneSetting.KeyMasterStatus
- DnsServerDnsSecZoneSetting.IsSigned
- DnsServerDnsSecZoneSetting.NSec3CurrentSalt
- DnsServerDnsSecZoneSetting.CurrentRollingSkdGuid
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DnsServerDnsSecZoneSetting class

Represents Domain Name System Security Extensions (DNSSEC) settings for a DNS zone.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerDnsSecZoneSetting
{
  String   ZoneName;
  String   DenialOfExistence;
  String   NSec3HashAlgorithm;
  Uint16   NSec3Iterations;
  boolean  NSec3OptOut;
  Uint8    NSec3RandomSaltLength;
  String   NSec3UserSalt;
  String   DistributeTrustAnchor[];
  boolean  EnableRfc5011KeyRollover;
  String   DSRecordGenerationAlgorithm[];
  datetime DSRecordSetTtl;
  datetime DnsKeyRecordSetTtl;
  datetime SignatureInceptionOffset;
  datetime SecureDelegationPollingPeriod;
  datetime PropagationTime;
  boolean  ParentHasSecureDelegation;
  boolean  IsKeyMasterServer;
  String   KeyMasterServer;
  String   KeyMasterStatus;
  boolean  IsSigned;
  String   NSec3CurrentSalt;
  String   CurrentRollingSkdGuid;
};
```

## Members

The **DnsServerDnsSecZoneSetting** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerDnsSecZoneSetting** class has these properties.

<dl> <dt>

**CurrentRollingSkdGuid**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The **GUID** of the currently rolling SKD.

**Windows Server 2012:** This property is supported beginning with Windows Server 2012 R2.

</dd> <dt>

**DenialOfExistence**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The setting used by the DNS server to provide signed proof of an unregistered name in the DNS database.

The possible values are.

<dt>

<span id="NSEC"></span><span id="nsec"></span>

**NSEC** ("NSEC")


</dt> <dd></dd> <dt>

<span id="NSEC3"></span><span id="nsec3"></span>

**NSEC3** ("NSEC3")


</dt> <dd></dd> </dl>

</dd> <dt>

**DistributeTrustAnchor**
</dt> <dd> <dl> <dt>

Data type: **String** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

An array that contains the types of trust anchors to publish when the DNS zone is signed.

The possible values are.

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

**None** ("None")


</dt> <dd></dd> <dt>

<span id="DnsKey"></span><span id="dnskey"></span><span id="DNSKEY"></span>

**DnsKey** ("DnsKey")


</dt> <dd></dd> </dl>

</dd> <dt>

**DnsKeyRecordSetTtl**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The time-to-live (TTL) value assigned to DNSKEY records when the DNS zone is signed.

</dd> <dt>

**DSRecordGenerationAlgorithm**
</dt> <dd> <dl> <dt>

Data type: **String** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

An array that contains strings that indicate the algorithms to use to write the dsset file when the DNS zone is signed.

The possible values are.

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

**None** ("None")


</dt> <dd></dd> <dt>

<span id="Sha1"></span><span id="sha1"></span><span id="SHA1"></span>

**Sha1** ("Sha1")


</dt> <dd></dd> <dt>

<span id="Sha256"></span><span id="sha256"></span><span id="SHA256"></span>

**Sha256** ("Sha256")


</dt> <dd></dd> <dt>

<span id="Sha384"></span><span id="sha384"></span><span id="SHA384"></span>

**Sha384** ("Sha384")


</dt> <dd></dd> </dl>

</dd> <dt>

**DSRecordSetTtl**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The time-to-live (TTL) value assigned to DS records when the DNS zone is signed.

</dd> <dt>

**EnableRfc5011KeyRollover**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether to maintain the DNS zone using key rollover procedures defined in RFC 5011.

</dd> <dt>

**IsKeyMasterServer**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If the current server is the key master server for the current zone.

</dd> <dt>

**IsSigned**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**True** if the current zone is signed; otherwise, **false**.

**Windows Server 2012:** This property is supported beginning with Windows Server 2012 R2.

</dd> <dt>

**KeyMasterServer**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The name of keymaster server for this zone.

</dd> <dt>

**KeyMasterStatus**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The status of the key master server for this zone.

The possible values are.

<dt>

<span id="Online"></span><span id="online"></span><span id="ONLINE"></span>

**Online** ("Online")


</dt> <dd></dd> <dt>

<span id="Offline"></span><span id="offline"></span><span id="OFFLINE"></span>

**Offline** ("Offline")


</dt> <dd></dd> </dl>

</dd> <dt>

**NSec3CurrentSalt**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current NSEC3 salt string used to sign the DNS zone.

**Windows Server 2012:** This property is supported beginning with Windows Server 2012 R2.

</dd> <dt>

**NSec3HashAlgorithm**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The NSEC3 salt string to use to sign the DNS zone.

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


</dt> <dd></dd> </dl>

</dd> <dt>

**NSec3Iterations**
</dt> <dd> <dl> <dt>

Data type: **Uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The number of NSEC3 hash iterations to perform when the DNS zone is signed.

</dd> <dt>

**NSec3OptOut**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**True** to sign the DNS zone using NSEC opt-out; otherwise, **false**.

</dd> <dt>

**NSec3RandomSaltLength**
</dt> <dd> <dl> <dt>

Data type: **Uint8**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The length, in bytes, of the random salt used when the DNS zone is signed.

</dd> <dt>

**NSec3UserSalt**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The user-specified NSEC3 salt string to use when the DNS zone is signed.

</dd> <dt>

**ParentHasSecureDelegation**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**True** if the parental delegation to the DNS zone is secure; otherwise, **false**.

</dd> <dt>

**PropagationTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The expected time, in seconds, required to propagate zone changes through Active Directory.

</dd> <dt>

**SecureDelegationPollingPeriod**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The duration, in seconds, between polling attempts for child zone key rollovers.

</dd> <dt>

**SignatureInceptionOffset**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates in seconds, how far in the past DNSSEC signature validity periods should begin when signing the DNS zone.

</dd> <dt>

**ZoneName**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the zone.

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

[DnsServerPSProvider Provider](dns-server-classes.md)
</dt> </dl>

 

 





