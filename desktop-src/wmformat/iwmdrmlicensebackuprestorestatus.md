---
title: IWMDRMLicenseBackupRestoreStatus interface
description: The IWMDRMLicenseBackupRestoreStatus interface provides a method to retrieve detailed status information about a license backup or restore operation.This interface is delivered with progress events generated during license backup and restore operations.
ms.assetid: fbcd059f-13d9-4edb-8946-b55c9da6dca4
keywords:
- IWMDRMLicenseBackupRestoreStatus interface windows Media Format
- IWMDRMLicenseBackupRestoreStatus interface windows Media Format , described
topic_type:
- apiref
api_name:
- IWMDRMLicenseBackupRestoreStatus
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IWMDRMLicenseBackupRestoreStatus interface

The **IWMDRMLicenseBackupRestoreStatus** interface provides a method to retrieve detailed status information about a license backup or restore operation.

This interface is delivered with progress events generated during license backup and restore operations. Several **MEWMDRMLicenseBackupProgress** events are generated during license backup, each of which has an accompanying instance of this interface. The same is true of **MEWMDRMLicenseRestoreProgress** events, which are generated during license restoration.

To retrieve a pointer to an instance of the **IWMDRMLicenseBackupRestoreStatus** interface, you must first call the **IMFMediaEvent::GetValue** method of the progress event. The value you retrieve from the event is a pointer to the **IUnknown** interface of the object that implements the **IWMDRMLicenseBackupRestoreStatus** interface.

## Members

The **IWMDRMLicenseBackupRestoreStatus** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IWMDRMLicenseBackupRestoreStatus** also has these types of members:

-   [Methods](#methods)

### Methods

The **IWMDRMLicenseBackupRestoreStatus** interface has these methods.



| Method                                                          | Description                                                                                   |
|:----------------------------------------------------------------|:----------------------------------------------------------------------------------------------|
| [**GetStatus**](iwmdrmlicensebackuprestorestatus-getstatus.md) | Retrieves detailed status information about a license backup or restore operation.<br/> |



 

## See also

<dl> <dt>

[**Interfaces**](drm-interfaces.md)
</dt> </dl>

 

