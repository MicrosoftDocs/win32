---
title: Window Station Security and Access Rights
description: Security enables you to control access to window station objects. For more information about security, see Access-Control Model.
ms.assetid: b132da61-26b7-4457-9433-4894ca0e640a
ms.topic: article
ms.date: 05/31/2018
---

# Window Station Security and Access Rights

Security enables you to control access to window station objects. For more information about security, see [Access-Control Model](/windows/desktop/SecAuthZ/access-control-model).

You can specify a [security descriptor](/windows/desktop/SecAuthZ/security-descriptors) for a window station object when you call the [**CreateWindowStation**](/windows/win32/api/winuser/nf-winuser-createwindowstationa) function. If you specify NULL, the window station gets a default security descriptor. The ACLs in the default security descriptor for a window station come from the primary or impersonation token of the creator.

To get or set the security descriptor of a window station object, call the [**GetSecurityInfo**](/windows/desktop/api/aclapi/nf-aclapi-getsecurityinfo) and [**SetSecurityInfo**](/windows/desktop/api/aclapi/nf-aclapi-setsecurityinfo) functions.

When you call the [**OpenWindowStation**](/windows/win32/api/winuser/nf-winuser-openwindowstationa) function, the system checks the requested access rights against the object's security descriptor.

The valid access rights for window station objects include the [standard access rights](/windows/desktop/SecAuthZ/standard-access-rights) and some object-specific access rights. The following table lists the standard access rights used by all objects.

| Value                       | Meaning                                                                                                                                                                                                                                                                              |
|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DELETE (0x00010000L)        | Required to delete the object.                                                                                                                                                                                                                                                       |
| READ\_CONTROL (0x00020000L) | Required to read information in the security descriptor for the object, not including the information in the SACL. To read or write the SACL, you must request the ACCESS\_SYSTEM\_SECURITY access right. For more information, see [SACL Access Right](/windows/desktop/SecAuthZ/sacl-access-right). |
| SYNCHRONIZE (0x00100000L)   | Not supported for window station objects.                                                                                                                                                                                                                                            |
| WRITE\_DAC (0x00040000L)    | Required to modify the DACL in the security descriptor for the object.                                                                                                                                                                                                               |
| WRITE\_OWNER (0x00080000L)  | Required to change the owner in the security descriptor for the object.                                                                                                                                                                                                              |



 

The following table lists the object-specific access rights.



| Access right                        | Description                                                                                                                                                                                                                                                                   |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WINSTA\_ALL\_ACCESS (0x37F)         | All possible access rights for the window station.                                                                                                                                                                                                                            |
| WINSTA\_ACCESSCLIPBOARD (0x0004L)   | Required to use the clipboard.                                                                                                                                                                                                                                                |
| WINSTA\_ACCESSGLOBALATOMS (0x0020L) | Required to manipulate global atoms.                                                                                                                                                                                                                                          |
| WINSTA\_CREATEDESKTOP (0x0008L)     | Required to create new desktop objects on the window station.                                                                                                                                                                                                                 |
| WINSTA\_ENUMDESKTOPS (0x0001L)      | Required to enumerate existing desktop objects.                                                                                                                                                                                                                               |
| WINSTA\_ENUMERATE (0x0100L)         | Required for the window station to be enumerated.                                                                                                                                                                                                                             |
| WINSTA\_EXITWINDOWS (0x0040L)       | Required to successfully call the [**ExitWindows**](/windows/desktop/api/winuser/nf-winuser-exitwindows) or [**ExitWindowsEx**](/windows/desktop/api/winuser/nf-winuser-exitwindowsex) function. Window stations can be shared by users and this access type can prevent other users of a window station from logging off the window station owner. |
| WINSTA\_READATTRIBUTES (0x0002L)    | Required to read the attributes of a window station object. This attribute includes color settings and other global window station properties.                                                                                                                                |
| WINSTA\_READSCREEN (0x0200L)        | Required to access screen contents.                                                                                                                                                                                                                                           |
| WINSTA\_WRITEATTRIBUTES (0x0010L)   | Required to modify the attributes of a window station object. The attributes include color settings and other global window station properties.                                                                                                                               |



 

