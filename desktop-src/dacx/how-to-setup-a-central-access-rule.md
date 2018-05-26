---
title: How to setup a central access rule
description: This topic describes a Central Access Rule (CAR).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 0CE32378-C583-45D2-9960-F2AF3F78D84B
ms.prod: windows-server-dev
ms.technology: dynamic-access-control
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# How to setup a central access rule

This topic describes a Central Access Rule (CAR).

## Instructions

### Step 1: Central Access Rule (msAuthz-CentralAccessRule)

Central access rule defines who can have access to what scope of resources. It contains a unique name and a description. It also contains following expressions that are Security Descriptor Definition Language (SDDL) conditional expressions described in the [SDDL](https://msdn.microsoft.com/library/windows/desktop/aa379567) reference document.

-   Target Resources (msAuthz-ResourceCondition) - This expression describes the scope of resources that the permission will apply to. For example, if the expression state that resource department must be "Finance", it means that the rule applies only to all the files/folders that has department classified as "Finance". It is recommended to leave this as empty so that by default it applies to all resources.
-   Current Permissions (msAuthz-EffectiveSecurityPolicy) - This expression describes who can have access to resources. This can be either relative or explicit. For example, user department is "Finance" or the user department is the same as the resource department. Groups can be used instead of claims. For example, the user as a member of group "Finance Users" can be used. It is recommended to use a set of default permissions if the user does not provide any input. For example, the default should include Built in Administrator and File/Folder Owners. The permissions specified in this field will take effect in the system once the policy including this rule is published and selected on the resource.
-   Proposed Permissions (msAuthz-ProposedSecurityPolicy) - This expression uses the same format as current permissions. It will not take effect. Instead the access difference between current permission and this field will be logged to help IT administrators stage the permissions. By leaving this field as null, the audit log will not be generated. It is recommended to leave this field null if there is no difference between the current and proposed permission to avoid the system processing the same permission twice every time a user tries to access the target resources.
-   Previous Permissions (msAuthz-LastEffectiveSecurityPolicy) This field is a read-only field. It stores the previous permission. This field allows easy recovery to the last current permission.
-   

## Related topics

<dl> <dt>

[How to use central access policies for dynamic access control](how-to-use-central-access-policies-for-dynamic-access-control.md)
</dt> </dl>

 

 




