---
title: IVMRCClientControl Enabled property
description: The Enabled property indicates whether the control is enabled.
ms.assetid: 9a11d10e-45e9-4131-9491-0a06a0fd3845
keywords:
- Enabled property Virtual Server
- Enabled property Virtual Server , IVMRCClientControl interface
- IVMRCClientControl interface Virtual Server , Enabled property
- Enabled property Virtual Server , VMRCClientControl interface
- VMRCClientControl interface Virtual Server , Enabled property
topic_type:
- apiref
api_name:
- IVMRCClientControl.Enabled
- IVMRCClientControl.get_Enabled
- IVMRCClientControl.put_Enabled
- VMRCClientControl.Enabled
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

# IVMRCClientControl::Enabled property

The **Enabled** property indicates whether the control is enabled.

This property is read/write.

## Syntax


```C++
HRESULT put_Enabled(
  [in]  VARIANT_BOOL enabled
);

HRESULT get_Enabled(
  [out] VARIANT_BOOL *enabled
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
<td><pre><code>VMRCClientControl.Enabled( _
  ByRef enabled, _
  ByVal enabled _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Contains **vbTrue** if the control is enabled.

This property value is read/write.

## Error codes



| Name                                                                                     | Meaning                                          |
|------------------------------------------------------------------------------------------|--------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>         | The operation was successful.<br/>         |
| <dl> <dt>E\_INVALIDARG</dt> </dl> | The *enabled* parameter was **NULL**.<br/> |



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

 

 





