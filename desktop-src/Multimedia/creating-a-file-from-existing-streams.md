---
title: Creating a File from Existing Streams
description: Creating a File from Existing Streams
ms.assetid: 5149a766-7809-42b7-8e5c-b67b847b9218
keywords:
- AVISave function
- AVISaveV function
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Creating a File from Existing Streams

\[The feature associated with this page, [AVIFile Functions and Macros](/windows/win32/multimedia/avifile-functions-and-macros), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader). **Source Reader** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** instead of **AVIFile Functions and Macros**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

One way to create a file that contains data streams is to combine existing streams into a new file. The streams that provide data for the new file can reside in memory or in one or more files.

You can build a file from several streams by using the [**AVISave**](/windows/desktop/api/Vfw/nf-vfw-avisavea) function. This function creates a file and writes the data streams specified in its calling sequence to the file. The calling sequence for **AVISave** uses a variable number of arguments that include interfaces for the streams combined in the new file.

You can also combine data streams in a new file by using the [**AVISaveV**](/windows/desktop/api/Vfw/nf-vfw-avisaveva) function. This function provides the same functionality as **AVISave**, but when you use **AVISaveV**, your application specifies the data streams as an array, not as a variable number of arguments.

You can create a dialog box in which the user can select compression settings for the new file by using the [**AVISaveOptions**](/windows/desktop/api/Vfw/nf-vfw-avisaveoptions) function. The dialog box displays the current compression settings and lets the user edit them. Compression setting changes are stored in an [**AVICOMPRESSOPTIONS**](/windows/desktop/api/Vfw/ns-vfw-avicompressoptions) structure.

You can also include a callback function with [**AVISave**](/windows/desktop/api/Vfw/nf-vfw-avisavea) and [**AVISaveV**](/windows/desktop/api/Vfw/nf-vfw-avisaveva) that your application can use to display the progress of writing the file and, if needed, let the user cancel the save operation. You can include the address of the callback function in the calling sequence of **AVISave** or **AVISaveV**.

You can let the user select a filename for the new file by using the [**GetSaveFileNamePreview**](/windows/desktop/api/Vfw/nf-vfw-getsavefilenamepreviewa) function. This function displays the Save As dialog box in which the user can preview the first stream (normally the video stream) of an AVI file.

You can create a file interface pointer (and a virtual file) for a group of streams by using the [**AVIMakeFileFromStreams**](/windows/desktop/api/Vfw/nf-vfw-avimakefilefromstreams) function. Other AVIFile functions can use the file interface pointer returned by this function to access the streams in the virtual file. After you finish using the virtual file, delete the file interface pointer by using the [**AVIFileRelease**](/windows/desktop/api/Vfw/nf-vfw-avifilerelease) function.

> [!Note]  
> To minimize image and audio degradation, avoid compressing an AVI file more than once. Combine uncompressed pieces of video in your editing system and then compress the final product. For information about compression options, see [Video Compression Manager](video-compression-manager.md).

 

 

 




