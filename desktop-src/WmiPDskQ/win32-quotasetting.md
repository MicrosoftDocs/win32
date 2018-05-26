---
title: Win32\_QuotaSetting class
description: The Win32\_QuotaSetting \ 8194;WMI class contains setting information for disk quotas on a volume.The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.
ms.assetid: 7c58adf6-41e6-4e9f-891c-2d5c6e16aecd
keywords:
- Win32_QuotaSetting class
- Win32_QuotaSetting class, described
topic_type:
- apiref
api_name:
- Win32_QuotaSetting
- Win32_QuotaSetting.Caption
- Win32_QuotaSetting.DefaultLimit
- Win32_QuotaSetting.DefaultWarningLimit
- Win32_QuotaSetting.Description
- Win32_QuotaSetting.ExceededNotification
- Win32_QuotaSetting.SettingID
- Win32_QuotaSetting.State
- Win32_QuotaSetting.VolumePath
- Win32_QuotaSetting.WarningExceededNotification
api_location:
- Wmipdskq.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Win32\_QuotaSetting class

The **Win32\_QuotaSetting** [WMI class](https://msdn.microsoft.com/library/aa393244) contains setting information for disk quotas on a volume.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
class Win32_QuotaSetting : CIM_Setting
{
  string  Caption;
  sint64  DefaultLimit;
  sint64  DefaultWarningLimit;
  string  Description;
  boolean ExceededNotification;
  string  SettingID;
  uint32  State;
  string  VolumePath;
  boolean WarningExceededNotification;
};
```

## Members

The **Win32\_QuotaSetting** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_QuotaSetting** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

Short description of the object a one line string. This property is inherited from [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461).

</dd> <dt>

**DefaultLimit**
</dt> <dd> <dl> <dt>

Data type: **sint64**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) (Bytes)
</dt> </dl>

Default limit set for quotas on this specific volume.

**Windows Server 2003 and Windows XP:** Datatype is **uint64**.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> <dt>

**DefaultWarningLimit**
</dt> <dd> <dl> <dt>

Data type: **sint64**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) (Bytes)
</dt> </dl>

Default warning limit set for quotas on this specific volume.

**Windows Server 2003 and Windows XP:** Datatype is **uint64**.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Comment that describes the link. This property is inherited from [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461).

</dd> <dt>

**ExceededNotification**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **TRUE**, events are written to the event log when quotas are exceeded.

</dd> <dt>

**SettingID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

Name of a [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461) object.

</dd> <dt>

**State**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Level of quota management set for this volume.

The values are:



| Values                                                                       | Meaning                                                                                                                      |
|------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>0</dt> </dl> | Disabled<br/> Quota management is not enabled on this volume.<br/>                                               |
| <dl> <dt>1</dt> </dl> | Tracked<br/> Quotas are tracked but the limit value is not enforced and users may exceed their quota limit.<br/> |
| <dl> <dt>2</dt> </dl> | Enforced<br/> Quotas are tracked and enforced on this volume.<br/>                                               |



 

</dd> <dt>

**VolumePath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

Name of the volume where disk quotas are located. It can be volume name, volume path (such as D:\\\), or it can be the unique volume name (such as "\\\\\\\\?Volume{GUID}\\\\.").

</dd> <dt>

**WarningExceededNotification**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **TRUE**, events are written to the event log when warnings are exceeded.

</dd> </dl>

## Remarks

The **Win32\_QuotaSetting** class is derived from [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Wmipdskq.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wmipdskq.dll</dt> </dl> |



## See also

<dl> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/aa392727)
</dt> </dl>

 

 





