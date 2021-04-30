---
description: XAudio2 is a cross-platform API that has shipped for use on Xbox 360 as well as versions of Windows, including Windows XP, Windows Vista, Windows 7, and Windows 8.
ms.assetid: 875b44c4-30d6-8a6e-0cfc-9beb8c46f1b4
title: XAudio2 Versions
ms.topic: article
ms.date: 05/31/2018
---

# XAudio2 Versions

XAudio2 is a cross-platform API that has shipped for use on Xbox 360 as well as versions of Windows, including Windows XP, Windows Vista, Windows 7, and Windows 8. On Xbox 360, XAudio2 ships as a static library that is compiled into the main game executable. On Windows, XAudio2 is provided as a Dynamic Link Library (DLL) installed into the system folders of the Operating System.

## XAudio 2.9 (Windows 10 and redistributable for Windows 7 and Windows 8.x)

XAudio2 version 2.9 ships as part of Windows 10, XAUDIO2\_9.DLL, alongside XAudio 2.8 to support older applications. A [redistributable version of XAudio 2.9](xaudio2-redistributable.md) is also available for Windows 7 SP1, Windows 8 and Windows 8.1.

XAudio2.9 has been updated with the following changes:

-   New creation flags: XAUDIO2\_DEBUG\_ENGINE, XAUDIO2\_STOP\_ENGINE\_WHEN\_IDLE, XAUDIO2\_1024\_QUANTUM
-   xWMA support is available in this version of XAudio2.
-   The [**CreateHrtfApo**](/windows/desktop/api/HrtfApoApi/nf-hrtfapoapi-createhrtfapo) function is supported in the Windows 10 version of XAudio 2.9.
-   [**XAUDIO2FX\_REVERB\_PARAMETERS**](/windows/desktop/api/xaudio2fx/ns-xaudio2fx-xaudio2fx_reverb_parameters) now includes the value *SideDelay* for 7.1 systems.
-   The [**ReverbConvertI3DL2ToNative**](/windows/desktop/api/xaudio2fx/nf-xaudio2fx-reverbconverti3dl2tonative) function now includes the boolean *sevenDotOneReverb* parameter enabling 7.1 reverb.

## XAudio 2.8 (Windows 8.x)

XAudio2 version 2.8 ships today as a system component in Windows 8, XAUDIO2\_8.DLL. It is available “inbox” and does not require redistribution with an app. We recommend to use the Windows Software Development Kit (SDK) for Windows 8 to develop against XAudio2; the Windows SDK for Windows 8 contains the necessary header and import library for statically linking against XAUDIO2\_8.DLL.

XAudio2 2.8 has been updated with the following changes:

-   This version supports Windows Store app development; the XAudio2 API can be used in C++/DirectX Windows Store apps.
-   [**XAudio2Create**](/windows/desktop/api/xaudio2/nf-xaudio2-xaudio2create) is a flat Win32 API call and no longer creates an XAudio2 CLSID. Support for instantiating XAudio2 by CoCreateInstance has been removed.
-   The Initialize function is now implicitly called by the creation process and has been removed from the [**IXAudio2**](/windows/desktop/api/xaudio2/nn-xaudio2-ixaudio2) interface.
-   Device enumeration functionality has been removed from XAudio2; the GetDeviceDetails and GetDeviceCount functions have been removed from the [**IXAudio2**](/windows/desktop/api/xaudio2/nn-xaudio2-ixaudio2) interface. Apps that want to render to other audio devices on the system must pass a device identifier string to [**CreateMasteringVoice**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2-createmasteringvoice) instead of a device index. The default audio render device can still be created without enumeration.
-   [**IXAudio2MasteringVoice**](/windows/desktop/api/xaudio2/nn-xaudio2-ixaudio2masteringvoice) has an added function [**IXAudio2MasteringVoice::GetChannelMask**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2masteringvoice-getchannelmask) for that returns the channel mask for the destination output device.
-   The [X3DAudio](x3daudio.md) and [XAPOFX](xapofx-overview.md) libraries are merged into XAudio2. App code still uses separate headers, X3DAUDIO.H and XPOFX.H, but now links to a single import library, XAUDIO2\_8.LIB.
-   xWMA support is not available in this version of XAudio2; xWMA will not be supported as an audio buffer format when calling CreateSourceVoice. We now recommend the Media Foundation Source Reader object for decoding a wide variety of media formats into in-memory PCM buffers.
-   [**CreateFX**](/windows/desktop/api/XAPOFX/nf-xapofx-createfx) now takes four parameters rather than two. The newer parameters specify initial data as part of [XAPOFX](xapofx-overview.md) creation.

## XAudio 2.7 and earlier (Windows 7)

All previous versions of XAudio2 for use in apps have been provided as redistributable DLLs in the DirectX SDK. The first version of XAudio2, XAudio2 2.0, shipped in the March 2008 release of the DirectX SDK. The last version to ship in the DirectX SDK was XAudio2 2.7, available in the last release of the DirectX SDK in June 2010.

The legacy DirectX SDK is no longer available on Microsoft Downloads due to the retirement of all SHA-1 signed content. June 2010 was the end-of-life release.

Previous versions of XAudio2 cannot be used to build Windows Store apps for Windows 8.

## Related topics

<dl> <dt>

[Getting Started](getting-started.md)
</dt> <dt>

[XAudio2 Key Concepts](xaudio2-key-concepts.md)
</dt> </dl>

[Developer guide for redistributable version of XAudio 2.9](xaudio2-redistributable.md)
</dt> </dl>
 

 
