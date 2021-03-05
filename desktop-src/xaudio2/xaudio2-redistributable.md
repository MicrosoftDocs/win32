---
description: Developer guide for redistributable version of XAudio 2.9
ms.assetid: 
title: Developer guide for redistributable version of XAudio 2.9
ms.topic: article
ms.date: 10/17/2019
---

# Developer guide for redistributable version of XAudio 2.9

A version of XAudio 2.9 is available as a [NuGet package](/nuget/what-is-nuget). Developers can redistribute this version of XAudio 2.9 with their apps. This allows an app to use XAudio 2.9 on older versions of Windows that do no not include XAudio 2.9 as part of the operating system image. Use of this redistributable is preferred over redistributing XAudio 2.7 from the DirectX SDK, as XAudio 2.7 has not been updated since 2010.

## Supported platforms

The XAudio 2.9 NuGet package (*Microsoft.XAudio2.Redist.\*.nupkg*) includes a 32-bit and a 64-bit version of a DLL that implements the XAudio 2.9 API. The DLL is called XAUDIO2\_9REDIST.DLL. This DLL will work on Windows 7 SP1, Windows 8, Windows 8.1 and Windows 10.

When the DLL is used on a Windows 10 system, it checks the version number of the XAUDIO2\_9.DLL that is part of the operating system, and if the operating system is newer, it will delegate all API calls to XAUDIO2\_9.DLL in the operating system. This ensures that apps always use the latest version of XAudio 2.9 that is available on the current platform.

The DLL is not intended for Xbox One. If used on Xbox One, the DLL will always delegate all API calls to XAUDIO2\_9.DLL in the Xbox One operating system.

The DLL is not intended for UWP apps. UWP apps should use the XAUDIO2\_9.DLL that is part of the operating system.

## Installing the NuGet package

The easiest way to install the NuGet package is to use the [NuGet Package Manager](/nuget/consume-packages/install-use-packages-visual-studio) in Microsoft Visual Studio. If you do this, your Visual Studio project file will be automatically updated to include *Microsoft.XAudio2.Redist.targets*. The *.targets* file adds the Include folder with the header files for the XAudio2 to your collection of project include paths. The *.targets* file will also make your .DLL or .EXE link with XAUDIO2REDIST.LIB and XAPOBASEREDIST.LIB.

The library XAPOBASEREDIST.LIB is only needed if you intend to impement a custom XAudio Processing Object (XAPO) and you can remove it from the *Microsoft.XAudio2.Redist.targets* if it is unused.

You can also use other tools to extract the contents of the NuGet package, or even rename the file extension to .zip and extract the files with any ZIP extractor tool.

## Compiling your app

### Choosing which headers to include

