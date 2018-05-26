---
title: IVMVirtualServer VMRCEncryptionEnabled property
description: The VMRCEncryptionEnabled property contains TRUE if server administration VMRC session data is encrypted using SSL/TLS encryption.
ms.assetid: 77eb1490-224a-493f-af58-180d69b10463
keywords:
- VMRCEncryptionEnabled property Virtual Server
- VMRCEncryptionEnabled property Virtual Server , IVMVirtualServer interface
- IVMVirtualServer interface Virtual Server , VMRCEncryptionEnabled property
- VMRCEncryptionEnabled property Virtual Server , VMVirtualServer class
- VMVirtualServer class Virtual Server , VMRCEncryptionEnabled property
topic_type:
- apiref
api_name:
- IVMVirtualServer.VMRCEncryptionEnabled
- IVMVirtualServer.get_VMRCEncryptionEnabled
- IVMVirtualServer.put_VMRCEncryptionEnabled
- VMVirtualServer.VMRCEncryptionEnabled
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

# IVMVirtualServer::VMRCEncryptionEnabled property

The **VMRCEncryptionEnabled** property contains **TRUE** if server administration VMRC session data is encrypted using SSL/TLS encryption.

This property is read/write.

## Syntax


```C++
HRESULT put_VMRCEncryptionEnabled(
  [in]  VARIANT_BOOL shouldEnable
);

HRESULT get_VMRCEncryptionEnabled(
  [out] VARIANT_BOOL *isEnabled
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
<td><pre><code>VMVirtualServer.VMRCEncryptionEnabled( _
  ByRef isEnabled, _
  ByVal shouldEnable _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Contains **vbTrue** if the VMRC session data transferred over the network is to be encrypted using SSL/TLS encryption. Otherwise, VMRC session data is transferred without encryption.

This property value is read/write.

## Error codes



| Name                                                                                          | Meaning                                                               |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                              |
| <dl> <dt>E\_POINTER</dt> </dl>         | The parameter *isEnabled* is **NULL**.<br/>                     |
| <dl> <dt>E\_NOTIMPL</dt> </dl>         | SSL/TLS encryption is not supported in Virtual Server 1.0.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>                              |



## Remarks

SSL/TLS encryption is not supported in Virtual Server 1.0, attempts to set this property will always return **E\_NOTIMPL**.

## Examples

The following example displays the **VMRCEncryptionEnabled** property value of the [**VMVirtualServer**](ivmvirtualserver.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")
Wscript.Echo "Name: " & objVS.Name

Wscript.Echo "VMRC encryption enabled: " & objVS.VMRCEncryptionEnabled
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

 

 





