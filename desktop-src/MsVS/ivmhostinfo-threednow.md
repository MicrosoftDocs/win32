---
title: IVMHostInfo ThreeDNow property
description: The ThreeDNow property contains whether the host processor supports the 3DNow instruction set.
ms.assetid: '4d7385d4-e1a7-4fd2-a2c8-5f77a1dc5b21'
keywords: ["ThreeDNow property Virtual Server", "ThreeDNow property Virtual Server , IVMHostInfo interface", "IVMHostInfo interface Virtual Server , ThreeDNow property", "ThreeDNow property Virtual Server , VMHostInfo interface", "VMHostInfo interface Virtual Server , ThreeDNow property"]
topic_type:
- apiref
api_name:
- IVMHostInfo.ThreeDNow
- IVMHostInfo.get_ThreeDNow
- VMHostInfo.ThreeDNow
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMHostInfo::ThreeDNow property

The **ThreeDNow** property contains whether the host processor supports the 3DNow! instruction set.

This property is read-only.

## Syntax


```C++
HRESULT get_ThreeDNow(
  [out] VARIANT_BOOL *threeDNowEnabled
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
<td><pre><code>VMHostInfo.ThreeDNow( _
  ByRef threeDNowEnabled _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Contains **vbTrue** if 3DNow! instructions are supported by the host processor, **vbFalse** otherwise.

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

 

 





