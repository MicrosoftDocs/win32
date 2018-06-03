---
title: DnsServerResourceRecord class
description: DNS Server Resource Record.
audience: developer
ms.assetid: eb36f338-10fe-48b4-927f-7c005b960ef7
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerResourceRecord class
- DnsServerResourceRecord class, described
topic_type:
- apiref
api_name:
- DnsServerResourceRecord
- DnsServerResourceRecord.DistinguishedName
- DnsServerResourceRecord.HostName
- DnsServerResourceRecord.RecordType
- DnsServerResourceRecord.RecordClass
- DnsServerResourceRecord.TimeToLive
- DnsServerResourceRecord.RecordData
- DnsServerResourceRecord.Timestamp
- DnsServerResourceRecord.Type
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DnsServerResourceRecord class

DNS Server Resource Record.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerResourceRecord : DnsDomain
{
  string                      DistinguishedName;
  string                      HostName;
  string                      RecordType;
  string                      RecordClass;
  datetime                    TimeToLive;
  DnsServerResourceRecordData RecordData;
  datetime                    Timestamp;
  uint16                      Type;
};
```

## Members

The **DnsServerResourceRecord** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerResourceRecord** class has these properties.

<dl> <dt>

**DistinguishedName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Lightweight Directory Access Protocol (LDAP) name of the domain.

This property is inherited from [**DnsDomain**](dnsdomain.md).

</dd> <dt>

**HostName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Host Name

</dd> <dt>

**RecordClass**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Class

The possible values are.

<dt>

<span id="IN"></span><span id="in"></span>

**IN** ("IN")


</dt> <dd></dd> <dt>

<span id="CSNET"></span><span id="csnet"></span>

**CSNET** ("CSNET")


</dt> <dd></dd> <dt>

<span id="CHAOS"></span><span id="chaos"></span>

**CHAOS** ("CHAOS")


</dt> <dd></dd> <dt>

<span id="Hesiod"></span><span id="hesiod"></span><span id="HESIOD"></span>

**Hesiod** ("Hesiod")


</dt> <dd></dd> </dl>

</dd> <dt>

**RecordData**
</dt> <dd> <dl> <dt>

Data type: **DnsServerResourceRecordData**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerResourceRecordData**](dnsserverresourcerecorddata.md)")
</dt> </dl>

Record Data

</dd> <dt>

**RecordType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Record Type

The possible values are.

<dt>

<span id="A"></span><span id="a"></span>

<span id="A"></span><span id="a"></span>**A** ("A")


</dt> <dd></dd> <dt>

<span id="Ns"></span><span id="ns"></span><span id="NS"></span>

<span id="Ns"></span><span id="ns"></span><span id="NS"></span>**Ns** ("Ns")


</dt> <dd></dd> <dt>

<span id="Md"></span><span id="md"></span><span id="MD"></span>

<span id="Md"></span><span id="md"></span><span id="MD"></span>**Md** ("Md")


</dt> <dd></dd> <dt>

<span id="Mf"></span><span id="mf"></span><span id="MF"></span>

<span id="Mf"></span><span id="mf"></span><span id="MF"></span>**Mf** ("Mf")


</dt> <dd></dd> <dt>

<span id="CName"></span><span id="cname"></span><span id="CNAME"></span>

<span id="CName"></span><span id="cname"></span><span id="CNAME"></span>**CName** ("CName")


</dt> <dd></dd> <dt>

<span id="Soa"></span><span id="soa"></span><span id="SOA"></span>

<span id="Soa"></span><span id="soa"></span><span id="SOA"></span>**Soa** ("Soa")


</dt> <dd></dd> <dt>

<span id="Mb"></span><span id="mb"></span><span id="MB"></span>

<span id="Mb"></span><span id="mb"></span><span id="MB"></span>**Mb** ("Mb")


</dt> <dd></dd> <dt>

<span id="Mg"></span><span id="mg"></span><span id="MG"></span>

<span id="Mg"></span><span id="mg"></span><span id="MG"></span>**Mg** ("Mg")


</dt> <dd></dd> <dt>

<span id="Mr"></span><span id="mr"></span><span id="MR"></span>

<span id="Mr"></span><span id="mr"></span><span id="MR"></span>**Mr** ("Mr")


</dt> <dd></dd> <dt>

<span id="Null"></span><span id="null"></span><span id="NULL"></span>

<span id="Null"></span><span id="null"></span><span id="NULL"></span>**Null** ("Null")


</dt> <dd></dd> <dt>

<span id="Wks"></span><span id="wks"></span><span id="WKS"></span>

<span id="Wks"></span><span id="wks"></span><span id="WKS"></span>**Wks** ("Wks")


</dt> <dd></dd> <dt>

<span id="Ptr"></span><span id="ptr"></span><span id="PTR"></span>

<span id="Ptr"></span><span id="ptr"></span><span id="PTR"></span>**Ptr** ("Ptr")


</dt> <dd></dd> <dt>

<span id="HInfo"></span><span id="hinfo"></span><span id="HINFO"></span>

<span id="HInfo"></span><span id="hinfo"></span><span id="HINFO"></span>**HInfo** ("HInfo")


</dt> <dd></dd> <dt>

<span id="MInfo"></span><span id="minfo"></span><span id="MINFO"></span>

<span id="MInfo"></span><span id="minfo"></span><span id="MINFO"></span>**MInfo** ("MInfo")


</dt> <dd></dd> <dt>

<span id="Mx"></span><span id="mx"></span><span id="MX"></span>

<span id="Mx"></span><span id="mx"></span><span id="MX"></span>**Mx** ("Mx")


</dt> <dd></dd> <dt>

<span id="Text"></span><span id="text"></span><span id="TEXT"></span>

<span id="Text"></span><span id="text"></span><span id="TEXT"></span>**Text** ("Text")


</dt> <dd></dd> <dt>

<span id="Rp"></span><span id="rp"></span><span id="RP"></span>

<span id="Rp"></span><span id="rp"></span><span id="RP"></span>**Rp** ("Rp")


</dt> <dd></dd> <dt>

<span id="Afsdb"></span><span id="afsdb"></span><span id="AFSDB"></span>

<span id="Afsdb"></span><span id="afsdb"></span><span id="AFSDB"></span>**Afsdb** ("Afsdb")


</dt> <dd></dd> <dt>

<span id="X25"></span><span id="x25"></span>

<span id="X25"></span><span id="x25"></span>**X25** ("X25")


</dt> <dd></dd> <dt>

<span id="Isdn"></span><span id="isdn"></span><span id="ISDN"></span>

<span id="Isdn"></span><span id="isdn"></span><span id="ISDN"></span>**Isdn** ("Isdn")


</dt> <dd></dd> <dt>

<span id="Rt"></span><span id="rt"></span><span id="RT"></span>

<span id="Rt"></span><span id="rt"></span><span id="RT"></span>**Rt** ("Rt")


</dt> <dd></dd> <dt>

<span id="Nsap"></span><span id="nsap"></span><span id="NSAP"></span>

<span id="Nsap"></span><span id="nsap"></span><span id="NSAP"></span>**Nsap** ("Nsap")


</dt> <dd></dd> <dt>

<span id="NsapPtr"></span><span id="nsapptr"></span><span id="NSAPPTR"></span>

<span id="NsapPtr"></span><span id="nsapptr"></span><span id="NSAPPTR"></span>**NsapPtr** ("NsapPtr")


</dt> <dd></dd> <dt>

<span id="Sig"></span><span id="sig"></span><span id="SIG"></span>

<span id="Sig"></span><span id="sig"></span><span id="SIG"></span>**Sig** ("Sig")


</dt> <dd></dd> <dt>

<span id="Key"></span><span id="key"></span><span id="KEY"></span>

<span id="Key"></span><span id="key"></span><span id="KEY"></span>**Key** ("Key")


</dt> <dd></dd> <dt>

<span id="Px"></span><span id="px"></span><span id="PX"></span>

<span id="Px"></span><span id="px"></span><span id="PX"></span>**Px** ("Px")


</dt> <dd></dd> <dt>

<span id="Gpos"></span><span id="gpos"></span><span id="GPOS"></span>

<span id="Gpos"></span><span id="gpos"></span><span id="GPOS"></span>**Gpos** ("Gpos")


</dt> <dd></dd> <dt>

<span id="AAAA"></span><span id="aaaa"></span>

<span id="AAAA"></span><span id="aaaa"></span>**AAAA** ("AAAA")


</dt> <dd></dd> <dt>

<span id="Loc"></span><span id="loc"></span><span id="LOC"></span>

<span id="Loc"></span><span id="loc"></span><span id="LOC"></span>**Loc** ("Loc")


</dt> <dd></dd> <dt>

<span id="Nxt"></span><span id="nxt"></span><span id="NXT"></span>

<span id="Nxt"></span><span id="nxt"></span><span id="NXT"></span>**Nxt** ("Nxt")


</dt> <dd></dd> <dt>

<span id="Eid"></span><span id="eid"></span><span id="EID"></span>

<span id="Eid"></span><span id="eid"></span><span id="EID"></span>**Eid** ("Eid")


</dt> <dd></dd> <dt>

<span id="NimLoc"></span><span id="nimloc"></span><span id="NIMLOC"></span>

<span id="NimLoc"></span><span id="nimloc"></span><span id="NIMLOC"></span>**NimLoc** ("NimLoc")


</dt> <dd></dd> <dt>

<span id="Srv"></span><span id="srv"></span><span id="SRV"></span>

<span id="Srv"></span><span id="srv"></span><span id="SRV"></span>**Srv** ("Srv")


</dt> <dd></dd> <dt>

<span id="Atma"></span><span id="atma"></span><span id="ATMA"></span>

<span id="Atma"></span><span id="atma"></span><span id="ATMA"></span>**Atma** ("Atma")


</dt> <dd></dd> <dt>

<span id="Naptr"></span><span id="naptr"></span><span id="NAPTR"></span>

<span id="Naptr"></span><span id="naptr"></span><span id="NAPTR"></span>**Naptr** ("Naptr")


</dt> <dd></dd> <dt>

<span id="Kx"></span><span id="kx"></span><span id="KX"></span>

<span id="Kx"></span><span id="kx"></span><span id="KX"></span>**Kx** ("Kx")


</dt> <dd></dd> <dt>

<span id="Cert"></span><span id="cert"></span><span id="CERT"></span>

<span id="Cert"></span><span id="cert"></span><span id="CERT"></span>**Cert** ("Cert")


</dt> <dd></dd> <dt>

<span id="A6"></span><span id="a6"></span>

<span id="A6"></span><span id="a6"></span>**A6** ("A6")


</dt> <dd></dd> <dt>

<span id="DName"></span><span id="dname"></span><span id="DNAME"></span>

<span id="DName"></span><span id="dname"></span><span id="DNAME"></span>**DName** ("DName")


</dt> <dd></dd> <dt>

<span id="Sink"></span><span id="sink"></span><span id="SINK"></span>

<span id="Sink"></span><span id="sink"></span><span id="SINK"></span>**Sink** ("Sink")


</dt> <dd></dd> <dt>

<span id="Opt"></span><span id="opt"></span><span id="OPT"></span>

<span id="Opt"></span><span id="opt"></span><span id="OPT"></span>**Opt** ("Opt")


</dt> <dd></dd> <dt>

<span id="Ds"></span><span id="ds"></span><span id="DS"></span>

<span id="Ds"></span><span id="ds"></span><span id="DS"></span>**Ds** ("Ds")


</dt> <dd></dd> <dt>

<span id="Rrsig"></span><span id="rrsig"></span><span id="RRSIG"></span>

<span id="Rrsig"></span><span id="rrsig"></span><span id="RRSIG"></span>**Rrsig** ("Rrsig")


</dt> <dd></dd> <dt>

<span id="NSEC"></span><span id="nsec"></span>

<span id="NSEC"></span><span id="nsec"></span>**NSEC** ("NSEC")


</dt> <dd></dd> <dt>

<span id="DnsKey"></span><span id="dnskey"></span><span id="DNSKEY"></span>

<span id="DnsKey"></span><span id="dnskey"></span><span id="DNSKEY"></span>**DnsKey** ("DnsKey")


</dt> <dd></dd> <dt>

<span id="DhcId"></span><span id="dhcid"></span><span id="DHCID"></span>

<span id="DhcId"></span><span id="dhcid"></span><span id="DHCID"></span>**DhcId** ("DhcId")


</dt> <dd></dd> <dt>

<span id="Wins"></span><span id="wins"></span><span id="WINS"></span>

<span id="Wins"></span><span id="wins"></span><span id="WINS"></span>**Wins** ("Wins")


</dt> <dd></dd> <dt>

<span id="WinsR"></span><span id="winsr"></span><span id="WINSR"></span>

<span id="WinsR"></span><span id="winsr"></span><span id="WINSR"></span>**WinsR** ("WinsR")


</dt> <dd></dd> <dt>

<span id="TLSA"></span><span id="tlsa"></span>

<span id="TLSA"></span><span id="tlsa"></span>**TLSA** ("TLSA")


</dt> <dd>

**Windows Server 2012 R2 and Windows Server 2012:** Not supported.

</dd> <dt>

<span id="UNKNOWN"></span><span id="unknown"></span>

<span id="UNKNOWN"></span><span id="unknown"></span>**UNKNOWN** ("UNKNOWN")


</dt> <dd>

**Windows Server 2012 R2 and Windows Server 2012:** Not supported.

</dd> </dl>

</dd> <dt>

**Timestamp**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Time at which Resource Record was refreshed. Expressed in hours since January 1, 1601, Greenwich Mean Time (GMT)

</dd> <dt>

**TimeToLive**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Time To Live in seconds

</dd> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Type for Unknown record.

**Windows Server 2012 R2 and Windows Server 2012:** Not supported.

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

[**DnsDomain**](dnsdomain.md)
</dt> <dt>

[DnsServerPSProvider Provider](dns-server-classes.md)
</dt> </dl>

 

 





