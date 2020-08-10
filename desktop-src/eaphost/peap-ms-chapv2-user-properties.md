---
title: PEAP MS-CHAPv2 User Properties
description: Learn about the PEAP MS-CHAPv2 user properties. See a sample that's an instance of the mschapv2userpropertiesv1 legacy schema.
ms.assetid: af1ed6b1-712e-4b55-9ab4-b6b38f486fb1
ms.topic: article
ms.date: 05/31/2018
---

# PEAP MS-CHAPv2 User Properties

This sample is an instance of the [mschapv2userpropertiesv1](mschapv2userpropertiesv1schema-schema.md) legacy schema.

``` syntax
  <?xml version="1.0" ?> 
  <EapHostUserCredentials xmlns="http://www.microsoft.com/provisioning/EapHostUserCredentials"
    xmlns:eapCommon="http://www.microsoft.com/provisioning/EapCommon" 
    xmlns:baseEap="http://www.microsoft.com/provisioning/BaseEapMethodUserCredentials">
    <EapMethod>
      <eapCommon:Type>25</eapCommon:Type> 
      <eapCommon:AuthorId>0</eapCommon:AuthorId> 
    </EapMethod>
    <Credentials xmlns:eapUser="http://www.microsoft.com/provisioning/EapUserPropertiesV1"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xmlns:baseEap="http://www.microsoft.com/provisioning/BaseEapUserPropertiesV1"
      xmlns:MsPeap="http://www.microsoft.com/provisioning/MsPeapUserPropertiesV1"
      xmlns:MsChapV2="http://www.microsoft.com/provisioning/MsChapV2UserPropertiesV1">
      <baseEap:Eap>
        <baseEap:Type>25</baseEap:Type> 
        <MsPeap:EapType>
          <MsPeap:RoutingIdentity>test</MsPeap:RoutingIdentity> 
          <baseEap:Eap>
            <baseEap:Type>26</baseEap:Type> 
            <MsChapV2:EapType>
              <MsChapV2:Username>test</MsChapV2:Username> 
              <MsChapV2:Password>test</MsChapV2:Password> 
              <MsChapV2:LogonDomain>ias-domain</MsChapV2:LogonDomain> 
            </MsChapV2:EapType>
          </baseEap:Eap>
        </MsPeap:EapType>
      </baseEap:Eap>
    </Credentials>
  </EapHostUserCredentials>
```

## Related topics

<dl> <dt>

[User Properties](user-profiles.md)
</dt> <dt>

[EAPHost and Legacy Schema](eaphost-schemas.md)
</dt> </dl>

 

 




