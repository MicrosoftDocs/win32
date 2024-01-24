---
description: DVD Applications
ms.assetid: 6f41e0f1-e550-4ca6-9a80-ce4d498289e2
title: DVD Applications
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DVD Applications

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

DirectShow provides a component called the [DVD Navigator](dvd-navigator-filter.md) source filter which simplifies DVD navigation tasks in C++. The DVD Navigator has all the capabilities that you find on a full-featured stand-alone DVD player, plus additional capabilities specific to playing DVDs on personal computers. Using the DVD Navigator, C++ and scripting developers can create full-featured DVD applications without referring to the DVD specification. The DVD Navigator, in coordination with the decoder filters, also handles regional management and copyright protection (CSS and analog copy protection), isolating application developers from these details.

The DVD Navigator filter works across an entire DVD-Video volume, which consists of the files in the VIDEO\_TS directory. Unlike most DirectShow source filters that work with individual streams or files, the DVD Navigator uses the DVD-Video structure of titles, chapters, and time codes. Developers wishing to play individual MPEG-2 files in DirectShow should use the [MPEG-2 Demultiplexer](mpeg-2-demultiplexer.md) instead of the DVD Navigator filter. See [MPEG-2 Support in DirectShow](mpeg-2-support-in-directshow.md) for more information.

> [!Note]  
> To play DVDs, the user must have an MPEG-2 decoder.

 

This section contains the following topics.

-   [DVD Support Features in DirectShow](dvd-support-features-in-directshow.md)
-   [DVD Basics](dvd-basics.md)
-   [Building the DVD Filter Graph](building-the-dvd-filter-graph.md)
-   [Obtaining the DVD Interface Pointers](obtaining-the-dvd-interface-pointers.md)
-   [DVD Commands](dvd-commands.md)
-   [Identifying Valid DVD Operations](identifying-valid-dvd-operations.md)
-   [Synchronizing DVD Commands](synchronizing-dvd-commands.md)
-   [Data Flow in the DVD Navigator](data-flow-in-the-dvd-navigator.md)
-   [Handling DVD Event Notifications](handling-dvd-event-notifications.md)
-   [Working With DVD Menus](working-with-dvd-menus.md)
-   [Audio and Subpicture Streams](audio-and-subpicture-streams.md)
-   [Enforcing Parental Management Levels](enforcing-parental-management-levels.md)
-   [Saving and Restoring DvdState Objects](saving-and-restoring-dvdstate-objects.md)
-   [Working with DVD Text Strings](working-with-dvd-text-strings.md)
-   [Playing Karaoke Audio Streams](playing-karaoke-audio-streams.md)
-   [Handling Disc Ejections](handling-disc-ejections.md)
-   [DVD Playback Enhancements in Windows Vista](dvd-playback-enhancements-in-windows-vista.md)
-   [DVD Filter Graph Configuration](dvd-filter-graph-configuration.md)
-   [Shortcuts to C++ DVD Reference Pages](shortcuts-to-c-dvd-reference-pages.md)

For references on DVD/MPEG2 decoder development, see [DVD Decoder Development in DirectShow](dvd-decoder-development-in-directshow.md).

## Related topics

<dl> <dt>

[Using DirectShow](using-directshow.md)
</dt> </dl>

 

 



