---
title: CDROM\_EXCLUSIVE\_ACCESS structure
description: The CDROM\_EXCLUSIVE\_ACCESS structure is used with the IOCTL\_CDROM\_EXCLUSIVE\_ACCESS request to query the access state of a CD-ROM device or to lock or unlock the device for exclusive access.
ms.assetid: '95248a4a-1fc1-4985-baff-2fe77532d398'
keywords: ["CDROM_EXCLUSIVE_ACCESS structure Storage Devices", "PCDROM_EXCLUSIVE_ACCESS structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- CDROM_EXCLUSIVE_ACCESS
api_location:
- ntddcdrm.h
api_type:
- HeaderDef
---

# CDROM\_EXCLUSIVE\_ACCESS structure

The CDROM\_EXCLUSIVE\_ACCESS structure is used with the [**IOCTL\_CDROM\_EXCLUSIVE\_ACCESS**](ioctl-cdrom-exclusive-access.md) request to query the access state of a CD-ROM device or to lock or unlock the device for exclusive access.

## Syntax


```C++
typedef struct _CDROM_EXCLUSIVE_ACCESS {
  EXCLUSIVE_ACCESS_REQUEST_TYPE RequestType;
  ULONG                         Flags;
} CDROM_EXCLUSIVE_ACCESS, *PCDROM_EXCLUSIVE_ACCESS;
```



## Members

<dl> <dt>

**RequestType**
</dt> <dd>

An [**EXCLUSIVE\_ACCESS\_REQUEST\_TYPE**](exclusive-access-request-type.md)-typed enumeration value that specifies the type of operation.

</dd> <dt>

**Flags**
</dt> <dd>

A flag that specifies the characteristics of the operation. The meaning of the flag depends on the type of operation that **RequestType** specifies. The following table describes the possible values for **RequestType** and **Flags**:



<table>
<thead>
<tr class="header">
<th>RequestType</th>
<th>Flags</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>ExclusiveAccessQueryState</strong><br/></td>
<td>Not applicable<br/></td>
<td>Not applicable<br/></td>
</tr>
<tr class="even">
<td rowspan="2"> <strong>ExclusiveAccessLockDevice</strong><br/> ${REMOVE}$<br />
</td>
<td>0<br/></td>
<td>Requires that the caller dismount the file system<br/></td>
</tr>
<tr class="odd">
<td>CDROM_LOCK_IGNORE_VOLUME<br/></td>
<td>Ignores the file system mount and locks the device<br/></td>

</tr>
<tr class="even">
<td><strong>ExclusiveAccessUnlockDevice</strong><br/></td>
<td>CDROM_NO_MEDIA_NOTIFICATIONS<br/></td>
<td>Prevents the sending of a media removal notification and a media arrival notification on an exclusive access unlock<br/></td>
</tr>
</tbody>
</table>



 

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdrm.h (include Ntddcdrm.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_CDROM\_EXCLUSIVE\_ACCESS**](ioctl-cdrom-exclusive-access.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20CDROM_EXCLUSIVE_ACCESS%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






