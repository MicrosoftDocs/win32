---
title: PROPSHEETCFG structure
description: Used to contain property sheet configuration data.
ms.assetid: d3bde744-9d85-4506-894f-f8be3463721f
ms.tgt_platform: multiple
keywords:
- PROPSHEETCFG structure Active Directory
- PPROPSHEETCFG structure pointer Active Directory
topic_type:
- apiref
api_name:
- PROPSHEETCFG
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# PROPSHEETCFG structure

The **PROPSHEETCFG** structure is used to contain property sheet configuration data. This structure is contained in the [**CFSTR\_DS\_PROPSHEETCONFIG**](cfstr-ds-propsheetconfig.md) clipboard format.

> [!Note]  
> This structure is not defined in a published header file. To use this structure, you must define it yourself in the exact format shown.

 

## Syntax


```C++
typedef struct {
  LONG_PTR lNotifyHandle;
  HWND     hwndParentSheet;
  HWND     hwndHidden;
  WPARAM   wParamSheetClose;
} PROPSHEETCFG, *PPROPSHEETCFG;
```



## Members

<dl> <dt>

**lNotifyHandle**
</dt> <dd>

Contains the notification handle. This is identical to the handle passed for the *handle* parameter in the [**IExtendPropertySheet2::CreatePropertyPages**](/previous-versions/windows/desktop/legacy/aa814847(v=vs.85)) method.

</dd> <dt>

**hwndParentSheet**
</dt> <dd>

Contains the window handle of the parent property sheet.

</dd> <dt>

**hwndHidden**
</dt> <dd>

Contains the handle of the hidden window.

</dd> <dt>

**wParamSheetClose**
</dt> <dd>

Contains an application-defined 32-bit value. This value is passed back to the application in the *wParam* of the [**WM\_DSA\_SHEET\_CLOSE\_NOTIFY**](wm-dsa-sheet-close-notify.md) message.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |



## See also

<dl> <dt>

[**CFSTR\_DS\_PROPSHEETCONFIG**](cfstr-ds-propsheetconfig.md)
</dt> <dt>

[**WM\_DSA\_SHEET\_CLOSE\_NOTIFY**](wm-dsa-sheet-close-notify.md)
</dt> </dl>

 

