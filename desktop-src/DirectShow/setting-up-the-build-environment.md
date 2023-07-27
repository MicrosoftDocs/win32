---
description: Building DirectShow Applications
ms.assetid: 2fbdbe49-0d4d-4dce-afc3-7049c793ace0
title: Building DirectShow Applications
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Building DirectShow Applications

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This topic describes the headers and libraries needed to build DirectShow applications.

The latest DirectShow headers and libraries are available in the [Windows SDK](https://msdn.microsoft.com/windows/aa904949.aspx).

## Header Files

All DirectShow applications use the header file shown in the following table.



| Header File | Required For                 |
|-------------|------------------------------|
| Dshow.h     | All DirectShow applications. |



 

Some DirectShow interfaces require additional header files. These requirements are noted in the interface reference.

## Library Files

DirectShow uses the static library files shown in the following table.



| Library File | Description                                                                                                                    |
|--------------|--------------------------------------------------------------------------------------------------------------------------------|
| Strmiids.lib | Exports class identifiers (CLSIDs) and interface identifiers (IIDs).                                                           |
| Quartz.lib   | Exports the [**AMGetErrorText**](/windows/win32/api/errors/nf-errors-amgeterrortexta) function. If you do not call this function, this library is not required. |



 

Use the same .lib files for debug and release builds.

## Filter Base Classes

The Windows SDK provides a set of C++ classes that are recommended if you are writing a custom DirectShow filter. These classes are provided as sample code, which you can compile to a static library. For more information, see [DirectShow Base Classes](directshow-base-classes.md).

## Redistributable DLLs

DirectShow applications written for Windows XP with Service Pack 2 (SP2) and later do not need to redistribute any DirectShow DLLs.

For Windows XP with Service Pack 1 (SP1) and earlier, redistributable DirectShow DLLs are available from the Microsoft DirectX SDK. The latest version of these DLLs is version 9.0c. No further development of these redistributable DLLs is planned. Windows XP with Service Pack 2 (SP2) contains the version 9.0c DLLs.

The redstributable packages contain the following DLLs:

-   dxnt.cab
    -   amstream.dll
    -   devenum.dll
    -   encapi.dll
    -   ks.sys
    -   ksolay.ax
    -   ksproxy.ax
    -   ksuser.dll
    -   l3codecx.ax
    -   mciqtz32.dll
    -   mpg2splt.ax
    -   msdmo.dll
    -   mskssrv.sys
    -   mspclock.sys
    -   mspqm.sys
    -   mstee.sys
    -   mswebdvd.dll
    -   qasf.dll
    -   qcap.dll
    -   qdv.dll
    -   qdvd.dll
    -   qedit.dll
    -   qedwipes.dll
    -   quartz.dll
    -   stream.sys
    -   swenum.sys
-   bda.cab
    -   bdaplgin.ax
    -   bdasup.sys
    -   ccdecode.sys
    -   ipsink.ax
    -   kstvtune.ax
    -   kswdmcap.ax
    -   ksxbar.ax
    -   mpe.sys
    -   mpeg2data.ax
    -   msdv.sys
    -   msdvbnp.ax
    -   msvidctl.dll
    -   msyuv.dll
    -   nabtsfec.sys
    -   ndisip.sys
    -   psisdecd.dll
    -   psisrndr.ax
    -   slip.sys
    -   streamip.sys
    -   vbisurf.ax
    -   wstcodec.sys
    -   wstdecod.dll

## Related topics

<dl> <dt>

[Building DirectShow Filters](building-directshow-filters.md)
</dt> </dl>

 

 
