---
title: SRBEX\_DATA\_BIDIRECTIONAL structure
description: The SRBEX\_DATA\_BIDIRECTIONAL structure contains the extended SRB data for bi-directional transfer commands.
ms.assetid: 'B61247DC-8AC3-4A96-985B-A4CAC232555E'
keywords: ["SRBEX_DATA_BIDIRECTIONAL structure Storage Devices", "PSRBEX_DATA_BIDIRECTIONAL structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- SRBEX_DATA_BIDIRECTIONAL
api_location:
- Storport.h
api_type:
- HeaderDef
---

# SRBEX\_DATA\_BIDIRECTIONAL structure

The **SRBEX\_DATA\_BIDIRECTIONAL** structure contains the extended SRB data for bi-directional transfer commands.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
typedef struct _SRBEX_DATA_BIDIRECTIONAL {
  SRBEXDATATYPE       Type;
  ULONG               Length;
  ULONG               DataInTransferLength;
  ULONG               Reserved1;
  PVOID POINTER_ALIGN DataInBuffer;
} SRBEX_DATA_BIDIRECTIONAL, *PSRBEX_DATA_BIDIRECTIONAL;
```



## Members

<dl> <dt>

**Type**
</dt> <dd>

Data type indicator for the bidirectional extended SRB data structure. Set to **SrbExDataTypeBidirectional**.

</dd> <dt>

**Length**
</dt> <dd>

Length of the data in this structure, in bytes, starting with the **DataInTransferLength** member. Set to SRBEX\_DATA\_BIDIRECTIONAL\_LENGTH.

</dd> <dt>

**DataInTransferLength**
</dt> <dd>

Length of the data present in the **DataInBuffer** member.

</dd> <dt>

**Reserved1**
</dt> <dd>

This member is reserved. Set to 0.

</dd> <dt>

**DataInBuffer**
</dt> <dd>

A pointer to the buffer that contains the data sent from the device.

</dd> </dl>

## Requirements



|                    |                                                                                                                                  |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 8.<br/>                                                                                    |
| Header<br/>  | <dl> <dt>Storport.h (include Storport.h, Srb.h, or Minitape.h)</dt> </dl> |



## See also

<dl> <dt>

[**STORAGE\_REQUEST\_BLOCK**](storage-request-block.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SRBEX_DATA_BIDIRECTIONAL%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






