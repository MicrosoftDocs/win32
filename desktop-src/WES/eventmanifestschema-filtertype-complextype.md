---
title: FilterType Complex Type
description: Defines a data filter that a session uses to filter events based on event data.
ms.assetid: f2874b3f-cf3a-4dd9-b914-6adaac33cf7b
keywords:
- FilterType complex type EventLog
topic_type:
- apiref
api_name:
- FilterType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# FilterType Complex Type

Defines a data filter that a session uses to filter events based on event data.

``` syntax
<xs:complexType name="FilterType">
    <xs:simpleContent>
        <xs:extension
            base="string"
        >
            <xs:attribute name="value"
                type="UInt8Type"
                use="required"
             />
            <xs:attribute name="version"
                type="UInt8Type"
                use="optional"
             />
            <xs:attribute name="name"
                type="QName"
                use="required"
             />
            <xs:attribute name="symbol"
                type="CSymbolType"
                use="optional"
             />
            <xs:attribute name="message"
                type="strTableRef"
                use="optional"
             />
            <xs:attribute name="tid"
                type="token"
                use="optional"
             />
        </xs:extension>
    </xs:simpleContent>
</xs:complexType>
```

## Attributes



| Name    | Type                                                              | Description                                                                                                                                                                                                                                      |
|---------|-------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| message | [**strTableRef**](eventmanifestschema-strtableref-simpletype.md) | The localized description for the filter. The message string references a localized string in the [**stringTable**](eventmanifestschema-stringtable-resources-element.md) section of the manifest.<br/>                                   |
| name    | **QName**                                                         | A name that identifies the filter.<br/>                                                                                                                                                                                                    |
| symbol  | [**CSymbolType**](eventmanifestschema-csymboltype-simpletype.md) | The symbol to use to reference the filter in your application. The [**Message Compiler (MC.exe)**](message-compiler--mc-exe-.md) uses the symbol to create a constant for the filter in the header file that the compiler generates.<br/> |
| tid     | token                                                             | A template identifier that describes the filter data that the session passes to the provider when it enables the provider.<br/>                                                                                                            |
| value   | [**UInt8Type**](eventmanifestschema-hexint8type-simpletype.md)   | An integer value that uniquely identifies the filter within the list of filters that you define.<br/>                                                                                                                                      |
| version | [**UInt8Type**](eventmanifestschema-hexint8type-simpletype.md)   | An integer value that identifies this version of the filter. If not specified, the value is zero.<br/>                                                                                                                                     |



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



 

 





