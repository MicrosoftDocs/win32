---
title: SDK Connection Properties
description: Learn about SDK connection properties. See a sample that's an instance of the eaphostconfig native schema.
ms.assetid: 34c9b423-4f4c-484e-86d7-4594566cd396
ms.topic: article
ms.date: 05/31/2018
---

# SDK Connection Properties

This sample is an instance of the [eaphostconfig](eaphostconfigschema-schema.md) native schema.

``` syntax
  <?xml version="1.0" ?> 
  <EapHostConfig xmlns="http://www.microsoft.com/provisioning/EapHostConfig" 
    xmlns:eapCommon="http://www.microsoft.com/provisioning/EapCommon" 
    xmlns:baseEap="http://www.microsoft.com/provisioning/BaseEapMethodConfig">
    <EapMethod>
      <eapCommon:Type>40</eapCommon:Type> 
      <eapCommon:AuthorId>100</eapCommon:AuthorId> 
    </EapMethod>
    <Config>
      <EapType>40</EapType> 
      <ConfigData>seatac.bingo.com</ConfigData> 
    </Config>
  </EapHostConfig>
```

## Related topics

<dl> <dt>

[Connection Properties](connection-profiles.md)
</dt> <dt>

[EAPHost and Legacy Schema](eaphost-schemas.md)
</dt> </dl>

 

 




