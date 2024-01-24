---
title: WINBIO_BDB_ANSI_381_RECORD structure (Winbio\_types.h)
description: Contains information about a single fingerprint or palm sample from an end user.
ms.assetid: e0b32d05-3e96-4b42-9e18-57d10513f224
keywords:
- WINBIO_BDB_ANSI_381_RECORD structure Windows Biometric Framework API
topic_type:
- apiref
api_name:
- WINBIO_BDB_ANSI_381_RECORD
api_location:
- Winbio_types.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WINBIO\_BDB\_ANSI\_381\_RECORD structure

The **WINBIO\_BDB\_ANSI\_381\_RECORD** structure contains information about a single fingerprint or palm sample from an end user. A collection of these structures is included in each [**WINBIO\_BDB\_ANSI\_381\_HEADER**](winbio-bdb-ansi-381-header.md) structure.

## Syntax


```C++
typedef struct _WINBIO_BDB_ANSI_381_RECORD {
  ULONG                    BlockLength;
  USHORT                   HorizontalLineLength;
  USHORT                   VerticalLineLength;
  WINBIO_BIOMETRIC_SUBTYPE Position;
  UCHAR                    CountOfViews;
  UCHAR                    ViewNumber;
  UCHAR                    ImageQuality;
  UCHAR                    ImpressionType;
  UCHAR                    Reserved;
} WINBIO_BDB_ANSI_381_RECORD;
```



## Members

<dl> <dt>

**BlockLength**
</dt> <dd>

Contains the number of bytes in this structure plus the number of bytes of sample image data.

</dd> <dt>

**HorizontalLineLength**
</dt> <dd>

Specifies the number of pixels in a horizontal line of the sample.

</dd> <dt>

**VerticalLineLength**
</dt> <dd>

Specifies the number of pixels in a vertical line of the sample.

</dd> <dt>

**Position**
</dt> <dd>

A **WINBIO\_BIOMETRIC\_SUBTYPE** value that specifies the finger or palm used to generate the biometric sample. For more information, see Remarks.

</dd> <dt>

**CountOfViews**
</dt> <dd>

This must be set to one (1);

</dd> <dt>

**ViewNumber**
</dt> <dd>

This must be set to one (1);

</dd> <dt>

**ImageQuality**
</dt> <dd>

Reserved. This must be 254 (0xFE).

</dd> <dt>

**ImpressionType**
</dt> <dd>

Reserved.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved. Must be set to zero (0).

</dd> </dl>

## Remarks

The *Position* member specifies the area of the hand or palm used to make the biometric sample. The Windows Biometric Framework (WBF) currently supports only fingerprint capture and uses the following constants to represent position information.

-   WINBIO\_ANSI\_381\_POS\_UNKNOWN
-   WINBIO\_ANSI\_381\_POS\_RH\_THUMB
-   WINBIO\_ANSI\_381\_POS\_RH\_INDEX\_FINGER
-   WINBIO\_ANSI\_381\_POS\_RH\_MIDDLE\_FINGER
-   WINBIO\_ANSI\_381\_POS\_RH\_RING\_FINGER
-   WINBIO\_ANSI\_381\_POS\_RH\_LITTLE\_FINGER
-   WINBIO\_ANSI\_381\_POS\_LH\_THUMB
-   WINBIO\_ANSI\_381\_POS\_LH\_INDEX\_FINGER
-   WINBIO\_ANSI\_381\_POS\_LH\_MIDDLE\_FINGER
-   WINBIO\_ANSI\_381\_POS\_LH\_RING\_FINGER
-   WINBIO\_ANSI\_381\_POS\_LH\_LITTLE\_FINGER
-   WINBIO\_ANSI\_381\_POS\_RH\_FOUR\_FINGERS
-   WINBIO\_ANSI\_381\_POS\_LH\_FOUR\_FINGERS
-   WINBIO\_ANSI\_381\_POS\_TWO\_THUMBS

> [!IMPORTANT]
>
> Do not attempt to validate the value supplied for the *Position* value. The Windows Biometrics Service will validate the supplied value before passing it through to your implementation. If the value is **WINBIO\_SUBTYPE\_NO\_INFORMATION** or **WINBIO\_SUBTYPE\_ANY**, then validate where appropriate.

 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                                       |
| Header<br/>                   | <dl> <dt>Winbio\_types.h (include Winbio.h)</dt> </dl> |



## See also

<dl> <dt>

[Client Application Structures](client-application-structures.md)
</dt> </dl>

 

 