The XAudio 2.9 NuGet package includes the same XAudio2 header files that are included in the Windows 10 SDK. However, the header files have had some adjustments to them to make sure that you can use them while explicitly targeting all [supported platforms](#supported-platforms), including older versions of Windows.

If you [install the NuGet package](#installing-the-nuget-package) using the NuGet Package Manager in Microsoft Visual Studio then the path to the header files is placed in front of the path to the Windows SDK header files. That means that if code in your project includes the XAUDIO2.H header, it will pick up the cross-platform header from the NuGet package. This is normally the desired behavior.

You should be careful if adding the path to the include headers manually to the project, as specifying them in the wrong order can cause the OS-version specific [XAUDIO2.H](/windows/win32/api/xaudio2/) to be included from the Windows SDK, rather than the cross-platform version of XAUDIO2.H.

To make the inclusion of headers less error-prone, the NuGet package contains a version of each header with "REDIST" appended to it. For example, in addition to XAUDIO2.H, the NuGet package also includes XAUDIO2REDIST.H. If you prefer, your code can directly include XAUDIO2REDIST.H to eliminate any ambiguity about which header file is being used. When including the -REDIST.H version of a header file, the order in which the include file directories are listed in the project file do not matter.

Note that if your app is also being compiled for Xbox One, you should continue to include XAUDIO2.H when compiling for Xbox One, as some Xbox One-specific APIs are excluded from XAUDIO2REDIST.H. This NuGet package is not intended for Xbox One.

### Loading the DLL

We recommend that you link your app with XAUDIO2REDIST.LIB and install XAUDIO2\_9REDIST.DLL in the same folder as your app's executable. This will cause XAUDIO2\_9REDIST.DLL to be loaded as soon as your executable is launched. However, if you prefer, you may use [**LoadLibraryEx**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibraryexw) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) to load XAUDIO2\_9REDIST.DLL on demand. This is a good solution if your app does not always need to use the XAudio2 APIs. But if you do this, you should keep the XAUDIO2\_9REDIST.DLL loaded until the app exits, as attempting to unload the DLL can cause a crash if a background thread is still executing code in the DLL.

Unlike the older XAudio 2.7, it is not possible to use CoCreateInstance to load the DLL.

### Verifying the DLL signature

The XAUDIO2\_9REDIST.DLL binary is signed by Microsoft using a SHA-2 signature. Any code that attempts to validate the signature, e.g., anti-cheat modules for games, therefore needs to support SHA-2. Note that Windows 7 SP1 did not originally support SHA-2 and requires an update to add that functionality. The update is available as [KB4474419](https://support.microsoft.com/help/4474419/sha-2-code-signing-support-update).

## Testing

### Spatial sound in newer versions of Windows 10

Starting with the Windows 10 1903 update, XAudio 2.9 automatically uses [virtual surround sound](#spatial-sound-and-virtual-surround), if certain conditions are satisfied. We recommend testing game that generate multi-channel sound on Windows 10 1903 (or newer) to verify that the game sounds as expected.

#### Enabling spatial sound

The user can enable a spatial sound format by right-clicking on the speaker icon in the Windows system tray. 

XAudio 2.9 will only use the user's selected spatial sound format if the process that is using the XAudio2 API is recognized as a game by the Windows Game Bar. During development, it is possible that the process is not yet recognized as a game by the Game Bar. To change this, use the Win+G keyboard short-cut to bring up the Game Bar while the game is running. Then click on the "Settings" icon and check the checkbox that says, "Remember that this is a game".

#### Opting out from spatial sound

There is a way to opt out from having XAudio2 use the spatial sound encoder by specifying certain values for the [**AUDIO_STREAM_CATEGORY**](/windows/win32/api/audiosessiontypes/ne-audiosessiontypes-audio_stream_category) parameter in [**IXAudio2::CreateMasteringVoice**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2-createmasteringvoice). 

Spatial sound is enabled for these categories:

* AudioCategory_ForegroundOnlyMedia
* AudioCategory_GameEffects
* AudioCategory_GameMedia
* AudioCategory_Movie
* AudioCategory_Media

Spatial sound is not enabled if any of the following categories are specified:

* AudioCategory_Other
* AudioCategory_Communications
* AudioCategory_Alerts
* AudioCategory_SoundEffects
* AudioCategory_GameChat
* AudioCategory_Speech

### Error handling

It is important to test that you game can handle a change in audio device, for example, when headphones are plugged in, or unplugged. This should be tested with headphones that only support 44.1 kHz sampling rate. Many low-end USB headphones and Bluetooth headsets only support 44.1 kHz. The transition between 48 kHz sampling rate and 44.1 kHz sampling rate can cause an error even when the [virtual audio endpoint](#virtual-audio-endpoint) feature is used. The error will not happen if the headphones also support 48 kHz. Note that the virtual audio endpoint feature is not available on Windows 7 SP1.

The error code returned by XAudio 2.9 when it cannot automatically recover from a change in audio endpoint is [XAUDIO2\_E\_DEVICE\_INVALIDATED](xaudio2-error-codes.md). However, we recommend that apps do not hard-code a dependency on the error code having a specific value.

To be notified of the error, the app should implement the [**IXAudio2EngineCallback**](/windows/desktop/api/xaudio2/nn-xaudio2-ixaudio2enginecallback) interface and provide a pointer to that interface by invoking the [**IXAudio2::RegisterForCallbacks**](xaudio2-callbacks.md) method. The app's implementation of the [**IXAudio2EngineCallback::OnCriticalError**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2enginecallback-oncriticalerror) will be invoked by the XAudio2 API if an error occurs during playback.

Note that [**IXAudio2EngineCallback::OnCriticalError**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2enginecallback-oncriticalerror) is not necessarily invoked if the audio pipeline is paused. For example, if the user minimizes the app, or the app gets suspended for any reason, audio playback might be paused. If the change in audio device happens during this time, the error is only returned when the app invokes [**IXAudio2::StartEngine**](/windows/desktop/api/xaudio2/nf-xaudio2-ixaudio2-startengine) and/or invokes [**IXAudio2SourceVoice::Start**](/windows/desktop/api/xaudio2/nf-xaudio2-ixaudio2sourcevoice-start). If playback can be paused with your app, you should test changing the audio device while the playback is paused, to verify that the app still can recover from this situation.

## XAudio 2.9 API differences compared to XAudio 2.7

This section provides a summary of some of the API differences between XAudio 2.7 and the redistributable version of XAudio 2.9.

### Supported formats

XAudio 2.9 supports these input formats on PC:

* Linear 16-bit PCM
* Linear 32-bit Float PCM
* 16-bit ADPCM
* xWMA

The XMA format is only supported on Xbox One.

### Preferred CPU core

It is possible to specify which CPU core XAudio 2.9 should use for its audio processing thread. However, it is usually preferred to let XAudio 2.9 choose this value by itself. This is done by setting the **XAudio2Processor** parameter in the call to [**XAudio2Create**](/windows/desktop/api/xaudio2/nf-xaudio2-xaudio2create) to XAUDIO2\_USE\_DEFAULT\_PROCESSOR. 

XAudio 2.9 will choose a different CPU core on Xbox One than on PC. The IXAudio2Extension::GetProcessor method can be used to determine which CPU core XAudio2 has chosen.

### Virtual audio endpoint

XAudio 2.9 will use a virtual audio endpoint by default, when running on Windows 8 or later. This means that if the default audio endpoint changes while XAudio 2.9 is used, it will attempt to automatically switch to the new audio endpoint. An example of when this can happen when the default audio endpoint is a pair of headphones that are connected over USB, and then the user unplugs the headphones. This will cause the speakers to be the new default audio endpoint.

If the app specifies a specific audio format when invoking [**IXAudio2::CreateMasteringVoice**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2-createmasteringvoice), it may not be possible for XAudio 2.9 to perform this switch. For example, if the app specified that the Mastering Voice shall use a 48 kHz sampling rate and the new audio device only supports 44.1 kHz, then the automatic switch will fail, and XAudio 2.9 will report the [XAUDIO2\_E\_DEVICE\_INVALIDATED](xaudio2-error-codes.md) error.

It is possible for the app to opt out of using the virtual audio endpoint by passing in the [**XAUDIO2\_NO\_VIRTUAL\_AUDIO\_CLIENT**](xaudio2-boundary-values-and-flags.md) flag to [**IXAudio2::CreateMasteringVoice**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2-createmasteringvoice).

Virtual audio endpoints are not available on Windows 7 SP1. The **XAUDIO2\_NO\_VIRTUAL\_AUDIO\_CLIENT** flag has no effect on Windows 7 SP1.

### Audio categories

The app should specify a category for its audio stream. This is done by providing a value from the AudioCategory enumeration when invoking the [**IXAudio2::CreateMasteringVoice**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2-createmasteringvoice) method. For example, AudioCategory_GameEffects. The audio category can affect how Windows processes the sound or how it represents the audio stream in the volume control panel. The audio category also affects if [virtual surround sound](#spatial-sound-and-virtual-surround) is automatically enabled.

### Duration of audio processing quantum

On most PCs, XAudio 2.9 processes audio in 10 millisecond chunks. This is called the processing quantum. However, the duration of this quantum may be different than 10 milliseconds on some hardware. Apps that need to know the exact quantum can invoke the IXAudio2Extension::GetProcessingQuantum method to retrieve the value.

### Spatial sound and virtual surround

Starting with the Windows 10 1903 update, XAudio 2.9 automatically uses virtual surround sound, if certain conditions are satisfied. We recommend testing game that generate multi-channel sound on Windows 10 1903 (or newer) to verify that the game sounds as expected. See the [testing spatial sound](#spatial-sound-in-newer-versions-of-windows-10) section for a discussion about how to test this feature.

Normally, XAudio 2.9 performs a folds down any multi-channel audio to match the "physical" number of audio channels that are supported by the audio endpoint. For example, if the game provides a 7.1 channel audio source, but the sound is played on headphones, XAudio 2.9 will fold down the 7.1 channel audio into stereo, using an industry standard fold-down matrix. If the PC is connected to a HDMI audio endpoint, then the 7.1 channel audio will be transmitted as-is over the HDMI connection.

Windows 10 adds support for spatial audio, using a centralized encoder that encodes audio into a user-selected [spatial sound](../coreaudio/spatial-sound.md) format. Windows 10 comes included with a spatial sound format called Windows Sonic. Other formats, such as Dolby Atmos for Headphones, can be downloaded from the Microsoft Store. Some of the spatial sound formats, such as Windows Sonic and Dolby Atmos for Headphones, are designed to be used on stereo audio endpoints. These formats fold down surround sound to stereo using proprietary algorithms that achieve a "virtual" surround sound effect. In other words, the listener can perceive sound appearing from different positions in 3D space even while only wearing headphones, or while listening on a single pair of stereo speakers.

Similar effects can be achieved using the [X3DAudio](x3daudio.md) APIs that are included with XAudio 2.9. The main difference is that X3DAudio requires the app developer to explicitly program for 3D audio, whereas virtual surround sound is applied automatically to any tradional channel-based sound source.

On Windows 10 1903, and newer, games that use XAudio 2.9 will use the system-wide spatial sound format that the user has enabled on the audio endpoint, if any. This means that XAudio 2.9 will not perform the usual fold-down of surround sound to stereo. Instead, the surround sound signal will be delivered to the spatial sound encoder (e.g., Windows Sonic) to achieve a virtual surround sound effect.

### CreateHrtfApo

The [**CreateHrtfApo**](/windows/desktop/api/HrtfApoApi/nf-hrtfapoapi-createhrtfapo) function is only available on Windows 10. It is not implemented in the XAudio 2.9 redistributable.
