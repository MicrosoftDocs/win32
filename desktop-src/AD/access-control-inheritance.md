---
title: Access Control Inheritance
description: Access-control entries (ACEs) in an object access-control list (ACL) can belong to either Effective ACL or Inherit ACL.
ms.assetid: 2530eef5-7804-4b27-8756-d97be1cea116
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Access Control Inheritance

Access-control entries (ACEs) in an object access-control list (ACL) can belong to one of two categories:

-   Effective ACL: ACEs in this category apply to the object.
-   Inherit ACL: ACEs in this category are inherited by objects created in the container.

Each ACE in the DACL can belong to one, or more, categories. The categories for where an ACE belongs are determined by the inheritance control flags set in the ACE.

Three inheritance-control flags can be set in the [**AceFlags**](/windows/desktop/ADSI/iadsaccesscontrolentry-property-methods) property of an ACE.



| Flag                                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **ADS\_ACEFLAG\_INHERIT\_ACE**                | This flag indicates that the ACE is part of the inherit ACL and that child objects inherit the inheritance control flags of this ACE.                                                                                                                                                                                                                                                                                                                         |
| **ADS\_ACEFLAG\_NO\_PROPAGATE\_INHERIT\_ACE** | This flag indicates that the ACE is part of the inherit ACL, but that no inheritance control flags are propagated to direct child objects (direct descendants) and the ACE is effective on the direct child objects.                                                                                                                                                                                                                                          |
| **ADS\_ACEFLAG\_INHERIT\_ONLY\_ACE**          | This flag indicates that the ACE is not part of effective ACL. If this flag is not set, then the ACE is part of the effective ACL. This flag is useful for setting permissions inheritable by subobjects, but do not affect accessibility of the container. For example, if an ACE is intended to be inherited by user objects in a organizational unit, it is likely that it should not be enforced for access to the organizational unit itself.<br/> |



 

The **ADS\_ACEFLAG\_NO\_PROPAGATE\_INHERIT\_ACE** and **ADS\_ACEFLAG\_INHERIT\_ONLY\_ACE** flags are meaningful only if **ADS\_ACEFLAG\_INHERIT\_ACE** is present. This is because the **ADS\_ACEFLAG\_INHERIT\_ACE** flag adds inheritance behavior to an inheritable ACE, but does not define the type of inheritance. The **ADS\_ACEFLAG\_NO\_PROPAGATE\_INHERIT\_ACE** and **ADS\_ACEFLAG\_INHERIT\_ONLY\_ACE** flags define a specific type of inheritance behavior.

It is important to remember that the system also sets the following flags based on the type and state of the ACE.



| Flag                                    | Description                                           |
|-----------------------------------------|-------------------------------------------------------|
| **ADS\_ACEFLAG\_INHERITED\_ACE**        | This flag indicates that the ACE was inherited.       |
| **ADS\_ACEFLAG\_VALID\_INHERIT\_FLAGS** | This flag indicates that the inherit flags are valid. |



 

The following table lists the effects of the different flag combinations for the [**AceFlags**](/windows/desktop/ADSI/iadsaccesscontrolentry-property-methods) property of an ACE.



| Flag                                                                                                                    | Effect on object containing the ACE                     | Effect on direct child objects                                                      | Effect on objects below direct children               |
|-------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|-------------------------------------------------------------------------------------|-------------------------------------------------------|
| No flags set.                                                                                                           | Effective ACE: ACE applies to the object.               | ACE is not inherited.                                                               | ACE is not inherited.                                 |
| **ADS\_ACEFLAG\_INHERIT\_ACE**                                                                                          | Effective ACE                                           | ACE is inherited. ACE is an effective ACE.<br/>                               | ACE is inherited. ACE is an effective ACE.<br/> |
| **ADS\_ACEFLAG\_INHERIT\_ACE** \| **ADS\_ACEFLAG\_INHERIT\_ONLY\_ACE**                                                  | Not an Effective ACE: ACE does not apply to the object. | ACE is inherited. ACE is an effective ACE.<br/>                               | ACE is inherited. ACE is an effective ACE.<br/> |
| **ADS\_ACEFLAG\_INHERIT\_ACE** \| **ADS\_ACEFLAG\_NO\_PROPAGATE\_INHERIT\_ACE**                                         | Effective ACE                                           | ACE is inherited but without inheritance flags. ACE is an Effective ACE<br/>  | ACE is not inherited.                                 |
| **ADS\_ACEFLAG\_INHERIT\_ACE** \| **ADS\_ACEFLAG\_INHERIT\_ONLY\_ACE** \| **ADS\_ACEFLAG\_NO\_PROPAGATE\_INHERIT\_ACE** | Not an Effective ACE.                                   | ACE is inherited but without inheritance flags. ACE is an Effective ACE.<br/> | ACE is not inherited.                                 |



 

 

