---
title: WINBIO_BIR_HEADER structure (Winbio\_types.h)
description: Contains the header of a biometric information record (BIR).
ms.assetid: 4b020720-42ef-4ac7-aaa3-7a0e45198890
keywords:
- WINBIO_BIR_HEADER structure Windows Biometric Framework API
topic_type:
- apiref
api_name:
- WINBIO_BIR_HEADER
api_location:
- Winbio_types.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WINBIO\_BIR\_HEADER structure

The **WINBIO\_BIR\_HEADER** structure contains the header of a biometric information record (BIR).

## Syntax


```C++
typedef struct _WINBIO_BIR_HEADER {
  USHORT                   ValidFields;
  WINBIO_BIR_VERSION       HeaderVersion;
  WINBIO_BIR_VERSION       PatronHeaderVersion;
  WINBIO_BIR_DATA_FLAGS    DataFlags;
  WINBIO_BIOMETRIC_TYPE    Type;
  WINBIO_BIOMETRIC_SUBTYPE Subtype;
  WINBIO_BIR_PURPOSE       Purpose;
  WINBIO_BIR_QUALITY       DataQuality;
  LARGE_INTEGER            CreationDate;
  struct {
    LARGE_INTEGER BeginDate;
    LARGE_INTEGER EndDate;
  } ValidityPeriod;
  WINBIO_REGISTERED_FORMAT BiometricDataFormat;
  WINBIO_REGISTERED_FORMAT ProductId;
} WINBIO_BIR_HEADER;
```



## Members

<dl> <dt>

**ValidFields**
</dt> <dd>

Bitmask that specifies which fields in this structure are valid. For more information, see [**WINBIO\_BIR\_FIELD Constants**](winbio-bir-field-constants.md).

</dd> <dt>

**HeaderVersion**
</dt> <dd>

A **WINBIO\_BIR\_VERSION** constant that specifies the header version. Version numbers are 8-bit values where the upper four bits specify the major number and the low four bits specify the minor version number. Currently this must be WINBIO\_CBEFF\_HEADER\_VERSION (0x11).

</dd> <dt>

**PatronHeaderVersion**
</dt> <dd>

A **WINBIO\_BIR\_VERSION** constant that specifies the header version. Version numbers are 8-bit values where the upper four bits specify the major number and the low four bits specify the minor version number. Currently this must be WINBIO\_PATRON\_HEADER\_VERSION (0x11).

</dd> <dt>

**DataFlags**
</dt> <dd>

A value that specifies the format of the header data. This can be a bitwise **OR** of the following security and processing level flags. For more information, see [**WINBIO\_BIR\_DATA\_FLAGS Constants**](winbio-bir-data-flags-constants.md).



| Value                                                                                                                                                                                                                                                                                                     | Meaning                                                                                                                                                                                                             |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="WINBIO_DATA_FLAG_PRIVACY"></span><span id="winbio_data_flag_privacy"></span><dl> <dt>**WINBIO\_DATA\_FLAG\_PRIVACY**</dt> <dt>((UCHAR)0x02)</dt> </dl>                                       | The data is encrypted.<br/>                                                                                                                                                                                   |
| <span id="WINBIO_DATA_FLAG_INTEGRITY"></span><span id="winbio_data_flag_integrity"></span><dl> <dt>**WINBIO\_DATA\_FLAG\_INTEGRITY**</dt> <dt>((UCHAR)0x01)</dt> </dl>                                 | The data is digitally signed or protected by a message authentication code (MAC).<br/>                                                                                                                        |
| <span id="WINBIO_DATA_FLAG_SIGNED"></span><span id="winbio_data_flag_signed"></span><dl> <dt>**WINBIO\_DATA\_FLAG\_SIGNED**</dt> <dt>((UCHAR)0x04)</dt> </dl>                                          | If this flag and the **WINBIO\_DATA\_FLAG\_INTEGRITY** flag are set, the data is signed. If this flag is not set but the **WINBIO\_DATA\_FLAG\_INTEGRITY** flag is set, a MAC is computed over the data.<br/> |
| <span id="WINBIO_DATA_FLAG_RAW"></span><span id="winbio_data_flag_raw"></span><dl> <dt>**WINBIO\_DATA\_FLAG\_RAW**</dt> <dt>((UCHAR)0x20)</dt> </dl>                                                   | The data is in the format with which it was captured.<br/>                                                                                                                                                    |
| <span id="WINBIO_DATA_FLAG_INTERMEDIATE"></span><span id="winbio_data_flag_intermediate"></span><dl> <dt>**WINBIO\_DATA\_FLAG\_INTERMEDIATE**</dt> <dt>((UCHAR)0x40)</dt> </dl>                        | The data is not raw but has not been completely processed.<br/>                                                                                                                                               |
| <span id="WINBIO_DATA_FLAG_PROCESSED"></span><span id="winbio_data_flag_processed"></span><dl> <dt>**WINBIO\_DATA\_FLAG\_PROCESSED**</dt> <dt>((UCHAR)0x80)</dt> </dl>                                 | The data has been processed.<br/>                                                                                                                                                                             |
| <span id="WINBIO_DATA_FLAG_OPTION_MASK_PRESENT"></span><span id="winbio_data_flag_option_mask_present"></span><dl> <dt>**WINBIO\_DATA\_FLAG\_OPTION\_MASK\_PRESENT**</dt> <dt>((UCHAR)0x08)</dt> </dl> | This value is always 1.<br/>                                                                                                                                                                                  |



 

