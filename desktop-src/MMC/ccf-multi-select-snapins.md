---
title: CCF\_MULTI\_SELECT\_SNAPINS clipboard format
description: The CCF\_MULTI\_SELECT\_SNAPINS clipboard format enables MMC to pass a list of multiselection data objects during some multiselection operations.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 56419e7c-6583-4307-9b47-779914a05813
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- CCF_MULTI_SELECT_SNAPINS clipboard format MMC
topic_type:
- apiref
api_name:
- CCF_MULTI_SELECT_SNAPINS
api_location:
- Mmc.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CCF\_MULTI\_SELECT\_SNAPINS clipboard format

The CCF\_MULTI\_SELECT\_SNAPINS clipboard format enables MMC to pass a list of multiselection data objects during some multiselection operations. MMC creates a composite data object that contains the list of multiselection data objects. Snap-ins can call the **GetData** method of the composite data object and specify the CCF\_MULTI\_SELECT\_SNAPINS clipboard format to retrieve the list of multiselection data objects.

## Data Format

[**SMMCDataObjects**](/windows/win32/Mmc/ns-mmc-_smmcdataobjects?branch=master) structure.

## Remarks

The SMMCDataObjects structure contains the array of pointers to the multiselection data objects of each snap-in represented in the set of selected items in the result pane.

If there are n snap-ins whose objects are selected in the result pane, these n data objects will be passed in memory allocated by GlobalAlloc. The first DWORD contains the number of snap-ins; this will be followed by n pointers to the multiselection data objects.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                         |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                   |
| Header<br/>                   | <dl> <dt>Mmc.h</dt> </dl> |



## See also

<dl> <dt>

[**SMMCDataObjects**](/windows/win32/Mmc/ns-mmc-_smmcdataobjects?branch=master)
</dt> <dt>

[Multiselection](multiselection.md)
</dt> </dl>

 

 





