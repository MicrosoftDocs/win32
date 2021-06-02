---
title: OpcodeType Complex Type
description: Defines an operation within a component of the application.
ms.assetid: d97953df-669b-4c55-b1a8-925022b339b7
keywords:
- OpcodeType complex type EventLog
topic_type:
- apiref
api_name:
- OpcodeType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# OpcodeType Complex Type

Defines an operation within a component of the application. Used in conjunction with a task to identify the section of the application that is logging the event.

``` syntax
<xs:complexType name="OpcodeType"
    mixed="true"
>
    <xs:simpleContent>
        <xs:extension
            base="string"
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
            <xs:attribute name="mofValue"
                type="UInt8Type"
                use="optional"
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



| Name     | Type                                                              | Description                                                                                                                                                                                                                                                                                                          |
|----------|-------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| message  | [**strTableRef**](eventmanifestschema-strtableref-simpletype.md) | The localized display name for the opcode. The message string references a localized string in the [**stringTable**](eventmanifestschema-stringtable-resources-element.md) section of the manifest. <br/>                                                                                                     |
| mofValue | [**UInt8Type**](eventmanifestschema-hexint8type-simpletype.md)   | Reserved for internal use only.<br/>                                                                                                                                                                                                                                                                           |
| name     | **QName**                                                         | The name of the opcode. This name must be unique within the scope of this provider. <br/>                                                                                                                                                                                                                      |
| symbol   | [**CSymbolType**](eventmanifestschema-csymboltype-simpletype.md) | The symbol to use to reference the opcode in your application. The [**Message Compiler (MC.exe)**](message-compiler--mc-exe-.md) uses the symbol to create a constant for the opcode in the header file that the compiler generates. If you do not specify a symbol, the compiler generates one for you.<br/> |
| value    | [**UInt8Type**](eventmanifestschema-hexint8type-simpletype.md)   | The opcode value. You can specify values in the range 10 and 239. For a list of predefined opcode values, see Remarks.<br/>                                                                                                                                                                                    |



## Remarks

The following are the predefined opcode values that you can use. These values are defined in the Winmeta.xml file that is included in the Windows SDK.



| Name          | Value | Symbol                      | Description                                                                                            |
|---------------|-------|-----------------------------|--------------------------------------------------------------------------------------------------------|
| win:Info      | 0     | WINEVENT\_OPCODE\_INFO      | An informational event.                                                                                |
| win:Start     | 1     | WINEVENT\_OPCODE\_START     | An event that represents starting an activity.                                                         |
| win:Stop      | 2     | WINEVENT\_OPCODE\_STOP      | An event that represents stopping an activity. The event corresponds to the last unpaired start event. |
| win:DC\_Start | 3     | WINEVENT\_OPCODE\_DC\_START | An event that represents data collection starting. These are rundown event types.                      |
| win:DC\_Stop  | 4     | WINEVENT\_OPCODE\_DC\_STOP  | An event that represents data collection stopping. These are rundown event types.                      |
| win:Extension | 5     | WINEVENT\_OPCODE\_EXTENSION | An extension event.                                                                                    |
| win:Reply     | 6     | WINEVENT\_OPCODE\_REPLY     | A reply event.                                                                                         |
| win:Resume    | 7     | WINEVENT\_OPCODE\_RESUME    | An event that represents an activity resuming after being suspended.                                   |
| win:Suspend   | 8     | WINEVENT\_OPCODE\_SUSPEND   | An event that represents the activity being suspended pending another activity's completion.           |
| win:Send      | 9     | WINEVENT\_OPCODE\_SEND      | An event that represents transferring activity to another component.                                   |
| win:Receive   | 240   | WINEVENT\_OPCODE\_RECEIVE   | An event that represents receiving an activity transfer from another component.                        |



 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





