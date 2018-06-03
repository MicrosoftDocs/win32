---
Description: An array of OPTPARAM structures is used by CPSUI applications (including printer interface DLLs) for describing all the parameter values associated with a property sheet option. The array's address is included in an OPTTYPE structure.
ms.assetid: d0cd2867-783c-4a41-a819-e919d4ffc1e3
title: OPTPARAM structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# OPTPARAM structure

An array of OPTPARAM structures is used by CPSUI applications (including printer interface DLLs) for describing all the parameter values associated with a [property sheet option](https://www.bing.com/search?q=property sheet option). The array's address is included in an [**OPTTYPE**](opttype.md) structure.

## Syntax


```C++
typedef struct _OPTPARAM {
  WORD      cbSize;
  BYTE      Flags;
  BYTE      Style;
  LPTSTR    pData;
  ULONG_PTR IconID;
  LPARAM    lParam;
  ULONG_PTR dwReserved[2];
} OPTPARAM, *POPTPARAM;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

Size, in bytes, of the OPTPARAM structure.

</dd> <dt>

**Flags**
</dt> <dd>

Optional bit flags that modify the parameter's characteristics. The following flags can be set in any combination:

<dl> <dt>

<span id="OPTPF_DISABLED"></span><span id="optpf_disabled"></span>OPTPF\_DISABLED
</dt> <dd>

If set, the parameter is not user-selectable. Can be used with the following option types:

[**TVOT\_2STATES**](https://www.bing.com/search?q=**TVOT\_2STATES**)

[**TVOT\_3STATES**](https://www.bing.com/search?q=**TVOT\_3STATES**)

[**TVOT\_COMBOBOX**](https://www.bing.com/search?q=**TVOT\_COMBOBOX**)

[**TVOT\_LISTBOX**](https://www.bing.com/search?q=**TVOT\_LISTBOX**)

</dd> </dl>

<dl> <dt>

<span id="OPTPF_HIDE"></span><span id="optpf_hide"></span>OPTPF\_HIDE
</dt> <dd>

If set, the parameter not displayed in the treeview. Can be used with the following option types:

[**TVOT\_3STATES**](https://www.bing.com/search?q=**TVOT\_3STATES**)

[**TVOT\_COMBOBOX**](https://www.bing.com/search?q=**TVOT\_COMBOBOX**)

[**TVOT\_LISTBOX**](https://www.bing.com/search?q=**TVOT\_LISTBOX**)

</dd> </dl>

<dl> <dt>

<span id="OPTPF_ICONID_AS_HICON"></span><span id="optpf_iconid_as_hicon"></span>OPTPF\_ICONID\_AS\_HICON
</dt> <dd>

If set, the **IconID** member contains an icon handle.

If not set, the **IconID** member contains an icon resource identifier.

</dd> </dl>

<dl> <dt>

<span id="OPTPF_OVERLAY_NO_ICON"></span><span id="optpf_overlay_no_icon"></span>OPTPF\_OVERLAY\_NO\_ICON
</dt> <dd>

If set, CPSUI overlays its IDI\_CPSUI\_NO icon onto the icon identified by the **IconID** member.

</dd> </dl>

<dl> <dt>

<span id="OPTPF_OVERLAY_STOP_ICON"></span><span id="optpf_overlay_stop_icon"></span>OPTPF\_OVERLAY\_STOP\_ICON
</dt> <dd>

If set, CPSUI overlays the IDI\_CPSUI\_STOP icon onto the icon identified by the **IconID** member.

</dd> </dl>

<dl> <dt>

<span id="OPTPF_OVERLAY_WARNING_ICON"></span><span id="optpf_overlay_warning_icon"></span>OPTPF\_OVERLAY\_WARNING\_ICON
</dt> <dd>

If set, CPSUI overlays its IDI\_CPSUI\_WARNING icon onto the icon identified by the **IconID** member.

</dd> </dl>

<dl> <dt>

<span id="OPTPF_USE_HDLGTEMPLATE"></span><span id="optpf_use_hdlgtemplate"></span>OPTPF\_USE\_HDLGTEMPLATE
</dt> <dd>

If set, **lParam** contains a template handle.

If not set, **lParam** contains a template resource identifier.

(Used only if **Style** is PUSHBUTTON\_TYPE\_DLGPROC.)

</dd> </dl> </dd> <dt>

**Style**
</dt> <dd>

Push button style, used only for the [**TVOT\_PUSHBUTTON**](https://www.bing.com/search?q=**TVOT\_PUSHBUTTON**) option type.

</dd> <dt>

**pData**
</dt> <dd>

Pointer to the parameter's value. Use of this member is dependent on the [CPSUI option type](https://www.bing.com/search?q=CPSUI option type).

</dd> <dt>

**IconID**
</dt> <dd>

Usually identifies the icon to be associated with the option parameter, but is sometimes used for other purposes. Use of this member is dependent on the [CPSUI option type](https://www.bing.com/search?q=CPSUI option type).

</dd> <dt>

**lParam**
</dt> <dd>

Use of this member is dependent on the [CPSUI option type](https://www.bing.com/search?q=CPSUI option type).

</dd> <dt>

**dwReserved**
</dt> <dd>

Reserved, must be initialized to zero.

</dd> </dl>

## Remarks

If the OPTPF\_HIDE flag is set in all the OPTPARAM structures associated with an option, CPSUI hides the entire option.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Compstui.h (include Compstui.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20OPTPARAM%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




