---
title: TabbedToUnknownElement
description: TabbedToUnknownElement
ms.assetid: B0447B19-E281-4D30-8ED8-FC0EE13571C8
ms.topic: article
ms.date: 05/31/2018
---

# TabbedToUnknownElement

## Text

Tabbing has gone to an element outside the target hwnd.

## Type

Error

## Description

Using standard keyboard navigation (Tab or Shift+Tab) causes focus to shift outside the HWND of the verification target.

AccChecker moves up the element tree to the top-level HWND for the chosen verification target before running any verification tasks. This reduces the number of spurious errors generated if an HWND chosen for verification is part of a more complex client area.

## Possible causes

-   The verification target doesn't require a tabbing implementation to provide full functionality.
-   User interaction during verification, such as moving focus to a non-target HWND, interfered with the verification process.

 

 




