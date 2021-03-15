---
title: messageTable (EventsType) Element
description: Contains a reference to a string in the localization section of the manifest. | messageTable (EventsType) Element
ms.assetid: 4dcc1afe-8f2b-4baf-b40b-406f60368575
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

# messageTable (EventsType) Element

Contains a reference to a string in the localization section of the manifest.

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

The **messageTable** element is defined by the [**EventsType**](eventmanifestschema-eventstype-complextype.md) complex type.

## Child elements



| Element                                                             | Type | Description                                                                               |
|---------------------------------------------------------------------|------|-------------------------------------------------------------------------------------------|
| [**message**](eventmanifestschema-message-messagetable-element.md) |      | Specifies a reference to a string in the localization section of the manifest.<br/> |



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

[**events (InstrumentationType) Element**](eventmanifestschema-events-instrumentationtype-element.md)
</dt> </dl>

 

 





