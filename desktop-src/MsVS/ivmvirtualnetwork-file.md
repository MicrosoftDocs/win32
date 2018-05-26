---
title: IVMVirtualNetwork File property
description: The File property retrieves the full path to the virtual networks configuration file.
ms.assetid: b3382e1f-d5b4-41ef-b32b-09c4be342fc2
keywords:
- File property Virtual Server
- File property Virtual Server , IVMVirtualNetwork interface
- IVMVirtualNetwork interface Virtual Server , File property
- File property Virtual Server , VMVirtualNetwork class
- VMVirtualNetwork class Virtual Server , File property
topic_type:
- apiref
api_name:
- IVMVirtualNetwork.File
- IVMVirtualNetwork.get_File
- VMVirtualNetwork.File
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

# IVMVirtualNetwork::File property

The **File** property retrieves the full path to the virtual network's configuration file.

This property is read-only.

## Syntax


```C++
HRESULT get_File(
  [out] BSTR *file
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
<td><pre><code>VMVirtualNetwork.File( _
  ByRef file _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The full path to the virtual network's configuration file.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                       |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>      |
| <dl> <dt>E\_POINTER</dt> </dl>         | The parameter *file* was **NULL**.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>  |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualNetwork**](ivmvirtualnetwork.md)
</dt> </dl>

 

 





