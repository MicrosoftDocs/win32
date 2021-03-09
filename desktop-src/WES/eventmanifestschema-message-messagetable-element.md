---
title: message (messageTable) Element
description: Contains a reference to a string in the localization section of the manifest. | message (messageTable) Element
ms.assetid: 0988cf99-c7e1-446b-869e-9ac4a0976ac5
keywords:
- message element EventLog
topic_type:
- apiref
api_name:
- message
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# message (messageTable) Element

Contains a reference to a string in the localization section of the manifest.

``` syntax
<xs:element name="message">
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
```

The **message** element is defined by the [**messageTable**](eventmanifestschema-messagetable-instrumentationtype-element.md) element.

## Attributes



| Name    | Type   | Description                                                                                        |
|---------|--------|----------------------------------------------------------------------------------------------------|
| message | string | A reference to the localized string in the string table.<br/>                                |
| mid     | string | Not used.<br/>                                                                               |
| symbol  | string | The symbolic name that you want the message compiler to create for this message string.<br/> |
| value   | string | The number to use as the message identifier for this message.<br/>                           |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

**Parent elements**
</dt> <dt>

[**messageTable (EventsType)**](eventmanifestschema-messagetable-instrumentationtype-element.md)
</dt> <dt>

[**messageTable (MetadataType)**](eventmanifestschema-messagetable-metadatatype-element.md)
</dt> </dl>

 

 





