---
description: The RegisterUser action registers the user information with the installer to identify the user of a product.
ms.assetid: da615cb4-d36d-4180-8f97-c9f83c0df1c6
title: RegisterUser Action
ms.topic: article
ms.date: 05/31/2018
---

# RegisterUser Action

The RegisterUser action registers the user information with the installer to identify the user of a product.

## Sequence Restrictions

There are no sequence restrictions.

## ActionData Messages



| Field | Description of action data   |
|-------|------------------------------|
| \[1\] | Registered user information. |



 

## Remarks

The RegisterUser action is not performed during an administrative installation. If the product identifier entered by the user has not been validated by the [ValidateProductID action](validateproductid-action.md), the [**ProductID**](productid.md) property is not set and this action does nothing.

## Related topics

<dl> <dt>

[**USERNAME**](username.md)
</dt> <dt>

[**COMPANYNAME**](companyname.md)
</dt> <dt>

[**ProductID**](productid.md)
</dt> </dl>

 

 



