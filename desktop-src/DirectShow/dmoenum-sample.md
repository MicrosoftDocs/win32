---
description: DMOEnum Sample
ms.assetid: afd7853e-b0ab-42f6-8c2e-c2b0b40d989b
title: DMOEnum Sample
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DMOEnum Sample

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

## Description

This sample application enumerates all of the [DirectX Media Objects](directx-media-objects.md) (DMOs) registered in the user's system, and displays information about them.

The sample uses the [**DMOEnum**](/previous-versions/windows/desktop/api/Dmoreg/nf-dmoreg-dmoenum) function and the [**IEnumDMO**](/previous-versions/windows/desktop/api/Mediaobj/nn-mediaobj-ienumdmo) interface to enumerate the DMOs. It uses the [**IMediaObject**](/previous-versions/windows/desktop/api/Mediaobj/nn-mediaobj-imediaobject) interface and other DMO interfaces to retrieve information about each DMO.

## Usage

When the application launches, it enumerates all of the installed DMOs. If you select a specific DMO category, the application displays only the DMOs in that category. To view information about a DMO, select the DMO from the list. The application displays the number of streams, the preferred media types, the DLL server for that DMO, and other information about the DMO. To include or exclude keyed DMOs, toggle the **Include Keyed DMOs?** checkbox.

## Downloading the Sample

To download the DirectShow SDK samples, install the latest version of the [Windows SDK](https://msdn.microsoft.com/windowsvista/bb980924.aspx).

This sample is installed under the following path: *\[SDK Root\]*\\Samples\\Multimedia\\DirectShow\\Misc\\DMOEnum.

## Related topics

<dl> <dt>

[DirectShow Samples](directshow-samples.md)
</dt> </dl>

 

 



