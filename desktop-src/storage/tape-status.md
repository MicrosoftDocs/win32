---
title: TAPE\_STATUS enumeration
description: The TAPE\_STATUS enumeration provides a list of the status codes that the tape class driver uses to report the status of a tape device.
ms.assetid: '45e85ad1-5b75-410e-b9dd-061051bbaa74'
keywords: ["TAPE_STATUS enumeration Storage Devices", "PTAPE_STATUS enumeration pointer Storage Devices"]
topic_type:
- apiref
api_name:
- TAPE_STATUS
api_location:
- minitape.h
api_type:
- HeaderDef
---

# TAPE\_STATUS enumeration

The TAPE\_STATUS enumeration provides a list of the status codes that the tape class driver uses to report the status of a tape device.

## Syntax


```C++
typedef enum _TAPE_STATUS { 
  TAPE_STATUS_SEND_SRB_AND_CALLBACK        = 0,
  TAPE_STATUS_CALLBACK                     = 1,
  TAPE_STATUS_CHECK_TEST_UNIT_READY        = 2,
  TAPE_STATUS_SUCCESS                      = 3,
  TAPE_STATUS_INSUFFICIENT_RESOURCES       = 4,
  TAPE_STATUS_NOT_IMPLEMENTED              = 5,
  TAPE_STATUS_INVALID_DEVICE_REQUEST       = 6,
  TAPE_STATUS_INVALID_PARAMETER            = 7,
  TAPE_STATUS_MEDIA_CHANGED                = 8,
  TAPE_STATUS_BUS_RESET                    = 9,
  TAPE_STATUS_SETMARK_DETECTED             = 10,
  TAPE_STATUS_FILEMARK_DETECTED            = 11,
  TAPE_STATUS_BEGINNING_OF_MEDIA           = 12,
  TAPE_STATUS_END_OF_MEDIA                 = 13,
  TAPE_STATUS_BUFFER_OVERFLOW              = 14,
  TAPE_STATUS_NO_DATA_DETECTED             = 15,
  TAPE_STATUS_EOM_OVERFLOW                 = 16,
  TAPE_STATUS_NO_MEDIA                     = 17,
  TAPE_STATUS_IO_DEVICE_ERROR              = 18,
  TAPE_STATUS_UNRECOGNIZED_MEDIA           = 19,
  TAPE_STATUS_DEVICE_NOT_READY             = 20,
  TAPE_STATUS_MEDIA_WRITE_PROTECTED        = 21,
  TAPE_STATUS_DEVICE_DATA_ERROR            = 22,
  TAPE_STATUS_NO_SUCH_DEVICE               = 23,
  TAPE_STATUS_INVALID_BLOCK_LENGTH         = 24,
  TAPE_STATUS_IO_TIMEOUT                   = 25,
  TAPE_STATUS_DEVICE_NOT_CONNECTED         = 26,
  TAPE_STATUS_DATA_OVERRUN                 = 27,
  TAPE_STATUS_DEVICE_BUSY                  = 28,
  TAPE_STATUS_REQUIRES_CLEANING            = 29,
  TAPE_STATUS_CLEANER_CARTRIDGE_INSTALLED  = 30
} TAPE_STATUS, *PTAPE_STATUS;
```



## Constants

<dl> <dt>

<span id="TAPE_STATUS_SEND_SRB_AND_CALLBACK"></span><span id="tape_status_send_srb_and_callback"></span>**TAPE\_STATUS\_SEND\_SRB\_AND\_CALLBACK**
</dt> <dd>

