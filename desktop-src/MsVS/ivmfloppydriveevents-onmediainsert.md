---
title: IVMFloppyDriveEvents OnMediaInsert method
description: Called when media has been inserted into the drive.
ms.assetid: 'b0fee3a8-3084-4cca-af1f-b00c168c9fad'
keywords: ["OnMediaInsert method Virtual Server", "OnMediaInsert method Virtual Server , IVMFloppyDriveEvents interface", "IVMFloppyDriveEvents interface Virtual Server , OnMediaInsert method", "OnMediaInsert method Virtual Server , VMFloppyDrive interface", "VMFloppyDrive interface Virtual Server , OnMediaInsert method"]
topic_type:
- apiref
api_name:
- IVMFloppyDriveEvents.OnMediaInsert
- VMFloppyDrive.OnMediaInsert
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMFloppyDriveEvents::OnMediaInsert method

The **OnMediaInsert** method is called when media has been inserted into the drive.

## Syntax


```C++
HRESULT OnMediaInsert(
  [in] BSTR     mediaPath
);
```



## Parameters

<dl> <dt>

 *mediaPath* \[in\]
</dt> <dd>

The host drive letter, or path, to floppy image.

</dd> </dl>

## Return value

A [**32-bit value**](hresult-codes-specific-to-the-virtual-server.md) that describes an error or warning.

## Remarks

This method is called when media (a floppy disk image or a floppy disk in a host drive) is inserted. The client program must implement this interface method to receive notification of the [**vmFloppyDriveEvent\_OnMediaInsert**](vmfloppydriveevent.md) event originating from [**IVMFloppyDrive**](ivmfloppydrive.md).

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMFloppyDriveEvents**](ivmfloppydriveevents.md)
</dt> </dl>

 

 





