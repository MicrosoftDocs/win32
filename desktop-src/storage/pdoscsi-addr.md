---
title: PDOSCSI\_ADDR structure
description: The PDOSCSI\_ADDR structure is used to represent a SCSI address.
ms.assetid: ad31cff9-06bd-4c3a-b1e1-5a82cc6b48a2
keywords:
- PDOSCSI_ADDR structure Storage Devices
- PPDOSCSI_ADDR structure pointer Storage Devices
topic_type:
- apiref
api_name:
- PDOSCSI_ADDR
api_location:
- mpiodisk.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# PDOSCSI\_ADDR structure

The PDOSCSI\_ADDR structure is used to represent a SCSI address.

## Syntax


```C++
typedef struct _PDOSCSI_ADDR {
  UCHAR PortNumber;
  UCHAR ScsiPathId;
  UCHAR TargetId;
  UCHAR Lun;
} PDOSCSI_ADDR, *PPDOSCSI_ADDR;
```



## Members

<dl> <dt>

**PortNumber**
</dt> <dd>

An unsigned 8-bitfield that represents the PortNumber as defined by the SCSI\_ADDRESS structure in *Ntddscsi.h*.

</dd> <dt>

**ScsiPathId**
</dt> <dd>

An unsigned 8-bitfield that represents the PathId as defined by the SCSI\_ADDRESS structure in *Ntddscsi.h*.

</dd> <dt>

**TargetId**
</dt> <dd>

An unsigned 8-bitfield that represents the TargetId as defined by the SCSI\_ADDRESS structure in *Ntddscsi.h*.

</dd> <dt>

**Lun**
</dt> <dd>

An unsigned 8-bitfield that represents the Lun as defined by the SCSI\_ADDRESS structure in *Ntddscsi.h*.

</dd> </dl>

## Requirements



|                   |                                                                                                           |
|-------------------|-----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mpiodisk.h (include Mpiowmi.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20PDOSCSI_ADDR%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





