---
title: PEAP MS-CHAPv2 Connection Properties
description: Learn about PEAP MS-CHAPv2 connection properties. See a sample that's an instance of the mschapv2connectionpropertiesv1 legacy schema.
ms.assetid: a289343a-b702-4be2-baf5-2d004a8a8fea
ms.topic: article
ms.date: 05/31/2018
---

# PEAP MS-CHAPv2 Connection Properties

This sample is an instance of the [mschapv2connectionpropertiesv1](mschapv2connectionpropertiesv1schema-schema.md) legacy schema..

``` syntax
  <?xml version="1.0" ?> 
  <EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig" 
    xmlns:eapCommon="http://www.microsoft.com/provisioning/EapCommon" 
    xmlns:baseEap="http://www.microsoft.com/provisioning/BaseEapMethodConfig">
    <EapMethod>
      <eapCommon:Type>25</eapCommon:Type> 
      <eapCommon:AuthorId>0</eapCommon:AuthorId> 
    </EapMethod>
    <Config xmlns:baseEap="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1"
      xmlns:msPeap="http://www.microsoft.com/provisioning/MsPeapConnectionPropertiesV1" 
      xmlns:msChapV2="http://www.microsoft.com/provisioning/MsChapV2ConnectionPropertiesV1">
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
              <msChapV2:UseWinLogonCredentials>false</msChapV2:UseWinLogonCredentials> 
            </msChapV2:EapType>
          </baseEap:Eap>
          <msPeap:EnableQuarantineChecks>false</msPeap:EnableQuarantineChecks> 
          <msPeap:RequireCryptoBinding>false</msPeap:RequireCryptoBinding> 
          <msPeap:PeapExtensions /> 
        </msPeap:EapType>
      </baseEap:Eap>
    </Config>
  </EapHostConfig>
```

## Related topics

<dl> <dt>

[Connection Properties](connection-profiles.md)
</dt> <dt>

[EAPHost and Legacy Schema](eaphost-schemas.md)
</dt> </dl>

 

 




