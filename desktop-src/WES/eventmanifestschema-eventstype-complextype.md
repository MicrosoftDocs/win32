---
title: EventsType Complex Type
description: Contains a list of providers that are defined in the manifest. | EventsType Complex Type
ms.assetid: 43f9f577-eae0-45c5-aaf0-5a6df28d3b79
keywords:
- EventsType complex type EventLog
topic_type:
- apiref
api_name:
- EventsType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# EventsType Complex Type

Contains a list of providers that are defined in the manifest.

``` syntax
<xs:complexType name="EventsType">
    <xs:choice
        maxOccurs="unbounded"
    >
        <xs:element name="provider"
            type="ProviderType"
            maxOccurs="unbounded"
         />
        <xs:element name="messageTable"
            minOccurs="0"
        >
            <xs:complexType>
                <xs:sequence>
                    <xs:element name="message"
                        minOccurs="0"
                        maxOccurs="unbounded"
                    >
                        <xs:complexType>
                            <xs:attribute name="value"
                                type="UInt32Type"
                                use="required"
                             />
                            <xs:attribute name="mid"
                                type="xs:string"
                                use="optional"
                             />
                            <xs:attribute name="message"
                                type="strTableRef"
                                use="required"
                             />
                            <xs:attribute name="symbol"
                                type="CSymbolType"
                                use="optional"
                             />
                        </xs:complexType>
                    </xs:element>
                </xs:sequence>
            </xs:complexType>
        </xs:element>
        <xs:any
            processContents="lax"
            minOccurs="0"
            maxOccurs="unbounded"
            namespace="##other"
         />
    </xs:choice>
    <xs:anyAttribute
        namespace="##other"
     />
</xs:complexType>
```

## Child elements

| Element | Type | Description |
|---------|------|-------------|
| message |      | Defines a message string. |
| messageTable | | Defines a list of message strings. You should not have to use a message table except in the following cases where you must define a message table to explicitly assign resource numbers to message strings. <ul><li>You are migrating from a message text (.mc) file to a manifest but are still writing events to the application and system channels, so that legacy consumers to continue consuming the events. To make this work, the resource identifiers for the message strings defined in the manifest must be the same as the event identifiers. However, the message compiler automatically assigns resource identifiers to the message strings. To override the compiler, use the message table and set the value attribute to the event identifier and the message attribute to refer to a string in the string table in the localization section of the manifest.</li><li>If you want to identify more than 16 providers, you must include the message table that the seventeenth and on providers must use to assign resource values for the message strings that they define. If the provider references message strings that providers 1 through 16 defined, you do not include those message strings in the message table.</li></ul>|
| [**provider**](eventmanifestschema-provider-eventstype-element.md) | [**ProviderType**](eventmanifestschema-providertype-complextype.md) | A list of providers that you want to define. |

## Attributes

| Name    | Type                                                             | Description                                                                            |
|---------|------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| message | [**strTableRef**](eventmanifestschema-strtableref-simpletype.md) | A reference to the localized string in the string table.                               |
| mid     | xs:string                                                        | Not used.                                                                              |
| symbol  | [**CSymbolType**](eventmanifestschema-csymboltype-simpletype.md) | The symbolic name that you want the message compiler to create for this message string.|
| value   | [**UInt32Type**](eventmanifestschema-hexint32type-simpletype.md) | The number to use as the message identifier for this message.                          |


## Remarks

The practical limit of the number of providers that you can define in a manifest is 16 providers. If you specify more than 16 providers, you must use a message table to explicitly assign resource numbers to the message strings that the provider references. For more details, see the message element above.

## Requirements

| Requirement | Value |
|--------------------------|-------------------------------------------|
| Minimum supported client | Windows Vista \[desktop apps only\]       |
| Minimum supported server | Windows Server 2008 \[desktop apps only\] |
