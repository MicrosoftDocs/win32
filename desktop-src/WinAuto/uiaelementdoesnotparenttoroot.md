---
title: UiaElementDoesNotParentToRoot
description: UiaElementDoesNotParentToRoot
ms.assetid: 0A1EDF46-420D-46ED-BD61-CA5E40847071
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# UiaElementDoesNotParentToRoot

## Text

Element's parent chain does not go to the Root Element

## Type

Warning

## Description

The navigation from the given element to the UI tree root is broken.

This issue can cause unpredictable results for an application that tries to navigate the UI tree.

## Possible causes

Incorrect implementation of the UI tree parent child hierarchy.

## Related topics

<dl> <dt>

[**IUIAutomationTreeWalker**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationtreewalker?branch=master)
</dt> </dl>

 

 




