---
title: IOCTL\_STORAGE\_PREDICT\_FAILURE control code
description: Polls for a prediction of device failure.
ms.assetid: 56e178d9-e6bb-43d4-b062-da4e699c4efc
keywords:
- IOCTL_STORAGE_PREDICT_FAILURE control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_STORAGE_PREDICT_FAILURE
api_location:
- Ntddstor.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IOCTL\_STORAGE\_PREDICT\_FAILURE control code

Polls for a prediction of device failure. This request works with the IDE disk drives that support self-monitoring analysis and reporting technology (SMART). If the drive is a SCSI drive, the class driver attempts to verify if the SCSI disk supports the equivalent IDE SMART technology by check the inquiry information on the Information Exception Control Page, X3T10/94-190 Rev 4.

If the device supports prediction failure, the disk class driver queries the device for failure prediction status and reports the results. If the disk class driver assigns a nonzero value to the **PredictFailure** member of [**STORAGE\_PREDICT\_FAILURE**](storage-predict-failure.md) in the output buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**, the disk has bad sectors and is predicting a failure. The storage stack returns 512 bytes of vendor-specific information about the failure prediction in the **VendorSpecific** member of STORAGE\_PREDICT\_FAILURE.

If the **PredictFailure** member contains a value of zero, the disk is not predicting a failure.

If the device does not support failure prediction, IOCTL\_STORAGE\_PREDICT\_FAILURE fails with a status of STATUS\_INVALID\_DEVICE\_REQUEST, and the data in the output buffer is undefined

Other means of checking for disk failure include monitoring the event log and registering to receive a WMI event with WMI\_STORAGE\_PREDICT\_FAILURE\_EVENT\_GUID.

## Input Buffer

None.

## Input Buffer Length

None.

## Output Buffer

The driver returns a [**STORAGE\_PREDICT\_FAILURE**](storage-predict-failure.md) structure containing failure prediction data in the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**.

## Output Buffer Length

**Parameters.DeviceIoControl.OutputBufferLength** indicates the size, in bytes, of the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer,** which must be greater or equal to the **sizeof**(STORAGE\_PREDICT\_FAILURE).

## Status block

**Irp-&gt;IoStatus.Status** is set to STATUS\_SUCCESS if the request is successful. Otherwise, **Status** to the appropriate error condition as a [NTSTATUS](https://msdn.microsoft.com/library/windows/hardware/ff557697) code.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**STORAGE\_PREDICT\_FAILURE**](storage-predict-failure.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_STORAGE_PREDICT_FAILURE%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






