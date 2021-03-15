---
title: BaseEapParameters Complex Type
description: Defines the placeholder element for method type and method-specific configuration.
ms.assetid: 510debce-545c-4ce1-965b-e4b2185b7983
keywords:
- BaseEapParameters complex type EAPHost
topic_type:
- apiref
api_name:
- BaseEapParameters
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
ROBOTS: INDEX,FOLLOW
---


# BaseEapParameters Complex Type

The **BaseEapParameters** complex type defines the placeholder element for method type and method-specific configuration.

``` syntax
<xs:complexType name="BaseEapParameters">
    <xs:sequence>
        <xs:element name="Type"
            type="integer"
         />
        <xs:any
            processContents="lax"
            minOccurs="0"
            maxOccurs="unbounded"
            namespace="##any"
         />
    </xs:sequence>
</xs:complexType>
```

## Child elements



| Element                                                                            | Type    | Description                                     |
|------------------------------------------------------------------------------------|---------|-------------------------------------------------|
| [**Type**](baseeapconnectionpropertiesv1schema-type-baseeapparameters-element.md) | integer | Any schema instance is allowed here.<br/> |



## Remarks

In **BaseEapParameters** the method can define the constituent elements. The method also performs schema validation on the elements in **BaseEapParameters**.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[EAPHost and Legacy Schema](eaphost-schemas.md)
</dt> <dt>

[baseeapconnectionpropertiesv1 Schema](baseeapconnectionpropertiesv1schema-schema.md)
</dt> </dl>

 

 





