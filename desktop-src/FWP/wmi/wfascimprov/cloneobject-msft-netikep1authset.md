---
description: Copy this set.
ms.assetid: dd3d7786-3d33-4440-a04b-8a9b6af69937
title: CloneObject method of the MSFT\_NetIKEP1AuthSet class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetIKEP1AuthSet.CloneObject
api_type: 
- COM
api_location: 
- WFasCim.dll
ROBOTS: INDEX,FOLLOW
---

# CloneObject method of the MSFT\_NetIKEP1AuthSet class

Copy this set.

## Syntax


```mof
uint32 CloneObject(
  [in] string NewName,
  [in] string NewID,
  [in] string NewPolicyStore,
  [in] string NewGPOSession
);
```



## Parameters

<dl> <dt>

*NewName* \[in\]
</dt> <dd>

The new name for the set.

</dd> <dt>

*NewID* \[in\]
</dt> <dd>

The new ID for the set.

</dd> <dt>

*NewPolicyStore* \[in\]
</dt> <dd>

The new policy store for the set.

</dd> <dt>

*NewGPOSession* \[in\]
</dt> <dd>

The new GPOSession for the set.

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

[**MSFT\_NetIKEP1AuthSet**](msft-netikep1authset.md)
</dt> </dl>

 

 




