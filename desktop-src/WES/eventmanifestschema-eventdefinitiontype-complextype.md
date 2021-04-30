---
title: EventDefinitionType Complex Type
description: Defines an event that your provider can write.
ms.assetid: 09ea89c9-6618-4874-ac72-5ee19cde4040
keywords:
- EventDefinitionType complex type EventLog
topic_type:
- apiref
api_name:
- EventDefinitionType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# EventDefinitionType Complex Type

Defines an event that your provider can write.

``` syntax
<xs:complexType name="EventDefinitionType">
    <xs:simpleContent>
        <xs:extension
            base="string"
        >
            <xs:attribute name="value"
                type="UInt32Type"
                use="required"
             />
            <xs:attribute name="level"
                type="QName"
                use="optional"
             />
            <xs:attribute name="template"
                type="token"
                use="optional"
             />
            <xs:attribute name="channel"
                type="token"
                use="optional"
             />
            <xs:attribute name="keywords"
                type="QNameList"
                use="optional"
             />
            <xs:attribute name="task"
                type="QName"
                use="optional"
             />
            <xs:attribute name="opcode"
                type="QName"
                use="optional"
             />
            <xs:attribute name="symbol"
                type="CSymbolType"
                use="optional"
             />
            <xs:attribute name="version"
                type="unsignedByte"
                use="optional"
             />
            <xs:attribute name="message"
                type="strTableRef"
                use="optional"
             />
            <xs:attribute name="notLogged"
                type="boolean"
                use="optional"
                default="false"
             />
        </xs:extension>
    </xs:simpleContent>
</xs:complexType>
```

