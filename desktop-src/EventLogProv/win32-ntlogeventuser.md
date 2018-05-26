---
Description: The Win32\_NTLogEventUser association WMI class relates a Windows event with the currently logged-on user.
ms.assetid: 48134c3e-27fa-4007-ad25-2a86b6ade577
title: Win32\_NTLogEventUser class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Win32\_NTLogEventUser class

The **Win32\_NTLogEventUser** association [WMI class](https://msdn.microsoft.com/library/aa393244) relates a Windows event with the currently logged-on user.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
class Win32_NTLogEventUser
{
  Win32_NTLogEvent  REF Record;
  Win32_UserAccount REF User;
};
```

## Members

The **Win32\_NTLogEventUser** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_NTLogEventUser** class has these properties.

<dl> <dt>

**Record**
</dt> <dd> <dl> <dt>

Data type: **Win32\_NTLogEvent**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

Reference to the instance representing the event being associated with the user.

</dd> <dt>

**User**
</dt> <dd> <dl> <dt>

Data type: **Win32\_UserAccount**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

Reference to the instance representing the user associated with this event.

</dd> </dl>

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                       |
| Namespace<br/>                | Root\\CIMV2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>Ntevt.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Ntevt.dll</dt> </dl> |



## See also

<dl> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/aa392727)
</dt> </dl>

 

 




