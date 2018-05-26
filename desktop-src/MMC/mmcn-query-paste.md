---
title: MMCN\_QUERY\_PASTE message
description: Sent to a snap-ins IComponent implementation to verify that the snap-in can paste the items from the given data object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 19259852-be87-40f6-8475-26f7cc232db6
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- MMCN_QUERY_PASTE message MMC
topic_type:
- apiref
api_name:
- MMCN_QUERY_PASTE
api_location:
- Mmc.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MMCN\_QUERY\_PASTE message

The **MMCN\_QUERY\_PASTE** notification message is sent to a snap-in's [**IComponent**](/windows/win32/Mmc/ns-wmidata-_msmcaevent_pcicomponenterror?branch=master) implementation to verify that the snap-in can paste the items from the given data object.

## Parameters

<dl> <dt>

*lpDataObject* 
</dt> <dd>

The data object of the selected item provided by the snap-in.

</dd> <dt>

*arg* 
</dt> <dd>

The data object of the item(s) provided by the source snap-in that must be pasted.

</dd> <dt>

*param* 
</dt> <dd>

Not used prior to MMC 2.0. In MMC 2.0, param is a pointer to **DWORD**. To set Copy ("Copy Here") as the default drag-and-drop operation, your snap-in must set \*param equal to MMC\_DEFAULT\_OPERATION\_COPY. For more information, see [Using Copy as the Default Drag and Drop Verb](using-copy-as-the-default-drag-and-drop-verb.md).

</dd> </dl>

## Return value

<dl> <dt>

**S\_OK**
</dt> <dd>

The data can be pasted.

</dd> <dt>

**S\_FALSE**
</dt> <dd>

The data cannot be pasted.

</dd> </dl>

## Remarks

A snap-in must handle this notification and return S\_OK in order to enable the **Paste** menu item and toolbar button. Unlike other standard verbs, the state of the MMC\_VERB\_PASTE verb does not enable pasting, but informs MMC that the snap-in should be sent the **MMCN\_QUERY\_PASTE** notification.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                         |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                   |
| Header<br/>                   | <dl> <dt>Mmc.h</dt> </dl> |



## See also

<dl> <dt>

[**MMCN\_PASTE**](mmcn-paste.md)
</dt> <dt>

[**MMCN\_CANPASTE\_OUTOFPROC**](mmcn-canpaste-outofproc.md)
</dt> <dt>

[Drag and Drop](drag-and-drop.md)
</dt> <dt>

[Multiselection](multiselection.md)
</dt> <dt>

[Using Copy as the Default Drag and Drop Verb](using-copy-as-the-default-drag-and-drop-verb.md)
</dt> </dl>

 

 





