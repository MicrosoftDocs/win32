---
title: AddByZone method of the PS\_DnsServerZoneTransferPolicy class
description: Adds a new zone transfer policy by zone.
audience: developer
ms.assetid: 542dbe89-938b-4339-9bec-f43f7dec7396
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddByZone method
- AddByZone method, PS_DnsServerZoneTransferPolicy class
- PS_DnsServerZoneTransferPolicy class, AddByZone method
topic_type:
- apiref
api_name:
- PS_DnsServerZoneTransferPolicy.AddByZone
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AddByZone method of the PS\_DnsServerZoneTransferPolicy class

Adds a new zone transfer policy by zone.

## Syntax


```mof
uint32 AddByZone(
  [in]  string          ComputerName,
  [in]  boolean         PassThru,
  [in]  string          TransportProtocol,
  [in]  string          TimeOfDay,
  [in]  string          ServerInterfaceIP,
  [in]  uint32          ProcessingOrder,
  [in]  string          ClientSubnet,
  [in]  boolean         Disable,
  [in]  string          InternetProtocol,
  [in]  string          Name,
  [in]  string          Condition,
  [in]  string          ZoneName,
  [in]  string          Action,
  [out] DnsServerPolicy cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

Optional DNS server name.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to return the current instance in the *CmdletOutput* parameter. The default is **false**.

</dd> <dt>

*TransportProtocol* \[in\]
</dt> <dd>

Transport protocol criteria.

</dd> <dt>

*TimeOfDay* \[in\]
</dt> <dd>

time of day criteria.

</dd> <dt>

*ServerInterfaceIP* \[in\]
</dt> <dd>

The server interface.

</dd> <dt>

*ProcessingOrder* \[in\]
</dt> <dd>

The order in which the query will be processed.

</dd> <dt>

*ClientSubnet* \[in\]
</dt> <dd>

Client subnet record name.

</dd> <dt>

*Disable* \[in\]
</dt> <dd>

**true** to disable; otherwise **false**.

</dd> <dt>

*InternetProtocol* \[in\]
</dt> <dd>

Internet Protocol criteria.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Name of the policy.

</dd> <dt>

*Condition* \[in\]
</dt> <dd>

The condition of the policy.

And

Or

</dd> <dt>

*ZoneName* \[in\]
</dt> <dd>

Name of the zone.

</dd> <dt>

*Action* \[in\]
</dt> <dd>

Action taken if policy is matched.

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

[**PS\_DnsServerZoneTransferPolicy**](ps-dnsserverzonetransferpolicy.md)
</dt> </dl>

 

 





