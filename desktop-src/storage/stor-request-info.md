---
title: \_STOR\_REQUEST\_INFO\_V1 structure
description: The \_STOR\_REQUEST\_INFO\_V1 structure contains details about the storage driver IO request associated with a SCSI request block (SRB). \_STOR\_REQUEST\_INFO\_V1 is returned by the StorPortGetRequestInfo routine.
ms.assetid: 'CCC429B7-88BB-4DC3-86BC-6A5FCD405A5D'
keywords: ["_STOR_REQUEST_INFO_V1 structure Storage Devices", "STOR_REQUEST_INFO_V1 structure Storage Devices", "PSTOR_REQUEST_INFO_V1 structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- STOR_REQUEST_INFO_V1
api_location:
- Storport.h
api_type:
- HeaderDef
---

# \_STOR\_REQUEST\_INFO\_V1 structure

The **\_STOR\_REQUEST\_INFO\_V1** structure contains details about the storage driver IO request associated with a SCSI request block (SRB). **\_STOR\_REQUEST\_INFO\_V1** is returned by the [**StorPortGetRequestInfo**](storportgetrequestinfo.md) routine.

## Syntax


```C++
typedef struct _STOR_REQUEST_INFO_V1 {
  USHORT                Version;
  USHORT                Size;
  STOR_IO_PRIORITY_HINT PriorityHint;
  ULONG                 Flags;
  ULONG                 Key;
  ULONG                 Length;
  BOOLEAN               IsWriteRequest;
  UCHAR                 Reserved[3];
} STOR_REQUEST_INFO_V1, *PSTOR_REQUEST_INFO_V1;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

The version of this structure. Set this member to **STOR\_REQUEST\_INFO\_VER\_1**.

</dd> <dt>

**Size**
</dt> <dd>

The size of this structure. Set this value to **sizeof**(STOR\_REQUEST\_INFO).

</dd> <dt>

**PriorityHint**
</dt> <dd>

The priority hint set for the IO request.



| Value                                                                                                                                                                                                                                                                                   | Meaning                       |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|
| <span id="StorIoPriorityVeryLow"></span><span id="storiopriorityverylow"></span><span id="STORIOPRIORITYVERYLOW"></span><dl> <dt>**StorIoPriorityVeryLow**</dt> <dt>0</dt> </dl>     | Very low priority.<br/> |
| <span id="StorIoPriorityLow"></span><span id="storioprioritylow"></span><span id="STORIOPRIORITYLOW"></span><dl> <dt>**StorIoPriorityLow**</dt> <dt>1</dt> </dl>                     | Low priority.<br/>      |
| <span id="StorIoPriorityNormal"></span><span id="storioprioritynormal"></span><span id="STORIOPRIORITYNORMAL"></span><dl> <dt>**StorIoPriorityNormal**</dt> <dt>2</dt> </dl>         | Normal priority.<br/>   |
| <span id="StorIoPriorityHigh"></span><span id="storiopriorityhigh"></span><span id="STORIOPRIORITYHIGH"></span><dl> <dt>**StorIoPriorityHigh**</dt> <dt>3</dt> </dl>                 | High priority.<br/>     |
| <span id="StorIoPriorityCritical"></span><span id="storioprioritycritical"></span><span id="STORIOPRIORITYCRITICAL"></span><dl> <dt>**StorIoPriorityCritical**</dt> <dt>4</dt> </dl> | Critical priority.<br/> |



 

</dd> <dt>

**Flags**
</dt> <dd>

Flags set for handling the request. May be a combination of these values:



| Value                                                                                                                                                                                                                  | Meaning                                                      |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| <span id="REQUEST_INFO_NO_CACHE_FLAG"></span><span id="request_info_no_cache_flag"></span><dl> <dt>**REQUEST\_INFO\_NO\_CACHE\_FLAG**</dt> </dl>                | Non-cached writes are specified for this request.<br/> |
| <span id="REQUEST_INFO_PAGING_IO_FLAG"></span><span id="request_info_paging_io_flag"></span><dl> <dt>**REQUEST\_INFO\_PAGING\_IO\_FLAG**</dt> </dl>             | Paging IO is specified for this request.<br/>          |
| <span id="REQUEST_INFO_SEQUENTIAL_IO_FLAG"></span><span id="request_info_sequential_io_flag"></span><dl> <dt>**REQUEST\_INFO\_SEQUENTIAL\_IO\_FLAG**</dt> </dl> | Reads or writes are sequential.<br/>                   |
| <span id="REQUEST_INFO_TEMPORARY_FLAG"></span><span id="request_info_temporary_flag"></span><dl> <dt>**REQUEST\_INFO\_TEMPORARY\_FLAG**</dt> </dl>              | The file for this request is temporary.<br/>           |
| <span id="REQUEST_INFO_WRITE_THROUGH_FLAG"></span><span id="request_info_write_through_flag"></span><dl> <dt>**REQUEST\_INFO\_WRITE\_THROUGH\_FLAG**</dt> </dl> | No system buffering for the request.<br/>              |



 

</dd> <dt>

**Key**
</dt> <dd>

The read or write key for the request.

</dd> <dt>

**Length**
</dt> <dd>

The length of the data in this request.

</dd> <dt>

**IsWriteRequest**
</dt> <dd>

True if this is a write request. Otherwise, false, if this is a read request.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved.

</dd> </dl>

## Remarks

The caller to [**StorPortGetRequestInfo**](storportgetrequestinfo.md) allocates the **STOR\_REQUEST\_INFO** structure. Prior to calling **StorPortGetRequestInfo**, **Version** must be set to **STOR\_REQUEST\_INFO\_VER\_1** and **Size** must be set to **sizeof**(STOR\_REQUEST\_INFO). Otherwise, **StorPortGetRequestInfo** will return with a status of **STOR\_STATUS\_INVALID\_PARAMETER**.

## Requirements



|                    |                                                                                                            |
|--------------------|------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available in Windows 8 and later versions of Windows.<br/>                                           |
| Header<br/>  | <dl> <dt>Storport.h (include Storport.h)</dt> </dl> |



## See also

<dl> <dt>

[**StorPortGetRequestInfo**](storportgetrequestinfo.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20_STOR_REQUEST_INFO_V1%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






