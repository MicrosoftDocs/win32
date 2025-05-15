---
description: Used to authenticate to a wireless network for the first time before the computer has joined a domain.
ms.assetid: e1a5ce76-9761-4c65-8b26-a44bf2eb1835
title: Bootstrap profile sample
ms.topic: sample
ms.date: 05/14/2025
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Bootstrap profile sample

The Bootstrap profile sample can be used to authenticate to a wireless network for the first time before the computer has joined a domain.

This profile does not validate the certificates presented by the Remote Authentication Dial-In User Service (RADIUS) server, and should not be used after the machine is joined to a domain.

This sample is configured to use Wi-Fi Protected Access 2 security running in Enterprise mode (WPA2-Enterprise), authenticating with username/password (via PEAP-MSCHAPv2)

```xml
<?xml version="1.0" encoding="US-ASCII"?>
<WLANProfile xmlns="https://www.microsoft.com/networking/WLAN/profile/v1">
    <name>SampleBootstrap</name>
    <SSIDConfig>
        <SSID>
            <name>SampleBootstrap</name>
        </SSID>
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
            </authEncryption>
            <OneX xmlns="https://www.microsoft.com/networking/OneX/v1">
                <cacheUserData>true</cacheUserData>
                <authMode>machineOrUser</authMode>
               <EAPConfig>
                    <EapHostConfig xmlns="https://www.microsoft.com/provisioning/EapHostConfig" 
                                   xmlns:eapCommon="https://www.microsoft.com/provisioning/EapCommon" 
                                   xmlns:baseEap="https://www.microsoft.com/provisioning/BaseEapMethodConfig">
                        <EapMethod>
                            <eapCommon:Type>25</eapCommon:Type> 
                            <eapCommon:AuthorId>0</eapCommon:AuthorId> 
                       </EapMethod>
                       <Config xmlns:baseEap="https://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1" 
                               xmlns:msPeap="https://www.microsoft.com/provisioning/MsPeapConnectionPropertiesV1" 
                               xmlns:msChapV2="https://www.microsoft.com/provisioning/MsChapV2ConnectionPropertiesV1">
                           <baseEap:Eap>
                               <baseEap:Type>25</baseEap:Type> 
                               <msPeap:EapType>
                                   <msPeap:ServerValidation>
                                       <msPeap:DisableUserPromptForServerValidation>false</msPeap:DisableUserPromptForServerValidation> 
                                       <msPeap:TrustedRootCA /> 
                                   </msPeap:ServerValidation>
                                   <msPeap:FastReconnect>true</msPeap:FastReconnect> 
                                   <msPeap:InnerEapOptional>0</msPeap:InnerEapOptional> 
                                   <baseEap:Eap>
                                       <baseEap:Type>26</baseEap:Type> 
                                       <msChapV2:EapType>
                                           <msChapV2:UseWinLogonCredentials>true</msChapV2:UseWinLogonCredentials> 
                                       </msChapV2:EapType>
                                   </baseEap:Eap>
                                   <msPeap:EnableQuarantineChecks>false</msPeap:EnableQuarantineChecks> 
                                   <msPeap:RequireCryptoBinding>false</msPeap:RequireCryptoBinding> 
                                   <msPeap:PeapExtensions /> 
                               </msPeap:EapType>
                           </baseEap:Eap>
                       </Config>
                   </EapHostConfig>
                </EAPConfig>
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
