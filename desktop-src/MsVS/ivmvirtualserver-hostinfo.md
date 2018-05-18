---
title: IVMVirtualServer HostInfo property
description: The HostInfo property retrieves information about the physical PC.
ms.assetid: 'f3e15110-7b01-4dd5-8105-33ac991adc9a'
keywords: ["HostInfo property Virtual Server", "HostInfo property Virtual Server , IVMVirtualServer interface", "IVMVirtualServer interface Virtual Server , HostInfo property", "HostInfo property Virtual Server , VMVirtualServer class", "VMVirtualServer class Virtual Server , HostInfo property"]
topic_type:
- apiref
api_name:
- IVMVirtualServer.HostInfo
- IVMVirtualServer.get_HostInfo
- VMVirtualServer.HostInfo
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMVirtualServer::HostInfo property

The **HostInfo** property retrieves information about the physical PC.

This property is read-only.

## Syntax


```C++
HRESULT get_HostInfo(
  [out] IVMHostInfo **hostMachine
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
<td><pre><code>VMVirtualServer.HostInfo( _
  ByRef hostMachine _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The [**VMHostInfo**](ivmhostinfo.md) object which has information about the host machine.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                             |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>            |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *hostMachine* parameter is **NULL**.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>            |



## Examples

The following example displays a few of the [**VMHostInfo**](ivmhostinfo.md) object's property values of the [**VMVirtualServer**](ivmvirtualserver.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")

Wscript.Echo "Name: " & objVS.Name
Set objHI = objVS.HostInfo
Wscript.Echo "Host info:"
Wscript.Echo "    Host operating system: " & objHI.OperatingSystem
Wscript.Echo "    Host operating system version: " & _
             objHI.OSMajorVersion & "." & objHI.OSMinorVersion
Wscript.Echo "    Number of processors on host: " & _
             objHI.PhysicalProcessorCount
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

 

 





