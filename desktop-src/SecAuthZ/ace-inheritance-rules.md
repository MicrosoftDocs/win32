---
description: The system propagates inheritable access control entries (ACEs) to child objects according to a set of inheritance rules.
ms.assetid: 08f76aaa-8379-4ba8-9735-7568001bcd53
title: ACE Inheritance Rules
ms.topic: article
ms.date: 05/31/2018
---

# ACE Inheritance Rules

The system propagates inheritable [*access control entries*](/windows/desktop/SecGloss/a-gly) (ACEs) to child objects according to a set of inheritance rules. The system places inherited ACEs in the [*discretionary access control list*](/windows/desktop/SecGloss/d-gly) (DACL) of the child according to the preferred [order of ACEs in a DACL](order-of-aces-in-a-dacl.md). The system sets the INHERITED\_ACE flag in all inherited ACEs.

The ACEs inherited by container and noncontainer child objects differ, depending on the combinations of inheritance flags. These inheritance rules work the same for both DACLs and [*system access control lists*](/windows/desktop/SecGloss/s-gly) (SACLs).



| Parent ACE flag                                  | Effect on child ACL                                                                                                                                                                                                                      |
|--------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OBJECT\_INHERIT\_ACE only                        | Noncontainer child objects: Inherited as an effective ACE. Container child objects: Containers inherit an inherit-only ACE unless the NO\_PROPAGATE\_INHERIT\_ACE bit flag is also set.<br/>                                       |
| CONTAINER\_INHERIT\_ACE only                     | Noncontainer child objects: No effect on the child object. Container child objects: The child object inherits an effective ACE. The inherited ACE is inheritable unless the NO\_PROPAGATE\_INHERIT\_ACE bit flag is also set.<br/> |
| CONTAINER\_INHERIT\_ACE and OBJECT\_INHERIT\_ACE | Noncontainer child objects: Inherited as an effective ACE. Container child objects: The child object inherits an effective ACE. The inherited ACE is inheritable unless the NO\_PROPAGATE\_INHERIT\_ACE bit flag is also set.<br/> |
| No inheritance flags set                         | No effect on child container or noncontainer objects.                                                                                                                                                                                    |



 

If an inherited ACE is an effective ACE for the child object, the system maps any generic rights to the specific rights for the child object. Similarly, the system maps generic [*security identifiers*](/windows/desktop/SecGloss/s-gly) (SIDs), such as CREATOR\_OWNER, to the appropriate SID. If an inherited ACE is an inherit-only ACE, any generic rights or generic SIDs are left unchanged so that they can be mapped appropriately when the ACE is inherited by the next generation of child objects.

For a case in which a container object inherits an ACE that is both effective on the container and inheritable by its descendants, the container may inherit two ACEs. This occurs if the inheritable ACE contains generic information. The container inherits an inherit-only ACE that contains the generic information and an effective-only ACE in which the generic information has been mapped.

An [object-specific ACE](object-specific-aces.md) has an **InheritedObjectType** member that can contain a GUID to identify the type of object that can inherit the ACE.

If the **InheritedObjectType** GUID is not specified, the inheritance rules for an object-specific ACE are the same as for a standard ACE.

If the **InheritedObjectType** GUID is specified, the ACE is inheritable by objects that match the GUID if OBJECT\_INHERIT\_ACE is set, and by containers that match the GUID if CONTAINER\_INHERIT\_ACE is set. Note that currently only DS objects support object-specific ACEs, and the DS treats all object types as containers.

 

