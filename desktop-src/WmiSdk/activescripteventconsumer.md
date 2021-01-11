---
description: Runs a predefined script in an arbitrary scripting language when an event is delivered to it.
ms.assetid: 2c0aa216-4255-49ff-9bbd-d6c62b5b9139
ms.tgt_platform: multiple
title: ActiveScriptEventConsumer class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ActiveScriptEventConsumer
- ActiveScriptEventConsumer.CreatorSID
- ActiveScriptEventConsumer.KillTimeout
- ActiveScriptEventConsumer.MachineName
- ActiveScriptEventConsumer.MaximumQueueSize
- ActiveScriptEventConsumer.Name
- ActiveScriptEventConsumer.ScriptingEngine
- ActiveScriptEventConsumer.ScriptFileName
- ActiveScriptEventConsumer.ScriptText
api_type: 
- DllExport
api_location: 
- Scrcons.exe
---

# ActiveScriptEventConsumer class

The **ActiveScriptEventConsumer** class runs a predefined script in an arbitrary scripting language when an event is delivered to it. This class is one of the standard event consumers that WMI provides. For more information, see [Monitoring and Responding to Events with Standard Consumers](monitoring-and-responding-to-events-with-standard-consumers.md).


```cmd
Mofcomp -n:root\<namespace> scrcons.mof
```



You can configure the performance of all instances of **ActiveScriptEventConsumer** on a system by setting the values of either the [**Timeout**](scriptingstandardconsumersetting.md) or **MaximumScripts** property in the single instance of **ScriptingStandardConsumerSetting**.

## Syntax

``` syntax
[AMENDMENT]
class ActiveScriptEventConsumer : __EventConsumer
{
  uint8  CreatorSID[] = {1,1,0,0,0,0,0,5,18,0,0,0};
  uint32 KillTimeout = 0;
  string MachineName;
  uint32 MaximumQueueSize;
  string Name;
  string ScriptingEngine;
  string ScriptFileName;
  string ScriptText;
};
```

## Members

The **ActiveScriptEventConsumer** class has these types of members:

-   [Properties](#properties)

### Properties

The **ActiveScriptEventConsumer** class has these properties.

<dl> <dt>

**CreatorSID**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Array that represents the security identifier (SID), which uniquely identifies the creator of the Active Script Event consumer. This property is inherited from [**\_\_EventConsumer**](--eventconsumer.md).

</dd> <dt>

**KillTimeout**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number, in seconds, that the script is allowed to run. If 0 (zero), which is the default, the script is not terminated.

</dd> <dt>

**MachineName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the computer to which WMI sends events. By convention of Microsoft standard consumers, the script consumer cannot be run remotely. Third-party consumers can also use this property. This property is inherited from [**\_\_EventConsumer**](--eventconsumer.md).

</dd> <dt>

**MaximumQueueSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum queue, in bytes, for the Active Script Event consumer. This property is inherited from [**\_\_EventConsumer**](--eventconsumer.md).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Key**](standard-qualifiers.md)
</dt> </dl>

Unique identifier for the event consumer. If you rename the consumer, the result is two equal consumers that have different names.

</dd> <dt>

**ScriptFileName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the file from which the script text is read, intended as an alternative to specifying the text of the script in the **ScriptText** property. This property must be **NULL** if the **ScriptText** property is not **NULL**.

> [!Note]  
> When you specify the **ScriptFileName**, it is important to secure the executable that you are launching. If the executable is not in a secure location or secured with a strong access control list (ACL), anyone can replace the executable with a different one. For more information about ACLs, see [Creating a Security Descriptor (SD) for a New Object in C++](/windows/desktop/SecAuthZ/creating-a-security-descriptor-for-a-new-object-in-c--).

 

</dd> <dt>

**ScriptingEngine**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the scripting engine to use, for example, "VBScript". This property cannot be **NULL**.

</dd> <dt>

**ScriptText**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Text of the script that is expressed in a language known to the scripting engine. This property must be **NULL** if the **ScriptFileName** property is not **NULL**.

</dd> </dl>

## Remarks

This class is derived from the [**\_\_EventConsumer**](--eventconsumer.md) abstract class. It is located in the root\\subscription namespace.

When the text of a script is specified in the event consumer instance, the script has access to the event instance in the script environment variable **TargetEvent**.

The scripts run in the LocalSystem security context. As a security measure, only a local system administrator or a domain administrator can configure the scripting consumer. Access rights are not checked until run time. After the consumer is configured, any user can trigger the event that causes the script to .

Failure to load the scripting engine or parse and validate the script is considered a failure. Error return codes from the script and terminating the script by using a time-out are also considered failures.

Either **ScriptText** or **ScriptFileName** must be not **NULL**. If both properties are **NULL** or not **NULL**, an error is generated.

When WMI is run as a service, scripts run by **ActiveScriptEventConsumer** do not generate screen output. Scripts that use **MsgBox** do run, but they do not display information on the screen. Running the WMI service as an executable file is not supported, but WMI allows scripts that use the **MsgBox** function to display output or accept user input. None of the methods provided by the [WScript](/previous-versions//at5ydy31(v=vs.85)) object can be used because **ActiveScriptEventConsumer** does not use Windows Script Host (WSH).

## Examples

The [Create Permanent WMI Event registration to monitor files](https://Gallery.TechNet.Microsoft.Com/Create-Permenant-WMI-Event-f67ce5c2) PowerShell example on TechNet Gallery uses **ActiveScriptEventConsumer** as part of a complex script to set up a permanent WMI event registration.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\subscription<br/>                                                          |
| MOF<br/>                      | <dl> <dt>Scrcons.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Scrcons.exe</dt> </dl> |



## See also

<dl> <dt>

[Standard Consumer Classes](standard-consumer-classes.md)
</dt> <dt>

[Running a Script Based on an Event](running-a-script-based-on-an-event.md)
</dt> <dt>

[Receiving Events At All Times](receiving-events-at-all-times.md)
</dt> <dt>

[Creating a Logical Consumer](creating-a-logical-consumer.md)
</dt> <dt>

[**\_\_EventConsumer**](--eventconsumer.md)
</dt> <dt>

[**ScriptingStandardConsumerSetting**](scriptingstandardconsumersetting.md)
</dt> </dl>

 

