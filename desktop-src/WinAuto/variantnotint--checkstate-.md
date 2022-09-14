---
title: VariantNotInt (CheckState)
description: VariantNotInt (CheckState)
ms.assetid: 77140193-22E8-427D-AE9C-FEC6B93483DD
ms.topic: article
ms.date: 05/31/2018
---

# VariantNotInt (CheckState)

## Text

The variant returned from {0} should be an {1} but is a {2}.

## Type

Error

## Description

An element is reporting an invalid MSAA state. For example, the [**get\_accState**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accstate) method used to retrieve the MSAA state of an element should return an integer value that represents one of the MSAA state constants, but is returning another variant instead.

This issue causes problems for people who rely on a screen-reader and keyboard for navigation because an incorrect element state might be reported to the user.

## Possible causes

The element or its parent has an MSAA state set inappropriately.

## Related topics

<dl> <dt>

[**IAccessible::get\_accState**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accstate)
</dt> <dt>

[**Object State Constants**](object-state-constants.md)
</dt> </dl>

 

 




