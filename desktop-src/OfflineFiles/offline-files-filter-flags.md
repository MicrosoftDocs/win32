---
Description: Used in the IOfflineFilesItemFilter::GetFilterFlags method to control flag-based filtering of items.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 496126e0-d29b-415c-a3b3-44bdd9e71f78
ms.prod: windows-server-dev
ms.technology: offline-files
ms.tgt_platform: multiple
title: Offline Files Filter Flags
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Offline Files Filter Flags

Used in the [**IOfflineFilesItemFilter::GetFilterFlags**](/previous-versions/windows/desktop/api/CscObj/nf-cscobj-iofflinefilesitemfilter-getfilterflags) method to control flag-based filtering of items.

<dl> <dt>

<span id="OFFLINEFILES_ITEM_FILTER_FLAG_MODIFIED_DATA"></span><span id="offlinefiles_item_filter_flag_modified_data"></span>**OFFLINEFILES\_ITEM\_FILTER\_FLAG\_MODIFIED\_DATA**
</dt> <dd> <dl> <dt>

0x0000000000000001
</dt> <dt>



The item's data stream has been modified offline and has not yet been synchronized to the server.


</dt> </dl> </dd> <dt>

<span id="OFFLINEFILES_ITEM_FILTER_FLAG_MODIFIED_ATTRIBUTES"></span><span id="offlinefiles_item_filter_flag_modified_attributes"></span>**OFFLINEFILES\_ITEM\_FILTER\_FLAG\_MODIFIED\_ATTRIBUTES**
</dt> <dd> <dl> <dt>

0x0000000000000002
</dt> <dt>



One or more of the item's attributes have been modified offline and have not yet been synchronized to the server.


</dt> </dl> </dd> <dt>

<span id="OFFLINEFILES_ITEM_FILTER_FLAG_MODIFIED"></span><span id="offlinefiles_item_filter_flag_modified"></span>**OFFLINEFILES\_ITEM\_FILTER\_FLAG\_MODIFIED**
</dt> <dd> <dl> <dt>

0x0000000000000004
</dt> <dt>



The item's data stream or one or more of the item's attributes have been modified offline and have not yet been synchronized to the server.


</dt> </dl> </dd> <dt>

<span id="OFFLINEFILES_ITEM_FILTER_FLAG_CREATED"></span><span id="offlinefiles_item_filter_flag_created"></span>**OFFLINEFILES\_ITEM\_FILTER\_FLAG\_CREATED**
</dt> <dd> <dl> <dt>

0x0000000000000008
</dt> <dt>



The item was created offline and has not yet been synchronized to the server.


</dt> </dl> </dd> <dt>

<span id="OFFLINEFILES_ITEM_FILTER_FLAG_DELETED"></span><span id="offlinefiles_item_filter_flag_deleted"></span>**OFFLINEFILES\_ITEM\_FILTER\_FLAG\_DELETED**
</dt> <dd> <dl> <dt>

0x0000000000000010
</dt> <dt>



The item was deleted offline and has not yet been synchronized to the server.


</dt> </dl> </dd> <dt>

<span id="OFFLINEFILES_ITEM_FILTER_FLAG_DIRTY"></span><span id="offlinefiles_item_filter_flag_dirty"></span>**OFFLINEFILES\_ITEM\_FILTER\_FLAG\_DIRTY**
</dt> <dd> <dl> <dt>

0x0000000000000020
</dt> <dt>



The item has local changes that have not yet been synchronized to the server. This can mean one or more of the following   created offline, deleted offline, modified data, modified attributes.


</dt> </dl> </dd> <dt>

<span id="OFFLINEFILES_ITEM_FILTER_FLAG_SPARSE"></span><span id="offlinefiles_item_filter_flag_sparse"></span>**OFFLINEFILES\_ITEM\_FILTER\_FLAG\_SPARSE**
</dt> <dd> <dl> <dt>

0x0000000000000040
</dt> <dt>



The item is marked as sparse, meaning that it is not fully cached and is not available for offline use.


</dt> </dl> </dd> <dt>

<span id="OFFLINEFILES_ITEM_FILTER_FLAG_FILE"></span><span id="offlinefiles_item_filter_flag_file"></span>**OFFLINEFILES\_ITEM\_FILTER\_FLAG\_FILE**
</dt> <dd> <dl> <dt>

