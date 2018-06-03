---
title: TBSTATE\_WRAP Change
description: The TBSTATE\_WRAP flag is not supported by MMC.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e4c356b3-7485-4294-8d28-ff1bad4d2c9d
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# TBSTATE\_WRAP Change

The TBSTATE\_WRAP flag is not supported by MMC. The [**MMCBUTTON**](/windows/desktop/api/Mmc/ns-mmc-_mmcbutton) structure should not have its **fsType** member set to include the TBSTATE\_WRAP flag. The [**IToolbar::AddButtons**](/windows/desktop/api/Mmc/nf-mmc-itoolbar-addbuttons), [**IToolbar::InsertButton**](/windows/desktop/api/Mmc/nf-mmc-itoolbar-insertbutton), and [**IToolbar::SetButtonState**](/windows/desktop/api/Mmc/nf-mmc-itoolbar-setbuttonstate) methods use the caller's **fsType** value when managing a toolbar button. In MMC 2.0, setting the TBSTATE\_WRAP flag is ignored; in earlier versions of MMC, setting the TBSTATE\_WRAP flag for a button causes the next toolbar button to appear in the next line.

## Related topics

<dl> <dt>

[**MMCBUTTON**](/windows/desktop/api/Mmc/ns-mmc-_mmcbutton)
</dt> <dt>

[**IToolbar::AddButtons**](/windows/desktop/api/Mmc/nf-mmc-itoolbar-addbuttons)
</dt> <dt>

[**IToolbar::InsertButton**](/windows/desktop/api/Mmc/nf-mmc-itoolbar-insertbutton)
</dt> <dt>

[**IToolbar::SetButtonState**](/windows/desktop/api/Mmc/nf-mmc-itoolbar-setbuttonstate)
</dt> </dl>

 

 




