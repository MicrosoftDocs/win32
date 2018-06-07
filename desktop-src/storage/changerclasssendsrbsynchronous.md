---
title: ChangerClassSendSrbSynchronous routine
description: The ChangerClassSendSrbSynchronous routine synchronously sends an SRB to a specified device.
ms.assetid: 6765d7d5-528f-42c5-98c3-0484608a020b
keywords:
- ChangerClassSendSrbSynchronous routine Storage Devices
topic_type:
- apiref
api_name:
- ChangerClassSendSrbSynchronous
api_location:
- Mcd.lib
- Mcd.dll
api_type:
- LibDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ChangerClassSendSrbSynchronous routine

The **ChangerClassSendSrbSynchronous** routine synchronously sends an SRB to a specified device.

## Syntax


```C++
NTSTATUS ChangerClassSendSrbSynchronous(
  _In_ PDEVICE_OBJECT      DeviceObject,
  _In_ PSCSI_REQUEST_BLOCK Srb,
  _In_ PVOID               Buffer,
  _In_ ULONG               BufferSize,
  _In_ BOOLEAN             WriteToDevice
);
```



## Parameters

<dl> <dt>

*DeviceObject* \[in\]
</dt> <dd>

Pointer to the functional device object of the target device.

</dd> <dt>

*Srb* \[in\]
</dt> <dd>

Pointer to a partially initialized SCSI request block (SRB) to be sent to the target device.

</dd> <dt>

*Buffer* \[in\]
</dt> <dd>

Specifies address of the buffer that *Srb-&gt;***DataBuffer** should point to. **ChangerClassSendSrbSynchronous** creates an MDL for this buffer and passes it to the target device driver in the SRB IRP.

</dd> <dt>

*BufferSize* \[in\]
</dt> <dd>

Specifies length, in bytes, of the buffer.

</dd> <dt>

*WriteToDevice* \[in\]
</dt> <dd>

Indicates a write operation when **TRUE** and read operation when **FALSE**.

</dd> </dl>

## Return value

Returns STATUS\_SUCCESS if the SRB is transmitted successfully or the appropriate error code if the SRB fails or cannot be sent for some reason.

## Remarks

Changer miniclass drivers can call this class driver routine in Microsoft Windows XP and later operating systems. Miniclass drivers should use this routine to send an SRB to the port driver instead of calling the *classpnp.sys* library routine **ClassSendSrbSynchronous** directly. Although *classpnp.sys* is shipped with the Windows Driver Kit (WDK), it is not a supported API, and drivers that call this library's routines directly might not function properly in future releases.

**ChangerClassSendSrbSynchronous** finishes the initialization of the partially initialized SRB, setting the SRB's flags with the values indicated in the target's device object. **ChangerClassSendSrbSynchronous** creates the IRP that is used to convey the SRB to the target device, sends the IRP, then handles the IRP's completion.

If the IRP fails and the sense request data indicates that the IRP should be retried, **ChangerClassSendSrbSynchronous** will resend the IRP.

## Requirements



|                            |                                                                                                                |
|----------------------------|----------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                             |
| Header<br/>          | <dl> <dt>Mcd.h (include Mcd.h or Ntddchgr.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Mcd.lib</dt> </dl>                             |



## See also

<dl> <dt>

[**SCSI\_REQUEST\_BLOCK**](scsi-request-block.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ChangerClassSendSrbSynchronous%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






