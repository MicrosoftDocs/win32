---
title: IVMHostInfo SSE property
description: The SSE property contains whether the host processor supports the SSE instruction set.
ms.assetid: '2be1ee35-20ba-4050-933c-7cee0e765de7'
keywords: ["SSE property Virtual Server", "SSE property Virtual Server , IVMHostInfo interface", "IVMHostInfo interface Virtual Server , SSE property", "SSE property Virtual Server , VMHostInfo interface", "VMHostInfo interface Virtual Server , SSE property"]
topic_type:
- apiref
api_name:
- IVMHostInfo.SSE
- IVMHostInfo.get_SSE
- VMHostInfo.SSE
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMHostInfo::SSE property

The **SSE** property contains whether the host processor supports the SSE instruction set.

This property is read-only.

## Syntax


```C++
HRESULT get_SSE(
  [out] VARIANT_BOOL *sseEnabled
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
<td><pre><code>VMHostInfo.SSE( _
  ByRef sseEnabled _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Contains **vbTrue** if SSE instructions are supported by the host processor, **vbFalse** otherwise.

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
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMHostInfo**](ivmhostinfo.md)
</dt> </dl>

 

 





