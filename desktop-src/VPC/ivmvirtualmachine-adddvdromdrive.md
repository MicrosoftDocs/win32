---
title: IVMVirtualMachine AddDVDROMDrive method (VPCCOMInterfaces.h)
description: Adds a new CD or DVD drive to the virtual machine.
ms.assetid: d39f2728-6146-42ed-b67f-6586566a7209
keywords:
- AddDVDROMDrive method Virtual PC
- AddDVDROMDrive method Virtual PC , IVMVirtualMachine interface
- IVMVirtualMachine interface Virtual PC , AddDVDROMDrive method
topic_type:
- apiref
api_name:
- IVMVirtualMachine.AddDVDROMDrive
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualMachine::AddDVDROMDrive method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Adds a new CD or DVD drive to the virtual machine.

## Syntax


```C++
HRESULT AddDVDROMDrive(
  [in]          long        busNumber,
  [in]          long        deviceNumber,
  [out, retval] IVMDVDDrive **dvdDrive
);
```



## Parameters

<dl> <dt>

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

*dvdDrive* \[out, retval\]
</dt> <dd>

An [**IVMDVDDrive**](ivmdvddrive.md) object.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code/value                                                                                                                                                               | Description                                                    |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0</dt> </dl>                                     | The operation was successful.<br/>                       |
| <dl> <dt>**E\_POINTER**</dt> <dt>0x80004003</dt> </dl>                       | The *dvdDrive* parameter is **NULL**.<br/>               |
| <dl> <dt>**E\_INVALIDARG**</dt> <dt>0x80000003</dt> </dl>                    | A parameter is not valid.<br/>                           |
| <dl> <dt>**VM\_E\_VM\_UNKNOWN**</dt> <dt>0xA0040207</dt> </dl>               | The configuration is unknown.<br/>                       |
| <dl> <dt>**VM\_E\_VM\_RUNNING\_OR\_SAVED**</dt> <dt>0xA004020B</dt> </dl>    | The virtual machine is in a running or saved state.<br/> |
| <dl> <dt>**VM\_E\_DRIVE\_BUS\_LOC\_IN\_USE**</dt> <dt>0xA00400503</dt> </dl> | The specified bus location is in use.<br/>               |
| <dl> <dt>**VM\_E\_DRIVE\_INVALID**</dt> <dt>0xA0040502</dt> </dl>            | The drive specified is not valid.<br/>                   |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> <dt>0x80020009</dt> </dl>               | An unexpected error has occurred.<br/>                   |



 

## Remarks

You can only add a new CD or DVD drive to a stopped virtual machine.

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

 

