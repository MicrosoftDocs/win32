---
description: Each Active Directory object has a security descriptor assigned to it.
ms.assetid: 2e4ed13f-f09e-43b4-9862-95a79c229f0c
title: Directory Services Access Rights
ms.topic: article
ms.date: 05/31/2018
---

# Directory Services Access Rights

Each Active Directory object has a [*security descriptor*](/windows/desktop/SecGloss/s-gly) assigned to it. A set of trustee rights specific to directory service objects can be set within these security descriptors. These rights are listed in the following table. For more information, see [Control Access Rights](/windows/desktop/AD/control-access-rights).



| Rights                                | Meaning                                                                                                                                                                                                                                                                                 |
|---------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ACTRL\_DS\_OPEN<br/>            | Open a DS object.<br/>                                                                                                                                                                                                                                                            |
| ACTRL\_DS\_CREATE\_CHILD<br/>   | Create a child DS object.<br/>                                                                                                                                                                                                                                                    |
| ACTRL\_DS\_DELETE\_CHILD<br/>   | Delete a child DS object.<br/>                                                                                                                                                                                                                                                    |
| ACTRL\_DS\_LIST<br/>            | Enumerate a DS object.<br/>                                                                                                                                                                                                                                                       |
| ACTRL\_DS\_READ\_PROP<br/>      | Read the properties of a DS object.<br/>                                                                                                                                                                                                                                          |
| ACTRL\_DS\_WRITE\_PROP<br/>     | Write properties for a DS object.<br/>                                                                                                                                                                                                                                            |
| ACTRL\_DS\_SELF<br/>            | Access allowed only after validated rights checks supported by the object are performed. This flag can be used alone to perform all validated rights checks of the object or it can be combined with an identifier of a specific validated right to perform only that check.<br/> |
| ACTRL\_DS\_DELETE\_TREE<br/>    | Delete a tree of DS objects.<br/>                                                                                                                                                                                                                                                 |
| ACTRL\_DS\_LIST\_OBJECT<br/>    | List a tree of DS objects.<br/>                                                                                                                                                                                                                                                   |
| ACTRL\_DS\_CONTROL\_ACCESS<br/> | Access allowed only after extended rights checks supported by the object are performed. This flag can be used alone to perform all extended rights checks on the object or it can be combined with an identifier of a specific extended right to perform only that check.<br/>    |



 

 

