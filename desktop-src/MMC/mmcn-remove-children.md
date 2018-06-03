---
title: MMCN\_REMOVE\_CHILDREN message
description: The MMCN\_REMOVE\_CHILDREN notification message is sent to the snap-in's IComponentData Notify method to inform the snap-in that it must delete all the child items (the entire subtree) it has added below the specified item.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2540fedc-2ee5-44ed-a1bb-4da3eb2146c9
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- MMCN_REMOVE_CHILDREN message MMC
topic_type:
- apiref
api_name:
- MMCN_REMOVE_CHILDREN
api_location:
- Mmc.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MMCN\_REMOVE\_CHILDREN message

The **MMCN\_REMOVE\_CHILDREN** notification message is sent to the snap-in's [**IComponentData::Notify**](/windows/desktop/api/Mmc/nf-mmc-icomponentdata-notify) method to inform the snap-in that it must delete all the child items (the entire subtree) it has added below the specified item.

## Parameters

<dl> <dt>

*lpDataObject* \[in\]
</dt> <dd>

A pointer to the data object of the scope item whose child items need to be removed.

</dd> <dt>

*arg* 
</dt> <dd>

A value that specifies the HSCOPEITEM of the item whose child items need to be deleted.

</dd> <dt>

*param* 
</dt> <dd>

Not used.

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

The snap-in may use [**IConsoleNameSpace2::GetChildItem**](https://www.bing.com/search?q=**IConsoleNameSpace2::GetChildItem**) and [**IConsoleNameSpace2::GetNextItem**](https://www.bing.com/search?q=**IConsoleNameSpace2::GetNextItem**) to traverse the tree and determine the child items to be deleted.

The snap-in is only required to release its own resources for the deleted child items. It is not required to call [**IConsoleNameSpace2::DeleteItem**](https://www.bing.com/search?q=**IConsoleNameSpace2::DeleteItem**) to cause MMC to delete the items.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                         |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                   |
| Header<br/>                   | <dl> <dt>Mmc.h</dt> </dl> |



## See also

<dl> <dt>

[**IComponentData::Notify**](/windows/desktop/api/Mmc/nf-mmc-icomponentdata-notify)
</dt> </dl>

 

 





