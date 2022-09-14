---
title: Silent License Acquisition
description: Silent License Acquisition
ms.assetid: 'bf88f1bb-0cbb-4c30-92e0-3d342977d67f'
keywords:
- Windows Media Format SDK,silent license acquisition
- Windows Media Format SDK,licenses
- digital rights management (DRM),silent license acquisition
- DRM (digital rights management),silent license acquisition
- digital rights management (DRM),licenses
- DRM (digital rights management),licenses
- DRM Client Extended APIs,silent license acquisition
- Client Extended APIs,silent license acquisition
- silent license acquisition
- licenses,silent license acquisition
ms.topic: article
ms.date: 05/31/2018
---

# Silent License Acquisition

Silent license acquisition requires only a single method call that handles all of the network communications with the license server asynchronously.

This type of license acquisition is usually used as a response to the end user trying to access protected content—for example, trying to play a protected file in a media player application. Because silent license acquisition gets the license with a single call, it cannot be used if additional input from the user, such as payment for the content, is required.

To perform silent license acquisition, use the following steps:

1.  Call the [**IWMDRMLicenseManagement::AcquireLicense**](iwmdrmlicensemanagement-acquirelicense.md) method. Pass in the DRM header from the protected file as the *bstrHeaderData* parameter. Specify what rights you want the license to grant in the *bstrActions* parameter. Finally, set the *dwFlags* parameter to WMDRM\_ACQUIRE\_LICENSE\_SILENT.
2.  Trap events for the [**IWMDRMLicenseManagement**](iwmdrmlicensemanagement.md) interface. When you receive the **MEWMDRMLicenseAcquisitionCompleted** event, check its return code by calling the **IMFMediaEvent::GetStatus** method, which is documented in the Media Foundation documentation. If the retrieved **HRESULT** value is a success code, then the license was successfully downloaded and is in the local license store ready for use.

## Related topics

<dl> <dt>

[**Acquiring Licenses**](acquiring-licenses.md)
</dt> <dt>

[**Using the Media Foundation Event Model**](using-the-media-foundation-model.md)
</dt> </dl>

 

 




