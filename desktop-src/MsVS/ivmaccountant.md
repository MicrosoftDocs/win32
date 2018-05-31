---
title: IVMAccountant interface
description: The IVMAccountant interface provides access to accounting-related information for a virtual machine.
ms.assetid: bccb1750-090e-4aef-968e-5d07807ade7e
keywords:
- IVMAccountant interface Virtual Server
- IVMAccountant interface Virtual Server , described
topic_type:
- apiref
api_name:
- IVMAccountant
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMAccountant interface

The **IVMAccountant** interface provides access to accounting-related information for a virtual machine.

## When to use

The **IVMAccountant** for a virtual machine can be retrieved using the [**IVMVirtualMachine::Accountant**](ivmvirtualmachine-accountant.md) property.

## Members

The **IVMAccountant** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IVMAccountant** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IVMAccountant** interface has these methods.



| Method                                                                   | Description                                                      |
|:-------------------------------------------------------------------------|:-----------------------------------------------------------------|
| [**SetSchedulingParameters**](ivmaccountant-setschedulingparameters.md) | Sets the scheduling parameters for a virtual machine.<br/> |



 

### Properties

The **IVMAccountant** interface has these properties.



| Property                                                                                            | Access type          | Description                                                                                                             |
|:----------------------------------------------------------------------------------------------------|:---------------------|:------------------------------------------------------------------------------------------------------------------------|
| [**AllowableMaximumSystemCapacity**](ivmaccountant-allowablemaximumsystemcapacity.md)<br/>   | Read-only<br/> | The currently allowable maximum percentage of system capacity that can be assigned to this virtual machine.<br/>  |
| [**AllowableReservedSystemCapacity**](ivmaccountant-allowablereservedsystemcapacity.md)<br/> | Read-only<br/> | The currently allowable minimum percentage of system capacity that can be reserved for this virtual machine.<br/> |
| [**CPUUtilization**](ivmaccountant-cpuutilization.md)<br/>                                   | Read-only<br/> | The current CPU use of this virtual machine.<br/>                                                                 |
| [**CPUUtilizationHistory**](ivmaccountant-cpuutilizationhistory.md)<br/>                     | Read-only<br/> | An array of percentage values for the recent CPU use of this virtual machine.<br/>                                |
| [**DiskBytesRead**](ivmaccountant-diskbytesread.md)<br/>                                     | Read-only<br/> | The total number of bytes read by all IDE and SCSI controllers for this virtual machine.<br/>                     |
| [**DiskBytesWritten**](ivmaccountant-diskbyteswritten.md)<br/>                               | Read-only<br/> | The total number of bytes written by all IDE and SCSI controllers for this virtual machine.<br/>                  |
| [**MaximumSystemCapacity**](ivmaccountant-maximumsystemcapacity.md)<br/>                     | Read-only<br/> | The maximum percentage of system capacity that can be used by this virtual machine.<br/>                          |
| [**NetworkBytesReceived**](ivmaccountant-networkbytesreceived.md)<br/>                       | Read-only<br/> | The total number of bytes received by all virtual network interface cards for this virtual machine.<br/>          |
| [**NetworkBytesSent**](ivmaccountant-networkbytessent.md)<br/>                               | Read-only<br/> | The total number of bytes sent by all virtual network interface cards for this virtual machine.<br/>              |
| [**RelativeWeight**](ivmaccountant-relativeweight.md)<br/>                                   | Read-only<br/> | The relative weight assigned to this virtual machine.<br/>                                                        |
| [**ReservedSystemCapacity**](ivmaccountant-reservedsystemcapacity.md)<br/>                   | Read-only<br/> | The minimum percentage of system capacity assigned to this virtual machine.<br/>                                  |
| [**UpTime**](ivmaccountant-uptime.md)<br/>                                                   | Read-only<br/> | The number of seconds that the virtual machine has been running.<br/>                                             |



 

## Examples

The following example prints the accountant information for each virtual machine.


```VB
Set objVS = CreateObject("VirtualServer.Application")
set colVMs = objVS.VirtualMachines

For Each objVM in colVMS
    Set colAccountants = objVM.Accountant
        Wscript.Echo "Virtual machine: " & objVM.Name
        Wscript.Echo "Allowable maximum system capacity: " & colAccountants.AllowableMaximumSystemCapacity
        Wscript.Echo "Allowable reserved system capacity: " & colAccountants.AllowableReservedSystemCapacity
        Wscript.Echo "CPU utilization: " & colAccountants.CPUUtilization

        i = 1
        Wscript.Echo "CPU utilization history:"
        For Each intCPUUtilization in colAccountants.CPUUtilizationHistory
            Wscript.Echo vbTab & i & " -- " & intCPUUtilization
            i = i + 1
        Next

        Wscript.Echo "Disk bytes read: " & colAccountants.DiskBytesRead
        Wscript.Echo "Disk bytes written: " & colAccountants.DiskBytesWritten
        Wscript.Echo "Maximum system capacity: " & colAccountants.MaximumSystemCapacity
        Wscript.Echo "Network bytes received: " & colAccountants.NetworkBytesReceived
        Wscript.Echo "Network bytes sent: " & colAccountants.NetworkBytesSent
        Wscript.Echo "Relative weight: " & colAccountants.RelativeWeight
        Wscript.Echo "Reserved system capacity: " & colAccountants.ReservedSystemCapacity
        Wscript.Echo "Uptime: " & colAccountants.Uptime
        Wscript.Echo
Next
```



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5)
</dt> </dl>

 

 