</dd> <dt>

**Type**
</dt> <dd>

A WINBIO\_BIOMETRIC\_TYPE value that specifies the type of biometric data referenced in the biometric information record. Currently only **WINBIO\_TYPE\_FINGERPRINT** is supported. For more information, see [**WINBIO\_BIOMETRIC\_TYPE Constants**](winbio-biometric-type-constants.md).

</dd> <dt>

**Subtype**
</dt> <dd>

A **WINBIO\_BIOMETRIC\_SUBTYPE** value that specifies the sub-factor associated with the biometric data. For more information, see Remarks and [**WINBIO\_BIOMETRIC\_SUBTYPE Constants**](winbio-biometric-subtype-constants.md).

</dd> <dt>

**Purpose**
</dt> <dd>

A **WINBIO\_BIR\_PURPOSE** mask that specifies the intended use of the data. This can be a bitwise **OR** of the following values. For more information, see [**WINBIO\_BIR\_PURPOSE Constants**](winbio-bir-purpose-constants.md).

-   WINBIO\_PURPOSE\_VERIFY
-   WINBIO\_PURPOSE\_IDENTIFY
-   WINBIO\_PURPOSE\_ENROLL
-   WINBIO\_PURPOSE\_ENROLL\_FOR\_VERIFICATION
-   WINBIO\_PURPOSE\_ENROLL\_FOR\_IDENTIFICATION
-   WINBIO\_PURPOSE\_AUDIT

</dd> <dt>

**DataQuality**
</dt> <dd>

A value that specifies the relative quality of the biometric data in the biometric information record (BIR). This can be an integer from 0 to 100 or one of the following values. For more information, see [**WINBIO\_BIR\_QUALITY Constants**](winbio-bir-quality-constants.md).



| Value                                                                                                                                                                                                                                                                                                        | Meaning                                                                                          |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| <span id="WINBIO_DATA_QUALITY_NOT_SET"></span><span id="winbio_data_quality_not_set"></span><dl> <dt>**WINBIO\_DATA\_QUALITY\_NOT\_SET**</dt> <dt>((WINBIO\_BIR\_QUALITY)-1)</dt> </dl>                   | Quality measurements are supported by the BIR creator but no value is set in the BIR.<br/> |
| <span id="WINBIO_DATA_QUALITY_NOT_SUPPORTED"></span><span id="winbio_data_quality_not_supported"></span><dl> <dt>**WINBIO\_DATA\_QUALITY\_NOT\_SUPPORTED**</dt> <dt>((WINBIO\_BIR\_QUALITY)-2)</dt> </dl> | Quality measurements are not supported by the BIR creator.<br/>                            |



 

</dd> <dt>

**CreationDate**
</dt> <dd>

The date and time, in Coordinated Universal Time (Greenwich Mean Time), that the BIR was created.

