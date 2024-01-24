---
title: ProviderType Complex Type
description: Defines a provider and the metadata that it uses to define its events. | ProviderType Complex Type
ms.assetid: 70199cf5-a6d0-4780-9ff1-ed083a5b49ac
keywords:
- ProviderType complex type EventLog
topic_type:
- apiref
api_name:
- ProviderType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# ProviderType Complex Type

Defines a provider and the metadata that it uses to define its events.

``` syntax
<xs:complexType name="ProviderType">
    <xs:choice
        minOccurs="0"
        maxOccurs="unbounded"
    >
        <xs:element name="channels"
            type="ChannelListType"
         />
        <xs:element name="levels"
            type="LevelListType"
         />
        <xs:element name="tasks"
            type="TaskListType"
         />
        <xs:element name="opcodes"
            type="OpcodeListType"
         />
        <xs:element name="keywords"
            type="KeywordListType"
         />
        <xs:element name="maps"
            type="MapType"
         />
        <xs:element name="namedQueries"
            type="NamedQueryType"
         />
        <xs:element name="templates"
            type="TemplateListType"
         />
        <xs:element name="events"
            type="DefinitionType"
         />
        <xs:element name="filters"
            type="FilterListType"
         />
        <xs:any
            processContents="lax"
            namespace="##other"
         />
    </xs:choice>
    <xs:attribute name="name"
        type="anyURI"
        use="required"
     />
    <xs:attribute name="guid"
        type="GUIDType"
        use="required"
     />
    <xs:attribute name="resourceFileName"
        type="filePath"
        use="optional"
     />
    <xs:attribute name="messageFileName"
        type="filePath"
        use="optional"
     />
    <xs:attribute name="parameterFileName"
        type="filePath"
        use="optional"
     />
    <xs:attribute name="helpLink"
        type="anyURI"
        use="optional"
     />
    <xs:attribute name="symbol"
        type="CSymbolType"
        use="required"
     />
    <xs:attribute name="message"
        type="strTableRef"
        use="optional"
     />
    <xs:attribute name="source"
        use="optional"
        default="Xml"
    >
        <xs:simpleType>
            <xs:restriction
                base="xs:string"
            >
                <xs:enumeration
                    value="Xml"
                 />
                <xs:enumeration
                    value="Wbem"
                 />
            </xs:restriction>
        </xs:simpleType>
    </xs:attribute>
    <xs:attribute name="warnOnApplicationCompatibilityError"
        type="xs:boolean"
        use="optional"
        default="false"
     />
    <xs:anyAttribute
        processContents="lax"
        namespace="##other"
     />
</xs:complexType>
```

## Child elements



| Element                                                                       | Type                                                                         | Description                                                                                                                                                                                                                                                   |
|-------------------------------------------------------------------------------|------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**channels**](eventmanifestschema-channels-providertype-element.md)         | [**ChannelListType**](eventmanifestschema-channellisttype-complextype.md)   | Defines a list of channels to which providers can log events.<br/>                                                                                                                                                                                      |
| [**events**](eventmanifestschema-events-providertype-element.md)             | [**DefinitionType**](eventmanifestschema-definitiontype-complextype.md)     | Defines a list of event definitions of the events that the provider can log.<br/>                                                                                                                                                                       |
| **filters**                                                                   | [**FilterListType**](eventmanifestschema-filterlisttype-complextype.md)     | Defines a list of filters that your provider supports. You can use the filters, as you would level and keywords, to determine if you want to write an event. <br/> **Windows Server 2008 and Windows Vista:** Not supported until Windows 7.<br/> |
| [**keywords**](eventmanifestschema-keywords-providertype-element.md)         | [**KeywordListType**](eventmanifestschema-keywordlisttype-complextype.md)   | Defines a list of keywords that categorize events.<br/>                                                                                                                                                                                                 |
| [**levels**](eventmanifestschema-levels-providertype-element.md)             | [**LevelListType**](eventmanifestschema-levellisttype-complextype.md)       | Defines a list of levels that specify the severity of an event.<br/>                                                                                                                                                                                    |
| [**maps**](eventmanifestschema-maps-providertype-element.md)                 | [**MapType**](eventmanifestschema-maptype-complextype.md)                   | Defines a list of name/value pairs that you can reference in the template section of the manifest.<br/>                                                                                                                                                 |
| [**namedQueries**](eventmanifestschema-namedqueries-providertype-element.md) | [**NamedQueryType**](eventmanifestschema-namedquerytype-complextype.md)     | Not used. Defines a list of named queries that query the event message string for a value and perform a specified action if found.<br/>                                                                                                                 |
| [**opcodes**](eventmanifestschema-opcodes-providertype-element.md)           | [**OpcodeListType**](eventmanifestschema-opcodelisttype-complextype.md)     | Defines a list of opcodes that you can use to group events within a task.<br/>                                                                                                                                                                          |
| [**tasks**](eventmanifestschema-tasks-providertype-element.md)               | [**TaskListType**](eventmanifestschema-tasklisttype-complextype.md)         | Defines a list of tasks that a provider can use to group events. Typically, you use tasks to group events for a feature or component of the provider.<br/>                                                                                              |
| [**templates**](eventmanifestschema-templates-providertype-element.md)       | [**TemplateListType**](eventmanifestschema-templatelisttype-complextype.md) | Defines a list of templates that specify the data to include with the events.<br/>                                                                                                                                                                      |



