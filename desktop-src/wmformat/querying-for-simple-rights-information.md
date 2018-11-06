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
ms.date: 05/31/2018
---

# Querying for Simple Rights Information

The Windows Media DRM Client Extended APIs enable you to quickly get simple information about whether protected content can be accessed for various actions.

The [**IWMDRMLicenseQuery::QueryActionAllowed**](iwmdrmlicensequery-queryactionallowed.md) method can be used to determine quickly whether an action is permitted by a license in the local license store. **QueryActionAllowed** has been optimized to be much faster than queries for similar information using the objects of the Windows Media Format SDK. However, this type of query aggregates the licenses in the local license store and should be used only for simple features, such as might be needed for user interface elements, for example displaying a permission indicator.

## Related topics

<dl> <dt>

[**Getting Information from Licenses in the Local License Store**](getting-information-from-licenses-in-the-local-license-store.md)
</dt> </dl>

 

 




