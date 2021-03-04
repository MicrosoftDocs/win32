---
title: Vector Type (HLSL)
description: A vector contains between one and four scalar components; every component of a vector must be of the same type.
ms.assetid: 16e66f3c-c513-4d03-8adf-463dc8d83e12
keywords:
- Vector Type HLSL
topic_type:
- apiref
api_name:
- Vector Type
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# Vector Type

A vector contains between one and four scalar components; every component of a vector must be of the same type.



|                     |
|---------------------|
| **TypeNumber Name** |



 


```
TypeComponents Name
```



## Components



| Item                                                                                                                             | Description                                                                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="TypeComponents"></span><span id="typecomponents"></span><span id="TYPECOMPONENTS"></span>**TypeComponents**<br/> | A single name that contains two parts. The first part is one of the [scalar](dx-graphics-hlsl-data-types.md) types. The second part is the number of components, which must be between 1 and 4 inclusive.<br/> |
| <span id="Name"></span><span id="name"></span><span id="NAME"></span>**Name**<br/>                                         | An ASCII string that uniquely identifies the variable name.<br/>                                                                                                                                                |



 

## Examples

Here are some examples:


```
bool    bVector;   // scalar containing 1 Boolean
int1    iVector = 1;
float3  fVector = { 0.2f, 0.3f, 0.4f };
```



A vector can be declared using this syntax also:


```
vector <Type, Number> VariableName
```



Here are some examples:


```
vector <int,    1> iVector = 1;
vector <double, 4> dVector = { 0.2, 0.3, 0.4, 0.5 };
```

## See also

<dl> <dt>

[Data Types (DirectX HLSL)](dx-graphics-hlsl-data-types.md)
</dt> </dl>

 

 





