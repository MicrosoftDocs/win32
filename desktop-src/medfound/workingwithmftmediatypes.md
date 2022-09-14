---
description: Working with MFT Media Types
ms.assetid: 16c270ee-f246-4222-97e9-d8d0fe009155
title: Working with MFT Media Types
ms.topic: article
ms.date: 05/31/2018
---

# Working with MFT Media Types

A media type is a way to describe the format of a media stream. In Media Foundation, media types are represented by the **IMFMediaType** interface. This interface inherits the **IMFAttributes** interface. The details of a media type are specified as attributes.

To create a new media type, call the **MFCreateMediaType** function. This function returns a pointer to the **IMFMediaType** interface. The media type initially has no attributes.

The Media Foundation SDK provides several helper functions for initializing Media Types from format structures. For example the function **MFInitMediaTypeFromVideoInfoHeader** initializes a video type from a **VIDEOINFOHEADER** structure, and the function **MFInitMediaTypeFromWaveFormatEx** initializes a video type from a **WAVEFORMATEX** or **WAVEFORMATEXTENSIBLE** structure.

The format types that are used by the codecs are generally limited to those described by the **VIDEOINFOHEADER** and **WAVEFORMATEX** structures.

More information on creating and accessing Media Foundation media types is available in the Media Foundation SDK documentation.

## Related topics

<dl> <dt>

[Working with Codec MFTs](workingwithcodecmfts.md)
</dt> </dl>

 

 



