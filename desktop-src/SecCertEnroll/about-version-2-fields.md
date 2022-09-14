---
description: An X.509 version 2 certificate contains the basic fields defined in version 1 and adds the following fields.
ms.assetid: 533d43d7-0c49-4461-8ba8-368c103feb4f
title: Version 2 Fields
ms.topic: article
ms.date: 05/31/2018
---

# Version 2 Fields

An X.509 version 2 certificate contains the basic fields defined in version 1 and adds the following fields.

## Issuer Unique Identifier

Contains a unique value that can be used to make the X.500 name of the CA unambiguous when reused by different entities over time.

``` syntax
---------------------------------------------------------------------
-- Issuer Unique identifier
---------------------------------------------------------------------
issuerUniqueIdentifier ::= [1] IMPLICIT UniqueIdentifier OPTIONAL

UniqueIdentifier ::= BITSTRING
```

## Subject Unique Identifier

Contains a unique value that can be used to make the X.500 name of the certificate subject unambiguous when reused by different entities over time.

``` syntax
---------------------------------------------------------------------
-- Issuer Unique identifier
---------------------------------------------------------------------
subjectUniqueIdentifier ::= [2] IMPLICIT UniqueIdentifier OPTIONAL

UniqueIdentifier ::= BITSTRING
```

## Related topics

<dl> <dt>

[Basic Fields](about-basic-fields.md)
</dt> <dt>

[Version 3 Extensions](about-version-3-extensions.md)
</dt> <dt>

[X.509 Public Key Certificates](about-x-509-public-key-certificates.md)
</dt> </dl>

 

 



