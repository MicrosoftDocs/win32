---
title: IVMDVDDrive SetBusLocation method
description: The SetBusLocation method attaches the DVD drive to the specified bus location in the virtual machine.
ms.assetid: '291bcdd4-f593-4521-9d35-76361033573d'
keywords: ["SetBusLocation method Virtual Server", "SetBusLocation method Virtual Server , IVMDVDDrive interface", "IVMDVDDrive interface Virtual Server , SetBusLocation method", "SetBusLocation method Virtual Server , VMDVDDrive interface", "VMDVDDrive interface Virtual Server , SetBusLocation method"]
topic_type:
- apiref
api_name:
- IVMDVDDrive.SetBusLocation
- VMDVDDrive.SetBusLocation
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMDVDDrive::SetBusLocation method

The **SetBusLocation** method attaches the DVD drive to the specified bus location in the virtual machine.

## Syntax


```C++
HRESULT SetBusLocation(
  [in] VMDriveBusType busType,
  [in] long           busNumber,
  [in] long           deviceNumber
);
```



## Parameters

<dl> <dt>

*busType* \[in\]
</dt> <dd>

Enumerated value designating the type of bus (IDE or SCSI) to which this drive is to be attached.

</dd> <dt>

*busNumber* \[in\]
</dt> <dd>

The bus number to which this drive is to be attached. For example, on an IDE bus, this number would represent whether to use the primary or secondary bus number.

</dd> <dt>

*deviceNumber* \[in\]
</dt> <dd>

The device number to which this drive is to be attached. For example, on an IDE bus, this number would represent whether to use the primary or secondary device location.

</dd> </dl>

## Return value

This method can return one of these values.

This method supports standard return values, as well as the following. For information on Virtual Server specific return values not listed below, see [**HRESULT Codes Specific to the Virtual Server**](hresult-codes-specific-to-the-virtual-server.md).



| Return code                                                                                                    | Description                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                           | The operation was successful.<br/>                                                                                                |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                   | The bus location specified is not valid.<br/>                                                                                     |
| <dl> <dt>**VM\_E\_VM\_RUNNING**</dt> </dl>              | The bus location cannot be set while the virtual machine is running or in a saved state.<br/>                                     |
| <dl> <dt>**VM\_E\_DRIVE\_BUS\_LOC\_IN\_USE**</dt> </dl> | Another device is already attached to the specified bus location.<br/>                                                            |
| <dl> <dt>**VM\_E\_DRIVE\_INVALID**</dt> </dl>           | The current drive could not be initialized.<br/>                                                                                  |
| <dl> <dt>**VM\_E\_VM\_UNKNOWN**</dt> </dl>              | The changes could not be written to the preferences file because the virtual machine for this drive could not be determined.<br/> |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> </dl>              | An unexpected error occurred.<br/>                                                                                                |



 

## Remarks

Virtual Server does not support attaching a DVD drive to a SCSI bus. A **E\_INVALIDARG** error will be returned if the *busType* argument is set to **vmDriveBusType\_SCSI**.

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMDVDDrive**](ivmdvddrive.md)
</dt> <dt>

[**VMDriveBusType**](vmdrivebustype.md)
</dt> </dl>

 

 





