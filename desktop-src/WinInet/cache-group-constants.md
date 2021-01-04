---
title: Cache Group Constants (Wininet.h)
description: The following list contains the constants used by the cache group functions.
ms.assetid: 9ca2069e-497d-4747-acf4-d5b8020b8ab7
topic_type:
- apiref
api_name:
- CACHEGROUP_ATTRIBUTE_BASIC
- CACHEGROUP_ATTRIBUTE_FLAG
- CACHEGROUP_ATTRIBUTE_GET_ALL
- CACHEGROUP_ATTRIBUTE_GROUPNAME
- CACHEGROUP_ATTRIBUTE_QUOTA
- CACHEGROUP_ATTRIBUTE_STORAGE
- CACHEGROUP_ATTRIBUTE_TYPE
- CACHEGROUP_FLAG_FLUSHURL_ONDELETE
- CACHEGROUP_FLAG_GIDONLY
- CACHEGROUP_FLAG_NONPURGEABLE
- CACHEGROUP_READWRITE_MASK
- CACHEGROUP_SEARCH_ALL
- CACHEGROUP_SEARCH_BYURL
- CACHEGROUP_TYPE_INVALID
- GROUP_OWNER_STORAGE_SIZE
- GROUPNAME_MAX_LENGTH
api_location:
- Wininet.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Cache Group Constants

The following list contains the constants used by the cache group functions.

<dl> <dt>

<span id="CACHEGROUP_ATTRIBUTE_BASIC"></span><span id="cachegroup_attribute_basic"></span>**CACHEGROUP\_ATTRIBUTE\_BASIC**
</dt> <dd> <dl> <dt>

0x00000001
</dt> <dt>



Retrieves the flags, type, and disk quota attributes of the cache group. This is used by the [**GetUrlCacheGroupAttribute**](/windows/desktop/api/Wininet/nf-wininet-geturlcachegroupattributea) function.


</dt> </dl> </dd> <dt>

<span id="CACHEGROUP_ATTRIBUTE_FLAG"></span><span id="cachegroup_attribute_flag"></span>**CACHEGROUP\_ATTRIBUTE\_FLAG**
</dt> <dd> <dl> <dt>

0x00000002
</dt> <dt>



Sets or retrieves the flags associated with the cache group. This is used by the [**GetUrlCacheGroupAttribute**](/windows/desktop/api/Wininet/nf-wininet-geturlcachegroupattributea) and [**SetUrlCacheGroupAttribute**](/windows/desktop/api/Wininet/nf-wininet-seturlcachegroupattributea) functions.


</dt> </dl> </dd> <dt>

<span id="CACHEGROUP_ATTRIBUTE_GET_ALL"></span><span id="cachegroup_attribute_get_all"></span>**CACHEGROUP\_ATTRIBUTE\_GET\_ALL**
</dt> <dd> <dl> <dt>

0xffffffff
</dt> <dt>



Retrieves all the attributes of the cache group. This is used by the [**GetUrlCacheGroupAttribute**](/windows/desktop/api/Wininet/nf-wininet-geturlcachegroupattributea) function.


</dt> </dl> </dd> <dt>

<span id="CACHEGROUP_ATTRIBUTE_GROUPNAME"></span><span id="cachegroup_attribute_groupname"></span>**CACHEGROUP\_ATTRIBUTE\_GROUPNAME**
</dt> <dd> <dl> <dt>

0x000000010
</dt> <dt>



Sets or retrieves the group name of the cache group. This is used by the [**GetUrlCacheGroupAttribute**](/windows/desktop/api/Wininet/nf-wininet-geturlcachegroupattributea) and [**SetUrlCacheGroupAttribute**](/windows/desktop/api/Wininet/nf-wininet-seturlcachegroupattributea) functions.


</dt> </dl> </dd> <dt>

<span id="CACHEGROUP_ATTRIBUTE_QUOTA"></span><span id="cachegroup_attribute_quota"></span>**CACHEGROUP\_ATTRIBUTE\_QUOTA**
</dt> <dd> <dl> <dt>

0x00000008
</dt> <dt>



Sets or retrieves the disk quota associated with the cache group. This is used by the [**GetUrlCacheGroupAttribute**](/windows/desktop/api/Wininet/nf-wininet-geturlcachegroupattributea) and [**SetUrlCacheGroupAttribute**](/windows/desktop/api/Wininet/nf-wininet-seturlcachegroupattributea) functions.


</dt> </dl> </dd> <dt>

<span id="CACHEGROUP_ATTRIBUTE_STORAGE"></span><span id="cachegroup_attribute_storage"></span>**CACHEGROUP\_ATTRIBUTE\_STORAGE**
</dt> <dd> <dl> <dt>

0x00000020
</dt> <dt>



