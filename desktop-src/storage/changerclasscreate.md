---
title: ChangerClassCreate routine
description: The ChangerClassCreate routine is called by a changer minidriver to allow the class driver perform device-independent operations needed to create or close a device.
ms.assetid: 3abaf674-e8a8-42bb-ac31-1ca8f5e148e4
keywords:
- ChangerClassCreate routine Storage Devices
topic_type:
- apiref
api_name:
- ChangerClassCreate
api_location:
- mcd.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ChangerClassCreate routine

The **ChangerClassCreate** routine is called by a changer minidriver to allow the class driver perform device-independent operations needed to create or close a device.

## Syntax


```C++
NTSTATUS ChangerClassCreate(
  _In_ PDEVICE_OBJECT DeviceObject,
  _In_ PIRP           Irp
);
```



## Parameters

<dl> <dt>

*DeviceObject* \[in\]
</dt> <dd>

Pointer to the device object of the device to be created or closed.

</dd> <dt>

*Irp* \[in\]
</dt> <dd>

Pointer to the I/O request packet (IRP) that initiated the create or close operation.

</dd> </dl>

## Return value

If the operation succeeds, the **ChangerClassCreate** routine returns STATUS\_SUCCESS. Otherwise the routine returns one of the following status values.



| Return code                                                                                             | Description                                                                         |
|---------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| <dl> <dt>**STATUS\_NO\_SUCH\_DEVICE**</dt> </dl> | The device object does not have a properly initialized device extension.<br/> |
| <dl> <dt>**STATUS\_DEVICE\_BUSY**</dt> </dl>     | The device is already open. Only one open at a time is allowed.<br/>          |



 

## Requirements



|                            |                                                                                                                |
|----------------------------|----------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                             |
| Header<br/>          | <dl> <dt>Mcd.h (include Mcd.h or Ntddchgr.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ChangerClassCreate%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





