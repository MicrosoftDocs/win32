---
title: Writing to a File
description: Writing to a File
ms.assetid: a01f93e9-e0fe-4e81-aa9f-62cdca7bce4a
keywords:
- AVIFileWriteData function
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Writing to a File

\[The feature associated with this page, [AVIFile Functions and Macros](/windows/win32/multimedia/avifile-functions-and-macros), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader). **Source Reader** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** instead of **AVIFile Functions and Macros**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You can write supplementary information to a file that has been opened with write privileges by using the [**AVIFileWriteData**](/windows/desktop/api/Vfw/nf-vfw-avifilewritedata) function. This function copies the information from an application-supplied buffer and places it in one or more chunks in the file. The "INFO" chunk is a common RIFF chunk type in which the function stores supplementary information. For a description of RIFF files and their data chunks, see [Resource Interchange File Format Services](resource-interchange-file-format-services.md).

 

 




