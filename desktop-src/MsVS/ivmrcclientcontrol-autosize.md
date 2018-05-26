---
title: IVMRCClientControl AutoSize property
description: The AutoSize property indicates whether the control determines its own size.
ms.assetid: ad825bd7-f124-4e79-b5cd-58a031e2c255
keywords:
- AutoSize property Virtual Server
- AutoSize property Virtual Server , IVMRCClientControl interface
- IVMRCClientControl interface Virtual Server , AutoSize property
- AutoSize property Virtual Server , VMRCClientControl interface
- VMRCClientControl interface Virtual Server , AutoSize property
topic_type:
- apiref
api_name:
- IVMRCClientControl.AutoSize
- IVMRCClientControl.get_AutoSize
- IVMRCClientControl.put_AutoSize
- VMRCClientControl.AutoSize
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

# IVMRCClientControl::AutoSize property

The **AutoSize** property indicates whether the control determines its own size.

This property is read/write.

## Syntax


```C++
HRESULT put_AutoSize(
  [in]  VARIANT_BOOL autoSize
);

HRESULT get_AutoSize(
  [out] VARIANT_BOOL *autoSize
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
<td><pre><code>VMRCClientControl.AutoSize( _
  ByRef autoSize, _
  ByVal autoSize _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Contains **vbTrue** if the control determines its own size.

This property value is read/write.

## Error codes



| Name                                                                                     | Meaning                                           |
|------------------------------------------------------------------------------------------|---------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>         | The operation was successful.<br/>          |
| <dl> <dt>E\_INVALIDARG</dt> </dl> | The *autoSize* parameter was **NULL**.<br/> |



## Remarks

The current implementation of the VMRC Client control ignores attempts to enable or disable auto-sizing. The control always determines its own size and always returns **TRUE** when this property is read.

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

 

 





