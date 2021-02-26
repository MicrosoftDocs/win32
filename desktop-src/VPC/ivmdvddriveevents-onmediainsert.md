---
title: IVMDVDDriveEvents OnMediaInsert method (VPCCOMInterfaces.h)
description: Receives notification that media has been inserted into the drive. | IVMDVDDriveEvents OnMediaInsert method (VPCCOMInterfaces.h)
ms.assetid: a246e2dd-638e-4d2f-9089-74771cd8bb2b
keywords:
- OnMediaInsert method Virtual PC
- OnMediaInsert method Virtual PC , IVMDVDDriveEvents interface
- IVMDVDDriveEvents interface Virtual PC , OnMediaInsert method
topic_type:
- apiref
api_name:
- IVMDVDDriveEvents.OnMediaInsert
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMDVDDriveEvents::OnMediaInsert method

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

The host drive letter, or path, to the ISO image.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

This method is called when media (an ISO image or a disc in a host drive) is inserted. The client program must implement this interface method to receive notification of the vmDVDDriveEvent\_OnInsert event originating from [**IVMDVDDrive**](ivmdvddrive.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | DIID\_IVMDVDDriveEvents is defined as c2a7d8e9-e76c-4eb8-94f7-71a5122d249b<br/>         |



## See also

<dl> <dt>

[**IVMDVDDriveEvents**](ivmdvddriveevents.md)
</dt> </dl>

 

