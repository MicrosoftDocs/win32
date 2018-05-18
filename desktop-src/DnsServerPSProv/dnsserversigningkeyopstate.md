---
title: DnsServerSigningKeyOpState class
description: Represents the signing key operational state of a DNS server.
audience: developer
ms.assetid: '5a4fbe85-7d82-4311-9a23-2a801014d52a'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DnsServerSigningKeyOpState class", "DnsServerSigningKeyOpState class, described"]
topic_type:
- apiref
api_name:
- DnsServerSigningKeyOpState
- DnsServerSigningKeyOpState.CurrentRollState
- DnsServerSigningKeyOpState.ManualTrigger
- DnsServerSigningKeyOpState.PreRollEventFired
- DnsServerSigningKeyOpState.NextKeyGenerationTime
- DnsServerSigningKeyOpState.RevokedOrSwappedDnsKeys
- DnsServerSigningKeyOpState.FinalDnsKeys
- DnsServerSigningKeyOpState.ActiveKeyScope
- DnsServerSigningKeyOpState.StandbyKeyScope
- DnsServerSigningKeyOpState.NextKeyScope
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
---

# DnsServerSigningKeyOpState class

Represents the signing key operational state of a DNS server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerSigningKeyOpState
{
  Uint16                  CurrentRollState;
  boolean                 ManualTrigger;
  Uint16                  PreRollEventFired;
  datetime                NextKeyGenerationTime;
  DnsServerResourceRecord RevokedOrSwappedDnsKeys[];
  DnsServerResourceRecord FinalDnsKeys[];
  String                  ActiveKeyScope;
  String                  StandbyKeyScope;
  String                  NextKeyScope;
};
```

## Members

The **DnsServerSigningKeyOpState** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerSigningKeyOpState** class has these properties.

<dl> <dt>

**ActiveKeyScope**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The scope of the active key.

The possible values are.

<dt>

<span id="Default"></span><span id="default"></span><span id="DEFAULT"></span>

**Default** ("Default")


</dt> <dd></dd> <dt>

<span id="DnsKeyOnly"></span><span id="dnskeyonly"></span><span id="DNSKEYONLY"></span>

**DnsKeyOnly** ("DnsKeyOnly")


</dt> <dd></dd> <dt>

<span id="AllRecords"></span><span id="allrecords"></span><span id="ALLRECORDS"></span>

**AllRecords** ("AllRecords")


</dt> <dd></dd> <dt>

<span id="AddOnly"></span><span id="addonly"></span><span id="ADDONLY"></span>

**AddOnly** ("AddOnly")


</dt> <dd></dd> <dt>

<span id="DoNotPublish"></span><span id="donotpublish"></span><span id="DONOTPUBLISH"></span>

**DoNotPublish** ("DoNotPublish")


</dt> <dd></dd> <dt>

<span id="Revoked"></span><span id="revoked"></span><span id="REVOKED"></span>

**Revoked** ("Revoked")


</dt> <dd></dd> </dl>

</dd> <dt>

**CurrentRollState**
</dt> <dd> <dl> <dt>

Data type: **Uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The rollover status of the DNS server.

</dd> <dt>

**FinalDnsKeys**
</dt> <dd> <dl> <dt>

Data type: **DnsServerResourceRecord** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerResourceRecord**](dnsserverresourcerecord.md)")
</dt> </dl>

An array that contains the pre-signed DNSKEY resource record list for post-rollover operations.

</dd> <dt>

**ManualTrigger**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**true** to enable the manual trigger; otherwise, **false**.

</dd> <dt>

**NextKeyGenerationTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time when the next key was added to the zone.

</dd> <dt>

**NextKeyScope**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The scope of the next key.

The possible values are.

<dt>

<span id="Default"></span><span id="default"></span><span id="DEFAULT"></span>

**Default** ("Default")


</dt> <dd></dd> <dt>

<span id="DnsKeyOnly"></span><span id="dnskeyonly"></span><span id="DNSKEYONLY"></span>

**DnsKeyOnly** ("DnsKeyOnly")


</dt> <dd></dd> <dt>

<span id="AllRecords"></span><span id="allrecords"></span><span id="ALLRECORDS"></span>

**AllRecords** ("AllRecords")


</dt> <dd></dd> <dt>

<span id="AddOnly"></span><span id="addonly"></span><span id="ADDONLY"></span>

**AddOnly** ("AddOnly")


</dt> <dd></dd> <dt>

<span id="DoNotPublish"></span><span id="donotpublish"></span><span id="DONOTPUBLISH"></span>

**DoNotPublish** ("DoNotPublish")


</dt> <dd></dd> <dt>

<span id="Revoked"></span><span id="revoked"></span><span id="REVOKED"></span>

**Revoked** ("Revoked")


</dt> <dd></dd> </dl>

</dd> <dt>

**PreRollEventFired**
</dt> <dd> <dl> <dt>

Data type: **Uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The pre-rollover events that were initiated for Key Signing Keys (KSK).

</dd> <dt>

**RevokedOrSwappedDnsKeys**
</dt> <dd> <dl> <dt>

Data type: **DnsServerResourceRecord** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerResourceRecord**](dnsserverresourcerecord.md)")
</dt> </dl>

An array that contains the pre-signed DNSKEY resource record list for KSK revoke or ZSK swap operations.

</dd> <dt>

**StandbyKeyScope**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The scope of the standby key.

The possible values are.

<dt>

<span id="Default"></span><span id="default"></span><span id="DEFAULT"></span>

**Default** ("Default")


</dt> <dd></dd> <dt>

<span id="DnsKeyOnly"></span><span id="dnskeyonly"></span><span id="DNSKEYONLY"></span>

**DnsKeyOnly** ("DnsKeyOnly")


</dt> <dd></dd> <dt>

<span id="AllRecords"></span><span id="allrecords"></span><span id="ALLRECORDS"></span>

**AllRecords** ("AllRecords")


</dt> <dd></dd> <dt>

<span id="AddOnly"></span><span id="addonly"></span><span id="ADDONLY"></span>

**AddOnly** ("AddOnly")


</dt> <dd></dd> <dt>

<span id="DoNotPublish"></span><span id="donotpublish"></span><span id="DONOTPUBLISH"></span>

**DoNotPublish** ("DoNotPublish")


</dt> <dd></dd> <dt>

<span id="Revoked"></span><span id="revoked"></span><span id="REVOKED"></span>

**Revoked** ("Revoked")


</dt> <dd></dd> </dl>

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

[DnsServerPSProvider Provider](dns-server-classes.md)
</dt> </dl>

 

 





