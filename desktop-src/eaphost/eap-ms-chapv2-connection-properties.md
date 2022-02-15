---
title: EAP MS-CHAPv2 Connection Properties
description: Learn about the EAP MS-CHAPv2 connection properties. See an example that's an instance of the mschapv2connectionpropertiesv1 legacy schema.
ms.assetid: d6a057e0-56f6-4a31-9391-fde631ac2898
ms.topic: article
ms.date: 05/31/2018
---

# EAP MS-CHAPv2 Connection Properties

This sample is an instance of the [mschapv2connectionpropertiesv1](mschapv2connectionpropertiesv1schema-schema.md) legacy schema..

``` syntax
  <?xml version="1.0" ?> 
  <EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig" 
    xmlns:eapCommon="http://www.microsoft.com/provisioning/EapCommon" 
    xmlns:baseEap="http://www.microsoft.com/provisioning/BaseEapMethodConfig">
    <EapMethod>
      <eapCommon:Type>26</eapCommon:Type> 
      <eapCommon:AuthorId>0</eapCommon:AuthorId> 
    </EapMethod>
    <Config xmlns:baseEap="http://www.microsoft.com/provisioning/BaseEapConnectionPropertiesV1" 
      xmlns:msPeap="http://www.microsoft.com/provisioning/MsPeapConnectionPropertiesV1" 
      xmlns:msChapV2="http://www.microsoft.com/provisioning/MsChapV2ConnectionPropertiesV1">
      <baseEap:Eap>
        <baseEap:Type>26</baseEap:Type> 
        <msChapV2:EapType>
        <msChapV2:UseWinLogonCredentials>false</msChapV2:UseWinLogonCredentials> 
        </msChapV2:EapType>
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

 

 




