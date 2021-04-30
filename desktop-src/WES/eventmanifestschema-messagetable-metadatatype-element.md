---
title: messageTable (MetadataType) Element
description: Contains references to strings that are used in the event instrumentation manifest metadata section. The strings are stored in a group of message elements and IDs paired together.
ms.assetid: 868af191-0f9c-435b-878f-ef0584e097d1
keywords:
- messageTable element EventLog
topic_type:
- apiref
api_name:
- messageTable
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# messageTable (MetadataType) Element

Contains references to strings that are used in the event instrumentation manifest metadata section. The strings are stored in a group of [**message**](eventmanifestschema-message-messagetable-element.md) elements and IDs paired together.

``` syntax
<xs:element name="messageTable">
    <xs:complexType>
        <xs:sequence>
            <xs:element name="message"
                minOccurs="0"
                maxOccurs="unbounded"
            >
                <xs:complexType>
                    <xs:attribute name="value"
                        type="string"
                        use="required"
                     />
                    <xs:attribute name="mid"
                        type="string"
                        use="optional"
                     />
                    <xs:attribute name="message"
                        type="string"
                        use="required"
                     />
                    <xs:attribute name="symbol"
                        type="string"
                        use="optional"
                     />
                </xs:complexType>
            </xs:element>
        </xs:sequence>
    </xs:complexType>
</xs:element>
```

The **messageTable** element is defined by the [**MetadataType**](eventmanifestschema-metadatatype-complextype.md) complex type.

## Child elements



| Element                                                             | Type | Description                                                                               |
|---------------------------------------------------------------------|------|-------------------------------------------------------------------------------------------|
| [**message**](eventmanifestschema-message-messagetable-element.md) |      | Specifies a reference to a string in the localization section of the manifest.<br/> |



## Attributes



| Name    | Type   | Description                                                              |
|---------|--------|--------------------------------------------------------------------------|
| message | string | A reference to the localized string in the string table.<br/>      |
| mid     | string | Not used.<br/>                                                     |
| symbol  | string | The symbol used to reference the message.<br/>                     |
| value   | string | The number to use as the message identifier for this message.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

**Definition context of element in schema**
</dt> <dt>

[**MetadataType**](eventmanifestschema-metadatatype-complextype.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**metadata (instrumentationManifest)**](eventmanifestschema-metadata-instrumentationmanifest-element.md)
</dt> </dl>

 

 