The following are the [generic access rights](/windows/desktop/SecAuthZ/generic-access-rights) for the interactive window station object, which is the window station assigned to the logon session of the interactive user.



<table>
<thead>
<tr class="header">
<th>Access right</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>GENERIC_READ</td>
<td><dl> STANDARD_RIGHTS_READ<br />
WINSTA_ENUMDESKTOPS<br />
WINSTA_ENUMERATE<br />
WINSTA_READATTRIBUTES<br />
WINSTA_READSCREEN<br />
</dl></td>
</tr>
<tr class="even">
<td>GENERIC_WRITE</td>
<td><dl> STANDARD_RIGHTS_WRITE<br />
WINSTA_ACCESSCLIPBOARD<br />
WINSTA_CREATEDESKTOP<br />
WINSTA_WRITEATTRIBUTES<br />
</dl></td>
</tr>
<tr class="odd">
<td>GENERIC_EXECUTE</td>
<td><dl> STANDARD_RIGHTS_EXECUTE<br />
WINSTA_ACCESSGLOBALATOMS<br />
WINSTA_EXITWINDOWS<br />
</dl></td>
</tr>
<tr class="even">
<td>GENERIC_ALL</td>
<td><dl> STANDARD_RIGHTS_REQUIRED<br />
WINSTA_ACCESSCLIPBOARD<br />
WINSTA_ACCESSGLOBALATOMS<br />
WINSTA_CREATEDESKTOP<br />
WINSTA_ENUMDESKTOPS<br />
WINSTA_ENUMERATE<br />
WINSTA_EXITWINDOWS<br />
WINSTA_READATTRIBUTES<br />
WINSTA_READSCREEN<br />
WINSTA_WRITEATTRIBUTES<br />
</dl></td>
</tr>
</tbody>
</table>



 

The following are the [generic access rights](/windows/desktop/SecAuthZ/generic-access-rights) for a noninteractive window station object. The system assigns noninteractive window stations to all logon sessions other than that of the interactive user.



<table>
<thead>
<tr class="header">
<th>Access right</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>GENERIC_READ</td>
<td><dl> STANDARD_RIGHTS_READ<br />
WINSTA_ENUMDESKTOPS<br />
WINSTA_ENUMERATE<br />
WINSTA_READATTRIBUTES<br />
</dl></td>
</tr>
<tr class="even">
<td>GENERIC_WRITE</td>
<td><dl> STANDARD_RIGHTS_WRITE<br />
WINSTA_ACCESSCLIPBOARD<br />
WINSTA_CREATEDESKTOP<br />
</dl></td>
</tr>
<tr class="odd">
<td>GENERIC_EXECUTE</td>
<td><dl> STANDARD_RIGHTS_EXECUTE<br />
WINSTA_ACCESSGLOBALATOMS<br />
WINSTA_EXITWINDOWS<br />
</dl></td>
</tr>
<tr class="even">
<td>GENERIC_ALL</td>
<td><dl> STANDARD_RIGHTS_REQUIRED<br />
WINSTA_ACCESSCLIPBOARD<br />
WINSTA_ACCESSGLOBALATOMS<br />
WINSTA_CREATEDESKTOP<br />
WINSTA_ENUMDESKTOPS<br />
WINSTA_ENUMERATE<br />
WINSTA_EXITWINDOWS<br />
WINSTA_READATTRIBUTES<br />
</dl></td>
</tr>
</tbody>
</table>



 

You can request the ACCESS\_SYSTEM\_SECURITY access right to a window station object if you want to read or write the object's SACL. For more information, see [Access-Control Lists (ACLs)](/windows/desktop/SecAuthZ/access-control-lists) and [SACL Access Right](/windows/desktop/SecAuthZ/sacl-access-right).

 

 