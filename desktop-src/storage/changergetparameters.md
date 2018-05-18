---
title: ChangerGetParameters function
description: ChangerGetParameters handles the device-specific aspects of a device-control IRP with the IOCTL code IOCTL\_CHANGER\_GET\_PARAMETERS.
ms.assetid: 'c1f508a3-6aa8-4fed-af14-6466fcae30da'
keywords: ["ChangerGetParameters function Storage Devices"]
topic_type:
- apiref
api_name:
- ChangerGetParameters
api_location:
- mcd.h
api_type:
- HeaderDef
---

# ChangerGetParameters function

**ChangerGetParameters** handles the device-specific aspects of a device-control IRP with the IOCTL code [**IOCTL\_CHANGER\_GET\_PARAMETERS**](ioctl-changer-get-parameters.md).

## Syntax


```C++
NTSTATUS ChangerGetParameters(
  _In_ PDEVICE_OBJECT DeviceObject,
  _In_ PIRP           Irp
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

**ChangerGetParameters** returns the STATUS\_*XXX* value returned by the system port driver or one of the following values:

STATUS\_SUCCESS

STATUS\_INFO\_LENGTH\_MISMATCH

STATUS\_INSUFFICIENT\_RESOURCES

## Remarks

This routine is required.

**ChangerGetParameters** returns the parameters of a changer, including the number and type of its elements and the functionality it supports.

The changer class driver checks the output buffer length in the I/O stack location before calling **ChangerGetParameters**. If the output buffer length is smaller than **sizeof**([**GET\_CHANGER\_PARAMETERS**](get-changer-parameters.md)) the changer class driver returns with a value of STATUS\_INFO\_LENGTH\_MISMATCH.

**ChangerGetParameters** retrieves parameter data from the device by building SRBs with CDBs to get the SCSI parameter header page, the element address page, the transport geometry page, and the device capabilities page, or the non-SCSI equivalent of this data.

**ChangerGetParameters** then fills in a GET\_CHANGER\_PARAMETERS structure at *Irp***-&gt;AssociatedIrp.SystemBuffer** before returning to the changer class driver.

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

[**IOCTL\_CHANGER\_GET\_PARAMETERS**](changer-product-data.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ChangerGetParameters%20function%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






