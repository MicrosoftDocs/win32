---
description: Uses Extensible Authentication Protocol Transport Level Security (EAP-TLS) with certificates to authenticate to the network (WPA3-Enterprise 192-bit mode).
ms.assetid: 00493fc8-2b52-4417-a507-a2817d5866ed
title: WPA3-Enterprise 192-bit mode with EAP-TLS profile sample
ms.topic: sample
ms.date: 05/14/2025
---

# WPA3-Enterprise 192-bit mode with EAP-TLS profile sample

This sample profile uses Extensible Authentication Protocol Transport Level Security (EAP-TLS) with certificates to authenticate to the network.

This sample is configured to use WPA3-Enterprise 192-bit mode.

> [!NOTE]
> WPA3-Enterprise 192-bit mode imposes very strict certificate requirements on every certificate involved, including signing and leaf certificates. For more information, see [WPA3-Enterprise 192-bit mode
](/windows-server/networking/technologies/extensible-authentication-protocol/network-access#wpa3-enterprise-192-bit-mode).

The EAP-TLS credentials are obtained from the certificate store. If authentication based on the credentials in the certificate store fails, the user is prompted to provide valid credentials. No alternate servers, root certificate authorities, or user names are used for authentication if the first attempt fails.

```xml
<?xml version="1.0"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
    <name>WPA3Enterprise192BitMode</name>
    <SSIDConfig>
        <SSID>
            <name>WPA3Enterprise192BitMode</name>
        </SSID>
        <nonBroadcast>false</nonBroadcast>
    </SSIDConfig>
    <connectionType>ESS</connectionType>
    <connectionMode>manual</connectionMode>
    <autoSwitch>false</autoSwitch>
    <MSM>
        <security>
            <authEncryption>
                <authentication>WPA3ENT192</authentication>
                <encryption>GCMP256</encryption>
                <useOneX>true</useOneX>
            </authEncryption>
            <OneX xmlns="http://www.microsoft.com/networking/OneX/v1">
                <authMode>user</authMode>
                <EAPConfig>
                    <EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig">
                        <EapMethod>
                            <Type xmlns="http://www.microsoft.com/provisioning/EapCommon">13
                            </Type>
                            <VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0
                            </VendorId>
                            <VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0
                            </VendorType>
                            <AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0
                            </AuthorId>
                        </EapMethod>
                        <Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig">
                            <Eap xmlns="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1">
                                <Type>13</Type>
                                <EapType xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV1">
                                    <CredentialsSource>
                                        <CertificateStore>
                                            <SimpleCertSelection>true</SimpleCertSelection>
                                        </CertificateStore>
                                    </CredentialsSource>
                                    <ServerValidation>
                                        <DisableUserPromptForServerValidation>false</DisableUserPromptForServerValidation>
                                        <ServerNames></ServerNames>
                                        <TrustedRootCA>00 11 22 33 44 55 66 77 88 99 aa bb cc dd ee ff 00 11 22 33 </TrustedRootCA>
                                    </ServerValidation>
                                    <DifferentUsername>false</DifferentUsername>
                                    <PerformServerValidation xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">true
                                    </PerformServerValidation>
                                    <AcceptServerName xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">true
                                    </AcceptServerName>
                                </EapType>
                            </Eap>
                        </Config>
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
