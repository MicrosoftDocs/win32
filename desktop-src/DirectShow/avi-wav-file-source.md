---
description: AVI/WAV File Source
ms.assetid: b8abf5d8-ba7f-441d-beef-9f85859318d5
title: AVI/WAV File Source
ms.topic: article
ms.date: 05/31/2018
---

# AVI/WAV File Source

(Deprecated. For AVI and WAV files, use the [File Source (Async)](file-source--async--filter.md) and the [AVI Splitter](avi-splitter-filter.md) or [WAVE Parser](wave-parser-filter.md).)

The AVI/WAV File Source filter reads AVI and WAV source files and generates the appropriate output pins for the file type.

For WAV files, the filter creates an audio output pin, which produces an audio stream that can be connected to an audio rendering filter or intervening audio transform filter.

For AVI files, the filter creates a video output pin, which produces a compressed AVI stream suitable for the AVI codec filter, and an audio output pin, which produces an audio stream suitable for an audio rendering filter or an intervening audio transform filter.

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 



