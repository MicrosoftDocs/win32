---
description: Apply IPsec policy deltas.
ms.assetid: e4a0e32e-826e-4f09-95e3-14da3c8b3aa2
title: SetPolicyDelta method of the MSFT\_NetConSecRule class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetConSecRule.SetPolicyDelta
api_type: 
- COM
api_location: 
- WFasCim.dll
ROBOTS: INDEX,FOLLOW
---

# SetPolicyDelta method of the MSFT\_NetConSecRule class

Apply IPsec policy deltas

## Syntax


```mof
uint32 SetPolicyDelta(
        uint16  Action,
  [in]  string  IPv6Addresses[],
  [in]  string  IPv4Addresses[],
        uint16  EndpointType,
  [in]  boolean PassThru,
  [out] String  Output[]
);
```



## Parameters

<dl> <dt>

*Action* 
</dt> <dd>

Action

<dl> <dt>

<span id="Add"></span><span id="add"></span><span id="ADD"></span>**Add** (0)
</dt> <dt>

<span id="Delete_"></span><span id="delete_"></span><span id="DELETE_"></span>**Delete** (1 )
</dt> </dl> </dd> <dt>

*IPv6Addresses* \[in\]
</dt> <dd>

IPv6 Addresses

</dd> <dt>

*IPv4Addresses* \[in\]
</dt> <dd>

IPv4 Addresses

</dd> <dt>

*EndpointType* 
</dt> <dd>

Endpoint type

<dl> <dt>

<span id="Endpoint1"></span><span id="endpoint1"></span><span id="ENDPOINT1"></span>**Endpoint1** (0)
</dt> <dt>

<span id="Endpoint2_"></span><span id="endpoint2_"></span><span id="ENDPOINT2_"></span>**Endpoint2** (1 )
</dt> </dl> </dd> <dt>

*PassThru* \[in\]
</dt> <dd>

PassThru

</dd> <dt>

*Output* \[out\]
</dt> <dd>

Output NetConSecRule

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

 

 




