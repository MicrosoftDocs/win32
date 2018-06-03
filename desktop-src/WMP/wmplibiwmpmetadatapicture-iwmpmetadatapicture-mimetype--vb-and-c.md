---
title: IWMPMetadataPicture mimeType property
description: The mimeType property gets the MIME type of the image represented by the metadata attribute.
ms.assetid: 3ddd7f20-a183-4b95-bdcf-5497349f6db6
keywords:
- mimeType property Windows Media Player
- mimeType property Windows Media Player , IWMPMetadataPicture interface
- IWMPMetadataPicture interface Windows Media Player , mimeType property
topic_type:
- apiref
api_name:
- IWMPMetadataPicture.mimeType
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IWMPMetadataPicture::mimeType property

The `mimeType` property gets the MIME type of the image represented by the metadata attribute.

## Syntax


```CSharp
public System.String mimeType {get; set;}
```

<span codelanguage="VisualBasic"></span>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>VB</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>Public ReadOnly Property mimeType As System.String</code></pre></td>
</tr>
</tbody>
</table>



## Property value

A **System.String** that is the MIME type of the image.

## Remarks

Before using this property, you must have read access to the library. For more information, see [Library Access](library-access.md).

## Requirements



|                      |                                                                                                                        |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                      |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPMetadataPicture Interface (VB and C#)**](iwmpmetadatapicture--vb-and-c.md)
</dt> </dl>

 

 





