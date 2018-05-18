---
title: IVMRCClientControl ServerDisplayHeight property
description: The ServerDisplayHeight property contains the width of the video display area in pixels.
ms.assetid: '1f8a6744-9057-4750-9c23-fa6161fec419'
keywords: ["ServerDisplayHeight property Virtual Server", "ServerDisplayHeight property Virtual Server , IVMRCClientControl interface", "IVMRCClientControl interface Virtual Server , ServerDisplayHeight property", "ServerDisplayHeight property Virtual Server , VMRCClientControl interface", "VMRCClientControl interface Virtual Server , ServerDisplayHeight property"]
topic_type:
- apiref
api_name:
- IVMRCClientControl.ServerDisplayHeight
- IVMRCClientControl.get_ServerDisplayHeight
- VMRCClientControl.ServerDisplayHeight
api_location:
- VMRCClientControl.lib
- VMRCClientControl.dll
api_type:
- COM
---

# IVMRCClientControl::ServerDisplayHeight property

The **ServerDisplayHeight** property contains the width of the video display area in pixels.

This property is read-only.

## Syntax


```C++
HRESULT get_ServerDisplayHeight(
  [out] long *displayHeight
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
<td><pre><code>VMRCClientControl.ServerDisplayHeight( _
  ByRef displayHeight _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The height of the video display area in pixels.

This property value is read-only.

## Error codes



| Name                                                                                     | Meaning                                                |
|------------------------------------------------------------------------------------------|--------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>         | The operation was successful.<br/>               |
| <dl> <dt>E\_INVALIDARG</dt> </dl> | The *displayHeight* parameter was **NULL**.<br/> |



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

 

 





