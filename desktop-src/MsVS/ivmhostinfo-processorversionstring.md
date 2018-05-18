---
title: IVMHostInfo ProcessorVersionString property
description: The ProcessorVersionString property contains the version of the host processor.
ms.assetid: '05981a13-a6a2-4c92-becb-ed05c0b07bf7'
keywords: ["ProcessorVersionString property Virtual Server", "ProcessorVersionString property Virtual Server , IVMHostInfo interface", "IVMHostInfo interface Virtual Server , ProcessorVersionString property", "ProcessorVersionString property Virtual Server , VMHostInfo interface", "VMHostInfo interface Virtual Server , ProcessorVersionString property"]
topic_type:
- apiref
api_name:
- IVMHostInfo.ProcessorVersionString
- IVMHostInfo.get_ProcessorVersionString
- VMHostInfo.ProcessorVersionString
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMHostInfo::ProcessorVersionString property

The **ProcessorVersionString** property contains the version of the host processor.

This property is read-only.

## Syntax


```C++
HRESULT get_ProcessorVersionString(
  [out] BSTR *processorVersionString
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
<td><pre><code>VMHostInfo.ProcessorVersionString( _
  ByRef processorVersionString _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The version of the host processor.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                        |
|-----------------------------------------------------------------------------------------------|------------------------------------------------|
| <dl> <dt> S\_OK</dt> </dl>             | The operation was successful.<br/>       |
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

 

 





