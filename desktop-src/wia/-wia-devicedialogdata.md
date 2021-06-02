---
description: DEVICEDIALOGDATA structure - Defines the data needed to call a device dialog.
ms.assetid: 424defa6-1452-4a8b-bacc-738209c236c3
title: DEVICEDIALOGDATA structure (Wiadefd.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DEVICEDIALOGDATA
api_type: 
- HeaderDef
api_location: 
- Wiadefd.h
---

# DEVICEDIALOGDATA structure

Defines the data needed to call a device dialog.

## Syntax


```C++
typedef struct {
  DWORD    cbSize;
  HWND     hwndParent;
  IWiaItem *pIWiaItemRoot;
  DWORD    dwFlags;
  LONG     lIntent;
  LONG     lItemCount;
  IWiaItem **ppWiaItem;
} DEVICEDIALOGDATA;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Specifies the size of this structure in bytes.

</dd> <dt>

**hwndParent**
</dt> <dd>

Type: **HWND**

</dd> <dd>

Specifies the handle to the parent window of the dialog.

</dd> <dt>

**pIWiaItemRoot**
</dt> <dd>

Type: **[**IWiaItem**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiaitem)\***

</dd> <dd>

Points to an [**IWiaItem**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiaitem) interface that represents the valid root item in the application item tree.

</dd> <dt>

**dwFlags**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Specifies a set of flags that control the dialog box's operation. Can be set to any of the following values:



| Flag                                 | Meaning                                                                                                                                                                                     |
|--------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0                                    | Default behavior.                                                                                                                                                                           |
| WIA\_DEVICE\_DIALOG\_SINGLE\_IMAGE   | Restrict image selection to a single image in the device image acquisition dialog box.                                                                                                      |
| WIA\_DEVICE\_DIALOG\_USE\_COMMON\_UI | Use the system UI, if available, rather than the vendor-supplied UI. If the system UI is not available, the vendor UI is used. If neither UI is available, the function returns E\_NOTIMPL. |



 

</dd> <dt>

**lIntent**
</dt> <dd>

Type: **LONG**

</dd> <dd>

Specifies what type of data the image is intended to represent. For a list of image intent values, see [**Image Intent Constants**](-wia-imageintentconstants.md).

</dd> <dt>

**lItemCount**
</dt> <dd>

Type: **LONG**

</dd> <dd>

Receives the number of items in the array indicated by the **ppWiaItem** parameter.

</dd> <dt>

**ppWiaItem**
</dt> <dd>

Type: **[**IWiaItem**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiaitem)\*\***

</dd> <dd>

Receives the address of an array of pointers to [**IWiaItem**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiaitem) interfaces.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Wiadefd.h</dt> </dl> |



 

 




