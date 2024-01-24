---
description: The Account Object Access Rights type has the following access types.
ms.assetid: 42fb22bb-8135-4a8f-bce6-e767d6c5aaea
title: Account Object Access Rights
ms.topic: article
ms.date: 05/31/2018
---

# Account Object Access Rights

The Account Object Access Rights type has the following access types.



| Access type                     | Description                                                                                                                                                                                                                                           |
|---------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ACCOUNT\_VIEW                   | This access type is required to read the account information. This includes the [*privileges*](/windows/desktop/SecGloss/p-gly) assigned to the account, memory quotas assigned, and any special access types granted. |
| ACCOUNT\_ADJUST\_PRIVILEGES     | This access type is required to assign privileges to or remove privileges from an account.                                                                                                                                                            |
| ACCOUNT\_ADJUST\_QUOTAS         | This access type is required to change the system quotas assigned to an account.                                                                                                                                                                      |
| ACCOUNT\_ADJUST\_SYSTEM\_ACCESS | This access type is required to update the system access flags for the account.                                                                                                                                                                       |



 

## Generic Access Masks

The [**Account**](account-object.md) object publishes the following mappings from generic access types to specific access types.

``` syntax
    GENERIC_READ        STANDARD_RIGHTS_READ |
                        ACCOUNT_VIEW 
            
    GENERIC_WRITE       STANDARD_RIGHTS_WRITE |
                        ACCOUNT_ADJUST_PRIVILEGES |
                        ACCOUNT_ADJUST_QUOTAS |
                        ACCOUNT_ADJUST_SYSTEM_ACCESS

    GENERIC_EXECUTE        STANDARD_RIGHTS_EXECUTE
```

## Standard Access Types

This object does not support the (optional) SYNCHRONIZE standard access type. All required access types are supported. The mask of all supported access types for this object type is as follows.

``` syntax
    ACCOUNT_ALL_ACCESS  STANDARD_RIGHTS_REQUIRED |
                        ACCOUNT_VIEW |
                        ACCOUNT_ADJUST_PRIVILEGES |    
                        ACCOUNT_ADJUST_QUOTAS |
                        ACCOUNT_ADJUST_SYSTEM_ACCESS
```

 

 
