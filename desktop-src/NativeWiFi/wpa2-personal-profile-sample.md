---
description: Uses a pre-shared key for network authentication. This sample profile uses Wi-Fi Protected Access 2 security running in Personal mode (WPA2-Personal).
ms.assetid: dbbadac6-1b7e-4161-a775-a934cf201c9d
title: WPA2-Personal profile sample
ms.topic: sample
ms.date: 05/14/2025
---

# WPA2-Personal profile sample

This sample profile uses a pre-shared key for network authentication. The key is shared with the client and the access point. This sample profile is configured to use Wi-Fi Protected Access 2 security running in Personal mode (WPA2-Personal). The Advanced Encryption Standard (AES) cipher type is used for encryption.

```xml
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

```xml
<sharedKey>
    <keyType>passPhrase</keyType>
    <protected>false</protected>
    <keyMaterial> <!-- insert key here --> </keyMaterial>
</sharedKey>
```

## Related topics

* [Wireless profile samples](wireless-profile-samples.md)
* [WLAN_profile schema](wlan-profileschema-schema.md)
