---
title: SRBEX\_DATA\_POWER structure
description: The SRBEX\_DATA\_POWER structure contains the request data for an extended power SRB.
ms.assetid: '61F5C316-5214-45A6-B4BA-DEE6A224E811'
keywords: ["SRBEX_DATA_POWER structure Storage Devices", "PSRBEX_DATA_POWER structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- SRBEX_DATA_POWER
api_location:
- Storport.h
api_type:
- HeaderDef
---

# SRBEX\_DATA\_POWER structure

The **SRBEX\_DATA\_POWER** structure contains the request data for an extended power SRB.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
typedef struct _SRBEX_DATA_POWER {
  SRBEXDATATYPE           Type;
  ULONG                   Length;
  ULONG                   SrbPowerFlags;
  UCHAR                   Reserved[3];
  STOR_DEVICE_POWER_STATE DevicePowerState;
  STOR_POWER_ACTION       PowerAction;
} SRBEX_DATA_POWER, *PSRBEX_DATA_POWER;
```



## Members

<dl> <dt>

**Type**
</dt> <dd>

Data type indicator for the bidirectional extended SRB data structure. Set to **SrbExDataTypePower**.

</dd> <dt>

**Length**
</dt> <dd>

Length of the data in this structure starting with the **SrbPowerFlags** member. Set to SRBEX\_DATA\_POWER\_LENGTH.

</dd> <dt>

**SrbPowerFlags**
</dt> <dd>

Indicates that the power request is for the adapter if SRB\_POWER\_FLAGS\_ADAPTER\_REQUEST is set and that storage device address is reserved. Otherwise, *SrbPowerFlags* will be **NULL**, indicating that the request is for the storage device specified by an address at **AddressOffset** in the [**STORAGE\_REQUEST\_BLOCK**](storage-request-block.md) structure.

</dd> <dt>

**Reserved**
</dt> <dd>

This member is reserved. Set to 0.

</dd> <dt>

**DevicePowerState**
</dt> <dd>

An enumerator value of type [**STOR\_DEVICE\_POWER\_STATE**](stor-device-power-state.md) that specifies the requested power state of the device.

</dd> <dt>

**PowerAction**
</dt> <dd>

An enumerator value of type [**STOR\_POWER\_ACTION**](stor-power-action.md) that specifies the type of system shutdown that is about to occur. This value is meaningful only if the device is moving into the D1, D2, or D3 power state as indicated by the **DevicePowerState** member.

</dd> </dl>

## Requirements



|                    |                                                                                                                                  |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 8.<br/>                                                                                    |
| Header<br/>  | <dl> <dt>Storport.h (include Storport.h, Srb.h, or Minitape.h)</dt> </dl> |



## See also

<dl> <dt>

[**STOR\_DEVICE\_POWER\_STATE**](stor-device-power-state.md)
</dt> <dt>

[**STOR\_POWER\_ACTION**](stor-power-action.md)
</dt> <dt>

[**STORAGE\_REQUEST\_BLOCK**](storage-request-block.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SRBEX_DATA_POWER%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






