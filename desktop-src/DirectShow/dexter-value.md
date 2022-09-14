---
description: Identifies a property that is to be set on a transition or effect, along with the number of distinct values that the property assumes over the duration of the transition or effect.
ms.assetid: 3b1c35cf-f1f7-4f2c-8d94-1aaae4116833
title: DEXTER_VALUE structure (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DEXTER_VALUE
api_type: 
- HeaderDef
api_location: 
- Qedit.h
---

# DEXTER\_VALUE structure

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

Identifies a property that is to be set on a transition or effect, along with the number of distinct values that the property assumes over the duration of the transition or effect.

## Syntax


```C++
typedef struct {
  VARIANT        v;
  REFERENCE_TIME rt;
  DWORD          dwInterp;
} DEXTER_VALUE;
```



## Members

<dl> <dt>

**v**
</dt> <dd>

Value of the property.

</dd> <dt>

**rt**
</dt> <dd>

Time at which the property assumes the value, relative to the start of the transition or effect.

</dd> <dt>

**dwInterp**
</dt> <dd>

Flag indicating how the property progresses from the previous value to this value. Must be one of the following:



| Value                                                                                                                                                                           | Meaning                                                                             |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| <span id="DEXTERF_JUMP"></span><span id="dexterf_jump"></span><dl> <dt>**DEXTERF\_JUMP**</dt> </dl>                      | The property jumps instantly to the new value at the specified time.<br/>     |
| <span id="DEXTERF_INTERPOLATE"></span><span id="dexterf_interpolate"></span><dl> <dt>**DEXTERF\_INTERPOLATE**</dt> </dl> | The property is interpolated linearly over time from the previous value.<br/> |



 

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Qedit.h</dt> </dl> |



## See also

<dl> <dt>

[**IPropertySetter**](ipropertysetter.md)
</dt> <dt>

[**DEXTER\_PARAM**](dexter-param.md)
</dt> </dl>

 

 




