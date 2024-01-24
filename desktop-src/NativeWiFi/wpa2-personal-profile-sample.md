---
description: Uses a pre-shared key for network authentication. This sample profile uses Wi-Fi Protected Access 2 security running in Personal mode (WPA2-Personal).
ms.assetid: dbbadac6-1b7e-4161-a775-a934cf201c9d
title: WPA2-Personal profile sample
ms.topic: article
ms.date: 05/31/2018
---

# WPA2-Personal profile sample

This sample profile uses a pre-shared key for network authentication. The key is shared with the client and the access point. This sample profile is configured to use Wi-Fi Protected Access 2 security running in Personal mode (WPA2-Personal). The Advanced Encryption Standard (AES) cipher type is used for encryption.

**Windows 7 and Windows Server 2008 R2 with the Wireless LAN Service installed:** Changes are implemented on Windows 7 and Windows Server 2008 R2 with the Wireless LAN Service installed to optimize wireless networking performance. The default setting for [**autoSwitch**](wlan-profileschema-wlanprofile-element.md#autoswitch) when this element is not set in a wireless LAN profile has changed. The default setting is changed to "false" on Windows 7 and Windows Server 2008 R2 with the Wireless LAN Service installed. The default setting was "true" on Windows Server 2008 and Windows Vista. Please refer to the [**autoSwitch**](wlan-profileschema-wlanprofile-element.md#autoswitch) schema element description for more information.

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** The [**name**](wlan-profileschema-wlanprofile-element.md#name) child of the [**WLANProfile**](wlan-profileschema-wlanprofile-element.md) element is ignored. The name of the profile, as stored in the profile store, is derived from the [**name**](wlan-profileschema-ssid-ssidconfig-element.md#name) child of the [**SSID**](wlan-profileschema-ssid-ssidconfig-element.md) element.

``` syntax
<?xml version="1.0" encoding="US-ASCII"?>
<WLANProfile xmlns="https://www.microsoft.com/networking/WLAN/profile/v1">
    <name>SampleWPA2PSK</name>
    <SSIDConfig>
        <SSID>
            <name>SampleWPA2PSK</name>
        </SSID>
    </SSIDConfig>
    <connectionType>ESS</connectionType>
    <connectionMode>auto</connectionMode>
    <autoSwitch>false</autoSwitch>
    <MSM>
        <security>
            <authEncryption>
                <authentication>WPA2PSK</authentication>
                <encryption>AES</encryption>
                <useOneX>false</useOneX>
            </authEncryption>
        </security>
    </MSM>
</WLANProfile>
```

The shared key has been omitted from this sample profile. If you try to use this sample profile to connect to a network, you will be prompted to enter a shared key. You can avoid this prompt by adding a [**sharedKey**](wlan-profileschema-sharedkey-security-element.md) child element to the [**security**](wlan-profileschema-security-msm-element.md) element immediately following the [**authEncryption**](wlan-profileschema-authencryption-security-element.md) element.

The following snippet shows a [**sharedKey**](wlan-profileschema-sharedkey-security-element.md) element that contains an unencrypted key. You must replace the comment `<!-- insert key here -->` with the actual unencrypted key before using this snippet in a profile.

``` syntax
<sharedKey>
    <keyType>passPhrase</keyType>
    <protected>false</protected>
    <keyMaterial> <!-- insert key here --> </keyMaterial>
</sharedKey>
```

## Related topics

<dl> <dt>

[Wireless profile samples](wireless-profile-samples.md)
</dt> </dl>

 

 



