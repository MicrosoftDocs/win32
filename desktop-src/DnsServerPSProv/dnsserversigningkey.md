---
title: DnsServerSigningKey class
description: Represents a signing key for zone signing and key signing on a DNS server.
audience: developer
ms.assetid: 4c72a317-31aa-4833-9328-532c082141c6
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerSigningKey class
- DnsServerSigningKey class, described
topic_type:
- apiref
api_name:
- DnsServerSigningKey
- DnsServerSigningKey.ZoneName
- DnsServerSigningKey.KeyId
- DnsServerSigningKey.KeyType
- DnsServerSigningKey.CurrentState
- DnsServerSigningKey.KeyStorageProvider
- DnsServerSigningKey.StoreKeysInAD
- DnsServerSigningKey.CryptoAlgorithm
- DnsServerSigningKey.KeyLength
- DnsServerSigningKey.DnsKeySignatureValidityPeriod
- DnsServerSigningKey.DSSignatureValidityPeriod
- DnsServerSigningKey.ZoneSignatureValidityPeriod
- DnsServerSigningKey.InitialRolloverOffset
- DnsServerSigningKey.RolloverPeriod
- DnsServerSigningKey.RolloverType
- DnsServerSigningKey.NextRolloverAction
- DnsServerSigningKey.LastRolloverTime
- DnsServerSigningKey.NextRolloverTime
- DnsServerSigningKey.CurrentRolloverStatus
- DnsServerSigningKey.ActiveKey
- DnsServerSigningKey.StandbyKey
- DnsServerSigningKey.NextKey
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DnsServerSigningKey class

