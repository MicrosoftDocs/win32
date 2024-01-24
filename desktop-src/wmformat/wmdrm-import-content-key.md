---
title: WMDRM_IMPORT_CONTENT_KEY structure (Drmexternals.h)
description: The WMDRM\_IMPORT\_CONTENT\_KEY structure stores the content key used in importing protected content.
ms.assetid: 29a0f98d-96a3-46b2-a67c-dbb23449e927
keywords:
- WMDRM_IMPORT_CONTENT_KEY structure windows Media Format
- structure windows Media Format
topic_type:
- apiref
api_name:
- WMDRM_IMPORT_CONTENT_KEY
api_location:
- Drmexternals.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# WMDRM\_IMPORT\_CONTENT\_KEY structure

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **WMDRM\_IMPORT\_CONTENT\_KEY** structure stores the content key used in importing protected content.

## Syntax


```C++
typedef struct WMDRM_IMPORT_CONTENT_KEY {
  DWORD dwVersion;
  DWORD cbStructSize;
  DWORD dwIVKeyType;
  DWORD cbIVKey;
  DWORD dwContentKeyType;
  DWORD cbContentKey;
  BYTE  rgbKeyData[1];
} ;
```



## Members

<dl> <dt>

**dwVersion**
</dt> <dd>

Version.

</dd> <dt>

**cbStructSize**
</dt> <dd>

Size of structure in bytes.

</dd> <dt>

**dwIVKeyType**
</dt> <dd>

Initialization vector key type. Set to WMDRM\_KEYTYPE\_RC4.

</dd> <dt>

**cbIVKey**
</dt> <dd>

Size of the initialization vector key in bytes.

</dd> <dt>

**dwContentKeyType**
</dt> <dd>

Content key type. Set to WMDRM\_KEYTYPE\_COCKTAIL.

</dd> <dt>

**cbContentKey**
</dt> <dd>

Size of the content key in bytes.

</dd> <dt>

**rgbKeyData**
</dt> <dd>

Address of a buffer containing the content key. The buffer size must match the value of **cbContentKey**. This key should match the key imported from the XMR license message.

</dd> </dl>

## Remarks

This structure, including the buffer containing the session key, must be encrypted with the session key and included in the **pbEncryptedKeyMessage** member of the [**WMDRM\_IMPORT\_INIT\_STRUCT**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wmdrm_import_init_struct) structure.

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

 

 





