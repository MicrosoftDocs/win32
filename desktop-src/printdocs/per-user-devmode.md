---
description: A user can specify the default document settings for a printer. This is called the per-user DEVMODE because it only affects the defaults for a particular user, and the information for each printer is defined in a separate DEVMODE structure.
ms.assetid: f791f847-c31e-4a06-93cb-49117d8f0cb8
title: Per-User DEVMODE
ms.topic: article
ms.date: 05/31/2018
---

# Per-User DEVMODE

A user can specify the default document settings for a printer. This is called the *per-user DEVMODE* because it only affects the defaults for a particular user, and the information for each printer is defined in a separate [**DEVMODE**](/windows/win32/api/wingdi/ns-wingdi-devmodea) structure.

To set the per-user DEVMODE, call [**SetPrinter**](setprinter.md) with either the [**PRINTER\_INFO\_2**](printer-info-2.md) or the [**PRINTER\_INFO\_9**](printer-info-9.md) structure. To reset the per-user DEVMODE to the global default [**DEVMODE**](/windows/win32/api/wingdi/ns-wingdi-devmodea), call **SetPrinter** with the [**PRINTER\_INFO\_8**](printer-info-8.md) structure.

 

 



