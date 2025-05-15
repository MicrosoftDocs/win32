---
description: Used to connect to a network that requires security settings that comply with Federal Information Processing Standards (FIPS) 140-2 standard.
ms.assetid: 169df4a3-e8b9-4f05-874f-a7eef6658d01
title: FIPS profile sample
ms.topic: sample
ms.date: 05/14/2025
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# FIPS profile sample

The FIPS profile sample can be used to connect to a network that requires security settings that comply with Federal Information Processing Standards (FIPS) 140-2 standard. For more information about FIPS, see [**FIPSMode**](wlan-profileschema-authencryption-security-element.md#fipsmode).

```xml
<?xml version="1.0" encoding="US-ASCII"?>
<WLANProfile xmlns="https://www.microsoft.com/networking/WLAN/profile/v1">
    <name>FIPS_TEST</name>
    <SSIDConfig>
        <SSID>
            <hex>464950535F54455354</hex>
            <name>FIPS_TEST</name>
        </SSID>
        <nonBroadcast>false</nonBroadcast>
    </SSIDConfig>
    <connectionType>ESS</connectionType>
    <connectionMode>auto</connectionMode>
    <autoSwitch>false</autoSwitch>
    <MSM>
        <security>
            <authEncryption>
                <authentication>WPA2</authentication>
                <encryption>AES</encryption>
                <useOneX>true</useOneX>
                <FIPSMode xmlns="https://www.microsoft.com/networking/WLAN/profile/v2">true</FIPSMode>
            </authEncryption>
            <OneX xmlns="https://www.microsoft.com/networking/OneX/v1">
                <EAPConfig>
                    <EapHostConfig xmlns="https://www.microsoft.com/provisioning/EapHostConfig">
                    <EapMethod>
                        <Type xmlns="https://www.microsoft.com/provisioning/EapCommon">25</Type>
                        <VendorId xmlns="https://www.microsoft.com/provisioning/EapCommon">0</VendorId>
                        <VendorType xmlns="https://www.microsoft.com/provisioning/EapCommon">0</VendorType>
                        <AuthorId xmlns="https://www.microsoft.com/provisioning/EapCommon">0</AuthorId>
                    </EapMethod>
                    <ConfigBlob></ConfigBlob>
                    </EapHostConfig>
                </EAPConfig>
            </OneX>
        </security>
    </MSM>
</WLANProfile>
```

## Related topics

* [Wireless profile samples](wireless-profile-samples.md)
* [WLAN_profile schema](wlan-profileschema-schema.md)
* [Wireless Access Deployment](/windows-server/networking/core-network-guide/cncg/wireless/e-wireless-access-deployment)
* [Extensible Authentication Protocol (EAP) for network access](/windows-server/networking/technologies/extensible-authentication-protocol/network-access)
* [Configure EAP profiles and settings in Windows](/windows-server/networking/technologies/extensible-authentication-protocol/configure-eap-profiles)
