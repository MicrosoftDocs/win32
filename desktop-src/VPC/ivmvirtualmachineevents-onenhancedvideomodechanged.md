---
title: IVMVirtualMachineEvents OnEnhancedVideoModeChanged method (VPCCOMInterfaces.h)
description: Receives notification that a virtual machine's support for enhanced video mode has changed.
ms.assetid: be22a859-4687-4647-9f53-f79ae8ad52a5
keywords:
- OnEnhancedVideoModeChanged method Virtual PC
- OnEnhancedVideoModeChanged method Virtual PC , IVMVirtualMachineEvents interface
- IVMVirtualMachineEvents interface Virtual PC , OnEnhancedVideoModeChanged method
topic_type:
- apiref
api_name:
- IVMVirtualMachineEvents.OnEnhancedVideoModeChanged
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualMachineEvents::OnEnhancedVideoModeChanged method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Receives notification that a virtual machine's support for enhanced video mode has changed.

## Syntax


```C++
HRESULT OnEnhancedVideoModeChanged(
  [in] VARIANT_BOOL enhancedVideoMode
);
```



## Parameters

<dl> <dt>

*enhancedVideoMode* \[in\]
</dt> <dd>

Indicates whether enhanced video mode is available.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

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

 

