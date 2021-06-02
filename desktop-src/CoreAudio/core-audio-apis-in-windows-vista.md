---
description: Core Audio APIs
ms.assetid: 87ca9a31-1bc8-47ea-be00-40159d30e189
title: Core Audio APIs
ms.topic: article
ms.date: 05/31/2018
ms.custom: project-verbatim
---

# Core Audio APIs

> [!NOTE]
> For code examples, see [SDK samples that use the core audio APIs](./sdk-samples-that-use-the-core-audio-apis.md).

This documentation provides information about core audio application programming interfaces (APIs) for the Microsoft Windows family of operating systems. It provides guidelines for software developers to follow in developing applications that use the core audio APIs in Windows Vista. These APIs were new in Windows Vista and are not available in earlier versions of Windows.

The core audio APIs provide the means for audio applications to access audio endpoint devices such as headphones and microphones. The core audio APIs serve as the foundation for higher-level audio APIs such as Microsoft DirectSound and the Windows multimedia **waveXxx** functions. Most applications communicate with the higher-level APIs, but some applications with special requirements might need to communicate directly with the core audio APIs.

Starting with Windows 7, the existing APIs have been improved and new APIs have been added to support new scenarios. The stream and session management APIs have been improved so that the application can now enumerate and get extended control over the audio session. By using the new APIs, the application can implement a custom stream attenuation experience. New device-related APIs provide access to the driver properties of the endpoint devices.

This documentation includes the following sections.

| Section                                                                    | Description                                                                       |
|----------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| [About the Windows Core Audio APIs](about-the-windows-core-audio-apis.md) | Provides an overview of the Windows core audio APIs and describes basic concepts. |
| [Programming Guide](programming-guide.md)                                 | Describes the key features of the core audio APIs and how to use them.            |
| [Programming Reference](programming-reference.md)                         | Provides C++ reference information for the core audio APIs.                       |

## Related topics

[Media Technologies for Windows](/previous-versions/bg125389(v=msdn.10))

[SDK samples that use the core audio APIs](./sdk-samples-that-use-the-core-audio-apis.md)