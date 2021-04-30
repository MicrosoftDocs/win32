---
description: Use standard Windows controls whenever possible, because they are fully compatible with Microsoft Active Accessibility guidelines. This includes controls provided by Windows (User32.dll) and the Windows common controls library (Comctl32.dll).
ms.assetid: 2d0b255f-52be-423b-a495-64bf21041858
title: Using Standard Windows Controls
ms.topic: article
ms.date: 05/31/2018
---

# Using Standard Windows Controls

Use standard Windows controls whenever possible, because they are fully compatible with Microsoft Active Accessibility guidelines. This includes controls provided by Windows (User32.dll) and the Windows common controls library (Comctl32.dll).

Each standard Windows control is a separate window of a specific class, so the accessibility aid is notified when the focus moves to a new control. The aid can determine the controls window class, and any additional messages it can send to query or alter the controls state. The aid can also identify all of the child controls contained within a parent window and identify the parent of any control.

Some common controls are extremely flexible and can often substitute for less-accessible custom controls and owner-drawn controls. For example, a list view can replace an owner-drawn list box to display a check box next to each item. As another example, the enhanced button control can display both images and text. Previously, this required the use of a custom control.

 

 



