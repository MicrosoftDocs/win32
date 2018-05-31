---
title: IVMHostInfo ProcessorSpeedString property
description: The ProcessorSpeedString property contains the speed, in megahertz, of the host processor.
ms.assetid: ca9eee46-1062-44be-9fd3-ee2df58746f4
keywords:
- ProcessorSpeedString property Virtual Server
- ProcessorSpeedString property Virtual Server , IVMHostInfo interface
- IVMHostInfo interface Virtual Server , ProcessorSpeedString property
- ProcessorSpeedString property Virtual Server , VMHostInfo interface
- VMHostInfo interface Virtual Server , ProcessorSpeedString property
topic_type:
- apiref
api_name:
- IVMHostInfo.ProcessorSpeedString
- IVMHostInfo.get_ProcessorSpeedString
- VMHostInfo.ProcessorSpeedString
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IVMHostInfo::ProcessorSpeedString property

The **ProcessorSpeedString** property contains the speed, in megahertz, of the host processor.

This property is read-only.

## Syntax


```C++
HRESULT get_ProcessorSpeedString(
  [out] BSTR *processorSpeedString
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
<td><pre><code>VMHostInfo.ProcessorSpeedString( _
  ByRef processorSpeedString _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The speed, in megahertz, of the host processor.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                        |
|-----------------------------------------------------------------------------------------------|------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>       |
| <dl> <dt>E\_POINTER</dt> </dl>         | The outgoing parameter is **NULL**.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>       |



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

 

 





