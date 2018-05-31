---
title: IVMVirtualNetwork Security property
description: The Security property contains the IVMSecurity object associated with the virtual network.
ms.assetid: 7d92935f-3ac6-44a6-b367-bae596b4c285
keywords:
- Security property Virtual Server
- Security property Virtual Server , IVMVirtualNetwork interface
- IVMVirtualNetwork interface Virtual Server , Security property
- Security property Virtual Server , VMVirtualNetwork class
- VMVirtualNetwork class Virtual Server , Security property
topic_type:
- apiref
api_name:
- IVMVirtualNetwork.Security
- IVMVirtualNetwork.get_Security
- VMVirtualNetwork.Security
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

# IVMVirtualNetwork::Security property

The **Security** property contains the [**IVMSecurity**](ivmsecurity.md) object associated with the virtual network.

This property is read-only.

## Syntax


```C++
HRESULT get_Security(
  [out] IVMSecurity **outSecurity
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
<td><pre><code>VMVirtualNetwork.Security( _
  ByRef outSecurity _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The [**VMSecurity**](ivmsecurity.md) object which defines the security attributes of the virtual network.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                                           |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                          |
| <dl> <dt>E\_POINTER</dt> </dl>         | The parameter *outSecurity* is **NULL**.<br/>               |
| <dl> <dt>E\_OUTOFMEMORY</dt> </dl>     | Could not allocate memory for the security descriptor.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>                          |



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

 

 





