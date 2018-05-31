---
title: IVMRCClientControl MenuFontFace property
description: The MenuFontFace property contains client's menu font face.
ms.assetid: 008ac709-0e08-4969-b28d-c74a69ecf5a3
keywords:
- MenuFontFace property Virtual Server
- MenuFontFace property Virtual Server , IVMRCClientControl interface
- IVMRCClientControl interface Virtual Server , MenuFontFace property
- MenuFontFace property Virtual Server , VMRCClientControl interface
- VMRCClientControl interface Virtual Server , MenuFontFace property
topic_type:
- apiref
api_name:
- IVMRCClientControl.MenuFontFace
- IVMRCClientControl.get_MenuFontFace
- IVMRCClientControl.put_MenuFontFace
- VMRCClientControl.MenuFontFace
api_location:
- VMRCClientControl.lib
- VMRCClientControl.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IVMRCClientControl::MenuFontFace property

The **MenuFontFace** property contains client's menu font face.

This property is read/write.

## Syntax


```C++
HRESULT put_MenuFontFace(
  [in]  BSTR menuFontFace
);

HRESULT get_MenuFontFace(
  [out] BSTR *menuFontFace
);
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
<td><pre><code>VMRCClientControl.MenuFontFace( _
  ByRef menuFontFace, _
  ByVal menuFontFace _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The client's menu font face.

This property value is read/write.

## Error codes



| Name                                                                                     | Meaning                                                  |
|------------------------------------------------------------------------------------------|----------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>         | The operation was successful.<br/>                 |
| <dl> <dt>S\_FALSE</dt> </dl>      | This property cannot be changed at this time.<br/> |
| <dl> <dt>E\_INVALIDARG</dt> </dl> | The *menuFontFace* parameter was **NULL**.<br/>    |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VMRCClientControl.h</dt> </dl>    |
| Library<br/>  | <dl> <dt>VMRCClientControl.lib</dt> </dl>  |



## See also

<dl> <dt>

[**IVMRCClientControl**](ivmrcclientcontrol.md)
</dt> </dl>

 

 





