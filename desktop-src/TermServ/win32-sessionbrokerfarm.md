---
title: Win32_SessionBrokerFarm class
description: Defines the query for a session broker farm.
ms.assetid: 55a2a7ea-e891-4723-b919-ee3c908eaffb
ms.tgt_platform: multiple
keywords:
- Win32_SessionBrokerFarm class Remote Desktop Services
- Win32_SessionBrokerFarm class Remote Desktop Services , described
topic_type:
- apiref
api_name:
- Win32_SessionBrokerFarm
- Win32_SessionBrokerFarm.PluginName
- Win32_SessionBrokerFarm.FarmName
api_location:
- TssdWmi.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Win32\_SessionBrokerFarm class

Defines the query for a session broker farm.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("Win32_WIN32_SESSIONBROKERFARM_Prov"), AMENDMENT]
class Win32_SessionBrokerFarm
{
  string PluginName;
  string FarmName;
};
```

## Members

The **Win32\_SessionBrokerFarm** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_SessionBrokerFarm** class has these properties.

<dl> <dt>

**FarmName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

The name of the session broker farm that needs to be queried.

</dd> <dt>

**PluginName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

The name of the plug-in.

</dd> </dl>

## Examples

The following query string demonstrates how the **Win32\_SessionBrokerFarm** class is used in a query.


```CSharp
queryString = string.Format("SELECT * FROM Win32_SessionBrokerFarm WHERE PluginName = '{0}'", pluginName);
```



## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                      |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                               |
| MOF<br/>                      | <dl> <dt>TssdWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>TssdWmi.dll</dt> </dl> |



 

