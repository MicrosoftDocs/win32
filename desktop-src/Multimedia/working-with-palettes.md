---
title: Working with Palettes
description: Working with Palettes
ms.assetid: 0ad0d78b-4c2c-499c-ad5e-8324b59e89fc
keywords:
- WM_CAP_PAL_PASTE message
- capPalettePaste macro
- WM_CAP_PAL_OPEN message
- capPaletteOpen macro
- WM_CAP_PAL_AUTOCREATE message
- capPaletteAuto macro
- WM_CAP_PAL_MANUALCREATE message
- capPaletteManual macro
ms.topic: article
ms.date: 05/31/2018
---

# Working with Palettes

Initially, if the video capture format requires a palette, the capture window uses the palette supplied by the capture driver. This palette might consist of gray-scale values for black-and-white reproduction, or a broad selection of color values. You can retrieve an existing palette to replace the default palette by using the [**WM\_CAP\_PAL\_PASTE**](wm-cap-pal-paste.md) or [**WM\_CAP\_PAL\_OPEN**](wm-cap-pal-open.md) message (or the [**capPalettePaste**](/windows/desktop/api/Vfw/nf-vfw-cappalettepaste) or [**capPaletteOpen**](/windows/desktop/api/Vfw/nf-vfw-cappaletteopen) macro). Alternatively, you can create a custom palette to replace the default palette by using the [**WM\_CAP\_PAL\_AUTOCREATE**](wm-cap-pal-autocreate.md) or [**WM\_CAP\_PAL\_MANUALCREATE**](wm-cap-pal-manualcreate.md) message (or the [**capPaletteAuto**](/windows/desktop/api/Vfw/nf-vfw-cappaletteauto) or [**capPaletteManual**](/windows/desktop/api/Vfw/nf-vfw-cappalettemanual) macro). After you replace the default palette, the capture window and driver use the replacement palette until you create or open another palette.

The WM\_CAP\_PAL\_AUTOCREATE or WM\_CAP\_PAL\_MANUALCREATE message creates an optimized palette based on the current video input. This custom palette gives a video sequence the best color fidelity because it is based on colors that exist in the sequence. The capture window creates a three-dimensional histogram of the colors it samples. It reduces the number of colors by examining the absolute error between adjacent colors and consolidating those with the smallest error value.

When sending WM\_CAP\_PAL\_AUTOCREATE, you must specify the number of frames for AVICap to sample, and specify the size of the color palette. When specifying the number of frames, include enough frames to ensure that all colors in the sequence are sampled.

You can sample the current frame by using WM\_CAP\_PAL\_MANUALCREATE. By using this message with several manually selected frames, you can create a palette that contains the colors you want to appear in the palette.

A palette can contain up to 256 colors. If you merge palettes or if the video sequence is to be displayed simultaneously with other video or images, you should use a smaller color selection so that colors from each image or video clip can coexist.

You save a new palette by using the [**WM\_CAP\_PAL\_SAVE**](wm-cap-pal-save.md) message (or the [**capPaletteSave**](/windows/desktop/api/Vfw/nf-vfw-cappalettesave) macro) and later retrieve it by using the [**WM\_CAP\_PAL\_OPEN**](wm-cap-pal-open.md) message. You can save a palette for post-processing of the palette or for use in another application.

You can paste a palette from the clipboard into the capture window by using the [**WM\_CAP\_PAL\_PASTE**](wm-cap-pal-paste.md) message. The capture window passes the palette to the capture driver. Other applications can copy palettes to the clipboard. You can also copy a palette to the clipboard by using the [**WM\_CAP\_EDIT\_COPY**](wm-cap-edit-copy.md) message (or the [**capEditCopy**](/windows/desktop/api/Vfw/nf-vfw-capeditcopy) macro). This message copies the video frame buffer, including the palette, onto the clipboard.

 

 




