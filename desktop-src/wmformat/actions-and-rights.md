---
title: Actions and Rights
description: Actions and Rights
ms.assetid: 711c6a04-6c40-4ea5-8c4f-91d000286b7b
keywords:
- Windows Media Format SDK,digital rights management (DRM)
- Windows Media Format SDK,DRM licenses
- Windows Media Format SDK,licenses for DRM
- digital rights management (DRM),actions
- DRM (digital rights management),actions
- digital rights management (DRM),rights
- DRM (digital rights management),rights
- digital rights management (DRM),licenses
- DRM (digital rights management),licenses
- licenses,DRM
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Actions and Rights

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

When a file is protected by using Windows Media DRM, its use is completely restricted. Licenses can be issued to enable a user to use the content in specific ways. Each way in which a user might use the content is described by an action. For example, playing a file on a computer is an action.

A license that enables a given action is said to grant a right. For example, a license can grant the right to play content on a computer.

Actions and rights refer to the same ways of using content. The difference is that the action refers to the use while the right refers to the permission. Despite this distinction, the words action and right are often used interchangeably in this documentation and in other documents that describe Windows Media DRM.

The actions governed by Windows Media DRM rights are listed in the [Rights Constants](rights-constants.md) section of this documentation.

Certain methods of the Windows Media DRM Client Extended APIs use different constants to refer to the basic DRM rights. For example, the [**IWMDRMLicenseQuery::QueryLicenseState**](iwmdrmlicensequery-querylicensestate.md) method uses a set of strings specific to license states. Even though these constants are defining different strings than the basic rights constants, they refer to the same rights in the license.

## Related topics

<dl> <dt>

[**Concepts**](drmconcepts.md)
</dt> </dl>

 

 




