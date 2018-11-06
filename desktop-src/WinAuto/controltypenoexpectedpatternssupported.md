---
title: ControlTypeNoExpectedPatternsSupported
description: ControlTypeNoExpectedPatternsSupported
ms.assetid: 2C9CEFEA-8207-47A7-B100-A56CFBFB792D
ms.topic: article
ms.date: 05/31/2018
---

# ControlTypeNoExpectedPatternsSupported

## Text

Element with a ControlType of {0} should support at least one of these patterns:{1} but this element does not

## Type

Error

## Description

The element's UI Automation support does not comply with the UI Automation specification because the element should support at least one of the provided list of control patterns, but does not. As a result, this element might not be properly exposed to assistive technologies, which could have a serious impact on user experience.

## Possible causes

-   Incomplete UI Automation implementation.
-   The ControlType property is not set correctly.

## Remarks

AccChecker logs this error message for an indeterminate progress bar. You can ignore this message and/or add it to the suppressions list.

## Related topics

<dl> <dt>

[**UIA\_ControlTypePropertyId**](uiauto-automation-element-propids.md)
</dt> <dt>

[UI Automation Control Types Overview](uiauto-controltypesoverview.md)
</dt> <dt>

[UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md)
</dt> </dl>

 

 




