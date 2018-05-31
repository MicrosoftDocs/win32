---
title: IVMAccessRightsCollection interface
description: The IVMAccessRightsCollection interface defines the collection of access control entries. An IVMAccessRightsCollection object is returned from the IVMSecurity AccessRights property.
ms.assetid: f0620118-bb6d-4e69-a785-1a79223ff2d5
keywords:
- IVMAccessRightsCollection interface Virtual Server
- IVMAccessRightsCollection interface Virtual Server , described
topic_type:
- apiref
api_name:
- IVMAccessRightsCollection
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IVMAccessRightsCollection interface

The **IVMAccessRightsCollection** interface defines the collection of access control entries. An **IVMAccessRightsCollection** object is returned from the [**IVMSecurity::AccessRights**](ivmsecurity-accessrights.md) property.

## Members

The **IVMAccessRightsCollection** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IVMAccessRightsCollection** also has these types of members:

-   [Properties](#properties)

### Properties

The **IVMAccessRightsCollection** interface has these properties.



| Property                                                           | Access type          | Description                                                                                                              |
|:-------------------------------------------------------------------|:---------------------|:-------------------------------------------------------------------------------------------------------------------------|
| [**\_NewEnum**](ivmaccessrightscollection--newenum.md)<br/> | Read-only<br/> | The collection enumerator for this collection.<br/>                                                                |
| [**Count**](ivmaccessrightscollection-count.md)<br/>        | Read-only<br/> | The number of access control entries contained in this collection.<br/>                                            |
| [**Item**](ivmaccessrightscollection-item.md)<br/>          | Read-only<br/> | The [**IVMAccessRights**](ivmaccessrights.md) object that corresponds to the given index in this collection.<br/> |



 

## Remarks

The **IVMAccessRightsCollection** is a representation of an [**IVMSecurity**](ivmsecurity.md) object's Discretionary Access Control List and is used to enumerate the individual [**IVMAccessRights**](ivmaccessrights.md) objects representing the individual Access Control Entries in the DACL. These access rights apply to the Virtual Server object which contains the corresponding **IVMSecurity** object; not to any resources exposed by the guest operating system running inside a virtual machine.

## Examples

The following example prints the access right properties of the access control entries from the security object protecting access to a specific virtual machine object.


```VB
Dim vsApp
Dim vsVirtualMachine
Dim vsSecurity
Dim vsAccessRightsCollection
Dim vsAccessRights

Set vsApp = WScript.CreateObject("VirtualServer.Application")
Set vsVirtualMachine = vsApp.FindVirtualMachine("Windows Server 2003")
Set vsSecurity = vsVirtualMachine.Security
Set vsAccessRightsCollection = vsSecurity.AccessRights

For Each vsAccessRights In vsAccessRightsCollection
    Wscript.Echo "Name: " & vsAccessRights.Name
    Wscript.Echo "Change permissions: " & vsAccessRights.ChangePermissions
    Wscript.Echo "Delete access: " & vsAccessRights.DeleteAccess
    Wscript.Echo "Execute access: " & vsAccessRights.ExecuteAccess
    Wscript.Echo "Flags: " & vsAccessRights.Flags
    Wscript.Echo "Read access: " & vsAccessRights.ReadAccess
    Wscript.Echo "Read permissions: " & vsAccessRights.ReadPermissions
    Wscript.Echo "SID: " & vsAccessRights.SID
    Wscript.Echo "Special access: " & vsAccessRights.SpecialAccess
    Wscript.Echo "Type: " & vsAccessRights.Type
    Wscript.Echo "Write access: " & vsAccessRights.WriteAccess
    Wscript.Echo
Next
```



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



 

 





