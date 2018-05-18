---
title: IVMVirtualMachine Accountant property
description: The Accountant property contains an IVMAccountant object for this virtual machine.
ms.assetid: '03da7290-0cca-4429-9f3d-ef17d88b0a0b'
keywords: ["Accountant property Virtual Server", "Accountant property Virtual Server , IVMVirtualMachine interface", "IVMVirtualMachine interface Virtual Server , Accountant property", "Accountant property Virtual Server , VMVirtualMachine class", "VMVirtualMachine class Virtual Server , Accountant property"]
topic_type:
- apiref
api_name:
- IVMVirtualMachine.Accountant
- IVMVirtualMachine.get_Accountant
- VMVirtualMachine.Accountant
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMVirtualMachine::Accountant property

The **Accountant** property contains an [**IVMAccountant**](ivmaccountant.md) object for this virtual machine.

This property is read-only.

## Syntax


```C++
HRESULT get_Accountant(
  [out] IVMAccountant **accountant
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
<td><pre><code>VMVirtualMachine.Accountant( _
  ByRef accountant _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The [**VMAccountant**](ivmaccountant.md) object associated with this virtual machine.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                            |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>           |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *accountant* parameter is **NULL**.<br/> |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl> | The configuration is unknown.<br/>           |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>       |



## Examples

The following example displays property values of the Accountant object associated with a specific [**IVMVirtualMachine**](ivmvirtualmachine.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")

Set objVM = objVS.FindVirtualMachine("Windows Server 2003")

Set objAcnt = objVM.Accountant

Wscript.Echo "VM Name: " & objVM.Name
Wscript.Echo "  Allowable maximum system capacity: " & _
              objAcnt.AllowableMaximumSystemCapacity
Wscript.Echo "  Allowable reserved system capacity: " & _
              objAcnt.AllowableReservedSystemCapacity
Wscript.Echo "  CPU utilization: " & objAcnt.CPUUtilization
Wscript.Echo "  Disk bytes read: " & objAcnt.DiskBytesRead
Wscript.Echo "  Disk bytes written: " & objAcnt.DiskBytesWritten
Wscript.Echo "  Maximum system capacity: " & objAcnt.MaximumSystemCapacity
Wscript.Echo "  Network bytes received: " & objAcnt.NetworkBytesReceived
Wscript.Echo "  Network bytes sent: " & objAcnt.NetworkBytesSent
Wscript.Echo "  Relative weight: " & objAcnt.RelativeWeight
Wscript.Echo "  Reserved system capacity: " & objAcnt.ReservedSystemCapacity
Wscript.Echo "  Uptime: " & objAcnt.Uptime
```



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualMachine**](ivmvirtualmachine.md)
</dt> </dl>

 

 





