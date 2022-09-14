---
description: The product code is a GUID that is the principal identification of an application or product.
ms.assetid: 6fbad59b-27b7-4ac1-bad5-8a608c7b270f
title: Product Codes
ms.topic: article
ms.date: 05/31/2018
---

# Product Codes

The product code is a GUID that is the principal identification of an application or product. For more information, see the [**ProductCode**](productcode.md) property. If significant changes are made to a product then the product code should also be changed to reflect this. It is not however a requirement that the product code be changed if the changes to the product are relatively minor.

The 32-bit and 64-bit versions of an application's package must have different product codes. If any 32-bit component of an application is recompiled into a 64-bit component, a new product code must be assigned.

If a server exposed in the [PublishComponent Table](publishcomponent-table.md) is recompiled from 32-bits to 64-bits, the GUID in this table may also need to be changed so that 32-bit and 64-bit clients can identify the appropriate qualified component category. In this case, the product code must also be changed.

Note that letters in product code GUIDs must be uppercase. Utilities such as GUIDGEN generate GUIDs containing lowercase letters. The lowercase letters in these GUIDs must be changed to uppercase to be used as a product code or package code. For more information, see [Changing the Product Code](changing-the-product-code.md).

The package code is a GUID identifying a particular Windows Installer [*package*](p-gly.md). The package code associates an .msi file with an application or product and can also be used for the verification of sources. The product and package codes are not interchangeable. No two nonidentical .msi files should ever have the same package code. Although it is common to ship an application that has the same package code and product code, the two values can diverge as the application is updated. For more information, see [Package Codes](package-codes.md).

 

 



