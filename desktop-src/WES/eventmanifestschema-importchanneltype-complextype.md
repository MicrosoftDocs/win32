---
title: ImportChannelType Complex Type
description: Identifies a channel that has been defined by another provider or in a manifest that contains a metadata section.
ms.assetid: da14d837-0ed8-4d85-9820-46c77753768d
keywords:
- ImportChannelType complex type EventLog
topic_type:
- apiref
api_name:
- ImportChannelType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# ImportChannelType Complex Type

Identifies a channel that has been defined by another provider or in a manifest that contains a metadata section.

``` syntax
<xs:complexType name="ImportChannelType"
    mixed="true"
>
    <xs:simpleContent>
        <xs:extension
            base="string"
        >
            <xs:attribute name="chid"
                type="token"
                use="optional"
             />
            <xs:attribute name="name"
                type="anyURI"
                use="required"
             />
            <xs:attribute name="symbol"
                type="CSymbolType"
                use="optional"
             />
        </xs:extension>
    </xs:simpleContent>
</xs:complexType>
```

## Attributes



| Name   | Type                                                              | Description                                                                                                                                                                                                                                                                                                            |
|--------|-------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| chid   | token                                                             | An identifier that uniquely identifies the channel in the list of channels that the provider defines or imports. Use this value when referencing this channel in an event definition. If you do not specify a channel identifier, use the channel's name to reference this channel in an event definition.<br/>  |
| name   | anyURI                                                            | The name of the channel to import.<br/>                                                                                                                                                                                                                                                                          |
| symbol | [**CSymbolType**](eventmanifestschema-csymboltype-simpletype.md) | The symbol to use to reference the channel in your application. The [**Message Compiler (MC.exe)**](message-compiler--mc-exe-.md) uses the symbol to create a constant for the channel in the header file that the compiler generates. If you do not specify a symbol, the compiler generates one for you.<br/> |



## Remarks

The manifest that defined the imported channel must be installed before your provider writes events; otherwise, the events cannot be written to the channel (the write operation succeeds, the events are simply not written to the channel).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





