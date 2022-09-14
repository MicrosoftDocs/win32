---
description: Specifies information about a cellular network.
ms.assetid: 52d07b64-7939-4f1c-9793-be07af098053
title: providerType Complex Type (Mobile Broadband)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- providerType
api_type: 
- Schema
---

# providerType Complex Type

The **providerType** complex type specifies information about a cellular network.

``` syntax
<xs:complexType name="providerType">
    <xs:sequence>
        <xs:element name="ProviderID"
            type="providerIdType"
         />
        <xs:element name="ProviderName"
            type="providerNameType"
         />
    </xs:sequence>
</xs:complexType>
```

## Child elements



| Element                                                          | Type                                                           | Description               |
|------------------------------------------------------------------|----------------------------------------------------------------|---------------------------|
| [**ProviderID**](schema-providerid-providertype-element.md)     | [**providerIdType**](schema-provideridtype-simpletype.md)     | Provider ID.<br/>   |
| [**ProviderName**](schema-providername-providertype-element.md) | [**providerNameType**](schema-providernametype-simpletype.md) | Provider name.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps \| UWP apps\]<br/> |
| Minimum supported server<br/> | None supported<br/>                         |



 

 




