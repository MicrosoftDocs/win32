---
title: IVMVirtualNetwork Name property
description: The Name property contains the unique name of this virtual network.
ms.assetid: c7f964e4-7aed-42a3-8c46-70736d013b17
keywords:
- Name property Virtual Server
- Name property Virtual Server , IVMVirtualNetwork interface
- IVMVirtualNetwork interface Virtual Server , Name property
- Name property Virtual Server , VMVirtualNetwork class
- VMVirtualNetwork class Virtual Server , Name property
topic_type:
- apiref
api_name:
- IVMVirtualNetwork.Name
- IVMVirtualNetwork.get_Name
- IVMVirtualNetwork.put_Name
- VMVirtualNetwork.Name
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IVMVirtualNetwork::Name property

The **Name** property contains the unique name of this virtual network.

This property is read/write.

## Syntax


```C++
HRESULT put_Name(
  [in]  BSTR virtualNetworkName
);

HRESULT get_Name(
  [out] BSTR *virtualNetworkName
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
<td><pre><code>VMVirtualNetwork.Name( _
  ByRef virtualNetworkName, _
  ByVal virtualNetworkName _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The name of the virtual network.

This property value is read/write.

## Error codes



| Name                                                                                          | Meaning                                                           |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                          |
| <dl> <dt> E\_POINTER</dt> </dl>        | The *virtualNetworkName* parameter is **NULL**.<br/>        |
| <dl> <dt>E\_INVALIDARG</dt> </dl>      | The *virtualNetworkName* parameter is an empty string.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>                      |



## Remarks

Virtual network names are case-insensitive, for example, "MyNetwork" and "mynetwork" refer to the same virtual network.

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

 

 





