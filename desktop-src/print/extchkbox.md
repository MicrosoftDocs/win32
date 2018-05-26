---
Description: The EXTCHKBOX structure is used by CPSUI applications (including printer interface DLLs) for specifying an extended check box, which can be added to a property sheet page option.
ms.assetid: b3b82474-d4e5-467c-93dc-30edac189c66
title: EXTCHKBOX structure
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# EXTCHKBOX structure

The EXTCHKBOX structure is used by CPSUI applications (including printer interface DLLs) for specifying an extended check box, which can be added to a property sheet page option.

## Syntax


```C++
typedef struct _EXTCHKBOX {
  WORD      cbSize;
  WORD      Flags;
  LPTSTR    pTitle;
  LPTSTR    pSeparator;
  LPTSTR    pCheckedName;
  ULONG_PTR IconID;
  WORD      wReserved[4];
  ULONG_PTR dwReserved[2];
} EXTCHKBOX, *PEXTCHKBOX;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

Size, in bytes, of the EXTCHKBOX structure.

</dd> <dt>

**Flags**
</dt> <dd>

Bit flags, which can be one of the following:

<dl> <dt>

<span id="ECBF_CHECKNAME_AT_FRONT"></span><span id="ecbf_checkname_at_front"></span>ECBF\_CHECKNAME\_AT\_FRONT
</dt> <dd>

If set, CPSUI displays strings in the order "pCheckedName pSeparator *SelectName*", where *SelectName* is the string associated with the option's selected value.

If not set, CPSUI displays strings in the order "*SelectName* pSeparator pCheckedName".

</dd> </dl>

<dl> <dt>

<span id="ECBF_CHECKNAME_ONLY_ENABLED"></span><span id="ecbf_checkname_only_enabled"></span>ECBF\_CHECKNAME\_ONLY\_ENABLED
</dt> <dd>

If set, CPSUI displays the pCheckedName string only if the option is checked and enabled (that is, OPTIF\_ECB\_CHECKED is set and OPTIF\_DISABLED is clear in the OPTITEM structure).

If not set, CPSUI always displays the pCheckedName string if the option is checked (that is, OPTIF\_ECB\_CHECKED is set in the OPTITEM structure), even if the option is disabled.

</dd> </dl>

<dl> <dt>

<span id="ECBF_ICONID_AS_HICON"></span><span id="ecbf_iconid_as_hicon"></span>ECBF\_ICONID\_AS\_HICON
</dt> <dd>

If set, the **IconID** member contains an icon handle.

If not set, the **IconID** member contains an icon resource identifier.

</dd> </dl>

<dl> <dt>

<span id="ECBF_OVERLAY_ECBICON_IF_CHECKED"></span><span id="ecbf_overlay_ecbicon_if_checked"></span>ECBF\_OVERLAY\_ECBICON\_IF\_CHECKED
</dt> <dd>

If set, and if the check box is checked (that is, OPTIF\_ECB\_CHECKED is set in the OPTITEM structure), CPSUI overlays the icon identified by the **IconID** member onto the icon associated with the option item.

</dd> </dl>

<dl> <dt>

<span id="ECBF_OVERLAY_NO_ICON"></span><span id="ecbf_overlay_no_icon"></span>ECBF\_OVERLAY\_NO\_ICON
</dt> <dd>

If set, CPSUI overlays its IDI\_CPSUI\_NO icon onto the icon identified by the **IconID** member.

</dd> </dl>

<dl> <dt>

<span id="ECBF_OVERLAY_STOP_ICON"></span><span id="ecbf_overlay_stop_icon"></span>ECBF\_OVERLAY\_STOP\_ICON
</dt> <dd>

If set, CPSUI overlays the IDI\_CPSUI\_STOP icon onto the icon identified by the **IconID** member.

</dd> </dl>

<dl> <dt>

<span id="ECBF_OVERLAY_WARNING_ICON"></span><span id="ecbf_overlay_warning_icon"></span>ECBF\_OVERLAY\_WARNING\_ICON
</dt> <dd>

If set, CPSUI overlays its IDI\_CPSUI\_WARNING icon onto the icon identified by the **IconID** member.

</dd> </dl> </dd> <dt>

**pTitle**
</dt> <dd>

String identifier, representing the check box title. This can be a 32-bit pointer to a NULL-terminated string, or it can be a 16-bit string resource identifier with HIWORD set to zero.

</dd> <dt>

**pSeparator**
</dt> <dd>

String identifier, representing a separator character to be displayed between the checked name string and the selected option string This can be a 32-bit pointer to a NULL-terminated string, or it can be a 16-bit string resource identifier with HIWORD set to zero.

</dd> <dt>

**pCheckedName**
</dt> <dd>

String identifier, representing the text to be displayed when the check box is checked. This can be a 32-bit pointer to a NULL-terminated string, or it can be a 16-bit string resource identifier with HIWORD set to zero.

</dd> <dt>

**IconID**
</dt> <dd>

One of the following icon identifiers:

-   An icon resource identifier. This can be application-defined, or it can be one of the CPSUI-supplied, IDI\_CPSUI-prefixed icon resource identifiers.

-   An icon handle. If a handle is specified, ECBF\_ICONID\_AS\_HICON must be set in the **Flags** member.

If this value is zero, an icon is not displayed.

</dd> <dt>

**wReserved**
</dt> <dd>

Reserved, must be initialized to zero.

</dd> <dt>

**dwReserved**
</dt> <dd>

Reserved, must be initialized to zero.

</dd> </dl>

## Remarks

An extended check box is a CPSUI-defined type of check box that can be associated with an [**OPTITEM**](optitem.md) structure. An OPTITEM structure can have one extended check box or one extended push button associated with it.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Compstui.h (include Compstui.h)</dt> </dl> |



## See also

<dl> <dt>

[**EXTPUSH**](extpush.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20EXTCHKBOX%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





