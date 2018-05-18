---
title: ENUMPROPERTY structure
description: Do not use. Used by the IMimeEnumProperties interface to enumerate the properties in an IMimePropertySet object.
ms.assetid: 'f04a07a9-c055-437b-918e-4b051afdb9da'
keywords: ["ENUMPROPERTY structure Windows Mail (formerly Outlook Express)", "LPENUMPROPERTY structure pointer Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- ENUMPROPERTY
api_location:
- Mimeole.h
api_type:
- HeaderDef
---

# ENUMPROPERTY structure

Do not use. Used by the [**IMimeEnumProperties**](oe-imimeenumproperties.md) interface to enumerate the properties in an [**IMimePropertySet**](oe-imimepropertyset.md) object.

## Syntax


```C++
typedef struct tagENUMPROPERTY {
  LPSTR      pszName;
  HHEADERROW hRow;
  DWORD      dwPropId;
} ENUMPROPERTY, *LPENUMPROPERTY;
```



## Members

<dl> <dt>

**pszName**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains the name of the property.

</dd> <dt>

**hRow**
</dt> <dd>

Type: **HHEADERROW**

</dd> <dd>

Contains the handle of this property.

</dd> <dt>

**dwPropId**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains the value of the property ID.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| Product<br/>                  | Outlook Express 6.0<br/>                                                         |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl> |



 

 





