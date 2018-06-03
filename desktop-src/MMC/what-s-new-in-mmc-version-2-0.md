---
title: MMC Version 2.0
description: Describes the features that are new in MMC Version 2.0.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d7b0fec6-84d2-4558-ac22-4508fd9541eb
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- what's new in MMC version 2.0 MMC 2.0
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MMC Version 2.0

The following items are part of MMC version 2.0, that is included with the Windows and Windows Server operating systems. The MMC 3.0 SDK is a successor to the MMC 2.0 SDK and provides a managed infrastructure for creating snap-ins.

## New Features

[Console File and User Mode Changes](console-file-and-user-mode-changes.md)

[Extending Views](extending-views.md)

[MMC 2.0 Automation Object Model](mmc-2-0-automation-object-model.md)

[Providing MUI-Compliant Help Files](providing-mui-compliant-help-files.md)

[Registering Snap-in Names](registering-snap-in-names.md)

[Restoring Result Views](restoring-result-views.md)

[Retrieving a Snap-in's List View Results](retrieving-a-snap-in-s-list-view-results.md)

[Running 32-bit and 64-bit Snap-ins in 64-bit Windows](running-32-bit-and-64-bit-snap-ins-in-64-bit-windows.md)

[Supporting Visual Styles in Snap-ins](supporting-visual-styles-in-snap-ins.md)

[TBSTATE\_WRAP Change](tbstate-wrap-change.md)

[Using MMC 2.0 Drag-and-Drop Features](using-mmc-2-0-drag-and-drop-features.md)

[Using the Extended View Extension](using-the-extended-view-extension.md)

## New Interfaces

[**IComponent2**](/windows/desktop/api/Mmc/nn-mmc-icomponent2)

[**IComponentData2**](/windows/desktop/api/Mmc/nn-mmc-icomponentdata2)

[**IConsole3**](/windows/desktop/api/Mmc/nn-mmc-iconsole3)

[**IConsolePower**](/windows/desktop/api/Mmc/nn-mmc-iconsolepower)

[**IConsolePowerSink**](/windows/desktop/api/Mmc/nn-mmc-iconsolepowersink)

[**IContextMenuCallback2**](/windows/desktop/api/Mmc/nn-mmc-icontextmenucallback2)

[**IExtendView**](/windows/desktop/api/Mmc/nn-mmc-iextendview)

[**IMMCVersionInfo**](/windows/desktop/api/Mmc/nn-mmc-immcversioninfo)

[**INodeProperties**](/windows/desktop/api/Mmc/nn-mmc-inodeproperties)

[**IResultData2**](/windows/desktop/api/Mmc/nn-mmc-iresultdata2)

[**ISnapinProperties**](/windows/desktop/api/Mmcobj/nn-mmcobj-isnapinproperties)

[**ISnapinPropertiesCallback**](/windows/desktop/api/Mmcobj/nn-mmcobj-isnapinpropertiescallback)

[**IViewExtensionCallback**](/windows/desktop/api/Mmc/nn-mmc-iviewextensioncallback)

## New Automation Objects and Collections

[**AppEventsDHTMLConnector Object**](appeventsdhtmlconnector-object.md)

[**Application Object**](application-object.md)

[**Column Object**](column-object.md)

[**Columns Collection**](columns-collection.md)

[**ContextMenu Object**](contextmenu-object.md)

[**Document Object**](document-object.md)

[**Extension Object**](extension-object.md)

[**Extensions Collection**](extensions-collection.md)

[**Frame Object**](frame-object.md)

[**MenuItem Object**](menuitem-object.md)

[**Node Object**](node-object.md)

[**Nodes Collection**](nodes-collection.md)

[**Properties Collection**](properties-collection.md)

[**Property Object**](property-object.md)

[**ScopeNamespace Object**](scopenamespace-object.md)

[**SnapIn Object**](snapin-object.md)

[**SnapIns Collection**](snapins-collection.md)

[**View Object**](view-object.md)

[**Views Collection**](views-collection.md)

## New Structures

[**CONTEXTMENUITEM2**](/windows/desktop/api/Mmc/ns-mmc-_contextmenuitem2)

[**MMC\_EXT\_VIEW\_DATA**](/windows/desktop/api/Mmc/ns-mmc-_mmc_ext_view_data)

[**MMC\_SNAPIN\_PROPERTY**](/windows/desktop/api/Mmcobj/ns-mmcobj-_mmc_snapin_property)

[**RESULT\_VIEW\_TYPE\_INFO**](/windows/desktop/api/Mmc/ns-mmc-_result_view_type_info)

## New Enumerations

[**ColumnSortOrder**](/windows/desktop/api/MmcObj/ne-mmcobj-columnsortorder)

[**DocumentMode**](/windows/desktop/api/MmcObj/ne-mmcobj-documentmode)

[**ExportListOptions**](/windows/desktop/api/MmcObj/ne-mmcobj-exportlistoptions)

[**ListViewMode**](/windows/desktop/api/MmcObj/ne-mmcobj-listviewmode)

[**MMC\_PROPERTY\_ACTION**](/windows/desktop/api/Mmcobj/ne-mmcobj-_mmc_property_action)

[**MMC\_VIEW\_TYPE**](/windows/desktop/api/Mmc/ne-mmc-_mmc_view_type)

[**ViewOptions**](/windows/desktop/api/MmcObj/ne-mmcobj-viewoptions)

> [!Note]  
> The [**ColumnSortOrder**](/windows/desktop/api/MmcObj/ne-mmcobj-columnsortorder), [**DocumentMode**](/windows/desktop/api/MmcObj/ne-mmcobj-documentmode), [**ExportListOptions**](/windows/desktop/api/MmcObj/ne-mmcobj-exportlistoptions), [**ListViewMode**](/windows/desktop/api/MmcObj/ne-mmcobj-listviewmode) and [**ViewOptions**](/windows/desktop/api/MmcObj/ne-mmcobj-viewoptions) enumerations are part of the [MMC 2.0 Automation Object Model](mmc-2-0-automation-object-model.md).

 

## Related topics

<dl> <dt>

[Miscellaneous MMC 2.0 Information](miscellaneous-mmc-2-0-information.md)
</dt> <dt>

[MMC 2.0 Release Information](mmc-2-0-release-information.md)
</dt> </dl>

 

 




