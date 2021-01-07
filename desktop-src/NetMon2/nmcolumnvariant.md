---
description: Provides a line in the top pane of the Event Viewer that serves as a container for all possible data inserted into a column.
ms.assetid: 2ad32c23-5dbe-46be-b0cc-ccf7a6fe8ec3
title: NMCOLUMNVARIANT structure (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- NMCOLUMNVARIANT
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# NMCOLUMNVARIANT structure

The **NMCOLUMNVARIANT** structure provides a line in the top pane of the Event Viewer that serves as a container for all possible data inserted into a column.

## Syntax


```C++
typedef struct {
  NMCOLUMNTYPE Type;
  union {
    BYTE        Uint8Val;
    char        Sint8Val;
    WORD        Uint16Val;
    short       Sint16Val;
    DWORD       Uint32Val;
    LONG        Sint32Val;
    DOUBLE      Float64Val;
    DWORD       FrameVal;
    BOOL        YesNoVal;
    BOOL        OnOffVal;
    BOOL        TrueFalseVal;
    BYTE        MACAddrVal[MAC_ADDRESS_SIZE];
    IPX_ADDRESS IPXAddrVal;
    DWORD       IPAddrVal;
    DOUBLE      VarTimeVal;
    LPSTR       pStringVal;
  } Value;
} NMCOLUMNVARIANT;
```



## Members

<dl> <dt>

**Type**
</dt> <dd>

A value from the [**NMCOLUMNTYPE**](nmcolumntype.md) enumeration type.

</dd> <dt>

**Value**
</dt> <dd> <dl> <dt>

**Uint8Val**
</dt> <dd>

8-bit unsigned integer value.

</dd> <dt>

**Sint8Val**
</dt> <dd>

8-bit signed integer value.

</dd> <dt>

**Uint16Val**
</dt> <dd>

16-bit unsigned integer value.

</dd> <dt>

**Sint16Val**
</dt> <dd>

16-bit signed integer value.

</dd> <dt>

**Uint32Val**
</dt> <dd>

32-bit unsigned integer value.

</dd> <dt>

**Sint32Val**
</dt> <dd>

32-bit signed integer value.

</dd> <dt>

**Float64Val**
</dt> <dd>

64-bit float value.

</dd> <dt>

**FrameVal**
</dt> <dd>

Frame number.

</dd> <dt>

**YesNoVal**
</dt> <dd>

Displays Yes or No.

</dd> <dt>

**OnOffVal**
</dt> <dd>

Displays On or Off.

</dd> <dt>

**TrueFalseVal**
</dt> <dd>

Displays True or False.

</dd> <dt>

**MACAddrVal**
</dt> <dd>

MAC address.

</dd> <dt>

**IPXAddrVal**
</dt> <dd>

IPX address.

</dd> <dt>

**IPAddrVal**
</dt> <dd>

IP address.

</dd> <dt>

**VarTimeVal**
</dt> <dd>

Variant time. Use **VariantTimetoSystemTime** to convert to system time.

</dd> <dt>

**pStringVal**
</dt> <dd>

Pointer to a string.

</dd> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



## See also

<dl> <dt>

[**NMCOLUMNTYPE**](nmcolumntype.md)
</dt> </dl>

 

 




