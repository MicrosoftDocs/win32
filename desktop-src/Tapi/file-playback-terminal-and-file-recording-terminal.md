---
description: The File Playback Terminal and File Recording Terminal expose the ITTerminal and ITMultiTrackTerminal interfaces. These objects also expose the ITMediaControl interface, which provides methods for stopping, starting, and media navigation.
ms.assetid: 16b04ce1-d625-4824-bb1e-994a292cd42c
title: File Playback Terminal and File Recording Terminal
ms.topic: article
ms.date: 05/31/2018
---

# File Playback Terminal and File Recording Terminal

The File Playback Terminal and File Recording Terminal expose the [**ITTerminal**](/windows/win32/api/tapi3if/nn-tapi3if-itterminal) and [**ITMultiTrackTerminal**](/windows/desktop/api/tapi3if/nn-tapi3if-itmultitrackterminal) interfaces. These objects also expose the [**ITMediaControl**](/windows/desktop/api/tapi3if/nn-tapi3if-itmediacontrol) interface, which provides methods for stopping, starting, and media navigation.

The File Playback Terminal exposes the [**ITMediaPlayback**](/windows/desktop/api/tapi3if/nn-tapi3if-itmediaplayback) interface, which has playback-specific methods.

The File Recording Terminal exposes the [**ITMediaRecord**](/windows/desktop/api/tapi3if/nn-tapi3if-itmediarecord) interface, which provides recording-specific methods.

As [multitrack terminals](multitrack-terminals.md), File Recording Terminal and File Playback Terminal each manage a collection of [track terminals](track-terminals.md).

 

 
