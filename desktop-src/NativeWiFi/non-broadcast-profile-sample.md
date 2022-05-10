---
description: Used to connect to networks which do not broadcast their network name or SSID.
ms.assetid: 564324ad-6723-4676-ab5c-0b5d2957d201
title: Non-Broadcast profile sample
ms.topic: article
ms.date: 05/31/2018
---

# Non-Broadcast profile sample

The non-broadcast profile sample can be used to connect to networks which do not broadcast their network name or SSID.

This sample profile is configured to use Wi-Fi Protected Access security running in Personal mode (WPA-Personal). Temporal Key Integrity Protocol (TKIP) is used for encryption. Profiles that use other security and cipher types can also be configured as non-broadcast profiles.

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** The [**name**](wlan-profileschema-name-wlanprofile-element.md) child of the [**WLANProfile**](wlan-profileschema-wlanprofile-element.md) element is ignored. The name of the profile, as stored in the profile store, is derived from the [**name**](wlan-profileschema-name-ssid-element.md) child of the [**SSID**](wlan-profileschema-ssid-ssidconfig-element.md) element.

``` syntax
<?xml version="1.0" encoding="US-ASCII"?>
<WLANProfile xmlns="https://www.microsoft.com/networking/WLAN/profile/v1">
    <name>SampleNonBroadcast</name>
    <SSIDConfig>
        <SSID>
            <name>SampleNonBroadcast</name>
        </SSID>
        <nonBroadcast>true</nonBroadcast>
    </SSIDConfig>
    <connectionType>ESS</connectionType>
    <connectionMode>auto</connectionMode>
    <MSM>
        <security>
            <authEncryption>
                <authentication>WPAPSK</authentication>
                <encryption>TKIP</encryption>
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

[Wireless Profile Samples](wireless-profile-samples.md)
</dt> </dl>

 

 



