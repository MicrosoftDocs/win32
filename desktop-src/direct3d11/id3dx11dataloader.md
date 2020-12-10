---
title: ID3DX11DataLoader interface (D3DX11core.h)
description: Note The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps. Data loading object used by ID3DX11ThreadPump Interface for loading data asynchronously.
ms.assetid: 878929ea-0228-4650-9ca0-f83d60d9f915
keywords:
- ID3DX11DataLoader interface Direct3D 11
- ID3DX11DataLoader interface Direct3D 11 , described
topic_type:
- apiref
api_name:
- ID3DX11DataLoader
api_location:
- D3DX11.lib
- D3DX11.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ID3DX11DataLoader interface

> [!Note]  
> The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.

 

Data loading object used by [**ID3DX11ThreadPump Interface**](id3dx11threadpump.md) for loading data asynchronously.

## Members

The **ID3DX11DataLoader** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **ID3DX11DataLoader** also has these types of members:

-   [Methods](#methods)

### Methods

The **ID3DX11DataLoader** interface has these methods.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: left;">Method</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;"><a href="id3dx11dataloader-decompress.md"><strong>Decompress</strong></a></td>
<td style="text-align: left;"><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.
</blockquote>
<br/> Decompresses encoded data.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="id3dx11dataloader-destroy.md"><strong>Destroy</strong></a></td>
<td style="text-align: left;"><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.
</blockquote>
<br/> Destroys the loader after a work item completes.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="id3dx11dataloader-load.md"><strong>Load</strong></a></td>
<td style="text-align: left;"><blockquote>
[!Note]<br />
The D3DX (D3DX 9, D3DX 10, and D3DX 11) utility library is deprecated for Windows 8 and is not supported for Windows Store apps.
</blockquote>
<br/> Loads data from a disk.<br/></td>
</tr>
</tbody>
</table>



 

## Remarks

This object can be inherited and its members redefined. Doing so would enable you to customize the API for loading and decompressing your own custom file formats.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>D3DX11core.h</dt> </dl> |
| Library<br/>                  | <dl> <dt>D3DX11.lib</dt> </dl>   |



## See also

<dl> <dt>

[D3DX Interfaces](d3d11-graphics-reference-d3dx11-interfaces.md)
</dt> </dl>

 