Represents a signing key for zone signing and key signing on a DNS server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerSigningKey
{
  String   ZoneName;
  String   KeyId;
  String   KeyType;
  String   CurrentState;
  String   KeyStorageProvider;
  boolean  StoreKeysInAD;
  String   CryptoAlgorithm;
  Uint32   KeyLength;
  datetime DnsKeySignatureValidityPeriod;
  datetime DSSignatureValidityPeriod;
  datetime ZoneSignatureValidityPeriod;
  datetime InitialRolloverOffset;
  datetime RolloverPeriod;
  String   RolloverType;
  String   NextRolloverAction;
  datetime LastRolloverTime;
  datetime NextRolloverTime;
  String   CurrentRolloverStatus;
  String   ActiveKey;
  String   StandbyKey;
  String   NextKey;
};
```

## Members

The **DnsServerSigningKey** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerSigningKey** class has these properties.

<dl> <dt>

**ActiveKey**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A pointer string for the active key.

</dd> <dt>

**CryptoAlgorithm**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The type of DNSSEC signature generation algorithm used by the key.

The possible values are.

<dt>

<span id="RsaSha1"></span><span id="rsasha1"></span><span id="RSASHA1"></span>

**RsaSha1** ("RsaSha1")


</dt> <dd></dd> <dt>

<span id="RsaSha1NSec3"></span><span id="rsasha1nsec3"></span><span id="RSASHA1NSEC3"></span>

**RsaSha1NSec3** ("RsaSha1NSec3")


</dt> <dd></dd> <dt>

<span id="RsaSha256"></span><span id="rsasha256"></span><span id="RSASHA256"></span>

**RsaSha256** ("RsaSha256")


</dt> <dd></dd> <dt>

<span id="RsaSha512"></span><span id="rsasha512"></span><span id="RSASHA512"></span>

**RsaSha512** ("RsaSha512")


</dt> <dd></dd> <dt>

<span id="ECDsaP256Sha256"></span><span id="ecdsap256sha256"></span><span id="ECDSAP256SHA256"></span>

**ECDsaP256Sha256** ("ECDsaP256Sha256")


</dt> <dd></dd> <dt>

<span id="ECDsaP384Sha384"></span><span id="ecdsap384sha384"></span><span id="ECDSAP384SHA384"></span>

**ECDsaP384Sha384** ("ECDsaP384Sha384")


</dt> <dd></dd> </dl>

</dd> <dt>

**CurrentRolloverStatus**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The state of the key.

The possible values are.

<dt>

<span id="NotRolling"></span><span id="notrolling"></span><span id="NOTROLLING"></span>

**NotRolling** ("NotRolling")


</dt> <dd></dd> <dt>

<span id="Queued"></span><span id="queued"></span><span id="QUEUED"></span>

**Queued** ("Queued")


</dt> <dd></dd> <dt>

<span id="RollStarted"></span><span id="rollstarted"></span><span id="ROLLSTARTED"></span>

**RollStarted** ("RollStarted")


</dt> <dd></dd> <dt>

<span id="ZskWaitingForDnsKeyTtl"></span><span id="zskwaitingfordnskeyttl"></span><span id="ZSKWAITINGFORDNSKEYTTL"></span>

**ZskWaitingForDnsKeyTtl** ("ZskWaitingForDnsKeyTtl")


</dt> <dd></dd> <dt>

<span id="ZskWaitingForMaxZoneTtlKskWaitingForDSUpdate"></span><span id="zskwaitingformaxzonettlkskwaitingfordsupdate"></span><span id="ZSKWAITINGFORMAXZONETTLKSKWAITINGFORDSUPDATE"></span>

**ZskWaitingForMaxZoneTtlKskWaitingForDSUpdate** ("ZskWaitingForMaxZoneTtlKskWaitingForDSUpdate")


</dt> <dd></dd> <dt>

<span id="KskWaitingForDSTtl"></span><span id="kskwaitingfordsttl"></span><span id="KSKWAITINGFORDSTTL"></span>

**KskWaitingForDSTtl** ("KskWaitingForDSTtl")


</dt> <dd></dd> <dt>

<span id="KskWaitingForDnsKeyTtl"></span><span id="kskwaitingfordnskeyttl"></span><span id="KSKWAITINGFORDNSKEYTTL"></span>

**KskWaitingForDnsKeyTtl** ("KskWaitingForDnsKeyTtl")


</dt> <dd></dd> <dt>

<span id="WaitingForRFC5011RemoveHoldDown"></span><span id="waitingforrfc5011removeholddown"></span><span id="WAITINGFORRFC5011REMOVEHOLDDOWN"></span>

**WaitingForRFC5011RemoveHoldDown** ("WaitingForRFC5011RemoveHoldDown")


</dt> <dd></dd> <dt>

<span id="RollError"></span><span id="rollerror"></span><span id="ROLLERROR"></span>

**RollError** ("RollError")


</dt> <dd></dd> </dl>

</dd> <dt>

**CurrentState**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The state of the key.

The possible values are.

<dt>

<span id="Active"></span><span id="active"></span><span id="ACTIVE"></span>

**Active** ("Active")


</dt> <dd></dd> <dt>

<span id="Retired"></span><span id="retired"></span><span id="RETIRED"></span>

**Retired** ("Retired")


</dt> <dd></dd> </dl>

</dd> <dt>

**DnsKeySignatureValidityPeriod**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The duration in which the signatures that cover DNSKEY record sets are valid.

</dd> <dt>

**DSSignatureValidityPeriod**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The duration in which the signatures that cover DS record sets are valid.

</dd> <dt>

**InitialRolloverOffset**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The duration for which the first scheduled key rollover is delayed. This allows key rollovers to be staggered.

</dd> <dt>

**KeyId**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The unique identifier of the key.

</dd> <dt>

**KeyLength**
</dt> <dd> <dl> <dt>

Data type: **Uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The length, in bits, of the key. The length ranges from 1024 to 4096, in 64 bit increments.

</dd> <dt>

**KeyStorageProvider**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The Key Storage Provider (KSP) used to generate keys.

</dd> <dt>

**KeyType**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The type of the key.

The possible values are.

<dt>

<span id="ZoneSigningKey"></span><span id="zonesigningkey"></span><span id="ZONESIGNINGKEY"></span>

**ZoneSigningKey** ("ZoneSigningKey")


</dt> <dd></dd> <dt>

<span id="KeySigningKey"></span><span id="keysigningkey"></span><span id="KEYSIGNINGKEY"></span>

**KeySigningKey** ("KeySigningKey")


</dt> <dd></dd> </dl>

</dd> <dt>

**LastRolloverTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time at which the last rollover event was performed.

</dd> <dt>

**NextKey**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A pointer string for the next key. This key will be used during the next key rollover event.

</dd> <dt>

**NextRolloverAction**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The action to take for the next key rollover event.

The possible values are.

<dt>

<span id="Normal"></span><span id="normal"></span><span id="NORMAL"></span>

**Normal** ("Normal")


</dt> <dd></dd> <dt>

<span id="RevokeStandby"></span><span id="revokestandby"></span><span id="REVOKESTANDBY"></span>

**RevokeStandby** ("RevokeStandby")


</dt> <dd></dd> <dt>

<span id="Retire"></span><span id="retire"></span><span id="RETIRE"></span>

**Retire** ("Retire")


</dt> <dd></dd> </dl>

</dd> <dt>

**NextRolloverTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time at which the next rollover action must take place.

</dd> <dt>

**RolloverPeriod**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The duration between scheduled key rollovers.

</dd> <dt>

**RolloverType**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The key rollover type.

The possible values are.

<dt>

<span id="DoubleSignature"></span><span id="doublesignature"></span><span id="DOUBLESIGNATURE"></span>

**DoubleSignature** ("DoubleSignature")


</dt> <dd></dd> <dt>

<span id="Prepublish"></span><span id="prepublish"></span><span id="PREPUBLISH"></span>

**Prepublish** ("Prepublish")


</dt> <dd></dd> </dl>

</dd> <dt>

**StandbyKey**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A pointer string for the standby key.

</dd> <dt>

**StoreKeysInAD**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**true** if the key is stored in a zone object in Active Directory; otherwise, **false**.

</dd> <dt>

**ZoneName**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the zone to which the key is assigned.

</dd> <dt>

**ZoneSignatureValidityPeriod**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The duration in which the signatures that cover all other record sets are valid.

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

 

 





