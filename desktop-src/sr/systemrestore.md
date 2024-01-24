---
title: SystemRestore class
description: Provides methods for disabling and enabling monitoring, listing available restore points, and initiating a restore on the local system.
ms.assetid: '87216a56-6d40-44ea-a1ab-d43590b639a4'
keywords:
- SystemRestore class System Restore
- SystemRestore class System Restore , described
topic_type:
- apiref
api_name:
- SystemRestore
- SystemRestore.Description
- SystemRestore.RestorePointType
- SystemRestore.EventType
- SystemRestore.SequenceNumber
- SystemRestore.CreationTime
api_location:
- Root\Default
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# SystemRestore class

Provides methods for disabling and enabling monitoring, listing available restore points, and initiating a restore on the local system.

## Syntax

``` syntax
class SystemRestore
{
  String Description;
  uint32 RestorePointType;
  uint32 EventType;
  uint32 SequenceNumber;
  String CreationTime;
};
```

## Members

The **SystemRestore** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **SystemRestore** class has these methods.



| Method                                                             | Description                                                 |
|:-------------------------------------------------------------------|:------------------------------------------------------------|
| [**CreateRestorePoint**](createrestorepoint-systemrestore.md)     | Creates a restore point.<br/>                         |
| [**Disable**](disable-systemrestore.md)                           | Disables monitoring on a particular drive.<br/>       |
| [**Enable**](enable-systemrestore.md)                             | Enables monitoring on a particular drive.<br/>        |
| [**GetLastRestoreStatus**](getlastrestorestatus-systemrestore.md) | Retrieves the status of the last system restore.<br/> |
| [**Restore**](restore-systemrestore.md)                           | Initiates a system restore.<br/>                      |



 

### Properties

The **SystemRestore** class has these properties.

<dl> <dt>

**CreationTime**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The time at which the state change occurred.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The description to be displayed so the user can easily identify a restore point. The maximum length of an ANSI string is MAX\_DESC. The maximum length of a Unicode string is MAX\_DESC\_W. For more information, see [Restore Point Description Text](restore-point-description-text.md).

</dd> <dt>

**EventType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The type of event. This member can be one of the following values.



| Value                                                                                                                                                                                                                                                           | Meaning                                                                                                                                                                                         |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="BEGIN_NESTED_SYSTEM_CHANGE"></span><span id="begin_nested_system_change"></span><dl> <dt>**BEGIN\_NESTED\_SYSTEM\_CHANGE**</dt> <dt>102</dt> </dl> | A system change has begun. A subsequent nested call does not create a new restore point. <br/> Subsequent calls must use END\_NESTED\_SYSTEM\_CHANGE, not END\_SYSTEM\_CHANGE.<br/> |
| <span id="BEGIN_SYSTEM_CHANGE"></span><span id="begin_system_change"></span><dl> <dt>**BEGIN\_SYSTEM\_CHANGE**</dt> <dt>100</dt> </dl>                       | A system change has begun.<br/>                                                                                                                                                           |
| <span id="END_NESTED_SYSTEM_CHANGE"></span><span id="end_nested_system_change"></span><dl> <dt>**END\_NESTED\_SYSTEM\_CHANGE**</dt> <dt>103</dt> </dl>       | A system change has ended.<br/>                                                                                                                                                           |
| <span id="END_SYSTEM_CHANGE"></span><span id="end_system_change"></span><dl> <dt>**END\_SYSTEM\_CHANGE**</dt> <dt>101</dt> </dl>                             | A system change has ended.<br/>                                                                                                                                                           |



 

</dd> <dt>

**RestorePointType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The type of restore point. This member can be one of the following values.



| Value                                                                                                                                                                                                                                          | Meaning                                                                                                                                                       |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="APPLICATION_INSTALL"></span><span id="application_install"></span><dl> <dt>**APPLICATION\_INSTALL**</dt> <dt>0</dt> </dl>         | An application has been installed.<br/>                                                                                                                 |
| <span id="APPLICATION_UNINSTALL"></span><span id="application_uninstall"></span><dl> <dt>**APPLICATION\_UNINSTALL**</dt> <dt>1</dt> </dl>   | An application has been uninstalled.<br/>                                                                                                               |
| <span id="CANCELLED_OPERATION"></span><span id="cancelled_operation"></span><dl> <dt>**CANCELLED\_OPERATION**</dt> <dt>13</dt> </dl>        | An application needs to delete the restore point it created. For example, an application would use this flag when a user cancels an installation. <br/> |
| <span id="DEVICE_DRIVER_INSTALL"></span><span id="device_driver_install"></span><dl> <dt>**DEVICE\_DRIVER\_INSTALL**</dt> <dt>10</dt> </dl> | A device driver has been installed.<br/>                                                                                                                |
| <span id="MODIFY_SETTINGS"></span><span id="modify_settings"></span><dl> <dt>**MODIFY\_SETTINGS**</dt> <dt>12</dt> </dl>                    | An application has had features added or removed.<br/>                                                                                                  |



 

</dd> <dt>

**SequenceNumber**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

The sequence number of the restore point.

</dd> </dl>

## Remarks

You can obtain a list of restore points by using the [**SWbemServices.InstancesOf**](/windows/desktop/WmiSdk/swbemservices-instancesof) method to retrieve a collection of **SystemRestore** objects. You can use the class properties to identify the restore point.

## Examples

The following sample script enumerates the current restore points.


```VB
'SystemRestore Class
'Provides methods for disabling and enabling monitoring, 
'listing available restore points, and initiating a 
'restore on the local system.

Set RPSet = GetObject("winmgmts:root/default").InstancesOf ("SystemRestore")
for each RP in RPSet
    wscript.Echo "Dir: RP" & RP.SequenceNumber & ", Name: " & RP.Description & ", Type: ", RP.RestorePointType & ", Time: " & RP.CreationTime
next
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | None supported<br/>                                                         |
| Namespace<br/>                | Root\\Default<br/>                                                          |
| MOF<br/>                      | <dl> <dt>Sr.mof</dt> </dl> |



## See also

<dl> <dt>

[Windows Management Instrumentation](/windows/desktop/WmiSdk/wmi-start-page)
</dt> </dl>

 

