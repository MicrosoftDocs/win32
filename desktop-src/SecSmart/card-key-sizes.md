---
title: CARD\_KEY\_SIZES structure
description: Contains information about the key lengths supported by a smart card.
ms.assetid: 'e4d262c2-5e82-4c6a-8e5d-c7bce5f64956'
keywords: ["CARD_KEY_SIZES structure Security", "PCARD_KEY_SIZES structure pointer Security"]
topic_type:
- apiref
api_name:
- CARD_KEY_SIZES
api_location:
- Cardmod.h
api_type:
- HeaderDef
---

# CARD\_KEY\_SIZES structure

This topic is not current. For the most current information about the Smart Card API, see [Smart Card Minidriver Specification](http://go.microsoft.com/fwlink/p/?linkid=178045).

The **CARD\_KEY\_SIZES** structure contains information about the [*key lengths*](https://msdn.microsoft.com/library/windows/desktop/ms721590#-security-key-length-gly) supported by a [*smart card*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-smart-card-gly).

## Syntax


```C++
typedef struct _CARD_KEY_SIZES {
  DWORD dwVersion;
  DWORD dwMinimumBitlen;
  DWORD dwMaximumBitlen;
  DWORD dwIncrementalBitlen;
} CARD_KEY_SIZES, *PCARD_KEY_SIZES;
```



## Members

<dl> <dt>

**dwVersion**
</dt> <dd>

The version number of the structure.

</dd> <dt>

**dwMinimumBitlen**
</dt> <dd>

The minimum supported length, in bits, of a key.

</dd> <dt>

**dwMaximumBitlen**
</dt> <dd>

The maximum supported length, in bits, of a key.

</dd> <dt>

**dwIncrementalBitlen**
</dt> <dd>

The number of bits for increments of the key length. For example, if the minimum key length is 512 bits, and the value of this member is 64, then valid key lengths are 512 bits, 576 bits, 640 bits, and so on, up to the maximum key length.

</dd> </dl>

## Remarks

The [**CardQueryKeySizes**](cardquerykeysizes.md) function initializes this structure.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Cardmod.h</dt> </dl> |



## See also

<dl> <dt>

[Microsoft Base Smart Card Cryptographic Service Provider](microsoft-base-smart-card-cryptographic-service-provider.md)
</dt> <dt>

[**CardQueryKeySizes**](cardquerykeysizes.md)
</dt> </dl>

 

 





