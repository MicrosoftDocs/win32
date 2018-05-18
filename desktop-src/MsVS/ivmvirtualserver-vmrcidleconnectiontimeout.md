---
title: IVMVirtualServer VMRCIdleConnectionTimeout property
description: The VMRCIdleConnectionTimeout property contains the time in seconds after which idle VMRC connections are disconnected.
ms.assetid: 'a824d13a-99fa-4af2-9da7-517e5a16f824'
keywords: ["VMRCIdleConnectionTimeout property Virtual Server", "VMRCIdleConnectionTimeout property Virtual Server , IVMVirtualServer interface", "IVMVirtualServer interface Virtual Server , VMRCIdleConnectionTimeout property", "VMRCIdleConnectionTimeout property Virtual Server , VMVirtualServer class", "VMVirtualServer class Virtual Server , VMRCIdleConnectionTimeout property"]
topic_type:
- apiref
api_name:
- IVMVirtualServer.VMRCIdleConnectionTimeout
- IVMVirtualServer.get_VMRCIdleConnectionTimeout
- IVMVirtualServer.put_VMRCIdleConnectionTimeout
- VMVirtualServer.VMRCIdleConnectionTimeout
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMVirtualServer::VMRCIdleConnectionTimeout property

The **VMRCIdleConnectionTimeout** property contains the time in seconds after which idle VMRC connections are disconnected.

This property is read/write.

## Syntax


```C++
HRESULT put_VMRCIdleConnectionTimeout(
  [in]  long idleTimeout
);

HRESULT get_VMRCIdleConnectionTimeout(
  [out] long *idleTimeout
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
<td><pre><code>VMVirtualServer.VMRCIdleConnectionTimeout( _
  ByRef idleTimeout, _
  ByVal idleTimeout _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The time in seconds after which idle VMRC connections will be disconnected.

This property value is read/write.

## Error codes



| Name                                                                                          | Meaning                                                                    |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                                   |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *idleTimeout* parameter is **NULL**.<br/>                        |
| <dl> <dt>E\_INVALIDARG</dt> </dl>      | The *idleTimeout* parameter is not in the valid range of times.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>                                   |



## Remarks

The VMRC connection idle timeout is specified in seconds, and must be within the range of 1 second to 24 hours (86400 seconds).

## Examples

The following example displays the **VMRCIdleConnectionTimeout** property value of the [**VMVirtualServer**](ivmvirtualserver.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")
Wscript.Echo "Name: " & objVS.Name

Wscript.Echo "VMRC idle connection timeout: " & _
             objVS.VMRCIdleConnectionTimeout
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

 

 





