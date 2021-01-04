---
title: IVMMouse ScrollWheelPosition property (VPCCOMInterfaces.h)
description: Adjusts the z-coordinate of the mouse (relative only).
ms.assetid: 52269d0c-a7a8-4dc2-bb27-c891d1e9c293
keywords:
- ScrollWheelPosition property Virtual PC
- ScrollWheelPosition property Virtual PC , IVMMouse interface
- IVMMouse interface Virtual PC , ScrollWheelPosition property
topic_type:
- apiref
api_name:
- IVMMouse.ScrollWheelPosition
- IVMMouse.put_ScrollWheelPosition
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMMouse::ScrollWheelPosition property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Adjusts the z-coordinate of the mouse (relative only).

This property is write-only.

## Syntax


```C++
HRESULT put_ScrollWheelPosition(
  [in] long position
);
```



## Property value

The z-coordinate indicating the number of pixels the mouse is to be moved along the z-axis.

## Error codes



| Name/value                                                                                                                                                                     | Meaning                                                                                                 |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                                        | The operation was successful.<br/>                                                                |
| <dl> <dt>VM\_E\_VM\_NOT\_RUNNING</dt> <dt>0xA0040206</dt> </dl>             | The virtual machine to which this mouse device is attached is not currently running.<br/>         |
| <dl> <dt>VM\_E\_MOUSE\_NOT\_ACTIVE</dt> <dt>0xA0040800</dt> </dl>           | The mouse device has not been powered up, or is not currently active in the virtual machine.<br/> |
| <dl> <dt>VM\_E\_USING\_ABSOLUTE\_COORDINATES</dt> <dt>0xA0040801</dt> </dl> | The scroll wheel position cannot be set when the mouse device is using absolute coordinates.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl>                  | An unexpected error has occurred.<br/>                                                            |



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMmouse is defined as ac903f6d-6346-4f29-8875-5d511a13895e<br/>                   |



## See also

<dl> <dt>

[**IVMMouse**](ivmmouse.md)
</dt> </dl>

 

