---
title: IVMFloppyDriveCollection Item property (VPCCOMInterfaces.h)
description: Floppy object that corresponds to the specified index.
ms.assetid: 068a1f1c-ae84-4689-b68a-ce25b68fc06b
keywords:
- Item property Virtual PC
- Item property Virtual PC , IVMFloppyDriveCollection interface
- IVMFloppyDriveCollection interface Virtual PC , Item property
topic_type:
- apiref
api_name:
- IVMFloppyDriveCollection.Item
- IVMFloppyDriveCollection.get_Item
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMFloppyDriveCollection::Item property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves the floppy object that corresponds to the specified index.

This property is read-only.

## Syntax


```C++
HRESULT get_Item(
  [in]          long           index,
  [out, retval] IVMFloppyDrive **floppyDrive
);
```



## Property value

The [**IVMFloppyDrive**](ivmfloppydrive.md) object.

## Error codes



| Name/value                                                                                                                                                    | Meaning                                                                                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                       | The operation was successful.<br/>                                                      |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>         | The *floppyDrive* parameter is **NULL**.<br/>                                           |
| <dl> <dt>DISP\_E\_BADINDEX</dt> <dt>0x8002000B</dt> </dl>  | The index of the requested item does not correspond to an item in this collection.<br/> |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> <dt>0xA0040207</dt> </dl> | The configuration is unknown.<br/>                                                      |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl> | An unexpected error has occurred.<br/>                                                  |



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMFloppyDriveCollection is defined as 8ba70a25-f698-4ee5-85ce-3cc93a925516<br/>   |



## See also

<dl> <dt>

[**IVMFloppyDrive**](ivmfloppydrive.md)
</dt> <dt>

[**IVMFloppyDriveCollection**](ivmfloppydrivecollection.md)
</dt> </dl>

 