## Attributes



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>channel</td>
<td>token</td>
<td>An identifier that identifies the channel to where the event is written. Specify a channel identifier of one of the channels that you defined or imported. If the channel does not specify a channel identifier, use the channel's name. For details on defining or importing a channel, see the <a href="eventmanifestschema-channellisttype-complextype.md"><strong>ChannelListType</strong></a> complex type.<br/> If you do not specify a channel, the event is not written to a channel. Typically, the only reason not to specify a channel is if you are writing events only to an ETW session. For details, see creating an ETW session, see <a href="/windows/desktop/ETW/controlling-event-tracing-sessions">Controlling Event Tracing Sessions</a>.<br/></td>
</tr>
<tr class="even">
<td>keywords</td>
<td><a href="eventmanifestschema-qnamelist-simpletype.md"><strong>QNameList</strong></a></td>
<td>A space-separated list of keyword names that identify the category of events to which this event belongs. Specify a keyword name from the list of keywords that you define. For details on defining keywords, see the <a href="eventmanifestschema-keywordtype-complextype.md"><strong>KeywordType</strong></a> complex type.<br/> If you do not specify keywords, the event descriptor will contain a zero for keywords.<br/></td>
</tr>
<tr class="odd">
<td>level</td>
<td><strong>QName</strong></td>
<td>The level of verbosity to use when writing the event. Specify the name of a level that you defined in the manifest or one of the levels defined in the \Include\Winmeta.xml file that is included in the Windows SDK. For details on defining a level, see the <a href="eventmanifestschema-leveltype-complextype.md"><strong>LevelType</strong></a> complex type.<br/> If you do not specify a level, the event descriptor will contain a zero for level.<br/> You must specify a level if the channel type to which the event is written is Admin; the level must be one of the following levels defined in Winmeata.xml:
<ul>
<li>win:Critical</li>
<li>win:Error</li>
<li>win:Warning</li>
<li>win:Informational</li>
</ul>
<br/></td>
</tr>
<tr class="even">
<td>message</td>
<td><a href="eventmanifestschema-strtableref-simpletype.md"><strong>strTableRef</strong></a></td>
<td>The localized message for the event. The message string references a localized string in the <a href="eventmanifestschema-stringtable-resources-element.md"><strong>stringTable</strong></a> section of the manifest.<br/> You must specify a message if the channel type to which the event is written is Admin.<br/></td>
</tr>
<tr class="odd">
<td>notLogged</td>
<td>boolean</td>
<td>Determines whether the provider logs this event. Specify true if the provider logs this event; otherwise, false. Use this attribute to indicate that the provider is no longer logging this event instead of removing the event from the manifest. Retaining the event in the manifest will let consumers decode older etl files that include the event.<br/> <strong>Windows Server 2008 and Windows Vista:</strong> This attribute is not supported in versions of the message compiler that shipped prior to the Windows 7 version of the Windows SDK.<br/></td>
</tr>
<tr class="even">
<td>opcode</td>
<td><strong>QName</strong></td>
<td>The name of an opcode that identifies an operation within the task. Specify the name of an opcode that you defined in the manifest or one of the opcodes defined in Winmeta.xml. For details on defining an opcode, see the <a href="eventmanifestschema-opcodetype-complextype.md"><strong>OpcodeType</strong></a> complex type.<br/> If the task that you reference contains task-specific (local) opcodes, you can specify one of its task-specific opcodes or an opcode defined at the provider level (a global opcode). If you specify a global opcode, the value of the global opcode cannot be the same as one of the local opcodes for the task.<br/> If you reference a local opcode, the task attribute must reference the task to which the local opcode belongs.<br/> If you do not specify an opcode, the event descriptor will contain a zero for opcode.<br/></td>
</tr>
<tr class="odd">
<td>symbol</td>
<td><a href="eventmanifestschema-csymboltype-simpletype.md"><strong>CSymbolType</strong></a></td>
<td>The symbol to use to reference the event descriptor for this event in your application. The <a href="message-compiler--mc-exe-.md"><strong>Message Compiler (MC.exe)</strong></a> uses the symbol to create a constant for the event descriptor in the header file that the compiler generates. If you do not specify a symbol, the compiler generates one for you. You use the descriptor when you call the <a href="/windows/desktop/api/evntprov/nf-evntprov-eventwrite"><strong>EventWrite</strong></a> function to write the event.<br/></td>
</tr>
<tr class="even">
<td>task</td>
<td><strong>QName</strong></td>
<td>The name of a task that identifies the component or subcomponent that generates this event. Specify the name of a task that you defined in the manifest. For details on defining a task, see the <a href="eventmanifestschema-tasktype-complextype.md"><strong>TaskType</strong></a> complex type.<br/> If you do not specify a task, the event descriptor will contain a zero for task.<br/></td>
</tr>
<tr class="odd">
<td>template</td>
<td>token</td>
<td>The template identifier of the template that defines the data items that this event includes. Specify the identifier of a template that you defined in the manifest. For details on defining a template, see the <a href="eventmanifestschema-templateitemtype-complextype.md"><strong>TemplateItemType</strong></a> complex type.<br/></td>
</tr>
<tr class="even">
<td>value</td>
<td><a href="eventmanifestschema-hexint32type-simpletype.md"><strong>UInt32Type</strong></a></td>
<td>The event identifier. The identifier must be unique within the list of events that you define.<br/></td>
</tr>
<tr class="odd">
<td>version</td>
<td>unsignedByte</td>
<td>A one-byte version number of the event definition.<br/></td>
</tr>
</tbody>
</table>



## Remarks

If you use [**EvtFormatMessage**](/windows/desktop/api/WinEvt/nf-winevt-evtformatmessage) to format the message string for the event (or use the Event Viewer to view the message string), the message string can contain insertion strings and any of the format strings that the Win32 **FormatMessage** function supports. The insertion strings are limited to %*n* or %*n*!s! (for example, %1) where *n* is the one-based reference the data items defined in the event's template. The message string can also contain parameter insertion strings in the form %%*n* (for example, %%4). The maximum number of insertion strings that the message can contain is 100.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

