---
title: WMDRM_IMPORT_SESSION_KEY structure (Drmexternals.h)
description: The WMDRM\_IMPORT\_SESSION\_KEY structure holds the session key for importing protected content.
ms.assetid: 2dd1e8ec-a25f-4ced-8f1b-286534c66ebf
keywords:
- WMDRM_IMPORT_SESSION_KEY structure windows Media Format
- structure windows Media Format
topic_type:
- apiref
api_name:
- WMDRM_IMPORT_SESSION_KEY
api_location:
- Drmexternals.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WMDRM\_IMPORT\_SESSION\_KEY structure

The **WMDRM\_IMPORT\_SESSION\_KEY** structure holds the session key for importing protected content.

## Syntax


```C++
typedef struct WMDRM_IMPORT_SESSION_KEY {
  DWORD dwKeyType;
  DWORD cbKey;
  BYTE  rgbKey[1];
} ;
```



## Members

<dl> <dt>

**dwKeyType**
</dt> <dd>

Session key type. Set to WMDRM\_KEYTYPE\_RC4.

</dd> <dt>

**cbKey**
</dt> <dd>

Size of the session key, in bytes. This value can be as large as you need, given the limits of a single RSA OAEP operation over the entire message (this structure plus the session key).

</dd> <dt>

**rgbKey**
</dt> <dd>

Address of a buffer containing the session key. The buffer size must match the value of **cbKey**. The data in the buffer is a randomly generated key value.

</dd> </dl>

## Remarks

This structure, including the buffer containing the session key, must be encrypted with the Windows Media DRM machine public key and included in the **pbEncryptedSessionKeyMessage** member of the [**WMDRM\_IMPORT\_INIT\_STRUCT**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wmdrm_import_init_struct) structure.

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

 

 





