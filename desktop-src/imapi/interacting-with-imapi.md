---
title: Interacting with IMAPI
description: The following steps describe a typical interaction between an application and IMAPI.
ms.assetid: e57a86c4-7e27-40cf-a9c1-081b3f20d9d9
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Interacting with IMAPI

The following steps describe a typical interaction between an application and IMAPI.

1.  Create an instance of the **MSDiscMasterObj** (using **CoCreateInstance**, smart pointers from an import, and so on) and request the [**IDiscMaster**](/windows/win32/Imapi/nn-imapi-idiscmaster?branch=master) interface.
2.  Acquire access to IMAPI by calling [**IDiscMaster::Open**](/windows/win32/Imapi/nf-imapi-idiscmaster-open?branch=master). If this call succeeds, the application has full access to all the interfaces and methods implemented in **MSDiscMasterObj**.
3.  Retrieve the disc master format enumerator using [**EnumDiscMasterFormats**](/windows/win32/Imapi/nf-imapi-idiscmaster-enumdiscmasterformats?branch=master). Enumerate the set of formats that the disc master object supports, then select the active format. The formats returned from the enumerator are the IIDs of the interfaces for [**IJolietDiscMaster**](/windows/win32/Imapi/nn-imapi-ijolietdiscmaster?branch=master) and [**IRedbookDiscMaster**](/windows/win32/Imapi/nn-imapi-iredbookdiscmaster?branch=master).
4.  Retrieve the disc recorder enumerator using [**EnumDiscRecorders**](/windows/win32/Imapi/nf-imapi-idiscmaster-enumdiscrecorders?branch=master). Enumerate the list of supported disc recorders (specific to the active format), then select the active recorder. The [**IDiscRecorder**](/windows/win32/Imapi/nn-imapi-idiscrecorder?branch=master) interface represents a physical device.
5.  Use [**IDiscMaster::ProgressAdvise**](/windows/win32/Imapi/nf-imapi-idiscmaster-progressadvise?branch=master) to register for progress callbacks.
6.  Use the interface for the selected format to build up content. Content builds incrementally, so tracks or folder contents can be added to a disc piece by piece. Building up this content is called *staging an image*. The contents of the staged image cannot be incrementally deleted (you cannot remove a track that has been added), but it is possible to clear the contents of a staged image so that staging can start again. Use [**IDiscMaster::ClearFormatContent**](/windows/win32/Imapi/nf-imapi-idiscmaster-clearformatcontent?branch=master) to restart staging.

**For Audio:  **

1.  Use [**IRedbookDiscMaster::CreateAudioTrack**](/windows/win32/Imapi/nf-imapi-iredbookdiscmaster-createaudiotrack?branch=master) to indicate a new audio track is being started on the disc.
2.  Use [**IRedbookDiscMaster::AddAudioTrackBlocks**](/windows/win32/Imapi/nf-imapi-iredbookdiscmaster-addaudiotrackblocks?branch=master) to add raw audio data to a track. The application can use [**GetAvailableAudioTrackBlocks**](/windows/win32/Imapi/nf-imapi-iredbookdiscmaster-getavailableaudiotrackblocks?branch=master), [**GetTotalAudioBlocks**](/windows/win32/Imapi/nf-imapi-iredbookdiscmaster-gettotalaudioblocks?branch=master), and [**GetUsedAudioBlocks**](/windows/win32/Imapi/nf-imapi-iredbookdiscmaster-getusedaudioblocks?branch=master) to retrieve statistical information.
3.  Use [**IRedbookDiscMaster::CloseAudioTrack**](/windows/win32/Imapi/nf-imapi-iredbookdiscmaster-closeaudiotrack?branch=master) to close an audio track.
4.  Repeat steps 1-3 until out of space or all audio tracks have been written.

**For Data:  **

1.  Use [**IJolietDiscMaster::AddData**](/windows/win32/Imapi/nf-imapi-ijolietdiscmaster-adddata?branch=master) to add the contents of a folder to the image. The items within a folder are placed in the root of the image file. Use [**GetTotalDataBlocks**](/windows/win32/Imapi/nf-imapi-ijolietdiscmaster-gettotaldatablocks?branch=master) and [**GetUsedDataBlocks**](/windows/win32/Imapi/nf-imapi-ijolietdiscmaster-getuseddatablocks?branch=master) to retrieve statistical information.
2.  Repeat the above step until out of space or all data has been added.

**For All Discs:  **

1.  Use [**IDiscMaster::RecordDisc**](/windows/win32/Imapi/nf-imapi-idiscmaster-recorddisc?branch=master) to record the disc.
2.  Close the IMAPI session using [**IDiscMaster::Close**](/windows/win32/Imapi/nf-imapi-idiscmaster-close?branch=master). Closing the session clears the contents of the disc stash.

 

 




