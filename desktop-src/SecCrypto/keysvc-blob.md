---
description: The KEYSVC\_BLOB structure defines a key service BLOB. This structure is used by the RKeyPFXInstall function.
ms.assetid: 255b5fab-6271-4d3f-9c56-a63278b8b104
title: KEYSVC_BLOB structure (Rkeysvcc.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- KEYSVC_BLOB
api_type: 
- HeaderDef
api_location: 
- Rkeysvcc.h
---

# KEYSVC\_BLOB structure

The **KEYSVC\_BLOB** structure defines a key service BLOB. This structure is used by the [**RKeyPFXInstall**](rkeypfxinstall.md) function.

## Syntax


```C++
typedef struct _KEYSVC_BLOB {
  ULONG cb;
  BYTE  *pb;
} KEYSVC_BLOB, *PKEYSVC_BLOB;
```



## Members

<dl> <dt>

**cb**
</dt> <dd>

A **ULONG** value that specifies the size, in bytes, of **pb**.

</dd> <dt>

**pb**
</dt> <dd>

A pointer to a **BYTE** that contains the BLOB, in [*PKCS \#12*](../secgloss/p-gly.md) format.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Rkeysvcc.h</dt> </dl> |



## See also

<dl> <dt>

[**RKeyPFXInstall**](rkeypfxinstall.md)
</dt> <dt>

[**KEYSVC\_UNICODE\_STRING**](keysvc-unicode-string.md)
</dt> </dl>

 

 
