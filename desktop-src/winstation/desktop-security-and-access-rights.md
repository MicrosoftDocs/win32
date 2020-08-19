---
title: Desktop Security and Access Rights
description: Security enables you to control access to desktop objects. For more information about security, see Access-Control Model.
ms.assetid: 6512d128-3b0c-4ba7-8709-2fd225389a40
ms.topic: article
ms.date: 05/31/2018
---

# Desktop Security and Access Rights

Security enables you to control access to desktop objects. For more information about security, see [Access-Control Model](/windows/desktop/SecAuthZ/access-control-model).

You can specify a [security descriptor](/windows/desktop/SecAuthZ/security-descriptors) for a desktop object when you call the [**CreateDesktop**](/windows/win32/api/winuser/nf-winuser-createdesktopa) or [**CreateDesktopEx**](/windows/win32/api/winuser/nf-winuser-createdesktopexa) function. If you specify NULL, the desktop gets a default security descriptor. The ACLs in the default security descriptor for a desktop come from its parent window station.

To get or set the security descriptor of a window station object, call the [**GetSecurityInfo**](/windows/desktop/api/aclapi/nf-aclapi-getsecurityinfo) and [**SetSecurityInfo**](/windows/desktop/api/aclapi/nf-aclapi-setsecurityinfo) functions.

When you call the [**OpenDesktop**](/windows/win32/api/winuser/nf-winuser-opendesktopa) or [**OpenInputDesktop**](/windows/win32/api/winuser/nf-winuser-openinputdesktop) function, the system checks the requested access rights against the object's security descriptor.

The valid access rights for desktop objects include the [standard access rights](/windows/desktop/SecAuthZ/standard-access-rights) and some object-specific access rights. The following table lists the standard access rights used by all objects.

| Value                       | Meaning                                                                                                                                                                                                                                                                              |
|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DELETE (0x00010000L)        | Required to delete the object.                                                                                                                                                                                                                                                       |
| READ\_CONTROL (0x00020000L) | Required to read information in the security descriptor for the object, not including the information in the SACL. To read or write the SACL, you must request the ACCESS\_SYSTEM\_SECURITY access right. For more information, see [SACL Access Right](/windows/desktop/SecAuthZ/sacl-access-right). |
| SYNCHRONIZE (0x00100000L)   | Not supported for desktop objects.                                                                                                                                                                                                                                                   |
| WRITE\_DAC (0x00040000L)    | Required to modify the DACL in the security descriptor for the object.                                                                                                                                                                                                               |
| WRITE\_OWNER (0x00080000L)  | Required to change the owner in the security descriptor for the object.                                                                                                                                                                                                              |



 

The following table lists the object-specific access rights.



| Access right                       | Description                                                                                 |
|------------------------------------|---------------------------------------------------------------------------------------------|
| DESKTOP\_CREATEMENU (0x0004L)      | Required to create a menu on the desktop.                                                   |
| DESKTOP\_CREATEWINDOW (0x0002L)    | Required to create a window on the desktop.                                                 |
| DESKTOP\_ENUMERATE (0x0040L)       | Required for the desktop to be enumerated.                                                  |
| DESKTOP\_HOOKCONTROL (0x0008L)     | Required to establish any of the window hooks.                                              |
| DESKTOP\_JOURNALPLAYBACK (0x0020L) | Required to perform journal playback on a desktop.                                          |
| DESKTOP\_JOURNALRECORD (0x0010L)   | Required to perform journal recording on a desktop.                                         |
| DESKTOP\_READOBJECTS (0x0001L)     | Required to read objects on the desktop.                                                    |
| DESKTOP\_SWITCHDESKTOP (0x0100L)   | Required to activate the desktop using the [**SwitchDesktop**](/windows/win32/api/winuser/nf-winuser-switchdesktop) function. |
| DESKTOP\_WRITEOBJECTS (0x0080L)    | Required to write objects on the desktop.                                                   |



 

The following are the [generic access rights](/windows/desktop/SecAuthZ/generic-access-rights) for a desktop object contained in the interactive window station of the user's logon session.



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
<td><dl> DESKTOP_ENUMERATE<br />
DESKTOP_READOBJECTS<br />
STANDARD_RIGHTS_READ<br />
</dl></td>
</tr>
<tr class="even">
<td>GENERIC_WRITE</td>
<td><dl> DESKTOP_CREATEMENU<br />
DESKTOP_CREATEWINDOW<br />
DESKTOP_HOOKCONTROL<br />
DESKTOP_JOURNALPLAYBACK<br />
DESKTOP_JOURNALRECORD<br />
DESKTOP_WRITEOBJECTS<br />
STANDARD_RIGHTS_WRITE<br />
</dl></td>
</tr>
<tr class="odd">
<td>GENERIC_EXECUTE</td>
<td><dl> DESKTOP_SWITCHDESKTOP<br />
STANDARD_RIGHTS_EXECUTE<br />
</dl></td>
</tr>
<tr class="even">
<td>GENERIC_ALL</td>
<td><dl> DESKTOP_CREATEMENU<br />
DESKTOP_CREATEWINDOW<br />
DESKTOP_ENUMERATE<br />
DESKTOP_HOOKCONTROL<br />
DESKTOP_JOURNALPLAYBACK<br />
DESKTOP_JOURNALRECORD<br />
DESKTOP_READOBJECTS<br />
DESKTOP_SWITCHDESKTOP<br />
DESKTOP_WRITEOBJECTS<br />
STANDARD_RIGHTS_REQUIRED<br />
</dl></td>
</tr>
</tbody>
</table>



 

You can request the ACCESS\_SYSTEM\_SECURITY access right to a desktop object if you want to read or write the object's SACL. For more information, see [Access-Control Lists (ACLs)](/windows/desktop/SecAuthZ/access-control-lists) and [SACL Access Right](/windows/desktop/SecAuthZ/sacl-access-right).

 

 