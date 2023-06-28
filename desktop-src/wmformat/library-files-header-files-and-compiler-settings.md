---
title: Library Files, Header Files, and Compiler Settings
description: Library Files, Header Files, and Compiler Settings
ms.assetid: 7563bb3a-7bea-4e0c-8205-a16b276c8d1e
keywords:
- Windows Media Format SDK,DRM library files
- Windows Media Format SDK,library files
- Windows Media Format SDK,DRM header files
- Windows Media Format SDK,header files
- Windows Media Format SDK,DRM compiler settings
- Windows Media Format SDK,compiler settings
- digital rights management (DRM),library files
- DRM (digital rights management),library files
- digital rights management (DRM),header files
- DRM (digital rights management),header files
- digital rights management (DRM),compiler settings
- DRM (digital rights management),compiler settings
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Library Files, Header Files, and Compiler Settings

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The programming components of the Windows Media DRM Client Extended APIs are defined in the wmdrmsdk.h header file, and implemented in the wmdrmsdk.lib and mfuuid.lib libraries.

Some of the functionality of the Windows Media DRM Client Extended APIs requires that you obtain a protected library from Microsoft. This library, called the stub library in this documentation, is specific to the recipient and specifies the application security level for your applications. The stub library replaces wmdrmsdk.lib; you should never link to both.

**Note** The DRM stub library is separate from the stub library used by the rest of the Windows Media Format SDK but is licensed using the same method.

**Note** The DRM stub library must be linked into your application after the library file msvcrt.lib to avoid linker errors.

The stub library contains an embedded certificate which can be revoked by Microsoft if you fail to comply with the terms and conditions of the license agreement.

Specific methods that require the stub library are labeled in the documentation. If you try to use such a method without linking to the stub library, it will return an NS\_E\_DRM\_STUBLIB\_REQUIRED error.

The DRM subsystem can not be used in a debug build. If this is attempted, methods of the API will return the NS\_E\_DRM\_DEBUGGING\_NOT\_ALLOWED error.

## Related topics

<dl> <dt>

[**Getting Started**](drm-getting-started.md)
</dt> <dt>

[**Library Files and Compiler Settings**](library-files-and-compiler-settings.md)
</dt> <dt>

[**Obtaining the Required DRM Library**](obtaining-the-required-drm-library.md)
</dt> </dl>

 

 




