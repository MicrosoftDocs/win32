---
title: Obtaining the Required DRM Library
description: Obtaining the Required DRM Library
ms.assetid: 7bd13b77-439e-40cf-99e8-b359247da74d
keywords:
- Windows Media Format SDK,obtaining required DRM libraries
- Advanced Systems Format (ASF),obtaining required DRM libraries
- ASF (Advanced Systems Format),obtaining required DRM libraries
- digital rights management (DRM),obtaining required libraries
- DRM (digital rights management),obtaining required libraries
- digital rights management (DRM),build information
- DRM (digital rights management),build information
- digital rights management (DRM),debugging information
- DRM (digital rights management),debugging information
- debugging DRM
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Obtaining the Required DRM Library

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

To create or play DRM-protected digital media files, your application must link to a static library that is provided in binary form by Microsoft. This library is sometimes called a stub library or "stublib" and it uniquely identifies your application.

In this documentation, the DRM library is referred to as "WMStubDRM.lib". The name of the library you receive will include an identifying number. To obtain this library, you must sign a license agreement with Microsoft. The terms of the agreement may differ depending on whether you request an evaluation license or a production license. For more information on the DRM licensing process, see the Windows Media Licensing Form at the [Microsoft Web site](https://www.microsoft.com/licensing/default).

The library that you receive has a DRM security level that depends on the type of license agreement you enter into. A DRM license can restrict applications with DRM components below a specified security level from accessing the file contents. This security level is not the same as the DRM individualization level, nor is it related to any of the numerical values of output protection levels (OPLs). The following table shows examples of DRM security levels for different players and portable devices.



| Security level | Players and portable devices                                                                                                                                                                                                                                                                                                   | Example                                                                                                                                                                                          |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 150            | Devices that do not support Windows Media DRM. DRM protection is removed when content is transferred to such a device.                                                                                                                                                                                                         | Devices that support Windows Media-based content but not protected content                                                                                                                       |
| 1,000          | Player applications based on the Windows Media Format 9.5 SDK or earlier that do not meet additional requirements for level 2000.Devices based on Windows Media Portable Device DRM v1.<br/> Devices based on Windows CE 4.2 and later.<br/>                                                                       | Windows Media Player 6.4, Windows Media Player 7Portable media devices that support Windows Media Portable Device DRM v1.<br/>                                                             |
| 2,000          | Player applications that are based on Windows Media Format 9 Series SDK or later, and that follow a stricter set of content protection guidelines than applications at level 1000.Devices based on Windows Media DRM 10 for Portable Devices.<br/> Devices based on Windows Media DRM 10 for Network Devices.<br/> | Windows Media Player 9 Series and laterPortable media devices that support Windows Media DRM 10 for Portable Devices<br/> Portable Media Center devices based on Windows Mobile<br/> |



 

## Build and Debugging Information

When you link to WMStubDRM.lib, do NOT link to wmvcore.lib. The DRM component will not work properly if the application links to both libraries.

A user breakpoint in the DRM component will prevent both debug and release versions of applications from accessing protected content when running inside the debugger. To troubleshoot DRM-related functions in your application, you must write your own trace routines that save information such as **HRESULT** values to some location such as a log file.

If you attempt to run a release version of an application on a system with a debug version of the SDK bits installed (or the other way around), you will encounter heap errors during playback of DRM version 7 content. Be sure to run debug applications over debug SDK bits, and release applications over release bits. The same problem will occur if you run a debug version of the SDK with an individualized DRM component (which is always a release build).

**Notes** DRM is not supported by the x64-based version of this SDK.

The WMStubDRM.lib files that are associated with the Windows Media Format 9.5 SDK can be used only with the components of Microsoft Visual Studio  .NET 2003. If you are using an older version of the stub library, there are no new restrictions for its use.

## Related topics

<dl> <dt>

[**Enabling DRM Support**](enabling-drm-support.md)
</dt> </dl>

 

 





