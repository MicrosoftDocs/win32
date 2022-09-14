---
title: AVIFile Reference
description: AVIFile Reference
ms.assetid: 73532d83-89c2-4911-8558-ce110e9f0f95
ms.topic: article
ms.date: 05/31/2018
---

# AVIFile Reference

This section describes the functions, structures, and macros for applications using the AVIFile services. These elements are grouped as follows:

## AVIFile Library Operations

-   [**AVIFileInit**](/windows/desktop/api/Vfw/nf-vfw-avifileinit)
-   [**AVIFileExit**](/windows/desktop/api/Vfw/nf-vfw-avifileexit)

## Opening and Closing AVI Files

-   [**AVIFileOpen**](/windows/desktop/api/Vfw/nf-vfw-avifileopen)
-   [**AVIFileAddRef**](/windows/desktop/api/Vfw/nf-vfw-avifileaddref)
-   [**AVIFileRelease**](/windows/desktop/api/Vfw/nf-vfw-avifilerelease)
-   [**GetOpenFileNamePreview**](/windows/desktop/api/Vfw/nf-vfw-getopenfilenamepreviewa)

## Reading from a File

-   [**AVIFileInfo**](/windows/desktop/api/Vfw/nf-vfw-avifileinfo)
-   [**AVIFILEINFO**](/windows/desktop/api/Vfw/ns-vfw-avifileinfoa)
-   [**AVIFileReadData**](/windows/desktop/api/Vfw/nf-vfw-avifilereaddata)

## Writing to a File

-   [**AVIFileWriteData**](/windows/desktop/api/Vfw/nf-vfw-avifilewritedata)

## Using the Clipboard

-   [**AVIPutFileOnClipboard**](/windows/desktop/api/Vfw/nf-vfw-aviputfileonclipboard)
-   [**AVIGetFromClipboard**](/windows/desktop/api/Vfw/nf-vfw-avigetfromclipboard)
-   [**AVIClearClipboard**](/windows/desktop/api/Vfw/nf-vfw-aviclearclipboard)

## Opening and Closing Streams

-   [**AVIFileGetStream**](/windows/desktop/api/Vfw/nf-vfw-avifilegetstream)
-   [**AVIStreamOpenFromFile**](/windows/desktop/api/Vfw/nf-vfw-avistreamopenfromfilea)
-   [**AVIStreamAddRef**](/windows/desktop/api/Vfw/nf-vfw-avistreamaddref)
-   [**AVIStreamRelease**](/windows/desktop/api/Vfw/nf-vfw-avistreamrelease)

## Reading Stream Information

-   [**AVISTREAMINFO**](/windows/desktop/api/Vfw/ns-vfw-avistreaminfoa)
-   [**AVIStreamReadData**](/windows/desktop/api/Vfw/nf-vfw-avistreamreaddata)
-   [**AVIStreamDataSize**](/windows/desktop/api/Vfw/nf-vfw-avistreamdatasize)
-   [**AVIStreamReadFormat**](/windows/desktop/api/Vfw/nf-vfw-avistreamreadformat)
-   [**AVIStreamFormatSize**](/windows/desktop/api/Vfw/nf-vfw-avistreamformatsize)
-   [**AVIStreamRead**](/windows/desktop/api/Vfw/nf-vfw-avistreamread)
-   [**AVIStreamSampleSize**](/windows/desktop/api/Vfw/nf-vfw-avistreamsamplesize)
-   [**AVIStreamBeginStreaming**](/windows/desktop/api/Vfw/nf-vfw-avistreambeginstreaming)
-   [**AVIStreamEndStreaming**](/windows/desktop/api/Vfw/nf-vfw-avistreamendstreaming)

## Decompressing Video Data in a Stream

-   [**AVIStreamGetFrameOpen**](/windows/desktop/api/Vfw/nf-vfw-avistreamgetframeopen)
-   [**AVIStreamGetFrame**](/windows/desktop/api/Vfw/nf-vfw-avistreamgetframe)
-   [**AVIStreamGetFrameClose**](/windows/desktop/api/Vfw/nf-vfw-avistreamgetframeclose)

## Creating a File from Existing Streams

-   [**AVISave**](/windows/desktop/api/Vfw/nf-vfw-avisavea)
-   [**AVISaveV**](/windows/desktop/api/Vfw/nf-vfw-avisaveva)
-   [**AVISaveOptions**](/windows/desktop/api/Vfw/nf-vfw-avisaveoptions)
-   [**GetSaveFileNamePreview**](/windows/desktop/api/Vfw/nf-vfw-getsavefilenamepreviewa)
-   [**AVIMakeFileFromStreams**](/windows/desktop/api/Vfw/nf-vfw-avimakefilefromstreams)

## Writing Individual Streams

