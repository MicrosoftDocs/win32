---
title: ComplexDataType Complex Type
description: Defines a structure that contains one or more data items.
ms.assetid: 1495daef-1dfd-4f62-9543-569cc74102f4
keywords:
- ComplexDataType complex type EventLog
topic_type:
- apiref
api_name:
- ComplexDataType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# ComplexDataType Complex Type

Defines a structure that contains one or more data items.

``` syntax
<xs:complexType name="ComplexDataType">
    <xs:sequence>
        <xs:element name="Data"
            type="DataType"
            minOccurs="0"
            maxOccurs="unbounded"
         />
    </xs:sequence>
    <xs:attribute name="Name"
        type="string"
        use="optional"
     />
</xs:complexType>
```

## Child elements



| Element                                                  | Type                                                      | Description                                                                                                             |
|----------------------------------------------------------|-----------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| [**Data**](eventschema-data-complexdatatype-element.md) | [**DataType**](eventschema-datafieldtype-complextype.md) | The list of data items in the structure. The list of items are in the same order as defined in the template.<br/> |



## Attributes



| Name | Type   | Description                                                                                                                                                                                                                  |
|------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Name | string | The name of the structure. This is the name that is specified when you defined the structure in the template (see the [**TemplateItemType**](eventmanifestschema-templateitemtype-complextype.md) complex type).<br/> |



## Remarks

The [**EvtRender**](/windows/desktop/api/WinEvt/nf-winevt-evtrender) function renders the contents of a structure as a binary blob; the function does not render the individual data items of the structure.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





