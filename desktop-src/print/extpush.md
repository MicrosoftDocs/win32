---
Description: The EXTPUSH structure is used by CPSUI applications (including printer interface DLLs) for specifying an extended push button, which can be added to a property sheet page option. When the button is pushed, a new dialog can be displayed.
ms.assetid: c38d7eca-6486-4bb1-b0a8-7f69fe13f7db
title: EXTPUSH structure
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# EXTPUSH structure

The EXTPUSH structure is used by CPSUI applications (including printer interface DLLs) for specifying an extended push button, which can be added to a property sheet page option. When the button is pushed, a new dialog can be displayed.

## Syntax


```C++
typedef struct _EXTPUSH {
  WORD      cbSize;
  WORD      Flags;
  LPTSTR    pTitle;
  union {
    DLGPROC DlgProc;
    FARPROC pfnCallBack;
  };
  ULONG_PTR IconID;
  union {
    WORD   DlgTemplateID;
    HANDLE hDlgTemplate;
  };
  ULONG_PTR dwReserved[3];
} EXTPUSH, *PEXTPUSH;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

Size, in bytes, of the EXTPUSH structure.

</dd> <dt>

**Flags**
</dt> <dd>

Bit flags, which can be one of the following:

<dl> <dt>

<span id="EPF_ICONID_AS_HICON"></span><span id="epf_iconid_as_hicon"></span>EPF\_ICONID\_AS\_HICON
</dt> <dd>

If set, the **IconID** member contains an icon handle.

If not set, the **IconID** member contains an icon resource identifier.

</dd> </dl>

<dl> <dt>

<span id="EPF_INCLUDE_SETUP_TITLE"></span><span id="epf_include_setup_title"></span>EPF\_INCLUDE\_SETUP\_TITLE
</dt> <dd>

If set, CPSUI appends "Setup" to the string pointed to by **pTitle**.

</dd> </dl>

<dl> <dt>

<span id="EPF_NO_DOT_DOT_DOT"></span><span id="epf_no_dot_dot_dot"></span>EPF\_NO\_DOT\_DOT\_DOT
</dt> <dd>

If set, CPSUI does not append "..." to the string pointed to by **pTitle**.

</dd> </dl>

<dl> <dt>

<span id="EPF_OVERLAY_NO_ICON"></span><span id="epf_overlay_no_icon"></span>EPF\_OVERLAY\_NO\_ICON
</dt> <dd>

If set, CPSUI overlays its IDI\_CPSUI\_NO icon onto the icon identified by the **IconID** member.

</dd> </dl>

<dl> <dt>

<span id="EPF_OVERLAY_STOP_ICON"></span><span id="epf_overlay_stop_icon"></span>EPF\_OVERLAY\_STOP\_ICON
</dt> <dd>

If set, CPSUI overlays the IDI\_CPSUI\_STOP icon onto the icon identified by the **IconID** member.

</dd> </dl>

<dl> <dt>

<span id="EPF_OVERLAY_WARNING_ICON"></span><span id="epf_overlay_warning_icon"></span>EPF\_OVERLAY\_WARNING\_ICON
</dt> <dd>

If set, CPSUI overlays its IDI\_CPSUI\_WARNING icon onto the icon identified by the **IconID** member.

</dd> </dl>

<dl> <dt>

<span id="EPF_PUSH_TYPE_DLGPROC"></span><span id="epf_push_type_dlgproc"></span>EPF\_PUSH\_TYPE\_DLGPROC
</dt> <dd>

If set, the **DlgProc** and **DlgTemplateID/hDlgTemplate** members are valid.

If not set, the **pfnCallBack** member is valid.

</dd> </dl>

<dl> <dt>

<span id="EPF_USE_HDLGTEMPLATE"></span><span id="epf_use_hdlgtemplate"></span>EPF\_USE\_HDLGTEMPLATE
</dt> <dd>

If set, **hDlgTemplate** contains a template handle.

If not set, **DlgTemplateID** contains a template resource identifier.

</dd> </dl> </dd> <dt>

**pTitle**
</dt> <dd>

String identifier, representing the push button title. This can be a 32-bit pointer to a NULL-terminated string, or it can be a 16-bit string resource identifier with HIWORD set to zero.

</dd> <dt>

**DlgProc**
</dt> <dd>

DLGPROC-typed pointer to a dialog box procedure to process messages for the push button's dialog box. (The DLGPROC pointer type is described in the Microsoft Windows SDK documentation.) For more information, see the following Remarks section.

If this pointer is supplied, EPF\_PUSH\_TYPE\_DLGPROC must be set in **Flags**.

</dd> <dt>

**pfnCallBack**
</dt> <dd>

Pointer to a [**\_CPSUICALLBACK**](-cpsuicallback.md)-typed callback function to handle the CPSUICB\_REASON\_PUSHBUTTON reason. For more information, see the following Remarks section.

If this pointer is supplied, EPF\_PUSH\_TYPE\_DLGPROC must be cleared in **Flags**.

</dd> <dt>

**IconID**
</dt> <dd>

One of the following icon identifiers:

-   An icon resource identifier. This can be application-defined, or it can be one of the CPSUI-supplied, IDI\_CPSUI-prefixed icon resource identifiers.

-   An icon handle. If a handle is specified, EPF\_ICONID\_AS\_HICON must be set in the **Flags** member.

CPSUI displays the icon next to the push button. If this value is zero, an icon is not displayed.

</dd> <dt>

**DlgTemplateID**
</dt> <dd>

DIALOG resource identifier, describing a dialog box template.

Not used if EPF\_USE\_HDLGTEMPLATE is set in **Flags**.

</dd> <dt>

**hDlgTemplate**
</dt> <dd>

Handle to a DLGTEMPLATE structure (described in the Microsoft Windows SDK documentation).

Used only if EPF\_USE\_HDLGTEMPLATE is set in **Flags**.

</dd> <dt>

**dwReserved**
</dt> <dd>

Reserved, must be initialized to zero.

</dd> </dl>

## Remarks

An extended push button is a CPSUI-defined type of push button that can be associated with an [**OPTITEM**](optitem.md) structure. An OPTITEM structure can have one extended push button or one extended check box associated with it.

When you use the EXTPUSH structure to create a push button, you can optionally create an additional dialog box that opens when the user clicks on the button. To create this dialog box, you should specify a pointer to a dialog box procedure in the **DlgProc** member, and include a dialog template specification in either the **DlgTemplateID** or the **hDlgTemplate** member.

If EPF\_USE\_HDLGTEMPLATE is set in **Flags**, CPSUI creates the dialog box by calling **DialogBoxIndirectParam** (described in the Windows SDK documentation), passing the contents of the **DlgProc** and **hDlgTemplate** members.

If EPF\_USE\_HDLGTEMPLATE is not set in **Flags**, CPSUI creates the dialog box by calling **DialogBoxParam** (described in the Windows SDK documentation), passing the contents of the **DlgProc** and **DlgTemplateID** members.

When the dialog box procedure is called with a *uMsg* value of WM\_INITDIALOG, the *lParam* value is the address of a [**CPSUICBPARAM**](cpsuicbparam.md) structure, with the **Reason** member set to CPSUICB\_REASON\_EXTPUSH. (For more information about the *uMsg* and *lParam* parameters, see **DialogProc** in the Windows SDK documentation.)

If you do not need CPSUI to display a dialog box when the user clicks on the button, you can specify the address of a [**\_CPSUICALLBACK**](-cpsuicallback.md)-typed callback function in the **pfnCallBack** member. When a user clicks on the button, CPSUI calls the callback function. The accompanying CPSUICBPARAM structure's **Reason** member will be set to CPSUICB\_REASON\_EXTPUSH.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Compstui.h (include Compstui.h)</dt> </dl> |



## See also

<dl> <dt>

[**EXTCHKBOX**](extchkbox.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20EXTPUSH%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





