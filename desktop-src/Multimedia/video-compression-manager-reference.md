---
title: Video Compression Manager Reference
description: Video Compression Manager Reference
ms.assetid: 'dd678b24-62af-495f-bdd6-3082c1a753dd'
keywords: ["Video for Windows (VFW),video compression manager (VCM)", "VFW (Video for Windows),video compression manager (VCM)"]
---

# Video Compression Manager Reference

This section describes the functions, structures, messages, and macros, associated with VCM. These elements are grouped as follows.

## Compressor Installation and Removal

-   [**ICInstall**](icinstall.md)
-   [**ICLocate**](iclocate.md)
-   [**ICOPEN**](icopen-struct.md)
-   [**ICClose**](icclose.md)
-   [**ICRemove**](icremove.md)
-   [**ICOpenFunction**](icopenfunction.md)

## Locating and Opening a Compressor

-   [**ICLocate**](iclocate.md)
-   [**ICOPEN**](icopen-struct.md)
-   [**ICDecompressOpen**](icdecompressopen.md)
-   [**ICDrawOpen**](icdrawopen.md)
-   [**ICINFO**](icinfo-struct.md)
-   [**ICClose**](icclose.md)

## Selecting Compressors

-   [**ICCompressorChoose**](iccompressorchoose.md)
-   [**ICCompressorFree**](iccompressorfree.md)
-   [**COMPVARS**](compvars.md)

## Configuring Compressors

-   [**ICM\_CONFIGURE**](icm-configure.md)
-   [**ICM\_GETSTATE**](icm-getstate.md)
-   [**ICM\_SETSTATE**](icm-setstate.md)
-   [**ICSendMessage**](icsendmessage.md)

## Compressor Information

-   [**ICGetInfo**](icgetinfo.md)
-   [**ICINFO**](icinfo-struct.md)
-   [**ICM\_GETDEFAULTKEYFRAMERATE**](icm-getdefaultkeyframerate.md)
-   [**ICGetDisplayFormat**](icgetdisplayformat.md)
-   [**ICM\_GETDEFAULTQUALITY**](icm-getdefaultquality.md)
-   [**ICM\_ABOUT**](icm-about.md)

## Single Image Compression

-   [**ICImageCompress**](icimagecompress.md)

## Sequence Compression

-   [**ICSeqCompressFrame**](icseqcompressframe.md)
-   [**ICSeqCompressFrameStart**](icseqcompressframestart.md)
-   [**ICSeqCompressFrameEnd**](icseqcompressframeend.md)

## COMPVARS

-   [**ICCompressorChoose**](iccompressorchoose.md)

## Image Data Compression

-   [**ICCOMPRESS**](iccompress-struct.md)
-   [**ICM\_COMPRESS\_GET\_FORMAT**](icm-compress-get-format.md)
-   [**ICM\_COMPRESS\_QUERY**](icm-compress-query.md)
-   [**ICM\_COMPRESS\_GET\_SIZE**](icm-compress-get-size.md)
-   [**ICM\_COMPRESS\_BEGIN**](icm-compress-begin.md)
-   [**ICM\_COMPRESS\_END**](icm-compress-end.md)

## Compressor Monitoring

-   [**ICSETSTATUSPROC**](icsetstatusproc-struct.md)

## Decompressing Single Images

-   [**ICImageDecompress**](icimagedecompress.md)

## Decompressing Image Data

-   [**ICDECOMPRESSEX**](icdecompressex-struct.md)
-   [**ICDecompressExBegin**](icdecompressexbegin.md)
-   [**ICM\_DECOMPRESSEX\_END**](icm-decompressex-end.md)
-   [**ICM\_DECOMPRESS\_GET\_FORMAT**](icm-decompress-get-format.md)
-   [**ICM\_DECOMPRESS\_GET\_PALETTE**](icm-decompress-get-palette.md)
-   [**ICDecompressExQuery**](icdecompressexquery.md)
-   [**ICDECOMPRESS**](icdecompress-struct.md)
-   [**ICM\_DECOMPRESS\_BEGIN**](icm-decompress-begin.md)
-   [**ICM\_DECOMPRESS\_END**](icm-decompress-end.md)
-   [**ICM\_DECOMPRESS\_QUERY**](icm-decompress-query.md)

## Using Hardware-Drawing Capabilities

-   [**ICGetInfo**](icgetinfo.md)
-   [**ICDRAWBEGIN**](icdrawbegin-struct.md)
-   [**ICM\_DRAW\_END**](icm-draw-end.md)
-   [**ICM\_DRAW\_FLUSH**](icm-draw-flush.md)
-   [**ICM\_DRAW\_QUERY**](icm-draw-query.md)
-   [**ICDrawSuggestFormat**](icdrawsuggestformat.md)
-   [**ICM\_DRAW\_START**](icm-draw-start.md)
-   [**ICM\_DRAW\_STOP**](icm-draw-stop.md)
-   [**ICM\_GETBUFFERSWANTED**](icm-getbufferswanted.md)
-   [**ICM\_DRAW\_REALIZE**](icm-draw-realize.md)
-   [**ICDrawOpen**](icdrawopen.md)
-   [**ICDRAW**](icdraw-struct.md)
-   [**ICM\_DRAW\_GETTIME**](icm-draw-gettime.md)
-   [**ICM\_DRAW\_SETTIME**](icm-draw-settime.md)
-   [**ICM\_DRAW\_WINDOW**](icm-draw-window.md)
-   [**ICM\_DRAW\_REALIZE**](icm-draw-realize.md)
-   [**ICM\_DRAW\_CHANGEPALETTE**](icm-draw-changepalette.md)
-   [**ICM\_DRAW\_RENDERBUFFER**](icm-draw-renderbuffer.md)

## Related topics

<dl> <dt>

[Video Compression Manager](video-compression-manager.md)
</dt> </dl>

 

 




