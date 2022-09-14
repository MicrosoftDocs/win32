---
title: UiaDuplicateAccessKey
description: UiaDuplicateAccessKey
ms.assetid: 83B742F7-2839-4F3B-B459-F8505ABDDFCA
ms.topic: article
ms.date: 05/31/2018
---

# UiaDuplicateAccessKey

## Text

There is a sibling Automation Element that has the same access key / accelerator key

## Type

Error

## Description

The access/accelerator key assigned to the element is also assigned to another element in the verification target.

This issue causes problems for people who rely on the keyboard for navigation because multiple elements might be invoked or cycle focus using the same shortcut or accelerator key.

## Related topics

<dl> <dt>

[**IUIAutomationElement::CurrentName**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-get_currentname)
</dt> <dt>

[**IUIAutomationElement::CurrentAcceleratorKey**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-get_currentacceleratorkey)
</dt> <dt>

[**IUIAutomationElement::CurrentAccessKey**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-get_currentaccesskey)
</dt> <dt>

[**UIA\_AcceleratorKeyPropertyId**](uiauto-automation-element-propids.md)
</dt> <dt>

[**UIA\_AccessKeyPropertyId**](uiauto-automation-element-propids.md)
</dt> <dt>

[**UIA\_NamePropertyId**](uiauto-automation-element-propids.md)
</dt> </dl>

 

 




