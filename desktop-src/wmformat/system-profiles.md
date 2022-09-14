---
title: System Profiles
description: System Profiles
ms.assetid: '5f687aae-cf9b-4b2d-a3aa-d130b443fbf3'
keywords:
- Windows Media Format SDK,system profiles
- Advanced Systems Format (ASF),system profiles
- ASF (Advanced Systems Format),system profiles
- Windows Media Format SDK,profile IDs
- Advanced Systems Format (ASF),profile IDs
- ASF (Advanced Systems Format),profile IDs
- system profiles,list of
- profile IDs
ms.topic: article
ms.date: 05/31/2018
---

# System Profiles

The following table contains the full list of supported system profiles. Each listed profile has a name and a profile ID. The profile ID is a constant set to the GUID value assigned to the system profile. To use the system profile IDs in your code, you must include wmsysprf.h in your application. For examples showing how to load a system profile, see [To Load a System Profile](to-load-a-system-profile.md).

> [!IMPORTANT]
> The profiles listed below all use the version 8 Windows Media Audio and Windows Media Video codecs. There are no predefined system profiles that use the Windows Media 9 Series codecs. You can create your own Windows Media 9 Series profile by using a version 8 profile as a starting point. For more information, see [Reusing Stream Configurations](reusing-stream-configurations.md).

 



