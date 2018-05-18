---
title: AVIFile Reference
description: AVIFile Reference
ms.assetid: '73532d83-89c2-4911-8558-ce110e9f0f95'
---

# AVIFile Reference

This section describes the functions, structures, and macros for applications using the AVIFile services. These elements are grouped as follows:

## AVIFile Library Operations

-   [**AVIFileInit**](avifileinit.md)
-   [**AVIFileExit**](avifileexit.md)

## Opening and Closing AVI Files

-   [**AVIFileOpen**](avifileopen.md)
-   [**AVIFileAddRef**](avifileaddref.md)
-   [**AVIFileRelease**](avifilerelease.md)
-   [**GetOpenFileNamePreview**](getopenfilenamepreview.md)

## Reading from a File

-   [**AVIFileInfo**](avifileinfo.md)
-   [**AVIFILEINFO**](avifileinfo-struct.md)
-   [**AVIFileReadData**](avifilereaddata.md)

## Writing to a File

-   [**AVIFileWriteData**](avifilewritedata.md)

## Using the Clipboard

-   [**AVIPutFileOnClipboard**](aviputfileonclipboard.md)
-   [**AVIGetFromClipboard**](avigetfromclipboard.md)
-   [**AVIClearClipboard**](aviclearclipboard.md)

## Opening and Closing Streams

-   [**AVIFileGetStream**](avifilegetstream.md)
-   [**AVIStreamOpenFromFile**](avistreamopenfromfile.md)
-   [**AVIStreamAddRef**](avistreamaddref.md)
-   [**AVIStreamRelease**](avistreamrelease.md)

## Reading Stream Information

-   [**AVISTREAMINFO**](avistreaminfo-struct.md)
-   [**AVIStreamReadData**](avistreamreaddata.md)
-   [**AVIStreamDataSize**](avistreamdatasize.md)
-   [**AVIStreamReadFormat**](avistreamreadformat.md)
-   [**AVIStreamFormatSize**](avistreamformatsize.md)
-   [**AVIStreamRead**](avistreamread.md)
-   [**AVIStreamSampleSize**](avistreamsamplesize.md)
-   [**AVIStreamBeginStreaming**](avistreambeginstreaming.md)
-   [**AVIStreamEndStreaming**](avistreamendstreaming.md)

## Decompressing Video Data in a Stream

-   [**AVIStreamGetFrameOpen**](avistreamgetframeopen.md)
-   [**AVIStreamGetFrame**](avistreamgetframe.md)
-   [**AVIStreamGetFrameClose**](avistreamgetframeclose.md)

## Creating a File from Existing Streams

-   [**AVISave**](avisave.md)
-   [**AVISaveV**](avisavev.md)
-   [**AVISaveOptions**](avisaveoptions.md)
-   [**GetSaveFileNamePreview**](getsavefilenamepreview.md)
-   [**AVIMakeFileFromStreams**](avimakefilefromstreams.md)

## Writing Individual Streams

-   [**AVIFileCreateStream**](avifilecreatestream.md)
-   [**AVIStreamSetFormat**](avistreamsetformat.md)
-   [**AVIStreamWrite**](avistreamwrite.md)
-   [**AVIFileWriteData**](avifilewritedata.md)
-   [**AVIStreamWriteData**](avistreamwritedata.md)
-   [**AVIStreamRelease**](avistreamrelease.md)

## Finding the Starting Position in a Stream

-   [**AVIStreamStart**](avistreamstart.md)
-   [**AVIStreamStartTime**](avistreamstarttime.md)
-   [**AVIStreamLength**](avistreamlength.md)
-   [**AVIStreamLengthTime**](avistreamlengthtime.md)
-   [**AVIStreamFindSample**](avistreamfindsample.md)
-   [**AVIStreamEnd**](avistreamend.md)
-   [**AVIStreamEndTime**](avistreamendtime.md)

## Finding Sample and Key Frames

-   [**AVIStreamFindSample**](avistreamfindsample.md)
-   [**AVIStreamIsKeyFrame**](avistreamiskeyframe.md)
-   [**AVIStreamNearestKeyFrame**](avistreamnearestkeyframe.md)
-   [**AVIStreamNearestKeyFrameTime**](avistreamnearestkeyframetime.md)
-   [**AVIStreamNearestSample**](avistreamnearestsample.md)
-   [**AVIStreamNearestSampleTime**](avistreamnearestsampletime.md)
-   [**AVIStreamNextKeyFrame**](avistreamnextkeyframe.md)
-   [**AVIStreamNextKeyFrameTime**](avistreamnextkeyframetime.md)
-   [**AVIStreamNextSample**](avistreamnextsample.md)
-   [**AVIStreamNextSampleTime**](avistreamnextsampletime.md)
-   [**AVIStreamPrevKeyFrame**](avistreamprevkeyframe.md)
-   [**AVIStreamPrevKeyFrameTime**](avistreamprevkeyframetime.md)
-   [**AVIStreamPrevSample**](avistreamprevsample.md)
-   [**AVIStreamPrevSampleTime**](avistreamprevsampletime.md)
-   [**AVIStreamSampleToSample**](avistreamsampletosample.md)

## Switching Between Samples and Time

-   [**AVIStreamSampleToTime**](avistreamsampletotime.md)
-   [**AVIStreamTimeToSample**](avistreamtimetosample.md)

## Creating Temporary Streams

-   [**AVIStreamCreate**](avistreamcreate.md)
-   [**AVIMakeCompressedStream**](avimakecompressedstream.md)
-   [**AVIStreamRelease**](avistreamrelease.md)

## Editing AVI Streams

-   [**CreateEditableStream**](createeditablestream.md)
-   [**EditStreamCut**](editstreamcut.md)
-   [**EditStreamCopy**](editstreamcopy.md)
-   [**EditStreamPaste**](editstreampaste.md)
-   [**EditStreamClone**](editstreamclone.md)
-   [**EditStreamSetInfo**](editstreamsetinfo.md)
-   [**EditStreamSetName**](editstreamsetname.md)

## Related topics

<dl> <dt>

[AVIFile Functions and Macros](avifile-functions-and-macros.md)
</dt> </dl>

 

 




