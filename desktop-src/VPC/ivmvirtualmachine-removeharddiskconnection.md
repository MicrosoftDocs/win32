---
title: IVMVirtualMachine RemoveHardDiskConnection method (VPCCOMInterfaces.h)
description: Removes the specified hard disk connection from the virtual machine.
ms.assetid: d31f2442-aae4-4987-9188-fd32778604a1
keywords:
- RemoveHardDiskConnection method Virtual PC
- RemoveHardDiskConnection method Virtual PC , IVMVirtualMachine interface
- IVMVirtualMachine interface Virtual PC , RemoveHardDiskConnection method
topic_type:
- apiref
api_name:
- IVMVirtualMachine.RemoveHardDiskConnection
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualMachine::RemoveHardDiskConnection method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Removes the specified hard disk connection from the virtual machine.

## Syntax


```C++
HRESULT RemoveHardDiskConnection(
  [in] IVMHardDiskConnection *hardDiskConnection
);
```



## Parameters

<dl> <dt>

*hardDiskConnection* \[in\]
</dt> <dd>

An [**IVMHardDiskConnection**](ivmharddiskconnection.md) object that represents the hard disk connection to be removed.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code/value                                                                                                                                                            | Description                                                           |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0</dt> </dl>                                  | The operation was successful.<br/>                              |
| <dl> <dt>**E\_POINTER**</dt> <dt>0x80004003</dt> </dl>                    | The parameter is **NULL**.<br/>                                 |
| <dl> <dt>**VM\_E\_VM\_UNKNOWN**</dt> <dt>0xA0040207</dt> </dl>            | The configuration is unknown.<br/>                              |
| <dl> <dt>**VM\_E\_VM\_RUNNING\_OR\_SAVED**</dt> <dt>0xA004020B</dt> </dl> | The virtual machine is in a running or saved state.<br/>        |
| <dl> <dt>**VM\_E\_DRIVE\_INVALID**</dt> <dt>0xA0040502</dt> </dl>         | The drive specified is not connected to this bus location.<br/> |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> <dt>0x80020009</dt> </dl>            | An unexpected error has occurred.<br/>                          |



 

## Remarks

You can only remove an existing hard disk connection from a stopped virtual machine. A list of connections currently attached to the virtual machine is obtained by enumerating the [**HardDiskConnections**](ivmvirtualmachine-harddiskconnections.md) property.

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

 

