---
description: Turns NAT64 on.
ms.assetid: 685ba50e-152d-4731-a940-e78ab775fe72
title: Enable method of the MSFT\_NetNatTransitionConfiguration class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetNatTransitionConfiguration.Enable
api_type: 
- COM
api_location: 
- NetTtCim.dll
ROBOTS: INDEX,FOLLOW
---

# Enable method of the MSFT\_NetNatTransitionConfiguration class

Turns NAT64 on.

## Syntax


```mof
uint32 Enable(
  [in]  boolean                            PassThru,
  [out] MSFT_NetNatTransitionConfiguration OutputObject
);
```



## Parameters

<dl> <dt>

*PassThru* \[in\]
</dt> <dd>

Specifies whether the method should output the [**MSFT\_NetNatTransitionConfiguration**](msft-netnattransitionconfiguration.md) object that results from turning NAT64 on in the *OutputObject* parameter.

</dd> <dt>

*OutputObject* \[out\]
</dt> <dd>

Receives the [**MSFT\_NetNatTransitionConfiguration**](msft-netnattransitionconfiguration.md) object that results from turning NAT64 on

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                          |
| MOF<br/>                      | <dl> <dt>NetTtCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetTtCim.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_NetNatTransitionConfiguration**](msft-netnattransitionconfiguration.md)
</dt> </dl>

 

 




