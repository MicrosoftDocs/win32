---
title: IVMFloppyDriveEvents OnMediaInsert method (VPCCOMInterfaces.h)
description: Receives notification that media has been inserted into the drive. | IVMFloppyDriveEvents OnMediaInsert method (VPCCOMInterfaces.h)
ms.assetid: 922fca14-8ef6-4d3d-b1b6-72d2ea83e8ef
keywords:
- OnMediaInsert method Virtual PC
- OnMediaInsert method Virtual PC , IVMFloppyDriveEvents interface
- IVMFloppyDriveEvents interface Virtual PC , OnMediaInsert method
topic_type:
- apiref
api_name:
- IVMFloppyDriveEvents.OnMediaInsert
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMFloppyDriveEvents::OnMediaInsert method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Receives notification that media has been inserted into the drive.

## Syntax


```C++
HRESULT OnMediaInsert(
  [in] BSTR mediaPath
);
```



## Parameters

<dl> <dt>

*mediaPath* \[in\]
</dt> <dd>

The host drive letter, or path, to floppy image.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

This method is called when media (a floppy disk image or a floppy disk in a host drive) is inserted. The client program must implement this interface method to receive notification of the vmFloppyDriveEvent\_OnMediaInsert event originating from [**IVMFloppyDrive**](ivmfloppydrive.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | DIID\_IVMFloppyDriveEvents is defined as a9ed3401-4e09-4177-86ec-a13bf9fa7d4e<br/>      |



## See also

<dl> <dt>

[**IVMFloppyDriveEvents**](ivmfloppydriveevents.md)
</dt> </dl>

 

