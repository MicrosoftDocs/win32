---
Description: The CPSUICBPARAM structure is used as the input parameter to \_CPSUICALLBACK-typed callback functions.
ms.assetid: b5545efa-6cb4-41d0-9338-be9a269fa193
title: CPSUICBPARAM structure
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CPSUICBPARAM structure

The CPSUICBPARAM structure is used as the input parameter to [**\_CPSUICALLBACK**](-cpsuicallback.md)-typed callback functions.

## Syntax


```C++
typedef struct _CPSUICBPARAM {
  WORD      cbSize;
  WORD      Reason;
  HWND      hDlg;
  POPTITEM  pOptItem;
  WORD      cOptItem;
  WORD      Flags;
  POPTITEM  pCurItem;
  union {
    LONG   OldSel;
    LPTSTR pOldSel;
  };
  ULONG_PTR UserData;
  ULONG_PTR Result;
} CPSUICBPARAM, *PCPSUICBPARAM;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

CPSUI-supplied size, in bytes, of the CPSUICBPARAM structure.

</dd> <dt>

**Reason**
</dt> <dd>

CPSUI-supplied value indicating the reason it is calling the callback function. This can be one of the following values:

<dl> <dt>

<span id="CPSUICB_REASON_ABOUT"></span><span id="cpsuicb_reason_about"></span>CPSUICB\_REASON\_ABOUT
</dt> <dd>

The user has clicked on the page's **About** button, and the application previously set the CPSUIF\_ABOUT\_CALLBACK flag in a [**COMPROPSHEETUI**](compropsheetui.md) structure. CPSUI sets *pCurItem* to the value contained in **pOptItem**, and sets **pOldSel** to point to the **COMPROPSHEETUI** structure.

</dd> </dl>

<dl> <dt>

<span id="CPSUICB_REASON_APPLYNOW"></span><span id="cpsuicb_reason_applynow"></span>CPSUICB\_REASON\_APPLYNOW
</dt> <dd>

The user has clicked on the page's **Apply** or **OK** button, and CPSUI has received a PSN\_APPLY notification message (described in the Microsoft Windows SDK documentation). CPSUI sets **pCurItem** to point to the option to which **pOptItem** points. It also sets **OldSel** to minus one to indicate that all valid changed option values should be applied now.

</dd> </dl>

<dl> <dt>

<span id="CPSUICB_REASON_DLGPROC"></span><span id="cpsuicb_reason_dlgproc"></span>CPSUICB\_REASON\_DLGPROC
</dt> <dd>

The option identified by **pCurItem** is a push button ([**TVOT\_PUSHBUTTON**](print.tvot_pushbutton) option type), and the user has clicked on the button.

The push button option's OPTPARAM **Style** field is set to PUSHBUTTON\_TYPE\_DLGPROC.

</dd> </dl>

<dl> <dt>

<span id="CPSUICB_REASON_ECB_CHANGED"></span><span id="cpsuicb_reason_ecb_changed"></span>CPSUICB\_REASON\_ECB\_CHANGED
</dt> <dd>

The option identified by **pCurItem** is an extended check box, and the user has changed the box's state.

</dd> </dl>

<dl> <dt>

<span id="CPSUICB_REASON_EXTPUSH"></span><span id="cpsuicb_reason_extpush"></span>CPSUICB\_REASON\_EXTPUSH
</dt> <dd>

The option identified by **pCurItem** is an extended push button, and the user has clicked on the button.

</dd> </dl>

<dl> <dt>

<span id="CPSUICB_REASON_ITEMS_REVERTED"></span><span id="cpsuicb_reason_items_reverted"></span>CPSUICB\_REASON\_ITEMS\_REVERTED
</dt> <dd>

The user clicked on the page's **Undo** button, and CPSUI has reverted all selections to their original values.

</dd> </dl>

<dl> <dt>

<span id="CPSUICB_REASON_KILLACTIVE"></span><span id="cpsuicb_reason_killactive"></span>CPSUICB\_REASON\_KILLACTIVE
</dt> <dd>

The property sheet page is about to lose activation, and CPSUI has received a PSN\_KILLACTIVE notification message (described in the Windows SDK documentation). CPSUI sets **pCurItem** to the value contained in **pOptItem**, and sets **pOldSel** to point to the [**COMPROPSHEETUI**](compropsheetui.md) structure.

</dd> </dl>

<dl> <dt>

<span id="CPSUICB_REASON_OPTITEM_SETFOCUS"></span><span id="cpsuicb_reason_optitem_setfocus"></span>CPSUICB\_REASON\_OPTITEM\_SETFOCUS
</dt> <dd>

The option identified by **pCurItem** has received input focus.

</dd> </dl>

<dl> <dt>

<span id="CPSUICB_REASON_PUSHBUTTON"></span><span id="cpsuicb_reason_pushbutton"></span>CPSUICB\_REASON\_PUSHBUTTON
</dt> <dd>

The option identified by **pCurItem** is a push button ([**TVOT\_PUSHBUTTON**](print.tvot_pushbutton) option type), and the user has clicked on the button.

The push button item's [**OPTPARAM**](optparam.md) **Style** field is set to PUSHBUTTON\_TYPE\_CALLBACK.

</dd> </dl>

<dl> <dt>

<span id="CPSUICB_REASON_SEL_CHANGED"></span><span id="cpsuicb_reason_sel_changed"></span>CPSUICB\_REASON\_SEL\_CHANGED
</dt> <dd>

The user has changed the selected value for the option pointed to by **pCurItem**.

</dd> </dl>

<dl> <dt>

<span id="CPSUICB_REASON_SETACTIVE"></span><span id="cpsuicb_reason_setactive"></span>CPSUICB\_REASON\_SETACTIVE
</dt> <dd>

The property sheet page is about to become active, and CPSUI has received a PSN\_SETACTIVE notification message (described in the Windows SDK documentation). CPSUI sets **pCurItem** to the value contained in **pOptItem**, and sets **pOldSel** to point to the [**COMPROPSHEETUI**](compropsheetui.md) structure.

</dd> </dl> </dd> <dt>

**hDlg**
</dt> <dd>

CPSUI-supplied handle to the currently active dialog box.

</dd> <dt>

**pOptItem**
</dt> <dd>

CPSUI-supplied pointer to an array of [**OPTITEM**](optitem.md) structures. This is the same pointer that the application previously supplied in a [**COMPROPSHEETUI**](compropsheetui.md) structure.

</dd> <dt>

**cOptItem**
</dt> <dd>

CPSUI-supplied number of OPTITEM structures in the array pointed to by **pOptItem**. This is the same number that the application previously supplied in a [**COMPROPSHEETUI**](compropsheetui.md) structure.

</dd> <dt>

**Flags**
</dt> <dd>

CPSUI-supplied flags. This is the same set of flags that the application previously supplied in a [**COMPROPSHEETUI**](compropsheetui.md) structure.

</dd> <dt>

**pCurItem**
</dt> <dd>

CPSUI-supplied pointer to a member of the OPTITEM array pointed to by **pOptItem**. This array member represents the "current" option, which is the one for which the callback function was called.

</dd> <dt>

**OldSel**
</dt> <dd>

If the **Reason** member contains CPSUICB\_REASON\_SEL\_CHANGED, CPSUI sets this union to the previous contents of the **OldSel**/**pOldSel** member of the [**OPTITEM**](optitem.md) structure pointed to by **pCurItem**.

For all other **Reason** values, the contents of this union should be ignored.

</dd> <dt>

**pOldSel**
</dt> <dd>

If the **Reason** member contains CPSUICB\_REASON\_SEL\_CHANGED, CPSUI sets this union to the previous contents of the **OldSel**/**pOldSel** member of the [**OPTITEM**](optitem.md) structure pointed to by **pCurItem**.

For all other **Reason** values, the contents of this union should be ignored.

</dd> <dt>

**UserData**
</dt> <dd>

CPSUI-supplied user data. This is the same value that the application previously supplied in a [**COMPROPSHEETUI**](compropsheetui.md) structure.

</dd> <dt>

**Result**
</dt> <dd>

Result value supplied by the [**\_CPSUICALLBACK**](-cpsuicallback.md)-typed callback function. By default, CPSUI sets this value to CPSUI\_OK. After the callback function returns, CPSUI calls its [**ComPropSheet**](compropsheet.md) function with a function code of [**CPSFUNC\_SET\_RESULT**](print.cpsfunc_set_result), supplying the **Reason** member contents as the result value.

This member is used only if the **Reason** member is CPSUICB\_REASON\_APPLYNOW and the callback function does not return CPSUI\_ACTION\_NO\_APPLY\_EXIT.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Compstui.h (include Compstui.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20CPSUICBPARAM%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




