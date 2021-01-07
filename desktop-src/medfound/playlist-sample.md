---
description: Playlist Sample
ms.assetid: ffe663ce-3e9a-4dfc-8904-6f055332c119
title: Playlist Sample
ms.topic: article
ms.date: 05/31/2018
---

# Playlist Sample

Shows how to use Microsoft Media Foundation to play a sequence of audio files in a playlist. The sample uses the [Sequencer Source](sequencer-source.md) to create and manage the playlist.

> [!Note]  
> This sample is no longer included in the SDK.

 

## APIs Demonstrated

This sample demonstrates the following Media Foundation interfaces:

-   [**IMFMediaSourceTopologyProvider**](/windows/desktop/api/mfidl/nn-mfidl-imfmediasourcetopologyprovider)
-   [**IMFMediaSession**](/windows/desktop/api/mfidl/nn-mfidl-imfmediasession)
-   [**IMFSequencerSource**](/windows/desktop/api/mfidl/nn-mfidl-imfsequencersource)

## Usage

The Playlist sample builds a Windows application.

-   To create a new playlist, select **Add to Playlist** from the **File** menu. In the **Open File** dialog, select one or more audio files. The files are added to the playlist.
-   To play the sequence, click **Play**.
-   To pause the current segment, click **Pause**.
-   To stop the current segment, click **Stop**.
-   To skip to a file, double-click the item in the playlist.
-   To delete a file from the playlist, select the item in the playlist. Then select **Remove from Playlist** from the **File** menu.

## Requirements



| Product                                                        | Version   |
|----------------------------------------------------------------|-----------|
| [Windows SDK](https://msdn.microsoft.com/windowsvista/bb980924.aspx) | Windows 7 |



 

## Downloading the Sample

This sample is available in the following locations.



| Location                                                     | Path/URL                                                   |
|--------------------------------------------------------------|------------------------------------------------------------|
| [Windows SDK](https://www.microsoft.com/download/details.aspx?id=8279) | *SDK Root*\\Samples\\multimedia\\mediafoundation\\Playlist |



 

## Related topics

<dl> <dt>

[BasicPlayback Sample](/previous-versions//bb970475(v=vs.85))
</dt> <dt>

[Media Foundation SDK Samples](media-foundation-sdk-samples.md)
</dt> <dt>

[Sequencer Source](sequencer-source.md)
</dt> </dl>

 

 
