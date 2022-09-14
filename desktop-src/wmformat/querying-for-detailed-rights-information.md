---
title: Querying for Detailed Rights Information
description: Querying for Detailed Rights Information
ms.assetid: d9d5c299-1f61-41df-ab2c-7f4d196e9290
keywords:
- Windows Media Format SDK,querying for detailed rights
- Windows Media Format SDK,detailed rights queries
- digital rights management (DRM),querying for detailed rights
- DRM (digital rights management),querying for detailed rights
- digital rights management (DRM),detailed rights queries
- DRM (digital rights management),detailed rights queries
- DRM Client Extended APIs,querying for detailed rights
- Client Extended APIs,querying for detailed rights
- DRM Client Extended APIs,detailed rights queries
- Client Extended APIs,detailed rights queries
ms.topic: article
ms.date: 05/31/2018
---

# Querying for Detailed Rights Information

By using the [**IWMDRMLicenseQuery::QueryLicenseState**](iwmdrmlicensequery-querylicensestate.md) method, you can obtain detailed information about the rights granted by licenses for a key ID. The information that you get from this method is aggregated from all licenses in the local license store that apply to the specified key ID.

**QueryLicenseState** uses the [**DRM\_LICENSE\_STATE\_DATA**](drmdrm-license-state-data.md) structure to display aggregate information about all the licenses for the specified key ID. This usage is different than by other objects in the Windows Media Format SDK.

## Related topics

<dl> <dt>

[**Getting Information from Licenses in the Local License Store**](getting-information-from-licenses-in-the-local-license-store.md)
</dt> </dl>

 

 




