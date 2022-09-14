---
description: CSingleFilterTerminal is an additional terminal base class applicable to both static and dynamic terminals.
ms.assetid: d423438f-1324-4df3-beaa-fdef325fac2e
title: CSingleFilterTerminal
ms.topic: article
ms.date: 05/31/2018
---

# CSingleFilterTerminal

**CSingleFilterTerminal** is an additional terminal base class applicable to both static and dynamic terminals. It is derived from [**CBaseTerminal**](cbaseterminal.md) and makes the implementation more specific by assuming that the terminal has a single DirectShow filter. When this condition is met, deriving a terminal implementation from **CSingleFilterTerminal** is much easier than deriving from **CBaseTerminal**.

Defined in MSPterm.h.

 

 



