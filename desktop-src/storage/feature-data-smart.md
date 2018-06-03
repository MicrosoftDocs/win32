---
title: FEATURE\_DATA\_SMART structure
description: The FEATURE\_DATA\_SMART structure holds data for the S.M.A.R.T. feature.
ms.assetid: cf6578d1-e455-4bbe-a89f-bc0292e24a4a
keywords:
- FEATURE_DATA_SMART structure Storage Devices
- PFEATURE_DATA_SMART structure pointer Storage Devices
topic_type:
- apiref
api_name:
- FEATURE_DATA_SMART
api_location:
- ntddmmc.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# FEATURE\_DATA\_SMART structure

The FEATURE\_DATA\_SMART structure holds data for the S.M.A.R.T. feature.

## Syntax


```C++
typedef struct _FEATURE_DATA_SMART {
  FEATURE_HEADER Header;
  UCHAR          FaultFailureReportingPagePresent  :1;
  UCHAR          Reserved1  :7;
  UCHAR          Reserved02[3];
} FEATURE_DATA_SMART, *PFEATURE_DATA_SMART;
```



## Members

<dl> <dt>

**Header**
</dt> <dd>

Contains a [**FEATURE\_HEADER**](feature-header.md) structure with header information for this feature descriptor.

</dd> <dt>

**FaultFailureReportingPagePresent**
</dt> <dd>

Indicates, when set to 1, that the device supports the Fault / Failure Reporting Mode. If set to zero, the device does not support this mode.

</dd> <dt>

**Reserved1**
</dt> <dd>

Reserved.

</dd> <dt>

**Reserved02**
</dt> <dd>

Reserved.

</dd> </dl>

## Remarks

This structure holds data for the feature named "S.M.A.R.T." by the *SCSI Multimedia - 4 (MMC-4)* specification. Devices that support this feature support Self-Monitoring Analysis and Reporting Technology (SMART).

## Requirements



|                   |                                                                                                           |
|-------------------|-----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddmmc.h (include Ntddcdrm.h)</dt> </dl> |



## See also

<dl> <dt>

[**FEATURE\_HEADER**](feature-header.md)
</dt> <dt>

[**FEATURE\_NUMBER**](feature-number.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20FEATURE_DATA_SMART%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






