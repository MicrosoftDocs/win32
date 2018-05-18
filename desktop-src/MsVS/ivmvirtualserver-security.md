---
title: IVMVirtualServer Security property
description: The IVMSecurity object associated with Virtual Server.
ms.assetid: '83bfe2fb-8fdc-4f10-8458-4b1527d6c544'
keywords: ["Security property Virtual Server", "Security property Virtual Server , IVMVirtualServer interface", "IVMVirtualServer interface Virtual Server , Security property", "Security property Virtual Server , VMVirtualServer class", "VMVirtualServer class Virtual Server , Security property"]
topic_type:
- apiref
api_name:
- IVMVirtualServer.Security
- IVMVirtualServer.get_Security
- IVMVirtualServer.put_Security
- VMVirtualServer.Security
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMVirtualServer::Security property

The [**IVMSecurity**](ivmsecurity.md) object associated with Virtual Server.

This property is read/write.

## Syntax


```C++
HRESULT put_Security(
  [in]  IVMSecurity *security
);

HRESULT get_Security(
  [out] IVMSecurity **security
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
<td><pre><code>VMVirtualServer.Security( _
  ByRef security, _
  ByVal security _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Contains a [**VMSecurity**](ivmsecurity.md) object which represents the security attributes of Virtual Server.

This property value is read/write.

## Error codes



| Name                                                                                          | Meaning                                                                                                                  |
|-----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                                                                                 |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *security* parameter is **NULL**.<br/>                                                                         |
| <dl> <dt>E\_OUTOFMEMORY</dt> </dl>     | Could not allocate memory for the security descriptor.<br/>                                                        |
| <dl> <dt>E\_ACCESSDENIED</dt> </dl>    | The client has insufficient access rights to modify the security attributes.<br/>                                  |
| <dl> <dt>E\_FAIL</dt> </dl>            | The security attributes could not be applied. This may occur if the application data folders cannot be found.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>                                                                             |



## Examples

The following example displays property values of the [**VMSecurity**](ivmsecurity.md) object associated with the [**VMVirtualServer**](ivmvirtualserver.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")
Wscript.Echo "Name: " & objVS.Name

Set objSec = objVS.Security
Wscript.Echo "Security principle: "
Wscript.Echo "    Owner Name: " & objSec.OwnerName
Wscript.Echo "    Owner SID: " & objSec.OwnerSID
Wscript.Echo "    Group Name: " & objSec.GroupName
Wscript.Echo "    Group SID: " & objSec.GroupSID
```



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualServer**](ivmvirtualserver.md)
</dt> </dl>

 

 





