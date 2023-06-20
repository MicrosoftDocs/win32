---
title: Introduction for Users of the Windows Media Format SDK
description: Introduction for Users of the Windows Media Format SDK
ms.assetid: 21f06c43-213e-4fbf-a33a-c1890b4b40ce
keywords:
- Windows Media Format SDK,DRM Client Extended APIs
- Windows Media Format SDK,Client Extended APIs
- Windows Media Format SDK,Extended APIs
- Windows Media Format SDK,APIs
- Windows Media Format SDK,digital rights management (DRM)
- digital rights management (DRM),Client Extended APIs
- DRM (digital rights management),Client Extended APIs
- digital rights management (DRM),Extended APIs
- DRM (digital rights management),Extended APIs
- digital rights management (DRM),APIs
- DRM (digital rights management),APIs
- DRM Client Extended APIs,about
- Client Extended APIs,about
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Introduction for Users of the Windows Media Format SDK

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Much of the functionality provided by the Windows Media DRM Client Extended APIs is the same as the functionality provided by the objects of the Windows Media Format SDK. The Windows Media Format SDK provides developers with the objects needed to create, access, and manipulate media files that use the Advanced Systems Format (ASF) file structure. Because Windows Media DRM is intended to protect ASF files, client-side DRM functionality was included in the Windows Media Format SDK.

The Windows Media DRM Client Extended APIs are being released in conjunction with Microsoft's next-generation digital media platform, the Microsoft Media Foundation SDK. Media Foundation will include ASF functionality that overlaps some of the features of the Windows Media Format SDK. Because there are now two Microsoft SDKs that manipulate ASF files, the client-side DRM functionality is being separated from the Windows Media Format SDK into the Windows Media DRM Client Extended APIs. These APIs can be accessed by users of both the Windows Media Format SDK and the Media Foundation SDK. At present, these APIs are included as part of the Windows Media Format SDK installation package and are documented as part of the Windows Media Format SDK. However, the Windows Media DRM Client Extended APIs are implemented in their own library and have their own header file. After installing the Windows Media Format SDK, these APIs can be used one their own, without including any Windows Media Format SDK headers or libraries in your application.

If you develop applications that use the Windows Media Format SDK you must decide whether to use the DRM functionality that SDK provides, or to use the Windows Media DRM Client Extended APIs. While many of the features of these two SDKs are very similar, the Windows Media DRM Client Extended APIs offer the following features not available to users of the older DRM routines:

-   Ability to import content protected by a third-party rights management system.
-   Ability to export content protected by Windows Media DRM to a third-party rights management system.
-   Direct enumeration of licenses in the license store.
-   Simple, aggregated rights querying based on key ID (no need to load the media file).
-   Ability to renew revoked components by using the standard Media Foundation interface, **IMFContentEnabler**.

## Related topics

<dl> <dt>

[**About the Windows Media DRM Client Extended APIs**](about-the-windows-media-drm-client-extended-apis.md)
</dt> </dl>

 

 




