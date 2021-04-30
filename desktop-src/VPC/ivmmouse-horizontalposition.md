---
title: IVMMouse HorizontalPosition property (VPCCOMInterfaces.h)
description: Absolute x-coordinate of the mouse.
ms.assetid: 8cf2a247-b6db-49f6-8e19-c862004f26cd
keywords:
- HorizontalPosition property Virtual PC
- HorizontalPosition property Virtual PC , IVMMouse interface
- IVMMouse interface Virtual PC , HorizontalPosition property
topic_type:
- apiref
api_name:
- IVMMouse.HorizontalPosition
- IVMMouse.get_HorizontalPosition
- IVMMouse.put_HorizontalPosition
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMMouse::HorizontalPosition property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves the absolute x-coordinate of the mouse.

This property is read/write.

## Syntax


```C++
HRESULT put_HorizontalPosition(
  [in]          long position
);

HRESULT get_HorizontalPosition(
  [out, retval] long *position
);
```



## Property value

The x-coordinate indicating the new position of the mouse. When using absolute coordinates, this value specifies the new x-coordinate of the mouse. When using relative coordinates, this value specifies the number of pixels the mouse should be moved in the x direction.

## Error codes



| Name/value                                                                                                                                                                       | Meaning                                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                                          | The operation was successful.<br/>                                                                                                                |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>                            | The parameter is **NULL**.<br/>                                                                                                                   |
| <dl> <dt>VM\_E\_VM\_NOT\_RUNNING</dt> <dt>0xA0040206</dt> </dl>               | The virtual machine to which this mouse device is attached is not currently running.<br/>                                                         |
| <dl> <dt>VM\_E\_ADDITIONS\_FEATURE\_NOT\_AVAIL</dt> <dt>0xA0040505</dt> </dl> | Integration components must be installed to retrieve the mouse position, or to set the mouse position when using absolute coordinates.<br/>       |
| <dl> <dt>VM\_E\_USING\_RELATIVE\_COORDINATES</dt> <dt>0xA0040802</dt> </dl>   | The mouse device is currently set to use relative mouse coordinates.<br/>                                                                         |
| <dl> <dt>VM\_E\_MOUSE\_NOT\_ACTIVE</dt> <dt>0xA0040800</dt> </dl>             | The absolute coordinates cannot be retrieved if the mouse device is not powered up, or if it is not currently active in the virtual machine.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl>                    | An unexpected error has occurred.<br/>                                                                                                            |



## Remarks

This property cannot be retrieved when using relative coordinates.

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

 

