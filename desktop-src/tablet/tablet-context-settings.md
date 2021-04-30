---
description: Contains information used in creating a tablet context.
ms.assetid: 10466c23-f4cb-4205-886b-d85a2f530afe
title: TABLET_CONTEXT_SETTINGS structure
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- TABLET_CONTEXT_SETTINGS
api_type: 
- NA
api_location: 
---

# TABLET\_CONTEXT\_SETTINGS structure

Contains information used in creating a tablet context.

## Syntax


```C++
typedef struct _TABLET_CONTEXT_SETTINGS {
  ULONG cPktProps;
  GUID  *pguidPktProps;
  ULONG cPktBtns;
  GUID  *pguidPktBtns;
  DWORD *pdwBtnDnMask;
  DWORD *pdwBtnUpMask;
  LONG  lXMargin;
  LONG  lYMargin;
} TABLET_CONTEXT_SETTINGS;
```



## Members

<dl> <dt>

**cPktProps**
</dt> <dd>

The number of properties in a packet.

</dd> <dt>

**pguidPktProps**
</dt> <dd>

Unique identifiers for the packet properties.

</dd> <dt>

**cPktBtns**
</dt> <dd>

The number of buttons.

</dd> <dt>

**pguidPktBtns**
</dt> <dd>

Unique identifiers for the buttons.

</dd> <dt>

**pdwBtnDnMask**
</dt> <dd>

The button down mask.

</dd> <dt>

**pdwBtnUpMask**
</dt> <dd>

The button up mask.

</dd> <dt>

**lXMargin**
</dt> <dd>

The X direction margin.

</dd> <dt>

**lYMargin**
</dt> <dd>

The Y direction margin.

</dd> </dl>

## Remarks

Typically, an application obtains the default values from the [**ITablet::GetDefaultContextSettings Method**](itablet-getdefaultcontextsettings.md), modifies values to suit their needs, and then passes the modified settings structure to the [**ITablet::CreateContext Method**](itablet-createcontext.md).

This structure determines what events an application will get, how they will be processed, and how they will be delivered to the application or to Windows itself.

The button masks together determine what kinds of events will be processed by the context.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/> |
| Minimum supported server<br/> | None supported<br/>                                     |



 

 




