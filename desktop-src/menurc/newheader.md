---
title: NEWHEADER structure
description: Contains the number of icon or cursor components in a resource group. The structure definition provided here is for explanation only; it is not present in any standard header file.
ms.assetid: 1549579a-b558-42a9-9b3b-5b382334221c
keywords:
- NEWHEADER structure Menus and Other Resources
topic_type:
- apiref
api_name:
- NEWHEADER
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# NEWHEADER structure

Contains the number of icon or cursor components in a resource group. The structure definition provided here is for explanation only; it is not present in any standard header file.

## Syntax


```C++
typedef struct {
  WORD Reserved;
  WORD ResType;
  WORD ResCount;
} NEWHEADER, *NEWHEADER;
```



## Members

<dl> <dt>

**Reserved**
</dt> <dd>

Type: **WORD**

</dd> <dd>

Reserved; must be zero.

</dd> <dt>

**ResType**
</dt> <dd>

Type: **WORD**

</dd> <dd>

The resource type. This member must have one of the following values.



| Value                                                                                                                                                                                                       | Meaning                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|
| <span id="RES_CURSOR"></span><span id="res_cursor"></span><dl> <dt>**RES\_CURSOR**</dt> <dt>2</dt> </dl> | Cursor resource type.<br/> |
| <span id="RES_ICON"></span><span id="res_icon"></span><dl> <dt>**RES\_ICON**</dt> <dt>1</dt> </dl>       | Icon resource type.<br/>   |



 

</dd> <dt>

**ResCount**
</dt> <dd>

Type: **WORD**

</dd> <dd>

The number of icon or cursor components in the resource group.

</dd> </dl>

## Remarks

One or more [**RESDIR**](resdir.md) structures immediately follow the **NEWHEADER** structure in the .res file. The **ResCount** member specifies the number of **RESDIR** structures.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>       |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**RESDIR**](resdir.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Resources](resources.md)
</dt> </dl>

 

 





