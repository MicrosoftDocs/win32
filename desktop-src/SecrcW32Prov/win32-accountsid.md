---
Description: The Win32\_AccountSID association WMI class relates a security account instance with a security descriptor instance.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a0d65893-49c8-4764-be07-e95c490a237c
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: Win32\_AccountSID class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_AccountSID class

The **Win32\_AccountSID** association [WMI class](https://msdn.microsoft.com/library/aa393244) relates a security account instance with a security descriptor instance.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("SECRCW32"), Association, UUID("{8502C582-5FBB-11D2-AAC1-006008C78BC7}"), AMENDMENT]
class Win32_AccountSID
{
  Win32_Account REF Element;
  Win32_SID     REF Setting;
};
```

## Members

The **Win32\_AccountSID** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_AccountSID** class has these properties.

<dl> <dt>

**Element**
</dt> <dd> <dl> <dt>

Data type: **Win32\_Account**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Reference to the instance representing the security account. This property value cannot be **NULL**.

</dd> <dt>

**Setting**
</dt> <dd> <dl> <dt>

Data type: **Win32\_SID**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Reference to the instance representing the security descriptor. This property value cannot be **NULL**.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Secrcw32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/aa392727)
</dt> </dl>

 

 




