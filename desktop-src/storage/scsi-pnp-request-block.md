---
title: SCSI\_PNP\_REQUEST\_BLOCK structure
description: TheSCSI\_PNP\_REQUEST\_BLOCK structure is a special version of a SCSI\_REQUEST\_BLOCK that is used for plug and play (PNP) requests.Note The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future.
ms.assetid: '0627065b-62c2-4df8-973c-b4fb5811296e'
keywords: ["SCSI_PNP_REQUEST_BLOCK structure Storage Devices", "PSCSI_PNP_REQUEST_BLOCK structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- SCSI_PNP_REQUEST_BLOCK
api_location:
- storport.h
api_type:
- HeaderDef
---

# SCSI\_PNP\_REQUEST\_BLOCK structure

The**SCSI\_PNP\_REQUEST\_BLOCK** structure is a special version of a [**SCSI\_REQUEST\_BLOCK**](scsi-request-block.md) that is used for plug and play (PNP) requests.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
typedef struct _SCSI_PNP_REQUEST_BLOCK {
  USHORT                     Length;
  UCHAR                      Function;
  UCHAR                      SrbStatus;
  UCHAR                      PnPSubFunction;
  UCHAR                      PathId;
  UCHAR                      TargetId;
  UCHAR                      Lun;
  STOR_PNP_ACTION            PnPAction;
  ULONG                      SrbFlags;
  ULONG                      DataTransferLength;
  ULONG                      TimeOutValue;
  PVOID                      DataBuffer;
  PVOID                      SenseInfoBuffer;
  struct _SCSI_REQUEST_BLOCK  *NextSrb;
  PVOID                      OriginalRequest;
  PVOID                      SrbExtension;
  ULONG                      SrbPnPFlags;
#ifdef _WIN64
  ULONG                      Reserved;
#endif 
  UCHAR                      Reserved4[16];
} SCSI_PNP_REQUEST_BLOCK, *PSCSI_PNP_REQUEST_BLOCK;
```



## Members

<dl> <dt>

**Length**
</dt> <dd>

The size, in bytes, of the **SCSI\_PNP\_REQUEST\_BLOCK** structure.

</dd> <dt>

**Function**
</dt> <dd>

The operation to perform. For the **SCSI\_PNP\_REQUEST\_BLOCK** structure, this member is always set to SRB\_FUNCTION\_PNP.

</dd> <dt>

**SrbStatus**
</dt> <dd>

The status of the completed request. The miniport driver should set this value before notifying the Storport driver that the request has completed. A miniport driver notifies the Storport driver that the request has completed by calling the [**StorPortNotification**](storportnotification.md) routine with a notification type of **RequestComplete**. For a list of possible status values, see [**SCSI\_REQUEST\_BLOCK**](scsi-request-block.md).

</dd> <dt>

**PnPSubFunction**
</dt> <dd>

This member is not currently used. Miniport drivers ignore this member.

</dd> <dt>

**PathId**
</dt> <dd>

The SCSI port or bus identifier for the request. This value is zero based.

</dd> <dt>

**TargetId**
</dt> <dd>

The target controller or device identifier on the bus.

</dd> <dt>

**Lun**
</dt> <dd>

The logical unit number (LUN) of the device.

</dd> <dt>

**PnPAction**
</dt> <dd>

The plug and play action to perform. This member can have one of the following values:



| Value                                                                                                                                                                                                                                                                                                                      | Meaning                                                                       |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| <span id="StorStartDevice"></span><span id="storstartdevice"></span><span id="STORSTARTDEVICE"></span><dl> <dt>**StorStartDevice**</dt> <dt>0x00</dt> </dl>                                                             | Start the device.<br/>                                                  |
| <span id="StorRemoveDevice"></span><span id="storremovedevice"></span><span id="STORREMOVEDEVICE"></span><dl> <dt>**StorRemoveDevice**</dt> <dt>0x02</dt> </dl>                                                         | Remove the device.<br/>                                                 |
| <span id="StorStopDevice"></span><span id="storstopdevice"></span><span id="STORSTOPDEVICE"></span><dl> <dt>**StorStopDevice**</dt> <dt>0x04</dt> </dl>                                                                 | Stop the device.<br/>                                                   |
| <span id="StorQueryCapabilities"></span><span id="storquerycapabilities"></span><span id="STORQUERYCAPABILITIES"></span><dl> <dt>**StorQueryCapabilities**</dt> <dt>0x09</dt> </dl>                                     | Query the capabilities of the device.<br/>                              |
| <span id="StorQueryResourceRequirements"></span><span id="storqueryresourcerequirements"></span><span id="STORQUERYRESOURCEREQUIREMENTS"></span><dl> <dt>**StorQueryResourceRequirements**</dt> <dt>0x0B</dt> </dl>     | Query the resource requirements for the device.<br/>                    |
| <span id="StorFilterResourceRequirements"></span><span id="storfilterresourcerequirements"></span><span id="STORFILTERRESOURCEREQUIREMENTS"></span><dl> <dt>**StorFilterResourceRequirements**</dt> <dt>0x0D</dt> </dl> | Filter the resource requirements for the device. <br/>                  |
| <span id="StorSupriseRemoval"></span><span id="storsupriseremoval"></span><span id="STORSUPRISEREMOVAL"></span><dl> <dt>**StorSupriseRemoval**</dt> <dt>0x17</dt> </dl>                                                 | Surprise Removal of the device. This value was added in Windows 7.<br/> |



 

</dd> <dt>

**SrbFlags**
</dt> <dd>

Miniport driver should ignore this member.

</dd> <dt>

**DataTransferLength**
</dt> <dd>

Miniport driver should ignore this member.

</dd> <dt>

**TimeOutValue**
</dt> <dd>

The interval, in seconds, that the request can execute before the Storport driver determines that the request has timed out.

</dd> <dt>

**DataBuffer**
</dt> <dd>

Miniport driver should ignore this member.

</dd> <dt>

**SenseInfoBuffer**
</dt> <dd>

Miniport driver should ignore this member.

</dd> <dt>

**NextSrb**
</dt> <dd>

Miniport driver should ignore this member.

</dd> <dt>

**OriginalRequest**
</dt> <dd>

Miniport driver should ignore this member.

</dd> <dt>

**SrbExtension**
</dt> <dd>

A pointer to the SRB extension. A miniport driver must not use this member if it set **SrbExtensionSize** to zero in the [**HW\_INITIALIZATION\_DATA**](hw-initialization-data--storport-.md) structure. The Storport driver does not initialize the memory that this member points to. The HBA can directly access the data that the miniport driver writes into the SRB extension. A miniport driver can obtain the physical address of the SRB extension by calling the [**StorPortGetPhysicalAddress**](storportgetphysicaladdress.md) routine.

</dd> <dt>

**SrbPnPFlags**
</dt> <dd>

The PNP flags. Currently, the only flag allowed is SRB\_PNP\_FLAGS\_ADAPTER\_REQUEST, which indicates that the PNP request is for the adapter, and not for one of the devices on the adapter. If this flag is set, the miniport driver should ignore the values in the **PathId**, **TargetId**, and **Lun**.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved for system use.

</dd> <dt>

**Reserved4**
</dt> <dd>

Reserved for system use.

</dd> </dl>

## Remarks

The Storport driver sends **SCSI\_PNP\_REQUEST\_BLOCK** requests to a miniport driver to notify the miniport driver of Windows plug and play events that affect storage devices that are connected to the adapter.

The Storport driver calls [**HwStorBuildIo**](hwstorbuildio.md) to pass SRBs to the miniport driver. **HwStorBuildIo** checks the **Function** member of the SRB to determine the type of the SRB. If the **Function** member is set to SRB\_FUNCTION\_PNP, the SRB is a structure of type **SCSI\_PNP\_REQUEST\_BLOCK**.

## Requirements



|                   |                                                                                                                                  |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Storport.h (include Storport.h, Minitape.h, or Srb.h)</dt> </dl> |



## See also

<dl> <dt>

[**HwStorBuildIo**](hwstorbuildio.md)
</dt> <dt>

[**SCSI\_REQUEST\_BLOCK**](scsi-request-block.md)
</dt> <dt>

[**StorPortNotification**](storportnotification.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SCSI_PNP_REQUEST_BLOCK%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






