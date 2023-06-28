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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Querying for Detailed Rights Information

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

By using the [**IWMDRMLicenseQuery::QueryLicenseState**](iwmdrmlicensequery-querylicensestate.md) method, you can obtain detailed information about the rights granted by licenses for a key ID. The information that you get from this method is aggregated from all licenses in the local license store that apply to the specified key ID.

**QueryLicenseState** uses the [**DRM\_LICENSE\_STATE\_DATA**](drmdrm-license-state-data.md) structure to display aggregate information about all the licenses for the specified key ID. This usage is different than by other objects in the Windows Media Format SDK.

## Related topics

<dl> <dt>

[**Getting Information from Licenses in the Local License Store**](getting-information-from-licenses-in-the-local-license-store.md)
</dt> </dl>

 

 




