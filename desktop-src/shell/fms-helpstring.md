---
Description: Contains information that File Manager uses to add a Help string for a menu or toolbar command item.
title: FMS\_HELPSTRING structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# FMS\_HELPSTRING structure

Contains information that File Manager uses to add a Help string for a menu or toolbar command item.

## Syntax


```C++
typedef struct _FMS_HELPSTRING {
  INT       idCommand;
  HMENU     hMenu;
  __wchar_t szHelp[128];
} FMS_HELPSTRING;
```



## Members

<dl> <dt>

**idCommand**
</dt> <dd>

Type: **INT**

</dd> <dd>

The identifier of the command item.

</dd> <dt>

**hMenu**
</dt> <dd>

Type: **HMENU**

</dd> <dd>

The identifier of the menu bar.

</dd> <dt>

**szHelp**
</dt> <dd>

Type: **\_\_wchar\_t\[128\]**

</dd> <dd>

The null-terminated string that receives the Help text.

</dd> </dl>

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wfext.h</dt> </dl> |



## See also

<dl> <dt>

[**FMExtensionProc**](fmextensionproc.md)
</dt> <dt>

[**FMEVENT\_HELPMENUITEM**](fmevent-helpmenuitem.md)
</dt> </dl>

 

 




