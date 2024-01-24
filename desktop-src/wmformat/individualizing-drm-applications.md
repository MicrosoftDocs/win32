---
title: Individualizing DRM Applications
description: Individualizing DRM Applications
ms.assetid: 8d87c663-bc54-4928-9eee-d09c358e61f8
keywords:
- Windows Media Format SDK,individualizing DRM applications
- Windows Media Format SDK,application individualizing
- Advanced Systems Format (ASF),individualizing DRM applications
- ASF (Advanced Systems Format),individualizing DRM applications
- Advanced Systems Format (ASF),application individualizing
- ASF (Advanced Systems Format),application individualizing
- digital rights management (DRM),individualizing applications
- DRM (digital rights management),individualizing applications
- digital rights management (DRM),application individualizing
- DRM (digital rights management),application individualizing
- application individualizing
- individualizing DRM applications
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Individualizing DRM Applications

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

To increase security, the DRM component of applications can be *individualized*. An individualized application is one that has received an upgrade to its DRM components that differentiates it from all other copies of the same application. Content owners can require that their protected files be played only on an application that has been individualized.

The individualization process starts when the application contacts the Microsoft Individualization Service, which then installs a security upgrade on the user's computer. Because the Individualization Service handles information from the user, you must display the Microsoft privacy policy or provide a link to that page at the Microsoft Web site: <https://privacy.microsoft.com/privacystatement>.

Individualization can be accomplished in different ways. For example, individualization can take place when a user plays a protected file. The license request is sent to the [*Windows Media License Service*](wmformat-glossary.md), which inspects the certificate of the application requesting the [*license*](wmformat-glossary.md). If the DRM component of the application has not been individualized, Windows Media License Service refuses to issue the license, because it is the policy of Windows Media License Service to issue licenses only to individualized players. The application can then notify the user that the application must be upgraded. If the user agrees, a security upgrade is provided to individualize the DRM component of the application.

For a better user experience, you can initiate the individualization process as a security upgrade step during setup; then the user is not interrupted to get a security upgrade while trying to play a protected file. You can also actively encourage individualization by adding a **Security Upgrade** menu command or button to the application.

> [!Note]  
> DRM is not supported by the x64-based version of this SDK.

 

## Related topics

<dl> <dt>

[**Digital Rights Management Features**](digital-rights-management-features.md)
</dt> <dt>

[**Enabling DRM Support**](enabling-drm-support.md)
</dt> </dl>

 

 




