---
title: Win32\_PowerSettingCapabilities class
description: Represents the association between the power setting and the power setting definition. An instance of Win32\_PowerSettingCapabilities is created for each power setting.
ms.assetid: 3ae5bb65-7da4-4fda-abac-28620aff3f96
keywords:
- Win32_PowerSettingCapabilities class
- Win32_PowerSettingCapabilities class, described
topic_type:
- apiref
api_name:
- Win32_PowerSettingCapabilities
- Win32_PowerSettingCapabilities.ManagedElement
- Win32_PowerSettingCapabilities.Capabilities
api_location:
- PowerWmiProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Win32\_PowerSettingCapabilities class

Represents the association between the power setting and the power setting definition. An instance of **Win32\_PowerSettingCapabilities** is created for each power setting.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Provider("PowerWmiProvider"), Dynamic]
class Win32_PowerSettingCapabilities : CIM_ElementCapabilities
{
  string REF ManagedElement;
  string REF Capabilities;
};
```

## Members

The **Win32\_PowerSettingCapabilities** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_PowerSettingCapabilities** class has these properties.

<dl> <dt>

**Capabilities**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The **InstanceID** of the power setting definition that corresponds to the value of the setting.

</dd> <dt>

**ManagedElement**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The **InstanceID** of the power setting to which this setting data applies.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                               |
| Namespace<br/>                | Root\\CIMV2\\power<br/>                                                                   |
| MOF<br/>                      | <dl> <dt>PowerWmiProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>PowerWmiProvider.dll</dt> </dl> |



 

 





