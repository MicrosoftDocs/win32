---
title: IVMVirtualServer VMRCEncryptionCertificate property
description: The VMRCEncryptionCertificate property contains the security certificate used by SSL/TLS encryption to protect VMRC session data.
ms.assetid: d0c4c660-792f-4462-a400-80b819307a7e
keywords:
- VMRCEncryptionCertificate property Virtual Server
- VMRCEncryptionCertificate property Virtual Server , IVMVirtualServer interface
- IVMVirtualServer interface Virtual Server , VMRCEncryptionCertificate property
- VMRCEncryptionCertificate property Virtual Server , VMVirtualServer class
- VMVirtualServer class Virtual Server , VMRCEncryptionCertificate property
topic_type:
- apiref
api_name:
- IVMVirtualServer.VMRCEncryptionCertificate
- IVMVirtualServer.get_VMRCEncryptionCertificate
- IVMVirtualServer.put_VMRCEncryptionCertificate
- VMVirtualServer.VMRCEncryptionCertificate
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

# IVMVirtualServer::VMRCEncryptionCertificate property

The **VMRCEncryptionCertificate** property contains the security certificate used by SSL/TLS encryption to protect VMRC session data.

This property is read/write.

## Syntax


```C++
HRESULT put_VMRCEncryptionCertificate(
  [in]  BSTR certificate
);

HRESULT get_VMRCEncryptionCertificate(
  [out] BSTR *certificate
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
<td><pre><code>VMVirtualServer.VMRCEncryptionCertificate( _
  ByRef certificate, _
  ByVal certificate _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The Base-64 encoded security certificate used by SSL/TLS encryption to protected session data. A zero-length string indicates that no security certificate will be used and the VMRC session cannot be protected by encryption.

This property value is read/write.

## Error codes



| Name                                                                                          | Meaning                                                                          |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                                         |
| <dl> <dt>E\_POINTER</dt> </dl>         | The parameter *certificate* referenced is **NULL**.<br/>                   |
| <dl> <dt>E\_INVALIDARG</dt> </dl>      | The parameter *certificate* contains an invalid security certificate.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>                                         |



## Remarks

When this property is set to a zero-length string, it indicates that no security certificate is in use. In this case, VMRC sessions cannot be protected.

The private key referenced by the security certificate must already exist on the computer on which Virtual Server is running.

## Examples

The following example displays the **VMRCEncryptionCertificate** property value of the [**VMVirtualServer**](ivmvirtualserver.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")

Wscript.Echo "Name: " & objVS.Name
If objVS.VMRCEncryptionCertificate = "" Then
  Wscript.Echo "VMRC encryption certificate: [none]"
Else
  Wscript.Echo "VMRC encryption certificate: " & _
                objVS.VMRCEncryptionCertificate
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

 

 





