---
title: STORAGE\_DIAGNOSTIC\_DATA structure
description: Describes diagnostic data about the storage driver stack. The STORAGE\_DIAGNOSTIC\_DATA structure is provided in the output buffer of an IOCTL\_STORAGE\_DIAGNOSTIC request.
ms.assetid: 68BC990B-DD0C-49CD-95EC-672FD1459B39
keywords:
- STORAGE_DIAGNOSTIC_DATA structure Storage Devices
- PSTORAGE_DIAGNOSTIC_DATA structure pointer Storage Devices
topic_type:
- apiref
api_name:
- STORAGE_DIAGNOSTIC_DATA
api_location:
- ntddstor.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# STORAGE\_DIAGNOSTIC\_DATA structure

Describes diagnostic data about the storage driver stack. The **STORAGE\_DIAGNOSTIC\_DATA** structure is provided in the output buffer of an [**IOCTL\_STORAGE\_DIAGNOSTIC**](https://www.bing.com/search?q=**IOCTL\_STORAGE\_DIAGNOSTIC**) request.

## Syntax


```C++
typedef struct _STORAGE_DIAGNOSTIC_DATA {
  ULONG                          Version;
  ULONG                          Size;
  GUID                           ProviderId;
   ULONG                         BufferSize;
  ULONG                          Reserved;
  _Field_size_(BufferSize) UCHAR DiagnosticDataBuffer[ANYSIZE_ARRAY];
} STORAGE_DIAGNOSTIC_DATA, *PSTORAGE_DIAGNOSTIC_DATA;
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

**ProviderId**
</dt> <dd>

Specifies the GUID of a diagnostic data provider.

</dd> <dt>

**BufferSize**
</dt> <dd>

If the request failed because of buffer too small, this field should be filled with the required buffer size for a *DiagnosticDataBuffer* needed by provider; if the request is successful, it should be filled with returned buffer size of *DiagnosticDataBuffer*; it should be cleared to zero for other cases.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved for future use.

</dd> <dt>

**DiagnosticDataBuffer**
</dt> <dd>

Specifies the Diagnostic data buffer.

</dd> </dl>

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 10, version 1709.<br/>                          |
| Header<br/>  | <dl> <dt>Ntddstor.h</dt> </dl> |



## See also

<dl> <dt>

[**STORAGE\_DIAGNOSTIC\_REQUEST**](storage-diagnostic-request.md)
</dt> <dt>

[**IOCTL\_STORAGE\_DIAGNOSTIC**](https://www.bing.com/search?q=**IOCTL\_STORAGE\_DIAGNOSTIC**)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_DIAGNOSTIC_DATA%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






