---
title: PSCSIWMI\_QUERY\_REGINFO callback function
description: A miniport driver's HwScsiWmiQueryReginfo routine is called to obtain information about the data and event blocks to be registered on behalf of the miniport driver by the SCSI port driver.
ms.assetid: '416f8629-324f-4698-bbe9-699f5d53011e'
keywords: ["HwScsiWmiQueryReginfo callback function Storage Devices", "PSCSIWMI_QUERY_REGINFO"]
topic_type:
- apiref
api_name:
- HwScsiWmiQueryReginfo
api_location:
- scsiwmi.h
api_type:
- UserDefined
---

# PSCSIWMI\_QUERY\_REGINFO callback function

A miniport driver's **HwScsiWmiQueryReginfo** routine is called to obtain information about the data and event blocks to be registered on behalf of the miniport driver by the SCSI port driver. This routine is required.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
UCHAR HwScsiWmiQueryReginfo(
  _In_  PVOID                    DeviceContext,
  _In_  PSCSIWMI_REQUEST_CONTEXT RequestContext,
  _Out_ PWCHAR                   *MofResourceName
);
```



## Parameters

<dl> <dt>

*DeviceContext* \[in\]
</dt> <dd>

Points to the miniport driver-defined context value passed to [**ScsiPortWmiDispatchFunction**](scsiportwmidispatchfunction.md).

</dd> <dt>

*RequestContext* \[in\]
</dt> <dd>

Points to the SCSIWMI\_REQUEST\_CONTEXT structure that the miniport driver passed to [**ScsiPortWmiDispatchFunction**](scsiportwmidispatchfunction.md).

</dd> <dt>

*MofResourceName* \[out\]
</dt> <dd>

Points to a **null**-terminated Unicode string that indicates the name of the MOF resource attached to the miniport driver's binary image file. This string can be declared as a constant in the miniport driver. If the miniport driver does not have a MOF resource attached, it should set *MofResourceName* to **NULL**.

</dd> </dl>

## Return value

**HwScsiWmiQueryReginfo** always returns SRB\_STATUS\_SUCCESS.

## Remarks

When a miniport driver receives an SRB in which the **Function** member is set to SRB\_FUNCTION\_WMI, it calls [**ScsiPortWmiDispatchFunction**](scsiportwmidispatchfunction.md) with a pointer to an initialized SCSI\_WMILIB\_CONTEXT structure and *MinorFunction* set to **Srb-&gt;WmiSubFunction**. If *MinorFunction* indicates a request for registration information, the SCSI port driver calls the miniport driver's **HwScsiWmiQueryReginfo** routine.

The miniport driver provides new or updated registration information about individual blocks, or indicates blocks to remove, in the SCSI\_WMILIB\_CONTEXT structure it passes to [**ScsiPortWmiDispatchFunction**](scsiportwmidispatchfunction.md). The miniport driver's **HwScsiWmiQueryReginfo** routine supplies a pointer to its MOF resource name.

The miniport driver must not pend or block the SRB. The miniport driver must not call [**ScsiPortWmiPostProcess**](scsiportwmipostprocess.md) or [**ScsiPortNotification**](scsiportnotification.md) from its **HwScsiWmiQueryReginfo** routine.

## Requirements



|                            |                                                                                                          |
|----------------------------|----------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                       |
| Header<br/>          | <dl> <dt>Scsiwmi.h (include Scsiwmi.h)</dt> </dl> |



## See also

<dl> <dt>

[**SCSI\_WMILIB\_CONTEXT**](scsi-wmilib-context.md)
</dt> <dt>

[**SCSIWMI\_REQUEST\_CONTEXT**](scsiwmi-request-context.md)
</dt> <dt>

[**ScsiPortWmiDispatchFunction**](scsiportwmidispatchfunction.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20PSCSIWMI_QUERY_REGINFO%20callback%20function%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






