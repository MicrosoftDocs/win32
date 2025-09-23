---
description: Turns NAT64 off.
ms.assetid: 3582d8c5-2944-4fe7-af19-9c0219c050f9
title: Disable method of the MSFT\_NetNatTransitionConfiguration class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetNatTransitionConfiguration.Disable
api_type: 
- COM
api_location: 
- NetTtCim.dll
ROBOTS: INDEX,FOLLOW
---

# Disable method of the MSFT\_NetNatTransitionConfiguration class

Turns NAT64 off.

## Syntax


```mof
uint32 Disable(
  [in]  boolean                            PassThru,
  [out] MSFT_NetNatTransitionConfiguration OutputObject
);
```



## Parameters

<dl> <dt>

*PassThru* \[in\]
</dt> <dd>

Specifies whether the method should output the [**MSFT\_NetNatTransitionConfiguration**](msft-netnattransitionconfiguration.md) object that results from turning NAT64 off in the *OutputObject* parameter.

</dd> <dt>

*OutputObject* \[out\]
</dt> <dd>

Receives the [**MSFT\_NetNatTransitionConfiguration**](msft-netnattransitionconfiguration.md) object that results from turning NAT64 off.

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

 

 