## Attributes



| Name                                | Type                                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-------------------------------------|-------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| guid                                | [**GUIDType**](eventmanifestschema-guidtype-simpletype.md)       | A GUID that uniquely identifies the provider.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| helpLink                            | anyURI                                                            | The URL or MS help link to content that provides information about the events that the provider raises.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                           |
| message                             | [**strTableRef**](eventmanifestschema-strtableref-simpletype.md) | The localized display name for the provider. The message string references a localized string in the [**stringTable**](eventmanifestschema-stringtable-resources-element.md) section of the manifest. <br/>                                                                                                                                                                                                                                                                                                                           |
| messageFileName                     | [**filePath**](eventmanifestschema-filepath-simpletype.md)       | The full path to the file that contains the provider's localized message resources. The file can be an executable file or DLL file.<br/>                                                                                                                                                                                                                                                                                                                                                                                               |
| name                                | anyURI                                                            | The name of the provider. The name should be of the form, *Company*-*Product*-*Component*.<br/> The name cannot be longer than 255 characters, and cannot contain the characters: '>', '<', '&', '"', '\|', '\\', ':', '', '?', '\*', or characters with codes less than 31. In addition, the name must follow the general constraints on file and registry key names. These constraints can be found at [Naming a File](/windows/desktop/FileIO/naming-a-file), and [Registry Element Size Limits](/windows/desktop/SysInfo/registry-element-size-limits).<br/> |
| parameterFileName                   | [**filePath**](eventmanifestschema-filepath-simpletype.md)       | The full path to the file that contain the provider's parameter string resources. The file can be an executable file or DLL file. You can specify more than one parameter file separated by a semicolon. The file is searched when an event's message string contains a parameter string. Parameters let you provide localizable insert strings. See Remarks for more information.<br/>                                                                                                                                                |
| resourceFileName                    | [**filePath**](eventmanifestschema-filepath-simpletype.md)       | The full path to the file that contains the provider's metadata resources. The file can be an executable file or DLL file.<br/>                                                                                                                                                                                                                                                                                                                                                                                                        |
| source                              |                                                                   | For internal use only.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| symbol                              | [**CSymbolType**](eventmanifestschema-csymboltype-simpletype.md) | The symbol to use to reference the provider's GUID in your application. The [**Message Compiler (MC.exe)**](message-compiler--mc-exe-.md) uses the symbol to create a constant for the provider's GUID in the header file that the compiler generates.<br/>                                                                                                                                                                                                                                                                           |
| warnOnApplicationCompatibilityError | **xs:boolean**                                                    | For internal use only.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |



## Remarks

The Windows Event Viewer (Eventvwr.exe) will use the localized message string if available; otherwise, it uses the string from the name attribute.

The paths for resourceFileName, messageFileName, and parameterFileName can contain environment variables. If you define a new environment variable to use in the path, you must restart the computer so that the event log service can pick up the new variable; otherwise, the service will not be able to find your provider's resources.

An event's message string can contain insertion strings and parameter strings. An insertion string is of the form %*n*, where *n* is a one-based index that identifies a data item from the event's data template that you want to insert into the message. A parameter string (see the **parameterFileName** attribute) is of the form %%*n*, where n is the identifier of a message in the message table. If the event's message string contained "%1 %%11 = %2 %%12" and the data item values for %1 and %2 were 8 and 2, respectively, and the parameter strings for %%11 and %%12 were "quarts" and "gallons", respectively, the formatted string would be "8 quarts = 2 gallons".

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

