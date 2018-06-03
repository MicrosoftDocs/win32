---
title: TAPE\_VERIFY\_INQUIRY\_ROUTINE routine
description: TAPE\_VERIFY\_INQUIRY\_ROUTINE determines whether the tape miniclass driver recognizes and supports a given device. This routine is required.
ms.assetid: ed216b13-546a-4d0c-82db-79c175912556
keywords:
- ( TAPE_VERIFY_INQUIRY_ROUTINE) routine Storage Devices
- TAPE_VERIFY_INQUIRY_ROUTINE
topic_type:
- apiref
api_name:
- ( TAPE_VERIFY_INQUIRY_ROUTINE)
api_location:
- minitape.h
api_type:
- UserDefined
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# TAPE\_VERIFY\_INQUIRY\_ROUTINE routine

*TAPE\_VERIFY\_INQUIRY\_ROUTINE* determines whether the tape miniclass driver recognizes and supports a given device. This routine is required.

## Syntax


```C++
TAPE_VERIFY_INQUIRY_ROUTINE (*TAPE_VERIFY_INQUIRY_ROUTINE);

BOOLEAN (*TAPE_VERIFY_INQUIRY_ROUTINE)(
  _In_ PINQUIRYDATA            InquiryData,
  _In_ PMODE_CAPABILITIES_PAGE ModeCapabilitiesPage
)
{ ... }
```



## Parameters

<dl> <dt>

*InquiryData* \[in\]
</dt> <dd>

Pointer to SCSI inquiry data for the device.

</dd> <dt>

*ModeCapabilitiesPage* \[in\]
</dt> <dd>

Pointer to a MODE\_CAPABILITIES\_PAGE structure that contains low-level information about the device. The format of this structure is defined by the QIC 157 standard and is subject to change. The pointer is **NULL** if the tape device does not support a mode capabilities page.

</dd> </dl>

## Return value

*TAPE\_VERIFY\_INQUIRY\_ROUTINE* returns **TRUE** if the miniclass driver supports the device.

## Remarks

*TAPE\_VERIFY\_INQUIRY\_ROUTINE* examines the *InquiryData*, particularly the **VendorId** and **ProductId** members, to determine whether the tape miniclass driver supports the tape device. *TAPE\_VERIFY\_INQUIRY\_ROUTINE* uses [**TapeClassCompareMemory**](tapeclasscomparememory.md) to compare ID strings against values the tape miniclass driver supports.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Minitape.h (include Minitape.h)</dt> </dl> |



## See also

<dl> <dt>

[**TapeClassCompareMemory**](tapeclasscomparememory.md)
</dt> <dt>

[**TAPE\_STATUS**](tape-status.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20TAPE_VERIFY_INQUIRY_ROUTINE%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






