---
title: Special Cookie Values
description: Shows the use of cookies of special types.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 63c25455-7b0e-4049-a204-157f83d3aa5a
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- special cookie values MMC
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Special Cookie Values

In certain situations, the **MMC\_COOKIE** value that MMC passes in a call to the snap-in's [**IComponent::QueryDataObject**](/windows/win32/Mmc/nf-mmc-icomponent-querydataobject?branch=master) method is a special type of cookie.

To determine if the cookie value is that of a special cookie, the snap-in can use the [**IS\_SPECIAL\_COOKIE**](/windows/win32/Mmc/nf-mmc-is_special_cookie?branch=master) macro. A return value of **TRUE** indicates that the cookie value is that of a special cookie type. The snap-in can then handle the data object appropriately based on the specific value of the cookie.

The special cookie can take two values: MMC\_MULTI\_SELECT\_COOKIE and MMC\_WINDOW\_COOKIE. These values are reserved by MMC and should never be used by snap-ins to identify any scope or result items that they insert. These values are defined in the mmc.idl file.

The MMC\_MULTI\_SELECT\_COOKIE value is used during multiselection. MMC passes this value to the snap-in to request a pointer to a multiselection data object. For more information about multiselection data objects, see [Multiselection](multiselection.md).

The MMC\_WINDOW\_COOKIE value is used for windows created programmatically in calls to the [**IConsole2::NewWindow**](iconsole2-newwindow.md) method and with the *lOptions* parameter set to MMC\_NW\_OPTION\_CUSTOMTITLE. MMC passes the value to request a pointer to the data object that supplies the string that represents the snap-in's static node in the title bar.

 

 




