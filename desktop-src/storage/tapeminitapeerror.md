---
title: TAPE\_ERROR\_ROUTINE routine
description: TAPE\_ERROR\_ROUTINE provides device-specific error handling when an SRB is completed with an error status. This routine is optional.
ms.assetid: 'a39fac12-f284-4b3a-a9ab-ae75934f810e'
keywords: ["( TAPE_ERROR_ROUTINE) routine Storage Devices", "TAPE_ERROR_ROUTINE"]
topic_type:
- apiref
api_name:
- ( TAPE_ERROR_ROUTINE)
api_location:
- minitape.h
api_type:
- UserDefined
---

# TAPE\_ERROR\_ROUTINE routine

*TAPE\_ERROR\_ROUTINE* provides device-specific error handling when an SRB is completed with an error status. This routine is optional.

## Syntax


```C++
TAPE_ERROR_ROUTINE (*TAPE_ERROR_ROUTINE);

VOID (*TAPE_ERROR_ROUTINE)(
  _In_    PVOID               MinitapeExtension,
  _In_    PSCSI_REQUEST_BLOCK Srb,
  _Inout_ PTAPE_STATUS        TapeStatus
)
{ ... }
```



## Parameters

<dl> <dt>

*MinitapeExtension* \[in\]
</dt> <dd>

Pointer to the driver-specific minitape extension. This is **NULL** if the miniclass driver did not request a minitape extension when it initialized.

</dd> <dt>

*Srb* \[in\]
</dt> <dd>

Pointer to the SRB for the operation that failed.

</dd> <dt>

*TapeStatus* \[in, out\]
</dt> <dd>

Pointer to the [**TAPE\_STATUS**](tape-status.md) set by the tape class driver. The tape miniclass driver can change the TAPE\_STATUS or leave it unchanged.

</dd> </dl>

## Return value

None.

## Remarks

Most tape miniclass drivers do not provide a *TAPE\_ERROR\_ROUTINE* routine because the [**TAPE\_STATUS**](tape-status.md) codes set by the tape class driver are appropriate.

For some devices, however, a tape miniclass driver can identify a more appropriate error code than the tape class driver. For example, if the tape class driver returns TAPE\_STATUS\_BUS\_RESET, the tape miniclass driver might be able to determine that the real problem is more accurately represented by TAPE\_STATUS\_NO\_MEDIA for some devices.

A tape miniclass driver optionally specifies an entry point for its *TAPE\_ERROR\_ROUTINE* routine in the TAPE\_INIT\_DATA\_EX structure it passes to [**TapeClassInitialize**](tapeclassinitialize.md) from its **DriverEntry** routine. For such a miniclass driver, when an error occurs during a read, write, or device-control command, the tape class driver sets an appropriate TAPE\_STATUS code and calls the miniclass driver's *TAPE\_ERROR\_ROUTINE* routine with the minitape extension, the failed SRB, and the TAPE\_STATUS code that would be returned.

*TAPE\_ERROR\_ROUTINE* determines whether to alter the status provided by the tape class driver based on the input parameters and its knowledge of the device. If the SRB\_STATUS\_AUTOSENSE\_VALID bit is set in **Srb-&gt;SrbStatus**, then the SRB contains SCSI sense information at **SenseInfoBuffer**. The length of the buffer is **SenseInfoBufferLength**. The *TAPE\_ERROR\_ROUTINE* routine should examine this information along with the **SrbStatus** and **ScsiStatus** in the SRB to determine whether to change the TAPE\_STATUS returned.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Minitape.h (include Minitape.h)</dt> </dl> |



## See also

<dl> <dt>

[**DriverEntry of Tape Miniclass Driver**](driverentry-of-tape-miniclass-driver.md)
</dt> <dt>

[**SCSI\_REQUEST\_BLOCK**](scsi-request-block.md)
</dt> <dt>

[**TAPE\_INIT\_DATA\_EX**](tape-init-data-ex.md)
</dt> <dt>

[**TapeClassInitialize**](tapeclassinitialize.md)
</dt> <dt>

[**TAPE\_STATUS**](tape-status.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20TAPE_ERROR_ROUTINE%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






