---
title: MMCN\_FILTER\_CHANGE message
description: The MMCN\_FILTER\_CHANGE notification is introduced in MMC 1.2.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'b779f04c-1129-4e05-83c5-fd15ff72f1c2'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["MMCN_FILTER_CHANGE message MMC"]
topic_type:
- apiref
api_name:
- MMCN_FILTER_CHANGE
api_location:
- Mmc.h
api_type:
- HeaderDef
---

# MMCN\_FILTER\_CHANGE message

The **MMCN\_FILTER\_CHANGE** notification is introduced in MMC 1.2.

The **MMCN\_FILTER\_CHANGE** notification message is sent to the snap-in's [**IComponent**](icomponent.md) implementation when the filter value for a filtered result view column has been changed.

MMC calls [**IComponent::Notify**](icomponent-notify.md) with the **MMCN\_FILTER\_CHANGE** notification as the *event* parameter when filtering has been enabled or disabled, or when the filter value of a particular column has changed.

## Parameters

<dl> <dt>

*lpDataObject* \[in\]
</dt> <dd>

Not used (NULL).

</dd> <dt>

*arg* \[in\]
</dt> <dd>

Filter change code (see [**MMC\_FILTER\_CHANGE\_CODE**](mmc-filter-change-code.md) enumeration).

</dd> <dt>

*param* \[in\]
</dt> <dd>

Column number of changed value, if change code is MFCC\_VALUE\_CHANGE.

</dd> </dl>

## Return value

<dl> <dt>

**S\_OK**
</dt> <dd>

The snap-in successfully handled the notification.

</dd> <dt>

**S\_FALSE**
</dt> <dd>

The snap-in does not handle the notification.

</dd> </dl>

## Remarks

The snap-in receives an **MMCN\_FILTER\_CHANGE** notification with the *arg* parameter set to MFCC\_ENABLE when the user clicks the **Filtered** menu item or the snap-in programmatically sets the view mode to filtered view by setting the MMC\_VIEW\_OPTIONS\_FILTERED option in the [**IComponent::GetResultViewType**](icomponent-getresultviewtype.md) method.

The snap-in receives an **MMCN\_FILTER\_CHANGE** notification with the *arg* parameter set to MFCC\_DISABLE when the user or the snap-in turns off filtering.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                         |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                   |
| Header<br/>                   | <dl> <dt>Mmc.h</dt> </dl> |



## See also

<dl> <dt>

[**IComponent::Notify**](icomponent-notify.md)
</dt> <dt>

[**IHeaderCtrl2**](iheaderctrl2.md)
</dt> <dt>

[**MMC\_FILTER\_CHANGE\_CODE**](mmc-filter-change-code.md)
</dt> <dt>

[Adding Filtered Views](adding-filtered-views.md)
</dt> </dl>

 

 





