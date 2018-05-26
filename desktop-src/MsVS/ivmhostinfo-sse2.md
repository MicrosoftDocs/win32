---
title: IVMHostInfo SSE2 property
description: The SSE2 property contains whether the host processor supports the SSE2 instruction set.
ms.assetid: 2b4123d3-bbd8-44a9-a74c-8e085841aa3d
keywords:
- SSE2 property Virtual Server
- SSE2 property Virtual Server , IVMHostInfo interface
- IVMHostInfo interface Virtual Server , SSE2 property
- SSE2 property Virtual Server , VMHostInfo interface
- VMHostInfo interface Virtual Server , SSE2 property
topic_type:
- apiref
api_name:
- IVMHostInfo.SSE2
- IVMHostInfo.get_SSE2
- VMHostInfo.SSE2
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

# IVMHostInfo::SSE2 property

The **SSE2** property contains whether the host processor supports the SSE2 instruction set.

This property is read-only.

## Syntax


```C++
HRESULT get_SSE2(
  [out] VARIANT_BOOL *sse2Enabled
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
<td><pre><code>VMHostInfo.SSE2( _
  ByRef sse2Enabled _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Contains **vbTrue** if SSE2 instructions are supported by the host processor, **vbFalse** otherwise.

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

 

 





