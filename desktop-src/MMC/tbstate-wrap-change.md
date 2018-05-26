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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# TBSTATE\_WRAP Change

The TBSTATE\_WRAP flag is not supported by MMC. The [**MMCBUTTON**](/windows/win32/Mmc/ns-mmc-_mmcbutton?branch=master) structure should not have its **fsType** member set to include the TBSTATE\_WRAP flag. The [**IToolbar::AddButtons**](/windows/win32/Mmc/nf-mmc-itoolbar-addbuttons?branch=master), [**IToolbar::InsertButton**](/windows/win32/Mmc/nf-mmc-itoolbar-insertbutton?branch=master), and [**IToolbar::SetButtonState**](/windows/win32/Mmc/nf-mmc-itoolbar-setbuttonstate?branch=master) methods use the caller's **fsType** value when managing a toolbar button. In MMC 2.0, setting the TBSTATE\_WRAP flag is ignored; in earlier versions of MMC, setting the TBSTATE\_WRAP flag for a button causes the next toolbar button to appear in the next line.

## Related topics

<dl> <dt>

[**MMCBUTTON**](/windows/win32/Mmc/ns-mmc-_mmcbutton?branch=master)
</dt> <dt>

[**IToolbar::AddButtons**](/windows/win32/Mmc/nf-mmc-itoolbar-addbuttons?branch=master)
</dt> <dt>

[**IToolbar::InsertButton**](/windows/win32/Mmc/nf-mmc-itoolbar-insertbutton?branch=master)
</dt> <dt>

[**IToolbar::SetButtonState**](/windows/win32/Mmc/nf-mmc-itoolbar-setbuttonstate?branch=master)
</dt> </dl>

 

 




