---
title: Project Considerations
description: Project Considerations
ms.assetid: aebe2886-0af0-443a-a5be-651f11936639
keywords:
- Windows Media Format SDK,project considerations
- Advanced Systems Format (ASF),project considerations
- ASF (Advanced Systems Format),project considerations
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Project Considerations

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You must ensure that the end user can properly run applications that you create with the Windows Media Format SDK. This section describes two things you must consider when distributing applications, file name extensions and software redistribution.

You must use the correct file name extensions for any files created with your applications. Using proper file name extensions makes it easier for end users to recognize ASF files and prevents confusion when decoding files.

You must provide any redistributables that are required to run your applications. Without the correct redistributables, users will not be able to use your applications.

The following sections describe file name extensions and software redistribution in detail.



| Section                                                                      | Description                                                                                                     |
|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| [File Name Extension Guidelines](file-name-extension-guidelines.md)         | Provides information about the file name extensions you should use for ASF files that your program creates.     |
| [Software Redistribution](software-redistribution.md)                       | Describes the redistributables for the Windows Media Format SDK and how to include them with your applications. |
| [Registering Application Dependency](registering-application-dependency.md) | Describes how to register your application as being dependent on the Windows Media Format SDK runtime.          |



 

 

 




