---
title: IVMDVDDrive SetBusLocation method (VPCCOMInterfaces.h)
description: Attaches the DVD drive to the specified bus location in the virtual machine.
ms.assetid: 765274b8-91bc-475a-ac4d-994b2425a421
keywords:
- SetBusLocation method Virtual PC
- SetBusLocation method Virtual PC , IVMDVDDrive interface
- IVMDVDDrive interface Virtual PC , SetBusLocation method
topic_type:
- apiref
api_name:
- IVMDVDDrive.SetBusLocation
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMDVDDrive::SetBusLocation method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Attaches the DVD drive to the specified bus location in the virtual machine.

## Syntax


```C++
HRESULT SetBusLocation(
  [in] long busNumber,
  [in] long deviceNumber
);
```



## Parameters

<dl> <dt>

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



| Return code/value                                                                                                                                                            | Description                                                                                                                             |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0</dt> </dl>                                  | The operation was successful.<br/>                                                                                                |
| <dl> <dt>**E\_INVALIDARG**</dt> <dt>0x80000003</dt> </dl>                 | The bus location specified is not valid.<br/>                                                                                     |
| <dl> <dt>**E\_FAIL**</dt> <dt>0x80004005</dt> </dl>                       | An unexpected error has occurred.<br/>                                                                                            |
| <dl> <dt>**VM\_E\_VM\_RUNNING\_OR\_SAVED**</dt> <dt>0xA004020B</dt> </dl> | The bus location cannot be set while the virtual machine is running or in a saved state.<br/>                                     |
| <dl> <dt>**VM\_E\_BUS\_LOC\_IN\_USE**</dt> </dl>                                                                      | Another device is already attached to the specified bus location.<br/>                                                            |
| <dl> <dt>**VM\_E\_DRIVE\_INVALID**</dt> <dt>0xA0040502</dt> </dl>         | The current drive could not be initialized.<br/>                                                                                  |
| <dl> <dt>**VM\_E\_VM\_UNKNOWN**</dt> <dt>0xA0040207</dt> </dl>            | The changes could not be written to the preferences file because the virtual machine for this drive could not be determined.<br/> |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> <dt>0x80020009</dt> </dl>            | An unexpected error has occurred.<br/>                                                                                            |



 

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

 

