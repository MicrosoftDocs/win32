---
title: Non-Silent License Acquisition
description: Non-Silent License Acquisition
ms.assetid: 3b3fce53-9202-4e55-82d5-7c70ea833087
keywords:
- Windows Media Format SDK,non-silent license acquisition
- Windows Media Format SDK,licenses
- digital rights management (DRM),non-silent license acquisition
- DRM (digital rights management),non-silent license acquisition
- digital rights management (DRM),licenses
- DRM (digital rights management),licenses
- DRM Client Extended APIs,non-silent license acquisition
- Client Extended APIs,non-silent license acquisition
- non-silent license acquisition
- licenses,non-silent license acquisition
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Non-Silent License Acquisition

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Non-silent license acquisition enables the license provider to interact with the end user through a Web page, as an intermediate step in the license acquisition process. Non-silent license acquisition is initiated in response to a user trying to access protected content.

To perform non-silent license acquisition, use the following steps:

1.  Call the [**IWMDRMLicenseManagement::AcquireLicense**](iwmdrmlicensemanagement-acquirelicense.md) method. Pass in the DRM header from the protected file as the *bstrHeaderData* parameter. Specify what rights you want the license to grant in the *bstrActions* parameter. Finally, set the *dwFlags* parameter to WMDRM\_ACQUIRE\_LICENSE\_NONSILENT.
2.  Trap events for the **IWMDRMLicenseManagement** interface. When you receive the **MEWMDRMLicenseAcquisitionCompleted** event, get its associated value by calling **IMFMediaEvent::GetValue**. The value should be of type VT\_UNKNOWN, a pointer to an **IUnknown** interface.
3.  Call the **QueryInterface** method of the **IUnknown** interface retrieved in step 2 to get the [**IWMDRMNonSilentLicenseAquisition**](iwmdrmnonsilentlicenseaquisition.md) interface.
4.  Call [**IWMDRMNonSilentLicenseAquisition::GetChallenge**](iwmdrmnonsilentlicenseaquisition-getchallenge.md) to retrieve the license challenge. Also call [**IWMDRMNonSilentLicenseAquisition::GetURL**](iwmdrmnonsilentlicenseaquisition-geturl.md) if you do not have the URL of the license server already.
5.  Send the challenge to the Web page specified by the URL.

## Related topics

<dl> <dt>

[**Acquiring Licenses**](acquiring-licenses.md)
</dt> <dt>

[**Using the Media Foundation Event Model**](using-the-media-foundation-model.md)
</dt> </dl>

 

 




