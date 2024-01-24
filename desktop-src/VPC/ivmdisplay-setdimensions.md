---
title: IVMDisplay SetDimensions method (VPCCOMInterfaces.h)
description: Sets the height and width of the VM's display, in pixels.
ms.assetid: 8ad5cfc4-59b4-4327-b088-d54adf9c6fda
keywords:
- SetDimensions method Virtual PC
- SetDimensions method Virtual PC , IVMDisplay interface
- IVMDisplay interface Virtual PC , SetDimensions method
topic_type:
- apiref
api_name:
- IVMDisplay.SetDimensions
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMDisplay::SetDimensions method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Sets the height and width of the virtual machine's (VM's) display, in pixels.

## Syntax


```C++
HRESULT SetDimensions(
  [in] long displayPixelWidth,
  [in] long displayPixelHeight
);
```



## Parameters

<dl> <dt>

*displayPixelWidth* \[in\]
</dt> <dd>

The width, in pixels. The value must be between the values of 640 and 2048. If the value is not evenly divisible by 8, then it will be reduced to the next lower multiple of 8.

</dd> <dt>

*displayPixelHeight* \[in\]
</dt> <dd>

The height, in pixels. The value must be between the values of 480 and 1920.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code/value                                                                                                                                                                    | Description                                                                                                                                                                                                      |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0</dt> </dl>                                          | The operation was successful.<br/>                                                                                                                                                                         |
| <dl> <dt>**E\_INVALIDARG**</dt> <dt>0x80000003</dt> </dl>                         | The *displayPixelWidth* parameter is not evenly divisible by 8 or the *displayPixelWidth* or *displayPixelHeight* parameter is outside of the allowed minimum (640x480) or maximum 2048x1920) values.<br/> |
| <dl> <dt>**VM\_E\_TIMED\_OUT**</dt> <dt>0xA0040202</dt> </dl>                     | The resolution change did not finish in a timely manner.<br/>                                                                                                                                              |
| <dl> <dt>**VM\_E\_VM\_NOT\_RUNNING**</dt> <dt>0xA0040206</dt> </dl>               | The virtual machine must be running for this operation.<br/>                                                                                                                                               |
| <dl> <dt>**VM\_E\_VM\_UNKNOWN**</dt> <dt>0xA0040207</dt> </dl>                    | The virtual machine is not valid or is not currently running.<br/>                                                                                                                                         |
| <dl> <dt>**VM\_E\_NO\_DISPLAY**</dt> <dt>0xA0040850</dt> </dl>                    | Unable to locate a valid display for the VM.<br/>                                                                                                                                                          |
| <dl> <dt>**VM\_E\_ADDITIONS\_FEATURE\_NOT\_AVAIL**</dt> <dt>0xA0040505</dt> </dl> | The version of the integration components installed in the guest operating system does not support this operation.<br/>                                                                                    |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> <dt>0x80020009</dt> </dl>                    | An unexpected error has occurred.<br/>                                                                                                                                                                     |



 

## Remarks

The minimum size of the virtual machine's display is 640 x 480 pixels. The maximum size is 2048 x 1920. Attempts to set the display size to values outside these limits, or to any width not evenly divisible by 8, will result in an **E\_INVALIDARG** error being returned.

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

 

