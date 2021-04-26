---
description: 'Other D3DX constants include the following:'
ms.assetid: 4f868a80-ad86-4598-9de3-a026e03aab93
title: Other D3DX Constants
ms.topic: article
ms.date: 05/31/2018
---

# Other D3DX Constants

Other D3DX constants include the following:

## 16-Bit Floating Point Numbers



| \#define                | Description                             |
|-------------------------|-----------------------------------------|
| D3DX\_16F\_DIG          | Number of decimal digits of precision   |
| D3DX\_16F\_EPSILON      | Smallest such that 1.0 + epsilon != 1.0 |
| D3DX\_16F\_MANT\_DIG    | Number of bits in mantissa              |
| D3DX\_16F\_MAX          | Maximum value                           |
| D3DX\_16F\_MAX\_10\_EXP | Maximum decimal exponent                |
| D3DX\_16F\_MAX\_EXP     | Maximum binary exponent                 |
| D3DX\_16F\_MIN          | Minimum positive value                  |
| D3DX\_16F\_MIN\_10\_EXP | Minimum decimal exponent                |
| D3DX\_16F\_MIN\_EXP     | Minimum binary exponent                 |
| D3DX\_16F\_RADIX        | Exponent radix                          |
| D3DX\_16F\_ROUNDS       | Addition rounding: near                 |
| D3DX\_1BYPI             | 1/pi                                    |
| D3DX\_PI                | pi                                      |
| D3DX\_DEFAULT\_FLOAT    | Maximum float value                     |



 

These \#defines are declared in d3dx9.h and d3dx9math.h.

## PRT Constants



| \#define         | Description                                |
|------------------|--------------------------------------------|
| D3DXSH\_MINORDER | Lowest allowable order of the simulation.  |
| D3DXSH\_MAXORDER | Highest allowable order of the simulation. |



 

These \#defines are declared in d3dx9math.h. For more about PRT, see [Precomputed Radiance Transfer (Direct3D 9)](precomputed-radiance-transfer.md).

## Texture Constants



| \#define               | Description                                                        |
|------------------------|--------------------------------------------------------------------|
| D3DFMT\_FROM\_FILE     | Take the format exactly from a file.                               |
| D3DX\_DEFAULT          | A default value.                                                   |
| D3DX\_DEFAULT\_NONPOW2 | Do not round up numbers such as width or height to a power of two. |
| D3DX\_FROM\_FILE       | Take the texture dimensions exactly from a file.                   |



 

These \#defines are declared in d3dx9.h.

## Other D3DX Constants

The UNUSED16 and D3DX\_VERSION constants defined in D3dx9mesh.h and D3dx9core.h are used internally. Do not use these constants.

## Related topics

<dl> <dt>

[D3DX Constants](dx9-graphics-reference-d3dx-constants.md)
</dt> </dl>

 

 



