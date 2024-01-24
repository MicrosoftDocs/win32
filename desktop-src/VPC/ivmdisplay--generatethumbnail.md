---
title: IVMDisplay _GenerateThumbnail method (VPCCOMInterfaces.h)
description: Retrieves an array of pixels representing a thumbnail image of the virtual machine's screen. | IVMDisplay _GenerateThumbnail method (VPCCOMInterfaces.h)
ms.assetid: c97bb0ff-55cd-491f-a706-0ba15c9a6b54
keywords:
- _GenerateThumbnail method Virtual PC
- _GenerateThumbnail method Virtual PC , IVMDisplay interface
- IVMDisplay interface Virtual PC , _GenerateThumbnail method
topic_type:
- apiref
api_name:
- IVMDisplay._GenerateThumbnail
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMDisplay::\_GenerateThumbnail method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves an array of pixels representing a thumbnail image of the virtual machine's screen.

## Syntax


```C++
HRESULT _GenerateThumbnail(
  [out] unsigned long thumbnailImage[3072]
);
```



## Parameters

<dl> <dt>

*thumbnailImage* \[out\]
</dt> <dd>

The array of pixels representing a thumbnail image of the virtual machine's screen.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code/value                                                                                                                                                 | Description                                  |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0</dt> </dl>                       | The operation was successful.<br/>     |
| <dl> <dt>**E\_POINTER**</dt> <dt>0x80004003</dt> </dl>         | The parameter is **NULL**.<br/>        |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> <dt>0x80020009</dt> </dl> | An unexpected error has occurred.<br/> |



 

## Remarks

This interface returns the thumbnail more efficiently than the [**Thumbnail**](ivmdisplay-thumbnail.md) property, but is not usable from scripting clients. The thumbnail is always 64 pixels wide by 48 pixels high. Each pixel is 32 bits, where the upper 8 bits represent the blue value of the pixel, the next 8 bits represent the green value of the pixel, and the next 8 bits represent the red value of the pixel. The first 64 elements in the array is the first row of the thumbnail, the next 64 elements is the second row, and so on. This method returns a static array of pixels, which is more efficient than returning a **SAFEARRAY** of **VARIANT** values, but is not compatible with scripting clients.

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

 

