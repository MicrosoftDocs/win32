---
title: SRBEX\_DATA\_PNP structure
description: The SRBEX\_DATA\_PNP structure contains the request data for an extended plug and play (PNP) SRB.
ms.assetid: CB64AF68-C40D-44F0-8F52-6BF05E23E5E1
keywords:
- SRBEX_DATA_PNP structure Storage Devices
- PSRBEX_DATA_PNP structure pointer Storage Devices
topic_type:
- apiref
api_name:
- SRBEX_DATA_PNP
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

# SRBEX\_DATA\_PNP structure

The **SRBEX\_DATA\_PNP** structure contains the request data for an extended plug and play (PNP) SRB.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
typedef struct _SRBEX_DATA_PNP {
  SRBEXDATATYPE   Type;
  ULONG           Length;
  UCHAR           PnPSubFunction;
  UCHAR           Reserved[3];
  STOR_PNP_ACTION PnPAction;
  ULONG           SrbPnPFlags;
  ULONG           Reserved1;
} SRBEX_DATA_PNP, *PSRBEX_DATA_PNP;
```



## Members

<dl> <dt>

**Type**
</dt> <dd>

Data type indicator for the bidirectional extended SRB data structure. Set to **SrbExDataTypePnp**.

</dd> <dt>

**Length**
</dt> <dd>

Length of the data in this structure starting with the **PnPSubFunction** member. Set to SRBEX\_DATA\_PNP\_LENGTH.

</dd> <dt>

**PnPSubFunction**
</dt> <dd>

This member is not currently used. Set to 0.

</dd> <dt>

**Reserved**
</dt> <dd>

This member is reserved. Set to 0.

</dd> <dt>

**PnPAction**
</dt> <dd>

The plug and play action to perform. This member can have one of the following values:



| Value                                                                                                                                                                                                                                                                                                                      | Meaning                                                                                     |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| <span id="StorStartDevice"></span><span id="storstartdevice"></span><span id="STORSTARTDEVICE"></span><dl> <dt>**StorStartDevice**</dt> <dt>0x00</dt> </dl>                                                             | Start the device.<br/>                                                                |
| <span id="StorRemoveDevice"></span><span id="storremovedevice"></span><span id="STORREMOVEDEVICE"></span><dl> <dt>**StorRemoveDevice**</dt> <dt>0x02</dt> </dl>                                                         | Remove the device.<br/>                                                               |
| <span id="StorStopDevice"></span><span id="storstopdevice"></span><span id="STORSTOPDEVICE"></span><dl> <dt>**StorStopDevice**</dt> <dt>0x04</dt> </dl>                                                                 | Stop the device.<br/>                                                                 |
| <span id="StorQueryCapabilities"></span><span id="storquerycapabilities"></span><span id="STORQUERYCAPABILITIES"></span><dl> <dt>**StorQueryCapabilities**</dt> <dt>0x09</dt> </dl>                                     | Query the capabilities of the device.<br/>                                            |
| <span id="StorQueryResourceRequirements"></span><span id="storqueryresourcerequirements"></span><span id="STORQUERYRESOURCEREQUIREMENTS"></span><dl> <dt>**StorQueryResourceRequirements**</dt> <dt>0x0B</dt> </dl>     | Query the resource requirements for the device.<br/>                                  |
| <span id="StorFilterResourceRequirements"></span><span id="storfilterresourcerequirements"></span><span id="STORFILTERRESOURCEREQUIREMENTS"></span><dl> <dt>**StorFilterResourceRequirements**</dt> <dt>0x0D</dt> </dl> | Filter the resource requirements for the device. <br/>                                |
| <span id="StorSupriseRemoval"></span><span id="storsupriseremoval"></span><span id="STORSUPRISEREMOVAL"></span><dl> <dt>**StorSupriseRemoval**</dt> <dt>0x17</dt> </dl>                                                 | Surprise Removal of the device. This value is available starting with Windows 7.<br/> |



 

</dd> <dt>

**SrbPnPFlags**
</dt> <dd>

Indicates that the PNP request is for the adapter if SRB\_PNP\_FLAGS\_ADAPTER\_REQUEST is set and that storage device address is reserved. Otherwise, *SrbPnPFlags* will be **NULL**, indicating that the request is for the storage device specified by an address at **AddressOffset** in the [**STORAGE\_REQUEST\_BLOCK**](storage-request-block.md) structure.

</dd> <dt>

**Reserved1**
</dt> <dd>

This member is reserved. Set to 0.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SRBEX_DATA_PNP%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






