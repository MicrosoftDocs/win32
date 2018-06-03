---
title: STORAGE\_OFFLOAD\_WRITE\_OUTPUT structure
description: The STORAGE\_OFFLOAD\_WRITE\_OUTPUT structure is the output of an IOCTL\_STORAGE\_MANAGE\_DATA\_SET\_ATTRIBUTES control code request when the Action member of DEVICE\_MANAGE\_DATA\_SET\_ATTRIBUTES is set to DeviceDsmAction\_OffloadWrite.
ms.assetid: 95EF1722-5171-4A09-8676-7910E53E3868
keywords:
- STORAGE_OFFLOAD_WRITE_OUTPUT structure Storage Devices
- PSTORAGE_OFFLOAD_WRITE_OUTPUT structure pointer Storage Devices
topic_type:
- apiref
api_name:
- STORAGE_OFFLOAD_WRITE_OUTPUT
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

# STORAGE\_OFFLOAD\_WRITE\_OUTPUT structure

The **STORAGE\_OFFLOAD\_WRITE\_OUTPUT** structure is the output of an [**IOCTL\_STORAGE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](ioctl-storage-manage-data-set-attributes.md) control code request when the **Action** member of [**DEVICE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](device-manage-data-set-attributes.md) is set to **DeviceDsmAction\_OffloadWrite**.

On input, a token value in [**DEVICE\_DSM\_OFFLOAD\_WRITE\_PARAMETERS**](device-dsm-offload-write-parameters.md) uniquely identifies the data set ranges requested for writing in the [**DEVICE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](device-manage-data-set-attributes.md) structure. The **STORAGE\_OFFLOAD\_WRITE\_OUTPUT** structure contains the results of the write operation.

## Syntax


```C++
typedef struct _STORAGE_OFFLOAD_WRITE_OUTPUT {
  ULONG     OffloadWriteFlags;
  ULONG     Reserved;
  ULONGLONG LengthCopied;
} STORAGE_OFFLOAD_WRITE_OUTPUT, *PSTORAGE_OFFLOAD_WRITE_OUTPUT;
```



## Members

<dl> <dt>

**OffloadWriteFlags**
</dt> <dd>

Flags indicating the result of the offload write operation. This is set to one of the following.



| Value                                                                                                                                                                                                                                    | Meaning                                                                         |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| <span id="STORAGE_OFFLOAD_WRITE_RANGE_TRUNCATED"></span><span id="storage_offload_write_range_truncated"></span><dl> <dt>**STORAGE\_OFFLOAD\_WRITE\_RANGE\_TRUNCATED**</dt> </dl> | The offload write was performed but the range written was truncated.<br/> |
| <span id="STORAGE_OFFLOAD_TOKEN_INVALID_________"></span><span id="storage_offload_token_invalid_________"></span><dl> <dt>**STORAGE\_OFFLOAD\_TOKEN\_INVALID** </dt> </dl>       | The token provided for the offload write operation was invalid.<br/>      |



 

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved.

</dd> <dt>

**LengthCopied**
</dt> <dd>

Bytes copied for the write request in [**DEVICE\_DSM\_OFFLOAD\_WRITE\_PARAMETERS**](device-dsm-offload-write-parameters.md).

</dd> </dl>

## Remarks

The **STORAGE\_OFFLOAD\_WRITE\_OUTPUT** structure is returned at the beginning of the system buffer.

## Requirements



|                    |                                                                                                            |
|--------------------|------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available in Windows 8 and later versions of Windows.<br/>                                           |
| Header<br/>  | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**DEVICE\_DSM\_OFFLOAD\_WRITE\_PARAMETERS**](device-dsm-offload-write-parameters.md)
</dt> <dt>

[**DEVICE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](device-manage-data-set-attributes.md)
</dt> <dt>

[**IOCTL\_STORAGE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](ioctl-storage-manage-data-set-attributes.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_OFFLOAD_WRITE_OUTPUT%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






