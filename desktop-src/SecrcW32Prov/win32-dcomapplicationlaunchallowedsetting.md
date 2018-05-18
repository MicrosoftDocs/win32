---
Description: 'The Win32\_DCOMApplicationLaunchAllowedSetting association WMI class relates the Win32\_DCOMApplication instance and the user SIDs that can launch it.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '87896b0e-9574-4d22-ad79-c3daf28aa847'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'Win32\_DCOMApplicationLaunchAllowedSetting class'
---

# Win32\_DCOMApplicationLaunchAllowedSetting class

The **Win32\_DCOMApplicationLaunchAllowedSetting** association [WMI class](https://msdn.microsoft.com/library/aa393244) relates the [**Win32\_DCOMApplication**](https://msdn.microsoft.com/library/aa394115) instance and the user SIDs that can launch it.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Association, Dynamic, Provider("CIMWin32"), UUID("{0F73ED55-8ED9-11d2-B340-00105A1F8569}"), AMENDMENT]
class Win32_DCOMApplicationLaunchAllowedSetting
{
  Win32_DCOMApplication REF Element;
  Win32_SID             REF Setting;
};
```

## Members

The **Win32\_DCOMApplicationLaunchAllowedSetting** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_DCOMApplicationLaunchAllowedSetting** class has these properties.

<dl> <dt>

**Element**
</dt> <dd> <dl> <dt>

Data type: **Win32\_DCOMApplication**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Element"), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) (" Microsoft CIM Win32\|Win32\_DCOMApplication\|AppID")
</dt> </dl>

Reference to the [**Win32\_DCOMApplication**](win32-dcomapplicationaccessallowedsetting.md) instance representing a DCOM application.

</dd> <dt>

**Setting**
</dt> <dd> <dl> <dt>

Data type: **Win32\_SID**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Setting"), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) (" Microsoft CIM Win32\|Win32\_SID\|SID")
</dt> </dl>

Reference to the [**Win32\_SID**](win32-sid.md) instance representing the role of a user that can access a component grouped under the associated [**Win32\_DCOMApplication**](https://msdn.microsoft.com/library/aa394115) instance.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Secrcw32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/aa392727)
</dt> </dl>

 

 




