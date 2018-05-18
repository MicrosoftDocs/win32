---
title: MMCN\_RENAME message
description: The MMCN\_RENAME notification message is sent to either the snap-in's IComponentData or IComponent implementation depending on the type of item (scope or result) that must be renamed.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '1a77e563-e469-466e-b61a-e127dfb19c1a'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["MMCN_RENAME message MMC"]
topic_type:
- apiref
api_name:
- MMCN_RENAME
api_location:
- Mmc.h
api_type:
- HeaderDef
---

# MMCN\_RENAME message

The **MMCN\_RENAME** notification message is sent to either the snap-in's [**IComponentData**](icomponentdata.md) or [**IComponent**](icomponent.md) implementation depending on the type of item (scope or result) that must be renamed.

## Parameters

<dl> <dt>

*lpDataObject* 
</dt> <dd>

A pointer to the data object of the scope or result item to be renamed.

</dd> <dt>

*arg* 
</dt> <dd>

Not used.

</dd> <dt>

*param* 
</dt> <dd>

The new name. The following line of code shows how the parameter can be used:

LPOLESTR *pszNewName* = (LPOLESTR)*param*;

</dd> </dl>

## Return value

<dl> <dt>

**S\_OK**
</dt> <dd>

To allow the rename.

</dd> <dt>

**S\_FALSE**
</dt> <dd>

To disallow the rename.

</dd> </dl>

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                         |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                   |
| Header<br/>                   | <dl> <dt>Mmc.h</dt> </dl> |



 

 





