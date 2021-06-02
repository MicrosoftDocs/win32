---
title: IVMVirtualMachine AddHardDiskConnection method (VPCCOMInterfaces.h)
description: Adds a new hard disk connection to the virtual machine.
ms.assetid: 0f4e0666-2cfd-4c73-884d-6f8b43186c05
keywords:
- AddHardDiskConnection method Virtual PC
- AddHardDiskConnection method Virtual PC , IVMVirtualMachine interface
- IVMVirtualMachine interface Virtual PC , AddHardDiskConnection method
topic_type:
- apiref
api_name:
- IVMVirtualMachine.AddHardDiskConnection
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualMachine::AddHardDiskConnection method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Adds a new hard disk connection to the virtual machine (VM).

## Syntax


```C++
HRESULT AddHardDiskConnection(
  [in]          BSTR                  hardDiskPath,
  [in]          long                  busNumber,
  [in]          long                  deviceNumber,
  [out, retval] IVMHardDiskConnection **hardDiskConnection
);
```



## Parameters

<dl> <dt>

*hardDiskPath* \[in\]
</dt> <dd>

The full path of the virtual hard disk (VHD) file to connect.

</dd> <dt>

*busNumber* \[in\]
</dt> <dd>

The bus to which the drive will be attached.



| Value                                                                        | Meaning                                                  |
|------------------------------------------------------------------------------|----------------------------------------------------------|
| <dl> <dt>0</dt> </dl> | The drive will be attached to the first bus.<br/>  |
| <dl> <dt>1</dt> </dl> | The drive will be attached to the second bus.<br/> |



 

</dd> <dt>

*deviceNumber* \[in\]
</dt> <dd>

The device to which the drive will be attached.



| Value                                                                        | Meaning                                                                |
|------------------------------------------------------------------------------|------------------------------------------------------------------------|
| <dl> <dt>0</dt> </dl> | The drive will be attached to the first device on the bus.<br/>  |
| <dl> <dt>1</dt> </dl> | The drive will be attached to the second device on the bus.<br/> |



 

</dd> <dt>

*hardDiskConnection* \[out, retval\]
</dt> <dd>

An [**IVMHardDiskConnection**](ivmharddiskconnection.md) object.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code/value                                                                                                                                                                              | Description                                                                                                                                               |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0</dt> </dl>                                                    | The operation was successful.<br/>                                                                                                                  |
| <dl> <dt>**E\_POINTER**</dt> <dt>0x80004003</dt> </dl>                                      | The *hardDiskConnection* parameter is **NULL**.<br/>                                                                                                |
| <dl> <dt>**E\_INVALIDARG**</dt> <dt>0x80000003</dt> </dl>                                   | A *hardDiskPath* parameter is **NULL** or the *busNumber* or *deviceNumber* parameter is not valid.<br/>                                            |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_FILE\_NOT\_FOUND)**</dt> <dt>0x80070002</dt> </dl>   | The system cannot find the file specified by the *hardDiskPath* parameter.<br/>                                                                     |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_PATH\_NOT\_FOUND)**</dt> <dt>0x80070003</dt> </dl>   | The system cannot find the path specified by the *hardDiskPath* parameter.<br/>                                                                     |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_INVALID\_NAME)**</dt> <dt>0x8007007b</dt> </dl>      | The *hardDiskPath* parameter contains an invalid character (one of "\*?<>/\|":").<br/>                                                        |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_BAD\_PATHNAME)**</dt> <dt>0x800700a1</dt> </dl>      | The *hardDiskPath* parameter specifies an empty or relative path. An absolute path is required.<br/>                                                |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_BUFFER\_OVERFLOW)**</dt> <dt>0x8007006f</dt> </dl>   | The path specified by the *hardDiskPath* parameter is too long. The path must be less than 260 characters.<br/>                                     |
| <dl> <dt>**VM\_E\_VM\_UNKNOWN**</dt> <dt>0xA0040207</dt> </dl>                              | The configuration is unknown.<br/>                                                                                                                  |
| <dl> <dt>**VM\_E\_VM\_RUNNING\_OR\_SAVED**</dt> <dt>0xA004020B</dt> </dl>                   | The VM is in a running or saved state.<br/>                                                                                                         |
| <dl> <dt>**VM\_E\_DRIVE\_BUS\_LOC\_IN\_USE**</dt> <dt>0xA00400503</dt> </dl>                | The specified bus location is in use.<br/>                                                                                                          |
| <dl> <dt>**VM\_E\_INVALID\_HD\_FILE**</dt> <dt>0xA0040682</dt> </dl>                        | The VHD is greater than 127 GB and cannot be connected to the IDE bus.<br/>                                                                         |
| <dl> <dt>**VM\_E\_UNSUPPORTED\_HD\_DISK\_TYPE**</dt> <dt>0xA00400686</dt> </dl>             | The *hardDiskPath* parameter refers to a linked VHD or a differencing VHD to a linked VHD. Linked VHDs cannot be attached to virtual machines.<br/> |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_SHARING\_VIOLATION)**</dt> <dt>0x80070020</dt> </dl> | The specified VHD is already connected to another bus location for this VM.<br/>                                                                    |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> <dt>0x80020009</dt> </dl>                              | An unexpected error has occurred.<br/>                                                                                                              |



 

## Remarks

You can only add a new hard disk connection to a stopped virtual machine.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMVirtualMachine is defined as f7092aa1-33ed-4f78-a59f-c00adfc2edd7<br/>          |



## See also

<dl> <dt>

[**IVMVirtualMachine**](ivmvirtualmachine.md)
</dt> </dl>

 

