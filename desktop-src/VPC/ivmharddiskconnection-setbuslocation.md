---
title: IVMHardDiskConnection SetBusLocation method (VPCCOMInterfaces.h)
description: Sets the bus location to which this hard disk is attached.
ms.assetid: 0aa303ae-d8bf-4d38-94ab-bdbb4e744c7b
keywords:
- SetBusLocation method Virtual PC
- SetBusLocation method Virtual PC , IVMHardDiskConnection interface
- IVMHardDiskConnection interface Virtual PC , SetBusLocation method
topic_type:
- apiref
api_name:
- IVMHardDiskConnection.SetBusLocation
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMHardDiskConnection::SetBusLocation method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Sets the bus location to which this hard disk is attached.

## Syntax


```C++
HRESULT SetBusLocation(
  [in] long vmBusNumber,
  [in] long vmDeviceNumber
);
```



## Parameters

<dl> <dt>

*vmBusNumber* \[in\]
</dt> <dd>

The bus number to be used.

</dd> <dt>

*vmDeviceNumber* \[in\]
</dt> <dd>

The device number to be used.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code/value                                                                                                                                                               | Description                                                                                                 |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0</dt> </dl>                                     | The operation was successful.<br/>                                                                    |
| <dl> <dt>**E\_INVALIDARG**</dt> <dt>0x80000003</dt> </dl>                    | The bus location specified is not valid.<br/>                                                         |
| <dl> <dt>**VM\_E\_VM\_RUNNING\_OR\_SAVED**</dt> <dt>0xA004020B</dt> </dl>    | The bus location could not be set because the virtual machine is in a running or saved state.<br/>    |
| <dl> <dt>**VM\_E\_DRIVE\_BUS\_LOC\_IN\_USE**</dt> <dt>0xA00400503</dt> </dl> | The bus location could not be set because another device is currently attached to this location.<br/> |
| <dl> <dt>**VM\_E\_DRIVE\_INVALID**</dt> <dt>0xA0040502</dt> </dl>            | The current drive is not valid.<br/>                                                                  |
| <dl> <dt>**VM\_E\_VM\_UNKNOWN**</dt> <dt>0xA0040207</dt> </dl>               | The current virtual machine is not valid.<br/>                                                        |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> <dt>0x80020009</dt> </dl>               | An unexpected error has occurred.<br/>                                                                |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMHardDiskconnection is defined as aefa36a5-463a-46ae-9e6c-a1fb4e12e671<br/>      |



## See also

<dl> <dt>

[**IVMHardDiskConnection**](ivmharddiskconnection.md)
</dt> </dl>

 

