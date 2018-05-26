---
title: MMCN\_BTN\_CLICK message
description: Sent to the snap-ins IComponent, IComponentData, or IExtendControlbar implementation when a user clicks a toolbar button.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 166488ab-942f-4e25-9007-b9b79aac5995
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- MMCN_BTN_CLICK message MMC
topic_type:
- apiref
api_name:
- MMCN_BTN_CLICK
api_location:
- Mmc.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MMCN\_BTN\_CLICK message

The **MMCN\_BTN\_CLICK** notification message is sent to the snap-in's [**IComponent**](/windows/win32/Mmc/ns-wmidata-_msmcaevent_pcicomponenterror?branch=master), [**IComponentData**](/windows/win32/Mmc/nn-mmc-icomponentdata?branch=master), or [**IExtendControlbar**](/windows/win32/Mmc/nn-mmc-iextendcontrolbar?branch=master) implementation when a user clicks a toolbar button.

## Parameters

<dl> <dt>

*lpDataObject* \[in\]
</dt> <dd>

For [**IComponent::Notify**](/windows/win32/Mmc/nf-mmc-icomponent-notify?branch=master) or [**IComponentData::Notify**](/windows/win32/Mmc/nf-mmc-icomponentdata-notify?branch=master), the pointer to the data object of the currently selected scope or result item. Not used by [**IExtendControlBar::ControlbarNotify**](/windows/win32/Mmc/nf-mmc-iextendcontrolbar-controlbarnotify?branch=master).

</dd> <dt>

*arg* 
</dt> <dd>

For [**IComponent::Notify**](/windows/win32/Mmc/nf-mmc-icomponent-notify?branch=master) or [**IComponentData::Notify**](/windows/win32/Mmc/nf-mmc-icomponentdata-notify?branch=master), this parameter must be 0 (zero). For [**IExtendControlBar::ControlbarNotify**](/windows/win32/Mmc/nf-mmc-iextendcontrolbar-controlbarnotify?branch=master), this parameter is the data object of the currently selected scope or result item.

</dd> <dt>

*param* \[in\]
</dt> <dd>

For [**IComponent::Notify**](/windows/win32/Mmc/nf-mmc-icomponent-notify?branch=master) or [**IComponentData::Notify**](/windows/win32/Mmc/nf-mmc-icomponentdata-notify?branch=master), this parameter is the verb that was selected (one of the [**MMC\_CONSOLE\_VERB**](/windows/win32/Mmc/ne-mmc-_mmc_console_verb?branch=master) enumerations). For [**IExtendControlBar::ControlbarNotify**](/windows/win32/Mmc/nf-mmc-iextendcontrolbar-controlbarnotify?branch=master), this parameter is the snap-in-defined command ID of the selected toolbar button.

</dd> </dl>

## Return value

<dl> <dt>

**S\_OK**
</dt> <dd>

The snap-in successfully handled the notification.

</dd> <dt>

**S\_FALSE**
</dt> <dd>

The snap-in does not handle the notification. MMC then performs a default operation for the notification.

</dd> </dl>

## Remarks

For a custom view (custom OCX or webpage) for which the MMC\_VERB\_PROPERTIES verb is enabled, when the user clicks the Properties button on the console toolbar, MMC sends the snap-in an **MMCN\_BTN\_CLICK** notification message. The notification's *param* argument contains the MMC\_VERB\_PROPERTIES enumerator value, and its *lpDataObject* argument contains DOBJ\_CUSTOMOCX or DOBJ\_CUSTOMWEB.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                         |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                   |
| Header<br/>                   | <dl> <dt>Mmc.h</dt> </dl> |



## See also

<dl> <dt>

[**IComponent::Notify**](/windows/win32/Mmc/nf-mmc-icomponent-notify?branch=master)
</dt> <dt>

[**IComponentData::Notify**](/windows/win32/Mmc/nf-mmc-icomponentdata-notify?branch=master)
</dt> <dt>

[**IExtendControlbar::ControlbarNotify**](/windows/win32/Mmc/nf-mmc-iextendcontrolbar-controlbarnotify?branch=master)
</dt> </dl>

 

 





