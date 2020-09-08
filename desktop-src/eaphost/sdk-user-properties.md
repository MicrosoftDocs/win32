---
title: SDK User Properties
description: Learn about the SDK user properties. See a sample that's an instance of the eaphostusercredentials native schema.
ms.assetid: e8a9656d-48e7-4580-a84d-2b829e7a692f
ms.topic: article
ms.date: 05/31/2018
---

# SDK User Properties

This sample is an instance of the [eaphostusercredentials](eaphostusercredentialsschema-schema.md) native schema.

``` syntax
  <?xml version="1.0" ?>  
  <EapHostUserCredentials xmlns="https://www.microsoft.com/provisioning/EapHostUserCredentials" 
    xmlns:eapCommon="https://www.microsoft.com/provisioning/EapCommon" 
    xmlns:baseEap="https://www.microsoft.com/provisioning/BaseEapMethodUserCredentials">
    <EapMethod>
      <eapCommon:Type>40</eapCommon:Type> 
      <eapCommon:AuthorId>100</eapCommon:AuthorId> 
    </EapMethod> 
    <Credentials>
      <EapType>40</EapType> 
      <Identity>test</Identity> 
      <Password>test</Password> 
    </Credentials>
  </EapHostUserCredentials>
```

## Related topics

<dl> <dt>

[User Properties](user-profiles.md)
</dt> <dt>

[EAPHost and Legacy Schema](eaphost-schemas.md)
</dt> </dl>

 

 




