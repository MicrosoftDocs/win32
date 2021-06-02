---
title: DebugDataType Complex Type
description: Defines the data that can be logged for Windows software trace preprocessor (WPP) events.
ms.assetid: 75638e0f-7a26-473e-a0c4-bd8972ac171f
keywords:
- DebugDataType complex type EventLog
topic_type:
- apiref
api_name:
- DebugDataType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# DebugDataType Complex Type

Defines the data that can be logged for Windows software trace preprocessor (WPP) events.

``` syntax
<xs:complexType name="DebugDataType">
    <xs:sequence>
        <xs:element name="SequenceNumber"
            type="unsignedInt"
            minOccurs="0"
         />
        <xs:element name="FlagsName"
            type="string"
            minOccurs="0"
         />
        <xs:element name="LevelName"
            type="string"
            minOccurs="0"
         />
        <xs:element name="Component"
            type="string"
         />
        <xs:element name="SubComponent"
            type="string"
            minOccurs="0"
         />
        <xs:element name="FileLine"
            type="string"
            minOccurs="0"
         />
        <xs:element name="Function"
            type="unsignedInt"
            minOccurs="0"
         />
        <xs:element name="Message"
            type="string"
         />
        <xs:any
            minOccurs="0"
            maxOccurs="unbounded"
            processContents="lax"
            namespace="##other"
         />
    </xs:sequence>
    <xs:anyAttribute
        processContents="lax"
        namespace="##other"
     />
</xs:complexType>
```

## Child elements



| Element                                                                    | Type        | Description                                                                                                        |
|----------------------------------------------------------------------------|-------------|--------------------------------------------------------------------------------------------------------------------|
| [**Component**](eventschema-component-debugdatatype-element.md)           | string      | The name of the component that logged the trace message.<br/>                                                |
| [**FileLine**](eventschema-fileline-debugdatatype-element.md)             | string      | The name of the source file and the line within the source file that logged the trace message.<br/>          |
| [**FlagsName**](eventschema-flagname-debugdatatype-element.md)            | string      | The flag value passed to the provider when it was enabled.<br/>                                              |
| [**Function**](eventschema-function-debugdatatype-element.md)             | unsignedInt | The name of the function that logged the trace message.<br/>                                                 |
| [**LevelName**](eventschema-levelname-debugdatatype-element.md)           | string      | The level value passed to the provider when it was enabled.<br/>                                             |
| [**Message**](eventschema-message-debugdatatype-element.md)               | string      | The message string. The XML contains this element if the WPP event specified the FormattedString field.<br/> |
| [**SequenceNumber**](eventschema-sequencenumber-debugdatatype-element.md) | unsignedInt | The local or global sequence number of the trace message.<br/>                                               |
| [**SubComponent**](eventschema-subcomponent-debugdatatype-element.md)     | string      | The name of the subcomponent that logged the trace message.<br/>                                             |



## Remarks

The elements are included only if the provider set the %TRACE\_FORMAT\_PREFIX% environment variable to include them. For details on these elements, see Trace Message Prefix.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





