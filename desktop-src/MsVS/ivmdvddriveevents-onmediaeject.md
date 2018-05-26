---
title: IVMDVDDriveEvents OnMediaEject method
description: Called when media has been ejected from the drive.
ms.assetid: a7ed86ae-0739-4be1-b7b3-2baf18e64e5a
keywords:
- OnMediaEject method Virtual Server
- OnMediaEject method Virtual Server , IVMDVDDriveEvents interface
- IVMDVDDriveEvents interface Virtual Server , OnMediaEject method
- OnMediaEject method Virtual Server , VMDVDDrive interface
- VMDVDDrive interface Virtual Server , OnMediaEject method
topic_type:
- apiref
api_name:
- IVMDVDDriveEvents.OnMediaEject
- VMDVDDrive.OnMediaEject
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IVMDVDDriveEvents::OnMediaEject method

The **OnMediaEject** method is called when media has been ejected from the drive.

## Syntax


```C++
HRESULT OnMediaEject(
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

A [**32-bit value**](hresult-codes-specific-to-the-virtual-server.md) that describes an error or warning.

## Remarks

This method is called when media (an ISO image or a disc in a host drive) is ejected. The client program must implement this interface method to receive notification of the [**vmDVDDriveEvent\_OnEject**](vmdvddriveevent.md) event originating from [**IVMDVDDrive**](ivmdvddrive.md).

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMDVDDriveEvents**](ivmdvddriveevents.md)
</dt> </dl>

 

 





