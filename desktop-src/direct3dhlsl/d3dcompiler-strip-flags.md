---
title: D3DCOMPILER\_STRIP\_FLAGS enumeration
description: Strip flag options.
ms.assetid: 44e2af42-f5db-4206-aa00-37d070b2ca3b
keywords:
- D3DCOMPILER_STRIP_FLAGS enumeration HLSL
topic_type:
- apiref
api_name:
- D3DCOMPILER_STRIP_FLAGS
api_location:
- D3Dcompiler.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DCOMPILER\_STRIP\_FLAGS enumeration

Strip flag options.

## Members



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Member</th>
<th>Description</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>D3DCOMPILER_STRIP_REFLECTION_DATA</strong></td>
<td>Remove reflection data.<br/></td>
<td>0x00000001</td>
</tr>
<tr class="even">
<td><strong>D3DCOMPILER_STRIP_DEBUG_INFO</strong></td>
<td>Remove debug information.<br/></td>
<td>0x00000002</td>
</tr>
<tr class="odd">
<td><strong>D3DCOMPILER_STRIP_TEST_BLOBS</strong></td>
<td>Remove test blob data.<br/></td>
<td>0x00000004</td>
</tr>
<tr class="even">
<td><strong>D3DCOMPILER_STRIP_PRIVATE_DATA</strong></td>
<td><blockquote>
[!Note]<br />
This value is supported by the D3dcompiler_44.dll or later version of the file.
</blockquote>
<br/> Remove private data.<br/></td>
<td>0x00000008</td>
</tr>
<tr class="odd">
<td><strong>D3DCOMPILER_STRIP_ROOT_SIGNATURE</strong></td>
<td><blockquote>
[!Note]<br />
This value is supported by the D3dcompiler_47.dll or later version of the file.
</blockquote>
<br/> Remove the root signature. Refer to [Specifying Root Signatures in HLSL](https://msdn.microsoft.com/library/windows/desktop/dn913202) for more information on using Direct3D12 with HLSL.<br/></td>
<td>0x00000010</td>
</tr>
<tr class="even">
<td><strong>D3DCOMPILER_STRIP_FORCE_DWORD</strong></td>
<td>Forces this enumeration to compile to 32 bits in size. Without this value, some compilers would allow this enumeration to compile to a size other than 32 bits. This value is not used.<br/></td>
<td>0x7fffffff</td>
</tr>
</tbody>
</table>



## Remarks

These flags are used by [**D3DStripShader**](d3dstripshader.md).

## Requirements



|                   |                                                                                          |
|-------------------|------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3Dcompiler.h</dt> </dl> |



## See also

<dl> <dt>

[Enumerations](dx-graphics-d3dcompiler-reference-enums.md)
</dt> </dl>

 

 





