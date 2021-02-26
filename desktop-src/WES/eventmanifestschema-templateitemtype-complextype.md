---
title: TemplateItemType Complex Type
description: A template that defines the data to include with an event. | TemplateItemType Complex Type
ms.assetid: 1681af7d-03ef-47bc-bc02-ce1a9903fb44
keywords:
- TemplateItemType complex type EventLog
topic_type:
- apiref
api_name:
- TemplateItemType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# TemplateItemType Complex Type

A template that defines the data to include with an event.

``` syntax
<xs:complexType name="TemplateItemType">
    <xs:sequence
        maxOccurs="unbounded"
    >
        <xs:choice
            maxOccurs="unbounded"
            minOccurs="0"
        >
            <xs:element name="data"
                type="DataDefinitionType"
             />
            <xs:element name="struct"
                type="StructDefinitionType"
             />
        </xs:choice>
        <xs:element name="binary"
            minOccurs="0"
        >
            <xs:complexType>
                <xs:attribute name="name"
                    type="string"
                    use="optional"
                 />
            </xs:complexType>
        </xs:element>
        <xs:element name="UserData"
            type="XmlType"
            minOccurs="0"
         />
    </xs:sequence>
    <xs:attribute name="tid"
        type="token"
        use="required"
     />
    <xs:attribute name="name"
        type="string"
        use="optional"
     />
</xs:complexType>
```

## Child elements



| Element                                                                   | Type                                                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|---------------------------------------------------------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**binary**](eventmanifestschema-binary-templateitemtype-element.md)     |                                                                                      | Reserved for internal use only.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [**data**](eventmanifestschema-data-templateitemtype-element.md)         | [**DataDefinitionType**](eventmanifestschema-datadefinitiontype-complextype.md)     | Defines a data item that you want to include with the event.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [**struct**](eventmanifestschema-struct-templateitemtype-element.md)     | [**StructDefinitionType**](eventmanifestschema-structdefinitiontype-complextype.md) | Defines a structure that includes one or more data items that you want to include with the event. Providers write the structure as a blob and not as individual members of the structure.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [**UserData**](eventmanifestschema-userdata-templateitemtype-element.md) | [**XmlType**](eventmanifestschema-xmltype-complextype.md)                           | An XML fragment that is used to render the event data. If you do not include the fragment, the event data is rendered in the order that the data items are defined in the template. The contents of this element is any valid XML fragment. The fragment must contain only one top-level node and the top-level node must specify its own namespace. <br/> To reference a data item in the fragment, set the text body for a node in the fragment to %*n*, where *n* is the one-based index of the top-level data items in the list of data items (you cannot reference members of a structure). The index value that you specify must not be greater than the number of top-level data items in the template.<br/> This element follows all **data** and **struct** elements. <br/> |



## Attributes



| Name | Type   | Description                                                                                                                                                                                           |
|------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| name | string | Reserved for internal use only.<br/>                                                                                                                                                            |
| name | string | The name of the template.<br/>                                                                                                                                                                  |
| tid  | token  | An identifier that uniquely identifies the template within the list of templates that the provider defines. Use this name to reference the template when you define your event definition.<br/> |



## Remarks

The template definition must have at least one data or struct child element. The provider must write the event data in the order of the data items defined in the template.

The size of all the data items in the template must be less than 64 KB.

## Examples

The following example shows how to create a template definition.


```XML
<templates>
   <template tid="T1">
       <data name="PrinterName" intype="win:UnicodeString" />
       <UserData>
          <PrinterConnectionFailure 
              xmlns="schemas.microsoft.com/schemas/event/Microsoft.Windows.PrintSpooler/1.0.1.0/6382e26fc390d748">
              <PrinterName>%1</PrinterName>
          </PrinterConnectionFailure>
       </xml>
   </template>
</templates>
```



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





