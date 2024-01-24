---
title: IVMVirtualMachineEvents OnConfigurationChanged method (VPCCOMInterfaces.h)
description: Receives notification that a value in the configuration for this virtual machine has changed.
ms.assetid: 1955f23e-b318-41aa-b82e-81283be81608
keywords:
- OnConfigurationChanged method Virtual PC
- OnConfigurationChanged method Virtual PC , IVMVirtualMachineEvents interface
- IVMVirtualMachineEvents interface Virtual PC , OnConfigurationChanged method
topic_type:
- apiref
api_name:
- IVMVirtualMachineEvents.OnConfigurationChanged
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualMachineEvents::OnConfigurationChanged method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Receives notification that a value in the configuration for this virtual machine has changed.

## Syntax


```C++
HRESULT OnConfigurationChanged(
  [in] BSTR    configKey,
  [in] VARIANT configData
);
```



## Parameters

<dl> <dt>

*configKey* \[in\]
</dt> <dd>

The value inside the configuration that has changed.

</dd> <dt>

*configData* \[in\]
</dt> <dd>

The new value for the configuration.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

This method is called when the configuration changes for this virtual machine. The client program must implement this interface method to receive notification of the vmVirtualMachineEvent\_ConfigurationChanged event originating from [**IVMVirtualMachine**](ivmvirtualmachine.md).

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

 

