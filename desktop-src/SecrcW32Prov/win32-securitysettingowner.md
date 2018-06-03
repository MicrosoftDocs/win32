---
Description: The Win32\_SecuritySettingOwner abstract association WMI class relates the security settings of an object and its owner.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 22291634-8d1f-43bb-91cd-3ac89b03be32
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: Win32\_SecuritySettingOwner class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_SecuritySettingOwner class

The **Win32\_SecuritySettingOwner** abstract association [WMI class](https://msdn.microsoft.com/library/aa393244) relates the security settings of an object and its owner.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[abstract, Association, UUID("{8502C585-5FBB-11D2-AAC1-006008C78BC7}"), AMENDMENT]
class Win32_SecuritySettingOwner
{
  Win32_SID             REF Owner;
  Win32_SecuritySetting REF SecuritySetting;
};
```

## Members

The **Win32\_SecuritySettingOwner** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_SecuritySettingOwner** class has these properties.

<dl> <dt>

**Owner**
</dt> <dd> <dl> <dt>

Data type: **Win32\_SID**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Reference to the instance representing the object's owner.

</dd> <dt>

**SecuritySetting**
</dt> <dd> <dl> <dt>

Data type: **Win32\_SecuritySetting**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Reference to the instance representing the security settings of an object.

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

 

 




