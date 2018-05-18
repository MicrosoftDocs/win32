---
title: DnsServerZoneQueryStatistics class
description: Manages zone query statistics for the specified record type.
audience: developer
ms.assetid: '096180e0-2509-4dda-ad51-07fba90ae076'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DnsServerZoneQueryStatistics class", "DnsServerZoneQueryStatistics class, described"]
topic_type:
- apiref
api_name:
- DnsServerZoneQueryStatistics
- DnsServerZoneQueryStatistics.RecordType
- DnsServerZoneQueryStatistics.QueriesResponded
- DnsServerZoneQueryStatistics.QueriesReceived
- DnsServerZoneQueryStatistics.QueriesFailure
- DnsServerZoneQueryStatistics.QueriesNameError
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
---

# DnsServerZoneQueryStatistics class

Manages zone query statistics for the specified record type.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerZoneQueryStatistics
{
  string RecordType;
  uint64 QueriesResponded;
  uint64 QueriesReceived;
  uint64 QueriesFailure;
  uint64 QueriesNameError;
};
```

## Members

The **DnsServerZoneQueryStatistics** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerZoneQueryStatistics** class has these properties.

<dl> <dt>

**QueriesFailure**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of query responses that indicated server failures.

</dd> <dt>

**QueriesNameError**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of query responses that indicated a name error.

</dd> <dt>

**QueriesReceived**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of queries received for record type.

</dd> <dt>

**QueriesResponded**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of query responses sent for record type.

</dd> <dt>

**RecordType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The type of record for which to manage zone query statistics.

The possible values are.

<dt>

<span id="A"></span><span id="a"></span>

**A** ("ZONE\_STATS\_TYPE\_RECORD\_A")


</dt> <dd></dd> <dt>

<span id="AAAA"></span><span id="aaaa"></span>

**AAAA** ("ZONE\_STATS\_TYPE\_RECORD\_AAAA")


</dt> <dd></dd> <dt>

<span id="PTR"></span><span id="ptr"></span>

**PTR** ("ZONE\_STATS\_TYPE\_RECORD\_PTR")


</dt> <dd></dd> <dt>

<span id="CNAME"></span><span id="cname"></span>

**CNAME** ("ZONE\_STATS\_TYPE\_RECORD\_CNAME")


</dt> <dd></dd> <dt>

<span id="MX"></span><span id="mx"></span>

**MX** ("ZONE\_STATS\_TYPE\_RECORD\_MX")


</dt> <dd></dd> <dt>

<span id="AFSDB"></span><span id="afsdb"></span>

**AFSDB** ("ZONE\_STATS\_TYPE\_RECORD\_AFSDB")


</dt> <dd></dd> <dt>

<span id="ATMA"></span><span id="atma"></span>

**ATMA** ("ZONE\_STATS\_TYPE\_RECORD\_ATMA")


</dt> <dd></dd> <dt>

<span id="DHCID"></span><span id="dhcid"></span>

**DHCID** ("ZONE\_STATS\_TYPE\_RECORD\_DHCID")


</dt> <dd></dd> <dt>

<span id="DNAME"></span><span id="dname"></span>

**DNAME** ("ZONE\_STATS\_TYPE\_RECORD\_DNAME")


</dt> <dd></dd> <dt>

<span id="HINFO"></span><span id="hinfo"></span>

**HINFO** ("ZONE\_STATS\_TYPE\_RECORD\_HINFO")


</dt> <dd></dd> <dt>

<span id="ISDN"></span><span id="isdn"></span>

**ISDN** ("ZONE\_STATS\_TYPE\_RECORD\_ISDN")


</dt> <dd></dd> <dt>

<span id="MG"></span><span id="mg"></span>

**MG** ("ZONE\_STATS\_TYPE\_RECORD\_MG")


</dt> <dd></dd> <dt>

<span id="MB"></span><span id="mb"></span>

**MB** ("ZONE\_STATS\_TYPE\_RECORD\_MB")


</dt> <dd></dd> <dt>

<span id="MINFO"></span><span id="minfo"></span>

**MINFO** ("ZONE\_STATS\_TYPE\_RECORD\_MINFO")


</dt> <dd></dd> <dt>

<span id="NAPTR"></span><span id="naptr"></span>

**NAPTR** ("ZONE\_STATS\_TYPE\_RECORD\_NAPTR")


</dt> <dd></dd> <dt>

<span id="NXT"></span><span id="nxt"></span>

**NXT** ("ZONE\_STATS\_TYPE\_RECORD\_NXT")


</dt> <dd></dd> <dt>

<span id="KEY"></span><span id="key"></span>

**KEY** ("ZONE\_STATS\_TYPE\_RECORD\_KEY")


</dt> <dd></dd> <dt>

<span id="MR"></span><span id="mr"></span>

**MR** ("ZONE\_STATS\_TYPE\_RECORD\_MR")


</dt> <dd></dd> <dt>

<span id="RP"></span><span id="rp"></span>

**RP** ("ZONE\_STATS\_TYPE\_RECORD\_RP")


</dt> <dd></dd> <dt>

<span id="RT"></span><span id="rt"></span>

**RT** ("ZONE\_STATS\_TYPE\_RECORD\_RT")


</dt> <dd></dd> <dt>

<span id="SRV"></span><span id="srv"></span>

**SRV** ("ZONE\_STATS\_TYPE\_RECORD\_SRV")


</dt> <dd></dd> <dt>

<span id="SIG"></span><span id="sig"></span>

**SIG** ("ZONE\_STATS\_TYPE\_RECORD\_SIG")


</dt> <dd></dd> <dt>

<span id="TEXT"></span><span id="text"></span>

**TEXT** ("ZONE\_STATS\_TYPE\_RECORD\_TEXT")


</dt> <dd></dd> <dt>

<span id="WKS"></span><span id="wks"></span>

**WKS** ("ZONE\_STATS\_TYPE\_RECORD\_WKS")


</dt> <dd></dd> <dt>

<span id="X25"></span><span id="x25"></span>

**X25** ("ZONE\_STATS\_TYPE\_RECORD\_X25")


</dt> <dd></dd> <dt>

<span id="DNSKEY"></span><span id="dnskey"></span>

**DNSKEY** ("ZONE\_STATS\_TYPE\_RECORD\_DNSKEY")


</dt> <dd></dd> <dt>

<span id="DS"></span><span id="ds"></span>

**DS** ("ZONE\_STATS\_TYPE\_RECORD\_DS")


</dt> <dd></dd> <dt>

<span id="NS"></span><span id="ns"></span>

**NS** ("ZONE\_STATS\_TYPE\_RECORD\_NS")


</dt> <dd></dd> <dt>

<span id="SOA"></span><span id="soa"></span>

**SOA** ("ZONE\_STATS\_TYPE\_RECORD\_SOA")


</dt> <dd></dd> <dt>

<span id="ALL"></span><span id="all"></span>

**ALL** ("ZONE\_STATS\_TYPE\_RECORD\_ALL")


</dt> <dd></dd> <dt>

<span id="OTHERS"></span><span id="others"></span>

**OTHERS** ("ZONE\_STATS\_TYPE\_RECORD\_OTHERS")


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

 

 





