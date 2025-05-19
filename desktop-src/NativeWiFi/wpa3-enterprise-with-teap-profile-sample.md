---
description: Uses Tunnel Extensible Authentication Protocol with WPA3-Enterprise.
ms.assetid: 4ee4bf07-e866-4d3a-8131-95f4a6f86153
title: WPA3-Enterprise with TEAP profile sample
ms.topic: sample
ms.date: 05/14/2025
---

# WPA3-Enterprise with TEAP profile sample

This sample profile uses Tunnel Extensible Authentication Protocol (TEAP) with EAP-TLS (certificates) as both inner methods to authenticate to the network.

This sample is configured to use WPA3-Enterprise.

The EAP-TLS credentials are obtained from the certificate store. If authentication based on the credentials in the certificate store fails, the user is prompted to provide valid credentials. No alternate servers, root certificate authorities, or user names are used for authentication if the first attempt fails.

The first method runs as machine and the second method runs as user.

```xml
<?xml version="1.0"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
    <name>Wpa3EnterpriseTeap</name>
    <SSIDConfig>
        <SSID>
            <name>Wpa3EnterpriseTeap</name>
        </SSID>
        <nonBroadcast>false</nonBroadcast>
    </SSIDConfig>
    <connectionType>ESS</connectionType>
    <connectionMode>manual</connectionMode>
    <autoSwitch>false</autoSwitch>
    <MSM>
        <security>
            <authEncryption>
                <authentication>WPA3ENT</authentication>
                <encryption>AES</encryption>
                <useOneX>true</useOneX>
            </authEncryption>
            <PMKCacheMode>enabled</PMKCacheMode>
            <PMKCacheTTL>720</PMKCacheTTL>
            <PMKCacheSize>128</PMKCacheSize>
            <preAuthMode>disabled</preAuthMode>
            <OneX xmlns="http://www.microsoft.com/networking/OneX/v1">
                <cacheUserData>true</cacheUserData>
                <authMode>machineOrUser</authMode>
                <EAPConfig>
                    <EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig">
                        <EapMethod>
                            <Type xmlns="http://www.microsoft.com/provisioning/EapCommon">55</Type>
                            <VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId>
                            <VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType>
                            <AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">311</AuthorId>
                        </EapMethod>
                        <Config xmlns="http://www.microsoft.com/provisioning/EapHostConfig">
                            <EapTeap xmlns="http://www.microsoft.com/provisioning/EapTeapConnectionPropertiesV1">
                                <ServerValidation>
                                    <TrustedRootCAHash>00 11 22 33 44 55 66 77 88 99 aa bb cc dd ee ff 00 11 22 33</TrustedRootCAHash>
                                    <DisablePrompt>true</DisablePrompt>
                                    <DownloadTrustedServerRoot>false</DownloadTrustedServerRoot>
                                </ServerValidation>
                                <Phase2Authentication>
                                    <InnerMethodConfig>
                                        <EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig">
                                            <EapMethod>
                                                <Type xmlns="http://www.microsoft.com/provisioning/EapCommon">13</Type>
                                                <VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId>
                                                <VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType>
                                                <AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId>
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
                                                        </ServerValidation>
                                                        <DifferentUsername>false</DifferentUsername>
                                                        <PerformServerValidation xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">false</PerformServerValidation>
                                                        <AcceptServerName xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">false</AcceptServerName>
                                                        <TLSExtensions xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">
                                                            <FilteringInfo xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV3">
                                                                <CAHashList Enabled="true">
                                                                    <IssuerHash>00 11 22 33 44 55 66 77 88 99 aa bb cc dd ee ff 00 11 22 33</IssuerHash>
                                                                </CAHashList>
                                                            </FilteringInfo>
                                                        </TLSExtensions>
                                                    </EapType>
                                                </Eap>
                                            </Config>
                                        </EapHostConfig>
                                    </InnerMethodConfig>
                                    <InnerMethodConfig>
                                        <EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig">
                                            <EapMethod>
                                                <Type xmlns="http://www.microsoft.com/provisioning/EapCommon">13</Type>
                                                <VendorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorId>
                                                <VendorType xmlns="http://www.microsoft.com/provisioning/EapCommon">0</VendorType>
                                                <AuthorId xmlns="http://www.microsoft.com/provisioning/EapCommon">0</AuthorId>
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
                                                        </ServerValidation>
                                                        <DifferentUsername>false</DifferentUsername>
                                                        <PerformServerValidation xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">false</PerformServerValidation>
                                                        <AcceptServerName xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">false</AcceptServerName>
                                                        <TLSExtensions xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV2">
                                                            <FilteringInfo xmlns="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV3">
                                                                <CAHashList Enabled="true">
                                                                    <IssuerHash>00 11 22 33 44 55 66 77 88 99 aa bb cc dd ee ff 00 11 22 33</IssuerHash>
                                                                </CAHashList>
                                                            </FilteringInfo>
                                                        </TLSExtensions>
                                                    </EapType>
                                                </Eap>
                                            </Config>
                                        </EapHostConfig>
                                    </InnerMethodConfig>
                                </Phase2Authentication>
                                <Phase1Identity>
                                    <IdentityPrivacy>false</IdentityPrivacy>
                                </Phase1Identity>
                            </EapTeap>
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
