---
title: IME mode model changes
description: IME mode model changed from per-user to per-thread
ms.assetid: C9717AF2-7055-47CA-8F8F-BC0F483B2259
ms.topic: article
ms.date: 05/31/2018
---

# IME mode model changed from per-user to per-thread

## Platforms

<dl> Clients - Windows 8.1  
Servers - Windows Server 2012 R2  
</dl>

## Description

In Windows 8, the IME Conversion Mode and IME Sentence Mode were based on the User context, and changing the mode of an application affected all other applications. This behavior could be disabled by using the "Let me set a different input method for each app window" setting in the advanced settings section of the language control panel.

In order to improve compatibility, in Windows 8.1 the modes are stored in an Input context regardless of how the "Let me set a different input method for each app window" control is set. In Windows 8.1, the "Let me set a different input method for each app window" setting affects only the selection of the input method itself.

At application start up, the IME mode is set to the following defaults:



| &nbsp;   | Software input panel | Hardware keyboard |
|----------|----------------------|-------------------|
| KOR, JPN | On                   | Off               |
| CHS,CHT  | On                   | On                |



 

## Manifestations

When a user changes the IME mode on an application, the change doesn’t affect other applications.

## Resources

-   [IME Conversion Mode Values](../intl/ime-conversion-mode-values.md)
-   [IME Sentence Mode Values](../intl/ime-sentence-mode-values.md)

 

 