Sets or retrieves the group owner storage associated with the cache group. This is used by the [**GetUrlCacheGroupAttribute**](/windows/desktop/api/Wininet/nf-wininet-geturlcachegroupattributea) and [**SetUrlCacheGroupAttribute**](/windows/desktop/api/Wininet/nf-wininet-seturlcachegroupattributea) functions.


</dt> </dl> </dd> <dt>

<span id="CACHEGROUP_ATTRIBUTE_TYPE"></span><span id="cachegroup_attribute_type"></span>**CACHEGROUP\_ATTRIBUTE\_TYPE**
</dt> <dd> <dl> <dt>

0x00000004
</dt> <dt>



Sets or retrieves the cache group type. This is used by the [**GetUrlCacheGroupAttribute**](/windows/desktop/api/Wininet/nf-wininet-geturlcachegroupattributea) and [**SetUrlCacheGroupAttribute**](/windows/desktop/api/Wininet/nf-wininet-seturlcachegroupattributea) functions.


</dt> </dl> </dd> <dt>

<span id="CACHEGROUP_FLAG_FLUSHURL_ONDELETE"></span><span id="cachegroup_flag_flushurl_ondelete"></span>**CACHEGROUP\_FLAG\_FLUSHURL\_ONDELETE**
</dt> <dd> <dl> <dt>

0x00000002
</dt> <dt>



Indicates that all the cache entries associated with the cache group should be deleted, unless the entry belongs to another cache group.


</dt> </dl> </dd> <dt>

<span id="CACHEGROUP_FLAG_GIDONLY"></span><span id="cachegroup_flag_gidonly"></span>**CACHEGROUP\_FLAG\_GIDONLY**
</dt> <dd> <dl> <dt>

0x00000004
</dt> <dt>



Indicates that the function should only create a unique GROUPID for the cache group and not create the actual group.


</dt> </dl> </dd> <dt>

<span id="CACHEGROUP_FLAG_NONPURGEABLE"></span><span id="cachegroup_flag_nonpurgeable"></span>**CACHEGROUP\_FLAG\_NONPURGEABLE**
</dt> <dd> <dl> <dt>

0x00000001
</dt> <dt>



Indicates that the cache group cannot be purged.


</dt> </dl> </dd> <dt>

<span id="CACHEGROUP_READWRITE_MASK"></span><span id="cachegroup_readwrite_mask"></span>**CACHEGROUP\_READWRITE\_MASK**
</dt> <dd> <dl> <dt>

0x0000003c
</dt> <dt>



Sets the type, disk quota, group name, and owner storage attributes of the cache group. This is used by the [**SetUrlCacheGroupAttribute**](/windows/desktop/api/Wininet/nf-wininet-seturlcachegroupattributea) function.


</dt> </dl> </dd> <dt>

<span id="CACHEGROUP_SEARCH_ALL"></span><span id="cachegroup_search_all"></span>**CACHEGROUP\_SEARCH\_ALL**
</dt> <dd> <dl> <dt>

0x00000000
</dt> <dt>



Indicates that all of the cache groups in the user's system should be enumerated.


</dt> </dl> </dd> <dt>

<span id="CACHEGROUP_SEARCH_BYURL"></span><span id="cachegroup_search_byurl"></span>**CACHEGROUP\_SEARCH\_BYURL**
</dt> <dd> <dl> <dt>

0x00000001
</dt> <dt>



Not currently implemented.


</dt> </dl> </dd> <dt>

<span id="CACHEGROUP_TYPE_INVALID"></span><span id="cachegroup_type_invalid"></span>**CACHEGROUP\_TYPE\_INVALID**
</dt> <dd> <dl> <dt>

0x00000001
</dt> <dt>



Indicates that the cache group type is invalid.


</dt> </dl> </dd> <dt>

<span id="GROUP_OWNER_STORAGE_SIZE"></span><span id="group_owner_storage_size"></span>**GROUP\_OWNER\_STORAGE\_SIZE**
</dt> <dd> <dl> <dt>

0x00000004
</dt> <dt>



Length of the group owner storage array.


</dt> </dl> </dd> <dt>

<span id="GROUPNAME_MAX_LENGTH"></span><span id="groupname_max_length"></span>**GROUPNAME\_MAX\_LENGTH**
</dt> <dd> <dl> <dt>

0x00000078
</dt> <dt>



Maximum number of characters allowed for a cache group name.


</dt> </dl> </dd> </dl>

## Remarks

> [!Note]  
> WinINet does not support server implementations. In addition, it should not be used from a service. For server implementations or services use [Microsoft Windows HTTP Services (WinHTTP)](/windows/desktop/WinHttp/winhttp-start-page).

 

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Wininet.h</dt> </dl> |



 

