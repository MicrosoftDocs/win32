---
title: PSCSIWMI\_FUNCTION\_CONTROL callback function
description: A miniport drivers HwScsiWmiFunctionControl routine is called to enable or disable notification of events.
ms.assetid: a975e201-9015-4315-830e-4cd7cc5a3bc5
keywords:
- HwScsiWmiFunctionControl callback function Storage Devices
- PSCSIWMI_FUNCTION_CONTROL
topic_type:
- apiref
api_name:
- HwScsiWmiFunctionControl
api_location:
- scsiwmi.h
api_type:
- UserDefined
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# PSCSIWMI\_FUNCTION\_CONTROL callback function

A miniport driver's **HwScsiWmiFunctionControl** routine is called to enable or disable notification of events. It is also called to enable or disable data collection for data blocks that the miniport driver designated as expensive to collect. This routine is optional.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
BOOLEAN HwScsiWmiFunctionControl(
  _In_ PVOID                          DeviceContext,
  _In_ PSCSIWMI_REQUEST_CONTEXT       RequestContext,
  _In_ ULONG                          GuidIndex,
  _In_ SCSIWMI_ENABLE_DISABLE_CONTROL Function,
  _In_ BOOLEAN                        Enable
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

Points to a value containing an enumerator value of type [**SCSIWMI\_REQUEST\_CONTEXT**](scsiwmi-request-context.md) that the miniport driver passed to [**ScsiPortWmiDispatchFunction**](scsiportwmidispatchfunction.md).

</dd> <dt>

*GuidIndex* \[in\]
</dt> <dd>

Specifies the block by its index into the list of GUIDs in the SCSI\_WMILIB\_CONTEXT structure that the miniport driver passed to [**ScsiPortWmiDispatchFunction**](scsiportwmidispatchfunction.md).

</dd> <dt>

*Function* \[in\]
</dt> <dd>

Specifies **ScsiWmiEventControl** to enable or disable an event, or **ScsiWmiDataBlockControl** to enable or disable data collection for a block that was registered as expensive to collect (that is, a block for which the miniport driver set WMIREG\_FLAG\_EXPENSIVE in **Flags** of the SCSIWMIGUIDREGINFO structure used to register the block).

</dd> <dt>

*Enable* \[in\]
</dt> <dd>

Specifies **TRUE** to enable the event or data collection, or **FALSE** to disable it.

</dd> </dl>

## Return value

**HwScsiWmiFunctionControl** returns SRB\_STATUS\_PENDING if the request is pending, or a nonzero SRB status value if the request was completed. The SRB status value returned by this routine is the same as what was passed in to [**ScsiPortWmiPostProcess**](scsiportwmipostprocess.md). Although the return value data type is BOOLEAN, the **HwScsiWmiFunctionControl** routine actually returns an SRB status value.

## Remarks

When a miniport driver receives an SRB in which the **Function** member is set to SRB\_FUNCTION\_WMI, it calls [**ScsiPortWmiDispatchFunction**](scsiportwmidispatchfunction.md) with a pointer to an initialized SCSI\_WMILIB\_CONTEXT structure and *MinorFunction* set to **Srb-&gt;WmiSubFunction**. The SCSI port driver calls a miniport driver's **HwScsiWmiFunctionControl** routine if *MinorFunction* indicates a request to enable or disable an event, or to enable or disable collection for a data block that the miniport driver registered as expensive to collect.

If a miniport driver does not implement a **HwScsiWmiFunctionControl** routine, it must set **WmiFunctionControl** to **NULL** in the SCSI\_WMILIB\_CONTEXT the miniport driver passes to [**ScsiPortWmiDispatchFunction**](scsiportwmidispatchfunction.md). The port driver returns SRB\_STATUS\_SUCCESS to the caller.

It is unnecessary for the miniport driver to check whether events or data collection are already enabled for a block because the port driver sends a single enable request when the first data consumer enables the block, and sends a single disable request when the last data consumer disables the block. The port driver will not call **HwScsiWmiFunctionControl** more than once to enable a block without an intervening call to disable it.

If the SRB is completed in the **HwScsiWmiFunctionControl** callback, then the miniport driver calls [**ScsiPortWmiPostProcess**](scsiportwmipostprocess.md) with an appropriate *SrbStatus*. If the miniport driver pends this SRB, then it should call **ScsiPortWmiPostProcess** when the SRB is done and before completing the SRB.

## Requirements



|                            |                                                                                                          |
|----------------------------|----------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                       |
| Header<br/>          | <dl> <dt>Scsiwmi.h (include Scsiwmi.h)</dt> </dl> |



## See also

<dl> <dt>

[**SCSIWMIGUIDREGINFO**](scsiwmiguidreginfo.md)
</dt> <dt>

[**SCSI\_WMILIB\_CONTEXT**](scsi-wmilib-context.md)
</dt> <dt>

[**ScsiPortWmiDispatchFunction**](scsiportwmidispatchfunction.md)
</dt> <dt>

[**ScsiPortWmiPostProcess**](scsiportwmipostprocess.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20PSCSIWMI_FUNCTION_CONTROL%20callback%20function%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






