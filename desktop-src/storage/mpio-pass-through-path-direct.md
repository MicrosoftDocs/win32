---
title: MPIO\_PASS\_THROUGH\_PATH\_DIRECT structure
description: The MPIO\_PASS\_THROUGH\_PATH\_DIRECT structure is used together with an IOCTL\_MPIO\_PASS\_THROUGH\_PATH\_DIRECT request to instruct the port driver to send an embedded SCSI command to the target device.
ms.assetid: 'a14eb3a9-f2b6-4abc-8eaa-23bd4a87580e'
keywords: ["MPIO_PASS_THROUGH_PATH_DIRECT structure Storage Devices", "PMPIO_PASS_THROUGH_PATH_DIRECT structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- MPIO_PASS_THROUGH_PATH_DIRECT
api_location:
- ntddscsi.h
api_type:
- HeaderDef
---

# MPIO\_PASS\_THROUGH\_PATH\_DIRECT structure

The **MPIO\_PASS\_THROUGH\_PATH\_DIRECT** structure is used together with an [**IOCTL\_MPIO\_PASS\_THROUGH\_PATH\_DIRECT**](ioctl-mpio-pass-through-path-direct.md) request to instruct the port driver to send an embedded SCSI command to the target device.

## Syntax


```C++
typedef struct _MPIO_PASS_THROUGH_PATH_DIRECT {
  SCSI_PASS_THROUGH_DIRECT PassThrough;
  ULONG                    Version;
  USHORT                   Length;
  UCHAR                    Flags;
  UCHAR                    PortNumber;
  ULONGLONG                MpioPathId;
} MPIO_PASS_THROUGH_PATH_DIRECT, *PMPIO_PASS_THROUGH_PATH_DIRECT;
```



## Members

<dl> <dt>

**PassThrough**
</dt> <dd>

Contains a [**SCSI\_PASS\_THROUGH\_DIRECT**](scsi-pass-through-direct.md) structure that is set up in the same way as it is for an [**IOCTL\_SCSI\_PASS\_THROUGH\_DIRECT**](ioctl-scsi-pass-through-direct.md) request.

</dd> <dt>

**Version**
</dt> <dd>

Should be zero.

</dd> <dt>

**Length**
</dt> <dd>

The size of the **MPIO\_PASS\_THROUGH\_PATH\_DIRECT** structure.

</dd> <dt>

**Flags**
</dt> <dd> <dl> <dt>

In the following table, either the first or the second flag must be set, but not both. The third flag may or may not be set independent of the first two.
</dt> <dt>





| Flag                                           | Meaning                                                                                                                                                                                                                                                                                                                                                                   |
|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MPIO\_IOCTL\_FLAG\_USE\_PATHID<br/>      | The real LUN is specified in terms of the supplied **MpioPathId** member. Either this flag or MPIO\_IOCTL\_FLAG\_USE\_SCSIADDRESS must be set, but not both.<br/>                                                                                                                                                                                                   |
| MPIO\_IOCTL\_FLAG\_USE\_SCSIADDRESS<br/> | The real LUN is specified in terms of the supplied PortNumber member and the **PathId** and **TargetId** members of the embedded SCSI\_PASS\_THROUGH\_DIRECT structure. These values can be obtained by using a WMI request for the PDOSCSI\_ADDR that is associated with the real LUN. This flag or MPIO\_IOCTL\_FLAG\_USE\_PATHID must be set, but not both.<br/> |
| MPIO\_IOCTL\_FLAG\_INVOLVE\_DSM<br/>     | The claiming DSM should choose the real LUN.<br/>                                                                                                                                                                                                                                                                                                                   |



 


</dt> </dl> </dd> <dt>

**PortNumber**
</dt> <dd>

The port number if MPIO\_IOCTL\_FLAG\_USE\_SCSIADDRESS is set. Otherwise, this member is zero. If MPIO\_IOCTL\_FLAG\_USE\_SCSIADDRESS is set, the **PathId** and **TargetId** values are taken from the embedded [**SCSI\_PASS\_THROUGH\_DIRECT**](scsi-pass-through-direct.md) structure.

</dd> <dt>

**MpioPathId**
</dt> <dd>

The **PathId** for the real LUN. This value can be obtained by using a WMI request for the PDO\_INFORMATION that is associated with the real LUN. This value is set only if MPIO\_IOCTL\_FLAG\_USE\_PATHID is set.

</dd> </dl>

## Remarks

The **MPIO\_PASS\_THROUGH\_PATH\_DIRECT** structure is used for a single-buffered device control request. To use double-buffering, callers should use [**IOCTL\_MPIO\_PASS\_THROUGH\_PATH**](ioctl-mpio-pass-through-path.md).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddscsi.h (include Ntddscsi.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_SCSI\_PASS\_THROUGH**](ioctl-scsi-pass-through.md)
</dt> <dt>

[**IOCTL\_SCSI\_PASS\_THROUGH\_DIRECT**](ioctl-scsi-pass-through-direct.md)
</dt> <dt>

[**SCSI\_PASS\_THROUGH**](scsi-pass-through.md)
</dt> <dt>

[**IOCTL\_MPIO\_PASS\_THROUGH\_PATH**](ioctl-mpio-pass-through-path.md)
</dt> <dt>

[**IOCTL\_MPIO\_PASS\_THROUGH\_PATH\_DIRECT**](ioctl-mpio-pass-through-path-direct.md)
</dt> <dt>

[**SCSI\_REQUEST\_BLOCK**](scsi-request-block.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MPIO_PASS_THROUGH_PATH_DIRECT%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






