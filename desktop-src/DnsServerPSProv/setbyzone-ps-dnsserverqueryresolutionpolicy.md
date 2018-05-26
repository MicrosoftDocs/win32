---
title: SetByZone method of the PS\_DnsServerQueryResolutionPolicy class
description: Sets the DNS server name resolution policy by zone.
audience: developer
ms.assetid: 196d77da-4f52-4ce2-ab5d-99de2f107638
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetByZone method
- SetByZone method, PS_DnsServerQueryResolutionPolicy class
- PS_DnsServerQueryResolutionPolicy class, SetByZone method
topic_type:
- apiref
api_name:
- PS_DnsServerQueryResolutionPolicy.SetByZone
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SetByZone method of the PS\_DnsServerQueryResolutionPolicy class

Sets the DNS server name resolution policy by zone.

## Syntax


```mof
uint32 SetByZone(
  [in]  boolean         PassThru,
  [in]  string          ComputerName,
  [in]  string          ZoneScope,
  [in]  string          ZoneName,
  [in]  string          ClientSubnet,
  [in]  string          Condition,
  [in]  string          Fqdn,
  [in]  string          InternetProtocol,
  [in]  string          Name,
  [in]  uint32          ProcessingOrder,
  [in]  string          QType,
  [in]  string          ServerInterfaceIP,
  [in]  string          TimeOfDay,
  [in]  string          TransportProtocol,
  [out] DnsServerPolicy cmdletOutput
);
```



## Parameters

<dl> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to return the current instance in the *CmdletOutput* parameter. The default is **false**.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Optional DNS server name.

</dd> <dt>

*ZoneScope* \[in\]
</dt> <dd>

Scope and weight of the zone.

</dd> <dt>

*ZoneName* \[in\]
</dt> <dd>

Name of the zone.

</dd> <dt>

*ClientSubnet* \[in\]
</dt> <dd>

Client subnet record name.

</dd> <dt>

*Condition* \[in\]
</dt> <dd>

The condition of the policy.

And

Or

</dd> <dt>

*Fqdn* \[in\]
</dt> <dd>

Fully-qualified domain name.

</dd> <dt>

*InternetProtocol* \[in\]
</dt> <dd>

Internet Protocol criteria.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Name of the policy to set.

</dd> <dt>

*ProcessingOrder* \[in\]
</dt> <dd>

The order in which the query will be processed.

</dd> <dt>

*QType* \[in\]
</dt> <dd>

Query type.

</dd> <dt>

*ServerInterfaceIP* \[in\]
</dt> <dd>

The server interface.

</dd> <dt>

*TimeOfDay* \[in\]
</dt> <dd>

Time of day criteria.

</dd> <dt>

*TransportProtocol* \[in\]
</dt> <dd>

Transport protocol criteria.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On return, contains a [**DnsServerPolicy**](dnsserverpolicy.md). This parameter returns a value only if *PassThru* is set to **true.**

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServerQueryResolutionPolicy**](ps-dnsserverqueryresolutionpolicy.md)
</dt> </dl>

 

 





