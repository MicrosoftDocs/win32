---
title: IWMDRMLicenseManagement interface
description: The IWMDRMLicenseManagement interface provides methods that perform general operations related to the local license store.To obtain an instance of this interface, call IWMDRMProvider CreateObject. Pass IID\_IWMDRMLicenseManagement as the riid parameter.
ms.assetid: 254bf54e-8ea6-4fd1-8abd-9d32539d529b
keywords:
- IWMDRMLicenseManagement interface windows Media Format
- IWMDRMLicenseManagement interface windows Media Format , described
topic_type:
- apiref
api_name:
- IWMDRMLicenseManagement
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IWMDRMLicenseManagement interface

The **IWMDRMLicenseManagement** interface provides methods that perform general operations related to the local license store.

To obtain an instance of this interface, call [**IWMDRMProvider::CreateObject**](iwmdrmprovider-createobject.md). Pass **IID\_IWMDRMLicenseManagement** as the *riid* parameter.

## Members

The **IWMDRMLicenseManagement** interface inherits from [**IWMDRMEventGenerator**](iwmdrmeventgenerator.md). **IWMDRMLicenseManagement** also has these types of members:

-   [Methods](#methods)

### Methods

The **IWMDRMLicenseManagement** interface has these methods.



| Method                                                                                               | Description                                                                                                             |
|:-----------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------|
| [**AcquireLicense**](iwmdrmlicensemanagement-acquirelicense.md)                                     | Asynchronously acquires a license from a specified URL.<br/>                                                      |
| [**BackupLicenses**](iwmdrmlicensemanagement-backuplicenses.md)                                     | Creates a backup of the licenses in the local license store.<br/>                                                 |
| [**CleanLicenseStore**](iwmdrmlicensemanagement-cleanlicensestore.md)                               | Removes marked licenses from the license store and defragments the store to improve performance.<br/>             |
| [**CreateLicenseEnumeration**](iwmdrmlicensemanagement-createlicenseenumeration.md)                 | Creates a license enumerator object populated with license information based on parameter values.<br/>            |
| [**CreateLicenseRevocationChallenge**](iwmdrmlicensemanagement-createlicenserevocationchallenge.md) | Generates a license revocation challenge.<br/>                                                                    |
| [**DeleteLicense**](iwmdrmlicensemanagement-deletelicense.md)                                       | Deletes a license from the temporary local license store.<br/>                                                    |
| [**MonitorLicenseAcquisition**](iwmdrmlicensemanagement-monitorlicenseacquisition.md)               | Initiates monitoring for a license acquisition process.<br/>                                                      |
| [**ProcessLicenseDeletionMessage**](iwmdrmlicensemanagement-processlicensedeletionmessage.md)       | Deletes a license that was imported for content originally protected with another content protection system.<br/> |
| [**ProcessLicenseRevocationResponse**](iwmdrmlicensemanagement-processlicenserevocationresponse.md) | Revokes licenses from the local license store.<br/>                                                               |
| [**RestoreLicenses**](iwmdrmlicensemanagement-restorelicenses.md)                                   | Restores previously backed up licenses.<br/>                                                                      |
| [**StoreLicense**](iwmdrmlicensemanagement-storelicense.md)                                         | Adds a license to the local license store.<br/>                                                                   |



 

## See also

<dl> <dt>

[**Interfaces**](drm-interfaces.md)
</dt> <dt>

[**IWMDRMEventGenerator**](iwmdrmeventgenerator.md)
</dt> </dl>

 

 





