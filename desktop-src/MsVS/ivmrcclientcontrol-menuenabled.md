---
title: IVMRCClientControl MenuEnabled property
description: The MenuEnabled property indicates whether the client's menu is displayed.
ms.assetid: 'c8afa3f8-6b43-460a-bf2d-b5dd4536de71'
keywords: ["MenuEnabled property Virtual Server", "MenuEnabled property Virtual Server , IVMRCClientControl interface", "IVMRCClientControl interface Virtual Server , MenuEnabled property", "MenuEnabled property Virtual Server , VMRCClientControl interface", "VMRCClientControl interface Virtual Server , MenuEnabled property"]
topic_type:
- apiref
api_name:
- IVMRCClientControl.MenuEnabled
- IVMRCClientControl.get_MenuEnabled
- IVMRCClientControl.put_MenuEnabled
- VMRCClientControl.MenuEnabled
api_location:
- VMRCClientControl.lib
- VMRCClientControl.dll
api_type:
- COM
---

# IVMRCClientControl::MenuEnabled property

The **MenuEnabled** property indicates whether the client's menu is displayed.

This property is read/write.

## Syntax


```C++
HRESULT put_MenuEnabled(
  [in]  VARIANT_BOOL menuEnabled
);

HRESULT get_MenuEnabled(
  [out] VARIANT_BOOL *menuEnabled
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
<td><pre><code>VMRCClientControl.MenuEnabled( _
  ByRef menuEnabled, _
  ByVal menuEnabled _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Contains **vbTrue** if the client's menu is displayed.

This property value is read/write.

## Error codes



| Name                                                                                     | Meaning                                                  |
|------------------------------------------------------------------------------------------|----------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>         | The operation was successful.<br/>                 |
| <dl> <dt>S\_FALSE</dt> </dl>      | This property cannot be changed at this time.<br/> |
| <dl> <dt>E\_INVALIDARG</dt> </dl> | The *menuEnabled* parameter was **NULL**.<br/>     |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VMRCClientControl.h</dt> </dl>    |
| Library<br/>  | <dl> <dt>VMRCClientControl.lib</dt> </dl>  |



## See also

<dl> <dt>

[**IVMRCClientControl**](ivmrcclientcontrol.md)
</dt> </dl>

 

 