</dd> <dt>

**ValidityPeriod**
</dt> <dd>

The period for which the BIR is valid.

<dl> <dt>

**BeginDate**
</dt> <dd>

The date and time, in Coordinated Universal Time, that the validity period starts.

</dd> <dt>

**EndDate**
</dt> <dd>

The date and time, in Coordinated Universal Time, at which the BIR ceases to be valid.

</dd> </dl> </dd> <dt>

**BiometricDataFormat**
</dt> <dd>

A [**WINBIO\_REGISTERED\_FORMAT**](winbio-registered-format.md) structure that specifies the data format of the standard data block in the [**WINBIO\_BIR**](winbio-bir.md) structure. The **WINBIO\_REGISTERED\_FORMAT** members cannot be zero. You can use the following constants to simplify error checking.



| Value                                                                                                                                                                                                                                                                                      | Meaning                                                                                                    |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| <span id="WINBIO_NO_FORMAT_OWNER_AVAILABLE"></span><span id="winbio_no_format_owner_available"></span><dl> <dt>**WINBIO\_NO\_FORMAT\_OWNER\_AVAILABLE**</dt> <dt>((USHORT)0)</dt> </dl> | No IBIA (International Biometric Industry Association) assigned owner value has been specified.<br/> |
| <span id="WINBIO_NO_FORMAT_TYPE_AVAILABLE"></span><span id="winbio_no_format_type_available"></span><dl> <dt>**WINBIO\_NO\_FORMAT\_TYPE\_AVAILABLE**</dt> <dt>((USHORT)0)</dt> </dl>    | No format type has been specified.<br/>                                                              |



 

</dd> <dt>

**ProductId**
</dt> <dd>

A [**WINBIO\_REGISTERED\_FORMAT**](winbio-registered-format.md) structure that specifies the product ID of the component that generated the standard data block in the BIR. The **WINBIO\_REGISTERED\_FORMAT** members can be zero.

</dd> </dl>

## Remarks

The *Subtype* parameter specifies the sub-factor associated with the biometric data. Currently, the Windows Biometric Framework (WBF) supports only fingerprint capture and uses the following constants to represent sub-type information:

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
> Do not attempt to validate the value supplied for the *Subtype* parameter value. The Windows Biometrics Service will validate the supplied value before passing it through to your implementation. If the value is **WINBIO\_SUBTYPE\_NO\_INFORMATION** or **WINBIO\_SUBTYPE\_ANY**, then validate where appropriate.

 

If any of the following bits are asserted, the **WINBIO\_BIR\_HEADER** structure is not correctly formed.


```C++
#define WINBIO_BIR_FIELD_NEVER_VALID    (WINBIO_BIR_FIELD_SUBHEAD_COUNT |   \
                                         WINBIO_BIR_FIELD_PATRON_ID |       \
                                         WINBIO_BIR_FIELD_INDEX |           \
                                         WINBIO_BIR_FIELD_CHALLENGE |       \
                                         WINBIO_BIR_FIELD_PAYLOAD )
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                                       |
| Header<br/>                   | <dl> <dt>Winbio\_types.h (include Winbio.h)</dt> </dl> |



## See also

<dl> <dt>

[Client Application Structures](client-application-structures.md)
</dt> <dt>

[**WINBIO\_BIOMETRIC\_SUBTYPE Constants**](winbio-biometric-subtype-constants.md)
</dt> <dt>

[**WINBIO\_BIR**](winbio-bir.md)
</dt> <dt>

[**WINBIO\_BIR\_DATA\_FLAGS Constants**](winbio-bir-data-flags-constants.md)
</dt> <dt>

[**WINBIO\_BIR\_FIELD Constants**](winbio-bir-field-constants.md)
</dt> <dt>

[**WINBIO\_BIR\_PURPOSE Constants**](winbio-bir-purpose-constants.md)
</dt> <dt>

[**WINBIO\_BIR\_QUALITY Constants**](winbio-bir-quality-constants.md)
</dt> <dt>

[**WINBIO\_BIR\_VERSION Constants**](winbio-bir-version-constants.md)
</dt> </dl>

 

 





