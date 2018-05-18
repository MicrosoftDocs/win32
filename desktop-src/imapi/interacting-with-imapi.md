---
title: Interacting with IMAPI
description: The following steps describe a typical interaction between an application and IMAPI.
ms.assetid: 'e57a86c4-7e27-40cf-a9c1-081b3f20d9d9'
---

# Interacting with IMAPI

The following steps describe a typical interaction between an application and IMAPI.

1.  Create an instance of the **MSDiscMasterObj** (using **CoCreateInstance**, smart pointers from an import, and so on) and request the [**IDiscMaster**](idiscmaster.md) interface.
2.  Acquire access to IMAPI by calling [**IDiscMaster::Open**](idiscmaster-open.md). If this call succeeds, the application has full access to all the interfaces and methods implemented in **MSDiscMasterObj**.
3.  Retrieve the disc master format enumerator using [**EnumDiscMasterFormats**](idiscmaster-enumdiscmasterformats.md). Enumerate the set of formats that the disc master object supports, then select the active format. The formats returned from the enumerator are the IIDs of the interfaces for [**IJolietDiscMaster**](ijolietdiscmaster.md) and [**IRedbookDiscMaster**](iredbookdiscmaster.md).
4.  Retrieve the disc recorder enumerator using [**EnumDiscRecorders**](idiscmaster-enumdiscrecorders.md). Enumerate the list of supported disc recorders (specific to the active format), then select the active recorder. The [**IDiscRecorder**](idiscrecorder.md) interface represents a physical device.
5.  Use [**IDiscMaster::ProgressAdvise**](idiscmaster-progressadvise.md) to register for progress callbacks.
6.  Use the interface for the selected format to build up content. Content builds incrementally, so tracks or folder contents can be added to a disc piece by piece. Building up this content is called *staging an image*. The contents of the staged image cannot be incrementally deleted (you cannot remove a track that has been added), but it is possible to clear the contents of a staged image so that staging can start again. Use [**IDiscMaster::ClearFormatContent**](idiscmaster-clearformatcontent.md) to restart staging.

**For Audio:  **

1.  Use [**IRedbookDiscMaster::CreateAudioTrack**](iredbookdiscmaster-createaudiotrack.md) to indicate a new audio track is being started on the disc.
2.  Use [**IRedbookDiscMaster::AddAudioTrackBlocks**](iredbookdiscmaster-addaudiotrackblocks.md) to add raw audio data to a track. The application can use [**GetAvailableAudioTrackBlocks**](iredbookdiscmaster-getavailableaudiotrackblocks.md), [**GetTotalAudioBlocks**](iredbookdiscmaster-gettotalaudioblocks.md), and [**GetUsedAudioBlocks**](iredbookdiscmaster-getusedaudioblocks.md) to retrieve statistical information.
3.  Use [**IRedbookDiscMaster::CloseAudioTrack**](iredbookdiscmaster-closeaudiotrack.md) to close an audio track.
4.  Repeat steps 1-3 until out of space or all audio tracks have been written.

**For Data:  **

1.  Use [**IJolietDiscMaster::AddData**](ijolietdiscmaster-adddata.md) to add the contents of a folder to the image. The items within a folder are placed in the root of the image file. Use [**GetTotalDataBlocks**](ijolietdiscmaster-gettotaldatablocks.md) and [**GetUsedDataBlocks**](ijolietdiscmaster-getuseddatablocks.md) to retrieve statistical information.
2.  Repeat the above step until out of space or all data has been added.

**For All Discs:  **

1.  Use [**IDiscMaster::RecordDisc**](idiscmaster-recorddisc.md) to record the disc.
2.  Close the IMAPI session using [**IDiscMaster::Close**](idiscmaster-close.md). Closing the session clears the contents of the disc stash.

 

 




