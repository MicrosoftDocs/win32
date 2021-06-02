---
description: Specifies the value that a property assumes at a given time.
ms.assetid: 117868b7-65e5-4b3b-9e50-4106ee6a65d0
title: DEXTER_PARAM structure (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DEXTER_PARAM
api_type: 
- HeaderDef
api_location: 
- Qedit.h
---

# DEXTER\_PARAM structure

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

Specifies the value that a property assumes at a given time.

## Syntax


```C++
typedef struct {
  BSTR   Name;
  DISPID dispID;
  LONG   nValues;
} DEXTER_PARAM;
```



## Members

<dl> <dt>

**Name**
</dt> <dd>

Name of the property.

</dd> <dt>

**dispID**
</dt> <dd>

Reserved. Set to zero.

</dd> <dt>

**nValues**
</dt> <dd>

Number of values that the property assumes.

</dd> </dl>

## Remarks

The object must support the **IDispatch** interface.

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Qedit.h</dt> </dl> |



## See also

<dl> <dt>

[**IPropertySetter**](ipropertysetter.md)
</dt> <dt>

[**DEXTER\_VALUE**](dexter-value.md)
</dt> </dl>

 

 




