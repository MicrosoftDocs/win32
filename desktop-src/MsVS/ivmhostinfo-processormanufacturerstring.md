---
title: IVMHostInfo ProcessorManufacturerString property
description: The ProcessorManufacturerString property contains the manufacturer of the host processor.
ms.assetid: 05c64080-bbbc-4861-b6be-573301490ba5
keywords:
- ProcessorManufacturerString property Virtual Server
- ProcessorManufacturerString property Virtual Server , IVMHostInfo interface
- IVMHostInfo interface Virtual Server , ProcessorManufacturerString property
- ProcessorManufacturerString property Virtual Server , VMHostInfo interface
- VMHostInfo interface Virtual Server , ProcessorManufacturerString property
topic_type:
- apiref
api_name:
- IVMHostInfo.ProcessorManufacturerString
- IVMHostInfo.get_ProcessorManufacturerString
- VMHostInfo.ProcessorManufacturerString
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

# IVMHostInfo::ProcessorManufacturerString property

The **ProcessorManufacturerString** property contains the manufacturer of the host processor.

This property is read-only.

## Syntax


```C++
HRESULT get_ProcessorManufacturerString(
  [out] BSTR *processorManufacturerString
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
<td><pre><code>VMHostInfo.ProcessorManufacturerString( _
  ByRef processorManufacturerString _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The manufacturer of the host processor.

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

 

 





