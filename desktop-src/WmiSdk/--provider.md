---
description: Serves as the parent class for the \_\_Win32Provider system class.
ms.assetid: e4cad7c6-4650-4334-b8c4-ac65381bced7
ms.tgt_platform: multiple
title: '__Provider class'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- __Provider
- All
api_type: 
- Schema
api_location: 
- All
---

# \_\_Provider class

The **\_\_Provider** system class is an abstract base class that serves as the parent class for the [**\_\_Win32Provider**](--win32provider.md) system class.

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[abstract]
class __Provider : __SystemClass
{
  string Name;
};
```

## Members

The **\_\_Provider** class has these types of members:

-   [Properties](#properties)

### Properties

The **\_\_Provider** class has these properties.

<dl> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Key**](standard-qualifiers.md)
</dt> </dl>

Language-neutral string that uniquely identifies the provider. The following format is suggested to prevent naming conflicts:

vendor\|provider\|version

For example, this provider name represents version 1.0 of the Microsoft TestProvider:

"Microsoft\|TestProvider\|V1.0"

</dd> </dl>

## Remarks

The **\_\_Provider** class is derived from [**\_\_SystemClass**](--systemclass.md), which has no properties.

Providers create [**\_\_Win32Provider**](--win32provider.md) instances to specify information about their physical implementation.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |
| Namespace<br/>                | All WMI namespaces<br/>  |



## See also

<dl> <dt>

[**\_\_SystemClass**](/windows/desktop/WmiSdk/--systemclass)
</dt> <dt>

[WMI System Classes](wmi-system-classes.md)
</dt> <dt>

[**\_\_Win32Provider**](--win32provider.md)
</dt> </dl>

 

