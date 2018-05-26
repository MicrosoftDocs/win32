---
title: MCD\_INIT\_DATA structure
description: The changer miniclass driver fills the MCD\_INIT\_DATA structure with pointers to its internal command processing routines and passes them to the changer class driver.
ms.assetid: 4fc4c36f-a2ad-4b9f-a30b-e7ed600c38e9
keywords:
- MCD_INIT_DATA structure Storage Devices
- PMCD_INIT_DATA structure pointer Storage Devices
topic_type:
- apiref
api_name:
- MCD_INIT_DATA
api_location:
- mcd.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MCD\_INIT\_DATA structure

The changer miniclass driver fills the MCD\_INIT\_DATA structure with pointers to its internal command processing routines and passes them to the changer class driver.

## Syntax


```C++
typedef struct _MCD_INIT_DATA {
  ULONG                       InitDataSize;
  CHANGER_EXTENSION_SIZE      ChangerAdditionalExtensionSize;
  CHANGER_INITIALIZE          ChangerInitialize;
  CHANGER_ERROR_ROUTINE       ChangerError;
  CHANGER_PERFORM_DIAGNOSTICS ChangerPerformDiagnostics;
  CHANGER_COMMAND_ROUTINE     ChangerGetParameters;
  CHANGER_COMMAND_ROUTINE     ChangerGetStatus;
  CHANGER_COMMAND_ROUTINE     ChangerGetProductData;
  CHANGER_COMMAND_ROUTINE     ChangerSetAccess;
  CHANGER_COMMAND_ROUTINE     ChangerGetElementStatus;
  CHANGER_COMMAND_ROUTINE     ChangerInitializeElementStatus;
  CHANGER_COMMAND_ROUTINE     ChangerSetPosition;
  CHANGER_COMMAND_ROUTINE     ChangerExchangeMedium;
  CHANGER_COMMAND_ROUTINE     ChangerMoveMedium;
  CHANGER_COMMAND_ROUTINE     ChangerReinitializeUnit;
  CHANGER_COMMAND_ROUTINE     ChangerQueryVolumeTags;
} MCD_INIT_DATA, *PMCD_INIT_DATA;
```



## Members

<dl> <dt>

**InitDataSize**
</dt> <dd>

Size of this structure in bytes.

</dd> <dt>

**ChangerAdditionalExtensionSize**
</dt> <dd>

Pointer to changer miniclass driver routine that returns the number of bytes the changer miniclass driver requires to store device-specific information in the device extension. This routine has the following prototype:


```
typedef
ULONG
(*CHANGER_EXTENSION_SIZE)(
  IN VOID
  );
```



</dd> <dt>

**ChangerInitialize**
</dt> <dd>

Pointer to changer miniclass driver routine that does miniclass driver-specific initialization and readies the changer to receive other requests. This routine has the following prototype:


```
typedef 
NTSTATUS
(*CHANGER_INITIALIZE)(
  IN PDEVICE_OBJECT  DeviceObject
  );
```



</dd> <dt>

**ChangerError**
</dt> <dd>

Pointer to changer miniclass driver routine that does device-specific error processing. This routine has the following prototype:


```
typedef
VOID
(*CHANGER_ERROR_ROUTINE)(
  IN PDEVICE_OBJECT  DeviceObject,
  IN PSCSI_REQUEST_BLOCK  Srb,
  IN NTSTATUS  *Status,
  IN BOOLEAN  *Retry
  );
```



</dd> <dt>

**ChangerPerformDiagnostics**
</dt> <dd>

Pointer to changer miniclass driver routine that performs diagnostic tests on the device. This routine has the following prototype:


```
typedef 
NTSTATUS
(*CHANGER_PERFORM_DIAGNOSTICS)(
  IN PDEVICE_OBJECT  DeviceObject,
  OUT PWMI_CHANGER_PROBLEM_DEVICE_ERROR  changerDeviceError
  );
```



</dd> <dt>

**ChangerGetParameters**
</dt> <dd>

Pointer to changer miniclass driver routine that handles the device-specific aspects of a device-control IRP with the IOCTL code [**IOCTL\_CHANGER\_GET\_PARAMETERS**](ioctl-changer-get-parameters.md). This routine has the following prototype:


```
typedef
NTSTATUS
(*CHANGER_COMMAND_ROUTINE)(
  IN PDEVICE_OBJECT  DeviceObject,
  IN PIRP  Irp
  );
```



</dd> <dt>

**ChangerGetStatus**
</dt> <dd>

Pointer to changer miniclass driver routine that handles the device-specific aspects of a device-control IRP with the IOCTL code [**IOCTL\_CHANGER\_GET\_STATUS**](ioctl-changer-get-status.md). This routine has the following prototype:


```
typedef
NTSTATUS
(*CHANGER_COMMAND_ROUTINE)(
  IN PDEVICE_OBJECT  DeviceObject,
  IN PIRP  Irp
  );
```



</dd> <dt>

**ChangerGetProductData**
</dt> <dd>

Pointer to a changer miniclass driver routine that handles the device-specific aspects of a device-control IRP with the IOCTL code [**IOCTL\_CHANGER\_GET\_PRODUCT\_DATA**](ioctl-changer-get-product-data.md). This routine has the following prototype:


```
typedef
NTSTATUS
(*CHANGER_COMMAND_ROUTINE)(
  IN PDEVICE_OBJECT  DeviceObject,
  IN PIRP  Irp
  );
```



</dd> <dt>

**ChangerSetAccess**
</dt> <dd>

Pointer to a changer miniclass driver routine that handles the device-specific aspects of a device-control IRP with the IOCTL code [**IOCTL\_CHANGER\_SET\_ACCESS**](ioctl-changer-set-access.md). This routine has the following prototype:


```
typedef
NTSTATUS
(*CHANGER_COMMAND_ROUTINE)(
  IN PDEVICE_OBJECT  DeviceObject,
  IN PIRP  Irp
  );
```



</dd> <dt>

**ChangerGetElementStatus**
</dt> <dd>

Pointer to a changer miniclass driver routine that handles the device-specific aspects of a device-control IRP with the IOCTL code [**IOCTL\_CHANGER\_GET\_ELEMENT\_STATUS**](ioctl-changer-get-element-status.md). This routine has the following prototype:


```
typedef
NTSTATUS
(*CHANGER_COMMAND_ROUTINE)(
  IN PDEVICE_OBJECT  DeviceObject,
  IN PIRP  Irp
  );
```



</dd> <dt>

**ChangerInitializeElementStatus**
</dt> <dd>

Pointer to a changer miniclass driver routine that handles the device-specific aspects of a device-control IRP with the IOCTL code [**IOCTL\_CHANGER\_INITIALIZE\_ELEMENT\_STATUS**](ioctl-changer-initialize-element-status.md). This routine has the following prototype:


```
typedef
NTSTATUS
(*CHANGER_COMMAND_ROUTINE)(
  IN PDEVICE_OBJECT  DeviceObject,
  IN PIRP  Irp
  );
```



</dd> <dt>

**ChangerSetPosition**
</dt> <dd>

Pointer to a changer miniclass driver routine that handles the device-specific aspects of a device-control IRP with the IOCTL code [**IOCTL\_CHANGER\_SET\_POSITION**](ioctl-changer-set-position.md). This routine has the following prototype:


```
typedef
NTSTATUS
(*CHANGER_COMMAND_ROUTINE)(
  IN PDEVICE_OBJECT  DeviceObject,
  IN PIRP  Irp
  );
```



</dd> <dt>

**ChangerExchangeMedium**
</dt> <dd>

Pointer to a changer miniclass driver routine that handles the device-specific aspects of a device-control IRP with the IOCTL code [**IOCTL\_CHANGER\_EXCHANGE\_MEDIUM**](ioctl-changer-exchange-medium.md). This routine has the following prototype:


```
typedef
NTSTATUS
(*CHANGER_COMMAND_ROUTINE)(
  IN PDEVICE_OBJECT  DeviceObject,
  IN PIRP  Irp
  );
```



</dd> <dt>

**ChangerMoveMedium**
</dt> <dd>

Pointer to a changer miniclass driver routine that handles the device-specific aspects of a device-control IRP with the IOCTL code [**IOCTL\_CHANGER\_MOVE\_MEDIUM**](ioctl-changer-move-medium.md). This routine has the following prototype:


