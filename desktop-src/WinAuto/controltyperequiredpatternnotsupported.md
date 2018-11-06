---
title: ControlTypeRequiredPatternNotSupported
description: ControlTypeRequiredPatternNotSupported
ms.assetid: D3DFB577-0F46-4598-A90F-C91A6A360AAC
ms.topic: article
ms.date: 05/31/2018
---

# ControlTypeRequiredPatternNotSupported

## Text

Element with a ControlType of {0} should support {1} but this element does not

## Type

Error

## Description

The element's UI Automation support does not comply with the UI Automation specification because the element should support the provided list of control patterns, but does not. As a result, this element might not be properly exposed to assistive technologies, which could have a serious impact on user experience.

## Possible causes

-   Incomplete UI Automation implementation.
-   The ControlType property is not set correctly.

## Related topics

<dl> <dt>

[**UIA\_ControlTypePropertyId**](uiauto-automation-element-propids.md)
</dt> <dt>

[UI Automation Control Types Overview](uiauto-controltypesoverview.md)
</dt> <dt>

[UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md)
</dt> </dl>

 

 




