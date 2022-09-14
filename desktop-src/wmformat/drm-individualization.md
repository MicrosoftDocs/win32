---
title: DRM Individualization
description: DRM Individualization
ms.assetid: 8f129bc1-3db9-4b41-9d60-daff037237ff
keywords:
- Windows Media Format SDK,DRM individualization
- digital rights management (DRM),individualization
- DRM (digital rights management),individualization
- individualization of DRM
ms.topic: article
ms.date: 05/31/2018
---

# DRM Individualization

Owners of protected content may require users to upgrade some of the digital rights management (DRM) components included in the Windows Media Format SDK before accessing their content. If a user accepts the upgrade, an individualized version of a security file (one unique to their computer) will be downloaded from a Microsoft Web site. If the user declines the upgrade, they will not be able to access the content; however, they will still be able to access unprotected content and protected content that does not require the upgrade. Performing a security upgrade helps increase the level of protection offered by DRM.

Individualization can be done either at setup time or when an application first encounters a protected ASF file that requires it. Because this process modifies a user's system components, the application must notify the user and obtain their informed consent before performing the upgrade. Microsoft Windows Media Player, for example, shows a dialog box with the following text:

**Security Upgrade Required**

**The owner of the protected content you are trying to access requires you to first upgrade some of the Microsoft digital rights management (DRM) components on your computer.**

**Click OK to upgrade your DRM components.**

**Details:**

**When you click OK, a unique identifier and a DRM security file are sent to a Microsoft service on the Internet. The file is replaced with a customized version that contains your unique identifier. This increases the level of protection provided by DRM.**

Any application that supports individualization should use the same or similar wording. For more information on Microsoft's Privacy Policy, see the [Privacy Statement](privacy-statement.md) section of this documentation.

> [!Note]  
> DRM is not supported by the x64-based version of this SDK.

 

## Related topics

<dl> <dt>

[**Digital Rights Management Features**](digital-rights-management-features.md)
</dt> <dt>

[**Individualizing DRM Applications**](individualizing-drm-applications.md)
</dt> </dl>

 

 