0x0000000000000080
</dt> <dt>



The item is a file.


</dt> </dl> </dd> <dt>

<span id="OFFLINEFILES_ITEM_FILTER_FLAG_DIRECTORY"></span><span id="offlinefiles_item_filter_flag_directory"></span>**OFFLINEFILES\_ITEM\_FILTER\_FLAG\_DIRECTORY**
</dt> <dd> <dl> <dt>

0x0000000000000100
</dt> <dt>



The item is a server, share, or directory.


</dt> </dl> </dd> <dt>

<span id="OFFLINEFILES_ITEM_FILTER_FLAG_PINNED_USER"></span><span id="offlinefiles_item_filter_flag_pinned_user"></span>**OFFLINEFILES\_ITEM\_FILTER\_FLAG\_PINNED\_USER**
</dt> <dd> <dl> <dt>

0x0000000000000200
</dt> <dt>



The item is pinned specifically for the calling user.


</dt> </dl> </dd> <dt>

<span id="OFFLINEFILES_ITEM_FILTER_FLAG_PINNED_OTHERS"></span><span id="offlinefiles_item_filter_flag_pinned_others"></span>**OFFLINEFILES\_ITEM\_FILTER\_FLAG\_PINNED\_OTHERS**
</dt> <dd> <dl> <dt>

0x0000000000000400
</dt> <dt>



This flag is reserved for future use.


</dt> </dl> </dd> <dt>

<span id="OFFLINEFILES_ITEM_FILTER_FLAG_PINNED_COMPUTER"></span><span id="offlinefiles_item_filter_flag_pinned_computer"></span>**OFFLINEFILES\_ITEM\_FILTER\_FLAG\_PINNED\_COMPUTER**
</dt> <dd> <dl> <dt>

0x0000000000000800
</dt> <dt>



The item is pinned for all users on the computer (by per-machine policy).


</dt> </dl> </dd> <dt>

<span id="OFFLINEFILES_ITEM_FILTER_FLAG_PINNED"></span><span id="offlinefiles_item_filter_flag_pinned"></span>**OFFLINEFILES\_ITEM\_FILTER\_FLAG\_PINNED**
</dt> <dd> <dl> <dt>

0x0000000000001000
</dt> <dt>



The item is pinned.


</dt> </dl> </dd> <dt>

<span id="OFFLINEFILES_ITEM_FILTER_FLAG_GHOST"></span><span id="offlinefiles_item_filter_flag_ghost"></span>**OFFLINEFILES\_ITEM\_FILTER\_FLAG\_GHOST**
</dt> <dd> <dl> <dt>

0x0000000000002000
</dt> <dt>



The item is currently a ghost; meaning that only namespace information is cached.


</dt> </dl> </dd> <dt>

<span id="OFFLINEFILES_ITEM_FILTER_FLAG_SUSPENDED"></span><span id="offlinefiles_item_filter_flag_suspended"></span>**OFFLINEFILES\_ITEM\_FILTER\_FLAG\_SUSPENDED**
</dt> <dd> <dl> <dt>

0x0000000000004000
</dt> <dt>



The item is currently suspended.


</dt> </dl> </dd> <dt>

<span id="OFFLINEFILES_ITEM_FILTER_FLAG_OFFLINE"></span><span id="offlinefiles_item_filter_flag_offline"></span>**OFFLINEFILES\_ITEM\_FILTER\_FLAG\_OFFLINE**
</dt> <dd> <dl> <dt>

0x0000000000008000
</dt> <dt>



The item is currently offline.


</dt> </dl> </dd> <dt>

<span id="OFFLINEFILES_ITEM_FILTER_FLAG_ONLINE"></span><span id="offlinefiles_item_filter_flag_online"></span>**OFFLINEFILES\_ITEM\_FILTER\_FLAG\_ONLINE**
</dt> <dd> <dl> <dt>

0x0000000000010000
</dt> <dt>



The item is currently online.


</dt> </dl> </dd> <dt>

