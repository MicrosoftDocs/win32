---
title: IVMHostInfo UTCTime property
description: The UTCTime property contains the current UTC time on the host machine.
ms.assetid: '50fbac09-8dcf-4c7c-abf4-527b50d6514f'
keywords: ["UTCTime property Virtual Server", "UTCTime property Virtual Server , IVMHostInfo interface", "IVMHostInfo interface Virtual Server , UTCTime property", "UTCTime property Virtual Server , VMHostInfo interface", "VMHostInfo interface Virtual Server , UTCTime property"]
topic_type:
- apiref
api_name:
- IVMHostInfo.UTCTime
- IVMHostInfo.get_UTCTime
- VMHostInfo.UTCTime
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMHostInfo::UTCTime property

The **UTCTime** property contains the current UTC time on the host machine.

This property is read-only.

## Syntax


```C++
HRESULT get_UTCTime(
  [out] DATE *UTCTime
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
<td><pre><code>VMHostInfo.UTCTime( _
  ByRef UTCTime _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The current UTC time on the host machine.

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
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMHostInfo**](ivmhostinfo.md)
</dt> </dl>

 

 





