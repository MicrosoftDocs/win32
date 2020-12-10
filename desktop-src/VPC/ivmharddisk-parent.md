---
title: IVMHardDisk Parent property (VPCCOMInterfaces.h)
description: Parent of the differencing virtual hard disk.
ms.assetid: 9a400fa0-ee0d-4474-a410-82756ea544fe
keywords:
- Parent property Virtual PC
- Parent property Virtual PC , IVMHardDisk interface
- IVMHardDisk interface Virtual PC , Parent property
topic_type:
- apiref
api_name:
- IVMHardDisk.Parent
- IVMHardDisk.get_Parent
- IVMHardDisk.put_Parent
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMHardDisk::Parent property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves and sets the parent of the differencing virtual hard disk.

This property is read/write.

## Syntax


```C++
HRESULT put_Parent(
  [in]          IVMHardDisk *parent
);

HRESULT get_Parent(
  [out, retval] IVMHardDisk **parent
);
```



## Property value

Sets the [**IVMHardDisk**](ivmharddisk.md) object associated with the parent hard disk image.

## Error codes



| Name/value                                                                                                                                                                               | Meaning                                                                                                                                                                                                                                                                               |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                                                  | The operation was successful.<br/>                                                                                                                                                                                                                                              |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>                                    | The parameter is **NULL**.<br/>                                                                                                                                                                                                                                                 |
| <dl> <dt>S\_FALSE</dt> <dt>1</dt> </dl>                                               | This is not a differencing hard disk, so it has no parent.<br/>                                                                                                                                                                                                                 |
| <dl> <dt>HRESULT\_FROM\_WIN32(ERROR\_FILE\_NOT\_FOUND)</dt> <dt>0x80070002</dt> </dl> | The system could not find the parent virtual hard disk file.<br/>                                                                                                                                                                                                               |
| <dl> <dt>HRESULT\_FROM\_WIN32(ERROR\_PATH\_NOT\_FOUND)</dt> <dt>0x80070003</dt> </dl> | The system could not find the path to the parent virtual hard disk file.<br/>                                                                                                                                                                                                   |
| <dl> <dt>VM\_E\_HD\_IMAGE\_OPEN\_FAIL</dt> <dt>0xA004067C</dt> </dl>                  | An error occurred while attempting to open the current hard disk image file.<br/>                                                                                                                                                                                               |
| <dl> <dt>VM\_E\_HD\_IMAGE\_ACCESS</dt> <dt>0xA0040681</dt> </dl>                      | An error occurred while attempting to access the current hard disk image file.<br/>                                                                                                                                                                                             |
| <dl> <dt>VM\_E\_PARENT\_CHILD\_ID\_MISMATCH</dt> <dt>0xA0040685</dt> </dl>            | The virtual hard disk image located by the *parent* parameter does not have the same ID as the child disk image. Make sure the parent virtual hard disk image located by the *parent* parameter is the same image used to create the differencing virtual hard disk image.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl>                            | An unexpected error has occurred.<br/>                                                                                                                                                                                                                                          |



## Remarks

This property is only valid with differencing hard disk images.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMHardDisk is defined as ffa14ae6-48f5-42a4-8a22-186f2e5c7db0<br/>                |



## See also

<dl> <dt>

[**IVMHardDisk**](ivmharddisk.md)
</dt> </dl>

 

