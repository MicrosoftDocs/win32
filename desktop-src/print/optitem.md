---
Description: The OPTITEM structure is used by CPSUI applications (including printer interface DLLs) for describing one property sheet option on a property sheet page, if the page is described by a COMPROPSHEETUI structure.
ms.assetid: 983f9774-d498-473a-bdfb-ec55cc4298cf
title: OPTITEM structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# OPTITEM structure

The OPTITEM structure is used by CPSUI applications (including printer interface DLLs) for describing one [property sheet option](https://www.bing.com/search?q=property+sheet+option) on a property sheet page, if the page is described by a [**COMPROPSHEETUI**](compropsheetui.md) structure.

## Syntax


```C++
typedef struct _OPTITEM {
  WORD      cbSize;
  BYTE      Level;
  BYTE      DlgPageIdx;
  DWORD     Flags;
  ULONG_PTR UserData;
  LPTSTR    pName;
  union {
    LONG   Sel;
    LPTSTR pSel;
  };
  union {
    PEXTCHKBOX pExtChkBox;
    PEXTPUSH   pExtPush;
  };
  POPTTYPE  pOptType;
  DWORD     HelpIndex;
  BYTE      DMPubID;
  BYTE      UserItemID;
  WORD      wReserved;
  POIEXT    pOIExt;
  ULONG_PTR dwReserved[3];
} OPTITEM, *POPTITEM;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

Size, in bytes, of the OPTITEM structure.

</dd> <dt>

**Level**
</dt> <dd>

Specifies the level of this option in the treeview. For more information, see the following Remarks section.

</dd> <dt>

**DlgPageIdx**
</dt> <dd>

Identifies the dialog to which the option belongs. Specifies an array index into the DLGPAGE array pointed to by the **pDlgPage** member of the [**COMPROPSHEETUI**](compropsheetui.md) structure.

If **pDlgPage** points to a CPSUI-supplied, predefined DLGPAGE structure, CPSUI supplies this index.

</dd> <dt>

**Flags**
</dt> <dd>

Optional bit flags that modify the option's characteristics. The OPTIF\_CHANGEONCE flag is set by CPSUI; all other flags are set by the caller. Any combination of the following flags can be set.

<dl> <dt>

<span id="OPTIF_CALLBACK"></span><span id="optif_callback"></span>OPTIF\_CALLBACK
</dt> <dd>

When a user modifies the option, CPSUI should call the [**\_CPSUICALLBACK**](-cpsuicallback.md)-typed callback function specified in the [**COMPROPSHEETUI**](compropsheetui.md) structure.

</dd> </dl>

<dl> <dt>

<span id="OPTIF_CHANGED"></span><span id="optif_changed"></span>OPTIF\_CHANGED
</dt> <dd>

The **\_CPSUICALLBACK**-typed callback function should set this flag if it modified the option, so that CPSUI will redisplay it.

</dd> </dl>

<dl> <dt>

<span id="OPTIF_CHANGEONCE"></span><span id="optif_changeonce"></span>OPTIF\_CHANGEONCE
</dt> <dd>

CPSUI sets this bit if a user modified the option.

</dd> </dl>

<dl> <dt>

<span id="OPTIF_COLLAPSE"></span><span id="optif_collapse"></span>OPTIF\_COLLAPSE
</dt> <dd>

Collapse this option and its children so that it is not expanded in the treeview.

</dd> </dl>

<dl> <dt>

<span id="OPTIF_DISABLED"></span><span id="optif_disabled"></span>OPTIF\_DISABLED
</dt> <dd>

Disables the option so that it is not user-modifiable.

</dd> </dl>

<dl> <dt>

<span id="OPTIF_ECB_CHECKED"></span><span id="optif_ecb_checked"></span>OPTIF\_ECB\_CHECKED
</dt> <dd>

The associated extended check box is in the checked state.

</dd> </dl>

<dl> <dt>

<span id="OPTIF_EXT_IS_EXTPUSH"></span><span id="optif_ext_is_extpush"></span>OPTIF\_EXT\_IS\_EXTPUSH
</dt> <dd>

If set, the **pExtPush** member is valid (unless **NULL**).

If not set, the **pExtChkBox** member is valid (unless **NULL**).

</dd> </dl>

<dl> <dt>

<span id="OPTIF_EXT_DISABLED"></span><span id="optif_ext_disabled"></span>OPTIF\_EXT\_DISABLED
</dt> <dd>

The extended check box or extended push button is not selectable.

</dd> </dl>

<dl> <dt>

<span id="OPTIF_EXT_HIDE"></span><span id="optif_ext_hide"></span>OPTIF\_EXT\_HIDE
</dt> <dd>

CPSUI will not display the extended check box or extended push button.

</dd> </dl>

<dl> <dt>

<span id="OPTIF_HAS_POIEXT"></span><span id="optif_has_poiext"></span>OPTIF\_HAS\_POIEXT
</dt> <dd>

If set, the **pOIExt** member is valid.

</dd> </dl>

<dl> <dt>

<span id="OPTIF_HIDE"></span><span id="optif_hide"></span>OPTIF\_HIDE
</dt> <dd>

CPSUI will not display this option in the treeview. CPSUI examines this flag only when initially creating the treeview, so changing the flag from its initial value has no effect.

</dd> </dl>

<dl> <dt>

<span id="_OPTIF_INITIAL_TVITEM"></span><span id="_optif_initial_tvitem"></span> OPTIF\_INITIAL\_TVITEM
</dt> <dd>

If set, CPSUI sets the initial window focus to this option when it displays the treeview. CPSUI expands tree nodes and scrolls the option into view as necessary. If the option is hidden, or if this flag is not set for any OPTITEM structure, CPSUI chooses the initial focus.

</dd> </dl>

<dl> <dt>

<span id="OPTIF_NO_GROUPBOX_NAME"></span><span id="optif_no_groupbox_name"></span>OPTIF\_NO\_GROUPBOX\_NAME
</dt> <dd>

If not set, and **pOptype** is not zero, CPSUI uses the **pName** string as the groupbox title.

If set, CPSUI provides a groupbox title.

</dd> </dl>

<dl> <dt>

<span id="OPTIF_OVERLAY_NO_ICON"></span><span id="optif_overlay_no_icon"></span>OPTIF\_OVERLAY\_NO\_ICON
</dt> <dd>

If set CPSUI overlays its IDI\_CPSUI\_NO icon onto the icon associated with the option. (See the **Sel/pSel** member.)

</dd> </dl>

<dl> <dt>

<span id="OPTIF_OVERLAY_STOP_ICON"></span><span id="optif_overlay_stop_icon"></span>OPTIF\_OVERLAY\_STOP\_ICON
</dt> <dd>

If set, CPSUI overlays its IDI\_CPSUI\_STOP icon onto the icon associated with the option. (See the **Sel/pSel** member.)

</dd> </dl>

<dl> <dt>

<span id="OPTIF_OVERLAY_WARNING_ICON"></span><span id="optif_overlay_warning_icon"></span>OPTIF\_OVERLAY\_WARNING\_ICON
</dt> <dd>

If set, CPSUI overlays its IDI\_CPSUI\_WARNING icon onto the icon associated with the option. (See the **Sel/pSel** member.)

</dd> </dl>

<dl> <dt>

<span id="OPTIF_SEL_AS_HICON"></span><span id="optif_sel_as_hicon"></span>OPTIF\_SEL\_AS\_HICON
</dt> <dd>

If set, the **Sel** member contains an icon handle.

If not set, the **Sel** member contains an icon resource identifier.

This flag can only be used when **pOptType** contains **NULL**.

</dd> </dl> </dd> <dt>

**UserData**
</dt> <dd>

Optional 32-bit value that can be set and used by the caller.

(Printer interface DLLs for [*Unidrv*](https://msdn.microsoft.com/0a51fa2b-3d09-4a5f-9fff-40604877a414) and [*Pscript*](https://msdn.microsoft.com/139a10e9-203b-499b-9291-8537eae9189c) use this member to supply a pointer to a [**USERDATA**](userdata.md) structure. [User interface plug-ins](https://www.bing.com/search?q=User+interface+plug-ins) can reference this structure.)

</dd> <dt>

**pName**
</dt> <dd>

String identifier representing a localized, displayable option name. This can be a 32-bit pointer to a NULL-terminated string, or it can be a 16-bit string resource identifier, with HIWORD set to zero. (Also see the description of **DMPubID**, below.)

</dd> <dt>

**Sel**
</dt> <dd>

This union indicates the option's currently selected parameter value. Its usage is dependent on the [CPSUI option type](https://www.bing.com/search?q=CPSUI+option+type).

If **pOptType** is **NULL**, the option has no parameters, so this union identifies an icon to be associated with the treeview node for the option. The icon identifier can be either an icon handle or an icon resource identifier, as indicated by OPTIF\_SEL\_AS\_HICON in **Flags**.

</dd> <dt>

**pSel**
</dt> <dd>

This union indicates the option's currently selected parameter value. Its usage is dependent on the [CPSUI option type](https://www.bing.com/search?q=CPSUI+option+type).

If **pOptType** is **NULL**, the option has no parameters, so this union identifies an icon to be associated with the treeview node for the option. The icon identifier can be either an icon handle or an icon resource identifier, as indicated by OPTIF\_SEL\_AS\_HICON in **Flags**.

</dd> <dt>

**pExtChkBox**
</dt> <dd>

Pointer to EXTCHKBOX structure

</dd> <dt>

**pExtPush**
</dt> <dd>

This union can be a pointer to an [**EXTCHKBOX**](extchkbox.md) structure, a pointer to an [**EXTPUSH**](extpush.md) structure, or **NULL**.

An OPTITEM structure can optionally have an EXTCHKBOX structure, an EXTPUSH structure, or neither, associated with it. If this union is not **NULL**, and if OPTIF\_EXT\_IS\_EXTPUSH is set in **Flags**, **pExtPush** is valid. If the flag is not set, **pExtChkBox** is valid.

</dd> <dt>

**pOptType**
</dt> <dd>

Pointer to an [**OPTTYPE**](opttype.md) structure that describes the option's display type. If **NULL**, the option has no parameters and is used as a parent to options with a higher **Level** value. The child options must immediately follow the parent in the OPTITEM array. (See the following Remarks section.)

</dd> <dt>

**HelpIndex**
</dt> <dd>

Help file index, which identifies help text to be associated with the option. If zero, help file text does not exist for this option. Note that the **pOIExt** member of this structure must be set with the address of an [**OIEXT**](oiext.md) structure in order for help text functionality to exist.

</dd> <dt>

**DMPubID**
</dt> <dd>

This member is meant for use by printer interface DLLs, when creating a **Document Properties** property sheet (see [**DrvDocumentPropertySheets**](drvdocumentpropertysheets.md)). It is a constant value specifying which, if any, public member of the [**DEVMODEW**](https://msdn.microsoft.com/b2369876-9a79-40c8-8d27-c8b9d8e68e6b) structure is associated with this option. The following table lists available constants, the associated DEVMODE structure member, and the required value for **pName** for each constant.



Constant Value

Public DEVMODE

Required pName Value

Structure Member

DMPUB\_COLOR<br/>

**dmColor**<br/>

IDS\_CPSUI\_COLOR\_APPERANCE<br/>

DMPUB\_COPIES\_COLLATE<br/>

**dmCopies** and **dmCollate**<br/>

IDS\_CPSUI\_COPIES<br/>

DMPUB\_DEFSOURCE<br/>

**dmDefSource**<br/>

IDS\_CPSUI\_SOURCE<br/>

DMPUB\_DITHERTYPE<br/>

**dmDitherType**<br/>

IDS\_CPSUI\_DITHERING<br/>

DMPUB\_DUPLEX<br/>

**dmDuplex**<br/>

IDS\_CPSUI\_DUPLEX<br/>

DMPUB\_FORMNAME<br/>

**dmFormName**<br/>

IDS\_CPSUI\_FORMNAME<br/>

DMPUB\_ICMINTENT<br/>

**dmICMIntent**<br/>

IDS\_CPSUI\_ICMINTENT<br/>

DMPUB\_ICMMETHOD<br/>

**dmICMMethod**<br/>

IDS\_CPSUI\_ICMMETHOD<br/>

DMPUB\_MEDIATYPE<br/>

**dmMediaType**<br/>

IDS\_CPSUI\_MEDIA<br/>

DMPUB\_NUP<br/>

Not contained in public section of DEVMODE.<br/>

IDS\_CPSUI\_NUP<br/>

DMPUB\_ORIENTATION<br/>

**dmOrientation**<br/>

IDS\_CPSUI\_ORIENTATION<br/>

DMPUB\_OUTPUTBIN<br/>

Not contained in public section of DEVMODE.<br/>

IDS\_CPSUI\_OUTPUTBIN<br/>

DMPUB\_PAGEORDER<br/>

Not contained in public section of DEVMODE.<br/>

IDS\_CPSUI\_PAGEORDER<br/>

DMPUB\_PRINTQUALITY<br/>

**dmPrintQuality**<br/>

IDS\_CPSUI\_PRINTQUALITY or IDS\_CPSUI\_RESOLUTION.<br/> If not specified, the default name is IDS\_CPSUI\_RESOLUTION.<br/>

DMPUB\_QUALITY<br/>

Not contained in public section of DEVMODE.<br/>

IDS\_CPSUI\_QUALITY\_SETTINGS<br/>

DMPUB\_SCALE<br/>

**dmScale**<br/>

IDS\_CPSUI\_SCALE<br/>

DMPUB\_TTOPTION<br/>

**dmTTOption**<br/>

IDS\_CPSUI\_TTOPTION<br/>

DMPUB\_NONE<br/>

Not contained in public section of DEVMODE.<br/>

Greater than or equal to DMPUB\_USER<br/>

Ignored by CPSUI, can be a caller-defined value.<br/>



 

CPSUI does not maintain a DEVMODE structure. The application is responsible for copying user-selected option parameters into a DEVMODE structure. CPSUI uses **DMPubID** contents to determine treeview placement of standard options, and to determine the contents of the **Layout** and **Paper/Quality** tabs (see the **pDlgPage** member of the [**COMPROPSHEETUI**](compropsheetui.md) structure).

For additional information about using the **DMPubID** member, see the following Remarks section.

</dd> <dt>

**UserItemID**
</dt> <dd>

Optional application-supplied value that can be used for option identification purposes. Not referenced by CPSUI.

</dd> <dt>

**wReserved**
</dt> <dd>

Reserved, must be initialized to zero.

</dd> <dt>

**pOIExt**
</dt> <dd>

Pointer to an optional [**OIEXT**](oiext.md) structure. The caller is responsible for allocating storage for this structure.

</dd> <dt>

**dwReserved**
</dt> <dd>

Reserved, must be initialized to zero.

</dd> </dl>

## Remarks

OPTITEM structures should be placed in an array, and the array's address should be placed in the **pOptItem** member of a [**COMPROPSHEETUI**](compropsheetui.md) structure.

The **Level** member allows you to create child nodes in the treeview. For example, to create a set of option nodes under a level 1 parent node, specify level 2 for each child node and include their OPTITEM structures in the OPTITEM array, immediately after the parent's OPTITEM structure. In the parent's OPTITEM structure, **pOptType** should be **NULL**.

The treeview root node is level 0. Options displayed when a user expands the root node are level 1. The maximum number of levels is 256.

For option values that are stored in a printer's DEVMODE structure, the **DMPubID** member must identify the option. For each **DMPubID** value that is used, a printer interface DLL must specify the [CPSUI option type](https://www.bing.com/search?q=CPSUI+option+type) listed in the following table.



| DMPubID Value                     | Required CPSUI Option Type                                                                                                  |
|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| DMPUB\_COLOR<br/>           | [**TVOT\_2STATES**](https://www.bing.com/search?q=**TVOT\_2STATES**)<br/>                                                                          |
| DMPUB\_COPIES\_COLLATE<br/> | [**TVOT\_UDARROW**](https://www.bing.com/search?q=**TVOT\_UDARROW**) plus [**EXTCHKBOX**](extchkbox.md) (See comments following this table.)<br/> |
| DMPUB\_DEFSOURCE<br/>       | [**TVOT\_LISTBOX**](https://www.bing.com/search?q=**TVOT\_LISTBOX**)<br/>                                                                          |
| DMPUB\_DITHERTYPE<br/>      | [**TVOT\_LISTBOX**](https://www.bing.com/search?q=**TVOT\_LISTBOX**)<br/>                                                                          |
| DMPUB\_DUPLEX<br/>          | [**TVOT\_2STATES**](https://www.bing.com/search?q=**TVOT\_2STATES**) or [**TVOT\_3STATES**](https://www.bing.com/search?q=**TVOT\_3STATES**)<br/>                               |
| DMPUB\_FORMNAME<br/>        | [**TVOT\_LISTBOX**](https://www.bing.com/search?q=**TVOT\_LISTBOX**)<br/>                                                                          |
| DMPUB\_ICMINTENT<br/>       | [**TVOT\_2STATES**](https://www.bing.com/search?q=**TVOT\_2STATES**) or [**TVOT\_3STATES**](https://www.bing.com/search?q=**TVOT\_3STATES**)<br/>                               |
| DMPUB\_ICMMETHOD<br/>       | [**TVOT\_2STATES**](https://www.bing.com/search?q=**TVOT\_2STATES**) or [**TVOT\_3STATES**](https://www.bing.com/search?q=**TVOT\_3STATES**)<br/>                               |
| DMPUB\_MEDIATYPE<br/>       | [**TVOT\_LISTBOX**](https://www.bing.com/search?q=**TVOT\_LISTBOX**)<br/>                                                                          |
| DMPUB\_NUP<br/>             | [**TVOT\_LISTBOX**](https://www.bing.com/search?q=**TVOT\_LISTBOX**)<br/>                                                                          |
| DMPUB\_ORIENTATION<br/>     | [**TVOT\_2STATES**](https://www.bing.com/search?q=**TVOT\_2STATES**) or [**TVOT\_3STATES**](https://www.bing.com/search?q=**TVOT\_3STATES**)<br/>                               |
| DMPUB\_OUTPUTBIN<br/>       | [**TVOT\_LISTBOX**](https://www.bing.com/search?q=**TVOT\_LISTBOX**)<br/>                                                                          |
| DMPUB\_PAGEORDER<br/>       | [**TVOT\_2STATES**](https://www.bing.com/search?q=**TVOT\_2STATES**) or [**TVOT\_3STATES**](https://www.bing.com/search?q=**TVOT\_3STATES**)<br/>                               |
| DMPUB\_PRINTQUALITY<br/>    | [**TVOT\_LISTBOX**](https://www.bing.com/search?q=**TVOT\_LISTBOX**)<br/>                                                                          |
| DMPUB\_QUALITY<br/>         | [**TVOT\_2STATES**](https://www.bing.com/search?q=**TVOT\_2STATES**) or [**TVOT\_3STATES**](https://www.bing.com/search?q=**TVOT\_3STATES**)<br/>                               |
| DMPUB\_SCALE<br/>           | [**TVOT\_UDARROW**](https://www.bing.com/search?q=**TVOT\_UDARROW**)<br/>                                                                          |
| DMPUB\_TTOPTION<br/>        | [**TVOT\_LISTBOX**](https://www.bing.com/search?q=**TVOT\_LISTBOX**)<br/>                                                                          |



 

If **DMPubID** is DMPUB\_COPIES\_COLLATE and the printer can collate copies, an extended check box (EXTCHKBOX structure) must be provided. The EXTCHCKBOX structure's members must be set as follows:


```
pExtCheckbox->cbSize = sizeof(EXTCHKBOX);
pExtCheckbox->pTitle = (PWSTR) IDS_CPSUI_COLLATE;
pExtCheckbox->pCheckedName = (PWSTR) IDS_CPSUI_COLLATED;
pExtCheckbox->IconID = IDI_CPSUI_COLLATE;
pExtCheckbox->Flags = ECBF_CHECKNAME_ONLY_ENABLED;
pExtCheckbox->pSeparator = (PWSTR)IDS_CPSUI_SLASH_SEP;
```



If OPTIF\_EXT\_HIDE is not set in **Flags**, CPSUI enables the check box if a user requests more than one copy, and disables it if only one copy is requested.

Additionally, CPSUI sets the option's display text to **copy** for one copy and **copies** for more than one copy.

If **DMPubID** is DMPUB\_COLOR, its first [**OPTPARAM**](optparam.md) structure (**Sel**=0) must represent Gray Scale, and **pData** in the OPTPARAM structure must be IDS\_CPSUI\_GRAYSCALE. Its second OPTPARAM structure (**Sel**=1) must represent Color, and **pData** in the OPTPARAM structure must be IDS\_CPSUI\_COLOR. If another option's **DMPubID** is DMPUB\_ICMINTENT and if Color is not selected, CPSUI disables the option for which DMPUB\_ICMINTENT is specified.

CPSUI disables color matching when Color is not selected.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Compstui.h (include Compstui.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20OPTITEM%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




