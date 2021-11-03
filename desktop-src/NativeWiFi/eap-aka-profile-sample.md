---
description: Uses Extensible Authentication Protocol Authentication and Key Agreement (EAP-AKA).
ms.assetid: f6de4748-4a97-4b9b-9f77-fe0963f87874
title: EAP-AKA Profile Sample
ms.topic: article
ms.date: 11/02/2021
---

# EAP-AKA Profile Sample

This sample profile uses EAP-AKA, which will rely on a SIM card to authenticate to the network.

The EAP host configuration used in this wireless profile sample was derived from the [EapAkaConnectionPropertiesV1 Schema](/openspecs/windows_protocols/ms-gpwl/6ce02b66-0cbd-47cf-bc34-0903b163aab0).

``` syntax
<?xml version="1.0"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
  <name>SampleEapAka</name>
  <SSIDConfig>
    <SSID>
      <name>SampleEapAka</name>
    </SSID>
    <nonBroadcast>false</nonBroadcast>
  </SSIDConfig>
  <connectionType>ESS</connectionType>
  <connectionMode>manual</connectionMode>
  <MSM>
    <security>
      <authEncryption>
        <authentication>WPA2</authentication>
        <encryption>AES</encryption>
        <useOneX>true</useOneX>
      </authEncryption>
      <OneX xmlns="http://www.microsoft.com/networking/OneX/v1">
        <authMode>user</authMode>
        <EAPConfig>
          <EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig">
            <EapMethod>
              <Type xmlns="http://www.microsoft.com/provisioning/EapCommon">23</Type>
              <VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId>
              <VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType>
              <AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId>
            </EapMethod>
            <Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig">
              <EapAka xmlns="http://www.microsoft.com/provisioning/EapAkaConnectionPropertiesV1">
                <DontRevealPermanentID>true</DontRevealPermanentID>
                <ProviderName></ProviderName>
                <Realm Enabled="true"></Realm>
              </EapAka>
            </Config>
          </EapHostConfig>
        </EAPConfig>
      </OneX>
    </security>
  </MSM>
</WLANProfile>
```

## Related topics

<dl> <dt>

[Wireless Profile Samples](wireless-profile-samples.md)
</dt> <dt>

[EAP-SIM configuration settings](/windows-server/networking/technologies/extensible-authentication-protocol/network-access#eap-sim-configuration-settings)
</dt> <dt>
  
[EAP-SIM](/openspecs/windows_protocols/ms-gpwl/73eddc23-79a2-4b02-966a-a8a909cd76e9)
</dt> <dt>
  
[EAP-AKA](/openspecs/windows_protocols/ms-gpwl/6ce02b66-0cbd-47cf-bc34-0903b163aab0)
</dt> <dt>
  
[EAP-AKA'](/openspecs/windows_protocols/ms-gpwl/cb085b34-e160-4eba-b292-bc748ae461b6)
</dt> </dl>
