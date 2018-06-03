---
title: CCF\_MMC\_MULTISELECT\_DATAOBJECT clipboard format
description: The CCF\_MMC\_MULTISELECT\_DATAOBJECT clipboard format enables a snap-in to determine whether the data object is a multiselect snap-ins data object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 25f6dba4-4df2-4a13-b13f-0bf8cbef3879
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- CCF_MMC_MULTISELECT_DATAOBJECT clipboard format MMC
topic_type:
- apiref
api_name:
- CCF_MMC_MULTISELECT_DATAOBJECT
api_location:
- Mmc.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CCF\_MMC\_MULTISELECT\_DATAOBJECT clipboard format

The CCF\_MMC\_MULTISELECT\_DATAOBJECT clipboard format enables a snap-in to determine whether the data object is a multiselect snap-ins data object.

## Data Format

DWORD.

## Remarks

Use the **IDataObject::GetData** method to retrieve data using this clipboard format.

If the data object is a multiselect snap-ins data object, the value 1 is passed with a return of S\_OK. If the data object is not a multiselect snap-ins data object, the value 0 is passed with a return of S\_OK. In addition, if DATA\_E\_FORMATETC is returned, the snap-in is not a multiselect snap-ins data object.

Be aware that a multiselect snap-ins data object is a data object that contains the array of pointers to the multiselection data objects of each snap-in represented in the set of selected items in the result pane. The data for a multiselect snap-ins data object can be retrieved using **IDataObject::GetData** using the [**CCF\_MULTI\_SELECT\_SNAPINS**](ccf-multi-select-snapins.md) clipboard format, whose data format is the [**SMMCDataObjects**](/windows/desktop/api/Mmc/ns-mmc-_smmcdataobjects) structure.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                         |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                   |
| Header<br/>                   | <dl> <dt>Mmc.h</dt> </dl> |



## See also

<dl> <dt>

[**CCF\_MULTI\_SELECT\_SNAPINS**](ccf-multi-select-snapins.md)
</dt> <dt>

[**SMMCDataObjects**](/windows/desktop/api/Mmc/ns-mmc-_smmcdataobjects)
</dt> <dt>

[Multiselection](multiselection.md)
</dt> </dl>

 

 





