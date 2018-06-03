---
title: D3D\_BLOB\_PART enumeration
description: Values that identify parts of the content of an arbitrary length data buffer.
ms.assetid: 333bc68a-0412-48e7-ac28-69ec5eea9ce8
keywords:
- D3D_BLOB_PART enumeration HLSL
topic_type:
- apiref
api_name:
- D3D_BLOB_PART
api_location:
- D3Dcompiler.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# D3D\_BLOB\_PART enumeration

Values that identify parts of the content of an arbitrary length data buffer.

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
<td><strong>D3D_BLOB_INPUT_SIGNATURE_BLOB</strong></td>
<td>The blob part is an input signature.<br/></td>

</tr>
<tr class="even">
<td><strong>D3D_BLOB_OUTPUT_SIGNATURE_BLOB</strong></td>
<td>The blob part is an output signature.<br/></td>

</tr>
<tr class="odd">
<td><strong>D3D_BLOB_INPUT_AND_OUTPUT_SIGNATURE_BLOB</strong></td>
<td>The blob part is an input and output signature.<br/></td>

</tr>
<tr class="even">
<td><strong>D3D_BLOB_PATCH_CONSTANT_SIGNATURE_BLOB</strong></td>
<td>The blob part is a patch constant signature.<br/></td>

</tr>
<tr class="odd">
<td><strong>D3D_BLOB_ALL_SIGNATURE_BLOB</strong></td>
<td>The blob part is all signature.<br/></td>

</tr>
<tr class="even">
<td><strong>D3D_BLOB_DEBUG_INFO</strong></td>
<td>The blob part is debug information.<br/></td>

</tr>
<tr class="odd">
<td><strong>D3D_BLOB_LEGACY_SHADER</strong></td>
<td>The blob part is a legacy shader.<br/></td>

</tr>
<tr class="even">
<td><strong>D3D_BLOB_XNA_PREPASS_SHADER</strong></td>
<td>The blob part is an XNA prepass shader.<br/></td>

</tr>
<tr class="odd">
<td><strong>D3D_BLOB_XNA_SHADER</strong></td>
<td>The blob part is an XNA shader.<br/></td>

</tr>
<tr class="even">
<td><strong>D3D_BLOB_PDB</strong></td>
<td>The blob part is program database (PDB) information.<br/>
<blockquote>
[!Note]<br />
This value is supported by the D3dcompiler_44.dll or later version of the file.
</blockquote>
<br/></td>

</tr>
<tr class="odd">
<td><strong>D3D_BLOB_PRIVATE_DATA</strong></td>
<td>The blob part is private data.<br/>
<blockquote>
[!Note]<br />
This value is supported by the D3dcompiler_44.dll or later version of the file.
</blockquote>
<br/></td>

</tr>
<tr class="even">
<td><strong>D3D_BLOB_ROOT_SIGNATURE</strong></td>
<td>The blob part is a root signature. Refer to [Specifying Root Signatures in HLSL](https://msdn.microsoft.com/library/windows/desktop/dn913202) for more information on using Direct3D12 with HLSL.<br/>
<blockquote>
[!Note]<br />
This value is supported by the D3dcompiler_47.dll or later version of the file.
</blockquote>
<br/></td>

</tr>
<tr class="odd">
<td><strong>D3D_BLOB_DEBUG_NAME</strong></td>
<td>The blob part is the debug name of the shader. If the application does not specify the debug name itself, an auto-generated name matching the PDB file of the shader is provided instead.<br/>
<blockquote>
[!Note]<br />
This value is supported by the D3dcompiler_47.dll as available on the Windows 10 Fall Creators Update and its SDK, or later version of the file.
</blockquote>
<br/></td>

</tr>
<tr class="even">
<td><strong>D3D_BLOB_TEST_ALTERNATE_SHADER</strong></td>
<td>The blob part is a test alternate shader.<br/>
<blockquote>
[!Note]<br />
This value identifies a test part and is only produced by special compiler versions. Therefore, this part type is typically not present in shaders.
</blockquote>
<br/></td>
<td>0x8000</td>
</tr>
<tr class="odd">
<td><strong>D3D_BLOB_TEST_COMPILE_DETAILS</strong></td>
<td>The blob part is test compilation details.<br/>
<blockquote>
[!Note]<br />
This value identifies a test part and is only produced by special compiler versions. Therefore, this part type is typically not present in shaders.
</blockquote>
<br/></td>

</tr>
<tr class="even">
<td><strong>D3D_BLOB_TEST_COMPILE_PERF</strong></td>
<td>The blob part is test compilation performance.<br/>
<blockquote>
[!Note]<br />
This value identifies a test part and is only produced by special compiler versions. Therefore, this part type is typically not present in shaders.
</blockquote>
<br/></td>

</tr>
<tr class="odd">
<td><strong>D3D_BLOB_TEST_COMPILE_REPORT</strong></td>
<td>The blob part is a test compilation report.<br/>
<blockquote>
[!Note]<br />
This value identifies a test part and is only produced by special compiler versions. Therefore, this part type is typically not present in shaders.
</blockquote>
<br/>
<blockquote>
[!Note]<br />
This value is supported by the D3dcompiler_44.dll or later version of the file.
</blockquote>
<br/></td>

</tr>
</tbody>
</table>



## Remarks

These values are passed to the [**D3DGetBlobPart**](d3dgetblobpart.md) or [**D3DSetBlobPart**](d3dsetblobpart.md) function.

## Requirements



|                   |                                                                                          |
|-------------------|------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3Dcompiler.h</dt> </dl> |



## See also

<dl> <dt>

[Enumerations](dx-graphics-d3dcompiler-reference-enums.md)
</dt> </dl>

 

 





