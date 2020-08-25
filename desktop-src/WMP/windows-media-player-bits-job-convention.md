---
title: Windows Media Player BITS Job Convention
description: Windows Media Player can automatically download and add digital media items to the library if you use Background Intelligent Transfer Service (BITS).
ms.assetid: 643faba7-9af2-4292-8d92-e321d7690a5b
keywords:
- Windows Media Player online stores,Background Intelligent Transfer Service (BITS)
- online stores,Background Intelligent Transfer Service (BITS)
- type 2 online stores,Background Intelligent Transfer Service (BITS)
- Background Intelligent Transfer Service (BITS)
- BITS (Background Intelligent Transfer Service)
- Windows Media Player online stores,BITS job convention
- online stores,BITS job convention
- type 2 online stores,BITS job convention
- BITS job convention
ms.topic: article
ms.date: 05/31/2018
---

# Windows Media Player BITS Job Convention

Windows Media Player can automatically download and add digital media items to the library if you use [Background Intelligent Transfer Service (BITS)](/windows/desktop/Bits/background-intelligent-transfer-service-portal). To take advantage of this feature, you must add your job to the BITS transfer queue and call **IBackgroundCopyJob::SetDescription**, providing a description string that uses the correct format.

> [!Note]  
> This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

## Syntax

``` syntax
::WMP_JOB:1:serviceId:Provider:AlbumArtist:AlbumTitle:TrackNumber:Title:Duration:Rating
```

## Parameters

<dl> <dt>

<span id="serviceId"></span><span id="serviceid"></span><span id="SERVICEID"></span>*serviceId*
</dt> <dd>

A randomly generated 32-bit value that Windows Media Player uses to identify the service.

</dd> <dt>

<span id="Provider"></span><span id="provider"></span><span id="PROVIDER"></span>*Provider*
</dt> <dd>

The provider name. This value must match a valid online store key name.

</dd> <dt>

<span id="AlbumArtist"></span><span id="albumartist"></span><span id="ALBUMARTIST"></span>*AlbumArtist*
</dt> <dd>

The name of the primary artist for the album.

</dd> <dt>

<span id="AlbumTitle"></span><span id="albumtitle"></span><span id="ALBUMTITLE"></span>*AlbumTitle*
</dt> <dd>

The title of the album.

</dd> <dt>

<span id="TrackNumber"></span><span id="tracknumber"></span><span id="TRACKNUMBER"></span>*TrackNumber*
</dt> <dd>

The CD track number.

</dd> <dt>

<span id="Title"></span><span id="title"></span><span id="TITLE"></span>*Title*
</dt> <dd>

The title of the content.

</dd> <dt>

<span id="Duration"></span><span id="duration"></span><span id="DURATION"></span>*Duration*
</dt> <dd>

The duration of the content.

</dd> <dt>

<span id="Rating"></span><span id="rating"></span><span id="RATING"></span>*Rating*
</dt> <dd>

The rating for the content.

</dd> </dl>

## Remarks

When Windows Media Player 10 or later uses BITS to download content, it enumerates the jobs in the transfer queue and inspects the description string for each job. If the description string matches the expected convention, Windows Media Player downloads the content.

You must add only one digital media file for download to each BITS job.

After you start a BITS job using this convention, you must let Windows Media Player complete the job. Windows Media Player will also remove the job from the BITS queue, move the downloaded file to the location where ripped music is saved, and add the downloaded file to the library.

The *serviceId* parameter must contain a nonzero 32-bit value. We recommend that you use the function [**CryptGenRandom**](/windows/desktop/api/wincrypt/nf-wincrypt-cryptgenrandom) to create this value.

The file name you specify using the *localName* parameter of **IBackgroundCopyJob::AddFile** must have a .wma, .wmv, .mp3, or .asf file name extension.

The remaining parameters are designed to contain metadata values related to the content. You can retrieve these values from your online store webpage by using **DownloadItem.getItemInfo**. You can retrieve the correct download collection by calling **DownloadManager.getDownloadCollection** and providing *serviceId* as the *collectionId* parameter.

Windows Media Player inspects the BITS queue periodically while the Player is running. To ensure that Windows Media Player checks the BITS queue for download jobs, you should create a value in the following registry subkey:

**HKEY\_CURRENT\_USER\\Software\\Microsoft\\MediaPlayer\\Services**

The value should be created as follows.



| Name                | Type      | Description                                                                                                                                                                                                          |
|---------------------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **RefreshDownload** | **DWORD** | Specifies whether Windows Media Player should inspect the BITS queue for download jobs. If the value is zero, the Player will not inspect the BITS queue. The Player must inspect the queue if the value is nonzero. |



 

You can use the following alternate syntax to add BITS jobs that Windows Media Player does not complete, but for which it simply shows status information:

``` syntax
::WMP_STATUS:1:serviceId:Provider:AlbumArtist:AlbumTitle:TrackNumber:Title:Duration:Rating
```

When you use the preceding syntax, you must write code to complete the BITS download, organize the content on the user's computer, and add the content to the library, if desired.

## Related topics

<dl> <dt>

[CryptGenRandom](/windows/desktop/api/wincrypt/nf-wincrypt-cryptgenrandom)
</dt> <dt>

[**DownloadItem.getItemInfo**](downloaditem-getiteminfo.md)
</dt> <dt>

[**DownloadManager.getDownloadCollection**](downloadmanager-getdownloadcollection.md)
</dt> <dt>

[**Reference for Type 2 Online Stores**](reference-for-type-2-online-stores.md)
</dt> </dl>

 

 