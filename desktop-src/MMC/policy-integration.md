---
title: Policy Integration
description: In Microsoft Windows, group policies are intended to allow administrators to determine access to tools and functionality on a group basis, for either computers or users.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7077387a-fb6a-4714-829d-429820143cb5
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- policy integration MMC
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Policy Integration

In Microsoft Windows, group policies are intended to allow administrators to determine access to tools and functionality on a group basis, for either computers or users. For MMC, administrators may wish to prevent a specific group from accessing specified snap-in functionality.

Group Policy, as it relates to MMC and snap-ins, can accomplish the following:

-   **Restrict author mode.** Administrators can specify that author mode is restricted for any group.
-   **Restrict access to specified snap-ins.** Administrators can restrict access to a specified list of snap-ins.
-   **Grant access to a list of permitted snap-ins.** Administrators can grant access to a specified list of snap-ins. Snap-ins not included in the list have restricted access.

Be aware that policies regarding MMC and snap-ins are applicable to individual users and groups of users. The policies cannot be applied to computers.

For more information about Group Policy, see the [Group Policy API](https://msdn.microsoft.com/library/aa374177) documentation. The rest of this section discusses the features that snap-ins must provide for administrators to apply Group Policy to them.

## Snap-ins and Group Policy

Group policies are administered using the Group Policy snap-in. The Group Policy snap-in obtains registry-based policy settings from an administrative template (.adm) file. An .adm file defines the property page the Group Policy snap-in will display to allow an administrator to manage its settings. The file also indicates the registry location where the settings are stored.

Each snap-in that can be administered with the Group Policy snap-in must provide an .adm file. The .adm file should display for the administrator two check boxes that allow the snap-in to be placed on either a "permitted" list or a "restricted" list. The list a snap-in is on is determined by a value of the **Restrict\_Run** named Boolean value at the following registry location:

**HKEY\_CURRENT\_USER**\\**SOFTWARE**\\**Policies**\\**Microsoft**\\**MMC**\\***SnapinGUID***

The **{snapin GUID}** key is the string representation of the snap-in's CLSID. The following table lists the different values that the **Restrict\_Run** named value can take:



| Value of Restrict\_Run | Description                                     |
|------------------------|-------------------------------------------------|
| Value not present      | Behavior is unrestricted.                       |
| 0                      | The snap-in is placed on the "permitted" list.  |
| 1                      | The snap-in is placed on the "restricted" list. |



 

The following is a sample .adm file for a snap-in:

``` syntax
CLASS USER

CATEGORY !!MMC

    CATEGORY !!MMC_EventVwr

        POLICY !!MMC_EventVwr

               KEYNAME "Software\Policies\Microsoft\MMC\{975797FC-4E2A-11D0-B702-00C04FD8DBF7}"

#if version >= 4

                       SUPPORTED !!SUPPORTED_Win2k

#endif

 

                EXPLAIN !!MMC_Permit_EventVwr_Explain

                VALUENAME "Restrict_Run"

                    VALUEON   NUMERIC 0

                    VALUEOFF  NUMERIC 1          

            END POLICY        

    END CATEGORY

END CATEGORY

 

[strings]

MMC="MMC"

MMC_EventVwr="Event Viewer"

MMC_Permit_EventVwr_Explain="When this checkbox is enabled, the users effected by this policy will be allowed to use the event viewer snapin unless it has been explicitly restricted."

SUPPORTED_Win2k="At least Microsoft Windows 2000"
```

A snap-in must provide its own .adm file for the Group Policy editor to set the snap-in's permission. Additionally, a new snap-in will not be added to the Global Policy's Restricted/Permitted Snap-in list by means of the .adm file.

## Related topics

<dl> <dt>

[Group Policy](https://msdn.microsoft.com/library/aa374177)
</dt> <dt>

[Distributing Your Snap-in](distributing-your-snap-in.md)
</dt> </dl>

 

 




