---
title: Scalar Types
description: Scalar Types
ms.assetid: bf24d27f-2720-4268-bc74-fc46afedb9aa
keywords:
- Scalar Types HLSL
topic_type:
- apiref
api_name:
- Scalar Types
api_type:
- NA
ms.topic: reference
ms.custom: snippet-project
ms.date: 07/29/2020
---

# Scalar Types


HLSL supports several scalar data types:

-   **bool** - true or false.
-   **int** - 32-bit signed integer.
-   **uint** - 32-bit unsigned integer.
-   **dword** - 32-bit unsigned integer.
-   **half** - 16-bit floating point value. This data type is provided only for language compatibility. Direct3D 10 shader targets map all half data types to float data types. A half data type cannot be used on a uniform global variable (use the /Gec flag if this functionality is desired).
-   **float** - 32-bit floating point value.
-   **double** - 64-bit floating point value. You cannot use double precision values as inputs and outputs for a stream. To pass double precision values between shaders, declare each **double** as a pair of **uint** data types. Then, use the [**asuint**](asuint.md) function to pack each **double** into the pair of **uint**s and the [**asdouble**](asdouble.md) function to unpack the pair of **uint**s back into the **double**.

Starting with Windows 8 HLSL also supports minimum precision scalar data types. Graphics drivers can implement minimum precision scalar data types by using any precision greater than or equal to their specified bit precision. We recommend not to rely on clamping or wrapping behavior that depends on specific underlying precision. For example, the graphics driver might execute arithmetic on a **min16float** value at full 32-bit precision.

-   **min16float** - minimum 16-bit floating point value.
-   **min10float** - minimum 10-bit floating point value.
-   **min16int** - minimum 16-bit signed integer.
-   **min12int** - minimum 12-bit signed integer.
-   **min16uint** - minimum 16-bit unsigned integer.

For more information about scalar literals, see [Grammar](dx-graphics-hlsl-appendix-grammar.md).

Starting with shader model 6.0 the following scalars were added (Windows 10 1607):

- **uint64_t** - A 64-bit unsigned integer.
- **int64_t** - A 64-bit signed integer.

For more information about shader model 6.0: [SM6.0 documentation](https://learn.microsoft.com/en-us/windows/win32/direct3dhlsl/hlsl-shader-model-6-0-features-for-direct3d-12).

Since shader model 6.2 the following data types can be used if -enable-16bit-types is used using DXC (Windows 10 1803):

- **float16_t** - Always a 16-bit floating point value (as opposed to other 16-bit floats which may or may not be 16-bit).
- **uint16_t** - A 16-bit unsigned integer.
- **int16_t** - A 16-bit signed integer.

For more information about 16-bit types, see [DXC: 16 Bit Scalar Types](https://github.com/microsoft/DirectXShaderCompiler/wiki/16-Bit-Scalar-Types). Do note that these require 16-bit support in hardware. This is supported starting at Turing or higher.

<table>
<colgroup>
<col  />
</colgroup>
<tbody>
<tr class="odd">
<td>Differences between Direct3D 9 and Direct3D 10:<br/> In Direct3D 10, the following types are modifiers to the float type.<br/>
<ul>
<li><strong>snorm float</strong> - IEEE 32-bit signed-normalized float in range -1 to 1 inclusive.</li>
<li><strong>unorm float</strong> - IEEE 32-bit unsigned-normalized float in range 0 to 1 inclusive.</li>
</ul>
For example, here is a 4-component signed-normalized float-variable declaration.<br/> <span data-codelanguage=""></span>
<table>
<colgroup>
<col  />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>snorm float4 fourComponentIEEEFloat;</code></pre></td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>



 

## String Type

HLSL also supports a **string** type, which is an ASCII string. There are no operations or states that accept strings, but effects can query string parameters and annotations.

## Example

```c
// top-level variable
float globalShaderVariable; 

// top-level function
void function(
in float4 position: POSITION0 // top-level argument
              )
{
  float localShaderVariable; // local variable
  function2(...)
}

void function2()
{
  ...
}
```

## See also



* [Declaring Scalar Types](./dx-graphics-hlsl-writing-shaders-9.md#declaring-shader-variables)
* [Data Types (DirectX HLSL)](dx-graphics-hlsl-data-types.md)
