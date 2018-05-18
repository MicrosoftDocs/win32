---
title: IncorrectRoundTrip
description: IncorrectRoundTrip
ms.assetid: '244537EB-E7DC-49E4-BEAF-CFE3ED25E0B2'
---

# IncorrectRoundTrip

## Text

Call to accNavigate((Click Snooze to be reminded again in:), 1, NAVDIR\_NEXT), then accNavigate((Open), 2, NAVDIR\_PREVIOUS), should have returned Click Snooze to be reminded again in:(ChildId=1), but returned Click Snooze to be reminded again in:

## Type

Error

## Description

using [**accNavigate**](iaccessible-iaccessible--accnavigate.md) to traverse the element tree of the verification target does not return the same starting element when the direction of traversal is reversed.

![example of an invalid msaa implementation that caused incorrect round-trip navigation](images/accchecker-invalid-round-trip.png)

This issue can cause navigation problems for automated tools because traversing elements might be erratic and unpredictable.

## Possible causes

An incorrect or invalid MSAA implementation.

## Related topics

<dl> <dt>

[**IAccessible::accNavigate**](iaccessible-iaccessible--accnavigate.md)
</dt> </dl>

 

 




