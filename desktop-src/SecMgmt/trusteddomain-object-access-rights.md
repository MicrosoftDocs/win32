---
description: Lists and explains the access rights of the TrustedDomain object.
ms.assetid: eb82864c-7e69-4ed5-a55d-d6792670bcd1
title: TrustedDomain Object Access Rights
ms.topic: article
ms.date: 05/31/2018
---

# TrustedDomain Object Access Rights

The [**TrustedDomain**](trusteddomain-object.md) object type has the following access types:



| Access type                  | Description                                                                      |
|------------------------------|----------------------------------------------------------------------------------|
| TRUSTED\_QUERY\_DOMAIN\_NAME | This access type is needed to query the name of the trusted domain.              |
| TRUSTED\_SET\_CONTROLLERS    | This access type is needed to set the list of controllers of the trusted domain. |
| TRUSTED\_QUERY\_POSIX        | This access type is needed to retrieve the Posix ID offset of a trusted domain.  |
| TRUSTED\_SET\_POSIX          | This access type is needed to set the Posix ID offset of a trusted domain.       |



 

## Generic Access Masks

This object type has the following generic access mappings:

``` syntax
    GENERIC_READ        STANDARD_RIGHTS_READ |
                    TRUSTED_QUERY_DOMAIN_NAME

    GENERIC_WRITE        STANDARD_RIGHTS_WRITE |
                    TRUSTED_SET_POSIX

    GENERIC_EXECUTE    STANDARD_RIGHTS_EXECUTE |
                    TRUSTED_QUERY_POSIX
```

## Standard Access Types

This object does not support the (optional) SYNCHRONIZE standard access type. All required access types are supported. The mask of all supported access types for this object type is:

``` syntax
    TRUSTED_ALL_ACCESS    STANDARD_RIGHTS_REQUIRED |
                    TRUSTED_QUERY_DOMAIN_NAME |
                    TRUSTED_QUERY_CONTROLLERS |
                    TRUSTED_SET_CONTROLLERS
```

 

 



