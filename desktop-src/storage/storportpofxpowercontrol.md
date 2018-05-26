---
title: StorPortPoFxPowerControl routine
description: The StorPortPoFxPowerControl routine sends a power control request to the power management framework (PoFx) to forward to the power engine plug-in (PEP).
ms.assetid: 1EBEBD5D-E0E5-48A3-8CDA-C336575E53C6
keywords:
- StorPortPoFxPowerControl routine Storage Devices
topic_type:
- apiref
api_name:
- StorPortPoFxPowerControl
api_location:
- storport.lib
- storport.dll
api_type:
- LibDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# StorPortPoFxPowerControl routine

The **StorPortPoFxPowerControl** routine sends a power control request to the power management framework (PoFx) to forward to the power engine plug-in (PEP).

## Syntax


```C++
ULONG StorPortPoFxPowerControl(
  _In_      PVOID   HwDeviceExtension,
  _In_      LPCGUID PowerControlCode,
  _In_opt_  PVOID   InBuffer,
  _In_      SIZE_T  InBufferSize,
  _Out_opt_ PVOID   OutBuffer,
  _In_      SIZE_T  OutBufferSize,
  _Out_opt_ PSIZE_T BytesReturned
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

A pointer to the hardware device extension for the host bus adapter (HBA). This is the device extension used to register the device in a prior call to [**StorPortInitializePoFxPower**](storportinitializepofxpower.md).

</dd> <dt>

*PowerControlCode* \[in\]
</dt> <dd>

A pointer to the power control code. This code is a GUID value that specifies the requested operation.

</dd> <dt>

*InBuffer* \[in, optional\]
</dt> <dd>

A pointer to a caller-allocated buffer that contains the input data for the operation. The format for the data in this buffer depends on the power control code specified by the *PowerControlCode* parameter. The *InBuffer* parameter is optional and can be specified as NULL if the specified operation requires no input data.

</dd> <dt>

*InBufferSize* \[in\]
</dt> <dd>

The size, in bytes, of the input buffer that is pointed to by the *InBuffer* parameter. If *InBuffer* is NULL, set *InBufferSize* to zero.

</dd> <dt>

*OutBuffer* \[out, optional\]
</dt> <dd>

A pointer to a caller-allocated buffer that is to contain the output data from the operation. The format for the data in this buffer depends on the power control code specified by the *PowerControlCode* parameter. The *OutBuffer* parameter is optional and can be specified as NULL if the specified operation produces no output data.

</dd> <dt>

*OutBufferSize* \[in\]
</dt> <dd>

The size, in bytes, of the output buffer that is pointed to by the *OutBuffer* parameter. If *OutBuffer* is NULL, set *OutBufferSize* to zero.

</dd> <dt>

*BytesReturned* \[out, optional\]
</dt> <dd>

A pointer to a location into which the routine writes the number of bytes of data that were written to the buffer that is pointed to by *OutBuffer*. The number of bytes written will be less than or equal to *OutBufferSize*. This parameter is optional and can be specified as **NULL** if the caller does not need to know how many bytes were written to the output buffer.

</dd> </dl>

## Return value

The **StorPortPoFxPowerControl** routine returns one of these status codes:



| Return code                                                                                                           | Description                                                                                                                                                                                                                     |
|-----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**STOR\_STATUS\_SUCCESS**</dt> </dl>                  | The power control operation specified in *PowerControlCode* was successfully executed.<br/>                                                                                                                               |
| <dl> <dt>**STOR\_STATUS\_INVALID\_PARAMETER**</dt> </dl>       | Either *HwDeviceExtension* or *Device* is NULL.<br/> -or-<br/> *Address* points to an invalid unit address structure.<br/> -or-<br/> The storage device specified by *Address* is not found.<br/> |
| <dl> <dt>**STOR\_STATUS\_INVALID\_DEVICE\_REQUEST**</dt> </dl> | The storage device is not registered with the PoFx.<br/>                                                                                                                                                                  |
| <dl> <dt>**STOR\_STATUS\_INVALID\_IRQL**</dt> </dl>            | The current IRQL &gt; DISPATCH\_LEVEL.<br/>                                                                                                                                                                               |
| <dl> <dt>**STOR\_STATUS\_UNSUCCESSFUL**</dt> </dl>             | The power control operation was unsuccessful.<br/>                                                                                                                                                                        |



 

## Remarks

A minport driver calls this routine to send a power control request directly to the PEP. A power control request is similar to an I/O control request (IOCTL). Unlike an IOCTL, however, a power control request is sent directly to PEP and is not observed by other device drivers in the device stack. During a **StorPortPoFxPowerControl** call, the PEP synchronously performs the requested operation.

Similarly, The PEP can send a power control request directly to the miniport. The miniport driver handles this request in its [**HwStorAdapterControl**](hwstoradaptercontrol.md) and [**HwStorUnitControl**](hwstorunitcontrol.md) routines. The *ControlType* parameter receives the **ScsiAdapterPoFxPowerControl** type in the **HwStorAdapterControl** routine and the **ScsiUnitPoFxPowerControl** in the **HwStorUnitControl** routine.

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Version<br/>         | Available in starting with Windows 8.<br/>                                                                                        |
| Header<br/>          | <dl> <dt>Storport.h</dt> </dl>                                                   |
| Library<br/>         | <dl> <dt>Storport.lib</dt> </dl>                                                 |
| IRQL<br/>            | &lt;= DISPATCH\_LEVEL<br/>                                                                                                        |



## See also

<dl> <dt>

[**HwStorAdapterControl**](hwstoradaptercontrol.md)
</dt> <dt>

[**HwStorUnitControl**](hwstorunitcontrol.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortPoFxPowerControl%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






