---
Description: The DLGPAGE structure is used for specifying a property sheet page to CPSUI's ComPropSheet function. The structure's address is included in a COMPROPSHEETUI structure, and all member values are supplied by the ComPropSheet caller.
ms.assetid: 61fb66b9-afd7-4ec4-bbbb-66a287398484
title: DLGPAGE structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# DLGPAGE structure

The DLGPAGE structure is used for specifying a property sheet page to CPSUI's [**ComPropSheet**](compropsheet.md) function. The structure's address is included in a [**COMPROPSHEETUI**](compropsheetui.md) structure, and all member values are supplied by the **ComPropSheet** caller.

## Syntax


```C++
typedef struct _DLGPAGE {
  WORD      cbSize;
  WORD      Flags;
  DLGPROC   DlgProc;
  LPTSTR    pTabName;
  ULONG_PTR IconID;
  union {
    WORD   DlgTemplateID;
    HANDLE hDlgTemplate;
  };
} DLGPAGE, *PDLGPAGE;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

Caller-supplied size, in bytes, of the DLGPAGE structure.

</dd> <dt>

**Flags**
</dt> <dd>

Caller-supplied bit flags, as described in the following table.



| Flag                              | Definition                                                                                                                                        |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| DPF\_ICONID\_AS\_HICON<br/> | If set, IconID contains an icon handle.<br/> If not set, IconID contains an icon resource identifier.<br/>                            |
| DPF\_USE\_HDLGTEMPLATE<br/> | If set, **hDlgTemplate** contains a template handle.<br/> If not set, **DlgTemplateID** contains a template resource identifier.<br/> |



 

</dd> <dt>

**DlgProc**
</dt> <dd>

Optional, caller-supplied DLGPROC-typed pointer to a dialog box procedure, used to process messages sent by the system when user events occur. (The DLGPROC pointer type is described in the Microsoft Windows SDK documentation.) If **NULL**, CPSUI supplies a dialog box procedure. For more information, see the following Remarks section.

</dd> <dt>

**pTabName**
</dt> <dd>

Caller-supplied pointer to a NULL-terminated string to be displayed on the page tab.

</dd> <dt>

**IconID**
</dt> <dd>

Caller-supplied, can be one of the following:

-   An icon resource identifier. This can be application-defined, or it can be one of the CPSUI-supplied, IDI\_CPSUI-prefixed icon resource identifiers.

-   An icon handle. If a handle is specified, DPF\_ICONID\_AS\_HICON must be set in the **Flags** member.

The specified icon is displayed on the page tab. If this value is zero, an icon is not displayed.

</dd> <dt>

**DlgTemplateID**
</dt> <dd>

Caller-supplied resource identifier for a dialog box template. This can refer to an application-supplied DIALOG resource, or it can be one of the following CPSUI-supplied identifiers (defined in compstui.h):



| Identifier                       | Type of Page                                                                     |
|----------------------------------|----------------------------------------------------------------------------------|
| DP\_STD\_DOCPROPPAGE1<br/> | Nontreeview page, used for a print document's **Layout** page.<br/>        |
| DP\_STD\_DOCPROPPAGE2<br/> | Nontreeview page, used for a print document's **Paper/Quality** page.<br/> |
| DP\_STD\_TREEVIEWPAGE<br/> | Generic treeview page.<br/>                                                |



 

The CPSUI-supplied identifiers refer to templates that can display [CPSUI option types](https://www.bing.com/search?q=CPSUI option types). The page size for those templates is 252 by 216 dialog box units. For more information, see [CPSUI-Supplied Pages and Templates](https://www.bing.com/search?q=CPSUI-Supplied Pages and Templates).

This member is not used if DPF\_USE\_HDLGTEMPLATE is set in **Flags**.

</dd> <dt>

**hDlgTemplate**
</dt> <dd>

Caller-supplied handle to a DLGTEMPLATE structure (described in the Microsoft Windows SDK documentation).

Used only if DPF\_USE\_HDLGTEMPLATE is set in **Flags**.

</dd> </dl>

## Remarks

CPSUI creates a property sheet page by allocating a PROPSHEETPAGE structure and passing it to CreatePropertySheetPage (described in the Windows SDK documentation). If the caller has specified a DLGPROC-typed pointer to a dialog box procedure in **DlgProc**, that procedure is used for handling the page's window messages. If **DlgProc** is **NULL**, CPSUI's own dialog box procedures are used.

When the dialog box procedure pointed to by **DlgProc** is called with a message value of WM\_INITDIALOG, it receives the PROPSHEETPAGE structure as input, and it also receives a [**PSPINFO**](pspinfo.md) structure.

If a caller-supplied dialog box procedure handles a message, it should return a nonzero value. If the function does not handle the message it should return zero, which causes CPSUI to handle the message.

The PROPSHEETPAGE structure, the DLGPROC pointer type, and the WM\_INITDIALOG message are described in the Windows SDK documentation.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Compstui.h (include Compstui.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20DLGPAGE%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




