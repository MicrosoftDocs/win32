---
title: IVMVirtualServer SupportDrivers property
description: The SupportDrivers property contains a collection of support drivers.
ms.assetid: 'b72c400f-4c2a-4af2-b219-e074ee6ffd6f'
keywords: ["SupportDrivers property Virtual Server", "SupportDrivers property Virtual Server , IVMVirtualServer interface", "IVMVirtualServer interface Virtual Server , SupportDrivers property", "SupportDrivers property Virtual Server , VMVirtualServer class", "VMVirtualServer class Virtual Server , SupportDrivers property"]
topic_type:
- apiref
api_name:
- IVMVirtualServer.SupportDrivers
- IVMVirtualServer.get_SupportDrivers
- VMVirtualServer.SupportDrivers
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMVirtualServer::SupportDrivers property

The **SupportDrivers** property contains a collection of support drivers.

This property is read-only.

## Syntax


```C++
HRESULT get_SupportDrivers(
  [out] IVMSupportDriverCollection **supportDriverCollection
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
<td><pre><code>VMVirtualServer.SupportDrivers( _
  ByRef supportDriverCollection _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The [**IVMSupportDriverCollection**](ivmsupportdrivercollection.md) object associated with Virtual Server.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                                         |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                        |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *supportDriverCollection* parameter is **NULL**.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>                        |



## Remarks

Support drivers are Windows drivers installed in the host operating system that provide support for Virtual Server.

## Examples

The following example displays the **SupportDrivers** property value of the [**VMVirtualServer**](ivmvirtualserver.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")
Wscript.Echo "Name: " & objVS.Name

Set objSDColl = objVS.SupportDrivers
If objSDColl.Count > 0 Then
  Wscript.Echo "Support drivers: "
  For Each objSD in objSDColl
    Wscript.Echo "    Type: " & objSD.Type & " (" & objSD.Description & ")"
  Next
End If
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

 

 





