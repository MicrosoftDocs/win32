---
title: DhcpServerv4Lease class
description: Dhcp Server v4 Client Lease.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '18336129-b5f5-4aeb-94ec-d1e6da88b590'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DhcpServerv4Lease class", "DhcpServerv4Lease class, described"]
topic_type:
- apiref
api_name:
- DhcpServerv4Lease
- DhcpServerv4Lease.AddressState
- DhcpServerv4Lease.IPAddress
- DhcpServerv4Lease.ScopeId
- DhcpServerv4Lease.Description
- DhcpServerv4Lease.ClientId
- DhcpServerv4Lease.HostName
- DhcpServerv4Lease.ClientType
- DhcpServerv4Lease.LeaseExpiryTime
- DhcpServerv4Lease.NapCapable
- DhcpServerv4Lease.NapStatus
- DhcpServerv4Lease.ProbationEnds
- DhcpServerv4Lease.PolicyName
- DhcpServerv4Lease.DnsRR
- DhcpServerv4Lease.DnsRegistration
- DhcpServerv4Lease.ServerIP
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
---

# DhcpServerv4Lease class

Dhcp Server v4 Client Lease.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class DhcpServerv4Lease
{
  string   AddressState;
  string   IPAddress;
  string   ScopeId;
  string   Description;
  string   ClientId;
  string   HostName;
  string   ClientType;
  DateTime LeaseExpiryTime;
  boolean  NapCapable;
  string   NapStatus;
  DateTime ProbationEnds;
  string   PolicyName;
  string   DnsRR;
  string   DnsRegistration;
  string   ServerIP;
};
```

## Members

The **DhcpServerv4Lease** class has these types of members:

-   [Properties](#properties)

### Properties

The **DhcpServerv4Lease** class has these properties.

<dl> <dt>

**AddressState**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Address state of the client.

<dt>

<span id="Offered"></span><span id="offered"></span><span id="OFFERED"></span>

**Offered** (Offered)


</dt> <dd></dd> <dt>

<span id="Active"></span><span id="active"></span><span id="ACTIVE"></span>

**Active** ("Active")


</dt> <dd></dd> <dt>

<span id="Declined"></span><span id="declined"></span><span id="DECLINED"></span>

**Declined** ("Declined")


</dt> <dd></dd> <dt>

<span id="Expired"></span><span id="expired"></span><span id="EXPIRED"></span>

**Expired** ("Expired")


</dt> <dd></dd> <dt>

<span id="ActiveReservation"></span><span id="activereservation"></span><span id="ACTIVERESERVATION"></span>

**ActiveReservation** ("ActiveReservation")


</dt> <dd></dd> <dt>

<span id="InactiveReservation"></span><span id="inactivereservation"></span><span id="INACTIVERESERVATION"></span>

**InactiveReservation** ("InactiveReservation")


</dt> <dd></dd> </dl>

</dd> <dt>

**ClientId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Client unique identifier for lease.

</dd> <dt>

**ClientType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Client type {UnSpecified, Dhcp, BootP, None}.

<dt>

<span id="UnSpecified"></span><span id="unspecified"></span><span id="UNSPECIFIED"></span>

**UnSpecified** ("UnSpecified")


</dt> <dd></dd> <dt>

<span id="Dhcp"></span><span id="dhcp"></span><span id="DHCP"></span>

**Dhcp** ("Dhcp")


</dt> <dd></dd> <dt>

<span id="BootP"></span><span id="bootp"></span><span id="BOOTP"></span>

**BootP** ("BootP")


</dt> <dd></dd> <dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

**None** ("None")


</dt> <dd></dd> </dl>

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Description for the client.

</dd> <dt>

**DnsRegistration**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates status of the DNS registration of the lease.

<dt>

<span id="Complete"></span><span id="complete"></span><span id="COMPLETE"></span>

**Complete** ("Complete")


</dt> <dd></dd> <dt>

<span id="Pending"></span><span id="pending"></span><span id="PENDING"></span>

**Pending** ("Pending")


</dt> <dd></dd> <dt>

<span id="NotApplicable"></span><span id="notapplicable"></span><span id="NOTAPPLICABLE"></span>

**NotApplicable** ("NotApplicable")


</dt> <dd></dd> </dl>

</dd> <dt>

**DnsRR**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates the type of DNS record to be registered by the DHCP server for the lease.

<dt>

<span id="A"></span><span id="a"></span>

**A** ("A")


</dt> <dd></dd> <dt>

<span id="PTR"></span><span id="ptr"></span>

**PTR** ("PTR")


</dt> <dd></dd> <dt>

<span id="AandPTR"></span><span id="aandptr"></span><span id="AANDPTR"></span>

**AandPTR** ("AandPTR")


</dt> <dd></dd> <dt>

<span id="NoRegistration"></span><span id="noregistration"></span><span id="NOREGISTRATION"></span>

**NoRegistration** ("NoRegistration")


</dt> <dd></dd> </dl>

**Windows Server 2012:** This value **A** is supported beginning with Windows Server 2012 R2.

</dd> <dt>

**HostName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Client name.

</dd> <dt>

**IPAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Client IP Address.

</dd> <dt>

**LeaseExpiryTime**
</dt> <dd> <dl> <dt>

Data type: **DateTime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Lease Expiry Time

</dd> <dt>

**NapCapable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates if the client is NAP capable or not.

</dd> <dt>

**NapStatus**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

NAP Status of the client.

<dt>

<span id="FullAccess"></span><span id="fullaccess"></span><span id="FULLACCESS"></span>

**FullAccess** ("FullAccess")


</dt> <dd></dd> <dt>

<span id="RestrictedAccess"></span><span id="restrictedaccess"></span><span id="RESTRICTEDACCESS"></span>

**RestrictedAccess** ("RestrictedAccess")


</dt> <dd></dd> <dt>

<span id="DropPacket"></span><span id="droppacket"></span><span id="DROPPACKET"></span>

**DropPacket** ("DropPacket")


</dt> <dd></dd> <dt>

<span id="InProbation"></span><span id="inprobation"></span><span id="INPROBATION"></span>

**InProbation** ("InProbation")


</dt> <dd></dd> <dt>

<span id="Exempt"></span><span id="exempt"></span><span id="EXEMPT"></span>

**Exempt** ("Exempt")


</dt> <dd></dd> <dt>

<span id="DefaultQuarantineSetting"></span><span id="defaultquarantinesetting"></span><span id="DEFAULTQUARANTINESETTING"></span>

**DefaultQuarantineSetting** ("DefaultQuarantineSetting")


</dt> <dd></dd> <dt>

<span id="NoQuarantineInfo"></span><span id="noquarantineinfo"></span><span id="NOQUARANTINEINFO"></span>

**NoQuarantineInfo** ("NoQuarantineInfo")


</dt> <dd></dd> </dl>

</dd> <dt>

**PolicyName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Name of the Policy based on which this IP address was leased.

</dd> <dt>

**ProbationEnds**
</dt> <dd> <dl> <dt>

Data type: **DateTime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

End-time of probation if the client is in probation.

</dd> <dt>

**ScopeId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Subnet address to which the client belongs.

</dd> <dt>

**ServerIP**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Server IP Address which indicates the server that has leased or renewed the IP address lease in a DHCP failover deployment.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





