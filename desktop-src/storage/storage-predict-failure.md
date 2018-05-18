---
title: STORAGE\_PREDICT\_FAILURE structure
description: The STORAGE\_PREDICT\_FAILURE structure is used in conjunction with IOCTL\_STORAGE\_PREDICT\_FAILURE to report whether a device is currently predicting a failure.
ms.assetid: '56e178d9-e6bb-43d4-b062-da4e699c4efc'
keywords: ["STORAGE_PREDICT_FAILURE structure Storage Devices", "PSTORAGE_PREDICT_FAILURE structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- STORAGE_PREDICT_FAILURE
api_location:
- ntddstor.h
api_type:
- HeaderDef
---

# STORAGE\_PREDICT\_FAILURE structure

The STORAGE\_PREDICT\_FAILURE structure is used in conjunction with [**IOCTL\_STORAGE\_PREDICT\_FAILURE**](ioctl-storage-predict-failure.md) to report whether a device is currently predicting a failure.

## Syntax


```C++
typedef struct _STORAGE_PREDICT_FAILURE {
  ULONG PredictFailure;
  UCHAR VendorSpecific[512];
} STORAGE_PREDICT_FAILURE, *PSTORAGE_PREDICT_FAILURE;
```



## Members

<dl> <dt>

**PredictFailure**
</dt> <dd>

Indicates when nonzero that the device is currently predicting an imminent failure.

</dd> <dt>

**VendorSpecific**
</dt> <dd>

Contains an array that holds 512 bytes of vendor-specific information if the device supports failure prediction.

</dd> </dl>

## Remarks

Upon receiving an [**IOCTL\_STORAGE\_PREDICT\_FAILURE**](ioctl-storage-predict-failure.md) device control request, the disk class driver attempts to verify if an IDE drive supports SMART. If the drive is a SCSI drive, the class driver attempts to verify if the SCSI disk supports the equivalent IDE SMART technology: Information Exception Control Page, X3T10/94-190 Rev 4.

If the device does not support failure prediction, the disk class driver fails the IRP with a status of STATUS\_INVALID\_DEVICE\_REQUEST.

If the device supports failure prediction, the disk class driver queries the device for failure prediction status. If the device has bad sectors and predicts a failure, the disk class driver returns a nonzero value in **PredictFailure**. If status indicates that the device does not predict any failures at this time, the disk class driver returns a value of 0 in **PredictFailure**.

## Requirements



|                   |                                                                                                                          |
|-------------------|--------------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h or Minitape.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_STORAGE\_PREDICT\_FAILURE**](ioctl-storage-predict-failure.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_PREDICT_FAILURE%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






