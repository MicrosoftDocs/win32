---
title: IVMRCClientControl MenuHeight property
description: The MenuHeight property contains the height of the clients menu in pixels.
ms.assetid: 24ec940b-5e14-4d97-9419-4c0c5851ca54
keywords:
- MenuHeight property Virtual Server
- MenuHeight property Virtual Server , IVMRCClientControl interface
- IVMRCClientControl interface Virtual Server , MenuHeight property
- MenuHeight property Virtual Server , VMRCClientControl interface
- VMRCClientControl interface Virtual Server , MenuHeight property
topic_type:
- apiref
api_name:
- IVMRCClientControl.MenuHeight
- IVMRCClientControl.get_MenuHeight
- IVMRCClientControl.put_MenuHeight
- VMRCClientControl.MenuHeight
api_location:
- VMRCClientControl.lib
- VMRCClientControl.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IVMRCClientControl::MenuHeight property

The **MenuHeight** property contains the height of the client's menu in pixels.

This property is read/write.

## Syntax


```C++
HRESULT put_MenuHeight(
  [in]  long menuHeight
);

HRESULT get_MenuHeight(
  [out] long *menuHeight
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
<td><pre><code>VMRCClientControl.MenuHeight( _
  ByRef menuHeight, _
  ByVal menuHeight _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The height of the client's menu in pixels.

This property value is read/write.

## Error codes



| Name                                                                                     | Meaning                                                  |
|------------------------------------------------------------------------------------------|----------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>         | The operation was successful.<br/>                 |
| <dl> <dt>S\_FALSE</dt> </dl>      | This property cannot be changed at this time.<br/> |
| <dl> <dt>E\_INVALIDARG</dt> </dl> | The *menuHeight* parameter was **NULL**.<br/>      |



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

 

 





