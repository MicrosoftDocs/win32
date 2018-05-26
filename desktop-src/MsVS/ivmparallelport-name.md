---
title: IVMParallelPort Name property
description: The Name property contains the name of the parallel port.
ms.assetid: d67f25e6-2c64-4d17-8eb8-9f71bda180eb
keywords:
- Name property Virtual Server
- Name property Virtual Server , IVMParallelPort interface
- IVMParallelPort interface Virtual Server , Name property
- Name property Virtual Server , VMParallelPort interface
- VMParallelPort interface Virtual Server , Name property
topic_type:
- apiref
api_name:
- IVMParallelPort.Name
- IVMParallelPort.get_Name
- IVMParallelPort.put_Name
- VMParallelPort.Name
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

# IVMParallelPort::Name property

The **Name** property contains the name of the parallel port.

This property is read/write.

## Syntax


```C++
HRESULT put_Name(
  [in]  BSTR portName
);

HRESULT get_Name(
  [out] BSTR *portName
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
<td><pre><code>VMParallelPort.Name( _
  ByRef portName, _
  ByVal portName _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The name of the parallel port (for example, "LPT1").

This property value is read/write.

## Error codes



| Name                                                                                           | Meaning                                                                 |
|------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>               | The operation was successful.<br/>                                |
| <dl> <dt>E\_POINTER</dt> </dl>          | The *portName* parameter is **NULL**.<br/>                        |
| <dl> <dt>E\_INVALIDARG</dt> </dl>       | The *portName* parameter refers to an invalid parallel port.<br/> |
| <dl> <dt> VM\_E\_VM\_UNKNOWN</dt> </dl> | The configuration is unknown.<br/>                                |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl>  | An unexpected error occurred.<br/>                                |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMParallelPort**](ivmparallelport.md)
</dt> </dl>

 

 





