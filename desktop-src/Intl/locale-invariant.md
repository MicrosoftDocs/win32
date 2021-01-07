---
description: LOCALE\_INVARIANT
ms.assetid: d37df17d-8cd5-4481-bee2-062cf9d78e9b
title: LOCALE_INVARIANT
ms.topic: article
ms.date: 05/31/2018
---

# LOCALE\_INVARIANT

**Windows XP:** The locale used for operating system-level functions that require consistent and locale-independent results. For example, the invariant locale is used when an application compares character strings using the [**CompareString**](/windows/win32/api/stringapiset/nf-stringapiset-comparestringw) function and expects a consistent result regardless of the user locale. The settings of the invariant locale are similar to those for English (United States) but should not be used to display formatted data. Typically, an application does not use LOCALE\_INVARIANT because it expects the results of an action to depend on the rules governing each individual locale. The value of LOCALE\_INVARIANT IS 0x007f.

 

 
