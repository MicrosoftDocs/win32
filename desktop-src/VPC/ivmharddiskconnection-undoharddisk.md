---
title: IVMHardDiskConnection UndoHardDisk property (VPCCOMInterfaces.h)
description: Retrieves a hard disk object corresponding to this connection's undo disk image.
ms.assetid: 0daec200-0bda-44cf-b97d-b9a179cb63f8
keywords:
- UndoHardDisk property Virtual PC
- UndoHardDisk property Virtual PC , IVMHardDiskConnection interface
- IVMHardDiskConnection interface Virtual PC , UndoHardDisk property
topic_type:
- apiref
api_name:
- IVMHardDiskConnection.UndoHardDisk
- IVMHardDiskConnection.get_UndoHardDisk
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMHardDiskConnection::UndoHardDisk property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves a hard disk object corresponding to this connection's undo disk image.

This property is read-only.

## Syntax


```C++
HRESULT get_UndoHardDisk(
  [out, retval] IVMHardDisk **undoHardDisk
);
```



## Property value

An [**IVMHardDisk**](ivmharddisk.md) object that describes the undo hard disk associated with this connection.

## Error codes



| Name/value                                                                                                                                                                               | Meaning                                                                                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                                                  | The operation was successful.<br/>                                                                                                    |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl>                            | An unexpected error has occurred.<br/>                                                                                                |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>                                    | The parameter is **NULL** or not valid.<br/>                                                                                          |
| <dl> <dt>HRESULT\_FROM\_WIN32(ERROR\_FILE\_NOT\_FOUND)</dt> <dt>0x80070002</dt> </dl> | The undo disk for this connection was not found.<br/>                                                                                 |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> <dt>0xA0040207</dt> </dl>                            | The current virtual machine configuration is not valid.<br/>                                                                          |
| <dl> <dt>VM\_E\_DRIVE\_INVALID</dt> <dt>0xA0040502</dt> </dl>                         | The bus location for this connection has not been properly initialized, or the device at this location is not a valid hard disk.<br/> |



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

 

