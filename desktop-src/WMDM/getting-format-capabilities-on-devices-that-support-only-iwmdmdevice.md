---
title: Getting format capabilities through IWMDMDevice
description: Getting Format Capabilities on Devices That Support Only IWMDMDevice
ms.assetid: bff079a1-d192-4e53-9b1d-9ad3b5dcca51
keywords:
- Windows Media Device Manager,device capabilities
- Device Manager,device capabilities
- programming guide,device capabilities
- desktop applications,device capabilities
- creating Windows Media Device Manager applications,device capabilities
- writing files to devices,device capabilities
- IWMDMDevice method
- Windows Media Device Manager,IWMDMDevice method
- Device Manager,IWMDMDevice method
- programming guide,IWMDMDevice method
- desktop applications,IWMDMDevice method
- creating Windows Media Device Manager applications,IWMDMDevice method
- writing files to devices,IWMDMDevice method
ms.topic: article
ms.date: 05/31/2018
---

# Getting format capabilities through IWMDMDevice

The recommended method for querying a device for its playback capabilities is [**IWMDMDevice3::GetFormatCapability**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmdevice3-getformatcapability). However, if a device does not support this method, the application instead can call [**IWMDMDevice::GetFormatSupport**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmdevice-getformatsupport) to retrieve an array of supported audio formats as [**\_WAVEFORMATEX**](-waveformatex.md) structures and MIME formats as strings from the device.

The following steps show how an application can use this method to query a device for supported formats:

1.  Call **GetFormatSupport** to retrieve arrays of both audio and mime formats.
2.  Loop through the retrieved audio formats and examine each [**\_WAVEFORMATEX**](-waveformatex.md) structure to try to find an acceptable audio format
3.  Loop through the retrieved MIME format strings (if desired) to find an acceptable file type. The SDK does not define constants for MIME formats; you should use industry standard values (which can be found at the iana.org Web site). A device should list the specific MIME types that it supports.

The following C++ code demonstrates retrieving format capabilities from a device, using **GetFormatSupport**.


```C++
// Function to print out device caps for a device 
// that supports only IWMDMDevice.
void CWMDMController::GetCaps(IWMDMDevice* pDevice)
{
    HRESULT hr = S_OK;

    // Get all capabilities for audio and mime support.
    _WAVEFORMATEX* pAudioFormats;
    LPWSTR* pMimeFormats;
    UINT numAudioFormats = 0;
    UINT numMimeFormats = 0;
    hr = pDevice->GetFormatSupport(
        &pAudioFormats,
        &numAudioFormats,
        &pMimeFormats,
        &numMimeFormats);
    if (FAILED(hr)) return;

    // Print out audio format data.
    if (numAudioFormats > 0)
    {
        // TODO: Display a banner for the supported audio-format listing.
    }
    else
    {
        // TODO: Display a message indicating that no audio formats are supported.
    }
    for (int i = 0; i < numAudioFormats; i++)
    {
       // TODO: For each valid audio format, display the max channel, 
       // max samples/second, avg. bytes/sec, block alignment, and 
       // max bits/sample values.
    }

    // Print out MIME formats.
    if (numMimeFormats > 0)
        // TODO: Display a banner to precede the MIME format listing.
    else
        // TODO: Display a banner indicating that no MIME formats are supported.
    for (i = 0; i < numMimeFormats; i++)
    {
        // TODO: Display the specified MIME format.
    }
    return;
}
```



## Related topics

<dl> <dt>

[**Discovering Device Format Capabilities**](discovering-device-format-capabilities.md)
</dt> <dt>

[**Getting Format Capabilities on Devices That Support IWMDMDevice3**](getting-format-capabilities-on-devices-that-support-iwmdmdevice3.md)
</dt> </dl>

 

 




