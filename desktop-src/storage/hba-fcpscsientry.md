---
title: HBA\_FcpScsiEntry structure
description: The HBA\_FcpScsiEntry structure defines a mapping between an operating system identifier for a logical unit and the corresponding fibre channel protocol (FCP) identifier for the logical unit.
ms.assetid: '19e40a1b-fcbf-4510-a7c0-aa9a61f2f651'
keywords: ["HBA_FcpScsiEntry structure Storage Devices", "HBA_FCPSCSIENTRY structure Storage Devices", "PHBA_FCPSCSIENTRY structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- HBA_FCPSCSIENTRY
api_location:
- hbaapi.h
api_type:
- HeaderDef
---

# HBA\_FcpScsiEntry structure

The HBA\_FcpScsiEntry structure defines a mapping between an operating system identifier for a logical unit and the corresponding fibre channel protocol (FCP) identifier for the logical unit.

## Syntax


```C++
typedef struct HBA_FcpScsiEntry {
  HBA_SCSIID ScsiId;
  HBA_FCPID  FcpId;
} HBA_FCPSCSIENTRY, *PHBA_FCPSCSIENTRY;
```



## Members

<dl> <dt>

**ScsiId**
</dt> <dd>

Contains a structure of type [**HBA\_ScsiId**](hba-scsiid.md) that holds information that the operating system uses to identify a SCSI device.

</dd> <dt>

**FcpId**
</dt> <dd>

Contains a structure of type [HBA\_FcpId](hba-fcpid.md) that uniquely identifies the device anywhere on the fibre channel network.

</dd> </dl>

## Requirements



|                   |                                                                                                        |
|-------------------|--------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbaapi.h (include Hbaapi.h)</dt> </dl> |



## See also

<dl> <dt>

[HBA\_FcpId](hba-fcpid.md)
</dt> <dt>

[**HBA\_ScsiId**](hba-scsiid.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HBA_FcpScsiEntry%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






