---
title: IVMRCClientControl ViewOnlyMode property
description: The ViewOnlyMode property indicates whether the client's view-only mode is enabled.
ms.assetid: 41b903d9-2b0c-455f-858b-23b50c9ba787
keywords:
- ViewOnlyMode property Virtual Server
- ViewOnlyMode property Virtual Server , IVMRCClientControl interface
- IVMRCClientControl interface Virtual Server , ViewOnlyMode property
- ViewOnlyMode property Virtual Server , VMRCClientControl interface
- VMRCClientControl interface Virtual Server , ViewOnlyMode property
topic_type:
- apiref
api_name:
- IVMRCClientControl.ViewOnlyMode
- IVMRCClientControl.get_ViewOnlyMode
- IVMRCClientControl.put_ViewOnlyMode
- VMRCClientControl.ViewOnlyMode
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

# IVMRCClientControl::ViewOnlyMode property

The **ViewOnlyMode** property indicates whether the client's view-only mode is enabled.

This property is read/write.

## Syntax


```C++
HRESULT put_ViewOnlyMode(
  [in]  VARIANT_BOOL viewOnlyMode
);

HRESULT get_ViewOnlyMode(
  [out] VARIANT_BOOL *viewOnlyMode
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
<td><pre><code>VMRCClientControl.ViewOnlyMode( _
  ByRef viewOnlyMode, _
  ByVal viewOnlyMode _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Contains **vbTrue** if the client's view-only mode is enabled.

This property value is read/write.

## Error codes



| Name                                                                                     | Meaning                                                  |
|------------------------------------------------------------------------------------------|----------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>         | The operation was successful.<br/>                 |
| <dl> <dt>S\_FALSE</dt> </dl>      | This property cannot be changed at this time.<br/> |
| <dl> <dt>E\_INVALIDARG</dt> </dl> | The *viewOnlyMode* parameter was **NULL**.<br/>    |



## Remarks

When the client's view-only mode is enabled, no user input is sent from the client to the VMRC server.

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

 

 





