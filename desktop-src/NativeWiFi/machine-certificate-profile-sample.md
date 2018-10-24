---
Description: Used to connect to a network that uses Extensible Authentication Protocol Transport Level Security (EAP-TLS) certificates stored on the local machine for 802.1X authentication.
ms.assetid: 4cc4cbb7-963f-4771-8a3d-2a37058c9011
title: Machine Certificate Profile Sample
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Machine Certificate Profile Sample

This profile sample shows a wired network profile used to connect to a network that uses Extensible Authentication Protocol Transport Level Security (EAP-TLS) certificates stored on the local machine for 802.1X authentication. To see a profile that uses EAP-TLS certificates stored on a smart card, see [Smart Card Certificate Sample Profile](smart-card-certificate-profile-sample.md).

The EAPHost configuration used in this wireless profile sample was derived from the [EAP-TLS Connection Properties](https://msdn.microsoft.com/en-us/library/Bb204661(v=VS.85).aspx) sample.

``` syntax
<?xml version="1.0" encoding="US-ASCII"?>
<LANProfile xmlns="http://www.microsoft.com/networking/LAN/profile/v1">
    <MSM>
        <security>
            <OneXEnforced>false</OneXEnforced>
            <OneXEnabled>true</OneXEnabled>
            <OneX xmlns="http://www.microsoft.com/networking/OneX/v1">
                <EAPConfig>
                    <EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig" 
                                   xmlns:eapCommon="http://www.microsoft.com/provisioning/EapCommon" 
                                   xmlns:baseEap="http://www.microsoft.com/provisioning/BaseEapMethodConfig">
 
                        <EapMethod>
                            <eapCommon:Type>13</eapCommon:Type> 
                            <eapCommon:AuthorId>0</eapCommon:AuthorId> 
                        </EapMethod>
                        <Config xmlns:baseEap="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1" 
                                xmlns:eapTls="http://www.microsoft.com/provisioning/EapTlsConnectionPropertiesV1">

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
</LANProfile>
```

## Related topics

<dl> <dt>

[Wired Profile Samples](wired-profile-samples.md)
</dt> </dl>

 

 



