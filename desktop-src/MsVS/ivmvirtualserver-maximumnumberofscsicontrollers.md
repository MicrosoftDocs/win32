---
title: IVMVirtualServer MaximumNumberOfSCSIControllers property
description: The MaximumNumberOfSCSIControllers property contains the maximum number of controllers allowed for SCSI.
ms.assetid: '7e32878b-3bfd-4abf-8b30-9c13d2a8aabd'
keywords: ["MaximumNumberOfSCSIControllers property Virtual Server", "MaximumNumberOfSCSIControllers property Virtual Server , IVMVirtualServer interface", "IVMVirtualServer interface Virtual Server , MaximumNumberOfSCSIControllers property", "MaximumNumberOfSCSIControllers property Virtual Server , VMVirtualServer class", "VMVirtualServer class Virtual Server , MaximumNumberOfSCSIControllers property"]
topic_type:
- apiref
api_name:
- IVMVirtualServer.MaximumNumberOfSCSIControllers
- IVMVirtualServer.get_MaximumNumberOfSCSIControllers
- VMVirtualServer.MaximumNumberOfSCSIControllers
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMVirtualServer::MaximumNumberOfSCSIControllers property

The **MaximumNumberOfSCSIControllers** property contains the maximum number of controllers allowed for SCSI.

This property is read-only.

## Syntax


```C++
HRESULT get_MaximumNumberOfSCSIControllers(
  [out] long *maxNumAdapters
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
<td><pre><code>VMVirtualServer.MaximumNumberOfSCSIControllers( _
  ByRef maxNumAdapters _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The maximum number of controllers allowed for SCSI.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                  |
|-----------------------------------------------------------------------------------------------|------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/> |
| <dl> <dt>E\_POINTER</dt> </dl>         | *maxNumAdapters* is **NULL**.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/> |



## Examples

The following example displays the **MaximumNumberOfSCSIControllers** property value of the [**VMVirtualServer**](ivmvirtualserver.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")

Wscript.Echo "Name: " & objVS.Name
Wscript.Echo "Maximum number of SCSI controllers: " & _
              objVS.MaximumNumberOfSCSIControllers
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

 

 





