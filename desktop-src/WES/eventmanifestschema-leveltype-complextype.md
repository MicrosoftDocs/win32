---
title: LevelType Complex Type
description: Defines a severity value that determines the verbosity of the events being logged.
ms.assetid: c71aedef-7c43-4343-9d6d-94eb45da49b9
keywords:
- LevelType complex type EventLog
topic_type:
- apiref
api_name:
- LevelType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# LevelType Complex Type

Defines a severity value that determines the verbosity of the events being logged.

``` syntax
<xs:complexType name="LevelType"
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
            <xs:attribute name="value"
                type="UInt8Type"
                use="required"
             />
            <xs:attribute name="message"
                type="strTableRef"
                use="optional"
             />
        </xs:extension>
    </xs:simpleContent>
</xs:complexType>
```

## Attributes



| Name    | Type                                                              | Description                                                                                                                                                                                                                                                                                                        |
|---------|-------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| message | [**strTableRef**](eventmanifestschema-strtableref-simpletype.md) | The localized display name for the level. The message string references a localized string in the [**stringTable**](eventmanifestschema-stringtable-resources-element.md) section of the manifest. <br/>                                                                                                    |
| name    | **QName**                                                         | The name to assign to this level. This name must be unique within the scope of the provider.<br/>                                                                                                                                                                                                            |
| symbol  | [**CSymbolType**](eventmanifestschema-csymboltype-simpletype.md) | The symbol to use to reference the level in your application. The [**Message Compiler (MC.exe)**](message-compiler--mc-exe-.md) uses the symbol to create a constant for the level in the header file that the compiler generates. If you do not specify a symbol, the compiler generates one for you.<br/> |
| value   | [**UInt8Type**](eventmanifestschema-hexint8type-simpletype.md)   | The level value. You can specify values in the range 16 to 255. For predefined level values, see Remarks.<br/>                                                                                                                                                                                               |



## Remarks

The following are the predefined level values that you can use. These values are defined in the Winmeta.xml file that is included in the Windows SDK.



| Name              | Value | Symbol                    | Description                                                             |
|-------------------|-------|---------------------------|-------------------------------------------------------------------------|
| win:Critical      | 1     | WINEVENT\_LEVEL\_CRITICAL | Identifies an abnormal exit or termination event.<br/>            |
| win:Error         | 2     | WINEVENT\_LEVEL\_ERROR    | Identifies a severe error event.<br/>                             |
| win:Warning       | 3     | WINEVENT\_LEVEL\_WARNING  | Identifies a warning event such as an allocation failure.<br/>    |
| win:Informational | 4     | WINEVENT\_LEVEL\_INFO     | Identifies a non-error event such as an entry or exit event.<br/> |
| win:Verbose       | 5     | WINEVENT\_LEVEL\_VERBOSE  | Identifies a detailed trace event.<br/>                           |



 

Higher numbers imply that you get lower levels as well. For example, if you specify win:Warning, you receive all warning, error, and critical events.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





