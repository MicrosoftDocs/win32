---
title: IVMVirtualMachine AddHardDiskConnection method
description: The AddHardDiskConnection method adds a new hard disk connection to the virtual machine.
ms.assetid: '706e1931-c1fb-460e-be02-872535761729'
keywords: ["AddHardDiskConnection method Virtual Server", "AddHardDiskConnection method Virtual Server , IVMVirtualMachine interface", "IVMVirtualMachine interface Virtual Server , AddHardDiskConnection method"]
topic_type:
- apiref
api_name:
- IVMVirtualMachine.AddHardDiskConnection
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMVirtualMachine::AddHardDiskConnection method

The **AddHardDiskConnection** method adds a new hard disk connection to the virtual machine.

## Syntax


```C++
HRESULT AddHardDiskConnection(
  [in]  BSTR                  hardDiskPath,
  [in]  VMDriveBusType        busType,
  [in]  long                  busNumber,
  [in]  long                  deviceNumber,
  [out] IVMHardDiskConnection **hardDiskConnection
);
```



## Parameters

<dl> <dt>

*hardDiskPath* \[in\]
</dt> <dd>

Full path specifying the virtual hard disk file to connect

</dd> <dt>

*busType* \[in\]
</dt> <dd>

Bus to attach the hard disk drive to.

</dd> <dt>

*busNumber* \[in\]
</dt> <dd>

Bus number to attach the hard disk to. For IDE, this number can be 0-1. For SCSI, this number is an index from 0 to the number returned by [**IVMSCSIControllerCollection::Count**](ivmscsicontrollercollection-count.md).

</dd> <dt>

*deviceNumber* \[in\]
</dt> <dd>

Device number to attach the hard disk to. For IDE, this number can be 0-1. For SCSI, this number can be 0-6.

</dd> <dt>

*hardDiskConnection* \[out\]
</dt> <dd>

A new [**IVMHardDiskConnection**](ivmharddiskconnection.md) object.

</dd> </dl>

## Return value

This method supports standard return values, as well as the following. For information on Virtual Server specific return values not listed below, see [**HRESULT Codes Specific to the Virtual Server**](hresult-codes-specific-to-the-virtual-server.md).



| Return code                                                                                                     | Description                                                                                                                                     |
|-----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt> **S\_OK**</dt> </dl>                           | The operation was successful.<br/>                                                                                                        |
| <dl> <dt> **E\_POINTER**</dt> </dl>                      | The *hardDiskPath* parameter is **NULL**, empty, or not valid; the *busType*, *busNumber*, or *deviceNumber* parameter is not valid.<br/> |
| <dl> <dt> **E\_POINTER**</dt> </dl>                      | The *hardDiskConnection* parameter is **NULL**.<br/>                                                                                      |
| <dl> <dt>**E\_FILE\_NOT\_FOUND**</dt> </dl>              | The system cannot find the file specified by the *hardDiskPath* parameter.<br/>                                                           |
| <dl> <dt>**E\_PATH\_NOT\_FOUND**</dt> </dl>              | The system cannot find the path specified by the *hardDiskPath* parameter.<br/>                                                           |
| <dl> <dt>**E\_INVALID\_NAME**</dt> </dl>                 | The *hardDiskPath* parameter contains an invalid character (one of "\*?&lt;&gt;/\|":").<br/>                                              |
| <dl> <dt>**E\_BAD\_PATHNAME**</dt> </dl>                 | The *hardDiskPath* parameter specifies an empty or relative path. An absolute path is required.<br/>                                      |
| <dl> <dt>**E\_BUFFER\_OVERFLOW**</dt> </dl>              | The path specified by the *hardDiskPath* parameter is too long. The path must be less than 260 characters.<br/>                           |
| <dl> <dt>**VM\_E\_VM\_UNKNOWN**</dt> </dl>               | The configuration is unknown.<br/>                                                                                                        |
| <dl> <dt>**VM\_E\_VM\_RUNNING**</dt> </dl>               | Virtual machine is running or saved.<br/>                                                                                                 |
| <dl> <dt> **VM\_E\_DRIVE\_BUS\_LOC\_IN\_USE**</dt> </dl> | The specified bus location is in use.<br/>                                                                                                |
| <dl> <dt>**E\_SHARING\_VIOLATION**</dt> </dl>            | The specified hard disk file is already connected to another bus location for this virtual machine.<br/>                                  |
| <dl> <dt> **DISP\_E\_EXCEPTION**</dt> </dl>              | An unexpected error has occurred.<br/>                                                                                                    |



 

## Remarks

You can only add a new hard disk connection to a stopped virtual machine.

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualMachine**](ivmvirtualmachine.md)
</dt> <dt>

[**VMDriveBusType**](vmdrivebustype.md)
</dt> </dl>

 

 





