---
title: PSCSIWMI\_EXECUTE\_METHOD callback function
description: A miniport drivers HwScsiWmiExecuteMethod routine is called to execute a method associated with a data block.
ms.assetid: 67a82442-591e-4e52-aaaf-b3cdb68c483a
keywords:
- HwScsiWmiExecuteMethod callback function Storage Devices
- PSCSIWMI_EXECUTE_METHOD
topic_type:
- apiref
api_name:
- HwScsiWmiExecuteMethod
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

# PSCSIWMI\_EXECUTE\_METHOD callback function

A miniport driver's **HwScsiWmiExecuteMethod** routine is called to execute a method associated with a data block. This routine is optional.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
BOOLEAN HwScsiWmiExecuteMethod(
  _In_    PVOID                    DeviceContext,
  _In_    PSCSIWMI_REQUEST_CONTEXT RequestContext,
  _In_    ULONG                    GuidIndex,
  _In_    ULONG                    InstanceIndex,
  _In_    ULONG                    MethodId,
  _In_    ULONG                    InBufferSize,
  _In_    ULONG                    OutBufferSize,
  _Inout_ PUCHAR                   Buffer
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

*GuidIndex* \[in\]
</dt> <dd>

Specifies the data block by its index into the list of GUIDs in the SCSI\_WMILIB\_CONTEXT structure that the miniport driver passed to [**ScsiPortWmiDispatchFunction**](scsiportwmidispatchfunction.md).

</dd> <dt>

*InstanceIndex* \[in\]
</dt> <dd>

If the block specified by *GuidIndex* has multiple instances, *InstanceIndex* specifies the instance.

</dd> <dt>

*MethodId* \[in\]
</dt> <dd>

Specifies the ID of the method to execute. The miniport driver defines the method ID as an item in a data block.

</dd> <dt>

*InBufferSize* \[in\]
</dt> <dd>

Indicates the size in bytes of the input data. If there is no input data, *InBufferSize* is zero.

</dd> <dt>

*OutBufferSize* \[in\]
</dt> <dd>

Indicates the number of bytes available in the buffer for output data.

</dd> <dt>

*Buffer* \[in, out\]
</dt> <dd>

Points to a buffer that holds the input data and receives the output data, if any, from the method. If the buffer is too small to receive all of the output, the miniport driver calls **ScsiPortWmiPostProcess** with SRB\_STATUS\_DATA\_OVERRUN and the size required.

</dd> </dl>

## Return value

**HwScsiWmiExecuteMethod** returns SRB\_STATUS\_PENDING if the request is pending, or a nonzero SRB status value if the request was completed. The SRB status value returned by this routine is the same as what was passed in to [**ScsiPortWmiPostProcess**](scsiportwmipostprocess.md). Although the return value data type is BOOLEAN, the **HwScsiWmiExecuteMethod** routine actually returns an SRB status value.

## Remarks

When a miniport driver receives an SRB in which the **Function** member is set to SRB\_FUNCTION\_WMI, it calls [**ScsiPortWmiDispatchFunction**](scsiportwmidispatchfunction.md) with a pointer to an initialized SCSI\_WMILIB\_CONTEXT structure and *MinorFunction* set to **Srb-&gt;WmiSubFunction**. The SCSI port driver calls the miniport driver's **HwScsiWmiExecuteMethod** routine if *MinorFunction* indicates a request to execute a method.

If a miniport driver does not implement a **HwScsiWmiExecuteMethod** routine, it must set **ExecuteWmiMethod** to **NULL** in the SCSI\_WMILIB\_CONTEXT the miniport driver passes to [**ScsiPortWmiDispatchFunction**](scsiportwmidispatchfunction.md). In this case, the port driver returns SRB\_STATUS\_ERROR to the caller.

If the method generates output, the miniport driver should check the size of the output buffer in *OutBufferSize* before performing any operation that might have side effects or that should not be performed twice. For example, if a method returns the values of a group of counters and then resets the counters, the miniport driver should check the buffer size before resetting the counters. This ensures that the port driver can safely resend the request with a larger buffer. If the buffer is too small, the miniport driver should call [**ScsiPortWmiPostProcess**](scsiportwmipostprocess.md) with SRB\_STATUS\_DATA\_OVERRUN and the size of the output buffer needed to fulfill the request.

The miniport driver executes the method and writes output, if any, to the buffer. Before returning from **HwScsiWmiExecuteMethod**, the miniport driver calls [**ScsiPortWmiPostProcess**](scsiportwmipostprocess.md) with an appropriate *SrbStatus* value and the number of bytes used in the output buffer.

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

[**ScsiPortWmiPostProcess**](scsiportwmipostprocess.md)
</dt> <dt>

[**ScsiPortWmiDispatchFunction**](scsiportwmidispatchfunction.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20PSCSIWMI_EXECUTE_METHOD%20callback%20function%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






