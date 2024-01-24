---
description: The printer escapes provided by 16-bit Windows allowed access special device features.
ms.assetid: 4bdd1d47-8cf4-4088-aec8-88193e71a828
title: Printer Escapes
ms.topic: article
ms.date: 05/31/2018
---

# Printer Escapes

The printer escapes provided by 16-bit Windows allowed access special device features. Most of these escapes are obsolete, but a few are provided to simplify the porting of 16-bit Windows-based applications. GDI supports a complete set of path functions that applications can use instead of the escapes to draw paths on any device. For a list of functions that replace some of the escapes, see the [**Escape**](/windows/desktop/api/Wingdi/nf-wingdi-escape) function.

Of the 64 original printer escapes, only **QUERYESCSUPPORT** and **PASSTHROUGH** can be used.

There is also an extended escape function called [**ExtEscape**](/windows/desktop/api/Wingdi/nf-wingdi-extescape). This function allows applications to access capabilities of a particular device not directly available through GDI.

 

 



