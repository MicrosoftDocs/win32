---
title: IVMSecurity interface
description: The IVMSecurity interface manipulates the access rights of an object in Virtual Server.
ms.assetid: '0c0f6836-fcff-424a-ac81-2df2bbe068a9'
keywords: ["IVMSecurity interface Virtual Server", "IVMSecurity interface Virtual Server , described"]
topic_type:
- apiref
api_name:
- IVMSecurity
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMSecurity interface

The **IVMSecurity** interface manipulates the access rights of an object in Virtual Server.

## Members

The **IVMSecurity** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IVMSecurity** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IVMSecurity** interface has these methods.



| Method                                                              | Description                                                                                                                           |
|:--------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------|
| [**\_ToSecurityDescriptor**](ivmsecurity--tosecuritydescriptor.md) | Creates a self-relative **SECURITY\_DESCRIPTOR** structure representing the current state of the **IVMSecurity** instance.<br/> |
| [**AddEntry**](ivmsecurity-addentry.md)                            | Adds a new access control entry.<br/>                                                                                           |
| [**FindEntry**](ivmsecurity-findentry.md)                          | Finds an existing access control entry.<br/>                                                                                    |
| [**RemoveEntry**](ivmsecurity-removeentry.md)                      | Removes an access control entry.<br/>                                                                                           |



 

### Properties

The **IVMSecurity** interface has these properties.



| Property                                                                          | Access type           | Description                                                                    |
|:----------------------------------------------------------------------------------|:----------------------|:-------------------------------------------------------------------------------|
| [**AccessRights**](ivmsecurity-accessrights.md)<br/>                       | Read-only<br/>  | Contains a representation of the discretionary access control list.<br/> |
| [**CurrentUserAccessRights**](ivmsecurity-currentuseraccessrights.md)<br/> | Read-only<br/>  | The access rights for the caller of the COM interface.<br/>              |
| [**GroupName**](ivmsecurity-groupname.md)<br/>                             | Read/write<br/> | The account name of the group.<br/>                                      |
| [**GroupSid**](ivmsecurity-groupsid.md)<br/>                               | Read/write<br/> | The SID string of the group.<br/>                                        |
| [**OwnerName**](ivmsecurity-ownername.md)<br/>                             | Read/write<br/> | The account name of the owner.<br/>                                      |
| [**OwnerSid**](ivmsecurity-ownersid.md)<br/>                               | Read/write<br/> | The SID string of the owner.<br/>                                        |



 

## Examples

The following example shows how to create and use an **IVMSecurity** object from VBScript:


```VB
Dim vsApp
    Set vsApp = WScript.CreateObject("VirtualServer.Application")

    Dim vsSecurity
    Set vsSecurity = WScript.CreateObject("VirtualServer.VMSecurity")

    Rem By default, the newly created VMSecurity object will have
    Rem the service account as the owner. Since this is normally 
    Rem the NetworkService account, we'll need to change the owner.

    vsSecurity.OwnerName = "Administrators"

    Rem Allow users to view and start virtual machines, but only
    Rem computer Administrators can configure them.

    Dim ace
    Set ace = vsSecurity.AddEntry("Administrators",vmAccessRights_Allowed)
    ace.WriteAccess = True
    ace.ReadAccess = True
    ace.ExecuteAccess = True
    ace.DeleteAccess = True
    ace.ReadPermissions = True
    ace.ChangePermissions = True

    Set ace = vsSecurity.AddEntry("Everyone",vmAccessRights_Allowed)
    ace.ReadAccess = True
    ace.ExecuteAccess = True
    ace.ReadPermissions = True

    Rem The service account also needs access.

    Set ace = vsSecurity.AddEntry("NT AUTHORITY\NetworkService",vmAccessRightsAllowed)
    ace.WriteAccess = True
    ace.ReadAccess = True
    ace.ExecuteAccess = True
    ace.DeleteAccess = True
    ace.ReadPermissions = True
    ace.ChangePermissions = True

    vsApp.Security = vsSecurity
```



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5)
</dt> </dl>

 

 





