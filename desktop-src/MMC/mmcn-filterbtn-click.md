---
title: MMCN\_FILTERBTN\_CLICK message
description: The MMCN\_FILTERBTN\_CLICK notification is introduced in MMC 1.2.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '82a1d00a-5787-4fad-b3c5-cbcf51a25338'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["MMCN_FILTERBTN_CLICK message MMC"]
topic_type:
- apiref
api_name:
- MMCN_FILTERBTN_CLICK
api_location:
- Mmc.h
api_type:
- HeaderDef
---

# MMCN\_FILTERBTN\_CLICK message

The **MMCN\_FILTERBTN\_CLICK** notification is introduced in MMC 1.2.

The **MMCN\_FILTERBTN\_CLICK** notification message is sent to the snap-in's [**IComponent**](icomponent.md) implementation when the user clicks the filter button on the header control of a filtered view. The snap-in responds to this notification by that displays a user interface element that allows the user to change the filter operator. Be aware that the filtered view mode does not affect the sort settings on the filtered list.

## Parameters

<dl> <dt>

*lpDataObject* \[in\]
</dt> <dd>

Not used (NULL).

</dd> <dt>

*arg* \[in\]
</dt> <dd>

ID of the column whose filter button was clicked.

</dd> <dt>

*param* \[in\]
</dt> <dd>

A pointer to a [**RECT**](https://msdn.microsoft.com/library/windows/desktop/dd162897) structure (**LPRECT**) with the coordinates of the filter button. The snap-in can use the contents of the structure to position the user interface element (usually a menu) used to change the filter operator.

</dd> </dl>

## Return value

<dl> <dt>

**S\_OK**
</dt> <dd>

The snap-in modified the filter operator and generates an [**MMCN\_FILTER\_CHANGE**](mmcn-filter-change.md) event.

</dd> <dt>

**S\_FALSE**
</dt> <dd>

The snap-in did not change the filter operator, or has already updated the filtered list.

</dd> </dl>

## Remarks

After the user's changes to the filter operator have been handled by the snap-in, the message handler returns **S\_OK** to generate an [**MMCN\_FILTER\_CHANGE**](mmcn-filter-change.md) notification with *arg* set to MFCC\_VALUE\_CHANGE and *param* set to the column ID of the affected filtered view column.

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

[**MMCN\_FILTER\_CHANGE**](mmcn-filter-change.md)
</dt> <dt>

[**MMC\_FILTER\_CHANGE\_CODE**](mmc-filter-change-code.md)
</dt> <dt>

[Adding Filtered Views](adding-filtered-views.md)
</dt> </dl>

 

 





