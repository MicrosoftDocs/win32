---
Description: The COMPROPSHEETUI structure is used as an input parameter to CPSUIs ComPropSheet function, if the function code is CPSFUNC\_ADD\_PCOMPROPSHEETUI. All structure members must be supplied by the caller of ComPropSheet.
ms.assetid: 7ebf46b7-5c31-482e-8644-a3d81f7dc5cc
title: COMPROPSHEETUI structure
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# COMPROPSHEETUI structure

The COMPROPSHEETUI structure is used as an input parameter to CPSUI's [**ComPropSheet**](compropsheet.md) function, if the function code is [**CPSFUNC\_ADD\_PCOMPROPSHEETUI**](print.cpsfunc_add_pcompropsheetui). All structure members must be supplied by the caller of *ComPropSheet*.

## Syntax


```C++
typedef struct _COMPROPSHEETUI {
  WORD           cbSize;
  WORD           Flags;
  HINSTANCE      hInstCaller;
  LPTSTR         pCallerName;
  ULONG_PTR      UserData;
  LPTSTR         pHelpFile;
  _CPSUICALLBACK pfnCallBack;
  POPTITEM       pOptItem;
  PDLGPAGE       pDlgPage;
  WORD           cOptItem;
  WORD           cDlgPage;
  ULONG_PTR      IconID;
  LPTSTR         pOptItemName;
  WORD           CallerVersion;
  WORD           OptItemVersion;
  ULONG_PTR      dwReserved[4];
} COMPROPSHEETUI, *PCOMPROPSHEETUI;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

Caller-supplied size, in bytes, of the COMPROPSHEETUI structure.

</dd> <dt>

**Flags**
</dt> <dd>

Optional caller-supplied bit flags, as described in the following list:

<dl> <dt>

<span id="CPSUIF_ABOUT_CALLBACK"></span><span id="cpsuif_about_callback"></span>CPSUIF\_ABOUT\_CALLBACK
</dt> <dd>

If set, the page's callback function (pointed to by the structure's **pfnCallback** member), supports CPSUICB\_REASON\_ABOUT, so CPSUI will call the callback function if the user clicks on the page's **About** button. (CPSUI supplies an **About** button for each treeview root node.)

</dd> </dl>

<dl> <dt>

<span id="CPSUIF_ICONID_AS_HICON"></span><span id="cpsuif_iconid_as_hicon"></span>CPSUIF\_ICONID\_AS\_HICON
</dt> <dd>

If set, the structure's **IconID** member contains an icon handle.

If not set, the **IconID** member contains an icon resource identifier.

</dd> </dl>

<dl> <dt>

<span id="CPSUIF_UPDATE_PERMISSION"></span><span id="cpsuif_update_permission"></span>CPSUIF\_UPDATE\_PERMISSION
</dt> <dd>

If set, the page's option values can be modified by the user.

</dd> </dl> </dd> <dt>

**hInstCaller**
</dt> <dd>

Caller-supplied module instance handle, received by the DLL's entry point function.

</dd> <dt>

**pCallerName**
</dt> <dd>

Caller-supplied pointer to a NULL-terminated text string representing the application's name. (For a printer interface DLL, this should be the driver's name, such as "PostScript Driver".)

</dd> <dt>

**UserData**
</dt> <dd>

Optional caller-supplied value, which CPSUI places in a [**CPSUICBPARAM**](cpsuicbparam.md) structure's **UserData** member when calling the function pointed to by **pfnCallBack**.

</dd> <dt>

**pHelpFile**
</dt> <dd>

Caller-supplied pointer to a NULL-terminated text string representing a path to a help file. For printer interface DLLs, this is typically the help file path obtained by calling GetPrinterDriver (described in the Microsoft Windows SDK documentation).

The help file is indexed by values contained in the **HelpIndex** member of [**OPTITEM**](optitem.md) structures.

</dd> <dt>

**pfnCallBack**
</dt> <dd>

Caller-supplied pointer to a [**\_CPSUICALLBACK**](-cpsuicallback.md)-typed callback function, which CPSUI calls when a user modifies the page's option values.

Can be used only if **pDlgPage** identifies a CPSUI-supplied [**DLGPAGE**](dlgpage.md) structure, or if the **DlgProc** member of an application-supplied DLGPAGE structure is **NULL**.

</dd> <dt>

**pOptItem**
</dt> <dd>

Caller-supplied pointer to an array of [**OPTITEM**](optitem.md) structures describing the page's options.

</dd> <dt>

**pDlgPage**
</dt> <dd>

This member specifies [**DLGPAGE**](dlgpage.md) structures that describe pages to be added to the property sheet. It can be either of the following:

-   A pointer to an array of DLGPAGE structures.

-   One of the pointers that is described in the following list. These pointers reference predefined DLGPAGE structures, supplied by CPSUI for use by printer interface DLLs.

    <dl> <dt>

<span id="CPSUI_PDLGPAGE_ADVDOCPROP"></span><span id="cpsui_pdlgpage_advdocprop"></span>CPSUI\_PDLGPAGE\_ADVDOCPROP
</dt> <dd>

    Defines one treeview page whose tab reads **Advanced**.

    For use only by a [**DrvDocumentPropertySheets**](drvdocumentpropertysheets.md) function.

    </dd> </dl>

    <dl> <dt>

<span id="CPSUI_PDLGPAGE_DOCPROP"></span><span id="cpsui_pdlgpage_docprop"></span>CPSUI\_PDLGPAGE\_DOCPROP
</dt> <dd>

    Defines three pages, whose tabs are **Layout**, **Paper/Quality**, and **Advanced**. The **Advanced** page is a treeview.

    For use only by a [**DrvDocumentPropertySheets**](drvdocumentpropertysheets.md) function.

    </dd> </dl>

    <dl> <dt>

<span id="CPSUI_PDLGPAGE_PRINTERPROP"></span><span id="cpsui_pdlgpage_printerprop"></span>CPSUI\_PDLGPAGE\_PRINTERPROP
</dt> <dd>

    Defines one treeview page whose tab reads **Device Settings**.

    For use only by a [**DrvDevicePropertySheets**](drvdevicepropertysheets.md) function.

    </dd> </dl>

    <dl> <dt>

<span id="CPSUI_PDLGPAGE_TREEVIEWONLY"></span><span id="cpsui_pdlgpage_treeviewonly"></span>CPSUI\_PDLGPAGE\_TREEVIEWONLY
</dt> <dd>

    Defines one treeview page.

    </dd> </dl>

</dd> <dt>

**cOptItem**
</dt> <dd>

Caller-supplied number of [**OPTITEM**](optitem.md) structures pointed to by **pOptItem**.

</dd> <dt>

**cDlgPage**
</dt> <dd>

Caller-supplied number of [**DLGPAGE**](dlgpage.md) structures pointed to by **pDlgPage**. Not used if **pDlgPage** specifies a predefined CPSUI\_PDLGPAGE-prefixed structure.

</dd> <dt>

**IconID**
</dt> <dd>

Caller-supplied, can be one of the following:

-   An icon resource identifier. This can be application-defined, or it can be one of the CPSUI-supplied, IDI\_CPSUI-prefixed icon resource identifiers.

-   An icon handle. If a handle is specified, CPSUIF\_ICONID\_AS\_HICON must be set in the **Flags** member.

The specified icon is displayed in the root node of the property sheet page's treeview.

</dd> <dt>

**pOptItemName**
</dt> <dd>

Caller-supplied pointer to a NULL-terminated string to be displayed in the root node of the property sheet page's treeview. For printer interface DLLs, this string typically represents a printer device type, such as "HP 4si".

</dd> <dt>

**CallerVersion**
</dt> <dd>

Caller-supplied version number, representing the calling application's current version. The high byte identifies the major version, and the low byte is the minor version. For example, a **CallerVersion** value of 0x310 specifies a caller version number of 3.16. The version number is displayed when a user clicks on a page's **About** button.

</dd> <dt>

**OptItemVersion**
</dt> <dd>

Caller-supplied version number, representing the root-level option item's current version. For printer interface DLLs, this typically represents a printer device version. The high byte identifies the major version, and the low byte is the minor version. For example, an **OptItemVersion** value of 0x3ff specifies a caller version number of 3.255. The version number is displayed when a user clicks on a page's **About** button.

</dd> <dt>

**dwReserved**
</dt> <dd>

Reserved. This array must be set to zero.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Compstui.h (include Compstui.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20COMPROPSHEETUI%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




