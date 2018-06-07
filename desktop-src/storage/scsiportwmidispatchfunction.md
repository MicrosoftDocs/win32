---
title: ScsiPortWmiDispatchFunction routine
description: The ScsiPortWmiDispatchFunction routine is a dispatch routine for miniport drivers that support WMI.
ms.assetid: 48806050-403b-4375-8b19-e867f905b761
keywords:
- ScsiPortWmiDispatchFunction routine Storage Devices
topic_type:
- apiref
api_name:
- ScsiPortWmiDispatchFunction
api_location:
- scsiwmi.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ScsiPortWmiDispatchFunction routine

The **ScsiPortWmiDispatchFunction** routine is a dispatch routine for miniport drivers that support WMI.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
BOOLEAN ScsiPortWmiDispatchFunction(
  _In_ PSCSI_WMILIB_CONTEXT     WmiLibInfo,
  _In_ UCHAR                    MinorFunction,
  _In_ PVOID                    DeviceContext,
  _In_ PSCSIWMI_REQUEST_CONTEXT RequestContext,
  _In_ PVOID                    DataPath,
  _In_ ULONG                    BufferSize,
  _In_ PVOID                    Buffer
);
```



## Parameters

<dl> <dt>

*WmiLibInfo* \[in\]
</dt> <dd>

Pointer to a [**SCSI\_WMILIB\_CONTEXT**](scsi-wmilib-context.md) structure that contains registration information for a miniport driver's data blocks and event blocks and defines entry points for the miniport driver's WMI library callback routines.

</dd> <dt>

*MinorFunction* \[in\]
</dt> <dd>

Indicates the WMI action to perform. The miniport driver sets *MinorFunction* to **Srb-&gt;WmiSubFunction** from the input SRB.

</dd> <dt>

*DeviceContext* \[in\]
</dt> <dd>

Pointer to a miniport driver-defined context value. The port driver will pass *DeviceContext* to the miniport driver's *HwScsiWmiXxx* callback routine. This value would typically point to a HW\_DEVICE\_EXTENSION structure.

</dd> <dt>

*RequestContext* \[in\]
</dt> <dd>

Pointer to a SCSIWMI\_REQUEST\_CONTEXT structure that contains context information for the WMI SRB. If the SRB can pend, the miniport driver must allocate this structure from the SRB extension because the request context must remain valid until after **ScsiPortWmiPostProcess** returns with the final SRB return status and buffer size. **ScsiPortWmiDispatchFunction** will pass *RequestContext* to the miniport driver's callback routine that processes this request.

</dd> <dt>

*DataPath* \[in\]
</dt> <dd>

Pointer to a GUID that represents the data block associated with the request. The miniport driver sets *DataPath* to **Srb-&gt;DataPath** from the input SRB.

</dd> <dt>

*BufferSize* \[in\]
</dt> <dd>

Specifies the size in bytes of the data buffer. The miniport driver sets *BufferSize* to **Srb-&gt;DataTransferLength** from the input SRB.

</dd> <dt>

*Buffer* \[in\]
</dt> <dd>

Pointer to the data buffer. The miniport driver sets *Buffer* to **Srb-&gt;DataBuffer** from the input SRB.

</dd> </dl>

## Return value

**ScsiPortWmiDispatchFunction** returns **TRUE** if the request is pending, or **FALSE** if the request was completed.

## Remarks

When a miniport driver receives an SRB in which the **Function** member is set to SRB\_FUNCTION\_WMI, it calls **ScsiPortWmiDispatchFunction** with request parameters, including a pointer to an initialized SCSI\_WMILIB\_CONTEXT structure. This structure contains information about the miniport driver's data blocks and event blocks and defines entry points for the miniport driver's *HwScsiWmiXxx* callback routines.

**ScsiPortWmiDispatchFunction** confirms that the SRB is a WMI request and determines whether the block specified by the request is valid for the miniport driver. If these conditions are met, **ScsiPortWmiDispatchFunction** processes the SRB by calling the appropriate *HwScsiWmiXxx* entry point in the miniport driver's SCSI\_WMILIB\_CONTEXT structure. If the miniport driver does not define an entry point for an optional *HwScsiWmiXxx* routine, the port driver handles the request.

In either case, after **ScsiPortWmiDispatchFunction** returns, the miniport driver should do the following for requests that it does not pend:

-   Set **Srb-&gt;DataTransferLength** to the value returned by **ScsiPortWmiGetReturnSize**

-   Set **Srb-&gt;SrbStatus** to the value returned by **ScsiPortWmiGetReturnStatus**

-   Call **ScsiPortNotification** with **RequestComplete** and again with **NextRequest**

## Requirements



|                            |                                                                                                                     |
|----------------------------|---------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                                  |
| Header<br/>          | <dl> <dt>Scsiwmi.h (include Miniport.h or Scsi.h)</dt> </dl> |



## See also

<dl> <dt>

[**SCSI\_WMILIB\_CONTEXT**](scsi-wmilib-context.md)
</dt> <dt>

[**ScsiPortNotification**](scsiportnotification.md)
</dt> <dt>

[**ScsiPortWmiGetReturnSize**](scsiportwmigetreturnsize.md)
</dt> <dt>

[**ScsiPortWmiGetReturnStatus**](scsiportwmigetreturnstatus.md)
</dt> <dt>

[**ScsiPortWmiPostProcess**](scsiportwmipostprocess.md)
</dt> <dt>

[**SCSIWMI\_REQUEST\_CONTEXT**](scsiwmi-request-context.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ScsiPortWmiDispatchFunction%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






