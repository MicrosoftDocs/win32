---
description: The PROPERTYINST structure defines an instance of a property in a piece of recognized data. Network Monitor allocates and fills in a PROPERTYINST structure when a property is attached to the capture.
ms.assetid: d8382a38-b634-4c65-b56b-44fee067a0fe
title: PROPERTYINST structure (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PROPERTYINST
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# PROPERTYINST structure

The **PROPERTYINST** structure defines an instance of a property in a piece of recognized data. Network Monitor allocates and fills in a **PROPERTYINST** structure when a property is attached to the capture.

## Syntax


```C++
typedef struct _PROPERTYINST {
  LPPROPERTYINFO lpPropertyInfo;
  LPSTR          szPropertyText;
  union {
    LPVOID           lpData;
    ULPBYTE          lpByte;
    ULPWORD          lpWord;
    ULPDWORD         lpDword;
    ULPLARGEINT      lpLargeInt;
    ULPSYSTEMTIME    lpSysTime;
    LPPROPERTYINSTEX lpPropertyInstEx;
  };
  WORD           DataLength;
  WORD           Level  :4;
  WORD           HelpID  :12;
  DWORD          IFlags;
} PROPERTYINST, *LPPROPERTYINST;
```



## Members

<dl> <dt>

**lpPropertyInfo**
</dt> <dd>

Pointer to the [PROPERTYINFO](propertyinfo.md) structure that defines the property.

</dd> <dt>

**szPropertyText**
</dt> <dd>

Pointer to a string that is displayed in the details pane of the Network Monitor UI.

</dd> <dt>

**lpData**
</dt> <dd>

Pointer to the start of the data for the property. The parser determines where the property data starts.

</dd> <dt>

**lpByte**
</dt> <dd>

Pointer to the **BYTE** data.

</dd> <dt>

**lpWord**
</dt> <dd>

Pointer to the **WORD** data.

</dd> <dt>

**lpDword**
</dt> <dd>

Pointer to the **DWORD** data.

</dd> <dt>

**lpLargeInt**
</dt> <dd>

Pointer to the [**LARGEINT**](largeint.md) data.

</dd> <dt>

**lpSysTime**
</dt> <dd>

Pointer to the [**SYSTEMTIME**](/windows/desktop/api/minwinbase/ns-minwinbase-systemtime) data.

</dd> <dt>

**lpPropertyInstEx**
</dt> <dd>

Pointer to a [PROPERTYINSTEX](propertyinstex.md) structure. The **lpPropertyInstEx** member is used only when you call [AttachPropertyInstanceEx](attachpropertyinstanceex.md).

If **lpPropertyInstEx** is used, you must set the **DataLength** member to 0xFFFF.

</dd> <dt>

**DataLength**
</dt> <dd>

Data length for this instance of the property. If the **lpPropertyInstEx** member points to a [**PROPERTYINSTEX**](propertyinstex.md) structure, you must set **DataLength** to 0xFFFF.

</dd> <dt>

**Level**
</dt> <dd>

Level information.

</dd> <dt>

**HelpID**
</dt> <dd>

Help file context identifier.

</dd> <dt>

**IFlags**
</dt> <dd>

Error condition flag.

</dd> </dl>

## Remarks

The **PROPERTYINST** structure defines an instance of an attached property. The parser accesses the **PROPERTYINST** structure through several helper functions. For example, when the [**FormatPropertyInstance**](formatpropertyinstance.md) function is called to format the data of a property, it modifies the **szPropertyText** member of the **PROPERTYINST** structure.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



## See also

<dl> <dt>

[AttachPropertyInstance](attachpropertyinstance.md)
</dt> <dt>

[AttachPropertyInstanceEx](attachpropertyinstanceex.md)
</dt> </dl>

 

