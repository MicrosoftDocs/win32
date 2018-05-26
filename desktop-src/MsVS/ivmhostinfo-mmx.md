---
title: IVMHostInfo MMX property
description: The MMX property contains whether the host processor supports the MMX instruction set.
ms.assetid: 248593ae-0be0-4be4-965d-af027f48b180
keywords:
- MMX property Virtual Server
- MMX property Virtual Server , IVMHostInfo interface
- IVMHostInfo interface Virtual Server , MMX property
- MMX property Virtual Server , VMHostInfo interface
- VMHostInfo interface Virtual Server , MMX property
topic_type:
- apiref
api_name:
- IVMHostInfo.MMX
- IVMHostInfo.get_MMX
- VMHostInfo.MMX
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

# IVMHostInfo::MMX property

The **MMX** property contains whether the host processor supports the MMX instruction set.

This property is read-only.

## Syntax


```C++
HRESULT get_MMX(
  [out] VARIANT_BOOL *mmxEnabled
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
<td><pre><code>VMHostInfo.MMX( _
  ByRef mmxEnabled _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Contains **vbTrue** if MMX instructions are supported by the host processor, **vbFalse** otherwise.

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

 

 





