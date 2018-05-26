---
title: Add method of the PS\_DhcpServerv4Lease class
description: Adds a new IPv4 address lease in the DHCP server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: bf450186-9059-453e-a605-fcd0bb775306
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Add method
- Add method, PS_DhcpServerv4Lease class
- PS_DhcpServerv4Lease class, Add method
topic_type:
- apiref
api_name:
- PS_DhcpServerv4Lease.Add
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Add method of the PS\_DhcpServerv4Lease class

Adds a new IPv4 address lease in the DHCP server.

## Syntax


```mof
uint32 Add(
  [in]  string            IPAddress,
  [in]  string            ScopeId,
  [in]  string            ClientId,
  [in]  string            AddressState,
  [in]  string            HostName,
  [in]  string            Description,
  [in]  string            ComputerName,
  [in]  boolean           PassThru,
  [in]  string            DnsRR,
  [in]  string            DnsRegistration,
  [in]  string            ClientType,
  [in]  datetime          LeaseExpiryTime,
  [in]  boolean           NapCapable,
  [in]  string            NapStatus,
  [in]  datetime          ProbationEnds,
  [in]  string            PolicyName,
  [out] DhcpServerv4Lease cmdletOutput
);
```



## Parameters

<dl> <dt>

*IPAddress* \[in\]
</dt> <dd>

IP Address for which the IP address lease record is to be added on the DHCP server

</dd> <dt>

*ScopeId* \[in\]
</dt> <dd>

Subnet mask to be set on the IP address lease record being added

</dd> <dt>

*ClientId* \[in\]
</dt> <dd>

Client identifier to be set on the IP address lease

</dd> <dt>

*AddressState* \[in\]
</dt> <dd>

State of the IP Address lease. Valid values are Offered, Active, Declined, Expired, Inactive. Default value is Active.

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


</dt> <dd></dd> </dl> </dd> <dt>

*HostName* \[in\]
</dt> <dd>

DNS hostname of the client for which the IP address lease is to be added

</dd> <dt>

*Description* \[in\]
</dt> <dd>

Description string to be set on the IP address lease

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If this parameter is specified, the cmdlet return the PowerShell objects which are deleted.

</dd> <dt>

*DnsRR* \[in\]
</dt> <dd>

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

**Windows Server 2012:** This parameter supports the **A** value beginning with Windows Server 2012 R2.

</dd> <dt>

*DnsRegistration* \[in\]
</dt> <dd>

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


</dt> <dd></dd> </dl> </dd> <dt>

*ClientType* \[in\]
</dt> <dd>

Type of the client. Valid values are UNSPECIFIED, DHCP, BOOTP, BOTH, RESERVATION, NONE.

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


</dt> <dd></dd> </dl> </dd> <dt>

*LeaseExpiryTime* \[in\]
</dt> <dd>

Expiry time of the IP address lease

</dd> <dt>

*NapCapable* \[in\]
</dt> <dd>

Indicate if the client is NAP capable or not. Valid values are True, False.

</dd> <dt>

*NapStatus* \[in\]
</dt> <dd>

NAP status of the client. Valid values are NOQUARANTINE, RESTRICTEDACCESS, DROPPACKET, PROBATION, EXEMPT, DEFAULTQUARSETTING, and NOQUARINFO. The default value is NOQUARANTINE.If NapStatus is specified as PROBATION and probation period is not specified, cmdlet will return an error. If NapStatus is not specified or is specified something other than Probation and probation period is not specified, the probation period to set to 0. If NapStatus is not specified and probation period is specified, the NapStatus is set to PROBATION. If NapStatus is not specified or specified other than Probation AND ProbationEnds is specified, cmdlet will return an error.

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


</dt> <dd></dd> </dl> </dd> <dt>

*ProbationEnds* \[in\]
</dt> <dd>

End-time of probation to be set on the IP address lease record. Default value is 0.

</dd> <dt>

*PolicyName* \[in\]
</dt> <dd>

Name of the policy to be set on the IP address lease record being added. Note: DHCP server does not perform any check on whether the policy specified exists on the server.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerv4Lease**](dhcpserverv4lease.md) class.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DhcpServerv4Lease**](ps-dhcpserverv4lease.md)
</dt> </dl>

 

 





