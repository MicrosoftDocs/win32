---
title: Access Control Lists for COM
description: Access Control Lists for COM
ms.assetid: ceb37563-7e7f-4704-b671-72ed65e3e102
ms.topic: article
ms.date: 05/31/2018
---

# Access Control Lists for COM

Windows Server XP Service Pack 2 (SP 2) and Windows Server 2003 Service Pack 1 (SP 1) introduce security enhancements for the Distributed Component Object Model (DCOM). One of these enhancements is more specific access rights for use in access control lists (ACLs). The access rights are:

``` syntax
COM_RIGHTS_EXECUTE 1
COM_RIGHTS_EXECUTE_LOCAL 2
COM_RIGHTS_EXECUTE_REMOTE 4
COM_RIGHTS_ACTIVATE_LOCAL 8
COM_RIGHTS_ACTIVATE_REMOTE 16
```

To provide backward compatibility, an ACL may exist in the format used before Windows XP SP 2 and Windows Server 2003 SP 1, which uses only the access right COM\_RIGHTS\_EXECUTE, or it may exist in the new format used in Windows XP SP 2 and Windows Server 2003 SP 1, which uses COM\_RIGHTS\_EXECUTE together with a combination of COM\_RIGHTS\_EXECUTE\_LOCAL, COM\_RIGHTS\_EXECUTE\_REMOTE, COM\_RIGHTS\_ACTIVATE\_LOCAL, and COM\_RIGHTS\_ACTIVATE\_REMOTE.

> [!Note]  
> COM\_RIGHTS\_EXECUTE must always be present; the absence of this right generates an invalid security descriptor.

 

You must not mix the old format and the new format within a single ACL; either all access control entries (ACEs) must grant only the COM\_RIGHTS\_EXECUTE access right, or they all must grant COM\_RIGHTS\_EXECUTE together with a combination of COM\_RIGHTS\_EXECUTE\_LOCAL, COM\_RIGHTS\_EXECUTE\_REMOTE, COM\_RIGHTS\_ACTIVATE\_LOCAL, and COM\_RIGHTS\_ACTIVATE\_REMOTE.

The following is an example of an incorrectly formatted ACL:

``` syntax
Revision 1
Sbz1 0
Control 0x8004
    SE_DACL_PRESENT
    SE_SELF_RELATIVE
Owner: S-1-5-21-1597522630-148096252-1166023319-500 (no name mapped)
Group: S-1-5-21-1597522630-148096252-1166023319-500 (no name mapped)
DACL:
    AclRevision 2
    Sbz1 0
    AclSize 128
    AceCount 4
    Sbz2 0
    Ace[0]
        AceType 0: ACCESS_ALLOWED_ACE_TYPE
        AceFlags 0
        AceSize 36
        AccessMask 0x1
        S-1-5-21-1597522630-148096252-1166023319-500 (no name mapped)
    Ace[1]
        AceType 0: ACCESS_ALLOWED_ACE_TYPE
        AceFlags 0
        AceSize 20
        AccessMask 0xb
        S-1-5-18 (Well Known Group: NT AUTHORITY\SYSTEM)
    Ace[2]
        AceType 0: ACCESS_ALLOWED_ACE_TYPE
        AceFlags 0
        AceSize 20
        AccessMask 0x9
        S-1-5-11 (Well Known Group: NT AUTHORITY\Authenticated Users)
SACL:
    (null)
```

Note that the first access control entry (ACE) grants COM\_RIGHTS\_EXECUTE (0x1) only, while the second ACE grants COM\_RIGHTS\_EXECUTE, COM\_RIGHTS\_EXECUTE\_LOCAL, and COM\_RIGHTS\_ACTIVATE\_LOCAL (0xb), and the third grants COM\_RIGHTS\_EXECUTE and COM\_RIGHTS\_ACTIVATE\_LOCAL (0x9).

To correct this, the first ACE should be changed to grant COM\_RIGHTS\_EXECUTE in combination with one of the other four access rights, or else the second and third ACEs should be changed to grant only COM\_RIGHTS\_EXECUTE.

## Related topics

<dl> <dt>

[DCOM Security Enhancements in Windows XP Service Pack 2 and Windows Server 2003 Service Pack 1](dcom-security-enhancements-in-windows-xp-service-pack-2-and-windows-server-2003-service-pack-1.md)
</dt> <dt>

[Security in COM](security-in-com.md)
</dt> </dl>

 

 




