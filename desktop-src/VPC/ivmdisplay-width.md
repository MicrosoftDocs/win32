---
title: IVMDisplay Width property (VPCCOMInterfaces.h)
description: Width of the VM's display, in pixels.
ms.assetid: a0062d75-dbb3-41ff-8112-87c1a31b088e
keywords:
- Width property Virtual PC
- Width property Virtual PC , IVMDisplay interface
- IVMDisplay interface Virtual PC , Width property
topic_type:
- apiref
api_name:
- IVMDisplay.Width
- IVMDisplay.get_Width
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMDisplay::Width property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves the width of the virtual machine's (VM's) display, in pixels.

This property is read-only.

## Syntax


```C++
HRESULT get_Width(
  [out, retval] long *displayPixelWidth
);
```



## Property value

The width, in pixels.

## Error codes



| Name/value                                                                                                                                                         | Meaning                                                                  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                            | The operation was successful.<br/>                                 |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>              | The parameter is **NULL**.<br/>                                    |
| <dl> <dt>VM\_E\_VM\_NOT\_RUNNING</dt> <dt>0xA0040206</dt> </dl> | The virtual machine must be running for this operation.<br/>       |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> <dt>0xA0040207</dt> </dl>      | The virtual machine is not valid or is not currently running.<br/> |
| <dl> <dt>VM\_E\_NO\_DISPLAY</dt> <dt>0xA0040850</dt> </dl>      | Unable to locate a valid display for the virtual machine.<br/>     |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl>      | An unexpected error has occurred.<br/>                             |



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMDisplay is defined as 960895e9-f743-4498-96aa-261f867e7fc5<br/>                 |



## See also

<dl> <dt>

[**IVMDisplay**](ivmdisplay.md)
</dt> </dl>

 

