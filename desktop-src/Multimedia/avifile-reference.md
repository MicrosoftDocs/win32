---
title: AVIFile Reference
description: AVIFile Reference
ms.assetid: 73532d83-89c2-4911-8558-ce110e9f0f95
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# AVIFile Reference

This section describes the functions, structures, and macros for applications using the AVIFile services. These elements are grouped as follows:

## AVIFile Library Operations

-   [**AVIFileInit**](/windows/win32/Vfw/nf-vfw-avifileinit?branch=master)
-   [**AVIFileExit**](/windows/win32/Vfw/nf-vfw-avifileexit?branch=master)

## Opening and Closing AVI Files

-   [**AVIFileOpen**](/windows/win32/Vfw/nf-vfw-avifileopen?branch=master)
-   [**AVIFileAddRef**](/windows/win32/Vfw/nf-vfw-avifileaddref?branch=master)
-   [**AVIFileRelease**](/windows/win32/Vfw/nf-vfw-avifilerelease?branch=master)
-   [**GetOpenFileNamePreview**](/windows/win32/Vfw/nf-vfw-getopenfilenamepreviewa?branch=master)

## Reading from a File

-   [**AVIFileInfo**](/windows/win32/Vfw/nf-vfw-avifileinfo?branch=master)
-   [**AVIFILEINFO**](/windows/win32/Vfw/ns-vfw-_avifileinfoa?branch=master)
-   [**AVIFileReadData**](/windows/win32/Vfw/nf-vfw-avifilereaddata?branch=master)

## Writing to a File

-   [**AVIFileWriteData**](/windows/win32/Vfw/nf-vfw-avifilewritedata?branch=master)

## Using the Clipboard

-   [**AVIPutFileOnClipboard**](/windows/win32/Vfw/nf-vfw-aviputfileonclipboard?branch=master)
-   [**AVIGetFromClipboard**](/windows/win32/Vfw/nf-vfw-avigetfromclipboard?branch=master)
-   [**AVIClearClipboard**](/windows/win32/Vfw/nf-vfw-aviclearclipboard?branch=master)

## Opening and Closing Streams

-   [**AVIFileGetStream**](/windows/win32/Vfw/nf-vfw-avifilegetstream?branch=master)
-   [**AVIStreamOpenFromFile**](/windows/win32/Vfw/nf-vfw-avistreamopenfromfilea?branch=master)
-   [**AVIStreamAddRef**](/windows/win32/Vfw/nf-vfw-avistreamaddref?branch=master)
-   [**AVIStreamRelease**](/windows/win32/Vfw/nf-vfw-avistreamrelease?branch=master)

## Reading Stream Information

-   [**AVISTREAMINFO**](/windows/win32/Vfw/ns-vfw-_avistreaminfoa?branch=master)
-   [**AVIStreamReadData**](/windows/win32/Vfw/nf-vfw-avistreamreaddata?branch=master)
-   [**AVIStreamDataSize**](/windows/win32/Vfw/nf-vfw-avistreamdatasize?branch=master)
-   [**AVIStreamReadFormat**](/windows/win32/Vfw/nf-vfw-avistreamreadformat?branch=master)
-   [**AVIStreamFormatSize**](/windows/win32/Vfw/nf-vfw-avistreamformatsize?branch=master)
-   [**AVIStreamRead**](/windows/win32/Vfw/nf-vfw-avistreamread?branch=master)
-   [**AVIStreamSampleSize**](/windows/win32/Vfw/nf-vfw-avistreamsamplesize?branch=master)
-   [**AVIStreamBeginStreaming**](/windows/win32/Vfw/nf-vfw-avistreambeginstreaming?branch=master)
-   [**AVIStreamEndStreaming**](/windows/win32/Vfw/nf-vfw-avistreamendstreaming?branch=master)

## Decompressing Video Data in a Stream

-   [**AVIStreamGetFrameOpen**](/windows/win32/Vfw/nf-vfw-avistreamgetframeopen?branch=master)
-   [**AVIStreamGetFrame**](/windows/win32/Vfw/nf-vfw-avistreamgetframe?branch=master)
-   [**AVIStreamGetFrameClose**](/windows/win32/Vfw/nf-vfw-avistreamgetframeclose?branch=master)

## Creating a File from Existing Streams

-   [**AVISave**](/windows/win32/Vfw/nf-vfw-avisavea?branch=master)
-   [**AVISaveV**](/windows/win32/Vfw/nf-vfw-avisaveva?branch=master)
-   [**AVISaveOptions**](/windows/win32/Vfw/nf-vfw-avisaveoptions?branch=master)
-   [**GetSaveFileNamePreview**](/windows/win32/Vfw/nf-vfw-getsavefilenamepreviewa?branch=master)
-   [**AVIMakeFileFromStreams**](/windows/win32/Vfw/nf-vfw-avimakefilefromstreams?branch=master)

## Writing Individual Streams

