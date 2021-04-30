---
description: Allows an administrator to manage a volume's disk quota properties.
title: DiskQuotaControl object
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DiskQuotaControl
api_type: 
- COM
api_location: 
- Shell32.dll
ms.assetid: 846297f2-b826-45de-8617-228790e87a63
api_name: 
 - DiskQuotaControl
api_type: 
 - COM
api_location: 
 - Shell32.dll
topic_type: 
 - APIRef
 - kbSyntax

---

# DiskQuotaControl object

Allows an administrator to manage a volume's disk quota properties. The NTFS file system allows an administrator to manage disk usage on a shared volume by allocating a specified amount of disk space, or *quota limit*, to each user. You can use this object to set the default quota limit that will be automatically assigned to all new users.

## Members

The **DiskQuotaControl** object has these types of members:

-   [Events](#events)
-   [Methods](#methods)
-   [Properties](#properties)

### Events

The **DiskQuotaControl** object has these events.



| Event                                                           | Description                                                                                                                   |
|:----------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------|
| [**OnUserNameChanged**](diskquotacontrol-onusernamechanged.md) | Occurs when the name information for a [**DIDiskQuotaUser**](didiskquotauser-object.md) object has been resolved.<br/> |



 

### Methods

The **DiskQuotaControl** object has these methods.



| Method                                                                                    | Description                                                                                |
|:------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------|
| [**AddUser**](diskquotacontrol-adduser.md)                                               | Assigns a nondefault disk quota to a new user.<br/>                                  |
| [**DeleteUser**](diskquotacontrol-deleteuser.md)                                         | Deletes a user from the volume.<br/>                                                 |
| [**FindUser**](diskquotacontrol-finduser.md)                                             | Finds a user's entry, by name, in the volume's quota file.<br/>                      |
| [**GiveUserNameResolutionPriority**](diskquotacontrol-giveusernameresolutionpriority.md) | Places the specified user object next in line for name resolution.<br/>              |
| [**Initialize**](diskquotacontrol-initialize.md)                                         | Opens a specified volume and initializes its quota control object.<br/>              |
| [**InvalidateSidNameCache**](diskquotacontrol-invalidatesidnamecache.md)                 | Invalidates the security ID user name cache.<br/>                                    |
| [**ShutdownNameResolution**](diskquotacontrol-shutdownnameresolution.md)                 | Shuts down the user name resolution thread.<br/>                                     |
| [**TranslateLogonNameToSID**](diskquotacontrol-translatelogonnametosid.md)               | Translates a logon name to the corresponding user security ID in string format.<br/> |



 

### Properties

The **DiskQuotaControl** object has these properties.



| Property                                                                                   | Access type           | Description                                                                                                                                                   |
|:-------------------------------------------------------------------------------------------|:----------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DefaultQuotaLimit**](diskquotacontrol-defaultquotalimit.md)<br/>                 | Read/write<br/> | Sets or gets the default quota limit.<br/>                                                                                                              |
| [**DefaultQuotaLimitText**](diskquotacontrol-defaultquotalimittext.md)<br/>         | Read-only<br/>  | Gets the default quota limit as a text string.<br/>                                                                                                     |
| [**DefaultQuotaThreshold**](diskquotacontrol-defaultquotathreshold.md)<br/>         | Read/write<br/> | Sets or gets the default quota threshold.<br/>                                                                                                          |
| [**DefaultQuotaThresholdText**](diskquotacontrol-defaultquotathresholdtext.md)<br/> | Read-only<br/>  | Gets the default quota threshold as a text string.<br/>                                                                                                 |
| [**LogQuotaLimit**](diskquotacontrol-logquotalimit.md)<br/>                         | Read/write<br/> | Sets or gets a Boolean value that indicates whether a system event log entry will be made when a user exceeds his or her assigned quota limit.<br/>     |
| [**LogQuotaThreshold**](diskquotacontrol-logquotathreshold.md)<br/>                 | Read/write<br/> | Sets or gets a Boolean value that indicates whether a system event log entry will be made when a user exceeds his or her assigned quota threshold.<br/> |
| [**QuotaFileIncomplete**](diskquotacontrol-quotafileincomplete.md)<br/>             | Read-only<br/>  | Gets a Boolean value that indicates whether the quota file for the volume is complete.<br/>                                                             |
| [**QuotaFileRebuilding**](diskquotacontrol-quotafilerebuilding.md)<br/>             | Read-only<br/>  | Gets a Boolean value that indicates whether the quota file for the volume is currently being rebuilt.<br/>                                              |
| [**QuotaState**](diskquotacontrol-quotastate.md)<br/>                               | Read/write<br/> | Sets or gets the state of the volume's disk quotas.<br/>                                                                                                |
| [**UserNameResolution**](diskquotacontrol-usernameresolution.md)<br/>               | Read/write<br/> | Sets or gets a value that controls how user SID are resolved to user names.<br/>                                                                        |



 

## Remarks

An administrator can use the **DiskQuotaControl** object to do a number of tasks, including the following:

-   Enabling and disabling the volume's disk quota system.
-   Obtaining the status of the quota system on the volume.
-   Denying disk space to users exceeding their quota limit.
-   Specifying the default warning threshold and quota limit values that will be assigned to new users.
-   Adding and removing users.

The **DiskQuotaControl** object allows you to set global default values for the volume for properties such as quota limits. However, each user is represented by a [**DIDiskQuotaUser**](didiskquotauser-object.md) object that can be used to specify individual quota settings.

There are several ways to obtain a user's [**DIDiskQuotaUser**](didiskquotauser-object.md) object:

-   The [**DIDiskQuotaUser**](didiskquotauser-object.md) objects for all users with quotas on the volume are exposed as a collection, and can be enumerated. For a discussion of how to enumerate **DIDiskQuotaUser** objects, see **Enumerating Disk Quota Users** in the Remarks section of **DIDiskQuotaUser**.
-   When you add a new user, the [**AddUser**](diskquotacontrol-adduser.md) method returns the user's [**DIDiskQuotaUser**](didiskquotauser-object.md) object.
-   If you have the user's name, the [**FindUser**](diskquotacontrol-finduser.md) method returns the user's [**DIDiskQuotaUser**](didiskquotauser-object.md) object.

This object makes the essential functionality of the IDiskQuotaControl interface available to scripting and Microsoft Visual Basic-based applications.

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

 

 




