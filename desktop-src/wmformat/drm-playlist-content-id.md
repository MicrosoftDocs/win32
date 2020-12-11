---
title: DRM_PLAYLIST_CONTENT_ID structure (Drmexternals.h)
description: The DRM\_PLAYLIST\_CONTENT\_ID structure contains information about content that is to be copied to CD as part of a playlist burn.
ms.assetid: 124e86ac-b0d4-40b2-868b-fe2fed1898e1
keywords:
- DRM_PLAYLIST_CONTENT_ID structure windows Media Format
- structure windows Media Format
topic_type:
- apiref
api_name:
- DRM_PLAYLIST_CONTENT_ID
api_location:
- Drmexternals.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# DRM\_PLAYLIST\_CONTENT\_ID structure

The **DRM\_PLAYLIST\_CONTENT\_ID** structure contains information about content that is to be copied to CD as part of a playlist burn.

## Syntax


```C++
typedef struct DRM_PLAYLIST_CONTENT_ID {
  LPCWSTR lpcwszV2Header;
  LPCSTR  lpcszV1KID;
  BYTE    *pbOtherData;
  DWORD   cbOtherData;
  DWORD   dwUniqueIDForSession;
  DWORD   dwValidFields;
} ;
```



## Members

<dl> <dt>

**lpcwszV2Header**
</dt> <dd>

DRM header. Use this member if the content is protected by Windows Media DRM version 2 or later.

</dd> <dt>

**lpcszV1KID**
</dt> <dd>

Key ID. Use this member if the content is protected by Windows Media DRM version 1.

</dd> <dt>

**pbOtherData**
</dt> <dd>

Buffer containing supplementary data.

</dd> <dt>

**cbOtherData**
</dt> <dd>

Size of the **pbOtherData** buffer in bytes.

</dd> <dt>

**dwUniqueIDForSession**
</dt> <dd>

Unique identifier for the content to be used in the current session.

</dd> <dt>

**dwValidFields**
</dt> <dd>

**DWORD** indicating the valid fields of this structure.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                      |
| Version<br/>                  | Windows Media Format 11 SDK<br/>                                                    |
| Header<br/>                   | <dl> <dt>Drmexternals.h</dt> </dl> |



## See also

<dl> <dt>

[**Structures**](structures.md)
</dt> </dl>

 

 





