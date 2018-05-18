---
title: IVMVirtualServer AvailableSystemCapacity property
description: The AvailableSystemCapacity property contains the percentage of currently available system capacity, based on the number of virtual machines currently running and their scheduling parameters.
ms.assetid: 'f849a270-77e7-486a-a188-ad674515f374'
keywords: ["AvailableSystemCapacity property Virtual Server", "AvailableSystemCapacity property Virtual Server , IVMVirtualServer interface", "IVMVirtualServer interface Virtual Server , AvailableSystemCapacity property", "AvailableSystemCapacity property Virtual Server , VMVirtualServer class", "VMVirtualServer class Virtual Server , AvailableSystemCapacity property"]
topic_type:
- apiref
api_name:
- IVMVirtualServer.AvailableSystemCapacity
- IVMVirtualServer.get_AvailableSystemCapacity
- VMVirtualServer.AvailableSystemCapacity
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMVirtualServer::AvailableSystemCapacity property

The **AvailableSystemCapacity** property contains the percentage of currently available system capacity, based on the number of virtual machines currently running and their scheduling parameters.

This property is read-only.

## Syntax


```C++
HRESULT get_AvailableSystemCapacity(
  [out] VARIANT *availableCapacity
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
<td><pre><code>VMVirtualServer.AvailableSystemCapacity( _
  ByRef availableCapacity _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The percentage of currently available system capacity, based on the number of virtual machines currently running and their scheduling parameters. The number is returned as a **Double** value.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                     |
|-----------------------------------------------------------------------------------------------|---------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>    |
| <dl> <dt>E\_POINTER</dt> </dl>         | *availableCapacity* is **NULL**.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>    |



## Remarks

In order to start a new virtual machine, its [**IVMAccountant::ReservedSystemCapacity**](ivmaccountant-reservedsystemcapacity.md) property cannot exceed this value.

## Examples

The following example displays the **AvailableSystemCapacity** property value of the [**VMVirtualServer**](ivmvirtualserver.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")

Wscript.Echo "Name: " & objVS.Name
Wscript.Echo "Available system capacity: " & objVS.AvailableSystemCapacity
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

 

 





