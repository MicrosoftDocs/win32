---
title: IVMDVDDrive BusNumber property (VPCCOMInterfaces.h)
description: Retrieves the bus number to which this device is attached.
ms.assetid: 8edc94da-22bc-4141-a6c7-1b18cca754fc
keywords:
- BusNumber property Virtual PC
- BusNumber property Virtual PC , IVMDVDDrive interface
- IVMDVDDrive interface Virtual PC , BusNumber property
topic_type:
- apiref
api_name:
- IVMDVDDrive.BusNumber
- IVMDVDDrive.get_BusNumber
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMDVDDrive::BusNumber property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves the bus number to which this device is attached.

This property is read-only.

## Syntax


```C++
HRESULT get_BusNumber(
  [out, retval] long *vmBusNumber
);
```



## Property value

The bus number. For example, on an IDE bus, this value would represent either the primary or secondary location.

## Error codes



| Name/value                                                                                                                                                       | Meaning                                                                           |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                          | The operation was successful.<br/>                                          |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>            | The parameter is **NULL**.<br/>                                             |
| <dl> <dt>VM\_E\_DRIVE\_INVALID</dt> <dt>0xA0040502</dt> </dl> | The bus location for this DVD drive has not been properly initialized.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl>    | An unexpected error has occurred.<br/>                                      |



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMDVDDrive is defined as b96328f6-6732-437d-a00d-ffa47e43971c<br/>                |



## See also

<dl> <dt>

[**IVMDVDDrive**](ivmdvddrive.md)
</dt> </dl>

 

