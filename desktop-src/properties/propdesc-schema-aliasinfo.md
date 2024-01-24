---
description: Specifies a sort alias or list of sort aliases by specifying an element that contains a sort property or list of sort properties.
ms.assetid: 4c514197-0df0-49c6-b39e-8a2a7cefa93d
title: aliasInfo
ms.topic: article
ms.date: 05/31/2018
---

# aliasInfo

Specifies a sort alias or list of sort aliases by specifying an element that contains a sort property or list of sort properties. There should be only one [aliasInfo]() element for each [propertyDescription](./propdesc-schema-propertydescription.md) element. For properties that set canGroupBy=true, unless a secondary sort property is specified (aliasInfo/@additionalSortByAliases=prop:example), the user may experience unexpected behavior when changing the sort order in a view that is grouped by the property. Specifically, the order of the groups will change, but the order of items within the groups will not.

## Syntax


```
<!-- aliasInfo -->
<xs:element name="aliasInfo">
    <xs:complexType>
        <xs:attribute name="sortByAlias" type="canonical-name"/>
        <xs:attribute name="additionalSortByAliases" type="proplist"/>
    </xs:complexType>
</xs:element>
```



## Element Information



| Parent Element                                                   | Child Elements |
|------------------------------------------------------------------|----------------|
| [propertyDescription](./propdesc-schema-propertydescription.md) | None           |



 

## Attributes



| Attribute               | Description                                                                                                                                                            |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| sortByAlias             | Public. Optional. The canonical name of the property that should be used to sort by. This string is of type canonical-type.                                            |
| additionalSortByAliases | Public. Optional. A semi-colon delimited list of additional properties to be used when sorting. The properties are applied to the sort in the sequence they are given. |



 

 

 
