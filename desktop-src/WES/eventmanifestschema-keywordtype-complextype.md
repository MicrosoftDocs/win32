---
title: KeywordType Complex Type
description: Defines a keyword that identifies a category of events. | KeywordType Complex Type
ms.assetid: 6bd41d4a-1d55-4cce-a1f8-136f749fde2a
keywords:
- KeywordType complex type EventLog
topic_type:
- apiref
api_name:
- KeywordType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# KeywordType Complex Type

Defines a keyword that identifies a category of events. A keyword is a tag that you attach to an event to group events based on their usage.

``` syntax
<xs:complexType name="KeywordType"
    mixed="true"
>
    <xs:simpleContent>
        <xs:extension
            base="xs:string"
        >
            <xs:attribute name="name"
                type="QName"
                use="required"
             />
            <xs:attribute name="symbol"
                type="CSymbolType"
                use="optional"
             />
            <xs:attribute name="mask"
                type="HexInt64Type"
                use="required"
             />
            <xs:attribute name="message"
                type="strTableRef"
                use="optional"
             />
            <xs:anyAttribute
                processContents="lax"
                namespace="##other"
             />
        </xs:extension>
    </xs:simpleContent>
</xs:complexType>
```

## Attributes



| Name    | Type                                                              | Description                                                                                                                                                                                                                                                                                                            |
|---------|-------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| mask    | [**HexInt64Type**](eventmanifestschema-hex64type-simpletype.md)  | A bitmask that must have only a single bit set. The bit represents a category of events (for example, read events or write events). You can specify bit values in the range from 0x0000000000000001 through 0x0000800000000000 (bits 0 through 47).<br/>                                                         |
| message | [**strTableRef**](eventmanifestschema-strtableref-simpletype.md) | The localized display name for the keyword. The message string references a localized string in the [**stringTable**](eventmanifestschema-stringtable-resources-element.md) section of the manifest.<br/>                                                                                                       |
| name    | **QName**                                                         | The name of the keyword. The name must be unique within the list of keywords that the provider defines.<br/>                                                                                                                                                                                                     |
| symbol  | [**CSymbolType**](eventmanifestschema-csymboltype-simpletype.md) | The symbol to use to reference the keyword in your application. The [**Message Compiler (MC.exe)**](message-compiler--mc-exe-.md) uses the symbol to create a constant for the keyword in the header file that the compiler generates. If you do not specify a symbol, the compiler generates one for you.<br/> |



## Remarks

The Winmeta.xml file that is included in the Windows SDK contains a list of keywords. These keywords are reserved and should not be used.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





