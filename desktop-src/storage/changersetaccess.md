---
title: ChangerSetAccess function
description: ChangerSetAccess handles the device-specific aspects of a device-control IRP with the IOCTL code IOCTL\_CHANGER\_SET\_ACCESS.
ms.assetid: 586820c5-5662-4f2d-9413-d06b9794173a
keywords:
- ChangerSetAccess function Storage Devices
topic_type:
- apiref
api_name:
- ChangerSetAccess
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

# ChangerSetAccess function

**ChangerSetAccess** handles the device-specific aspects of a device-control IRP with the IOCTL code[**IOCTL\_CHANGER\_SET\_ACCESS**](ioctl-changer-set-access.md).

## Syntax


```C++
NTSTATUS ChangerSetAccess(
  _In_ PDEVICE_OBJECT DeviceObject,
  _In_ PIRP           Irp
);
```



## Parameters

<dl> <dt>

*DeviceObject* \[in\]
</dt> <dd>

Pointer to the device object that represents the changer.

</dd> <dt>

*Irp* \[in\]
</dt> <dd>

Pointer to the IRP.

</dd> </dl>

## Return value

If the changer supports setting access, **ChangerSetAccess** returns the STATUS\_*XXX* value returned by the system port driver or one of the following values:

STATUS\_SUCCESS

STATUS\_INSUFFICIENT\_RESOURCES

STATUS\_INVALID\_PARAMETER

If the changer does not support setting access, ChangerSetAccess returns STATUS\_INVALID\_DEVICE\_REQUEST.

## Remarks

This routine is required.

**ChangerSetAccess** locks or unlocks a changer's IEport, door, or keypad, and extends or retracts an IEport.

The changer class driver checks the input buffer length in the I/O stack location before calling **ChangerSetAccess**. *Irp***-&gt;SystemBuffer** points to a [**CHANGER\_SET\_ACCESS**](changer-set-access.md) structure as an input parameter that indicates the element to set and the operation to perform.

**ChangerSetAccess** first checks for unsupported elements and operations, and returns the appropriate status code for those it doesn't support.

Next, **ChangerSetAccess** translates the zero-based element address passed by the system to the device-specific element address required by the changer.

Finally, **ChangerSetAccess** builds an SRB with a CDB for the given operation on the given element and sends it to the system port driver. The command to use depends on the changer. For example, the Exabyte miniclass driver uses the SCSI command PREVENT ALLOW MEDIUM REMOVAL to lock or unlock a changer door and MOVE MEDIUM to extend or retract an IEport.

## Requirements



|                            |                                                                                                                |
|----------------------------|----------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                             |
| Header<br/>          | <dl> <dt>Mcd.h (include Mcd.h or Ntddchgr.h)</dt> </dl> |
| IRQL<br/>            | PASSIVE\_LEVEL<br/>                                                                                      |



## See also

<dl> <dt>

[**GET\_CHANGER\_PARAMETERS**](get-changer-parameters.md)
</dt> <dt>

[**CHANGER\_SET\_ACCESS**](changer-set-access.md)
</dt> <dt>

[**IOCTL\_CHANGER\_SET\_ACCESS**](ioctl-changer-set-access.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ChangerSetAccess%20function%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






