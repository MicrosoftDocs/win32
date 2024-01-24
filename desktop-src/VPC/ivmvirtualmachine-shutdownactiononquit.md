---
title: IVMVirtualMachine ShutdownActionOnQuit property (VPCCOMInterfaces.h)
description: Action to be performed on this virtual machine if it is running when Windows Virtual PC is quit.
ms.assetid: 3f6b256e-c48a-4a7c-acee-83d996e13ec7
keywords:
- ShutdownActionOnQuit property Virtual PC
- ShutdownActionOnQuit property Virtual PC , IVMVirtualMachine interface
- IVMVirtualMachine interface Virtual PC , ShutdownActionOnQuit property
topic_type:
- apiref
api_name:
- IVMVirtualMachine.ShutdownActionOnQuit
- IVMVirtualMachine.get_ShutdownActionOnQuit
- IVMVirtualMachine.put_ShutdownActionOnQuit
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualMachine::ShutdownActionOnQuit property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves and sets the action to be performed on this virtual machine (VM) if it is running when Windows Virtual PC is quit.

This property is read/write.

## Syntax


```C++
HRESULT put_ShutdownActionOnQuit(
  [in]          VMShutdownAction shutdownAction
);

HRESULT get_ShutdownActionOnQuit(
  [out, retval] VMShutdownAction *shutdownAction
);
```



## Property value

Specifies how to shut down this VM if it is running when Windows Virtual PC is quit. For a list of values, see [**VMShutdownAction**](vmshutdownaction.md).

## Error codes



| Name/value                                                                                                                                                    | Meaning                                                                        |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                       | The operation was successful.<br/>                                       |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>         | The parameter is **NULL** or not a valid value.<br/>                     |
| <dl> <dt>E\_ACCESSDENIED</dt> <dt>0x80070005</dt> </dl>    | The current user has insufficient access to the configuration file.<br/> |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> <dt>0xA0040207</dt> </dl> | The configuration is unknown.<br/>                                       |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl> | An unexpected error has occurred.<br/>                                   |



## Remarks

By default, running VMs are saved when Windows Virtual PC is quit. The shutdown action **vmShutdownAction\_Save** (0) will save the VM's state. The **vmShutdownAction\_TurnOff** (1) action will turn off the VM. The **vmShutdownAction\_Shutdown** (2) action will shut down the guest operating system if the integration components are available and will save the VM otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMVirtualMachine is defined as f7092aa1-33ed-4f78-a59f-c00adfc2edd7<br/>          |



## See also

<dl> <dt>

[**IVMVirtualMachine**](ivmvirtualmachine.md)
</dt> <dt>

[**VMShutdownAction**](vmshutdownaction.md)
</dt> </dl>

 

