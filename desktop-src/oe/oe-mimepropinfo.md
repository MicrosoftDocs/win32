---
title: MIMEPROPINFO structure
description: Do not use. Holds information about a property in an IMimePropertySet object.
ms.assetid: '3d0538a8-f89a-42da-b1a8-c7c45adb43e9'
keywords: ["MIMEPROPINFO structure Windows Mail (formerly Outlook Express)", "LPMIMEPROPINFO structure pointer Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- MIMEPROPINFO
api_location:
- Mimeole.h
api_type:
- HeaderDef
---

# MIMEPROPINFO structure

Do not use. Holds information about a property in an [**IMimePropertySet**](oe-imimepropertyset.md) object.

## Syntax


```C++
typedef struct tagMIMEPROPINFO {
  DWORD        dwMask;
  HCHARSET     hCharset;
  ENCODINGTYPE ietEncoding;
  DWORD        dwRowNumber;
  DWORD        dwFlags;
  DWORD        dwPropId;
  DWORD        cValues;
  VARTYPE      vtDefault;
  VARTYPE      vtCurrent;
} MIMEPROPINFO, *LPMIMEPROPINFO;
```



## Members

<dl> <dt>

**dwMask**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains a bitmask that indicates the valid fields in this structure. For possible values, see [**PROPINFOMASK**](oe-propinfomask.md).

</dd> <dt>

**hCharset**
</dt> <dd>

Type: **HCHARSET**

</dd> <dd>

Contains a handle to the character set for this property.

</dd> <dt>

**ietEncoding**
</dt> <dd>

Type: **[**ENCODINGTYPE**](oe-encodingtype.md)**

</dd> <dd>

Contains the [**ENCODINGTYPE**](oe-encodingtype.md) for this property.

</dd> <dt>

**dwRowNumber**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains the header row number for this property.

</dd> <dt>

**dwFlags**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains a bitmask that describes the property. For possible values, see [**MIMEPROPFLAGS**](oe-mimepropflags.md)

</dd> <dt>

**dwPropId**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains the property ID for this property.

</dd> <dt>

**cValues**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains the number of times this property appears in the property set.

</dd> <dt>

**vtDefault**
</dt> <dd>

Type: **[VARTYPE](https://msdn.microsoft.com/library/windows/desktop/ms221127)**

</dd> <dd>

Contains the default [VARTYPE](https://msdn.microsoft.com/library/windows/desktop/ms221127) for this property.

</dd> <dt>

**vtCurrent**
</dt> <dd>

Type: **[VARTYPE](https://msdn.microsoft.com/library/windows/desktop/ms221127)**

</dd> <dd>

Contains the current [VARTYPE](https://msdn.microsoft.com/library/windows/desktop/ms221127) for this property.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| Product<br/>                  | Outlook Express 6.0<br/>                                                         |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl> |



 

 





