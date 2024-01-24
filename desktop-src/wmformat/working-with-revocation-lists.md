---
title: Working with Revocation Lists
description: Working with Revocation Lists
ms.assetid: 4463abb5-f48f-484f-b837-512313572c0a
keywords:
- Windows Media Format SDK,revocation lists
- Advanced Systems Format (ASF),revocation lists
- ASF (Advanced Systems Format),revocation lists
- revocation lists
- digital rights management (DRM),revocation lists
- DRM (digital rights management),revocation lists
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Working with Revocation Lists

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

To respond to security breaches and to ensure that player applications known to be broken or compromised cannot play or use protected files, each license that is issued contains a revocation list. A revocation list contains the application certificates of all those player applications known to be broken or corrupted. When a new license is received, the DRM component of the player application checks for a revocation list. If one is found that is newer than the one currently on the computer, the newer list is stored. The next time the consumer plays a protected ASF file, the DRM component compares the player application to the revocation list. If the player application is revoked, the DRM component sends an error message to the application.

Player applications can receive a revocation error message in the following scenarios:

-   The error message is received after the application calls the [**IWMDRMReader::AcquireLicense**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmreader-acquirelicense) method for a protected file. The call fails with the **HRESULT** code NS\_E\_DRM\_APPCERT\_REVOKED, which is supplied to the **OnStatus** callback function with WMT\_ACQUIRE\_LICENSE status. If this **HRESULT** code is ignored, errors will continue to occur.
-   The error message is received when the application creates the DRM-enabled reader and calls the [**IWMReader::Open**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreader-open) method for a protected file. The call fails with the **HRESULT** code NS\_E\_DRM\_APPCERT\_REVOKED, which is supplied to the [**IWMStatusCallback::OnStatus**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmstatuscallback-onstatus) callback method with WMT\_OPENED status. When a player application receives this error message, the application should notify end users and provide a way for them to restore functionality to their player. For example, the application can open a URL where end users can download an upgrade for the compromised application.

**Note** DRM is not supported by the x64-based version of this SDK.

## Related topics

<dl> <dt>

[**Digital Rights Management Features**](digital-rights-management-features.md)
</dt> <dt>

[**Handling License Acquisition Events**](handling-license-acquisition-events.md)
</dt> </dl>

 

 




