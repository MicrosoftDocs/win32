---
title: Library Files and Compiler Settings
description: Library Files and Compiler Settings
ms.assetid: ae043b1e-1d61-4d5a-be98-54f899fa24ed
keywords:
- Windows Media Format SDK,library files
- Windows Media Format SDK,compiler settings
- Windows Media Format SDK,header files
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Library Files and Compiler Settings

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

To develop an application using the Windows Media Format SDK, you must use Microsoft Visual C++ version 6.0 or later. The only programming languages appropriate for development are C++ and C.

The contents of the various header files included with this SDK are described in the following table.



| Header file                 | Description                                                                                                                                                                                                                                         |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| asferr.h                    | Defines error codes relating to ASF file operations. This header is included in wmsdk.h.                                                                                                                                                            |
| drmexternals.h              | Defines structures, enumerations, and constants used for digital rights management (DRM). Include this header when writing an application that uses DRM.                                                                                            |
| dshowasf.h                  | Defines the Microsoft DirectShow QASF filters. Include this header when writing a DirectShow application that creates or reads ASF files. For more information, see [DirectShow and Windows Media](directshow-and-windows-media.md).               |
| msnetobj.h                  | Defines the [**IRMGetLicense**](irmgetlicense.md) interface, which is implemented in one of the runtime libraries installed with the Windows Media Format SDK.                                                                                     |
| nserror.h                   | Defines error codes for Windows Media Technologies. Only a subset of these error codes are relevant to the Windows Media Format SDK. This header is included in wmsdk.h.                                                                            |
| wmdxva.h                    | Includes other headers and definitions needed to enable Microsoft DirectX Video Acceleration for playback of Windows Media based content. For more information, see [Enabling DirectX Video Acceleration](enabling-directx-video-acceleration.md). |
| wmnetsourcecreator.h        | Contains information needed to create network source plug-ins.                                                                                                                                                                                      |
| wmsbuffer.h                 | Defines the interfaces used by buffer objects. Include this header when creating your own buffers for file reading.                                                                                                                                 |
| wmsdk.h                     | The main header for applications using the Windows Media Format SDK. This header contains no definitions, but includes asferr.h, nserror.h, windows.h, and wmsdkidl.h. Include this header for all applications using this SDK.                     |
| wmsdkidl.h                  | Defines the interfaces, functions, structures, enumerations, and constants for most of the objects of the Windows Media Format SDK. This header is included in wmsdk.h.                                                                             |
| wmsinternaladminnetsource.h | Defines the interfaces of network source plug-ins.                                                                                                                                                                                                  |
| wmsysprf.h                  | Defines the constants for the system profiles. Include this header in applications that load system profiles by identifier.                                                                                                                         |



 

To use the Windows Media Format SDK, your compiler must be properly configured. The configuration is different for building in debug mode than for release mode. Configure your setting according to the following table. All these setting are configured in the Project Settings dialog box. To get to the dialog box, select **Settings** from the **Project** menu.



| Setting                                                                 | Debug value                                                                              | Release value                                                                           |
|-------------------------------------------------------------------------|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| (C/C++ tab, Category = Code Generation) Use run-time library            | Debug Multithreaded DLL                                                                  | Multithreaded DLL                                                                       |
| (Link tab, Category = General) Ignore all default libraries (check box) | Selected                                                                                 | Selected                                                                                |
| (Link tab, Category = General) Object/library modules                   | Include Msvcrtd.lib and Wmvcore.lib.Do not include Libc.lib or any variation.<br/> | Include Msvcrt.lib and Wmvcore.lib.Do not include Libc.lib or any variation.<br/> |



 

If you are using Microsoft Visual Studio .NET, the settings have been changed to different locations, as shown in the following table. All of these settings are configured in the **Property Pages** dialog box. To get to the dialog box, right-click on your project in the **Solution Explorer** pane and select **Properties** from the context menu.



| Setting                                                                  | Debug Value                                                                              | Release value                                                                           |
|--------------------------------------------------------------------------|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| (Configuration Properties / C/C++ / Code Generation) Runtime Library     | Multi-threaded Debug DLL (/MDd)                                                          | Multi-threaded DLL (/MD)                                                                |
| (Configuration Properties / Linker / Input) Additional Dependencies      | Include Msvcrtd.lib and Wmvcore.lib.Do not include Libc.lib or any variation.<br/> | Include Msvcrt.lib and Wmvcore.lib.Do not include Libc.lib or any variation.<br/> |
| (Configuration Properties / Linker / Input) Ignore All Default Libraries | Yes                                                                                      | Yes                                                                                     |



 

If you want to delay the loading of Wmvcore.dll, or any other DLL, use the link option /DELAYLOAD in Microsoft Visual C++ 6.0, or Delay Loaded DLLs in Microsoft Visual C++ .NET.

Additionally, you need to include the directories for the libraries and headers of the Windows Media Format SDK. To find the directory settings for Visual C++ 6.0, on the **Tools** menu, click **Options**, and then click the **Directories** tab. When using Visual C++ .NET, click **Options** on the **Tools** menu, and then select Projects / VC++ Directories in the options list. Add directories as shown in the following table. If you changed the installation directory for the Windows Media Format SDK, your path will be different.



| Directory type | Default path                 |
|----------------|------------------------------|
| Include files  | C:\\WMSDK\\WMFSDK11\\include |
| Library files  | C:\\WMSDK\\WMFSDK11\\lib     |



 

If you are using the Platform SDK then the default paths would appear as follows:



| Directory type | Default path                                              |
|----------------|-----------------------------------------------------------|
| Include files  | C:\\Program Files\\Microsoft SDsK\\Windows\\v6.0\\Include |
| Library files  | C:\\Program Files\\Microsoft SDsK\\Windows\\v6.0\\Lib     |



 

Before calling any of the creation functions, COM should be initialized with a call to **Coinitialize** or **CoinitializeEx**. Either the free threading model or the apartment threading model can be used, but the apartment threading model imposes threading restrictions on the application. For more information on the Microsoft Component Object Model (COM), see the COM page at the [Microsoft Web site](../com/the-component-object-model.md).

**Note** Applications that play or create files protected by Digital Rights Management (DRM) require an individualized static library that must be obtained separately from Microsoft. For more information, see the Windows Media Licensing Form at the [Microsoft Web site](https://www.microsoft.com/licensing/default). If you use the DRM library, you should not link to Wmvcore.lib.

## Related topics

<dl> <dt>

[**Getting Started**](getting-started.md)
</dt> </dl>

 

