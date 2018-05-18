---
title: HBA\_LUID structure
description: The HBA\_LUID structure contains the identification descriptor from the device identification page of the vital products data returned by a SCSI INQUIRY command.
ms.assetid: 'af272e27-6cb4-4f87-9c46-512ac80fa310'
keywords: ["HBA_LUID structure Storage Devices", "PHBA_LUID structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- HBA_LUID
api_location:
- hbaapi.h
api_type:
- HeaderDef
---

# HBA\_LUID structure

The HBA\_LUID structure contains the identification descriptor from the device identification page of the vital products data returned by a SCSI INQUIRY command.

## Syntax


```C++
typedef struct HBA_LUID {
  char buffer[256];
} HBA_LUID, *PHBA_LUID;
```



## Members

<dl> <dt>

**buffer**
</dt> <dd>

Contains a buffer that holds the identification descriptor.

</dd> </dl>

## Remarks

A vendor specific LUID is not guaranteed to be unique or persistent.

## Requirements



|                   |                                                                                                        |
|-------------------|--------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbaapi.h (include Hbaapi.h)</dt> </dl> |



## See also

<dl> <dt>

[**HBA\_FCPBindingEntry2**](hba-fcpbindingentry2.md)
</dt> <dt>

[**HBA\_FcpScsiEntryV2**](hba-fcpscsientryv2.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HBA_LUID%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