-   [**AVIFileCreateStream**](/windows/win32/Vfw/nf-vfw-avifilecreatestream?branch=master)
-   [**AVIStreamSetFormat**](/windows/win32/Vfw/nf-vfw-avistreamsetformat?branch=master)
-   [**AVIStreamWrite**](/windows/win32/Vfw/nf-vfw-avistreamwrite?branch=master)
-   [**AVIFileWriteData**](/windows/win32/Vfw/nf-vfw-avifilewritedata?branch=master)
-   [**AVIStreamWriteData**](/windows/win32/Vfw/nf-vfw-avistreamwritedata?branch=master)
-   [**AVIStreamRelease**](/windows/win32/Vfw/nf-vfw-avistreamrelease?branch=master)

## Finding the Starting Position in a Stream

-   [**AVIStreamStart**](/windows/win32/Vfw/nf-vfw-avistreamstart?branch=master)
-   [**AVIStreamStartTime**](/windows/win32/Vfw/nf-vfw-avistreamstarttime?branch=master)
-   [**AVIStreamLength**](/windows/win32/Vfw/nf-vfw-avistreamlength?branch=master)
-   [**AVIStreamLengthTime**](/windows/win32/Vfw/nf-vfw-avistreamlengthtime?branch=master)
-   [**AVIStreamFindSample**](/windows/win32/Vfw/nf-vfw-avistreamfindsample?branch=master)
-   [**AVIStreamEnd**](/windows/win32/Vfw/nf-vfw-avistreamend?branch=master)
-   [**AVIStreamEndTime**](/windows/win32/Vfw/nf-vfw-avistreamendtime?branch=master)

## Finding Sample and Key Frames

-   [**AVIStreamFindSample**](/windows/win32/Vfw/nf-vfw-avistreamfindsample?branch=master)
-   [**AVIStreamIsKeyFrame**](/windows/win32/Vfw/nf-vfw-avistreamiskeyframe?branch=master)
-   [**AVIStreamNearestKeyFrame**](/windows/win32/Vfw/nf-vfw-avistreamnearestkeyframe?branch=master)
-   [**AVIStreamNearestKeyFrameTime**](/windows/win32/Vfw/nf-vfw-avistreamnearestkeyframetime?branch=master)
-   [**AVIStreamNearestSample**](/windows/win32/Vfw/nf-vfw-avistreamnearestsample?branch=master)
-   [**AVIStreamNearestSampleTime**](/windows/win32/Vfw/nf-vfw-avistreamnearestsampletime?branch=master)
-   [**AVIStreamNextKeyFrame**](/windows/win32/Vfw/nf-vfw-avistreamnextkeyframe?branch=master)
-   [**AVIStreamNextKeyFrameTime**](/windows/win32/Vfw/nf-vfw-avistreamnextkeyframetime?branch=master)
-   [**AVIStreamNextSample**](/windows/win32/Vfw/nf-vfw-avistreamnextsample?branch=master)
-   [**AVIStreamNextSampleTime**](/windows/win32/Vfw/nf-vfw-avistreamnextsampletime?branch=master)
-   [**AVIStreamPrevKeyFrame**](/windows/win32/Vfw/nf-vfw-avistreamprevkeyframe?branch=master)
-   [**AVIStreamPrevKeyFrameTime**](/windows/win32/Vfw/nf-vfw-avistreamprevkeyframetime?branch=master)
-   [**AVIStreamPrevSample**](/windows/win32/Vfw/nf-vfw-avistreamprevsample?branch=master)
-   [**AVIStreamPrevSampleTime**](/windows/win32/Vfw/nf-vfw-avistreamprevsampletime?branch=master)
-   [**AVIStreamSampleToSample**](/windows/win32/Vfw/nf-vfw-avistreamsampletosample?branch=master)

## Switching Between Samples and Time

-   [**AVIStreamSampleToTime**](/windows/win32/Vfw/nf-vfw-avistreamsampletotime?branch=master)
-   [**AVIStreamTimeToSample**](/windows/win32/Vfw/nf-vfw-avistreamtimetosample?branch=master)

## Creating Temporary Streams

-   [**AVIStreamCreate**](/windows/win32/Vfw/nf-vfw-avistreamcreate?branch=master)
-   [**AVIMakeCompressedStream**](/windows/win32/Vfw/nf-vfw-avimakecompressedstream?branch=master)
-   [**AVIStreamRelease**](/windows/win32/Vfw/nf-vfw-avistreamrelease?branch=master)

## Editing AVI Streams

-   [**CreateEditableStream**](/windows/win32/Vfw/nf-vfw-createeditablestream?branch=master)
-   [**EditStreamCut**](/windows/win32/Vfw/nf-vfw-editstreamcut?branch=master)
-   [**EditStreamCopy**](/windows/win32/Vfw/nf-vfw-editstreamcopy?branch=master)
-   [**EditStreamPaste**](/windows/win32/Vfw/nf-vfw-editstreampaste?branch=master)
-   [**EditStreamClone**](/windows/win32/Vfw/nf-vfw-editstreamclone?branch=master)
-   [**EditStreamSetInfo**](/windows/win32/Vfw/nf-vfw-editstreamsetinfoa?branch=master)
-   [**EditStreamSetName**](/windows/win32/Vfw/nf-vfw-editstreamsetnamea?branch=master)

## Related topics

<dl> <dt>

[AVIFile Functions and Macros](avifile-functions-and-macros.md)
</dt> </dl>

 

 




