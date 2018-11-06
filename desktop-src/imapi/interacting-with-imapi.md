---
title: Interacting with IMAPI
description: The following steps describe a typical interaction between an application and IMAPI.
ms.assetid: e57a86c4-7e27-40cf-a9c1-081b3f20d9d9
ms.topic: article
ms.date: 05/31/2018
---

# Interacting with IMAPI

The following steps describe a typical interaction between an application and IMAPI.

1.  Create an instance of the **MSDiscMasterObj** (using **CoCreateInstance**, smart pointers from an import, and so on) and request the [**IDiscMaster**](/windows/desktop/api/Imapi/nn-imapi-idiscmaster) interface.
2.  Acquire access to IMAPI by calling [**IDiscMaster::Open**](/windows/desktop/api/Imapi/nf-imapi-idiscmaster-open). If this call succeeds, the application has full access to all the interfaces and methods implemented in **MSDiscMasterObj**.
3.  Retrieve the disc master format enumerator using [**EnumDiscMasterFormats**](/windows/desktop/api/Imapi/nf-imapi-idiscmaster-enumdiscmasterformats). Enumerate the set of formats that the disc master object supports, then select the active format. The formats returned from the enumerator are the IIDs of the interfaces for [**IJolietDiscMaster**](/windows/desktop/api/Imapi/nn-imapi-ijolietdiscmaster) and [**IRedbookDiscMaster**](/windows/desktop/api/Imapi/nn-imapi-iredbookdiscmaster).
4.  Retrieve the disc recorder enumerator using [**EnumDiscRecorders**](/windows/desktop/api/Imapi/nf-imapi-idiscmaster-enumdiscrecorders). Enumerate the list of supported disc recorders (specific to the active format), then select the active recorder. The [**IDiscRecorder**](/windows/desktop/api/Imapi/nn-imapi-idiscrecorder) interface represents a physical device.
5.  Use [**IDiscMaster::ProgressAdvise**](/windows/desktop/api/Imapi/nf-imapi-idiscmaster-progressadvise) to register for progress callbacks.
6.  Use the interface for the selected format to build up content. Content builds incrementally, so tracks or folder contents can be added to a disc piece by piece. Building up this content is called *staging an image*. The contents of the staged image cannot be incrementally deleted (you cannot remove a track that has been added), but it is possible to clear the contents of a staged image so that staging can start again. Use [**IDiscMaster::ClearFormatContent**](/windows/desktop/api/Imapi/nf-imapi-idiscmaster-clearformatcontent) to restart staging.

**For Audio:  **

1.  Use [**IRedbookDiscMaster::CreateAudioTrack**](/windows/desktop/api/Imapi/nf-imapi-iredbookdiscmaster-createaudiotrack) to indicate a new audio track is being started on the disc.
2.  Use [**IRedbookDiscMaster::AddAudioTrackBlocks**](/windows/desktop/api/Imapi/nf-imapi-iredbookdiscmaster-addaudiotrackblocks) to add raw audio data to a track. The application can use [**GetAvailableAudioTrackBlocks**](/windows/desktop/api/Imapi/nf-imapi-iredbookdiscmaster-getavailableaudiotrackblocks), [**GetTotalAudioBlocks**](/windows/desktop/api/Imapi/nf-imapi-iredbookdiscmaster-gettotalaudioblocks), and [**GetUsedAudioBlocks**](/windows/desktop/api/Imapi/nf-imapi-iredbookdiscmaster-getusedaudioblocks) to retrieve statistical information.
3.  Use [**IRedbookDiscMaster::CloseAudioTrack**](/windows/desktop/api/Imapi/nf-imapi-iredbookdiscmaster-closeaudiotrack) to close an audio track.
4.  Repeat steps 1-3 until out of space or all audio tracks have been written.

**For Data:  **

1.  Use [**IJolietDiscMaster::AddData**](/windows/desktop/api/Imapi/nf-imapi-ijolietdiscmaster-adddata) to add the contents of a folder to the image. The items within a folder are placed in the root of the image file. Use [**GetTotalDataBlocks**](/windows/desktop/api/Imapi/nf-imapi-ijolietdiscmaster-gettotaldatablocks) and [**GetUsedDataBlocks**](/windows/desktop/api/Imapi/nf-imapi-ijolietdiscmaster-getuseddatablocks) to retrieve statistical information.
2.  Repeat the above step until out of space or all data has been added.

**For All Discs:  **

1.  Use [**IDiscMaster::RecordDisc**](/windows/desktop/api/Imapi/nf-imapi-idiscmaster-recorddisc) to record the disc.
2.  Close the IMAPI session using [**IDiscMaster::Close**](/windows/desktop/api/Imapi/nf-imapi-idiscmaster-close). Closing the session clears the contents of the disc stash.

 

 




