---
Description: 'TBD.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '93ee5184-3f1c-4168-93cc-e1a43dd24e37'
ms.prod: 'windows-server-dev'
ms.technology:
- 'internet-protocol-address-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'MSFT\_IPAM\_DnsResourceRecord class'
---

# MSFT\_IPAM\_DnsResourceRecord class

TBD

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("IPAMServerPSProvider"), AMENDMENT]
class MSFT_IPAM_DnsResourceRecord
{
  string   InstanceID;
  string   RecordName;
  string   ZoneName;
  uint16   RecordType;
  string   RecordClass;
  string   TimeToLive;
  datetime Timestamp;
  string   RecordData;
  string   AccessScopePath;
  boolean  IsInheritedAccessScope;
};
```

## Members

The **MSFT\_IPAM\_DnsResourceRecord** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_IPAM\_DnsResourceRecord** class has these properties.

<dl> <dt>

**AccessScopePath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Access scope path for the DNS resource record.

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Opaquely and uniquely identifies an instance of this class within the scope of the instantiating Namespace.

</dd> <dt>

**IsInheritedAccessScope**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether the access scope for the DNS resource record is inherited from parent.

</dd> <dt>

**RecordClass**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The class of the DNS resource record.

</dd> <dt>

**RecordData**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Record data for the DNS resource record.

</dd> <dt>

**RecordName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the name of the DNS resource record.

</dd> <dt>

**RecordType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the type of DNS resource record.

The possible values are.

<dt>

<span id="NONE"></span><span id="none"></span>

**NONE** (0)


</dt> <dd></dd> <dt>

<span id="A"></span><span id="a"></span>

**A** (1)


</dt> <dd></dd> <dt>

<span id="AAAA"></span><span id="aaaa"></span>

**AAAA** (2)


</dt> <dd></dd> <dt>

<span id="PTR"></span><span id="ptr"></span>

**PTR** (3)


</dt> <dd></dd> <dt>

<span id="SOA"></span><span id="soa"></span>

**SOA** (4)


</dt> <dd></dd> <dt>

<span id="NS"></span><span id="ns"></span>

**NS** (5)


</dt> <dd></dd> <dt>

<span id="CNAME"></span><span id="cname"></span>

**CNAME** (6)


</dt> <dd></dd> <dt>

<span id="DNAME"></span><span id="dname"></span>

**DNAME** (7)


</dt> <dd></dd> <dt>

<span id="MX"></span><span id="mx"></span>

**MX** (8)


</dt> <dd></dd> <dt>

<span id="SRV"></span><span id="srv"></span>

**SRV** (9)


</dt> <dd></dd> <dt>

<span id="TXT"></span><span id="txt"></span>

**TXT** (10)


</dt> <dd></dd> <dt>

<span id="AFSDB"></span><span id="afsdb"></span>

**AFSDB** (11)


</dt> <dd></dd> <dt>

<span id="ATMA"></span><span id="atma"></span>

**ATMA** (12)


</dt> <dd></dd> <dt>

<span id="DHCID"></span><span id="dhcid"></span>

**DHCID** (13)


</dt> <dd></dd> <dt>

<span id="HINFO"></span><span id="hinfo"></span>

**HINFO** (14)


</dt> <dd></dd> <dt>

<span id="ISDN"></span><span id="isdn"></span>

**ISDN** (15)


</dt> <dd></dd> <dt>

<span id="NAPTR"></span><span id="naptr"></span>

**NAPTR** (16)


</dt> <dd></dd> <dt>

<span id="RP"></span><span id="rp"></span>

**RP** (17)


</dt> <dd></dd> <dt>

<span id="RT"></span><span id="rt"></span>

**RT** (18)


</dt> <dd></dd> <dt>

<span id="WINS"></span><span id="wins"></span>

**WINS** (19)


</dt> <dd></dd> <dt>

<span id="WINSR"></span><span id="winsr"></span>

**WINSR** (20)


</dt> <dd></dd> <dt>

<span id="WKS"></span><span id="wks"></span>

**WKS** (21)


</dt> <dd></dd> <dt>

<span id="X25"></span><span id="x25"></span>

**X25** (22)


</dt> <dd></dd> </dl>

</dd> <dt>

**Timestamp**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The timestamp value for the DNS resource record.

</dd> <dt>

**TimeToLive**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The TTL value for the DNS resource record.

</dd> <dt>

**ZoneName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the name of the DNS zone to which this DNS resource record belongs.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\IPAM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>IPAMServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IPAMServerPSProvider.dll</dt> </dl> |



 

 




