---
title: ListPad Control
description: Used on a list view taskpad DHTML page to display a list-view control that contains items from an IResultData result list.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0a6712f9-b5e6-4765-b4bd-31e1456eb97b
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- ListPad Control
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ListPad Control

The ListPad control is used on a list view taskpad DHTML page to display a list-view control that contains items from an IResultData result list.

The MMC list view taskpad templates use the ListPad control. To create a custom taskpad that displays items from an IResultData result list, the ListPad control should be placed as an object on the taskpad HTML page.

## Class ID

289228DE-A31E-11D1-A19C-0000F875B132

## Properties and Methods

The ListPad control has no properties or methods.

## Example

The following HTML code example embeds the ListPad control on an HTML page.


```C++
<object id="ListView"
    width="100%"
    height="100%"
    classid="clsid:289228DE-A31E-11D1-A19C-0000F875B132">
</object>
```



 

 




