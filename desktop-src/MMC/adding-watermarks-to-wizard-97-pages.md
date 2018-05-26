---
title: Adding Watermarks to Wizard 97 Pages
description: This feature is introduced in MMC 1.1.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a5f1a8bc-5867-48f0-8342-fae47be08c11
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- adding watermarks to Wizard 97 pages MMC
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Adding Watermarks to Wizard 97 Pages

This feature is introduced in MMC 1.1.

By implementing [**IExtendPropertySheet2::GetWatermarks**](/windows/win32/Mmc/nf-mmc-iextendpropertysheet2-getwatermarks?branch=master), you can specify the bitmaps used for the watermark on [*Welcome*](w-gly.md#mmc-welcome-page-gly) and [*Completion pages*](c-gly.md#mmc-completion-page-gly) and the header on interior pages.

By setting the pszHeaderTitle and pszHeaderSubTitle members of the [**PROPSHEETPAGE**](/windows/win32/Prsht/nc-prsht-lpfnaddpropsheetpage?branch=master) structure, you can specify the header title and subtitle text for interior wizard pages.

## Related topics

<dl> <dt>

[Adding Wizard Pages: Interfaces](adding-wizard-pages-interfaces.md)
</dt> <dt>

[Adding Wizard Pages: Implementation Details](adding-wizard-pages-implementation-details.md)
</dt> </dl>

 

 




