---
title: IVMDisplay SetDimensions method
description: The SetDimensions method sets the height and width, in pixels, of the virtual machine's display.
ms.assetid: 06c01c4e-47b3-4119-81de-325e7628c16e
keywords:
- SetDimensions method Virtual Server
- SetDimensions method Virtual Server , IVMDisplay interface
- IVMDisplay interface Virtual Server , SetDimensions method
- SetDimensions method Virtual Server , VMDisplay interface
- VMDisplay interface Virtual Server , SetDimensions method
topic_type:
- apiref
api_name:
- IVMDisplay.SetDimensions
- VMDisplay.SetDimensions
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IVMDisplay::SetDimensions method

The **SetDimensions** method sets the height and width, in pixels, of the virtual machine's display.

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

The width, in pixels, of the virtual machine's display. The argument must be between the values of 640 and 1600 and be evenly divisible by 8.

</dd> <dt>

*displayPixelHeight* \[in\]
</dt> <dd>

The height, in pixels, of the virtual machine's display. The argument must be between the values of 480 and 1200 and be evenly divisible by 8.

</dd> </dl>

## Return value

This method can return one of these values.

This method supports standard return values, as well as the following. For information on Virtual Server specific return values not listed below, see [**HRESULT Codes Specific to the Virtual Server**](hresult-codes-specific-to-the-virtual-server.md).



| Return code                                                                                                          | Description                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt> **S\_OK**</dt> </dl>                                | The operation was successful.<br/>                                                                                            |
| <dl> <dt> **E\_INVALIDARG**</dt> </dl>                        | The parameter is not evenly divisible by 8 or is outside of the allowed minimum (640x480) or maximum (1600x1200) values.<br/> |
| <dl> <dt>**VM\_E\_VM\_UNKNOWN**</dt> </dl>                    | The virtual machine is not valid or is not currently running.<br/>                                                            |
| <dl> <dt>**VM\_E\_NO\_DISPLAY**</dt> </dl>                    | Unable to locate a valid display for the virtual machine.<br/>                                                                |
| <dl> <dt>**VM\_E\_ADDITIONS\_FEATURE\_NOT\_AVAIL**</dt> </dl> | The version of the additions installed in the guest operating system does not support this operation.<br/>                    |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> </dl>                    | An unexpected error occurred.<br/>                                                                                            |



 

## Remarks

The minimum size of the virtual machine's display is 640 x 480 pixels. The maximum size is 1600 x 1200. Attempts to set the display size to values outside these limits, or to any value not evenly divisible by 8, will result in an **E\_INVALIDARG** error being returned.

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMDisplay**](ivmdisplay.md)
</dt> </dl>

 

 





