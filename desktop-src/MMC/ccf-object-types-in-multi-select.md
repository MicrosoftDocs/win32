---
title: CCF\_OBJECT\_TYPES\_IN\_MULTI\_SELECT clipboard format
description: The CCF\_OBJECT\_TYPES\_IN\_MULTI\_SELECT clipboard format enables a snap-in to specify the list of the node types represented by that snap-in in the set of selected items in the result pane.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 135b3526-e725-47b8-9676-b60a9456846c
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- CCF_OBJECT_TYPES_IN_MULTI_SELECT clipboard format MMC
topic_type:
- apiref
api_name:
- CCF_OBJECT_TYPES_IN_MULTI_SELECT
api_location:
- Mmc.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CCF\_OBJECT\_TYPES\_IN\_MULTI\_SELECT clipboard format

The CCF\_OBJECT\_TYPES\_IN\_MULTI\_SELECT clipboard format enables a snap-in to specify the list of the node types represented by that snap-in in the set of selected items in the result pane.

## Data Format

[**SMMCObjectTypes**](/windows/win32/Mmc/ns-mmc-_smmcobjecttypes?branch=master) structure. The structure contains the array of node type GUIDs that constitute the multiselection data object. A snap-in's multiselection data object has a list that contains each node type represented in the set of selected items for that particular snap-in in the result pane.

## Remarks

During a multiselection operation, MMC calls **IComponent::QueryDataObject** to request a pointer to the data object that will supply the list of node types (in GUID format) for all the currently selected items owned by the snap-in. MMC then calls **IDataObject::GetData** with the CCF\_OBJECT\_TYPES\_IN\_MULTI\_SELECT clipboard format on the **IDataObject** pointer returned by **IComponent::QueryDataObject**. In the snap-in's **IComponent::QueryDataObject** method implementation, the snap-in should create the multiselection data object when MMC passes MMC\_MULTI\_SELECT\_COOKIE as the *cookie* parameter.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                         |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                   |
| Header<br/>                   | <dl> <dt>Mmc.h</dt> </dl> |



## See also

<dl> <dt>

[**IComponent::QueryDataObject**](/windows/win32/Mmc/nf-mmc-icomponent-querydataobject?branch=master)
</dt> <dt>

[**SMMCObjectTypes**](/windows/win32/Mmc/ns-mmc-_smmcobjecttypes?branch=master)
</dt> </dl>

 

 





