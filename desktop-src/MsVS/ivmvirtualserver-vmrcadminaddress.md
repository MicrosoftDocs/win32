---
title: IVMVirtualServer VMRCAdminAddress property
description: The VMRCAdminAddress property contains the TCP/IP address of the host network adapter over which VMRC connections are accepted.
ms.assetid: 9f960363-6c2e-4ed2-b3cb-3dc72fbed318
keywords:
- VMRCAdminAddress property Virtual Server
- VMRCAdminAddress property Virtual Server , IVMVirtualServer interface
- IVMVirtualServer interface Virtual Server , VMRCAdminAddress property
- VMRCAdminAddress property Virtual Server , VMVirtualServer class
- VMVirtualServer class Virtual Server , VMRCAdminAddress property
topic_type:
- apiref
api_name:
- IVMVirtualServer.VMRCAdminAddress
- IVMVirtualServer.get_VMRCAdminAddress
- IVMVirtualServer.put_VMRCAdminAddress
- VMVirtualServer.VMRCAdminAddress
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

# IVMVirtualServer::VMRCAdminAddress property

The **VMRCAdminAddress** property contains the TCP/IP address of the host network adapter over which VMRC connections are accepted.

This property is read/write.

## Syntax


```C++
HRESULT put_VMRCAdminAddress(
  [in]  BSTR vmrcAdminAddress
);

HRESULT get_VMRCAdminAddress(
  [out] BSTR *vmrcAdminAddress
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
<td><pre><code>VMVirtualServer.VMRCAdminAddress( _
  ByRef vmrcAdminAddress, _
  ByVal vmrcAdminAddress _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The TCP/IP address of the host network adapter over which VMRC administration connections are accepted.

This property value is read/write.

## Error codes



| Name                                                                                          | Meaning                                                                                 |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                                                |
| <dl> <dt>E\_POINTER</dt> </dl>         | The parameter *vmrcAdminAddress* referenced **NULL**.<br/>                        |
| <dl> <dt>E\_INVALIDARG</dt> </dl>      | The parameter *vmrcAdminAddress* is not a valid TCP/IP address for the host.<br/> |
| <dl> <dt>E\_OUTOFMEMORY</dt> </dl>     | There is insufficient memory to retrieve the address.<br/>                        |
| <dl> <dt>E\_FAIL</dt> </dl>            | The address could not be retrieved.<br/>                                          |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>                                                |



## Remarks

If this property retrieves a zero-length string, the VMRC connections are accepted from all host network interfaces.

Setting this property to a zero-length string allows VMRC connections to be accepted from all host network interfaces.

## Examples

The following example displays the **VMRCAdminAddress** property value of the [**VMVirtualServer**](ivmvirtualserver.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")
Wscript.Echo "Name: " & objVS.Name

If objVS.VMRCAdminAddress = "" Then
  Wscript.Echo "VMRC admin address: [all]"
Else
  Wscript.Echo "VMRC admin address: " & objVS.VMRCAdminAddress
End If
```



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualServer**](ivmvirtualserver.md)
</dt> </dl>

 

 





