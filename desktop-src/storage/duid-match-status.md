---
title: DUID\_MATCH\_STATUS enumeration
description: The DUID\_MATCH\_STATUS enumeration lists the status values that the CompareStorageDuids routine returns.
ms.assetid: 61a60e77-387c-42d6-b56b-694ce0c86570
keywords:
- DUID_MATCH_STATUS enumeration Storage Devices
topic_type:
- apiref
api_name:
- DUID_MATCH_STATUS
api_location:
- storduid.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DUID\_MATCH\_STATUS enumeration

The DUID\_MATCH\_STATUS enumeration lists the status values that the [**CompareStorageDuids**](comparestorageduids.md) routine returns.

## Syntax


```C++
typedef enum _DUID_MATCH_STATUS { 
  DuidExactMatch                    = 0,
  DuidSubIdMatch                    = 1,
  DuidNoMatch                       = 2,
  DuidErrorGeneral                  = 100,
  DuidErrorMissingDuid              = 101,
  DuidErrorVersionMismatch          = 102,
  DuidErrorInvalidDuid              = 103,
  DuidErrorInvalidDeviceIdDescSize  = 104,
  DuidErrorInvalidDeviceDescSize    = 105,
  DuidErrorInvalidLayoutSigSize     = 106,
  DuidErrorInvalidLayoutSigVersion  = 107,
  DuidErrorMaximum                  = 108
} DUID_MATCH_STATUS;
```



## Constants

<dl> <dt>

<span id="DuidExactMatch"></span><span id="duidexactmatch"></span><span id="DUIDEXACTMATCH"></span>**DuidExactMatch**
</dt> <dd>

All fields in the two Device Unique Identifiers (DUIDs) match exactly.

</dd> <dt>

<span id="DuidSubIdMatch"></span><span id="duidsubidmatch"></span><span id="DUIDSUBIDMATCH"></span>**DuidSubIdMatch**
</dt> <dd>

Either the serial number or one of the unique sub-IDs matches. The two DUIDs probably represent the same device.

</dd> <dt>

<span id="DuidNoMatch"></span><span id="duidnomatch"></span><span id="DUIDNOMATCH"></span>**DuidNoMatch**
</dt> <dd>

None of the sub-IDs match in page 83h of the vital product data (VPD). None of the non-VPD data matches.

</dd> <dt>

<span id="DuidErrorGeneral"></span><span id="duiderrorgeneral"></span><span id="DUIDERRORGENERAL"></span>**DuidErrorGeneral**
</dt> <dd>

An error occurred for an unspecified cause.

</dd> <dt>

<span id="DuidErrorMissingDuid"></span><span id="duiderrormissingduid"></span><span id="DUIDERRORMISSINGDUID"></span>**DuidErrorMissingDuid**
</dt> <dd>

One of the two DUIDs to compare is missing.

</dd> <dt>

<span id="DuidErrorVersionMismatch"></span><span id="duiderrorversionmismatch"></span><span id="DUIDERRORVERSIONMISMATCH"></span>**DuidErrorVersionMismatch**
</dt> <dd>

The two DUIDs to compare do not have the same version.

</dd> <dt>

<span id="DuidErrorInvalidDuid"></span><span id="duiderrorinvalidduid"></span><span id="DUIDERRORINVALIDDUID"></span>**DuidErrorInvalidDuid**
</dt> <dd>

At least one of the two DUIDs to compare is invalid.

</dd> <dt>

<span id="DuidErrorInvalidDeviceIdDescSize"></span><span id="duiderrorinvaliddeviceiddescsize"></span><span id="DUIDERRORINVALIDDEVICEIDDESCSIZE"></span>**DuidErrorInvalidDeviceIdDescSize**
</dt> <dd>

At least one of the two DUIDs to compare contains an invalid device ID descriptor ([**STORAGE\_DEVICE\_ID\_DESCRIPTOR**](storage-device-id-descriptor.md)). This descriptor reports VPD data.

</dd> <dt>

<span id="DuidErrorInvalidDeviceDescSize"></span><span id="duiderrorinvaliddevicedescsize"></span><span id="DUIDERRORINVALIDDEVICEDESCSIZE"></span>**DuidErrorInvalidDeviceDescSize**
</dt> <dd>

At least one of the two DUIDs to compare contains an invalid device descriptor ([**STORAGE\_DEVICE\_DESCRIPTOR**](storage-device-descriptor.md)). This descriptor reports non-VPD inquiry data..

</dd> <dt>

<span id="DuidErrorInvalidLayoutSigSize"></span><span id="duiderrorinvalidlayoutsigsize"></span><span id="DUIDERRORINVALIDLAYOUTSIGSIZE"></span>**DuidErrorInvalidLayoutSigSize**
</dt> <dd>

At least one of the two DUIDs to compare contains an invalid drive layout signature size.

</dd> <dt>

<span id="DuidErrorInvalidLayoutSigVersion"></span><span id="duiderrorinvalidlayoutsigversion"></span><span id="DUIDERRORINVALIDLAYOUTSIGVERSION"></span>**DuidErrorInvalidLayoutSigVersion**
</dt> <dd>

At least one of the two DUIDs to compare contains an invalid drive layout signature.

</dd> <dt>

<span id="DuidErrorMaximum"></span><span id="duiderrormaximum"></span><span id="DUIDERRORMAXIMUM"></span>**DuidErrorMaximum**
</dt> <dd>

This value delimits the upper limit of the enumeration values in this enumeration. This value allows a DUID consumer to create a loop that tests for all valid error values that the [**CompareStorageDuids**](comparestorageduids.md) routine returns. As new identifier data is added to future versions of the DUID, new error values will specify which parts of the DUID are not well-formed.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Storduid.h (include Storduid.h)</dt> </dl> |



## See also

<dl> <dt>

[**CompareStorageDuids**](comparestorageduids.md)
</dt> <dt>

[**STORAGE\_DEVICE\_DESCRIPTOR**](storage-device-descriptor.md)
</dt> <dt>

[**STORAGE\_DEVICE\_ID\_DESCRIPTOR**](storage-device-id-descriptor.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DUID_MATCH_STATUS%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






