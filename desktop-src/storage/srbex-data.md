---
title: SRBEX\_DATA structure
description: The SRBEX\_DATA structure is the generalized format for containing extended SRB data.
ms.assetid: 15FB9877-6339-484B-83D5-6AD44EEE1D6E
keywords:
- SRBEX_DATA structure Storage Devices
- PSRBEX_DATA structure pointer Storage Devices
topic_type:
- apiref
api_name:
- SRBEX_DATA
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

# SRBEX\_DATA structure

The **SRBEX\_DATA** structure is the generalized format for containing extended SRB data.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
typedef struct _SRBEX_DATA {
  SRBEXDATATYPE Type;
  ULONG         Length;
  UCHAR         Data[ANYSIZE_ARRAY];
} SRBEX_DATA, *PSRBEX_DATA;
```



## Members

<dl> <dt>

**Type**
</dt> <dd>

Data type indicator for the extended SRB data structure. The possible values for **Type** are one of the following.



| Value                                                                                                                                                                                                                                            | Meaning                                                                                                                       |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| <span id="SrbExDataTypeUnknown"></span><span id="srbexdatatypeunknown"></span><span id="SRBEXDATATYPEUNKNOWN"></span><dl> <dt>**SrbExDataTypeUnknown**</dt> </dl>                         | The SRB extended data type is unknown.<br/>                                                                             |
| <span id="SrbExDataTypeBidirectional"></span><span id="srbexdatatypebidirectional"></span><span id="SRBEXDATATYPEBIDIRECTIONAL"></span><dl> <dt>**SrbExDataTypeBidirectional**</dt> </dl> | The SRB extended data is formatted as an [**SRBEX\_DATA\_BIDIRECTIONAL**](srbex-data-bidirectional.md) structure.<br/> |
| <span id="SrbExDataTypeScsiCdb16"></span><span id="srbexdatatypescsicdb16"></span><span id="SRBEXDATATYPESCSICDB16"></span><dl> <dt>**SrbExDataTypeScsiCdb16**</dt> </dl>                 | The SRB extended data is formatted as an [**SRBEX\_DATA\_SCSI\_CDB16**](srbex-data-scsi-cdb16.md) structure.<br/>      |
| <span id="SrbExDataTypeScsiCdb32"></span><span id="srbexdatatypescsicdb32"></span><span id="SRBEXDATATYPESCSICDB32"></span><dl> <dt>**SrbExDataTypeScsiCdb32**</dt> </dl>                 | The SRB extended data is formatted as an [**SRBEX\_DATA\_SCSI\_CDB32**](srbex-data-scsi-cdb32.md) structure.<br/>      |
| <span id="SrbExDataTypeScsiCdbVar"></span><span id="srbexdatatypescsicdbvar"></span><span id="SRBEXDATATYPESCSICDBVAR"></span><dl> <dt>**SrbExDataTypeScsiCdbVar**</dt> </dl>             | The SRB extended data is formatted as an [**SRBEX\_DATA\_SCSI\_CDB\_VAR**](srbex-data-scsi-cdb-var.md) structure.<br/> |
| <span id="SrbExDataTypeWmi"></span><span id="srbexdatatypewmi"></span><span id="SRBEXDATATYPEWMI"></span><dl> <dt>**SrbExDataTypeWmi**</dt> </dl>                                         | The SRB extended data is formatted as an [**SRBEX\_DATA\_WMI**](srbex-data-wmi.md) structure.<br/>                     |
| <span id="SrbExDataTypePower"></span><span id="srbexdatatypepower"></span><span id="SRBEXDATATYPEPOWER"></span><dl> <dt>**SrbExDataTypePower**</dt> </dl>                                 | The SRB extended data is formatted as an [**SRBEX\_DATA\_POWER**](srbex-data-power.md) structure.<br/>                 |
| <span id="SrbExDataTypePnp"></span><span id="srbexdatatypepnp"></span><span id="SRBEXDATATYPEPNP"></span><dl> <dt>**SrbExDataTypePnp**</dt> </dl>                                         | The SRB extended data is formatted as an [**SRBEX\_DATA\_PNP**](srbex-data-pnp.md) structure.<br/>                     |
| <span id="SrbExDataTypeIoInfo"></span><span id="srbexdatatypeioinfo"></span><span id="SRBEXDATATYPEIOINFO"></span><dl> <dt>**SrbExDataTypeIoInfo**</dt> </dl>                             | The SRB extended data is formatted as an [**SRBEX\_DATA\_IO\_INFO**](srbex-data-io-info.md) structure.<br/>            |



 

</dd> <dt>

**Length**
</dt> <dd>

Length of the SRB data, in bytes, present in the **Data** member.

</dd> <dt>

**Data**
</dt> <dd>

The extended SRB data block contents.

</dd> </dl>

## Remarks

The SRB extended data is present when the **SrbExDataOffset** array in the [**STORAGE\_REQUEST\_BLOCK**](storage-request-block.md) structure contains valid offset locations. A storage driver initially references a memory offset location contained in **SrbExDataOffset** as an **SRBEX\_DATA** structure. A pointer to the data block is then cast to the appropriate structure type based on the data type value in the **Type** member.

The following example code fragment shows how to access the extended data for the an SRB function of SRB\_FUNCTION\_PNP.


```C++
BOOLEAN CheckIo( _In_ PSCSI_REQUEST_BLOCK Srb)
{
    BOOLEAN result = TRUE;
    ULONG function;
    PSTORAGE_REQUEST_BLOCK SrbEx = (PSTORAGE_REQUEST_BLOCK)Srb;
    PSRBEX_DATA SrbExData = NULL;

    function = (SrbEx->Function == SRB_FUNCTION_STORAGE_REQUEST_BLOCK) ? SrbEx->SrbFunction : Srb->Function;

    switch (function)
    {
        case SRB_FUNCTION_PNP:
        {
            STOR_PNP_ACTION PnpAction;
            BOOLEAN ForAdapter;

            if (SrbEx->Function == SRB_FUNCTION_STORAGE_REQUEST_BLOCK)
            {
                PSRBEX_DATA_PNP SrbExDataPnp = NULL;

                SrbExData = (PSRBEX_DATA) ((PUCHAR)SrbEx + SrbEx->SrbExDataOffset[0]);
                if (SrbExData->Type == SrbExDataTypePnp)
                {
                    SrbExDataPnp = (PSRBEX_DATA_PNP) SrbExData;
                    ForAdapter = (SrbExDataPnp->SrbPnPFlags == SRB_PNP_FLAGS_ADAPTER_REQUEST);
                    PnpAction = SrbExDataPnp->PnPAction;
                }
                else
                {
                    ForAdapter = FALSE;
                    result = FALSE;
                }
            }
            else
            {
                PSCSI_PNP_REQUEST_BLOCK PnpSrb = (PSCSI_PNP_REQUEST_BLOCK)Srb;

                ForAdapter = (PnpSrb->SrbPnPFlags == SRB_PNP_FLAGS_ADAPTER_REQUEST);
                PnpAction = PnpSrb->PnPAction;
           }

           if (ForAdapter)
           {
               switch (PnpAction)
               {
                   case StorRemoveDevice:
                       //
                       // ...
                       //
                       Srb->SrbStatus = SRB_STATUS_SUCCESS;
                       break;

                   default:
                       Srb->SrbStatus = SRB_STATUS_INVALID_REQUEST;
                       result = FALSE;
                       break:
            }
        }

        default:
            break; 
    }

    return result;
}
```



## Requirements



|                    |                                                                                                                                  |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 8.<br/>                                                                                    |
| Header<br/>  | <dl> <dt>Storport.h (include Storport.h, Srb.h, or Minitape.h)</dt> </dl> |



## See also

<dl> <dt>

[**SRBEX\_DATA\_BIDIRECTIONAL**](srbex-data-bidirectional.md)
</dt> <dt>

[**SRBEX\_DATA\_IO\_INFO**](srbex-data-io-info.md)
</dt> <dt>

[**SRBEX\_DATA\_PNP**](srbex-data-pnp.md)
</dt> <dt>

[**SRBEX\_DATA\_POWER**](srbex-data-power.md)
</dt> <dt>

[**SRBEX\_DATA\_SCSI\_CDB16**](srbex-data-scsi-cdb16.md)
</dt> <dt>

[**SRBEX\_DATA\_SCSI\_CDB32**](srbex-data-scsi-cdb32.md)
</dt> <dt>

[**SRBEX\_DATA\_SCSI\_CDB\_VAR**](srbex-data-scsi-cdb-var.md)
</dt> <dt>

[**SRBEX\_DATA\_WMI**](srbex-data-wmi.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SRBEX_DATA%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






