---
title: AddByZone method of the PS\_DnsServerQueryResolutionPolicy class
description: Adds a query resolution policy to the DNS server by zone.
audience: developer
ms.assetid: 47fa13f7-ce7f-466f-9291-23d3072d6456
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddByZone method
- AddByZone method, PS_DnsServerQueryResolutionPolicy class
- PS_DnsServerQueryResolutionPolicy class, AddByZone method
topic_type:
- apiref
api_name:
- PS_DnsServerQueryResolutionPolicy.AddByZone
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AddByZone method of the PS\_DnsServerQueryResolutionPolicy class

Adds a query resolution policy to the DNS server by zone.

## Syntax


```mof
uint32 AddByZone(
  [in]  boolean         PassThru,
  [in]  string          ComputerName,
  [in]  string          ZoneName,
  [in]  string          ZoneScope,
  [in]  string          Action,
  [in]  string          ClientSubnet,
  [in]  string          Condition,
  [in]  string          Fqdn,
  [in]  string          TimeOfDay,
  [in]  string          TransportProtocol,
  [in]  string          InternetProtocol,
  [in]  boolean         Disable,
  [in]  string          Name,
  [in]  uint32          ProcessingOrder,
  [in]  string          QType,
  [in]  string          ServerInterfaceIP,
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

*ZoneName* \[in\]
</dt> <dd>

The name of the zone.

</dd> <dt>

*ZoneScope* \[in\]
</dt> <dd>

The scope and weight of the zone.

</dd> <dt>

*Action* \[in\]
</dt> <dd>

Action taken if policy is matched.

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

The fully-qualified domain name.

</dd> <dt>

*TimeOfDay* \[in\]
</dt> <dd>

time of day criteria.

</dd> <dt>

*TransportProtocol* \[in\]
</dt> <dd>

Transport protocol criteria.

</dd> <dt>

*InternetProtocol* \[in\]
</dt> <dd>

Internet Protocol criteria.

</dd> <dt>

*Disable* \[in\]
</dt> <dd>

**true** to disable; otherwise **false**.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Name of the policy to add.

</dd> <dt>

*ProcessingOrder* \[in\]
</dt> <dd>

The order in which the query will be processed.

</dd> <dt>

*QType* \[in\]
</dt> <dd>

The query type.

</dd> <dt>

*ServerInterfaceIP* \[in\]
</dt> <dd>

The server interface.

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

 

 





