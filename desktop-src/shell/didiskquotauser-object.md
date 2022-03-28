---
description: Allows a client to manage an NTFS volume's global disk quota settings. This object makes the essential functionality of the DIDiskQuotaUser interface available to scripting and Microsoft Visual Basic-based applications.
title: DIDiskQuotaUser object
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DIDiskQuotaUser
api_type: 
- COM
api_location: 
- Shell32.dll
ms.assetid: 0cdf3293-3dcf-44e7-a80d-4eacf9d09fbf

---

# DIDiskQuotaUser object

Allows a client to manage an NTFS volume's global disk quota settings. This object makes the essential functionality of the **DIDiskQuotaUser** interface available to scripting and Microsoft Visual Basic-based applications.

## Members

The **DIDiskQuotaUser** object has these types of members:

- [Methods](#methods)
- [Properties](#properties)

### Methods

The **DIDiskQuotaUser** object has these methods.



| Method                                           | Description                                             |
|:-------------------------------------------------|:--------------------------------------------------------|
| [**Invalidate**](didiskquotauser-invalidate.md) | Clears the object's cached user information.<br/> |



 

### Properties

The **DIDiskQuotaUser** object has these properties.



| Property                                                                        | Access type           | Description                                                                                          |
|:--------------------------------------------------------------------------------|:----------------------|:-----------------------------------------------------------------------------------------------------|
| [**AccountContainerName**](didiskquotauser-accountcontainername.md)<br/> | Read-only<br/>  | Gets the name of the user's account container.<br/>                                            |
| [**AccountStatus**](didiskquotauser-accountstatus.md)<br/>               | Read-only<br/>  | Gets the status of the user's account.<br/>                                                    |
| [**DisplayName**](didiskquotauser-displayname.md)<br/>                   | Read-only<br/>  | Gets the user's display name.<br/>                                                             |
| [**ID**](didiskquotauser-id.md)<br/>                                     | Read-only<br/>  | Gets an ID that uniquely identifies the user.<br/>                                             |
| [**LogonName**](didiskquotauser-logonname.md)<br/>                       | Read-only<br/>  | Gets the user's logon account name.<br/>                                                       |
| [**QuotaLimit**](didiskquotauser-quotalimit.md)<br/>                     | Read/write<br/> | Sets or gets the user's current [**quota limit**](diskquotacontrol-object.md).<br/>           |
| [**QuotaLimitText**](didiskquotauser-quotalimittext.md)<br/>             | Read-only<br/>  | Gets the user's current [**quota limit**](diskquotacontrol-object.md) as a text string. <br/> |
| [**QuotaThreshold**](didiskquotauser-quotathreshold.md)<br/>             | Read/write<br/> | Sets or gets the user's warning threshold, in bytes.<br/>                                      |
| [**QuotaThresholdText**](didiskquotauser-quotathresholdtext.md)<br/>     | Read-only<br/>  | Gets the user's warning threshold as a text string.<br/>                                       |
| [**QuotaUsed**](didiskquotauser-quotaused.md)<br/>                       | Read-only<br/>  | Gets the user's current disk usage, in bytes.<br/>                                             |
| [**QuotaUsedText**](didiskquotauser-quotausedtext.md)<br/>               | Read-only<br/>  | Gets the user's current disk usage as a text string.<br/>                                      |



 

## Remarks

Each user on the volume that is managed by the [**DiskQuotaControl**](diskquotacontrol-object.md) object has a **DIDiskQuotaUser** object associated with it. This object allows a client to manage an individual user's settings. There are several ways to obtain a user's **DIDiskQuotaUser** object:

-   The **DIDiskQuotaUser** objects for all users with quotas on the volume are exposed as a collection and can be enumerated. A discussion of how to enumerate **DIDiskQuotaUser** objects is found below.
-   When you add a new user, the [**AddUser**](diskquotacontrol-adduser.md) method returns the user's **DIDiskQuotaUser** object.
-   If you have the user's name, the [**FindUser**](diskquotacontrol-finduser.md) method returns the user's **DIDiskQuotaUser** object.

### Enumerating Disk Quota Users

The **DIDiskQuotaUser** objects for all users with a quota on the volume are exposed as a collection. The [**DiskQuotaControl**](diskquotacontrol-object.md) object exports a standard enumerator method that allows you to enumerate the collection of **DIDiskQuotaUser** objects. The following procedure illustrates how to perform the enumeration with Microsoft JScript (compatible with ECMA 262 language specification). You can use a similar procedure with Visual Basic or Microsoft Visual Basic Scripting Edition (VBScript).

1.  Create a new [**DiskQuotaControl**](diskquotacontrol-object.md) object.
2.  Initialize it with [**Initialize**](diskquotacontrol-initialize.md).
3.  Create a new JScript **Enumerator** object.
4.  Use a **for** loop to enumerate the **DIDiskQuotaUser** objects. There is no need to set a starting value. The enumerator object's **moveNext** method notifies the **item** method to return the next **DIDiskQuotaUser** object. The **atEnd** method returns **false** when you reach the end of the list.
5.  As needed, use the **DIDiskQuotaUser** object returned by the enumerator's **item** method to retrieve or set one or more of the associated user's disk quota properties.

The following code fragment illustrates how to enumerate **DIDiskQuotaUser** objects with JScript. The **Volume\_Label** argument that is passed to the **EnumUsers** function is a string value containing a volume label such as "C:\\\\".


```
function EnumUsers(Volume_Label)
{
    var Volume;
    var QuotaUsers;
    var QuotaUser;

    Volume = new ActiveXObject("Microsoft.DiskQuota.1");
    Volume.Initialize(Volume_Label, 1);

    QuotaUsers = new Enumerator(Volume);
    for (;!Users.atEnd(); Users.moveNext())
    {
       QuotaUser = QuotaUsers.item();

     //Use the QuotaUser object to retrieve or set one or more
     //of the user's disk quota properties
     ...
    }
}
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                          |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 5.0 or later)</dt> </dl> |



## See also

<dl> <dt>

[**Shell Object**](shell.md)
</dt> </dl>

 

 




