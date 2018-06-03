---
title: DnsServerValidity class
description: Represents a set of validation results for a DNS server.
audience: developer
ms.assetid: 9c69b084-2b2d-4ef1-86af-d97dbece5478
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerValidity class
- DnsServerValidity class, described
topic_type:
- apiref
api_name:
- DnsServerValidity
- DnsServerValidity.IPAddress
- DnsServerValidity.Result
- DnsServerValidity.UdpTried
- DnsServerValidity.TcpTried
- DnsServerValidity.RoundTripTime
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DnsServerValidity class

Represents a set of validation results for a DNS server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerValidity
{
  string   IPAddress;
  string   Result;
  boolean  UdpTried;
  boolean  TcpTried;
  datetime RoundTripTime;
};
```

## Members

The **DnsServerValidity** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerValidity** class has these properties.

<dl> <dt>

**IPAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The IP address of DNS server.

</dd> <dt>

**Result**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The validation results.

The possible values are.

<dt>

<span id="Success"></span><span id="success"></span><span id="SUCCESS"></span>

**Success** ("Success")


</dt> <dd></dd> <dt>

<span id="InvalidAddress"></span><span id="invalidaddress"></span><span id="INVALIDADDRESS"></span>

**InvalidAddress** ("InvalidAddress")


</dt> <dd></dd> <dt>

<span id="Unreachable"></span><span id="unreachable"></span><span id="UNREACHABLE"></span>

**Unreachable** ("Unreachable")


</dt> <dd></dd> <dt>

<span id="NoResponse"></span><span id="noresponse"></span><span id="NORESPONSE"></span>

**NoResponse** ("NoResponse")


</dt> <dd></dd> <dt>

<span id="NotAuthoritativeForZone"></span><span id="notauthoritativeforzone"></span><span id="NOTAUTHORITATIVEFORZONE"></span>

**NotAuthoritativeForZone** ("NotAuthoritativeForZone")


</dt> <dd></dd> <dt>

<span id="IPV4NotSupported"></span><span id="ipv4notsupported"></span><span id="IPV4NOTSUPPORTED"></span>

**IPV4NotSupported** ("IPV4NotSupported")


</dt> <dd></dd> <dt>

<span id="IPV6NotSupported"></span><span id="ipv6notsupported"></span><span id="IPV6NOTSUPPORTED"></span>

**IPV6NotSupported** ("IPV6NotSupported")


</dt> <dd></dd> <dt>

<span id="UnknownError"></span><span id="unknownerror"></span><span id="UNKNOWNERROR"></span>

**UnknownError** ("UnknownError")


</dt> <dd></dd> </dl>

</dd> <dt>

**RoundTripTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The duration of the validation operation.

</dd> <dt>

**TcpTried**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**true** if TCP validation was performed on the server; otherwise, **false**.

</dd> <dt>

**UdpTried**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**true** if UDP validation was performed on the server; otherwise, **false**.

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

 

 





