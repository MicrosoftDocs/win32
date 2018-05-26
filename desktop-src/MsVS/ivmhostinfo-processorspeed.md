---
title: IVMHostInfo ProcessorSpeed property
description: The ProcessorSpeed property contains the speed, in megahertz, of the host processor.
ms.assetid: 93baebe0-050e-498b-8f2d-be6b49938dee
keywords:
- ProcessorSpeed property Virtual Server
- ProcessorSpeed property Virtual Server , IVMHostInfo interface
- IVMHostInfo interface Virtual Server , ProcessorSpeed property
- ProcessorSpeed property Virtual Server , VMHostInfo interface
- VMHostInfo interface Virtual Server , ProcessorSpeed property
topic_type:
- apiref
api_name:
- IVMHostInfo.ProcessorSpeed
- IVMHostInfo.get_ProcessorSpeed
- VMHostInfo.ProcessorSpeed
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IVMHostInfo::ProcessorSpeed property

The **ProcessorSpeed** property contains the speed, in megahertz, of the host processor.

This property is read-only.

## Syntax


```C++
HRESULT get_ProcessorSpeed(
  [out] long *processorSpeed
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
<td><pre><code>VMHostInfo.ProcessorSpeed( _
  ByRef processorSpeed _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The speed, in megahertz, of the host processor.

This property value is read-only.

## Error codes



| Name                                                                                           | Meaning                                        |
|------------------------------------------------------------------------------------------------|------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>               | The operation was successful.<br/>       |
| <dl> <dt>E\_POINTER</dt> </dl>          | The outgoing parameter is **NULL**.<br/> |
| <dl> <dt> DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>       |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMHostInfo**](ivmhostinfo.md)
</dt> </dl>

 

 





