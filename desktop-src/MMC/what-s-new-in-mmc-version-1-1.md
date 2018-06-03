---
title: MMC Version 1.1
description: Describes the features that are new in MMC version 1.1.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ccd2485d-2b4f-4f10-932a-7291893a9bb9
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- MMC version 1.1 MMC
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MMC Version 1.1

The following items are new in MMC version 1.1, which shipped with Microsoft SQL Server 7.0 and Microsoft Systems Management Server 2.0.

## New Features

[Taskpads](using-taskpads.md)

[Dynamic Extensions](adding-dynamic-extensions.md)

[Required Extensions](adding-required-extensions.md)

[HTML Help Support](adding-html-help-support.md)

[Programmatic Expansion of Scope Items](programmatic-expansion-of-scope-items.md)

[Adding Wizard 97 Pages](adding-wizard-pages.md)

[Adding Watermarks to Wizard 97 Pages](adding-watermarks-to-wizard-97-pages.md)

[Status Bar Text](status-bar-text.md)

[Programmatic New Window Creation](programmatic-new-window-creation.md)

[MMC Taskpad Controls and Objects](mmc-taskpad-controls-and-objects.md)

## New Interfaces

[**IConsole2**](/windows/desktop/api/Mmc/nn-mmc-iconsole2)

[**IConsoleNameSpace2**](/windows/desktop/api/Mmc/nn-mmc-iconsolenamespace2)

[**IDisplayHelp**](/windows/desktop/api/Mmc/nn-mmc-idisplayhelp)

[**IEnumTASK**](/windows/desktop/api/Mmc/nn-mmc-ienumtask)

[**IExtendPropertySheet2**](/windows/desktop/api/Mmc/nn-mmc-iextendpropertysheet2)

[**IExtendTaskPad**](/windows/desktop/api/Mmc/nn-mmc-iextendtaskpad)

[**IHeaderCtrl2**](/windows/desktop/api/Mmc/nn-mmc-iheaderctrl2)

[**IRequiredExtensions**](/windows/desktop/api/Mmc/nn-mmc-irequiredextensions)

[**ISnapinHelp2**](/windows/desktop/api/Mmc/nn-mmc-isnapinhelp2)

[**IStringTable**](/windows/desktop/api/Mmc/nn-mmc-istringtable)

## New Exported Functions

[**MMCPropertyHelp**](/windows/desktop/api/Mmc/nf-mmc-mmcpropertyhelp)

## New Structures

[**MMC\_EXPANDSYNC\_STRUCT**](/windows/desktop/api/Mmc/ns-mmc-_mmc_expandsync_struct)

[**MMC\_LISTPAD\_INFO**](/windows/desktop/api/Mmc/ns-mmc-_mmc_listpad_info)

[**MMC\_RESTORE\_VIEW**](/windows/desktop/api/Mmc/ns-mmc-_mmc_restore_view)

[**MMC\_TASK**](/windows/desktop/api/Mmc/ne-mmc-_mmc_task_display_type)

[**MMC\_TASK\_DISPLAY\_BITMAP**](/windows/desktop/api/Mmc/ns-mmc-_mmc_task_display_bitmap)

[**MMC\_TASK\_DISPLAY\_OBJECT**](/windows/desktop/api/Mmc/ns-mmc-_mmc_task_display_object)

[**MMC\_TASK\_DISPLAY\_SYMBOL**](/windows/desktop/api/Mmc/ns-mmc-_mmc_task_display_symbol)

[**PROPSHEETPAGE**](/windows/desktop/api/Prsht/nc-prsht-lpfnaddpropsheetpage)

[**SMMCDynamicExtensions**](https://www.bing.com/search?q=**SMMCDynamicExtensions**)

[**SNodeID**](/windows/desktop/api/Mmc/ns-mmc-_snodeid)

## New Enumerations

[**MMC\_ACTION\_TYPE**](/windows/desktop/api/Mmc/ne-mmc-_mmc_action_type)

[**MMC\_CONSOLE\_VERB**](/windows/desktop/api/Mmc/ne-mmc-_mmc_console_verb) (Values added to the existing enumeration)

[**MMC\_TASK\_DISPLAY\_TYPE**](/windows/desktop/api/Mmc/ne-mmc-_mmc_task_display_type)

## New Notifications

[**MMCN\_EXPANDSYNC**](mmcn-expandsync.md)

[**MMCN\_LISTPAD**](mmcn-listpad.md)

[**MMCN\_PRELOAD**](mmcn-preload.md)

[**MMCN\_PRINT**](mmcn-print.md)

[**MMCN\_RESTORE\_VIEW**](mmcn-restore-view.md)

## New Clipboard Formats

[**CCF\_MMC\_DYNAMIC\_EXTENSIONS**](ccf-mmc-dynamic-extensions.md)

[**CCF\_NODEID**](ccf-nodeid.md)

[**CCF\_SNAPIN\_PRELOADS**](ccf-snapin-preloads.md)

## New View Options

[**MMC\_VIEW\_OPTIONS\_USEFONTLINKING**](/windows/desktop/api/Mmc/nf-mmc-icomponent-getresultviewtype)

 

 




