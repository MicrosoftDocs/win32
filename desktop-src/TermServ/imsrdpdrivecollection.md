---
title: IMsRdpDriveCollection interface
description: Represents a collection of drive objects.
ms.assetid: 26926b85-021d-4678-845f-93ba62b2b4a3
ms.tgt_platform: multiple
keywords:
- IMsRdpDriveCollection interface Remote Desktop Services
- IMsRdpDriveCollection interface Remote Desktop Services , described
topic_type:
- apiref
api_name:
- IMsRdpDriveCollection
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpDriveCollection interface

Represents a collection of drive objects.

## Members

The **IMsRdpDriveCollection** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IMsRdpDriveCollection** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IMsRdpDriveCollection** interface has these methods.



| Method                                                     | Description                                                 |
|:-----------------------------------------------------------|:------------------------------------------------------------|
| [**RescanDrives**](imsrdpdrivecollection-rescandrives.md) | Refreshes the list of objects in the collection.<br/> |



 

### Properties

The **IMsRdpDriveCollection** interface has these properties.



| Property                                                              | Access type          | Description                                                  |
|:----------------------------------------------------------------------|:---------------------|:-------------------------------------------------------------|
| [**DriveByIndex**](imsrdpdrivecollection-drivebyindex.md)<br/> | Read-only<br/> | Retrieves the drive at the specified index.<br/>       |
| [**DriveCount**](imsrdpdrivecollection-drivecount.md)<br/>     | Read-only<br/> | Retrieves the count of objects in the collection.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                           |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl>   |
| IID<br/>                      | IID\_IMsRdpDriveCollection is defined as 7ff17599-da2c-4677-ad35-f60c04fe1585<br/> |



## See also

<dl> <dt>

[Remote Desktop Web Connection Reference](remote-desktop-web-connection-reference.md)
</dt> <dt>

[**IMsRdpDrive**](imsrdpdrive.md)
</dt> </dl>

 

