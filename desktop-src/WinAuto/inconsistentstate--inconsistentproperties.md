---
title: InconsistentState, InconsistentProperties
description: InconsistentState, InconsistentProperties
ms.assetid: '82A2ECA8-0155-402A-A745-B97D3F633643'
---

# InconsistentState, InconsistentProperties

## Text

A control has states/properties that are inconsistent {0} and {1}

## Type

Error

## Description

An element is reporting inconsistent or conflicting MSAA states or UI Automation properties. For example, when the [**get\_accState**](iaccessible-iaccessible--get-accstate.md) method returns any of the following combinations.

-   STATE\_SYSTEM\_EXPANDED and STATE\_SYSTEM\_COLLAPSED
-   STATE\_SYSTEM\_SELECTED and not STATE\_SYSTEM\_SELECTABLE
-   STATE\_SYSTEM\_FOCUSED and not STATE\_SYSTEM\_FOCUSABLE

This issue causes problems for people who rely on a screen-reader and keyboard for navigation because an incorrect element state might be reported to the user.

## Possible causes

The element or its parent has an MSAA state set inappropriately.

## Related topics

<dl> <dt>

[**IAccessible::get\_accState**](iaccessible-iaccessible--get-accstate.md)
</dt> <dt>

[**Object State Constants**](object-state-constants.md)
</dt> <dt>

[States and Properties](uiauto-msaa.md#states-and-properties)
</dt> </dl>

 

 