```
typedef
NTSTATUS
(*CHANGER_COMMAND_ROUTINE)(
  IN PDEVICE_OBJECT  DeviceObject,
  IN PIRP  Irp
  );
```



</dd> <dt>

**ChangerReinitializeUnit**
</dt> <dd>

Pointer to a changer miniclass driver routine that handles the device-specific aspects of a device-control IRP with the IOCTL code [**IOCTL\_CHANGER\_REINITIALIZE\_TRANSPORT**](ioctl-changer-reinitialize-transport.md). This routine has the following prototype:


```
typedef
NTSTATUS
(*CHANGER_COMMAND_ROUTINE)(
  IN PDEVICE_OBJECT  DeviceObject,
  IN PIRP  Irp
  );
```



</dd> <dt>

**ChangerQueryVolumeTags**
</dt> <dd>

Pointer to a changer miniclass driver routine that handles the device-specific aspects of a device-control IRP with the IOCTL code of [**IOCTL\_CHANGER\_QUERY\_VOLUME\_TAGS**](ioctl-changer-query-volume-tags.md). This routine has the following prototype:


```
typedef
NTSTATUS
(*CHANGER_COMMAND_ROUTINE)(
  IN PDEVICE_OBJECT  DeviceObject,
  IN PIRP  Irp
  );
```



</dd> </dl>

## Remarks

This structure is used by the changer driver in Windows XP and later operating systems only.

## Requirements



|                   |                                                                                                  |
|-------------------|--------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mcd.h (include Mcd.h)</dt> </dl> |



## See also

<dl> <dt>

[**ChangerAdditionalExtensionSize**](changeradditionalextensionsize.md)
</dt> <dt>

[**ChangerInitialize**](changerinitialize.md)
</dt> <dt>

[**ChangerError**](changererror.md)
</dt> <dt>

[**ChangerPerformDiagnostics**](changerperformdiagnostics.md)
</dt> <dt>

[**ChangerGetParameters**](changergetparameters.md)
</dt> <dt>

[**ChangerGetStatus**](changergetstatus.md)
</dt> <dt>

[**ChangerGetProductData**](changergetproductdata.md)
</dt> <dt>

[**ChangerSetAccess**](changersetaccess.md)
</dt> <dt>

[**ChangerGetElementStatus**](changergetelementstatus.md)
</dt> <dt>

[**ChangerInitializeElementStatus**](changerinitializeelementstatus.md)
</dt> <dt>

[**ChangerSetPosition**](changersetposition.md)
</dt> <dt>

[**ChangerExchangeMedium**](changerexchangemedium.md)
</dt> <dt>

[**ChangerMoveMedium**](changermovemedium.md)
</dt> <dt>

[**ChangerReinitializeUnit**](changerreinitializeunit.md)
</dt> <dt>

[**ChangerQueryVolumeTags**](changerqueryvolumetags.md)
</dt> <dt>

[**IOCTL\_CHANGER\_GET\_PARAMETERS**](ioctl-changer-get-parameters.md)
</dt> <dt>

[**IOCTL\_CHANGER\_GET\_STATUS**](ioctl-changer-get-status.md)
</dt> <dt>

[**IOCTL\_CHANGER\_GET\_PRODUCT\_DATA**](ioctl-changer-get-product-data.md)
</dt> <dt>

[**IOCTL\_CHANGER\_SET\_ACCESS**](ioctl-changer-set-access.md)
</dt> <dt>

[**IOCTL\_CHANGER\_GET\_ELEMENT\_STATUS**](ioctl-changer-get-element-status.md)
</dt> <dt>

[**IOCTL\_CHANGER\_INITIALIZE\_ELEMENT\_STATUS**](ioctl-changer-initialize-element-status.md)
</dt> <dt>

[**IOCTL\_CHANGER\_SET\_POSITION**](ioctl-changer-set-position.md)
</dt> <dt>

[**IOCTL\_CHANGER\_EXCHANGE\_MEDIUM**](ioctl-changer-exchange-medium.md)
</dt> <dt>

[**IOCTL\_CHANGER\_MOVE\_MEDIUM**](ioctl-changer-move-medium.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MCD_INIT_DATA%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






