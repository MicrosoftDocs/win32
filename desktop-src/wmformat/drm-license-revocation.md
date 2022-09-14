---
title: License Revocation (Microsoft Windows Media DRM Client)
description: License Revocation (Microsoft Windows Media DRM Client)
ms.assetid: 615ddddf-4f2f-400d-9c4d-ff3a2851d699
keywords:
- Windows Media Format SDK,licenses
- Windows Media Format SDK,license revocation
- digital rights management (DRM),licenses
- DRM (digital rights management),licenses
- digital rights management (DRM),license revocation
- DRM (digital rights management),license revocation
- DRM Client Extended APIs,licenses
- Client Extended APIs,licenses
- DRM Client Extended APIs,license revocation
- Client Extended APIs,license revocation
- licenses,revocation
- license revocation,about
ms.topic: article
ms.date: 05/31/2018
---

# License Revocation (Microsoft Windows Media DRM Client)

License revocation refers to the removal of licenses from a local license store. A common scenario for license revocation occurs when a service provider, such as a music subscription service, must deactivate the service on a user's computer.

The license revocation process is initiated by a service provided by the license issuer. Your application can host this service or it can be a Web application. In either case, your application must be able to receive a license challenge created by the service.

To remove licenses from the license store, do the following:

1.  Upon receiving a license challenge from the license issuer, create a revocation challenge using the [**IWMDRMLicenseManagement::CreateLicenseRevocationChallenge**](iwmdrmlicensemanagement-createlicenserevocationchallenge.md) method. This method will allocate a buffer containing a revocation challenge data, which is passed to your application through the *ppbChallengeOutput* parameter.
2.  Send the license revocation challenge to a license revocation service. The server will generate a license revocation BLOB (LRB) in response.
3.  Remove the license from the local store using the [**IWMDRMLicenseManagement::ProcessLicenseRevocationResponse**](iwmdrmlicensemanagement-processlicenserevocationresponse.md) method, passing the LRB returned by license server.
4.  Deallocate the buffer allocated by **CreateLicenseRevocationChallenge** by using the **CoTaskMemFree** function.

For more information on how license revocation works or on how to write a revocation service, see [Implementing License Revocation](/docs/?url=%2flibrary%2fwmrm10%2fhtm%2fhowlicenserevokationworks.asp).

## Related topics

<dl> <dt>

[**Enabling DRM Support**](enabling-drm-support.md)
</dt> <dt>

[**Local License Store**](local-license-store.md)
</dt> <dt>

[**Programming Guide**](drm-programming-guide.md)
</dt> </dl>

 

 
