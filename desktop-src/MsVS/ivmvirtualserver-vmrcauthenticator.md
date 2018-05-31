---
title: IVMVirtualServer VMRCAuthenticator property
description: The VMRCAuthenticator property contains the authentication method to use for new VMRC connections.
ms.assetid: b7fdfd32-6014-42a6-a70d-020dc2a9346d
keywords:
- VMRCAuthenticator property Virtual Server
- VMRCAuthenticator property Virtual Server , IVMVirtualServer interface
- IVMVirtualServer interface Virtual Server , VMRCAuthenticator property
- VMRCAuthenticator property Virtual Server , VMVirtualServer class
- VMVirtualServer class Virtual Server , VMRCAuthenticator property
topic_type:
- apiref
api_name:
- IVMVirtualServer.VMRCAuthenticator
- IVMVirtualServer.get_VMRCAuthenticator
- IVMVirtualServer.put_VMRCAuthenticator
- VMVirtualServer.VMRCAuthenticator
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

# IVMVirtualServer::VMRCAuthenticator property

The **VMRCAuthenticator** property contains the authentication method to use for new VMRC connections.

This property is read/write.

## Syntax


```C++
HRESULT put_VMRCAuthenticator(
  [in]  VMRCAuthenticationType *authenticator
);

HRESULT get_VMRCAuthenticator(
  [out] IVMRCAuthenticator     **authenticator
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
<td><pre><code>VMVirtualServer.VMRCAuthenticator( _
  ByRef authenticator, _
  ByVal authenticator _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The [**VMRCAuthenticator**](ivmrcauthenticator.md) object representing the authentication method to use for new VMRC connections.

This property value is read/write.

## Error codes



| Name                                                                                          | Meaning                                                                                              |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                                                             |
| <dl> <dt>E\_POINTER</dt> </dl>         | The parameter *authenticator* is **NULL**.<br/>                                                |
| <dl> <dt>E\_INVALIDARG</dt> </dl>      | The *authenticator* instance represented an invalid or unsupported authentication method.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>                                                         |



## Examples

The following example displays properties of the **VMRCAuthenticator** property value of the [**VMVirtualServer**](ivmvirtualserver.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")

Wscript.Echo "Name: " & objVS.Name

Set objVMAColl = objVS.VMRCAuthenticators
Dim objAuth
If isNull(objVMAColl) Then
  Wscript.Echo "VMRC authenticators: [none]"
Else
  Wscript.Echo "VMRC authenticators: "
  For Each objAuth in objVMAColl
    Wscript.Echo "    Name: " & objAuth.Name & " (" & _
                                objAuth.Description & ")"
  Next
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

 

 





