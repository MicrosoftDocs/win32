---
title: IVMVirtualMachineEvents OnRequestShutdown method (VPCCOMInterfaces.h)
description: Receives notification that a shutdown request has been made.
ms.assetid: e04131fd-5ca7-4392-9725-ba62b905324a
keywords:
- OnRequestShutdown method Virtual PC
- OnRequestShutdown method Virtual PC , IVMVirtualMachineEvents interface
- IVMVirtualMachineEvents interface Virtual PC , OnRequestShutdown method
topic_type:
- apiref
api_name:
- IVMVirtualMachineEvents.OnRequestShutdown
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualMachineEvents::OnRequestShutdown method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Receives notification that a shutdown request has been made.

## Syntax


```C++
HRESULT OnRequestShutdown();
```



## Parameters

This method has no parameters.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

This method is called whenever the virtual machine session is about to shut down. The client program must implement this interface method to receive notification of the **vmVirtualMachineEvent\_RequestShutdown** event originating from [**IVMVirtualMachine**](ivmvirtualmachine.md).

This event notification is sent only when the virtual machines session is about to shut down. Operating system shutdown routines, such as [**IVMGuestOS::Shutdown**](ivmguestos-shutdown.md), do not fire this event directly unless they also attempt to perform a software power off of the virtual hardware.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | DIID\_IVMVirtualMachineEvents is defined as 9d84f560-bb67-4961-bd12-a4da780c67e4<br/>   |



## See also

<dl> <dt>

[**IVMVirtualMachineEvents**](ivmvirtualmachineevents.md)
</dt> </dl>

 

