---
description: Learn how to detect audio format capabilities for communications scenarios
title: Detect audio format capabilities for communications scenarios
ms.topic: concept-article
ms.date: 05/31/2018
---

# Detect audio format capabilities for communications scenarios

Some audio devices, such as Bluetooth devices, change their supported audio formats (channel count, sample rate, etc.) for capture or playback when the device is used in Communications mode. Such devices may enter Communications mode when the stream is explicitly categorized as a communications stream or when a microphone stream is opened.

For example, Bluetooth devices switch into bidirectional operation when used in Communications mode. Depending on the Bluetooth technology used (Classic Audio or LE Audio), the capabilities of the Bluetooth audio device, and the capabilities of the Bluetooth and Audio subsystems in the Windows PC, the sample rate and number of audio channels supported may vary.

Applications may wish to know the exact sample rate of an audio stream in Communications mode to optimize audio encoding. Similarly, applications may wish to know if stereo playback is supported while the microphone is used, to decide if features that depend on stereo playback (like Spatial Audio) are available to the user.

# Audio device behaviors in communications scenarios

Applications using audio devices (microphone or output endpoints) for communications purposes should categorize streams as [AudioCategory_Communications](/windows/win32/api/audiosessiontypes/ne-audiosessiontypes-audio_stream_category). Categorizing the stream correctly allows Windows to operate the device in the correct mode and to set appropriate latency parameters (when applicable for the audio device type). It also engages the right user experience behavior in the OS (such as ducking) and enables engaging of audio signal processing and formats optimized for the device and audio category. Finally, it allows the application to query what audio signal formats (channels, sample rate, bit depth, etc.) are being used.

Bluetooth devices have expected behaviors based on Bluetooth standards. Other types of audio devices may have varying behaviors depending on their hardware or software design.

## Bluetooth classic Audio behaviors

When using Bluetooth Classic Audio for communications scenarios, the Hands Free Profile (HFP) is used. When using HFP, both capture and output endpoints operate in mono - meaning Bluetooth Classic audio devices cannot support stereo playback while the microphone is in use.

Windows 11 supports both Continuously Variable Slope Delta (CVSD) at 8kHz (narrowband voice) and modified Sub Band Coding (mSBC) at 16kHz (wideband voice). The codec and sample rate selection depends on the capabilities of the Bluetooth and Audio subsystems in the Windows PC and of the Bluetooth audio device. Most modern PCs and Bluetooth audio devices support wideband voice.

See [Bluetooth Classic audio](/windows-hardware/drivers/bluetooth/bluetooth-classic-audio) for more information about HFP and the scenarios that cause it to be used.

## Bluetooth LE Audio behaviors

When using Bluetooth LE Audio for communications scenarios, the Telephony and Media Profile (TMAP) or Hearing Access Profile (HAP) is used.

Some Windows 11 PCs can stream stereo playback audio to Bluetooth LE Audio devices while the microphone is in use. When stereo is not supported by the OS or Bluetooth and Audio subsystems in the PC, or the user has manually configured their device to operate in 1 channel mode, playback operates in mono mode while the microphone is in use.

During communications scenarios, Windows streams audio at 32kHz to and from Bluetooth audio devices that support TMAP, and at 16kHz or 24kHz to and from Bluetooth audio devices that support HAP. In the future, additional sample rates may be supported by Windows.

For more information about Bluetooth LE Audio support in Windows 11, see See [Bluetooth Low Energy (LE) Audio](/windows-hardware/drivers/bluetooth/bluetooth-low-energy-audio).

## Application guidance and samples

The [IMMDeviceEnumerator](/windows/win32/api/mmdeviceapi/nn-mmdeviceapi-immdeviceenumerator) interface can be used to enumerate and select audio endpoints.

When opening a stream, the [SetClientProperties](/windows/win32/api/audioclient/nf-audioclient-iaudioclient2-setclientproperties) method can be used to categorize communications streams as **AudioCategory_Communications**.

Applications can query the stream format details (channel count, sample rate, etc.) using the [GetMixFormat](/windows/win32/api/audioclient/nf-audioclient-iaudioclient-getmixformat) method.

**GetMixFormat** may not return the correct channel count for Bluetooth LE Audio output endpoints on Windows 11 builds prior to Windows build 26100.4484. Applications relying on the methods shown below to retrieve the channel count for Bluetooth LE Audio output endpoints should only do so when running on build numbers equal to or above this.

```cpp
HRESULT PrintFormatDetailsForDevice(IMMDevice* audioDevice)
{
    // Variables
    HRESULT ReturnCode;
    IAudioClient2* AudioClient = nullptr;
    WAVEFORMATEX* FormatDetails = nullptr;

    // Open audio device
    ReturnCode = audioDevice->Activate(
        __uuidof(IAudioClient2), CLSCTX_ALL,
        nullptr, (void**)&AudioClient);

    // Create an AudioClientProperties with Communications category set
    AudioClientProperties clientProps = {};
    clientProps.cbSize = sizeof(AudioClientProperties);
    clientProps.eCategory = AudioCategory_Communications;

    // Set properties on the audio device
    ReturnCode = AudioClient->SetClientProperties(&clientProps);
    if (FAILED(ReturnCode)) 
    {
        std::wcerr << L"Warning: Failed to set Communications category: " << HResultToString(ReturnCode) << std::endl;
    }
    else 
    {
        // Query the mix format and print
        ReturnCode = AudioClient->GetMixFormat(&FormatDetails);
        if (FAILED(ReturnCode)) 
        {
            std::wcerr << L"Failed to get mix format: " << HResultToString(ReturnCode) << std::endl;
        }
        else 
        {
            if (FormatDetails != nullptr) 
            {
                std::wcout << L"Sample Rate: " << FormatDetails->nSamplesPerSec << L" Hz" << std::endl;
                std::wcout << L"Channels:    " << FormatDetails->nChannels << std::endl;
                ReturnCode = S_OK;
            }
            else 
            {
                std::wcerr << L"Failed to get mix format." << std::endl;
                ReturnCode = S_FALSE;
            }
        }
        CoTaskMemFree(FormatDetails);
    }    
    SafeRelease(&AudioClient);
    return ReturnCode;
}
```