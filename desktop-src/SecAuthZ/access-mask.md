---
description: Defines standard, specific, and generic rights. These rights are used in access control entries (ACEs) and are the primary means of specifying the requested or granted access to an object.
ms.assetid: f115ee54-3333-4109-8004-d71904a7a943
title: ACCESS_MASK (Winnt.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ACCESS\_MASK

The **ACCESS\_MASK** data type is a **DWORD** value that defines standard, specific, and generic rights. These rights are used in [*access control entries*](/windows/desktop/SecGloss/a-gly) (ACEs) and are the primary means of specifying the requested or granted access to an object.


```C++
typedef DWORD ACCESS_MASK;
typedef ACCESS_MASK* PACCESS_MASK;
```



## Remarks

The bits in this value are allocated as follows.



| Bits             | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0 15<br/>  | Specific rights. Contains the access mask specific to the object type associated with the mask.<br/>                                                                                                                                                                                                                                                                                                                                                                                                          |
| 16 23<br/> | Standard rights. Contains the object's standard access rights.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 24<br/>    | Access system security (**ACCESS\_SYSTEM\_SECURITY**). It is used to indicate access to a [*system access control list*](/windows/desktop/SecGloss/s-gly) (SACL). This type of access requires the calling process to have the **SE\_SECURITY\_NAME** (Manage auditing and security log) privilege. If this flag is set in the access mask of an audit access ACE (successful or unsuccessful access), the SACL access will be audited.<br/> |
| 25<br/>    | Maximum allowed (**MAXIMUM\_ALLOWED**).<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 26 27<br/> | Reserved.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 28<br/>    | Generic all (**GENERIC\_ALL**).<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 29<br/>    | Generic execute (**GENERIC\_EXECUTE**).<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 30<br/>    | Generic write (**GENERIC\_WRITE**).<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 31<br/>    | Generic read (**GENERIC\_READ**).<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |



 

Standard rights bits, 16 to 23, contain the object's standard access rights and can be a combination of the following predefined flags.



| Bit           | Flag                         | Meaning                                                                                                                                                                                                                                  |
|---------------|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16<br/> | **DELETE**<br/>        | Delete access.<br/>                                                                                                                                                                                                                |
| 17<br/> | **READ\_CONTROL**<br/> | Read access to the owner, group, and [*discretionary access control list*](/windows/desktop/SecGloss/d-gly) (DACL) of the security descriptor.<br/> |
| 18<br/> | **WRITE\_DAC**<br/>    | Write access to the DACL.<br/>                                                                                                                                                                                                     |
| 19<br/> | **WRITE\_OWNER**<br/>  | Write access to owner.<br/>                                                                                                                                                                                                        |
| 20<br/> | **SYNCHRONIZE**<br/>   | Synchronize access.<br/>                                                                                                                                                                                                           |



 

The following constants defined in Winnt.h represent the specific and standard access rights.


```C++
#define DELETE                           (0x00010000L)
#define READ_CONTROL                     (0x00020000L)
#define WRITE_DAC                        (0x00040000L)
#define WRITE_OWNER                      (0x00080000L)
#define SYNCHRONIZE                      (0x00100000L)

#define STANDARD_RIGHTS_REQUIRED         (0x000F0000L)

#define STANDARD_RIGHTS_READ             (READ_CONTROL)
#define STANDARD_RIGHTS_WRITE            (READ_CONTROL)
#define STANDARD_RIGHTS_EXECUTE          (READ_CONTROL)

#define STANDARD_RIGHTS_ALL              (0x001F0000L)

#define SPECIFIC_RIGHTS_ALL              (0x0000FFFFL)
```



## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                   |
| Header<br/>                   | <dl> <dt>Winnt.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Access Control](access-control.md)
</dt> <dt>

[Basic Access Control Structures](authorization-structures.md)
</dt> <dt>

[Access Rights and Access Masks](access-rights-and-access-masks.md)
</dt> <dt>

[**GENERIC\_MAPPING**](/windows/desktop/api/Winnt/ns-winnt-generic_mapping)
</dt> </dl>

 

