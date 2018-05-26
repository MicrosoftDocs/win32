---
title: DnsServerTrustAnchor class
description: Represents a trust anchor.
audience: developer
ms.assetid: 646e0b50-8322-4ec0-88b3-68e6cfb6c581
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerTrustAnchor class
- DnsServerTrustAnchor class, described
topic_type:
- apiref
api_name:
- DnsServerTrustAnchor
- DnsServerTrustAnchor.TrustAnchorName
- DnsServerTrustAnchor.TrustAnchorType
- DnsServerTrustAnchor.KeyTag
- DnsServerTrustAnchor.TrustAnchorState
- DnsServerTrustAnchor.EnteredStateTime
- DnsServerTrustAnchor.NextStateTime
- DnsServerTrustAnchor.TrustAnchorData
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DnsServerTrustAnchor class

Represents a trust anchor.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerTrustAnchor
{
  string                      TrustAnchorName;
  string                      TrustAnchorType;
  uint16                      KeyTag;
  string                      TrustAnchorState;
  datetime                    EnteredStateTime;
  datetime                    NextStateTime;
  DnsServerResourceRecordData TrustAnchorData;
};
```

## Members

The **DnsServerTrustAnchor** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerTrustAnchor** class has these properties.

<dl> <dt>

**EnteredStateTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time at which the current RFC5011 state was entered.

</dd> <dt>

**KeyTag**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The key tag of the DNSKEY resource record referred to by the current DS record.

</dd> <dt>

**NextStateTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

For a TA in the AddPend state, the time at which the TA may become Valid. For a TA in the Revoked state, the time at which the revoked key is eligible to be automatically removed. For all other states, this time is undefined and must be ignored and will be set to null.

</dd> <dt>

**TrustAnchorData**
</dt> <dd> <dl> <dt>

Data type: **DnsServerResourceRecordData**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerResourceRecordData**](dnsserverresourcerecorddata.md)")
</dt> </dl>

The DNSKEY or DS record data for the trust anchor.

</dd> <dt>

**TrustAnchorName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the trust anchor.

</dd> <dt>

**TrustAnchorState**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Trust anchor state.

The possible values are.

<dt>

<span id="Initialized"></span><span id="initialized"></span><span id="INITIALIZED"></span>

**Initialized** ("Initialized")


</dt> <dd></dd> <dt>

<span id="DSPending"></span><span id="dspending"></span><span id="DSPENDING"></span>

**DSPending** ("DSPending")


</dt> <dd></dd> <dt>

<span id="DSInvalid"></span><span id="dsinvalid"></span><span id="DSINVALID"></span>

**DSInvalid** ("DSInvalid")


</dt> <dd></dd> <dt>

<span id="AddPending"></span><span id="addpending"></span><span id="ADDPENDING"></span>

**AddPending** ("AddPending")


</dt> <dd></dd> <dt>

<span id="Valid"></span><span id="valid"></span><span id="VALID"></span>

**Valid** ("Valid")


</dt> <dd></dd> <dt>

<span id="Missing"></span><span id="missing"></span><span id="MISSING"></span>

**Missing** ("Missing")


</dt> <dd></dd> <dt>

<span id="Revoked"></span><span id="revoked"></span><span id="REVOKED"></span>

**Revoked** ("Revoked")


</dt> <dd></dd> <dt>

<span id="Deleted"></span><span id="deleted"></span><span id="DELETED"></span>

**Deleted** ("Deleted")


</dt> <dd></dd> </dl>

</dd> <dt>

**TrustAnchorType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The trust anchor type.

The possible values are.

<dt>

<span id="DnsKey"></span><span id="dnskey"></span><span id="DNSKEY"></span>

**DnsKey** ("DnsKey")


</dt> <dd></dd> <dt>

<span id="DS"></span><span id="ds"></span>

**DS** ("DS")


</dt> <dd></dd> </dl>

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

 

 





