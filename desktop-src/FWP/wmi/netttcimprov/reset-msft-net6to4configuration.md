---
description: Resets the 6to4 configuration.
ms.assetid: 7272a6a4-a18d-46a0-9c2b-9c27e3a8c49e
title: Reset method of the MSFT\_Net6to4Configuration class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_Net6to4Configuration.Reset
api_type: 
- COM
api_location: 
- NetTtCim.dll
ROBOTS: INDEX,FOLLOW
---

# Reset method of the MSFT\_Net6to4Configuration class

Resets the 6to4 configuration.

## Syntax


```mof
uint32 Reset(
  [in]  boolean                   State,
  [in]  boolean                   AutoSharing,
  [in]  boolean                   RelayName,
  [in]  boolean                   RelayState,
  [in]  boolean                   ResolutionInterval,
  [in]  boolean                   PassThru,
  [out] MSFT_Net6to4Configuration OutputObject
);
```



## Parameters

<dl> <dt>

*State* \[in\]
</dt> <dd>

Whether to reset the **State** property of the [**MSFT\_Net6to4Configuration**](msft-net6to4configuration.md) object.

</dd> <dt>

*AutoSharing* \[in\]
</dt> <dd>

Whether to reset the **AutoSharing** property of the [**MSFT\_Net6to4Configuration**](msft-net6to4configuration.md) object.

</dd> <dt>

*RelayName* \[in\]
</dt> <dd>

Whether to reset the **RelayName** property of the [**MSFT\_Net6to4Configuration**](msft-net6to4configuration.md) object.

</dd> <dt>

*RelayState* \[in\]
</dt> <dd>

Whether to reset the **RelayState** property of the [**MSFT\_Net6to4Configuration**](msft-net6to4configuration.md) object.

</dd> <dt>

*ResolutionInterval* \[in\]
</dt> <dd>

Whether to reset the **Resolution** property of the [**MSFT\_Net6to4Configuration**](msft-net6to4configuration.md) object.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Specifies whether the method should output the an object that represents the reset 6to4 configuration in the *OutputObject* parameter.

</dd> <dt>

*OutputObject* \[out\]
</dt> <dd>

Receives the reset [**MSFT\_Net6to4Configuration**](msft-net6to4configuration.md) object.

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

[**MSFT\_Net6to4Configuration**](msft-net6to4configuration.md)
</dt> </dl>

 

 




