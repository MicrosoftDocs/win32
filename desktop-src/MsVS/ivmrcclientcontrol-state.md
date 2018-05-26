---
title: IVMRCClientControl State property
description: The State property contains the state of the current connection to the VMRC server.
ms.assetid: 34170dda-88f4-488f-a4b7-e56e019336e7
keywords:
- State property Virtual Server
- State property Virtual Server , IVMRCClientControl interface
- IVMRCClientControl interface Virtual Server , State property
- State property Virtual Server , VMRCClientControl interface
- VMRCClientControl interface Virtual Server , State property
topic_type:
- apiref
api_name:
- IVMRCClientControl.State
- IVMRCClientControl.get_State
- VMRCClientControl.State
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

# IVMRCClientControl::State property

The **State** property contains the state of the current connection to the VMRC server.

This property is read-only.

## Syntax


```C++
HRESULT get_State(
  [out] VMRCState *state
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
<td><pre><code>VMRCClientControl.State( _
  ByRef state _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The state of the current connection to the VMRC server.

This property value is read-only.

## Error codes



| Name                                                                                     | Meaning                                        |
|------------------------------------------------------------------------------------------|------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>         | The operation was successful.<br/>       |
| <dl> <dt>E\_INVALIDARG</dt> </dl> | The *state* parameter was **NULL**.<br/> |



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

 

 





