---
title: IWMDRMNonSilentLicenseAquisition interface
description: The IWMDRMNonSilentLicenseAquisition interface provides methods that enable license acquisition requiring user intervention.This interface can be obtained by performing non-silent license acquisition.
ms.assetid: 57dc3daa-d457-49b0-b589-a72ba180e75e
keywords:
- IWMDRMNonSilentLicenseAquisition interface windows Media Format
- IWMDRMNonSilentLicenseAquisition interface windows Media Format , described
topic_type:
- apiref
api_name:
- IWMDRMNonSilentLicenseAquisition
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IWMDRMNonSilentLicenseAquisition interface

The **IWMDRMNonSilentLicenseAquisition** interface provides methods that enable license acquisition requiring user intervention.

This interface can be obtained by performing non-silent license acquisition. After you call [**IWMDRMLicenseManagement::AcquireLicense**](iwmdrmlicensemanagement-acquirelicense.md) an **MEWMDRMLicenseAcquisitionCompleted** event will be generated. Call the **IMFMediaEvent::GetValue** method of the event to get a pointer to an **IUnknown** interface that can be queried for a pointer to an instance of this interface.

## Members

The **IWMDRMNonSilentLicenseAquisition** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IWMDRMNonSilentLicenseAquisition** also has these types of members:

-   [Methods](#methods)

### Methods

The **IWMDRMNonSilentLicenseAquisition** interface has these methods.



| Method                                                                | Description                                                                             |
|:----------------------------------------------------------------------|:----------------------------------------------------------------------------------------|
| [**GetChallenge**](iwmdrmnonsilentlicenseaquisition-getchallenge.md) | Retrieves the license challenge that should be posted to the license server.<br/> |
| [**GetURL**](iwmdrmnonsilentlicenseaquisition-geturl.md)             | Retrieves the URL to which the license challenge should be posted.<br/>           |



 

## See also

<dl> <dt>

[**Interfaces**](drm-interfaces.md)
</dt> <dt>

[**Non-Silent License Acquisition**](non-silent-license-acquisition.md)
</dt> </dl>

 

