---
description: Reads a group policy object (GPO) and caches the results locally.
ms.assetid: e2f3b0d1-7294-4fec-ad4f-d757eb64f5c3
title: Open method of the MSFT\_NetGPO class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetGPO.Open
api_type: 
- COM
api_location: 
- WFasCim.dll
ROBOTS: INDEX,FOLLOW
---

# Open method of the MSFT\_NetGPO class

Reads a group policy object (GPO) and caches the results locally.

## Syntax


```mof
uint32 Open(
  [in]  string PolicyStore,
  [in]  string DomainController,
  [out] String GPOSession
);
```



## Parameters

<dl> <dt>

*PolicyStore* \[in\]
</dt> <dd>

The name of the policy store.

</dd> <dt>

*DomainController* \[in\]
</dt> <dd>

The name of the domain controller.

</dd> <dt>

*GPOSession* \[out\]
</dt> <dd>

When this method returns, contains the GPO session identifier.

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

[**MSFT\_NetGPO**](msft-netgpo.md)
</dt> </dl>

 

 




