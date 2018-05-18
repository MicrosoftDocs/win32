---
title: STORAGE\_DIAGNOSTIC\_REQUEST structure
description: Describes a diagnostic request about the storage driver stack. The STORAGE\_DIAGNOSTIC\_REQUEST structure is provided in the input buffer of an IOCTL\_STORAGE\_DIAGNOSTIC request.
ms.assetid: 'BAC83B5C-4F14-430D-9CEF-46812FC4DFED'
keywords: ["STORAGE_DIAGNOSTIC_REQUEST structure Storage Devices", "PSTORAGE_DIAGNOSTIC_REQUEST structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- STORAGE_DIAGNOSTIC_REQUEST
api_location:
- ntddstor.h
api_type:
- HeaderDef
---

# STORAGE\_DIAGNOSTIC\_REQUEST structure

Describes a diagnostic request about the storage driver stack. The **STORAGE\_DIAGNOSTIC\_REQUEST** structure is provided in the input buffer of an [**IOCTL\_STORAGE\_DIAGNOSTIC**](storage-ioctl_storage_diagnostic) request.

## Syntax


```C++
typedef struct _STORAGE_DIAGNOSTIC_REQUEST {
  ULONG                           Version;
  ULONG                           Size;
  ULONG                           Reserved;
   STORAGE_DIAGNOSTIC_TARGET_TYPE TargetType;
  STORAGE_DIAGNOSTIC_LEVEL        Level;
} STORAGE_DIAGNOSTIC_REQUEST, *PSTORAGE_DIAGNOSTIC_REQUEST;
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

**Reserved**
</dt> <dd>

Reserved for future use.

</dd> <dt>

**TargetType**
</dt> <dd>

Specifies the request target type. See definitions for [**STORAGE\_DIAGNOSTIC\_TARGET\_TYPE**](storage-diagnostic-target-type.md).

</dd> <dt>

**Level**
</dt> <dd>

Specifies the Diagnostic level. See definitions for [**STORAGE\_DIAGNOSTIC\_LEVEL**](storage-diagnostic-level.md).

</dd> </dl>

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 10, version 1709.<br/>                          |
| Header<br/>  | <dl> <dt>Ntddstor.h</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_STORAGE\_DIAGNOSTIC**](storage-ioctl_storage_diagnostic)
</dt> <dt>

[**STORAGE\_DIAGNOSTIC\_DATA**](storage-diagnostic-data.md)
</dt> <dt>

[**STORAGE\_DIAGNOSTIC\_LEVEL**](storage-diagnostic-level.md)
</dt> <dt>

[**STORAGE\_DIAGNOSTIC\_TARGET\_TYPE**](storage-diagnostic-target-type.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_DIAGNOSTIC_REQUEST%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






