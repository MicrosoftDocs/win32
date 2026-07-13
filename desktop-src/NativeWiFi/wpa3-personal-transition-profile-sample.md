---
description: Uses a pre-shared key for network authentication. This sample profile uses WPA3-Personal, but includes transition mode to connect to WPA2-Personal networks as well.
ms.assetid: 3f46c2bb-38cf-456a-a02f-2a2570613209
title: WPA3-Personal with transition mode profile sample
ms.topic: sample
ms.date: 05/14/2025
---

# WPA3-Personal with transition mode profile sample

This sample profile uses a password-based secure key exchange protocol (SAE) for network authentication. This sample profile is configured to use WPA3-Personal. It also includes transition mode, allowing clients that only support WPA2-PSK to connect to the network with the same profile (assuming the network is configured to also support WPA3 transition mode).

The shared key (`TestPassword1!`) is included in this sample profile in cleartext, so clients would not be prompted to enter the key on first connection. You can instead require the prompt by omitting the [**sharedKey**](wlan-profileschema-sharedkey-security-element.md) child element of the [**security**](wlan-profileschema-security-msm-element.md) element.

```xml
<?xml version="1.0"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
    <name>SampleWpa3TransitionProfile</name>
    <SSIDConfig>
        <SSID>
            <name>SampleWpa3TransitionProfile</name>
        </SSID>
    </SSIDConfig>
    <connectionType>ESS</connectionType>
    <connectionMode>auto</connectionMode>
    <MSM>
        <security>
            <authEncryption>
                <authentication>WPA3SAE</authentication>
                <encryption>AES</encryption>
                <useOneX>false</useOneX>
                <transitionMode xmlns="http://www.microsoft.com/networking/WLAN/profile/v4">true</transitionMode>
            </authEncryption>
            <sharedKey>
                <keyType>passPhrase</keyType>
                <protected>false</protected>
                <keyMaterial>TestPassword1!</keyMaterial>
            </sharedKey>
        </security>
    </MSM>
</WLANProfile>
```

## Related topics

* [Wireless profile samples](wireless-profile-samples.md)
* [WLAN_profile schema](wlan-profileschema-schema.md)
