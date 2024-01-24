---
description: The singleton ScriptingStandardConsumerSetting class provides registration data that is common to all instances of the ActiveScriptEventConsumer standard consumer class.
ms.assetid: d217e058-3529-4173-b896-ebff3d7b05c6
ms.tgt_platform: multiple
title: ScriptingStandardConsumerSetting class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ScriptingStandardConsumerSetting
- ScriptingStandardConsumerSetting.Caption
- ScriptingStandardConsumerSetting.Description
- ScriptingStandardConsumerSetting.MaximumScripts
- ScriptingStandardConsumerSetting.SettingID
- ScriptingStandardConsumerSetting.Timeout
api_type: 
- DllExport
api_location: 
- Scrcons.exe
---

# ScriptingStandardConsumerSetting class

The singleton **ScriptingStandardConsumerSetting** class provides registration data that is common to all instances of the [**ActiveScriptEventConsumer**](activescripteventconsumer.md) standard consumer class. An **ActiveScriptEventConsumer** instance uses the **MaximumScripts** and **Timeout** properties. For more information, see [Monitoring and Responding to Events with Standard Consumers](monitoring-and-responding-to-events-with-standard-consumers.md).

The following syntax is simplified from Managed Object Format (MOF) code and includes all of its inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Singleton, AMENDMENT]
class ScriptingStandardConsumerSetting : CIM_Setting
{
  string Caption = "Scripting Standard Consumer Setting";
  string Description = "Registration data common to all instances of the Scripting Standard Consumer";
  uint32 MaximumScripts = 300;
  string SettingID = "ScriptingStandardConsumerSetting";
  uint32 Timeout = 0;
};
```

## Members

The **ScriptingStandardConsumerSetting** class has these types of members:

-   [Properties](#properties)

### Properties

The **ScriptingStandardConsumerSetting** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](standard-qualifiers.md) (64)
</dt> </dl>

A short description of an object a one line string. Contains the string **ScriptingStandardConsumerSetting** because this is a singleton class.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A text description of an object.

</dd> <dt>

**MaximumScripts**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Maximum number of scripts that are run before a consumer starts a new instance. To clear out memory leaks from scripts, shut down the consumer regularly. The default value is 300.

</dd> <dt>

**SettingID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](standard-qualifiers.md) (256)
</dt> </dl>

Identifier for the setting object.

</dd> <dt>

**Timeout**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**units**](standard-qualifiers.md) ("Minutes")
</dt> </dl>

Maximum number of minutes before a consumer starts a new instance. If 0 (zero), the **MaximumScripts** property controls the consumer lifetime. The valid range for **Timeout** is 0 through 71,000 and the default value is 0 (zero).

</dd> </dl>

## Remarks

The single instance of the **ScriptingStandardConsumerSetting** class resides in the root\\cimv2 namespace.

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

[**CIM\_Setting**](/windows/desktop/CIMWin32Prov/cim-setting)
</dt> <dt>

[Standard Consumer Classes](standard-consumer-classes.md)
</dt> <dt>

[Running a Script Based on an Event](running-a-script-based-on-an-event.md)
</dt> <dt>

[Creating a Logical Consumer](creating-a-logical-consumer.md)
</dt> <dt>

[Receiving Events At All Times](receiving-events-at-all-times.md)
</dt> <dt>

[**\_\_EventConsumer**](--eventconsumer.md)
</dt> </dl>

 

