---
title: TaskType Complex Type
description: Defines a component or subcomponent of an application. | TaskType Complex Type
ms.assetid: d117636d-6363-43b6-ac5a-52234ac7c729
keywords:
- TaskType complex type EventLog
topic_type:
- apiref
api_name:
- TaskType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# TaskType Complex Type

Defines a component or subcomponent of an application.

``` syntax
<xs:complexType name="TaskType"
    mixed="true"
>
    <xs:sequence>
        <xs:element name="opcodes"
            type="OpcodeListType"
            minOccurs="0"
         />
    </xs:sequence>
    <xs:attribute name="name"
        type="QName"
        use="required"
     />
    <xs:attribute name="symbol"
        type="CSymbolType"
        use="optional"
     />
    <xs:attribute name="value"
        type="UInt16Type"
        use="required"
     />
    <xs:attribute name="eventGUID"
        type="GUIDType"
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
</xs:complexType>
```

## Child elements



| Element                                                         | Type                                                                     | Description                                                                                                                            |
|-----------------------------------------------------------------|--------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| [**opcodes**](eventmanifestschema-opcodes-tasktype-element.md) | [**OpcodeListType**](eventmanifestschema-opcodelisttype-complextype.md) | Defines a list of task-specific opcodes. You cannot use the opcode values defined in Winmeta.xml for task-specific opcodes.<br/> |



## Attributes



| Name      | Type                                                              | Description                                                                                                                                                                                                                                                                                                      |
|-----------|-------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| eventGUID | [**GUIDType**](eventmanifestschema-guidtype-simpletype.md)       | A globally unique identifier, in Registry format, that identifies the task. This attribute is required if you use the -mof message compiler argument to generate a MOF class for downlevel support.<br/>                                                                                                   |
| message   | [**strTableRef**](eventmanifestschema-strtableref-simpletype.md) | The localized display name for the task. The message string references a localized string in the [**stringTable**](eventmanifestschema-stringtable-resources-element.md) section of the manifest. <br/>                                                                                                   |
| name      | **QName**                                                         | The name of the task.<br/>                                                                                                                                                                                                                                                                                 |
| symbol    | [**CSymbolType**](eventmanifestschema-csymboltype-simpletype.md) | The symbol to use to reference the task in your application. The [**Message Compiler (MC.exe)**](message-compiler--mc-exe-.md) uses the symbol to create a constant for the task in the header file that the compiler generates. If you do not specify a symbol, the compiler generates one for you.<br/> |
| value     | [**UInt16Type**](eventmanifestschema-hexint16type-simpletype.md) | A numeric value that uniquely identifies this task within the list of tasks that the provider defines. The value must be in the range from 1 through 239.<br/>                                                                                                                                             |



## Examples

The following example shows how to specify a task.


```XML
<tasks>
  <task name="printspool:Disconnect" 
         symbol="PRINTSPOOL_TASK_DISCONNECT"
         value="0" 
         message="$(string.disconnect)"/>
 
  <task name="printspool:Connect" 
         symbol="PRINTSPOOL_TASK_CONNECT"
         value="1" 
         message="$(string.connect)">
       <opcodes>
          <opcode name="ReadRegistry" 
                  symbol="MYOPCODE_READ_REGISTRY" value="11"
                  message="$(string.ReadRegistry)"/>
       </opcodes>
   </task>
</tasks>
```



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