Directs the tape class driver to send the SRB to the device. A tape miniclass routine usually returns this status after filling in the SRB passed by the tape class driver. If the operation is successful, the class driver increments a counter called a "call number" and calls the miniclass routine again. If the SRB fails, the class driver might call the miniclass routine again. For more information about how and when tape miniclass drivers should report this status value, see [Processing Tape Device Control Requests](https://msdn.microsoft.com/library/windows/hardware/ff563934).

</dd> <dt>

<span id="TAPE_STATUS_CALLBACK"></span><span id="tape_status_callback"></span>**TAPE\_STATUS\_CALLBACK**
</dt> <dd>

Directs the tape class driver to increment the call number counter without sending an SRB to the device. For more information about how tape miniclass drivers should make use of this status value, see [Processing Tape Device Control Requests](https://msdn.microsoft.com/library/windows/hardware/ff563934).

</dd> <dt>

<span id="TAPE_STATUS_CHECK_TEST_UNIT_READY"></span><span id="tape_status_check_test_unit_ready"></span>**TAPE\_STATUS\_CHECK\_TEST\_UNIT\_READY**
</dt> <dd>

Directs the tape class driver to create an SRB for the TEST UNIT READY command and to send the SRB to the device.

</dd> <dt>

<span id="TAPE_STATUS_SUCCESS"></span><span id="tape_status_success"></span>**TAPE\_STATUS\_SUCCESS**
</dt> <dd>

Indicates that the operation was successful.

</dd> <dt>

<span id="TAPE_STATUS_INSUFFICIENT_RESOURCES"></span><span id="tape_status_insufficient_resources"></span>**TAPE\_STATUS\_INSUFFICIENT\_RESOURCES**
</dt> <dd>

Indicates that there were not enough resources available to the miniclass driver for it to complete the operation.

</dd> <dt>

<span id="TAPE_STATUS_NOT_IMPLEMENTED"></span><span id="tape_status_not_implemented"></span>**TAPE\_STATUS\_NOT\_IMPLEMENTED**
</dt> <dd>

Indicates that the requested operation is not supported.

</dd> <dt>

<span id="TAPE_STATUS_INVALID_DEVICE_REQUEST"></span><span id="tape_status_invalid_device_request"></span>**TAPE\_STATUS\_INVALID\_DEVICE\_REQUEST**
</dt> <dd>

Indicates that the requested operation is invalid.

</dd> <dt>

<span id="TAPE_STATUS_INVALID_PARAMETER"></span><span id="tape_status_invalid_parameter"></span>**TAPE\_STATUS\_INVALID\_PARAMETER**
</dt> <dd>

Indicates that one or more of the parameter values provided with the request are invalid.

</dd> <dt>

<span id="TAPE_STATUS_MEDIA_CHANGED"></span><span id="tape_status_media_changed"></span>**TAPE\_STATUS\_MEDIA\_CHANGED**
</dt> <dd>

Indicates that the media in the drive might have changed.

</dd> <dt>

<span id="TAPE_STATUS_BUS_RESET"></span><span id="tape_status_bus_reset"></span>**TAPE\_STATUS\_BUS\_RESET**
</dt> <dd>

Indicates that the bus has been reset.

</dd> <dt>

<span id="TAPE_STATUS_SETMARK_DETECTED"></span><span id="tape_status_setmark_detected"></span>**TAPE\_STATUS\_SETMARK\_DETECTED**
</dt> <dd>

Indicates that a setmark was encountered during a tape operation.

</dd> <dt>

<span id="TAPE_STATUS_FILEMARK_DETECTED"></span><span id="tape_status_filemark_detected"></span>**TAPE\_STATUS\_FILEMARK\_DETECTED**
</dt> <dd>

Indicates that a filemark was encountered during a tape operation.

</dd> <dt>

<span id="TAPE_STATUS_BEGINNING_OF_MEDIA"></span><span id="tape_status_beginning_of_media"></span>**TAPE\_STATUS\_BEGINNING\_OF\_MEDIA**
</dt> <dd>

Indicates that the beginning of the media was encountered during a tape operation.

</dd> <dt>

<span id="TAPE_STATUS_END_OF_MEDIA"></span><span id="tape_status_end_of_media"></span>**TAPE\_STATUS\_END\_OF\_MEDIA**
</dt> <dd>

Indicates that the end of the media was encountered during a tape operation.

</dd> <dt>

<span id="TAPE_STATUS_BUFFER_OVERFLOW"></span><span id="tape_status_buffer_overflow"></span>**TAPE\_STATUS\_BUFFER\_OVERFLOW**
</dt> <dd>

Indicates that a buffer overflow occurred.

</dd> <dt>

<span id="TAPE_STATUS_NO_DATA_DETECTED"></span><span id="tape_status_no_data_detected"></span>**TAPE\_STATUS\_NO\_DATA\_DETECTED**
</dt> <dd>

Indicates that no data was detected.

</dd> <dt>

<span id="TAPE_STATUS_EOM_OVERFLOW"></span><span id="tape_status_eom_overflow"></span>**TAPE\_STATUS\_EOM\_OVERFLOW**
</dt> <dd>

Indicates that an attempt was made to exceed the physical end of the media during a tape operation.

</dd> <dt>

<span id="TAPE_STATUS_NO_MEDIA"></span><span id="tape_status_no_media"></span>**TAPE\_STATUS\_NO\_MEDIA**
</dt> <dd>

Indicates that the tape operation failed, because there is no media in the drive.

</dd> <dt>

<span id="TAPE_STATUS_IO_DEVICE_ERROR"></span><span id="tape_status_io_device_error"></span>**TAPE\_STATUS\_IO\_DEVICE\_ERROR**
</dt> <dd>

Indicates that an I/O error occurred during a tape operation.

</dd> <dt>

<span id="TAPE_STATUS_UNRECOGNIZED_MEDIA"></span><span id="tape_status_unrecognized_media"></span>**TAPE\_STATUS\_UNRECOGNIZED\_MEDIA**
</dt> <dd>

Indicates that the type of the media is not supported.

</dd> <dt>

<span id="TAPE_STATUS_DEVICE_NOT_READY"></span><span id="tape_status_device_not_ready"></span>**TAPE\_STATUS\_DEVICE\_NOT\_READY**
</dt> <dd>

Indicates that the device is not ready.

</dd> <dt>

<span id="TAPE_STATUS_MEDIA_WRITE_PROTECTED"></span><span id="tape_status_media_write_protected"></span>**TAPE\_STATUS\_MEDIA\_WRITE\_PROTECTED**
</dt> <dd>

Indicates that the media is write protected.

</dd> <dt>

<span id="TAPE_STATUS_DEVICE_DATA_ERROR"></span><span id="tape_status_device_data_error"></span>**TAPE\_STATUS\_DEVICE\_DATA\_ERROR**
</dt> <dd>

Indicates that a cyclic redundancy check (CRC) error occurred.

</dd> <dt>

<span id="TAPE_STATUS_NO_SUCH_DEVICE"></span><span id="tape_status_no_such_device"></span>**TAPE\_STATUS\_NO\_SUCH\_DEVICE**
</dt> <dd>

Indicates that no such device exists.

</dd> <dt>

<span id="TAPE_STATUS_INVALID_BLOCK_LENGTH"></span><span id="tape_status_invalid_block_length"></span>**TAPE\_STATUS\_INVALID\_BLOCK\_LENGTH**
</dt> <dd>

Indicates that the block length is invalid.

</dd> <dt>

<span id="TAPE_STATUS_IO_TIMEOUT"></span><span id="tape_status_io_timeout"></span>**TAPE\_STATUS\_IO\_TIMEOUT**
</dt> <dd>

Indicates that the I/O operation timed out.

</dd> <dt>

<span id="TAPE_STATUS_DEVICE_NOT_CONNECTED"></span><span id="tape_status_device_not_connected"></span>**TAPE\_STATUS\_DEVICE\_NOT\_CONNECTED**
</dt> <dd>

Indicates that the device is disconnected.

</dd> <dt>

<span id="TAPE_STATUS_DATA_OVERRUN"></span><span id="tape_status_data_overrun"></span>**TAPE\_STATUS\_DATA\_OVERRUN**
</dt> <dd>

Indicates that the tape operation could not be performed because of a data overrun.

</dd> <dt>

<span id="TAPE_STATUS_DEVICE_BUSY"></span><span id="tape_status_device_busy"></span>**TAPE\_STATUS\_DEVICE\_BUSY**
</dt> <dd>

Indicates that the tape operation could not be performed, because the device is busy.

</dd> <dt>

<span id="TAPE_STATUS_REQUIRES_CLEANING"></span><span id="tape_status_requires_cleaning"></span>**TAPE\_STATUS\_REQUIRES\_CLEANING**
</dt> <dd>

Indicates that the tape operation could not be performed because the device requires cleaning.

</dd> <dt>

<span id="TAPE_STATUS_CLEANER_CARTRIDGE_INSTALLED"></span><span id="tape_status_cleaner_cartridge_installed"></span>**TAPE\_STATUS\_CLEANER\_CARTRIDGE\_INSTALLED**
</dt> <dd>

Indicates that the media currently in the drive is a cleaner cartridge.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Minitape.h (include Ntddtape.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_TAPE\_GET\_STATUS**](ioctl-tape-get-status.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20TAPE_STATUS%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






