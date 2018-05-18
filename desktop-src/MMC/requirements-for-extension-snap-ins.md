---
title: Requirements for Extension Snap-ins
description: Extension snap-ins are COM in-process DLLs that implement and expose MMC interfaces such as IExtendContextMenu and IExtendControlbar.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'a893c4a7-1d11-4afd-9490-fea79b54e41e'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["requirements for extension snap-ins MMC", "requirements MMC , extension snap-ins"]
---

# Requirements for Extension Snap-ins

Extension snap-ins are COM in-process DLLs that implement and expose MMC interfaces such as [**IExtendContextMenu**](iextendcontextmenu.md) and [**IExtendControlbar**](iextendcontrolbar.md).

Extension snap-ins have three requirements:

-   Extension snap-ins must implement the appropriate MMC interfaces and handle the MMC notifications that are sent in response to user actions.
-   Extension snap-ins must register themselves in several places in the registry. This is discussed in detail in [Registration Requirements for Extension Snap-ins](registration-requirements-for-extension-snap-ins.md).
-   Extension snap-ins must be aware of and support the clipboard formats published by any primary snap-ins whose node types they extend.

## Related topics

<dl> <dt>

[Implementing MMC Interfaces in Extension Snap-ins](implementing-mmc-interfaces-in-extension-snap-ins.md)
</dt> <dt>

[Registration Requirements for Extension Snap-ins](registration-requirements-for-extension-snap-ins.md)
</dt> <dt>

[Working with Extension Snap-ins](working-with-extension-snap-ins.md)
</dt> </dl>

 

 




