---
title: IVMVirtualServer VMRCAuthenticators property
description: The VMRCAuthenticators property contains the VMRC authentication methods supported by Virtual Server.
ms.assetid: 1f857193-50a1-4d1f-8369-65f3af5b5437
keywords:
- VMRCAuthenticators property Virtual Server
- VMRCAuthenticators property Virtual Server , IVMVirtualServer interface
- IVMVirtualServer interface Virtual Server , VMRCAuthenticators property
- VMRCAuthenticators property Virtual Server , VMVirtualServer object
- VMVirtualServer object Virtual Server , VMRCAuthenticators property
topic_type:
- apiref
api_name:
- IVMVirtualServer.VMRCAuthenticators
- IVMVirtualServer.get_VMRCAuthenticators
- VMVirtualServer.VMRCAuthenticators
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

# IVMVirtualServer::VMRCAuthenticators property

The **VMRCAuthenticators** property contains the VMRC authentication methods supported by Virtual Server.

This property is read-only.

## Syntax


```C++
HRESULT get_VMRCAuthenticators(
  [out] IVMRCAuthenticatorCollection **authenticators
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
<td><pre><code>VMVirtualServer.VMRCAuthenticators( _
  ByRef authenticators _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The [**IVMRCAuthenticatorCollection**](ivmrcauthenticatorcollection.md) object representing the VMRC authentication methods supported by Virtual Server.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                                |
|-----------------------------------------------------------------------------------------------|--------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>               |
| <dl> <dt>E\_POINTER</dt> </dl>         | The parameter *authenticators* is **NULL**.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>           |



## Examples

The following example displays properties of the **VMRCAuthenticators** property value of the [**VMVirtualServer**](ivmvirtualserver.md) object.


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

 

 





