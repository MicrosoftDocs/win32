---
title: IOCTL\_TAPE\_GET\_STATUS control code
description: Returns the current status of the drive in the Status field of the I/O status block.
ms.assetid: d5e491b8-d40c-4f2c-9117-5c3cb71913f7
keywords:
- IOCTL_TAPE_GET_STATUS control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_TAPE_GET_STATUS
api_location:
- Ntddtape.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IOCTL\_TAPE\_GET\_STATUS control code

Returns the current status of the drive in the **Status** field of the I/O status block.

## Input Buffer

None.

## Input Buffer Length

None.

## Output Buffer

None.

## Output Buffer Length

None.

## Status block

The **Information** field is set to zero. The **Status** field is set to one of the following NT status values:

-   STATUS\_SUCCESS

-   STATUS\_INSUFFICIENT\_RESOURCES

-   STATUS\_NOT\_IMPLEMENTED

-   STATUS\_INVALID\_DEVICE\_REQUEST

-   STATUS\_INVALID\_PARAMETER

-   STATUS\_VERIFY\_REQUIRED

-   STATUS\_BUS\_RESET

-   STATUS\_SETMARK\_DETECTED

-   STATUS\_FILEMARK\_DETECTED

-   STATUS\_BEGINNING\_OF\_MEDIA

-   STATUS\_END\_OF\_MEDIA

-   STATUS\_BUFFER\_OVERFLOW

-   STATUS\_NO\_DATA\_DETECTED

-   STATUS\_EOM\_OVERFLOW

-   STATUS\_NO\_MEDIA

-   STATUS\_IO\_DEVICE\_ERROR

-   STATUS\_UNRECOGNIZED\_MEDIA

-   STATUS\_DEVICE\_NOT\_READY

-   STATUS\_MEDIA\_WRITE\_PROTECTED

-   STATUS\_DEVICE\_DATA\_ERROR

-   STATUS\_NO\_SUCH\_DEVICE

-   STATUS\_INVALID\_BLOCK\_LENGTH

-   STATUS\_IO\_TIMEOUT

-   STATUS\_DEVICE\_NOT\_CONNECTED

-   STATUS\_DATA\_OVERRUN

-   STATUS\_DEVICE\_BUSY

-   STATUS\_DEVICE\_REQUIRES\_CLEANING

-   STATUS\_CLEANER\_CARTRIDGE\_INSTALLED

Each of these NT status values correspond to a value in the [**TAPE\_STATUS**](tape-status.md) enumerator. For more information about the significance of these values and a mapping between the NT status values and the TAPE\_STATUS values, see [Processing Tape Device Control Requests](https://msdn.microsoft.com/library/windows/hardware/ff563934).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddtape.h (include Ntddtape.h)</dt> </dl> |



## See also

<dl> <dt>

[**TAPE\_STATUS**](tape-status.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_TAPE_GET_STATUS%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






