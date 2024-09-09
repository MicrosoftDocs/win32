---
description: Uses Extensible Authentication Protocol Transport Level Security (EAP-TLS) with certificates to authenticate to the network (WPA2-Enterprise).
ms.assetid: ded07fda-ea7f-4c5a-9433-60196c3f14af
title: WPA2-Enterprise with TLS profile sample
ms.topic: article
ms.date: 05/31/2018
---

# WPA2-Enterprise with TLS profile sample

This sample profile uses Extensible Authentication Protocol Transport Level Security (EAP-TLS) with certificates to authenticate to the network.

This sample is configured to use Wi-Fi Protected Access 2 security running in Enterprise mode (WPA2-Enterprise). The WPA2-Enterprise security type uses 802.1X for the authentication exchange with the backend. The Advanced Encryption Standard (AES) cipher type is used for encryption.

The EAP-TLS credentials are obtained from the certificate store. If authentication based on the credentials in the certificate store fails, the user is prompted to provide valid credentials. No alternate servers, root certificate authorities, or user names are used for authentication if the first attempt fails.

The EAPHost configuration used in this wireless profile sample was derived from the [EAP-TLS Connection Properties](../eaphost/eap-tls-connection-properties.md) sample.

**Windows 7 and Windows Server 2008 R2 with the Wireless LAN Service installed:** Changes are implemented on Windows 7 and Windows Server 2008 R2 with the Wireless LAN Service installed to optimize wireless networking performance. The default setting for [**autoSwitch**](wlan-profileschema-wlanprofile-element.md#autoswitch) when this element is not set in a wireless LAN profile has changed. The default setting is changed to "false" on Windows 7 and Windows Server 2008 R2 with the Wireless LAN Service installed. The default setting was "true" on Windows Server 2008 and Windows Vista. Please refer to the [**autoSwitch**](wlan-profileschema-wlanprofile-element.md#autoswitch) schema element description for more information.

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** EAP-TLS is not supported.

``` syntax
<?xml version="1.0" encoding="US-ASCII"?>
<WLANProfile xmlns="https://www.microsoft.com/networking/WLAN/profile/v1">
    <name>SampleWPA2EnterpriseTLS</name>
    <SSIDConfig>
        <SSID>
            <name>SampleWPA2EnterpriseTLS</name>
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
                <EAPConfig>
                    <EapHostConfig xmlns="https://www.microsoft.com/provisioning/EapHostConfig" 
                                   xmlns:eapCommon="https://www.microsoft.com/provisioning/EapCommon" 
                                   xmlns:baseEap="https://www.microsoft.com/provisioning/BaseEapMethodConfig">
 
                        <EapMethod>
                            <eapCommon:Type>13</eapCommon:Type> 
                            <eapCommon:AuthorId>0</eapCommon:AuthorId> 
                        </EapMethod>
                        <Config xmlns:baseEap="https://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1" 
                                xmlns:eapTls="https://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV1">

                            <baseEap:Eap>
                                <baseEap:Type>13</baseEap:Type> 
                                <eapTls:EapType>
                                    <eapTls:CredentialsSource>
                                        <eapTls:CertificateStore />
                                    </eapTls:CredentialsSource>
                                    <eapTls:ServerValidation>
                                        <eapTls:DisableUserPromptForServerValidation>false</eapTls:DisableUserPromptForServerValidation> 
                                        <eapTls:ServerNames /> 
                                    </eapTls:ServerValidation> 
                                   <eapTls:DifferentUsername>false</eapTls:DifferentUsername> 
                               </eapTls:EapType>
                           </baseEap:Eap>
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

[Wireless profile samples](wireless-profile-samples.md)
</dt> </dl>

 

 
