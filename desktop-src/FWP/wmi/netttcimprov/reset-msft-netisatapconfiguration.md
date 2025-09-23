---
description: Resets the ISATAP configuration.
ms.assetid: 492bfe5f-3f98-48e7-9687-e571d76ec471
title: Reset method of the MSFT\_NetISATAPConfiguration class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetISATAPConfiguration.Reset
api_type: 
- COM
api_location: 
- NetTtCim.dll
ROBOTS: INDEX,FOLLOW
---

# Reset method of the MSFT\_NetISATAPConfiguration class

Resets the ISATAP configuration.

## Syntax


```mof
uint32 Reset(
  [in]  boolean                     State,
  [in]  boolean                     Router,
  [in]  boolean                     ResolutionState,
  [in]  boolean                     ResolutionInterval,
  [in]  boolean                     PassThru,
  [out] MSFT_NetISATAPConfiguration OutputObject
);
```



## Parameters

<dl> <dt>

*State* \[in\]
</dt> <dd>

Specifies whether to reset the **State** property of the [**MSFT\_NetISATAPConfiguration**](msft-netisatapconfiguration.md) object.

</dd> <dt>

*Router* \[in\]
</dt> <dd>

Specifies whether to reset the **Router** property of the [**MSFT\_NetISATAPConfiguration**](msft-netisatapconfiguration.md) object.

</dd> <dt>

*ResolutionState* \[in\]
</dt> <dd>

Specifies whether to reset the **ResolutionState** property of the [**MSFT\_NetISATAPConfiguration**](msft-netisatapconfiguration.md) object.

</dd> <dt>

*ResolutionInterval* \[in\]
</dt> <dd>

Specifies whether to reset the **ResolutionInterval** property of the [**MSFT\_NetISATAPConfiguration**](msft-netisatapconfiguration.md) object.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Specifies whether the method should output the an object that represents the reset ISATAP configuration in the *OutputObject* parameter.

</dd> <dt>

*OutputObject* \[out\]
</dt> <dd>

Receives the reset [**MSFT\_NetISATAPConfiguration**](msft-netisatapconfiguration.md) object.

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

[**MSFT\_NetISATAPConfiguration**](msft-netisatapconfiguration.md)
</dt> </dl>

 

 




