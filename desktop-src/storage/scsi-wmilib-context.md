---
title: SCSI\_WMILIB\_CONTEXT structure
description: A SCSI\_WMILIB\_CONTEXT structure provides registration information for a miniport driver's data and event blocks and defines entry points for the miniport driver's HwScsiWmiXxx callback routines.
ms.assetid: '7886cee8-1142-42e6-8206-84667621ba77'
keywords: ["SCSI_WMILIB_CONTEXT structure Storage Devices", "PSCSI_WMILIB_CONTEXT structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- SCSI_WMILIB_CONTEXT
api_location:
- scsiwmi.h
api_type:
- HeaderDef
---

# SCSI\_WMILIB\_CONTEXT structure

A SCSI\_WMILIB\_CONTEXT structure provides registration information for a miniport driver's data and event blocks and defines entry points for the miniport driver's **HwScsiWmi*Xxx*** callback routines.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
typedef struct _SCSIWMILIB_CONTEXT {
  ULONG                     GuidCount;
  PSCSIWMIGUIDREGINFO       GuidList;
  PSCSIWMI_QUERY_REGINFO    QueryWmiRegInfo;
  PSCSIWMI_QUERY_DATABLOCK  QueryWmiDataBlock;
  PSCSIWMI_SET_DATABLOCK    SetWmiDataBlock;
  PSCSIWMI_SET_DATAITEM     SetWmiDataItem;
  PSCSIWMI_EXECUTE_METHOD   ExecuteWmiMethod;
  PSCSIWMI_FUNCTION_CONTROL WmiFunctionControl;
} SCSI_WMILIB_CONTEXT, *PSCSI_WMILIB_CONTEXT;
```



## Members

<dl> <dt>

**GuidCount**
</dt> <dd>

Specifies the number of structures in the SCSIWMIGUIDREGINFO array at **GuidList**.

</dd> <dt>

**GuidList**
</dt> <dd>

Points to an array of **GuidCount** SCSIWMIGUIDREGINFO structures that contain registration information for each block.

</dd> <dt>

**QueryWmiRegInfo**
</dt> <dd>

Points to the driver's [**HwScsiWmiQueryReginfo**](hwscsiwmiqueryreginfo.md) routine, which is a required entry point for miniport drivers that support WMI.

</dd> <dt>

**QueryWmiDataBlock**
</dt> <dd>

Points to the driver's [**HwScsiWmiQueryDataBlock**](hwscsiwmiquerydatablock.md) routine, which is a required entry point for miniport drivers that support WMI.

</dd> <dt>

**SetWmiDataBlock**
</dt> <dd>

Points to the driver's [**HwScsiWmiSetDataBlock**](hwscsiwmisetdatablock.md) routine, which is an optional entry point for miniport drivers that support WMI. If the miniport driver does not implement this routine, it must set this member to **NULL**

</dd> <dt>

**SetWmiDataItem**
</dt> <dd>

Points to the driver's [**HwScsiWmiSetDataItem**](hwscsiwmisetdataitem.md) routine, which is an optional entry point for miniport drivers that support WMI. If the miniport driver does not implement this routine, it must set this member to **NULL**.

</dd> <dt>

**ExecuteWmiMethod**
</dt> <dd>

Points to the driver's [**HwScsiWmiExecuteMethod**](hwscsiwmiexecutemethod.md) routine, which is an optional entry point for miniport drivers that support WMI. If the miniport driver does not implement this routine, it must set this member to **NULL**

</dd> <dt>

**WmiFunctionControl**
</dt> <dd>

Points to the driver's [**HwScsiWmiFunctionControl**](hwscsiwmifunctioncontrol.md) routine, which is an optional entry point for miniport drivers that support WMI. If the miniport driver does not implement this routine, it must set this member to **NULL**.

</dd> </dl>

## Remarks

A SCSI miniport driver that supports WMI stores an initialized SCSI\_WMILIB\_CONTEXT structure (or a pointer to such a structure) in its device extension. A miniport driver can use the same SCSI\_WMILIB\_CONTEXT structure for multiple device objects if each device object supplies the same set of data blocks.

When the miniport driver receives an SRB in which the **Function** member is set to SRB\_FUNCTION\_WMI, it calls [**ScsiPortWmiDispatchFunction**](scsiportwmidispatchfunction.md) with request parameters, including a pointer to an initialized SCSI\_WMILIB\_CONTEXT structure. **ScsiPortWmiDispatchFunction** handles the request by calling the miniport driver's appropriate HwScsiWmiXxx routine.

If the miniport driver does not implement an optional HwScsiWmiXxx routine, the port driver returns an appropriate status to the caller.

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Scsiwmi.h (include Scsiwmi.h)</dt> </dl> |



## See also

<dl> <dt>

[**HwScsiWmiExecuteMethod**](hwscsiwmiexecutemethod.md)
</dt> <dt>

[**HwScsiWmiFunctionControl**](hwscsiwmifunctioncontrol.md)
</dt> <dt>

[**HwScsiWmiQueryDataBlock**](hwscsiwmiquerydatablock.md)
</dt> <dt>

[**HwScsiWmiQueryReginfo**](hwscsiwmiqueryreginfo.md)
</dt> <dt>

[**HwScsiWmiSetDataBlock**](hwscsiwmisetdatablock.md)
</dt> <dt>

[**HwScsiWmiSetDataItem**](hwscsiwmisetdataitem.md)
</dt> <dt>

[**ScsiPortWmiDispatchFunction**](scsiportwmidispatchfunction.md)
</dt> <dt>

[**SCSIWMIGUIDREGINFO**](scsiwmiguidreginfo.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SCSI_WMILIB_CONTEXT%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






