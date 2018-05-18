---
title: STORAGE\_DIAGNOSTIC\_MP\_REQUEST structure
description: Describes a diagnostic request to Miniport. The STORAGE\_DIAGNOSTIC\_MP\_REQUEST structure is provided in the input/output buffer of an IOCTL\_SCSI\_MINIPORT\_DIAGNOSTIC request.
ms.assetid: '1F2B15A6-7C05-4FBA-B54F-EEF013FF5739'
keywords: ["STORAGE_DIAGNOSTIC_MP_REQUEST structure Storage Devices", "PSTORAGE_DIAGNOSTIC_MP_REQUEST structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- STORAGE_DIAGNOSTIC_MP_REQUEST
api_location:
- ntddscsi.h
api_type:
- HeaderDef
---

# STORAGE\_DIAGNOSTIC\_MP\_REQUEST structure

Describes a diagnostic request to Miniport. The **STORAGE\_DIAGNOSTIC\_MP\_REQUEST** structure is provided in the input/output buffer of an [**IOCTL\_SCSI\_MINIPORT\_DIAGNOSTIC**](ioctl-scsi-miniport-diagnostic.md) request.

## Syntax


```C++
typedef struct _STORAGE_DIAGNOSTIC_MP_REQUEST {
  ULONG                           Version;
  ULONG                           Size;
   STORAGE_DIAGNOSTIC_TARGET_TYPE TargetType;
  STORAGE_DIAGNOSTIC_LEVEL        Level;
  GUID                            ProviderId;
  ULONG                           BufferSize;
  ULONG                           Reserved;
   _Field_size_(BufferSize) UCHAR DataBuffer[ANYSIZE_ARRAY];
} STORAGE_DIAGNOSTIC_MP_REQUEST, *PSTORAGE_DIAGNOSTIC_MP_REQUEST;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

Version of this structure.

</dd> <dt>

**Size**
</dt> <dd>

Specifies the whole size of the structure and the associated data buffer.

</dd> <dt>

**TargetType**
</dt> <dd>

Specifies the request target type. See definitions for [**STORAGE\_DIAGNOSTIC\_TARGET\_TYPE**](storage-diagnostic-target-type.md).

</dd> <dt>

**Level**
</dt> <dd>

Specifies the Diagnostic level. See definitions for [**STORAGE\_DIAGNOSTIC\_LEVEL**](storage-diagnostic-level.md).

</dd> <dt>

**ProviderId**
</dt> <dd>

Specifies the GUID of the diagnostic data provider.

</dd> <dt>

**BufferSize**
</dt> <dd>

Specifies the Data buffer size. As an input buffer, *BufferSize* should be set to number of bytes allocated for the *DataBuffer*. If the request is failed because of buffer too short, *BufferSize* should be set to the length required for *DataBuffer* by the diagnostic data provider; If the request is successful, it should be filled with returned data size of *DataBuffer*. For other cases, it should be cleared to 0.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved for future use.

</dd> <dt>

**DataBuffer**
</dt> <dd>

Specifies the Diagnostic data buffer.

</dd> </dl>

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 10, version 1709.<br/>                          |
| Header<br/>  | <dl> <dt>Ntddscsi.h</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_SCSI\_MINIPORT\_DIAGNOSTIC**](ioctl-scsi-miniport-diagnostic.md)
</dt> <dt>

[**STORAGE\_DIAGNOSTIC\_DATA**](storage-diagnostic-data.md)
</dt> <dt>

[**STORAGE\_DIAGNOSTIC\_LEVEL**](storage-diagnostic-level.md)
</dt> <dt>

[**STORAGE\_DIAGNOSTIC\_TARGET\_TYPE**](storage-diagnostic-target-type.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_DIAGNOSTIC_MP_REQUEST%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






