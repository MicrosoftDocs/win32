---
description: Lists and explains the access rights of the private data object.
ms.assetid: 82be57d0-487c-4eb7-83d5-0dd2d53a452b
title: Private Data Object Access Rights
ms.topic: article
ms.date: 05/31/2018
---

# Private Data Object Access Rights

The access types of this object type are:



| Access type          | Description                                      |
|----------------------|--------------------------------------------------|
| SECRET\_QUERY\_VALUE | This access type is needed to retrieve a secret. |
| SECRET\_SET\_VALUE   | This access type is needed to modify a secret.   |



 

## Generic Access Masks

This object type has the following generic access mappings:

``` syntax
    GENERIC_READ    STANDARD_RIGHTS_READ |
                    SECRET_QUERY_VALUE

    GENERIC_WRITE   STANDARD_RIGHTS_WRITE |
                    SECRET_SET_VALUE

    GENERIC_EXECUTE STANDARD_RIGHTS_EXECUTE
```

## Standard Access Types:

This object does not support the (optional) SYNCHRONIZE standard access type. All required access types are supported. The mask of all supported access types for this object type is:

``` syntax
    SECRET_ALL_ACCESS    STANDARD_RIGHTS_REQUIRED |
                    SECRET_QUERY_VALUE |
                    SECRET_SET_VALUE
```

 

 



