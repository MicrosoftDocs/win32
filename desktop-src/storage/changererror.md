---
title: ChangerError function
description: ChangerError performs device-specific error handling.
ms.assetid: e2196971-47ad-4ac4-a3e9-c8f7f6b05321
keywords:
- ChangerError function Storage Devices
topic_type:
- apiref
api_name:
- ChangerError
api_location:
- mcd.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ChangerError function

**ChangerError** performs device-specific error handling.

## Syntax


```C++
VOID ChangerError(
   PDEVICE_OBJECT      DeviceObject,
   PSCSI_REQUEST_BLOCK Srb,
   NTSTATUS            *Status,
   BOOLEAN             *Retry
);
```



## Parameters

<dl> <dt>

*DeviceObject* 
</dt> <dd>

Pointer to the device object that represents the changer.

</dd> <dt>

*Srb* 
</dt> <dd>

Pointer to the SCSI request block for the operation that failed.

</dd> <dt>

*Status* 
</dt> <dd>

Specifies the address of the STATUS\_*XXX* code set by the system. The changer miniclass driver can change the status or leave it as is.

</dd> <dt>

*Retry* 
</dt> <dd>

Pointer to a flag that indicates whether to retry the request. The changer miniclass driver can set this flag or leave it as is.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

This routine is required.

If an SRB fails with a SCSI status of CHECK CONDITION, the SCSI class driver calls the changer class driver's **ChangerClassError** routine. **ChangerClassError** performs device-independent error handling and calls the changer miniclass driver's **ChangerError** routine.

**ChangerError** first checks *Srb***-&gt;SrbStatus** with SRB\_STATUS\_AUTOSENSE\_VALID to make sure the sense data buffer is valid. If so, it checks the sense data in *Srb***-&gt;SenseInfoBuffer** to determine whether to update *\*Status* with a more accurate STATUS\_*XXX* code and/or set the *Retry* flag before returning to the changer class driver. The changer class driver's retry count determines whether the SRB is actually retried.

## Requirements



|                            |                                                                                                                |
|----------------------------|----------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                             |
| Header<br/>          | <dl> <dt>Mcd.h (include Mcd.h or Ntddchgr.h)</dt> </dl> |
| IRQL<br/>            | PASSIVE\_LEVEL<br/>                                                                                      |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ChangerError%20function%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





