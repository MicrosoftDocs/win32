---
description: Each type of securable object has a set of access rights that correspond to operations specific to that type of object.
ms.assetid: f43bccce-0f8c-4732-b678-5fd3218a9f84
title: Standard Access Rights
ms.topic: article
ms.date: 05/31/2018
---

# Standard Access Rights

Each type of securable object has a set of access rights that correspond to operations specific to that type of object. In addition to these object-specific access rights, there is a set of standard access rights that correspond to operations common to most types of securable objects.

The [access mask format](access-mask-format.md) includes a set of bits for the standard access rights. The following Windows constants for standard access rights are defined in Winnt.h.



| Constant      | Meaning                                                                                                                                                                                                                                                                                                                                      |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DELETE        | The right to delete the object.                                                                                                                                                                                                                                                                                                              |
| READ\_CONTROL | The right to read the information in the object's [*security descriptor*](/windows/desktop/SecGloss/s-gly), not including the information in the [*system access control list*](/windows/desktop/SecGloss/s-gly) (SACL). |
| SYNCHRONIZE   | The right to use the object for synchronization. This enables a thread to wait until the object is in the signaled state. Some object types do not support this access right.                                                                                                                                                                |
| WRITE\_DAC    | The right to modify the [*discretionary access control list*](/windows/desktop/SecGloss/d-gly) (DACL) in the object's security descriptor.                                                                                                                    |
| WRITE\_OWNER  | The right to change the owner in the object's security descriptor.                                                                                                                                                                                                                                                                           |



 

Winnt.h also defines the following combinations of the standard access rights constants.



| Constant                   | Meaning                                                                           |
|----------------------------|-----------------------------------------------------------------------------------|
| STANDARD\_RIGHTS\_ALL      | Combines DELETE, READ\_CONTROL, WRITE\_DAC, WRITE\_OWNER, and SYNCHRONIZE access. |
| STANDARD\_RIGHTS\_EXECUTE  | Currently defined to equal READ\_CONTROL.                                         |
| STANDARD\_RIGHTS\_READ     | Currently defined to equal READ\_CONTROL.                                         |
| STANDARD\_RIGHTS\_REQUIRED | Combines DELETE, READ\_CONTROL, WRITE\_DAC, and WRITE\_OWNER access.              |
| STANDARD\_RIGHTS\_WRITE    | Currently defined to equal READ\_CONTROL.                                         |



 

 

 
