---
title: Get method of the PS\_DnsServerResourceRecord class
description: Retrieve resource record from a specified zone.
audience: developer
ms.assetid: 4d817943-7cdc-4894-a469-235d864f2f82
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_DnsServerResourceRecord class
- PS_DnsServerResourceRecord class, Get method
topic_type:
- apiref
api_name:
- PS_DnsServerResourceRecord.Get
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Get method of the PS\_DnsServerResourceRecord class

Retrieve resource record from a specified zone.

## Syntax


```mof
uint32 Get(
  [in]  string                  Name,
  [in]  string                  ComputerName,
  [in]  string                  ZoneName,
  [in]  boolean                 Node,
  [in]  string                  ZoneScope,
  [in]  string                  VirtualizationInstance,
  [in]  string                  RRType,
  [out] DnsServerResourceRecord cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name of the record to be retrieved.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command.

</dd> <dt>

*ZoneName* \[in\]
</dt> <dd>

Specifies the name of the zone.

</dd> <dt>

*Node* \[in\]
</dt> <dd>

If specified, returns only the parameters at root of *Name.*

</dd> <dt>

*ZoneScope* \[in\]
</dt> <dd>

Name of the zone scope.

**Windows Server 2012:** Not supported.

</dd> <dt>

*VirtualizationInstance* \[in\]
</dt> <dd>

Unique identifier of the virtualization instance.

**Windows Server 2012 R2 and Windows Server 2012:** This parameter is not supported before Windows Server 2016.

</dd> <dt>

*RRType* \[in\]
</dt> <dd>

The type of resource record to delete.

The possible values are.

<dt>

<span id="A"></span><span id="a"></span>

<span id="A"></span><span id="a"></span>**A** ("A")


</dt> <dd></dd> <dt>

<span id="Ns"></span><span id="ns"></span><span id="NS"></span>

<span id="Ns"></span><span id="ns"></span><span id="NS"></span>**Ns** ("Ns")


</dt> <dd></dd> <dt>

<span id="CName"></span><span id="cname"></span><span id="CNAME"></span>

<span id="CName"></span><span id="cname"></span><span id="CNAME"></span>**CName** ("CName")


</dt> <dd></dd> <dt>

<span id="Wks"></span><span id="wks"></span><span id="WKS"></span>

<span id="Wks"></span><span id="wks"></span><span id="WKS"></span>**Wks** ("Wks")


</dt> <dd></dd> <dt>

<span id="Ptr"></span><span id="ptr"></span><span id="PTR"></span>

<span id="Ptr"></span><span id="ptr"></span><span id="PTR"></span>**Ptr** ("Ptr")


</dt> <dd>

> [!Note]  
> There is a leading space in this value.

 

</dd> <dt>

<span id="HInfo"></span><span id="hinfo"></span><span id="HINFO"></span>

<span id="HInfo"></span><span id="hinfo"></span><span id="HINFO"></span>**HInfo** ("HInfo")


</dt> <dd></dd> <dt>

<span id="Mx"></span><span id="mx"></span><span id="MX"></span>

<span id="Mx"></span><span id="mx"></span><span id="MX"></span>**Mx** ("Mx")


</dt> <dd></dd> <dt>

<span id="Txt"></span><span id="txt"></span><span id="TXT"></span>

<span id="Txt"></span><span id="txt"></span><span id="TXT"></span>**Txt** ("Txt")


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

<span id="AAAA"></span><span id="aaaa"></span>

<span id="AAAA"></span><span id="aaaa"></span>**AAAA** ("AAAA")


</dt> <dd></dd> <dt>

<span id="Srv"></span><span id="srv"></span><span id="SRV"></span>

<span id="Srv"></span><span id="srv"></span><span id="SRV"></span>**Srv** ("Srv")


</dt> <dd></dd> <dt>

<span id="Atma"></span><span id="atma"></span><span id="ATMA"></span>

<span id="Atma"></span><span id="atma"></span><span id="ATMA"></span>**Atma** ("Atma")


</dt> <dd></dd> <dt>

<span id="DName"></span><span id="dname"></span><span id="DNAME"></span>

<span id="DName"></span><span id="dname"></span><span id="DNAME"></span>**DName** ("DName")


</dt> <dd></dd> <dt>

<span id="Ds"></span><span id="ds"></span><span id="DS"></span>

<span id="Ds"></span><span id="ds"></span><span id="DS"></span>**Ds** ("Ds")


</dt> <dd></dd> <dt>

<span id="Rrsig"></span><span id="rrsig"></span><span id="RRSIG"></span>

<span id="Rrsig"></span><span id="rrsig"></span><span id="RRSIG"></span>**Rrsig** ("Rrsig")


</dt> <dd></dd> <dt>

<span id="Nsec"></span><span id="nsec"></span><span id="NSEC"></span>

<span id="Nsec"></span><span id="nsec"></span><span id="NSEC"></span>**Nsec** ("Nsec")


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

<span id="Tlsa"></span><span id="tlsa"></span><span id="TLSA"></span>

<span id="Tlsa"></span><span id="tlsa"></span><span id="TLSA"></span>**Tlsa** ("Tlsa")


</dt> <dd>

**Windows Server 2012 R2 and Windows Server 2012:** Not supported.

</dd> </dl> </dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Receives an embedded instance of the [**DnsServerResourceRecord**](dnsserverresourcerecord.md) class.

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

[**PS\_DnsServerResourceRecord**](ps-dnsserverresourcerecord.md)
</dt> </dl>

 

 





