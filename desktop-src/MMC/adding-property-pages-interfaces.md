---
title: Adding Property Pages Interfaces
description: MMC provides snap-in developers with the following interfaces for working with property pages
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d153dcb6-ae09-4949-a62b-4033dd245c0e
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- property pages MMC , interfaces
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Adding Property Pages: Interfaces

MMC provides snap-in developers with the following interfaces for working with property pages:

-   [**IExtendPropertySheet2**](/windows/win32/Mmc/nn-mmc-iextendpropertysheet2?branch=master)
-   [**IPropertySheetProvider**](/windows/win32/Mmc/nn-mmc-ipropertysheetprovider?branch=master)
-   [**IPropertySheetCallback**](/windows/win32/Mmc/nn-mmc-ipropertysheetcallback?branch=master)

## Other Property Page Constructs

The following constructs are also used for working with property pages:

-   [**MMCN\_PROPERTY\_CHANGE**](mmcn-property-change.md) notification
-   [**PROPSHEETPAGE**](/windows/win32/Prsht/nc-prsht-lpfnaddpropsheetpage?branch=master) structure
-   [**CreatePropertySheetPage**](_win32_createpropertysheetpage_cpp) API function
-   [**MMCFreeNotifyHandle**](/windows/win32/Mmc/nf-mmc-mmcfreenotifyhandle?branch=master) function
-   [**MMCPropertyChangeNotify**](/windows/win32/Mmc/nf-mmc-mmcpropertychangenotify?branch=master) function
-   [**MMCPropertyHelp**](/windows/win32/Mmc/nf-mmc-mmcpropertyhelp?branch=master) function
-   [**MMCPropPageCallback**](/windows/win32/Mmc/nf-mmc-mmcproppagecallback?branch=master) function

## Related topics

<dl> <dt>

[Adding Property Pages: Implementation Details](adding-property-pages-implementation-details.md)
</dt> </dl>

 

 




