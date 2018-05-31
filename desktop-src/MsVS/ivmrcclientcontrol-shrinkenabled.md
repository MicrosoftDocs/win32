---
title: IVMRCClientControl ShrinkEnabled property
description: Indicates whether the client's window stretches its contents to fit its size.
ms.assetid: 5aaa9d78-c643-47c2-84e0-bc124c437e53
keywords:
- ShrinkEnabled property Virtual Server
- ShrinkEnabled property Virtual Server , IVMRCClientControl interface
- IVMRCClientControl interface Virtual Server , ShrinkEnabled property
- ShrinkEnabled property Virtual Server , VMRCClientControl interface
- VMRCClientControl interface Virtual Server , ShrinkEnabled property
topic_type:
- apiref
api_name:
- IVMRCClientControl.ShrinkEnabled
- IVMRCClientControl.get_ShrinkEnabled
- IVMRCClientControl.put_ShrinkEnabled
- VMRCClientControl.ShrinkEnabled
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

# IVMRCClientControl::ShrinkEnabled property

The **ShrinkEnabled** property indicates whether the client's window stretches its contents to fit its size.

This property is read/write.

## Syntax


```C++
HRESULT put_ShrinkEnabled(
  [in]  VARIANT_BOOL stretchEnabled
);

HRESULT get_ShrinkEnabled(
  [out] VARIANT_BOOL *stretchEnabled
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
<td><pre><code>VMRCClientControl.ShrinkEnabled( _
  ByRef stretchEnabled, _
  ByVal stretchEnabled _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Contains **vbTrue** if the client's window stretches its contents to fit its size.

This property value is read/write.

## Error codes



| Name                                                                                     | Meaning                                                  |
|------------------------------------------------------------------------------------------|----------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>         | The operation was successful.<br/>                 |
| <dl> <dt>S\_FALSE</dt> </dl>      | This property cannot be changed at this time.<br/> |
| <dl> <dt>E\_INVALIDARG</dt> </dl> | The *stretchEnabled* parameter was **NULL**.<br/>  |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VMRCClientControl.h</dt> </dl>    |
| Library<br/>  | <dl> <dt>VMRCClientControl.lib</dt> </dl>  |



## See also

<dl> <dt>

[**IVMRCClientControl**](ivmrcclientcontrol.md)
</dt> </dl>

 

 





