---
title: IVMRCClientControl MenuBackColor property
description: The MenuBackColor property contains the clients menu background color specified in HTML hex string format.
ms.assetid: 3b3606e2-9a4d-400b-97ca-a26377d3083b
keywords:
- MenuBackColor property Virtual Server
- MenuBackColor property Virtual Server , IVMRCClientControl interface
- IVMRCClientControl interface Virtual Server , MenuBackColor property
- MenuBackColor property Virtual Server , VMRCClientControl interface
- VMRCClientControl interface Virtual Server , MenuBackColor property
topic_type:
- apiref
api_name:
- IVMRCClientControl.MenuBackColor
- IVMRCClientControl.get_MenuBackColor
- IVMRCClientControl.put_MenuBackColor
- VMRCClientControl.MenuBackColor
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

# IVMRCClientControl::MenuBackColor property

The **MenuBackColor** property contains the client's menu background color specified in HTML hex string format.

This property is read/write.

## Syntax


```C++
HRESULT put_MenuBackColor(
  [in]  BSTR menuBackColor
);

HRESULT get_MenuBackColor(
  [out] BSTR *menuBackColor
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
<td><pre><code>VMRCClientControl.MenuBackColor( _
  ByRef menuBackColor, _
  ByVal menuBackColor _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The client's menu background color specified in HTML hex string format.

This property value is read/write.

## Error codes



| Name                                                                                     | Meaning                                                  |
|------------------------------------------------------------------------------------------|----------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>         | The operation was successful.<br/>                 |
| <dl> <dt>S\_FALSE</dt> </dl>      | This property cannot be changed at this time.<br/> |
| <dl> <dt>E\_INVALIDARG</dt> </dl> | The *menuBackColor* parameter was **NULL**.<br/>   |



## Remarks

The color is specified using the standard HTML six-digit hex string format. This is in the form of "*rrggbb*". For example, "**000000**" represents black, "**FFFFFF**" represents white, and "**FF0000**" represents red.

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

 

 





