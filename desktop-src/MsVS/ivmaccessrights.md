---
title: IVMAccessRights interface
description: Defines the access rights for a particular account or group.
ms.assetid: 299e6ffd-34ba-42c7-a694-69ca7e31fccb
keywords:
- IVMAccessRights interface Virtual Server
- IVMAccessRights interface Virtual Server , described
topic_type:
- apiref
api_name:
- IVMAccessRights
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IVMAccessRights interface

The **IVMAccessRights** interface defines the access rights for a particular account or group.

## Members

The **IVMAccessRights** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IVMAccessRights** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IVMAccessRights** interface has these methods.



| Method                                                    | Description                                          |
|:----------------------------------------------------------|:-----------------------------------------------------|
| [**\_GetAccessMask**](ivmaccessrights--getaccessmask.md) | Retrieves the access rights as a bitmask.<br/> |



 

### Properties

The **IVMAccessRights** interface has these properties.



| Property                                                                  | Access type           | Description                                                                                                              |
|:--------------------------------------------------------------------------|:----------------------|:-------------------------------------------------------------------------------------------------------------------------|
| [**ChangePermissions**](ivmaccessrights-changepermissions.md)<br/> | Read/write<br/> | Indicates whether this entry controls the ability to change permissions.<br/>                                      |
| [**DeleteAccess**](ivmaccessrights-deleteaccess.md)<br/>           | Read/write<br/> | Indicates whether this entry controls delete access.<br/>                                                          |
| [**ExecuteAccess**](ivmaccessrights-executeaccess.md)<br/>         | Read/write<br/> | Indicates whether this entry controls execute access.<br/>                                                         |
| [**Flags**](ivmaccessrights-flags.md)<br/>                         | Read/write<br/> | The access control entry flags.<br/>                                                                               |
| [**Name**](ivmaccessrights-name.md)<br/>                           | Read/write<br/> | The account name of the user or group.<br/>                                                                        |
| [**ReadAccess**](ivmaccessrights-readaccess.md)<br/>               | Read/write<br/> | Indicates whether this entry controls read access.<br/>                                                            |
| [**ReadPermissions**](ivmaccessrights-readpermissions.md)<br/>     | Read/write<br/> | Indicates whether this entry controls the ability to read permissions.<br/>                                        |
| [**Sid**](ivmaccessrights-sid.md)<br/>                             | Read/write<br/> | The SID string of the user or group.<br/>                                                                          |
| [**SpecialAccess**](ivmaccessrights-specialaccess.md)<br/>         | Read/write<br/> | Indicates whether this entry controls permissions not mapped to generic read, write or execute access rights.<br/> |
| [**Type**](ivmaccessrights-type.md)<br/>                           | Read/write<br/> | The type of access control entry.<br/>                                                                             |
| [**WriteAccess**](ivmaccessrights-writeaccess.md)<br/>             | Read/write<br/> | Indicates whether this entry controls write access.<br/>                                                           |



 

## Remarks

The properties [**WriteAccess**](ivmaccessrights-writeaccess.md), [**ReadAccess**](ivmaccessrights-readaccess.md), and [**ExecuteAccess**](ivmaccessrights-executeaccess.md) control generic access rights to the protected object. For example, granting **WriteAccess** to a virtual machine sets the rights represented by the FILE\_GENERIC\_WRITE constant on the virtual machines configuration file. If a set of rights cannot be mapped to a generic access right, the [**SpecialAccess**](ivmaccessrights-specialaccess.md) property will return VARIANT\_TRUE. Although no ability to change the special access rights is provided by this interface, the rights will be preserved in the entry. You retrieve an **IVMAccessRights** instance from the [**IVMAccessRightsCollection**](ivmaccessrightscollection.md) of an [**IVMSecurity**](ivmsecurity.md) instance protecting a given resource.

## Examples

The following example prints the access right properties of the access control entries from the security object protecting access to the COM interfaces and global settings.


```VB
Dim vsApp
Dim vsSecurity
Dim vsAccessRights
Dim arProperty

Set vsApp = WScript.CreateObject("VirtualServer.Application")
Set vsSecurity = vsApp.Security
Set vsAccessRights = vsSecurity.AccessRights

For Each arProperty In vsAccessRights
  Wscript.Echo "Name: " & arProperty.Name
  Wscript.Echo "Change permissions: " & arProperty.ChangePermissions
  Wscript.Echo "Delete access: " & arProperty.DeleteAccess
  Wscript.Echo "Execute access: " & arProperty.ExecuteAccess
  Wscript.Echo "Flags: " & arProperty.Flags
  Wscript.Echo "Read access: " & arProperty.ReadAccess
  Wscript.Echo "Read permissions: " & arProperty.ReadPermissions
  Wscript.Echo "SID: " & arProperty.SID
  Wscript.Echo "Special access: " & arProperty.SpecialAccess
  Wscript.Echo "Type: " & arProperty.Type
  Wscript.Echo "Write access: " & arProperty.WriteAccess
  Wscript.Echo
Next
```



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5)
</dt> <dt>

[Microsoft Virtual Server 2005 Reference](microsoft-virtual-server-reference.md)
</dt> <dt>

[IVMAccessRights Methods](ivmaccessrights-methods.md)
</dt> <dt>

[IVMAccessRights Properties](ivmaccessrights-properties.md)
</dt> </dl>

 

 





