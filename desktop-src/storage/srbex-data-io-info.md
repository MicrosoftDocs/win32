---
title: SRBEX\_DATA\_IO\_INFO structure
description: The SRBEX\_DATA\_IO\_INFO structure contains additional information related to a read or write request in an extended SRB.
ms.assetid: D4B99D6F-0A0C-49CE-A8E2-19C1A835EDA6
keywords:
- SRBEX_DATA_IO_INFO structure Storage Devices
- PSRBEX_DATA_IO_INFO structure pointer Storage Devices
topic_type:
- apiref
api_name:
- SRBEX_DATA_IO_INFO
api_location:
- Storport.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# SRBEX\_DATA\_IO\_INFO structure

The **SRBEX\_DATA\_IO\_INFO** structure contains additional information related to a read or write request in an extended SRB.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
typedef struct _SRBEX_DATA_IO_INFO {
  SRBEXDATATYPE Type;
  ULONG         Length;
  ULONG         Flags;
  ULONG         Key;
  ULONG         RWLength;
  BOOLEAN       IsWriteRequest;
  UCHAR         CachePriority;
  UCHAR         Reserved[2];
  ULONG         Reserved1[3];
} SRBEX_DATA_IO_INFO, *PSRBEX_DATA_IO_INFO;
```



## Members

<dl> <dt>

**Type**
</dt> <dd>

Data type indicator for the bidirectional extended SRB data structure. Set to **SrbExDataTypeIoInfo**.

</dd> <dt>

**Length**
</dt> <dd>

Length of the data in this structure, in bytes, starting with the **Flags** member. Set to SRBEX\_DATA\_IO\_INFO\_LENGTH.

</dd> <dt>

**Flags**
</dt> <dd>

Flags set for handling the request. May be a combination of these values:



| Value                                                                                                                                                                                                                                        | Meaning                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| <span id="REQUEST_INFO_NO_CACHE_FLAG"></span><span id="request_info_no_cache_flag"></span><dl> <dt>**REQUEST\_INFO\_NO\_CACHE\_FLAG**</dt> </dl>                                      | Non-cached writes are specified for this request.<br/>                                                                          |
| <span id="REQUEST_INFO_PAGING_IO_FLAG"></span><span id="request_info_paging_io_flag"></span><dl> <dt>**REQUEST\_INFO\_PAGING\_IO\_FLAG**</dt> </dl>                                   | Paging IO is specified for this request.<br/>                                                                                   |
| <span id="REQUEST_INFO_SEQUENTIAL_IO_FLAG"></span><span id="request_info_sequential_io_flag"></span><dl> <dt>**REQUEST\_INFO\_SEQUENTIAL\_IO\_FLAG**</dt> </dl>                       | Reads or writes are sequential.<br/>                                                                                            |
| <span id="REQUEST_INFO_TEMPORARY_FLAG"></span><span id="request_info_temporary_flag"></span><dl> <dt>**REQUEST\_INFO\_TEMPORARY\_FLAG**</dt> </dl>                                    | The file for this request is temporary.<br/>                                                                                    |
| <span id="REQUEST_INFO_WRITE_THROUGH_FLAG"></span><span id="request_info_write_through_flag"></span><dl> <dt>**REQUEST\_INFO\_WRITE\_THROUGH\_FLAG**</dt> </dl>                       | No system buffering for the request.<br/>                                                                                       |
| <span id="REQUEST_INFO_HYBRID_WRITE_THROUGH_FLAG"></span><span id="request_info_hybrid_write_through_flag"></span><dl> <dt>**REQUEST\_INFO\_HYBRID\_WRITE\_THROUGH\_FLAG**</dt> </dl> | Perform a hybrid cache write through to disk<br/> This flag is available starting with Windows 8.1 Update.<br/>           |
| <span id="REQUEST_INFO_VALID_CACHEPRIORITY_FLAG"></span><span id="request_info_valid_cachepriority_flag"></span><dl> <dt>**REQUEST\_INFO\_VALID\_CACHEPRIORITY\_FLAG**</dt> </dl>     | The hybrid cache priority level is valid for this I/O.<br/> This flag is available starting with Windows 8.1 Update.<br/> |



 

</dd> <dt>

**Key**
</dt> <dd>

A tag value to identify a block of data transferred.

</dd> <dt>

**RWLength**
</dt> <dd>

The length, in bytes of the data to transfer.

</dd> <dt>

**IsWriteRequest**
</dt> <dd>

TRUE if the I/O operation in the SRB is a write request. Otherwise, FALSE; the I/O operation is a read request.

</dd> <dt>

**CachePriority**
</dt> <dd>

Priority level for a hybrid cache read or write.

This member is valid starting with Windows 8.1 Update.

</dd> <dt>

**Reserved**
</dt> <dd>

This member is reserved. Set to 0.

</dd> <dt>

**Reserved1**
</dt> <dd>

This member is reserved. Set to 0.

This member is present starting with Windows 8.1 Update.

</dd> </dl>

## Requirements



|                    |                                                                                                                                  |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 8.<br/>                                                                                    |
| Header<br/>  | <dl> <dt>Storport.h (include Storport.h, Srb.h, or Minitape.h)</dt> </dl> |



## See also

<dl> <dt>

[**STORAGE\_REQUEST\_BLOCK**](storage-request-block.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SRBEX_DATA_IO_INFO%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






