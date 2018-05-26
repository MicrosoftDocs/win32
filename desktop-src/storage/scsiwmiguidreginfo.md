---
title: SCSIWMIGUIDREGINFO structure
description: The SCSIWMIGUIDREGINFO structure contains information about a given data or event block supported by a SCSI miniport driver.
ms.assetid: 7116445e-751b-478a-8e58-8f5c90d06b9b
keywords:
- SCSIWMIGUIDREGINFO structure Storage Devices
- PSCSIWMIGUIDREGINFO structure pointer Storage Devices
topic_type:
- apiref
api_name:
- SCSIWMIGUIDREGINFO
api_location:
- scsiwmi.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SCSIWMIGUIDREGINFO structure

The SCSIWMIGUIDREGINFO structure contains information about a given data or event block supported by a SCSI miniport driver.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
typedef struct {
  LPCGUID Guid;
  ULONG   InstanceCount;
  ULONG   Flags;
} SCSIWMIGUIDREGINFO, *PSCSIWMIGUIDREGINFO;
```



## Members

<dl> <dt>

**Guid**
</dt> <dd>

Points to the GUID that identifies the block.

</dd> <dt>

**InstanceCount**
</dt> <dd>

Specifies the number of instances defined for the block.

</dd> <dt>

**Flags**
</dt> <dd>

Indicates characteristics of the block. The SCSI port driver sets all but the following WMIREG\_FLAG\_*XXX* on behalf of the miniport driver. A miniport driver might set one or more of the following flags:

<dl> <dt>

<span id="WMIREG_FLAG_EVENT_ONLY_GUID"></span><span id="wmireg_flag_event_only_guid"></span>WMIREG\_FLAG\_EVENT\_ONLY\_GUID
</dt> <dd>

The block can be enabled or disabled as an event only, and cannot be queried or set. If this flag is clear, the block can also be queried or set.

</dd> <dt>

<span id="WMIREG_FLAG_EXPENSIVE"></span><span id="wmireg_flag_expensive"></span>WMIREG\_FLAG\_EXPENSIVE
</dt> <dd>

Requests the port driver send an enable-collection SRB the first time a data consumer opens the data block and a disable-collection SRB when the last data consumer closes the data block. This is recommended if collecting such data affects performance. A miniport driver need not collect the data until a data consumer explicitly requests it by opening the block.

</dd> <dt>

<span id="WMIREG_FLAG_REMOVE_GUID"></span><span id="wmireg_flag_remove_guid"></span>WMIREG\_FLAG\_REMOVE\_GUID
</dt> <dd>

Removes support for a previously registered block when set.

</dd> </dl> </dd> </dl>

## Remarks

The miniport driver passes a pointer to a SCSI\_WMILIB\_CONTEXT which contains a SCSIWMIREGGUID array in the *WmiLibInfo* parameter of [**ScsiPortWmiDispatchFunction**](scsiportwmidispatchfunction.md). The miniport driver passes this information each time it calls **ScsiPortWmiDispatchFunction**. Each SCSIWMIREGGUID structure in the array represents one of the miniport driver's data or event blocks.

A miniport driver's SCSIWMIREGGUID array should include any standard data blocks defined in *wmicore.mof* for its device type, and might include miniport driver-defined data and event blocks. A miniport driver defines custom data and event blocks in a MOF file, which is compiled as a resource attached to the miniport driver's binary image and specified in the *MofResourceName* parameter of the miniport driver's HwScsiWmiQueryReginfo routine.

For more information about defining blocks, [Windows Management Instrumentation](https://msdn.microsoft.com/library/windows/hardware/ff547139).

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Scsiwmi.h (include Scsiwmi.h)</dt> </dl> |



## See also

<dl> <dt>

[**HwScsiWmiQueryReginfo**](hwscsiwmiqueryreginfo.md)
</dt> <dt>

[**SCSI\_WMILIB\_CONTEXT**](scsi-wmilib-context.md)
</dt> <dt>

[**ScsiPortWmiDispatchFunction**](scsiportwmidispatchfunction.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SCSIWMIGUIDREGINFO%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






