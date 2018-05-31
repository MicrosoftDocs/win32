---
title: IVMRCClientControl MenuFontSize property
description: The MenuFontSize property contains the client's menu font size..
ms.assetid: 214293e4-4b28-439f-a281-7a42fb055cbb
keywords:
- MenuFontSize property Virtual Server
- MenuFontSize property Virtual Server , IVMRCClientControl interface
- IVMRCClientControl interface Virtual Server , MenuFontSize property
- MenuFontSize property Virtual Server , VMRCClientControl interface
- VMRCClientControl interface Virtual Server , MenuFontSize property
topic_type:
- apiref
api_name:
- IVMRCClientControl.MenuFontSize
- IVMRCClientControl.get_MenuFontSize
- IVMRCClientControl.put_MenuFontSize
- VMRCClientControl.MenuFontSize
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

# IVMRCClientControl::MenuFontSize property

The **MenuFontSize** property contains the client's menu font size..

This property is read/write.

## Syntax


```C++
HRESULT put_MenuFontSize(
  [in]  long menuFontSize
);

HRESULT get_MenuFontSize(
  [out] long *menuFontSize
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
<td><pre><code>VMRCClientControl.MenuFontSize( _
  ByRef menuFontSize, _
  ByVal menuFontSize _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The client's menu font size.

This property value is read/write.

## Error codes



| Name                                                                                     | Meaning                                                  |
|------------------------------------------------------------------------------------------|----------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>         | The operation was successful.<br/>                 |
| <dl> <dt>S\_FALSE</dt> </dl>      | This property cannot be changed at this time.<br/> |
| <dl> <dt>E\_INVALIDARG</dt> </dl> | The *menuFontSize* parameter was **NULL**.<br/>    |



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

 

 





