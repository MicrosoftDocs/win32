---
description: Writes the local cached group policy object (GPO) information back to Active Directory Domain Services (AD DS).
ms.assetid: 7616de2f-cc19-425f-8c0c-90e5a018d909
title: Save method of the MSFT\_NetGPO class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetGPO.Save
api_type: 
- COM
api_location: 
- WFasCim.dll
ROBOTS: INDEX,FOLLOW
---

# Save method of the MSFT\_NetGPO class

Writes the local cached group policy object (GPO) information back to Active Directory Domain Services (AD DS).

## Syntax


```mof
uint32 Save(
  [in] String GPOSession
);
```



## Parameters

<dl> <dt>

*GPOSession* \[in\]
</dt> <dd>

The GPO session identifier.

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

 

 




