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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Silent License Acquisition

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 




