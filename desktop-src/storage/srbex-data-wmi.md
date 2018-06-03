---
title: SRBEX\_DATA\_WMI structure
description: The SRBEX\_DATA\_WMI structure contains the request data for an extended WMI SRB.
ms.assetid: 3FFBF258-50C3-4D2D-AFC8-184D2FF85EE4
keywords:
- SRBEX_DATA_WMI structure Storage Devices
- PSRBEX_DATA_WMI structure pointer Storage Devices
topic_type:
- apiref
api_name:
- SRBEX_DATA_WMI
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

# SRBEX\_DATA\_WMI structure

The **SRBEX\_DATA\_WMI** structure contains the request data for an extended WMI SRB.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
typedef struct _SRBEX_DATA_WMI {
  SRBEXDATATYPE       Type;
  ULONG               Length;
  UCHAR               WMISubFunction;
  UCHAR               WMIFlags;
  UCHAR               Reserved[2];
  ULONG               Reserved1;
  PVOID POINTER_ALIGN DataPath;
} SRBEX_DATA_WMI, *PSRBEX_DATA_WMI;
```



## Members

<dl> <dt>

**Type**
</dt> <dd>

Data type indicator for the bidirectional extended SRB data structure. Set to **SrbExDataTypeWmi**.

</dd> <dt>

**Length**
</dt> <dd>

Length of the data in this structure starting with the **WMISubFunction** member. Set to SRBEX\_DATA\_WMI\_LENGTH.

</dd> <dt>

**WMISubFunction**
</dt> <dd>

Indicates the WMI action to be performed. The subfunction value corresponds to the WMI minor IRP number that identifies the WMI operation.

</dd> <dt>

**WMIFlags**
</dt> <dd>

Indicates that the WMI request is for the adapter if SRB\_WMI\_FLAGS\_ADAPTER\_REQUEST is set and that storage device address is reserved. Otherwise, *WMIFlags* will be **NULL**, indicating that the request is for the storage device specified by an address at **AddressOffset** in the [**STORAGE\_REQUEST\_BLOCK**](storage-request-block.md) structure.

</dd> <dt>

**Reserved**
</dt> <dd>

This member is reserved. Contains zeros.

</dd> <dt>

**Reserved1**
</dt> <dd>

This member is reserved. Set to 0.

</dd> <dt>

**DataPath**
</dt> <dd>

Specifies the WMI data path for this request.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SRBEX_DATA_WMI%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






