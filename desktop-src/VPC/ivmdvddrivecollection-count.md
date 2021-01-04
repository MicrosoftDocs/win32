---
title: IVMDVDDriveCollection Count property (VPCCOMInterfaces.h)
description: Retrieves the number of CD and DVD drives in this collection.
ms.assetid: 22e39c42-1f98-4680-a97e-0d329dc608e2
keywords:
- Count property Virtual PC
- Count property Virtual PC , IVMDVDDriveCollection interface
- IVMDVDDriveCollection interface Virtual PC , Count property
topic_type:
- apiref
api_name:
- IVMDVDDriveCollection.Count
- IVMDVDDriveCollection.get_Count
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMDVDDriveCollection::Count property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves the number of CD and DVD drives in this collection.

This property is read-only.

## Syntax


```C++
HRESULT get_Count(
  [out, retval] long *count
);
```



## Property value

The number of CD and DVD drives.

## Error codes



| Name/value                                                                                                                                                    | Meaning                                      |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                       | The operation was successful.<br/>     |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>         | The parameter is **NULL**.<br/>        |
| <dl> <dt>E\_FAIL</dt> <dt>0x80004005</dt> </dl>            | An unexpected error has occurred.<br/> |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> <dt>0xA0040207</dt> </dl> | The configuration is unknown.<br/>     |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl> | An unexpected error has occurred.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMDVDDriveCollection is defined as bc86e297-e55f-4742-9614-ad11d3131f68<br/>      |



## See also

<dl> <dt>

[**IVMDVDDriveCollection**](ivmdvddrivecollection.md)
</dt> </dl>

 

