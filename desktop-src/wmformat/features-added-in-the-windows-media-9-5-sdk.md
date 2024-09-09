---
title: Features Added in the Windows Media 9.5 SDK
description: Features Added in the Windows Media 9.5 SDK
ms.assetid: 1525132c-8aa1-42bb-9552-41531fb83055
keywords:
- Windows Media Format SDK,features
- Windows Media Format SDK,new features
- Windows Media Format SDK,interface for application-specific processing
- Windows Media Format SDK,DirectX Video Acceleration (DXVA)
- Windows Media Format SDK,IWMPlayerHook interface
- IWMPlayerHook
- Windows Media Format SDK,x64-based versions of Windows
- Windows Media Format SDK,Windows Media Video Image codec
- Windows Media Format SDK,audio codecs
- Windows Media Format SDK,DRM 10 for Network Devices
- Windows Media Format SDK,DRM licenses
- Windows Media Format SDK,Advanced Profile codec
- Windows Media Format SDK,Sony/Philips Digital Interconnect Format (S/PDIF)
- Windows Media Format SDK,low-delay formats
- Windows Media Format SDK,approximate seeking mode
- Windows Media Format SDK,playlist burning
- Windows Media Format SDK,multiple language support
- Windows Media Format SDK,Windows Media Device Manager SDK
- Windows Media Format SDK,codec interfaces
- codecs,Windows Media Video Image
- digital rights management (DRM),Network Devices secure transfer protocol
- DRM (digital rights management),Network Devices secure transfer protocol
- digital rights management (DRM),licenses
- DRM (digital rights management),licenses
- codecs,Advanced Profile codec
- Sony/Philips Digital Interconnect Format (S/PDIF),transferring or transmitting using
- S/PDIF (Sony/Philips Digital Interconnect Format),transferring or transmitting using
- approximate seeking mode
- metadata,multiple-language support
- Windows Media Device Manager SDK
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Features Added in the Windows Media 9.5 SDK

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Windows Media Format 9.5 SDK introduced new features to provide enhanced content security and flexibility. The following changes were made to the SDK since the 9 Series release.

## New Interface for Application-specific Processing During DirectX Video Acceleration

Player applications that support DirectX Video Acceleration can now implement the [**IWMPlayerHook**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmplayerhook) interface to perform application-specific processing during DirectX VA decoding. The reader calls the [**IWMPLayerHook::PreDecode**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmplayerhook-predecode) callback method before passing compressed video samples to the video processor for decoding.

> [!Note]  
> To use the **IWMPlayerHook** interface and the associated [**IWMReaderAdvanced5**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreaderadvanced5) interface, you must have update number 888656 installed in the Windows Media Format SDK. You can download the update from the [Microsoft Web site](https://support.microsoft.com/?id=888656).

 

## Windows Media Format SDK version for x64-based versions of Windows

An x64-based version of the Windows Media Format SDK is available. This documentation applies to both the 32-bit versions and the x64-based version of the SDK. However, digital rights management (DRM) is not supported in the x64-based Windows Media Format SDK.

## New Version of the Windows Media Video Image Codec

The Windows Media Video 9 Image v2 codec simplifies the sample geometry calculations for panning and zooming. The new codec also supports several complex transitions between images.

## New Version of the Windows Media Audio Codecs

The Windows Media Format 9.5 SDK includes the following updated audio codecs:

-   Windows Media Audio 9.1
-   Windows Media Audio 9.1 Professional
-   Windows Media Audio 9.1 Lossless

## Windows Media DRM 10 for Network Devices Protocol Support

The Windows Media Format 9.5 SDK supports the new Windows Media DRM 10 for Network Devices secure transfer protocol. This protocol can be used to stream encrypted content over a local network to a playback device, such as a set-top video receiver.

Most of the procedures used to implement support for Windows Media DRM 10 for Network Devices must be performed by the application. However, you can use methods of the Windows Media Format SDK to provide the following functionality:

-   Maintain a database of devices, including those that are enabled for Windows Media DRM 10 for Network Devices.
-   Validate devices to ensure that they are "near" enough to the client on the network for secure streaming.
-   Convert DRM-protected files to Windows Media DRM 10 for Network Devices streams.
-   Write files using previously encrypted data.

## Support for New DRM Licenses

New licenses created by using the Windows Media Rights Manager SDK use Output Protection Levels (OPLs) to specify rights and restrictions for playing and copying content. The Windows Media Format SDK provides support for reading the OPLs from a license.

## New Video Codec

The Windows Media Video 9 Advanced Profile codec builds on the high quality of the Windows Media Video 9 codec while adding support for interlaced encoding.

## S/PDIF Output

Content encoded with one of the Windows Media Audio Professional codecs can now be transferred or transmitted using the Sony/Philips Digital Interconnect Format (S/PDIF).

## Low-Delay Audio

The Windows Media Audio 9.1 and Windows Media Audio 9.1 Professional codecs now each support several low-delay formats. These formats produce audio streams that can be started more quickly, reducing latency in stream-switching scenarios. Overall latency in live broadcasts is also improved by using low-delay formats.

## Approximate Seeking Mode

You can now seek to an approximate time in an ASF file with the reader. This mode improves performance when performing an imprecise seek, such as when a user clicks the seek bar in Windows Media Player. Approximate seeking returns the media sample for the previous cleanpoint instead of reconstructing the sample for the precise time sought.

## Playlist Burning

Windows Media DRM 10 supports rights for copying audio files to Red Book CD as part of a playlist. The Windows Media Format SDK provides methods for verifying whether the files in a playlist are allowed to be copied.

## Improved Multiple-Language Support for Metadata

In the Windows Media Format 9 Series SDK, all metadata added to a file was assigned to a language list that was given the language identifier of the default language. This caused problems when content distributors in different locales added some metadata, because users in the distributor's locale only see the few attributes added for their language. The Windows Media Format 9.5 SDK solves this problem by not creating a language list until there are attributes from two languages present in the file. At that point, all of the metadata is associated with the locale of the second language, which then becomes the default. In this way, a content distributor can keep all of the original metadata for a file, such as title and author, intact while adding some attributes pertinent to their locale.

## Windows Media Device Manager SDK Included in Installation

The installation package for the Windows Media Format 9.5 SDK installs the Windows Media Device Manager SDK. The documentation for the Windows Media Device Manager SDK can be found in the C:\\WMSDK\\WMFSDK95\\WMDM\\docs folder (your folder will be different if you do not install the Windows Media Format SDK in the default folder.)

## Codec Interface Documentation

This documentation includes information about using the Windows Media Audio and Video codecs outside of the Windows Media Format SDK. This documentation was originally released as part of a download from the Microsoft Developer Network. The sample applications that demonstrate using the codec DMOs directly are included in the Windows Media Format SDK installation along with headers.

## Related topics

<dl> <dt>

[**About the Windows Media Format SDK**](about-the-windows-media-format-sdk.md)
</dt> </dl>

 

 




