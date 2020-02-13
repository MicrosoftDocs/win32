---
title: Implementing License Revocation
description: Implementing License Revocation
ms.assetid: 50ecfeaa-89cd-4788-a25a-ee0ae8973bf0
keywords:
- Windows Media Format SDK,implementing license revocation
- Windows Media Format SDK,license revocation
- Windows Media Format SDK,revocation of licenses
- Advanced Systems Format (ASF),implementing license revocation
- ASF (Advanced Systems Format),implementing license revocation
- Advanced Systems Format (ASF),license revocation
- ASF (Advanced Systems Format),license revocation
- Advanced Systems Format (ASF),revocation of licenses
- ASF (Advanced Systems Format),revocation of licenses
- digital rights management (DRM),implementing license revocation
- DRM (digital rights management),implementing license revocation
- digital rights management (DRM),license revocation
- DRM (digital rights management),license revocation
- digital rights management (DRM),revocation of licenses
- DRM (digital rights management),revocation of licenses
- license revocation,implementing
ms.topic: article
ms.date: 05/31/2018
---

# Implementing License Revocation

The Windows Media Rights Manager 10 SDK includes a feature called license revocation. This feature enables license servers to request that licenses be removed from the client computer. The Windows Media Format SDK provides methods that process revocation messages and remove the licenses from the local license store.

The license revocation process is initiated by a service provided by the license issuer. Your application can host this service, or it can be a Web application. In either case, your application must be able to receive a license challenge created by the service.

To remove licenses from the license store, perform the following steps:

1.  Upon receiving a license challenge from the license issuer, call the [**WMCreateLicenseRevocationAgent**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreatelicenserevocationagent) function to create a license revocation agent object and obtain a pointer to the [**IWMLicenseRevocationAgent**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmlicenserevocationagent) interface.
2.  Call the [**IWMLicenseRevocationAgent::GetLRBChallenge**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmlicenserevocationagent-getlrbchallenge) method to generate the challenge response.
3.  Send the challenge response back to the license service component from which you received the challenge.
4.  The license service component sends a signed license revocation blob (LRB) to your application. When you receive it, call the [**IWMLicenseRevocationAgent::ProcessLRB**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmlicenserevocationagent-processlrb) method. **ProcessLRB** creates an acknowledgement message that you must send back to the license service to verify that the licenses were removed.

> [!Note]  
> DRM is not supported by the x64-based version of this SDK.

 

## Related topics

<dl> <dt>

[**Enabling DRM Support**](enabling-drm-support.md)
</dt> <dt>

[**IWMLicenseRevocationAgent Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmlicenserevocationagent)
</dt> </dl>

 

 