<span id="OFFLINEFILES_ITEM_FILTER_FLAG_USER_WRITE"></span><span id="offlinefiles_item_filter_flag_user_write"></span>**OFFLINEFILES\_ITEM\_FILTER\_FLAG\_USER\_WRITE**
</dt> <dd> <dl> <dt>

0x0000000000020000
</dt> <dt>



This flag is reserved for future use.


</dt> </dl> </dd> <dt>

<span id="OFFLINEFILES_ITEM_FILTER_FLAG_USER_READ"></span><span id="offlinefiles_item_filter_flag_user_read"></span>**OFFLINEFILES\_ITEM\_FILTER\_FLAG\_USER\_READ**
</dt> <dd> <dl> <dt>

0x0000000000040000
</dt> <dt>



This flag is reserved for future use.


</dt> </dl> </dd> <dt>

<span id="OFFLINEFILES_ITEM_FILTER_FLAG_USER_ANYACCESS"></span><span id="offlinefiles_item_filter_flag_user_anyaccess"></span>**OFFLINEFILES\_ITEM\_FILTER\_FLAG\_USER\_ANYACCESS**
</dt> <dd> <dl> <dt>

0x0000000000080000
</dt> <dt>



This flag is reserved for future use.


</dt> </dl> </dd> <dt>

<span id="OFFLINEFILES_ITEM_FILTER_FLAG_OTHER_WRITE"></span><span id="offlinefiles_item_filter_flag_other_write"></span>**OFFLINEFILES\_ITEM\_FILTER\_FLAG\_OTHER\_WRITE**
</dt> <dd> <dl> <dt>

0x0000000000100000
</dt> <dt>



This flag is reserved for future use.


</dt> </dl> </dd> <dt>

<span id="OFFLINEFILES_ITEM_FILTER_FLAG_OTHER_READ"></span><span id="offlinefiles_item_filter_flag_other_read"></span>**OFFLINEFILES\_ITEM\_FILTER\_FLAG\_OTHER\_READ**
</dt> <dd> <dl> <dt>

0x0000000000200000
</dt> <dt>



This flag is reserved for future use.


</dt> </dl> </dd> <dt>

<span id="OFFLINEFILES_ITEM_FILTER_FLAG_OTHER_ANYACCESS"></span><span id="offlinefiles_item_filter_flag_other_anyaccess"></span>**OFFLINEFILES\_ITEM\_FILTER\_FLAG\_OTHER\_ANYACCESS**
</dt> <dd> <dl> <dt>

0x0000000000400000
</dt> <dt>



This flag is reserved for future use.


</dt> </dl> </dd> <dt>

<span id="OFFLINEFILES_ITEM_FILTER_FLAG_GUEST_WRITE"></span><span id="offlinefiles_item_filter_flag_guest_write"></span>**OFFLINEFILES\_ITEM\_FILTER\_FLAG\_GUEST\_WRITE**
</dt> <dd> <dl> <dt>

0x0000000000800000
</dt> <dt>



This flag is reserved for future use.


</dt> </dl> </dd> <dt>

<span id="OFFLINEFILES_ITEM_FILTER_FLAG_GUEST_READ"></span><span id="offlinefiles_item_filter_flag_guest_read"></span>**OFFLINEFILES\_ITEM\_FILTER\_FLAG\_GUEST\_READ**
</dt> <dd> <dl> <dt>

0x0000000001000000
</dt> <dt>



This flag is reserved for future use.


</dt> </dl> </dd> <dt>

<span id="OFFLINEFILES_ITEM_FILTER_FLAG_GUEST_ANYACCESS"></span><span id="offlinefiles_item_filter_flag_guest_anyaccess"></span>**OFFLINEFILES\_ITEM\_FILTER\_FLAG\_GUEST\_ANYACCESS**
</dt> <dd> <dl> <dt>

0x0000000002000000
</dt> <dt>



This flag is reserved for future use.


</dt> </dl> </dd> </dl>

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                      |
| Header<br/>                   | <dl> <dt>CscObj.h</dt> </dl> |



## See also

<dl> <dt>

[**IOfflineFilesItemFilter::GetFilterFlags**](/previous-versions/windows/desktop/api/CscObj/nf-cscobj-iofflinefilesitemfilter-getfilterflags)
</dt> </dl>

 

 




