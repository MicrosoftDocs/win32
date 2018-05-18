---
title: IVMHostInfo NetworkAdapters property
description: The NetworkAdapters property contains an enumerable collection of the network interface cards that are installed on the host machine.
ms.assetid: 'f5d2a9ea-ce7c-41fe-be12-99504d50f80d'
keywords: ["NetworkAdapters property Virtual Server", "NetworkAdapters property Virtual Server , IVMHostInfo interface", "IVMHostInfo interface Virtual Server , NetworkAdapters property", "NetworkAdapters property Virtual Server , VMHostInfo interface", "VMHostInfo interface Virtual Server , NetworkAdapters property"]
topic_type:
- apiref
api_name:
- IVMHostInfo.NetworkAdapters
- IVMHostInfo.get_NetworkAdapters
- VMHostInfo.NetworkAdapters
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMHostInfo::NetworkAdapters property

The **NetworkAdapters** property contains an enumerable collection of the network interface cards that are installed on the host machine.

This property is read-only.

## Syntax


```C++
HRESULT get_NetworkAdapters(
  [out] VARIANT *hostNICs
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
<td><pre><code>VMHostInfo.NetworkAdapters( _
  ByRef hostNICs _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Contains a collection of the network interface cards that are installed on the host machine.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                        |
|-----------------------------------------------------------------------------------------------|------------------------------------------------|
| <dl> <dt> S\_OK</dt> </dl>             | The operation was successful.<br/>       |
| <dl> <dt> E\_POINTER</dt> </dl>        | The outgoing parameter is **NULL**.<br/> |
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

 

 





