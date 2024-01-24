---
description: MFT\_AudioDelay Sample
ms.assetid: 08f119f9-cacd-4000-96b6-60c8c0055e9c
title: MFT_AudioDelay Sample
ms.topic: article
ms.date: 05/31/2018
---

# MFT\_AudioDelay Sample

Shows how to implement an audio effect as a Media Foundation Transform (MFT). The audio delay MFT accepts PCM audio as input, applies a delay (echo) effect, and outputs the modified audio data.

## APIs Demonstrated

This sample demonstrates the following Microsoft Media Foundation interfaces:

-   [**IMFTransform**](/windows/desktop/api/mftransform/nn-mftransform-imftransform)

## Usage

The MFT\_AudioDelay sample builds a DLL that is a COM server for the MFT. Before using the MFT, you must register the DLL. You can use the TopoEdit tool to build a topology that includes the audio delay MFT. For more information about TopoEdit, see [TopoEdit](topoedit.md). You can also modify the [PlaybackFX Sample](/previous-versions//bb970336(v=vs.85)) to use the MFT. You will need to modify the AddBranchToPartialTopology function in Player.cpp. Change the following line from:

``` syntax
else if (majorType == MFMediaType_Audio)
{
    hr = CreateAudioBranch(pTopology, pSourceNode, GUID_NULL);
}
```

To:

``` syntax
else if (majorType == MFMediaType_Audio)
{
    hr = CreateAudioBranch(pTopology, pSourceNode, CLSID_DelayMFT);
}
```

The value CLSID\_DelayMFT is declared in the header file AudioDelayUuids.h in the MFT\_AudioDelay sample folder.

## Requirements



| Product                                                        | Version   |
|----------------------------------------------------------------|-----------|
| [Windows SDK](https://msdn.microsoft.com/windowsvista/bb980924.aspx) | Windows 7 |



 

## Downloading the Sample

This sample is available in the [Windows classic samples github repository](https://github.com/Microsoft/Windows-classic-samples/tree/master/Samples/Win7Samples/multimedia/mediafoundation/mft_audiodelay).

## Related topics

<dl> <dt>

[Media Foundation SDK Samples](media-foundation-sdk-samples.md)
</dt> <dt>

[Media Foundation Transforms](media-foundation-transforms.md)
</dt> <dt>

[MFT\_Grayscale Sample](mft-grayscale-sample.md)
</dt> <dt>

[Writing a Custom MFT](writing-a-custom-mft.md)
</dt> </dl>

 

 
