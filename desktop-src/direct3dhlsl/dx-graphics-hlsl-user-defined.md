---
title: User-Defined Type
description: Use the following syntax to declare a user-defined type.
ms.assetid: 8ef18864-f456-4b52-af83-f9b1050a0bba
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# User-Defined Type

Use the following syntax to declare a user-defined type.



|                                           |
|-------------------------------------------|
| typedef **\[const\] Type Name\[Index\]**; |



 

## Parameters



| Item                                                                                         | Description                                                                            |
|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| <span id="_const_"></span><span id="_CONST_"></span>**\[const\]**<br/>                 | Optional. This keyword explicitly marks the type as a constant.<br/>             |
| <span id="Type"></span><span id="type"></span><span id="TYPE"></span>**Type**<br/>     | Identifies the data type; must be one of the HLSL intrinsic data types.<br/>     |
| <span id="Name"></span><span id="name"></span><span id="NAME"></span>**Name**<br/>     | An ASCII string that uniquely identifies the variable name.<br/>                 |
| <span id="Index"></span><span id="index"></span><span id="INDEX"></span>**Index**<br/> | Optional array size. Must be an unsigned integer between 1 and 4 inclusive.<br/> |



 

In addition to the built-in intrinsic data types, HLSL supports user-defined or custom types which follow this syntax:

## Remarks

User-defined types are not case-sensitive. For convenience, the following types are automatically defined at super-global scope.


```
typedef vector <bool, #> bool#;
typedef vector <int, #> int#;
typedef vector <uint, #> uint#;
typedef vector <half, #> half#;
typedef vector <float, #> float#;
typedef vector <double, #> double#;

typedef matrix <bool, #, #> bool#x#;
typedef matrix <int, #, #> int#x#;
typedef matrix <uint, #, #> uint#x#;
typedef matrix <half, #, #> half#x#;
typedef matrix <float, #, #> float#x#;
typedef matrix <double, #, #> double#x#;
```



The pound sign (\#) represents an integer digit between 1 and 4.

For compatibility with DirectX 8 effects, the following types are automatically defined at super-global scope:


```
typedef int DWORD;
typedef float FLOAT; 
typedef vector <float, 4> VECTOR;
typedef matrix <float, 4, 4> MATRIX;
typedef string STRING;
typedef texture TEXTURE;
typedef pixelshader PIXELSHADER;
typedef vertexshader VERTEXSHADER;
```



## Related topics

<dl> <dt>

[Data Types (DirectX HLSL)](dx-graphics-hlsl-data-types.md)
</dt> </dl>

 

 





