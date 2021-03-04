---
description: About the Windows Media Codecs
ms.assetid: C0B0265C-AD20-433B-A554-112AEB0208B9
title: About the Windows Media Codecs
ms.topic: article
ms.date: 05/31/2018
---

# About the Windows Media Codecs

-   [Windows Media Audio Codecs](#windows-media-audio-codecs)
    -   [Windows Media Audio 9](#windows-media-audio-9)
    -   [Windows Media Audio 10 Professional](#windows-media-audio-10-professional)
    -   [Windows Media Audio 9 Lossless](#windows-media-audio-9-lossless)
    -   [Windows Media Audio 9 Voice](#windows-media-audio-9-voice)
    -   [Compatibility](#compatibility)
-   [Windows Media Video 9 Series Codecs](#windows-media-video-9-series-codecs)
    -   [Windows Media Video 9](#windows-media-video-9-series-codecs)
    -   [Windows Media Video 9 Screen](#windows-media-video-9-screen)
    -   [Windows Media Video 9 Image Version 2](#windows-media-video-9-image-version-2)
    -   [Windows Media Video 9 VCM](#windows-media-video-9-vcm)
    -   [Compatibility](#compatibility)
-   [Related topics](#related-topics)

## Windows Media Audio Codecs

### Windows Media Audio 9

This codec samples audio at 44.1 or 48 kilohertz (kHz) using 16 bits, similar to the current CD standard, offering CD quality at data rates from 64 to 192 kilobits per second (Kbps). The resulting sound quality is 20 percent better than audio sampled with Windows Media Audio 8 at equivalent data rates.

The Windows Media Audio 9 codec (WMA 9) supports variable bit rate encoding (VBR), which enables even higher quality audio at smaller file sizes by automatically varying the encoding bit rate according to the complexity of the audio data. With VBR, the encoding bit rate increases to capture complex sections of data and then decreases to maximize the compression of the less complex sections, producing compact, high-quality compression.

WMA 9 is backward-compatible with previous Windows Media Audio-compatible decoders, which means that WMA 9 content can be played with previous versions of Windows Media Player or older consumer electronic devices that support Windows Media. As with all Windows Media 9 Series codecs, it supports the Windows Media digital rights management platform, which is used to securely package and distribute copy-protected digital media.

### Windows Media Audio 10 Professional

Windows Media Audio 10 Professional (WMA 10 Pro) is the most flexible Windows Media audio codec available – supporting profiles that include everything from full-resolution 24-bit/96 kHz audio in stereo, 5.1 channel, or even 7.1 channel surround sound, to highly efficient mobile capabilities at 24 Kbps to 96 Kbps for stereo, and 128 Kbps to 256 Kbps for 5.1-channel sound. WMA 10 Pro offers incredible quality for consumers using high-fidelity hardware and 5.1 channel surround sound-equipped computers — and for consumers playing audio content on their mobile devices. WMA 10 Pro supports streaming, progressive download, or download-and-play delivery at 128 to 768 Kbps.

When using 5.1 surround sound audio compressed at 384 Kbps with WMA 10 Pro, most listeners cannot discern any differences between the compressed music and the original pulse code modulation (PCM) files. WMA Pro also offers dynamic range control using the maximum and average audio amplitudes that are calculated during the encoding process. Using the Quiet Mode feature in Windows Media Player 9 and later, users can hear either the full dynamic range, a medium difference range up to 12 decibels (dB) above the average, or a little difference range up to 6 dB above the average.

If a user tries to play back a file that was encoded using the 5.1 channel, 24-bit, 96 kHz sampling capabilities, but does not have a system or sound card that supports multi-channel or high-resolution sound, multiple channels are combined into stereo audio (for example, 16-bit, two channel audio), ensuring that users get the best playback experience their systems can provide.

The following table compares WMA Pro to competing compression technology.



| Audio Data              | Industry Compression\*        | Windows Media\*            | Compression Savings |
|-------------------------|-------------------------------|----------------------------|---------------------|
| 2 ch x 48 kHz x 16 bits | Dolby Digital 2.0 at 220 Kbps | WMA 10 Pro at 128 Kbps     | 1.7:1               |
| 6 ch x 48 kHz x 20 bits | Dolby Digital 5.1 at 384 Kbps | WMA 10 Pro at 192–256 Kbps | 1.5–2:1             |
| 6 ch x 48 kHz x 24 bits | DTS 5.1 at 1,536 Kbps         | WMA 10 Pro at 768 Kbps     | 2:1                 |



 

\* Content dependent

### Windows Media Audio 9 Lossless

The audio quality of content that is compressed using this codec is the best of all Windows Media Audio codecs. It creates a bit-for-bit duplicate of the original audio file so that no data is lost, which makes it ideal for archiving content masters.

Depending on the complexity of the original, content will be compressed at a 2:1 or 3:1 ratio. Although this is lower than the ratio achieved with other Windows Media Audio 9 Series codecs, it provides the same benefits of compression while leaving the data intact.

Like Windows Media Audio 9 Professional, the Windows Media Audio 9 Lossless codec also offers dynamic range control using the maximum and average audio amplitudes that are calculated during the encoding process. Using the Quiet Mode feature in Windows Media Player 9 and later, users can hear the full dynamic range, a medium difference range up to 12 dB above the average, or a little difference range up to 6 dB above the average.

### Windows Media Audio 9 Voice

This low-bit-rate codec is primarily targeted for speech content, but performs very well with mixed-mode content that includes both voice and music. In voice mode, the codec takes advantage of the relatively less complicated and narrower frequency range of the human voice to maximize compression. In music mode, the codec operates like the standard Windows Media Audio 9 codec. Encoded content can be configured to switch between voice and music modes automatically.

The Windows Media Audio 9 Voice codec offers superior quality for low-bit-rate streaming scenarios (less than 20 Kbps), such as radio broadcasts, advertising, e-books, podcasts, and voiceovers. The voice codec can also compress content to as low as 4 Kbps at 8 kHz.

### Compatibility

The following table outlines what your audience will experience when playing Windows Media Audio 9 Series content on earlier Microsoft Windows operating systems than Windows XP or with earlier versions of Windows Media Player. This table also lists the compatibility for Apple Mac OS X and Windows CE–based platforms.



| Codec                              | Feature                                       | Player backward compatibility                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|------------------------------------|-----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Windows Media Audio 9              | Constant-bit rate (CBR) encoding              | <dl> <dt>Windows Media Player 6.4 or later on non-portable devices (using transcoding as needed)</dt> <dt>Windows Media Player 9 for Mac OS X</dt> <dt>Windows Media Player 9 Series and Windows Media Player 9.1 for Pocket PC\*</dt> <dt>Windows Media Player 9 Series and Windows Media Player 9.1 for Smartphone\*</dt> </dl> |
|                                    | Variable-bit-rate (VBR) encoding              | Windows Media Player 7 or later on all devices that support the Player (using transcoding as needed)                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Windows Media Audio 9 Professional | General                                       | <dl> <dt>Windows Media Player 7 or later</dt> <dt>Windows Media Player 9 for Mac OS X</dt> </dl>                                                                                                                                                                                                                                                                                                                          |
|                                    | Discrete channel playback (for instance, 5.1) | Requires Windows Media Player 9 Series (or SDK) or later, Windows XP, and a multichannel audio card.                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                    | High-resolution audio (24-bit, 96 kHz)        | Requires Windows Media Player 9 Series (or SDK) or later, Windows XP, and a high-resolution audio card.                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                    | Dynamic range control                         | Requires Windows Media Player 9 Series (or SDK) or later and Windows XP.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Windows Media Audio 9 Lossless     | General                                       | <dl> <dt>Windows Media Player 7 or later</dt> <dt>Windows Media Player 9 for Mac OS X</dt> </dl>                                                                                                                                                                                                                                                                                                                          |
|                                    | Discrete channel playback (for instance, 5.1) | Requires Windows Media Player 9 Series (or SDK) or later, Windows XP, and a multichannel audio card.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Windows Media Audio 9 Voice        | General                                       | <dl> <dt>Windows Media Player 6.4 or later</dt> <dt>Windows Media Player 9 for Mac OS X</dt> <dt>Windows Media Player 9 Series and Windows Media Player 9.1 for Pocket PC\*</dt> <dt>Windows Media Player 9 Series and Windows Media Player 9.1 for Smartphone\*</dt> </dl>                                                       |



 

> [!Note]  
> \* All versions of Windows Media Player for Pocket PC and Smartphone are shipped as part of the Microsoft Windows Mobile operating system. Windows Media Player for Pocket PC and Windows Media Player for Smartphone are not available for download from Microsoft.

 

## Windows Media Video 9 Series Codecs

In 2006, the Society of Motion Picture and Television Engineers (SMPTE) formally published the Final Specification for SMPTE 421M, also known as VC-1. Formal standardization of VC-1 represents the culmination of years of technical scrutiny by over 75 companies, leading to a codec that is well-documented, extremely stable, easily licensable, and accepted by the industry. VC-1 supports three profiles: Simple, Main, and Advanced. The Simple and Main profiles have been complete for several years, and existing implementations such as WMV 9 have long supported the creation and playback of content using these profiles, as well as an early implementation of the Advanced profile. The completion of the Advanced profile and consequent standardization of all profiles in VC-1 represents the final step in a comprehensive specification that delivers high definition content—either interlaced or progressive—across any medium and to any capable device.

### Windows Media Video 9

Windows Media Video 9 is the Microsoft implementation of the VC-1 SMPTE standard. It supports Simple, Main, and Advanced profiles.

### Simple and Main Profiles

The Windows Media Video 9 Simple and Main profiles fully conform to the SMPTE VC-1 standard and provide high-quality video for streaming and downloading. These profiles support a wide range of bit rates, from high-definition content at one-half to one-third the bit rate of MPEG-2, to low-bit-rate Internet video delivered over a dial-up modem. This codec also supports professional-quality downloadable video with two-pass and variable bit rate (VBR) encoding. Windows Media Video 9 is already supported by a wide variety of players and devices.

### Advanced Profile

The Windows Media Video 9 Advanced profile fully conforms to the SMPTE VC-1 standard, supports interlaced content, and is transport-independent. Content creators can use this profile to deliver either progressive or interlaced content at data rates as low as one-third that of the MPEG-2 codec—with the same quality as MPEG-2.

In the past, interlaced video content was always de-interlaced before encoding with the Windows Media Video codec. Now, encoding applications such as Windows Media 9 Series, and third-party encoding solutions can support compression of interlaced content without first converting it to progressive content. Maintaining interlacing in an encoded file is important if the content is ever rendered on an interlaced display, such as a television.

Transport independence also enables the delivery of Windows Media Video 9 Advanced Profile over systems that are not Windows Media-based, such as standards-based broadcast infrastructures (through native MPEG-2 transport streams), wireless infrastructures (using real-time transfer protocol \[RTP\]), or even DVDs.

The following table compares Windows Media Video 9 Advanced Profile to competing compression technology.



| Video Data                                                  | Industry Compression\* | Windows Media\*                                      | Compression Savings |
|-------------------------------------------------------------|------------------------|------------------------------------------------------|---------------------|
| 480/24p 720x480 pixels/frame x 8 bits per channel x 24 fps  | MPEG-2 at 4–6 Mbps     | Windows Media Video 9 Advanced Profile at 1.3–2 Mbps | 3:1                 |
| 480/30i 720x480 pixels/frame x 8 bits per channel x 30 fps  | MPEG-2 at 6–8 Mbps     | Windows Media Video 9 Advanced Profile at 2–4 Mbps   | 2–3:1               |
| 720/24p 1280x720 pixels/frame x 8 bits per channel x 24 fps | MPEG-2 at 19 Mbps      | Windows Media Video 9 Advanced Profile at 5–8 Mbps   | 2.4–3.8:1           |



 

\*Content dependent

### Windows Media Video 9 Screen

The Windows Media Video 9 Screen codec is optimized for compressing sequential screen shots and highly static video that is captured from the computer display, which makes it ideal for delivering demos or demonstrating computer use for training. The codec takes advantage of the typical image simplicity and relative lack of motion to achieve a very high compression ratio.

During the encoding process, the codec automatically switches between lossy and lossless encoding modes, depending on the complexity of the video data. For complex data, the lossless mode preserves an exact copy of the data. For less complex data, the lossy mode discards some data to achieve a higher compression ratio. By automatically switching between these two modes, the codec maintains video quality while maximizing compression.

Overall, the Windows Media Video 9 Screen codec delivers better handling of bitmap images and screen motion, even on relatively modest CPUs. It is also up to 100 times more efficient than the commonly-used run length encoding.

### Windows Media Video 9 Image Version 2

The Windows Media Video 9 Image Version 2 codec is different from the other video codecs. Instead of processing uncompressed video, it transforms still images into video by using pan, zoom, and cross-fade transitions between clips to create an unlimited number of effects.

The results can then be delivered at data rates as low as 20 kilobits per second (Kbps). These files are compressed using either constant bit rate (CBR) or one-pass variable bit rate (VBR) modes.

> [!Note]  
> The Windows Media Video 9 Image Version 2 codec is not compatible with the Windows Media Video 9 Image codec.

 

### Windows Media Video 9 VCM

The Video Compression Manager (VCM) version of the Windows Media Video 9 Series codec enables earlier versions of encoding and editing applications to support the Windows Media Video 9 Series codec in file containers such as Audio Video Interleaved (AVI). This codec package also allows Windows Media Video (WMV) files based on Windows Media Format 9 Series to be played in Windows Media Player 6.4, in both ASF and AVI file containers.

### Compatibility

The following table outlines what your audience will experience when playing Windows Media Video 9 Series content on earlier Microsoft Windows operating systems or with earlier versions of Windows Media Player. This table also lists the compatibility for Apple Mac OS X and Windows CE–based platforms.



| Codec                                  | Feature             | Player backward compatibility                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|----------------------------------------|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Windows Media Video 9                  | General             | <dl> <dt>Windows Media Player 6.4 or later</dt> <dt>Windows Media Player 9 for Mac OS X</dt> <dt>Windows Media Player 9 Series and Windows Media Player 9.1 for Pocket PC\*</dt> <dt>Windows Media Player 9 Series and Windows Media Player 9.1 for Smartphone\* </dt> </dl> |
|                                        | Frame Interpolation | Requires Windows Media Player 9 Series (or Software Development Kit) or later and Windows XP.                                                                                                                                                                                                                                                                                                                                                                           |
| Windows Media Video 9 Advanced Profile | General             | Windows Media Player 7 or later                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Windows Media Video 9 Screen           | General             | Windows Media Player 7 or later                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Windows Media Video 9 Image Version 2  | General             | Windows Media Player 7 or later                                                                                                                                                                                                                                                                                                                                                                                                                                         |



 

> [!Note]  
> \*All versions of Windows Media Player for Pocket PC and Smartphone are shipped as part of the Microsoft Windows Mobile operating system. Windows Media Player for Pocket PC and Windows Media Player for Smartphone are not available for download from Microsoft.

 

## Related topics

<dl> <dt>

[Windows Media Codecs](windows-media-codecs.md)
</dt> </dl>

 

 



