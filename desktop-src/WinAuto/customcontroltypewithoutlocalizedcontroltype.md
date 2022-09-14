---
title: CustomControlTypeWithoutLocalizedControlType
description: CustomControlTypeWithoutLocalizedControlType
ms.assetid: F52E37AB-607B-4899-B59A-3E6EE87FFDA6
ms.topic: article
ms.date: 05/31/2018
---

# CustomControlTypeWithoutLocalizedControlType

## Text

Element doesn't have the LocalizedControlType property set

## Type

Error

## Description

The element's [**LocalizedControlType**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-get_currentlocalizedcontroltype) property is not set.

Most screen readers read the localized control type to describe the element’s nature. If the localized control type is not set, a screen reader falls back to reading the main control type, which is always in English and may not make sense to all users.

## Possible causes

## Related topics

<dl> <dt>

[The LocalizedControlType Property](uiauto-controltypesoverview.md)
</dt> <dt>

[**UIA\_LocalizedControlTypePropertyId**](uiauto-automation-element-propids.md)
</dt> </dl>

 

 




