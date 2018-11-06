---
title: FirstChildLastChildMismatch
description: FirstChildLastChildMismatch
ms.assetid: 98726C1A-DC43-4FC7-8ECA-628F63D0AFE3
ms.topic: article
ms.date: 05/31/2018
---

# FirstChildLastChildMismatch

## Text

When navigating by calling {0} from the tested node, and then repeatedly calling {1}, we finished at the following child: {2}. This did not match the result of calling {3} on the tested node, which yielded: {4}. Instead, the child should report as its parent the testing node.

## Type

Error

## Description

There is a problem when navigating between element’s children. 1. An incorrect or invalid UI Automation implementation.

This issue can cause navigation problems for automated tools because traversing elements might be erratic and unpredictable.

## Possible causes

An incorrect or invalid UI Automation implementation.

## Related topics

<dl> <dt>

[**IUIAutomationElement::GetCachedParent**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-getcachedparent)
</dt> <dt>

[**IUIAutomationTreeWalker**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationtreewalker)
</dt> </dl>

 

 




