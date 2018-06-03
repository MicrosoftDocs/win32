---
title: StorPortInvokeAcpiMethod routine
description: The StorPortInvokeAcpiMethod routine executes an ACPI method for a storage device.
ms.assetid: 2A8EF694-B699-46A0-9B1D-B7D0831F3944
keywords:
- StorPortInvokeAcpiMethod routine Storage Devices
topic_type:
- apiref
api_name:
- StorPortInvokeAcpiMethod
api_location:
- storport.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# StorPortInvokeAcpiMethod routine

The **StorPortInvokeAcpiMethod** routine executes an ACPI method for a storage device.

## Syntax


```C++
ULONG StorPortInvokeAcpiMethod(
  _In_      PVOID         HwDeviceExtension,
  _In_opt_  PSTOR_ADDRESS Address,
  _In_      ULONG         MethodName,
  _In_opt_  PVOID         InputBuffer,
  _In_      ULONG         InputBufferLength,
  _In_opt_  PVOID         OutputBuffer,
  _In_      ULONG         OutputBufferLength,
  _Out_opt_ PULONG        BytesReturned
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

A pointer to the hardware device extension for the host bus adapter (HBA).

</dd> <dt>

*Address* \[in, optional\]
</dt> <dd>

The address of the target device. This parameter is optional. If *Address* is set to **NULL**, the adapter is the target.

</dd> <dt>

*MethodName* \[in\]
</dt> <dd>

A four-byte name for the ACPI method. For example, ((ULONG) 'DDS\_') would name the \_SDD, or 'Set Device Data', ACPI method for an AHCI controller.

</dd> <dt>

*InputBuffer* \[in, optional\]
</dt> <dd>

A pointer to the input data to the method.

</dd> <dt>

*InputBufferLength* \[in\]
</dt> <dd>

The length, in bytes, of the buffer in *InputBuffer*.

</dd> <dt>

*OutputBuffer* \[in, optional\]
</dt> <dd>

A pointer to the output data from the method.

</dd> <dt>

*OutputBufferLength* \[in\]
</dt> <dd>

The length, in bytes, of the buffer in *OutputBuffer*.

</dd> <dt>

*BytesReturned* \[out, optional\]
</dt> <dd>

A pointer to the length, in bytes, of the data returned in *OutputBuffer*.

</dd> </dl>

## Return value

The **StorPortInvokeAcpiMethod** routine returns one of these status codes:



| Return code                                                                                                          | Description                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**STOR\_STATUS\_INVALID\_UNSUCCESSFUL**</dt> </dl>   | A general error condition exists.<br/>                                                                                                           |
| <dl> <dt>**STOR\_STATUS\_INVALID\_PARAMETER**</dt> </dl>      | *HwDeviceExtension*, *InputBuffer*, or *OutputBuffer* is NULL.<br/> -or-<br/> *Address* refers to a target that does not exist.<br/> |
| <dl> <dt>**STOR\_STATUS\_NOT\_IMPLEMENTED**</dt> </dl>        | The ACPI method is not implemented.<br/>                                                                                                         |
| <dl> <dt>**STOR\_STATUS\_INSUFFICIENT\_RESOURCES**</dt> </dl> | Insufficient resources are available to execute the method, or *OutputBufferLength* is not large enough for the returned data.<br/>              |
| <dl> <dt>**STOR\_STATUS\_INVALID\_IRQL**</dt> </dl>           | Current IRQL &gt; PASSIVE\_LEVEL.<br/>                                                                                                           |
| <dl> <dt>**STOR\_STATUS\_SUCCESS**</dt> </dl>                 | The method executed successfully.<br/>                                                                                                           |



 

## Remarks

The **StorPortInvokeAcpiMethod** enables a miniport driver to invoke ACPI methods defined for storage controllers and storage LUNs. The method names are four-byte character strings that occupy a **ULONG** value in *MethodName*.

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Version<br/>         | Available in Windows 8 and later versions of Windows.<br/>                                                                        |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| IRQL<br/>            | PASSIVE\_LEVEL<br/>                                                                                                               |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortInvokeAcpiMethod%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





