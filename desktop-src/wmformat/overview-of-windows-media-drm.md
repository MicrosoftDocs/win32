---
title: Overview of Windows Media DRM
description: Overview of Windows Media DRM
ms.assetid: 944b5e0b-649f-4955-8df3-4762726b9893
keywords:
- Windows Media Format SDK,digital rights management (DRM)
- Windows Media Format SDK,DRM licenses
- Windows Media Format SDK,licenses for DRM
- digital rights management (DRM),about
- DRM (digital rights management),about
- digital rights management (DRM),packaging Windows Media files
- DRM (digital rights management),packaging Windows Media files
- digital rights management (DRM),protected file licensing
- DRM (digital rights management),protected file licensing
- digital rights management (DRM),licenses
- DRM (digital rights management),licenses
- digital rights management (DRM),reading protected files
- DRM (digital rights management),reading protected files
- Advanced Systems Format (ASF),digital rights management (DRM)
- ASF (Advanced Systems Format),digital rights management (DRM)
- licenses,DRM
ms.topic: article
ms.date: 05/31/2018
---

# Overview of Windows Media DRM

Windows Media Digital Rights Management (DRM) is a system for protecting the content in Windows Media files so that unauthorized users cannot access it. There are three phases to the basic DRM cycle: packaging, licensing, and reading.

## Packaging Windows Media Files

Windows Media DRM is designed to work with Windows Media files. A Windows Media file is a file that conforms to the Advanced Systems Format (ASF) specification and only contains Audio and Video that has been compressed by using the Windows Media Audio and Video codecs.

When an ASF file is packaged, a DRM-specific section is added to the header. The DRM header contains a Key ID, which identifies the content for the purposes of licensing, and a license acquisition URL, which is the address of a Web page that can issue licenses to read the protected content. There is much more information that can be put in the DRM header, but it is optional. The DRM header is signed so that the packager can be verified.

The content in the ASF file is encrypted during the packing process. However, the following information in the packaged file is available even to clients that do not have a license:

-   Metadata that is stored in the ASF header.
-   Some metadata that is stored in the DRM header (for example, you can always get the license acquisition URL).

## Licensing Protected Files

For a packaged file to be read, a license must be issued to the client computer. A license is a set of data that describes the conditions under which data in protected files can be read. Most often, a license is issued for a protected file in response to the user trying to perform some operation on the file. It is also possible, however, for a license issuer to deliver licenses to a client before it is explicitly requested. For more information about licenses, see [Licenses](licenses.md).

## Reading Data from Protected Files

When a user tries to perform an operation on a protected file (play, burn to CD, copy to a device, and so on), the application must check for licenses for the content on the client computer. If a valid license exists on the client computer, the operation can proceed. If there isn't a license for the content, or if no license for the content that is on the client computer allows the requested action, then a license must be acquired.

## Related topics

<dl> <dt>

[**About the Windows Media DRM Client Extended APIs**](about-the-windows-media-drm-client-extended-apis.md)
</dt> </dl>

 

 




