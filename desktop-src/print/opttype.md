---
Description: 'The OPTTYPE structure is used by CPSUI applications (including printer interface DLLs) for describing the type and other characteristics of a property sheet option, if the option is specified by an OPTITEM structure.'
ms.assetid: '041dd438-e837-4912-bda7-de654204198b'
title: OPTTYPE structure
---

# OPTTYPE structure

The OPTTYPE structure is used by CPSUI applications (including printer interface DLLs) for describing the type and other characteristics of a [property sheet option](print.property_sheet_options), if the option is specified by an [**OPTITEM**](optitem.md) structure.

## Syntax


```C++
typedef struct _OPTTYPE {
  WORD      cbSize;
  BYTE      Type;
  BYTE      Flags;
  WORD      Count;
  WORD      BegCtrlID;
  POPTPARAM pOptParam;
  WORD      Style;
  WORD      wReserved[3];
  ULONG_PTR dwReserved[3];
} OPTTYPE, *POPTTYPE;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

Size, in bytes, of the OPTTYPE structure.

</dd> <dt>

**Type**
</dt> <dd>

Specifies the [CPSUI option type](print.cpsui_option_types).

</dd> <dt>

**Flags**
</dt> <dd>

Optional bit flags that modify the option's characteristics. The following flags can be set in any combination.

<dl> <dt>

<span id="OPTTF_NOSPACE_BEFORE_POSTFIX"></span><span id="opttf_nospace_before_postfix"></span>OPTTF\_NOSPACE\_BEFORE\_POSTFIX
</dt> <dd>

CPSUI should not add a space character between the string specified by the [**OPTITEM**](optitem.md) structure's **pName** string and the [**OPTPARAM**](optparam.md) structure's **pData** string, when displaying the option.

Valid only if the option type is or [**TVOT\_SCROLLBAR**](print.tvot_scrollbar) or [**TVOT\_TRACKBAR**](print.tvot_trackbar).

</dd> </dl>

<dl> <dt>

<span id="OPTTF_TYPE_DISABLED"></span><span id="opttf_type_disabled"></span>OPTTF\_TYPE\_DISABLED
</dt> <dd>

All the OPTPARAM structures to which **pOptParam** points are disabled, so that none of the parameter values are user-selectable.

</dd> </dl> </dd> <dt>

**Count**
</dt> <dd>

Specifies the number of [**OPTPARAM**](optparam.md) structures to which **pOptParam** points. This member's value is dependent on the [CPSUI option type](print.cpsui_option_types).

</dd> <dt>

**BegCtrlID**
</dt> <dd>

If **pDlgPage** in [**COMPROPSHEETUI**](compropsheetui.md) identifies a CPSUI-supplied page, or if **DlgTemplateID** in [**DLGPAGE**](dlgpage.md) identifies a CPSUI-supplied template, **BegCtrlID** is not used.

Otherwise, **BegCtrlID** must contain the first of a sequentially numbered set of Windows control identifiers. Control identifier usage is dependent on the [CPSUI option type](print.cpsui_option_types).

</dd> <dt>

**pOptParam**
</dt> <dd>

Pointer to an array of [**OPTPARAM**](optparam.md) structures describing the parameter values that a user can select for the option.

</dd> <dt>

**Style**
</dt> <dd>

Specifies flags that can be used to modify the option's display characteristics. The flags that can be specified are dependent on the [CPSUI option type](print.cpsui_option_types).

</dd> <dt>

**wReserved**
</dt> <dd>

Reserved, must be initialized to zero.

</dd> <dt>

**dwReserved**
</dt> <dd>

Reserved, must be initialized to zero.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Compstui.h (include Compstui.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20OPTTYPE%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




