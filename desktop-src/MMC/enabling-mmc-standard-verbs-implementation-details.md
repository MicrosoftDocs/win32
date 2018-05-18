---
title: Enabling MMC Standard Verbs Implementation Details
description: Enabling MMC Standard Verbs Implementation Details
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'edb6eeea-8c11-4ff8-8a80-692465c0acd2'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["enabling MMC standard verbs, implementation details"]
---

# Enabling MMC Standard Verbs: Implementation Details

**To enable standard verbs**

1.  Handle the [**MMCN\_SELECT**](mmcn-select.md) notification message, which MMC sends to indicate which item in the scope pane is currently selected.
2.  In the notification handler, call the [**IConsole2::QueryConsoleVerb**](iconsole2-queryconsoleverb.md) method to request a pointer to the MMC [**IConsoleVerb**](iconsoleverb.md) interface implementation.
3.  Use the returned interface pointer to call [**IConsoleVerb::SetVerbState**](iconsoleverb-setverbstate.md), one time for each standard verb to enable for the selected item. Also call other [**IConsoleVerb**](iconsoleverb.md) verbs as necessary.

## Related topics

<dl> <dt>

[Drag and Drop](drag-and-drop.md)
</dt> <dt>

[Enabling MMC Standard Verbs](enabling-mmc-standard-verbs.md)
</dt> </dl>

 

 




