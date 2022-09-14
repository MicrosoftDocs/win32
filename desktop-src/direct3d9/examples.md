---
description: Two example binary template definitions and an example of a binary data object follow.
ms.assetid: 'vs|directx_sdk|~\examples.htm'
title: Examples (Direct3D 9 Graphics)
ms.topic: article
ms.date: 05/31/2018
---

# Examples (Direct3D 9 Graphics)

Two example binary template definitions and an example of a binary data object follow.

> [!Note]  
> Data is stored in little-endian format, which is not shown in these examples.

 

The closed template RGB is identified by the UUID {55b6d780-37ec-11d0-ab39-0020af71e433} and has three members - r, g, and b - each of type float.


```
TOKEN_TEMPLATE, TOKEN_NAME, 3, 'R', 'G', 'B', TOKEN_OBRACE,
TOKEN_GUID, 55b6d780, 37ec, 11d0, ab, 39, 00, 20, af, 71, e4, 33,
TOKEN_FLOAT, TOKEN_NAME, 1, 'r', TOKEN_SEMICOLON,
TOKEN_FLOAT, TOKEN_NAME, 1, 'g', TOKEN_SEMICOLON,
TOKEN_FLOAT, TOKEN_NAME, 1, 'b', TOKEN_SEMICOLON,
TOKEN_CBRACE
```



The closed template Matrix4x4 is identified by the UUID {55b6d781-37ec-11d0-ab39-0020af71e433} and has one member - a two-dimensional array named matrix - of type float.


```
TOKEN_TEMPLATE, TOKEN_NAME, 9, 'M', 'a', 't', 'r', 'i', 'x', '4', 'x', '4', TOKEN_OBRACE,
TOKEN_GUID, 55b6d781, 37ec, 11d0, ab, 39, 00, 20, af, 71, e4, 33,
TOKEN_ARRAY, TOKEN_FLOAT, TOKEN_NAME, 6, 'm', 'a', 't', 'r', 'i', 'x',
TOKEN_OBRACKET, TOKEN_INTEGER, 4, TOKEN_CBRACKET,
TOKEN_OBRACKET, TOKEN_INTEGER, 4, TOKEN_CBRACKET,
TOKEN_CBRACE
```



The binary data object that follows shows an instance of the RGB template defined earlier. The example object is named blue, and its three members - r, g, and b - have the values 0.0, 0.0, and 1.0, respectively.


```
TOKEN_NAME, 3, 'R', 'G', 'B', TOKEN_NAME, 4, 'b', 'l', 'u', 'e', TOKEN_OBRACE,
TOKEN_FLOAT_LIST, 3, 0.0, 0.0, 1.0, TOKEN_CBRACE
```



## Related topics

<dl> <dt>

[Binary Encoding](binary-encoding.md)
</dt> </dl>

 

 