-   [**AVIFileCreateStream**](/windows/desktop/api/Vfw/nf-vfw-avifilecreatestream)
-   [**AVIStreamSetFormat**](/windows/desktop/api/Vfw/nf-vfw-avistreamsetformat)
-   [**AVIStreamWrite**](/windows/desktop/api/Vfw/nf-vfw-avistreamwrite)
-   [**AVIFileWriteData**](/windows/desktop/api/Vfw/nf-vfw-avifilewritedata)
-   [**AVIStreamWriteData**](/windows/desktop/api/Vfw/nf-vfw-avistreamwritedata)
-   [**AVIStreamRelease**](/windows/desktop/api/Vfw/nf-vfw-avistreamrelease)

## Finding the Starting Position in a Stream

-   [**AVIStreamStart**](/windows/desktop/api/Vfw/nf-vfw-avistreamstart)
-   [**AVIStreamStartTime**](/windows/desktop/api/Vfw/nf-vfw-avistreamstarttime)
-   [**AVIStreamLength**](/windows/desktop/api/Vfw/nf-vfw-avistreamlength)
-   [**AVIStreamLengthTime**](/windows/desktop/api/Vfw/nf-vfw-avistreamlengthtime)
-   [**AVIStreamFindSample**](/windows/desktop/api/Vfw/nf-vfw-avistreamfindsample)
-   [**AVIStreamEnd**](/windows/desktop/api/Vfw/nf-vfw-avistreamend)
-   [**AVIStreamEndTime**](/windows/desktop/api/Vfw/nf-vfw-avistreamendtime)

## Finding Sample and Key Frames

-   [**AVIStreamFindSample**](/windows/desktop/api/Vfw/nf-vfw-avistreamfindsample)
-   [**AVIStreamIsKeyFrame**](/windows/desktop/api/Vfw/nf-vfw-avistreamiskeyframe)
-   [**AVIStreamNearestKeyFrame**](/windows/desktop/api/Vfw/nf-vfw-avistreamnearestkeyframe)
-   [**AVIStreamNearestKeyFrameTime**](/windows/desktop/api/Vfw/nf-vfw-avistreamnearestkeyframetime)
-   [**AVIStreamNearestSample**](/windows/desktop/api/Vfw/nf-vfw-avistreamnearestsample)
-   [**AVIStreamNearestSampleTime**](/windows/desktop/api/Vfw/nf-vfw-avistreamnearestsampletime)
-   [**AVIStreamNextKeyFrame**](/windows/desktop/api/Vfw/nf-vfw-avistreamnextkeyframe)
-   [**AVIStreamNextKeyFrameTime**](/windows/desktop/api/Vfw/nf-vfw-avistreamnextkeyframetime)
-   [**AVIStreamNextSample**](/windows/desktop/api/Vfw/nf-vfw-avistreamnextsample)
-   [**AVIStreamNextSampleTime**](/windows/desktop/api/Vfw/nf-vfw-avistreamnextsampletime)
-   [**AVIStreamPrevKeyFrame**](/windows/desktop/api/Vfw/nf-vfw-avistreamprevkeyframe)
-   [**AVIStreamPrevKeyFrameTime**](/windows/desktop/api/Vfw/nf-vfw-avistreamprevkeyframetime)
-   [**AVIStreamPrevSample**](/windows/desktop/api/Vfw/nf-vfw-avistreamprevsample)
-   [**AVIStreamPrevSampleTime**](/windows/desktop/api/Vfw/nf-vfw-avistreamprevsampletime)
-   [**AVIStreamSampleToSample**](/windows/desktop/api/Vfw/nf-vfw-avistreamsampletosample)

## Switching Between Samples and Time

-   [**AVIStreamSampleToTime**](/windows/desktop/api/Vfw/nf-vfw-avistreamsampletotime)
-   [**AVIStreamTimeToSample**](/windows/desktop/api/Vfw/nf-vfw-avistreamtimetosample)

## Creating Temporary Streams

-   [**AVIStreamCreate**](/windows/desktop/api/Vfw/nf-vfw-avistreamcreate)
-   [**AVIMakeCompressedStream**](/windows/desktop/api/Vfw/nf-vfw-avimakecompressedstream)
-   [**AVIStreamRelease**](/windows/desktop/api/Vfw/nf-vfw-avistreamrelease)

## Editing AVI Streams

-   [**CreateEditableStream**](/windows/desktop/api/Vfw/nf-vfw-createeditablestream)
-   [**EditStreamCut**](/windows/desktop/api/Vfw/nf-vfw-editstreamcut)
-   [**EditStreamCopy**](/windows/desktop/api/Vfw/nf-vfw-editstreamcopy)
-   [**EditStreamPaste**](/windows/desktop/api/Vfw/nf-vfw-editstreampaste)
-   [**EditStreamClone**](/windows/desktop/api/Vfw/nf-vfw-editstreamclone)
-   [**EditStreamSetInfo**](/windows/desktop/api/Vfw/nf-vfw-editstreamsetinfoa)
-   [**EditStreamSetName**](/windows/desktop/api/Vfw/nf-vfw-editstreamsetnamea)

## Related topics

<dl> <dt>

[AVIFile Functions and Macros](avifile-functions-and-macros.md)
</dt> </dl>

 

 




