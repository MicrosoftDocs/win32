---
title: VariantNotInt (CheckRole)
description: VariantNotInt (CheckRole)
ms.assetid: 24A9E91D-92E6-492B-B5CE-DF42E5923F60
ms.topic: article
ms.date: 05/31/2018
---

# VariantNotInt (CheckRole)

## Text

The variant returned from {0} should be an {1} but is a {2}.

## Type

Error

## Description

An element is reporting an invalid MSAA role. For example, the [**get\_accRole**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accrole) method used to retrieve the MSAA role of an element should return an integer value that represents one of the MSAA role constants, but is returning another variant instead.

This issue causes problems for people who rely on a screen-reader and keyboard for navigation because elements may be incorrectly identified to the user.

## Possible causes

The element or its parent has an MSAA role set inappropriately.

## Related topics

<dl> <dt>

[**IAccessible::get\_accRole**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accrole)
</dt> <dt>

[**Object Roles**](object-roles.md)
</dt> </dl>

 

 




