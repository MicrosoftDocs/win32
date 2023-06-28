---
title: Querying for Simple Rights Information
description: Querying for Simple Rights Information
ms.assetid: 21ed3fb2-35b8-478a-a17e-f6b4da08d50d
keywords:
- Windows Media Format SDK,querying for simple rights
- Windows Media Format SDK,simple rights queries
- digital rights management (DRM),querying for simple rights
- DRM (digital rights management),querying for simple rights
- digital rights management (DRM),simple rights queries
- DRM (digital rights management),simple rights queries
- DRM Client Extended APIs,querying for simple rights
- Client Extended APIs,querying for simple rights
- DRM Client Extended APIs,simple rights queries
- Client Extended APIs,simple rights queries
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Querying for Simple Rights Information

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Windows Media DRM Client Extended APIs enable you to quickly get simple information about whether protected content can be accessed for various actions.

The [**IWMDRMLicenseQuery::QueryActionAllowed**](iwmdrmlicensequery-queryactionallowed.md) method can be used to determine quickly whether an action is permitted by a license in the local license store. **QueryActionAllowed** has been optimized to be much faster than queries for similar information using the objects of the Windows Media Format SDK. However, this type of query aggregates the licenses in the local license store and should be used only for simple features, such as might be needed for user interface elements, for example displaying a permission indicator.

## Related topics

<dl> <dt>

[**Getting Information from Licenses in the Local License Store**](getting-information-from-licenses-in-the-local-license-store.md)
</dt> </dl>

 

 




