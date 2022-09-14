---
description: MPEG-2 Support in DirectShow
ms.assetid: a4fe4cc9-86a5-4c83-94be-8901b97c8280
title: MPEG-2 Support in DirectShow
ms.topic: article
ms.date: 05/31/2018
---

# MPEG-2 Support in DirectShow

This section describes the components that you can use to play MPEG-2 content in DirectShow.

> [!Note]  
> Although DVD video is based on MPEG-2, this section does not describe DVD playback or navigation. For information about DVD in DirectShow, see [DVD Applications](dvd-applications.md).

 

MPEG-2 data can come from a local file, or from a live source, such as a network broadcast or D-VHS device. File playback is called *pull mode* because the parser filter pulls data from the file into the filter graph. Live sources are called *push mode* because the source filter pushes data into the graph.

DirectShow provides two filters that can parse MPEG-2 system streams:

-   [MPEG-2 Demultiplexer](mpeg-2-demultiplexer.md) ("demux"): This filter supports push mode for program streams and transport streams. In Windows XP and later, it also supports pull mode for program streams.
-   [MPEG-2 Splitter](mpeg-2-splitter.md): This filter supports pull mode for program streams on downlevel platforms. This filter is deprecated in Windows XP and later.

To use the MPEG-2 demux or MPEG-2 splitter, you must have DirectShow-compatible MPEG-2 audio and video decoders that accept packetized elementary streams (PES).

This section contains the following topics:

-   [Overview of MPEG-2 Systems](overview-of-mpeg-2-systems.md)
-   [Using the MPEG-2 Demultiplexer](using-the-mpeg-2-demultiplexer.md)
-   [Using the MPEG-2 Splitter](using-the-mpeg-2-splitter.md)
-   [MPEG Sample Properties](mpeg-sample-properties.md)

## Related topics

<dl> <dt>

[PSI Parser Filter Sample](psi-parser-filter-sample.md)
</dt> </dl>

 

 



