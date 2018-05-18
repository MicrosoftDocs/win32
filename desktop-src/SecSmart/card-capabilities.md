---
title: CARD\_CAPABILITIES structure
description: Contains information about the capabilities of a smart card.
ms.assetid: '94c45ee0-486e-41cd-aee8-6a11939c538d'
keywords: ["CARD_CAPABILITIES structure Security", "PCARD_CAPABILITIES structure pointer Security"]
topic_type:
- apiref
api_name:
- CARD_CAPABILITIES
api_location:
- Cardmod.h
api_type:
- HeaderDef
---

# CARD\_CAPABILITIES structure

This topic is not current. For the most current information about the Smart Card API, see [Smart Card Minidriver Specification](http://go.microsoft.com/fwlink/p/?linkid=178045).

The **CARD\_CAPABILITIES** structure contains information about the capabilities of a [*smart card*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-smart-card-gly).

## Syntax


```C++
typedef struct _CARD_CAPABILITIES {
  DWORD dwVersion;
  BOOL  fCertificateCompression;
  BOOL  fKeyGen;
} CARD_CAPABILITIES, *PCARD_CAPABILITIES;
```



## Members

<dl> <dt>

**dwVersion**
</dt> <dd>

The version number of the structure.

</dd> <dt>

**fCertificateCompression**
</dt> <dd>

If **TRUE**, the smart card module implements its own certificate compression.

</dd> <dt>

**fKeyGen**
</dt> <dd>

If **TRUE**, the underlying smart card can securely generate asymmetric keys.

</dd> </dl>

## Remarks

The [**CardQueryCapabilities**](cardquerycapabilities.md) function initializes this structure.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Cardmod.h</dt> </dl> |



## See also

<dl> <dt>

[**CardQueryCapabilities**](cardquerycapabilities.md)
</dt> </dl>

 

 





