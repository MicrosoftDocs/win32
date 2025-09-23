---
description: Synchronize IPsec policy.
ms.assetid: b5e51ada-736f-41e8-beed-66dd4de41fc2
title: SyncPolicyDelta method of the MSFT\_NetConSecRule class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetConSecRule.SyncPolicyDelta
api_type: 
- COM
api_location: 
- WFasCim.dll
ROBOTS: INDEX,FOLLOW
---

# SyncPolicyDelta method of the MSFT\_NetConSecRule class

Synchronize IPsec policy

## Syntax


```mof
uint32 SyncPolicyDelta(
  [in]  string Servers[],
  [in]  string Domains[],
  [in]  uint16 EndpointType,
  [in]  uint16 AddressType,
  [in]  string DnsServers[],
  [out] String Output[]
);
```



## Parameters

<dl> <dt>

*Servers* \[in\]
</dt> <dd>

Servers

</dd> <dt>

*Domains* \[in\]
</dt> <dd>

Domains

</dd> <dt>

*EndpointType* \[in\]
</dt> <dd>

Endpoint type

<dl> <dt>

<span id="Endpoint1"></span><span id="endpoint1"></span><span id="ENDPOINT1"></span>**Endpoint1** (0)
</dt> <dt>

<span id="Endpoint2_"></span><span id="endpoint2_"></span><span id="ENDPOINT2_"></span>**Endpoint2** (1 )
</dt> </dl> </dd> <dt>

*AddressType* \[in\]
</dt> <dd>

Types of addresses

<dl> <dt>

<span id="IPv4"></span><span id="ipv4"></span><span id="IPV4"></span>**IPv4** (0)
</dt> <dt>

<span id="IPv6_"></span><span id="ipv6_"></span><span id="IPV6_"></span>**IPv6** (1)
</dt> </dl> </dd> <dt>

*DnsServers* \[in\]
</dt> <dd>

Servers to perform name resolution against

</dd> <dt>

*Output* \[out\]
</dt> <dd>

Delta collection

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                         |
| MOF<br/>                      | <dl> <dt>WFasCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WFasCim.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_NetConSecRule**](msft-netconsecrule.md)
</dt> </dl>

 

 