| Profile name                                                                      | Profile ID                     | Description                                                                                                                                                         |
|-----------------------------------------------------------------------------------|--------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Windows Media Video 8 for Color Pocket PCs (225 Kbps)                             | WMProfile\_V80\_255VideoPDA    | Use this profile when creating video files for playback on faster color Pocket PCs.                                                                                 |
| Windows Media Video 8 for Color Pocket PCs (150 Kbps)                             | WMProfile\_V80\_150VideoPDA    | Use this profile when creating video files for playback on most Pocket PCs.                                                                                         |
| Windows Media Video 8 for Dial-up Modems or Single-channel ISDN (28.8 to 56 Kbps) | WMProfile\_V80\_28856VideoMBR  | Use this multiple bit rate profile for target audiences with dial-up modems or single-channel ISDN connections (bandwidth is between 28.8 Kbps and 56 Kbps).        |
| Windows Media Video 8 for LAN, Cable Modem, or xDSL (100 to 768 Kbps)             | WMProfile\_V80\_100768VideoMBR | Use this multiple bit rate profile for target audiences with dual-channel ISDN, LAN, cable modem, or xDSL connections (bandwidth is between 100 Kbps and 500 Kbps). |
| Windows Media Video 8 for Dial-up Modems or LAN (28.8 to 100 Kbps)                | WMProfile\_V80\_288100VideoMBR | Use this multiple bit rate profile for target audiences with dial-up modem, LAN, or dual-channel ISDN connections (bandwidth is between 28.8 and 100 Kbps).         |
| Windows Media Video 8 for Dial-up Modems (28.8 Kbps)                              | WMProfile\_V80\_288Video       | Use this profile for low bit rate audio/video delivery over 28.8 Kbps dial-up connections.                                                                          |
| Windows Media Video 8 for Dial-up Modems (56 Kbps)                                | WMProfile\_V80\_56Video        | Use this profile for low bit rate audio/video delivery over 56 Kbps dial-up connections.                                                                            |
| Windows Media Video 8 for Local Area Network (100 Kbps)                           | WMProfile\_V80\_100Video       | Use this profile for medium bit rate delivery over dual-channel ISDN, LAN, or cable modem connections.                                                              |
| Windows Media Video 8 for Local Area Network (256 Kbps)                           | WMProfile\_V80\_256Video       | Use this profile for high quality audio/video content intended for local playback or for download and playback.                                                     |
| Windows Media Video 8 for Local Area Network (384 Kbps)                           | WMProfile\_V80\_384Video       | Use this profile for high quality audio/video content intended for local playback or for download and playback.                                                     |
| Windows Media Video 8 for Local Area Network (768 Kbps)                           | WMProfile\_V80\_768Video       | Use this profile for high quality audio/video content intended for local playback or for download and playback.                                                     |
| Windows Media Video 8 for Broadband (NTSC, 700 Kbps)                              | WMProfile\_V80\_700NTSCVideo   | Use this profile for high quality audio/video content intended for local playback or download and playback.                                                         |
| Windows Media Video 8 for Broadband (NTSC, 1400 Kbps)                             | WMProfile\_V80\_1400NTSCVideo  | Use this profile for high quality audio/video content intended for local playback or for download and playback.                                                     |
| Windows Media Video 8 for Broadband (PAL, 384 Kbps)                               | WMProfile\_V80\_384PALVideo    | Use this profile for high quality audio/video content intended for local playback or for download and playback.                                                     |
| Windows Media Video 8 for Broadband (PAL, 700 Kbps)                               | WMProfile\_V80\_700PALVideo    | Use this profile for high quality audio/video content intended for local playback or for download and playback.                                                     |
| Windows Media Audio 8 for Dial-up Modem (Mono, 28.8 Kbps)                         | WMProfile\_V80\_288MonoAudio   | Use this profile for radio and music content (audio only).                                                                                                          |
| Windows Media Audio 8 for Dial-up Modem (FM Radio Stereo, 28.8 Kbps)              | WMProfile\_V80\_288StereoAudio | Use this profile for radio and music content (audio only).                                                                                                          |
| Windows Media Audio 8 for Dial-up Modem (32 Kbps)                                 | WMProfile\_V80\_32StereoAudio  | Use this profile for radio and music content (audio only).                                                                                                          |
| Windows Media Audio 8 for Dial-up Modem (Near CD quality, 48 Kbps)                | WMProfile\_V80\_48StereoAudio  | Use for radio, music, and general purpose audio content.                                                                                                            |
| Windows Media Audio 8 for Dial-up Modem (CD quality, 64 Kbps)                     | WMProfile\_V80\_64StereoAudio  | Use this profile for target audiences with high speed Internet or LAN connections.                                                                                  |
| Windows Media Audio 8 for ISDN (Better than CD quality, 96 Kbps)                  | WMProfile\_V80\_96StereoAudio  | Use this profile for target audiences with high speed Internet or LAN connections.                                                                                  |
| Windows Media Audio 8 for ISDN (Better than CD quality, 128 Kbps)                 | WMProfile\_V80\_128StereoAudio | Use this profile for target audiences with high speed Internet or LAN connections.                                                                                  |
| Windows Media Video 8 for Dial-up Modem (No audio, 28.8 Kbps)                     | WMProfile\_V80\_288VideoOnly   | Use this profile when creating video-only content for target audiences with dial-up modems.                                                                         |
| Windows Media Video 8 for Dial-up Modem (No audio, 56 Kbps)                       | WMProfile\_V80\_56VideoOnly    | Use this profile when creating video-only content for target audiences with dial-up modems.                                                                         |
| Windows Media 8 Fair Quality based VBR for Broadband                              | WMProfile\_V80\_FAIRVBRVideo   | Fair to high quality based profile for VBR content that is quality constrained.                                                                                     |
| Windows Media 8 High Quality based VBR for Broadband.                             | WMProfile\_V80\_HIGHVBRVideo   | High to best quality based profile for VBR content that is quality constrained.                                                                                     |
| Windows Media 8 Best Quality based VBR for Broadband.                             | WMProfile\_V80\_BESTVBRVideo   | Best quality based profile for VBR content that is quality constrained.                                                                                             |



 

The system profiles are available localized for languages other than English. For more information, see [Localized System Profiles](localized-system-profiles.md).

## Related topics

<dl> <dt>

[**IWMProfileManager::LoadProfileByID**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofilemanager-loadprofilebyid)
</dt> <dt>

[**IWMProfileManager2 Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmprofilemanager2)
</dt> <dt>

[**Working with Profiles**](working-with-profiles.md)
</dt> </dl>

 

 




