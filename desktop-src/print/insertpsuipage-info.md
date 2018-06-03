---
Description: The INSERTPSUIPAGE\_INFO structure is used as an input parameter to CPSUI's ComPropSheet function, if the function code is CPSFUNC\_INSERT\_PSUIPAGE. All member values must be supplied by the ComPropSheet caller.
ms.assetid: 99ec8cfa-3ec7-4080-b22a-dba0a86b7e4a
title: INSERTPSUIPAGE\_INFO structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# INSERTPSUIPAGE\_INFO structure

The INSERTPSUIPAGE\_INFO structure is used as an input parameter to CPSUI's [**ComPropSheet**](compropsheet.md) function, if the function code is [**CPSFUNC\_INSERT\_PSUIPAGE**](https://www.bing.com/search?q=**CPSFUNC\_INSERT\_PSUIPAGE**). All member values must be supplied by the **ComPropSheet** caller.

## Syntax


```C++
typedef struct _INSERTPSUIPAGE_INFO {
  WORD      cbSize;
  BYTE      Type;
  BYTE      Mode;
  ULONG_PTR dwData1;
  ULONG_PTR dwData2;
  ULONG_PTR dwData3;
} INSERTPSUIPAGE_INFO, *PINSERTPSUIPAGE_INFO;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

Caller-supplied size, in bytes, of the INSERTPSUIPAGE\_INFO structure.

</dd> <dt>

**Type**
</dt> <dd>

Caller-supplied integer value indicating the type of insertion being requested. The member can contain one of the following constants:

<dl> <dt>

<span id="PSUIPAGEINSERT_DLL"></span><span id="psuipageinsert_dll"></span>PSUIPAGEINSERT\_DLL
</dt> <dd>

CPSUI calls the specified [**PFNPROPSHEETUI**](pfnpropsheetui.md) typed function, with a reason value of PROPSHEETUI\_REASON\_INIT. The function is contained in a separate DLL.

</dd> </dl>

<dl> <dt>

<span id="PSUIPAGEINSERT_GROUP_PARENT"></span><span id="psuipageinsert_group_parent"></span>PSUIPAGEINSERT\_GROUP\_PARENT
</dt> <dd>

CPSUI creates a new [group parent](https://www.bing.com/search?q=group parent).

</dd> </dl>

<dl> <dt>

<span id="PSUIPAGEINSERT_HPROPSHEETPAGE"></span><span id="psuipageinsert_hpropsheetpage"></span>PSUIPAGEINSERT\_HPROPSHEETPAGE
</dt> <dd>

CPSUI inserts a page that has been created by calling **CreatePropertySheetPage** (see the Microsoft Windows SDK documentation).

(This is equivalent to calling [**ComPropSheet**](compropsheet.md) with a function code of [**CPSFUNC\_ADD\_HPROPSHEETPAGE**](https://www.bing.com/search?q=**CPSFUNC\_ADD\_HPROPSHEETPAGE**).)

</dd> </dl>

<dl> <dt>

<span id="PSUIPAGEINSERT_PCOMPROPSHEETUI"></span><span id="psuipageinsert_pcompropsheetui"></span>PSUIPAGEINSERT\_PCOMPROPSHEETUI
</dt> <dd>

CPSUI inserts pages described by a [**COMPROPSHEETUI**](compropsheetui.md) structure.

(This is equivalent to calling [**ComPropSheet**](compropsheet.md) with a function code of [**CPSFUNC\_ADD\_PCOMPROPSHEETUI**](https://www.bing.com/search?q=**CPSFUNC\_ADD\_PCOMPROPSHEETUI**).)

</dd> </dl>

<dl> <dt>

<span id="PSUIPAGEINSERT_PFNPROPSHEETUI"></span><span id="psuipageinsert_pfnpropsheetui"></span>PSUIPAGEINSERT\_PFNPROPSHEETUI
</dt> <dd>

CPSUI calls the specified [**PFNPROPSHEETUI**](pfnpropsheetui.md) typed function, with a reason value of PROPSHEETUI\_REASON\_INIT.

(This is equivalent to calling [**ComPropSheet**](compropsheet.md) with a function code of [**CPSFUNC\_ADD\_PFNPROPSHEETUI**](https://www.bing.com/search?q=**CPSFUNC\_ADD\_PFNPROPSHEETUI**).)

</dd> </dl>

<dl> <dt>

<span id="PSUIPAGEINSERT_PROPSHEETPAGE"></span><span id="psuipageinsert_propsheetpage"></span>PSUIPAGEINSERT\_PROPSHEETPAGE
</dt> <dd>

CPSUI inserts the page described by the specified PROPSHEETPAGE structure.

(This is equivalent to calling [**ComPropSheet**](compropsheet.md) with a function code of [**CPSFUNC\_ADD\_PROPSHEETPAGE**](https://www.bing.com/search?q=**CPSFUNC\_ADD\_PROPSHEETPAGE**).)

</dd> </dl> </dd> <dt>

**Mode**
</dt> <dd>

Caller-supplied value indicating where CPSUI should insert the new pages. It must be one of the following values:

<dl> <dt>

<span id="INSPSUIPAGE_MODE_AFTER"></span><span id="inspsuipage_mode_after"></span>INSPSUIPAGE\_MODE\_AFTER
</dt> <dd>

CPSUI inserts pages after the page identified by the CPSUI page handle that is specified by the *lParam1* parameter to [**ComPropSheet**](compropsheet.md).

</dd> </dl>

<dl> <dt>

<span id="INSPSUIPAGE_MODE_BEFORE"></span><span id="inspsuipage_mode_before"></span>INSPSUIPAGE\_MODE\_BEFORE
</dt> <dd>

CPSUI inserts pages before the page identified by the CPSUI page handle that is specified by the *lParam1* parameter to [**ComPropSheet**](compropsheet.md).

</dd> </dl>

<dl> <dt>

<span id="INSPSUIPAGE_MODE_FIRST_CHILD"></span><span id="inspsuipage_mode_first_child"></span>INSPSUIPAGE\_MODE\_FIRST\_CHILD
</dt> <dd>

CPSUI inserts pages as the first children of the parent group identified by the *hComPropSheet* parameter to [**ComPropSheet**](compropsheet.md).

The *lParam1* parameter to [**ComPropSheet**](compropsheet.md) is ignored.

</dd> </dl>

<dl> <dt>

<span id="INSPUIPAGE_MODE_INDEX"></span><span id="inspuipage_mode_index"></span>INSPUIPAGE\_MODE\_INDEX
</dt> <dd>

CPSUI inserts pages as children of the parent group identified by the *hComPropSheet* parameter to [**ComPropSheet**](compropsheet.md).

The *lParam1* parameter to [**ComPropSheet**](compropsheet.md) specifies a zero-based index identifying where, within the set of children, the specified pages should be inserted. If *lParam1* is 0, the pages are inserted starting at page 1; if *lParam1* is 1, the pages are inserted starting at page 2; and so on. If the index is greater than the number of existing children, the new pages are added as the last children. The *lParam1* value must be specified as HINSPSUIPAGE\_INDEX(index).

</dd> </dl>

<dl> <dt>

<span id="INSPSUIPAGE_MODE_LAST_CHILD"></span><span id="inspsuipage_mode_last_child"></span>INSPSUIPAGE\_MODE\_LAST\_CHILD
</dt> <dd>

CPSUI inserts pages as the last children of the parent group identified by the *hComPropSheet* parameter to [**ComPropSheet**](compropsheet.md).

The *lParam1* parameter to [**ComPropSheet**](compropsheet.md) is ignored.

</dd> </dl> </dd> <dt>

**dwData1**
</dt> <dd></dd> <dt>

**dwData2**
</dt> <dd></dd> <dt>

**dwData3**
</dt> <dd>

Caller-supplied values that depend on the contents of the **Type** member, as follows:

<dl> <dt>

<span id="PSUIPAGEINSERT_DLL"></span><span id="psuipageinsert_dll"></span>PSUIPAGEINSERT\_DLL
</dt> <dd>

dwData1 - Caller-supplied pointer to a NULL-terminated string representing the DLL path name.

dwData2 - Caller-supplied pointer to a NULL-terminated string representing the name of a [**PFNPROPSHEETUI**](pfnpropsheetui.md) typed function, contained in the specified DLL.

dwData3 - Caller-supplied 32-bit value, passed to the PFNPROPSHEETUI-typed function for its *lParam* parameter.

</dd> </dl>

<dl> <dt>

<span id="PSUIPAGEINSERT_GROUP_PARENT"></span><span id="psuipageinsert_group_parent"></span>PSUIPAGEINSERT\_GROUP\_PARENT
</dt> <dd>

dwData1 - Not used, must be zero.

dwData2 - Not used, must be zero.

dwData3 - Not used, must be zero.

</dd> </dl>

<dl> <dt>

<span id="PSUIPAGEINSERT_HPROPSHEETPAGE"></span><span id="psuipageinsert_hpropsheetpage"></span>PSUIPAGEINSERT\_HPROPSHEETPAGE
</dt> <dd>

dwData1 - Caller-supplied handle to a property sheet, returned by **CreatePropertySheetPage**.

dwData2 - Not used, must be zero.

dwData3 - Not used, must be zero.

</dd> </dl>

<dl> <dt>

<span id="PSUIPAGEINSERT_PCOMPROPSHEETUI"></span><span id="psuipageinsert_pcompropsheetui"></span>PSUIPAGEINSERT\_PCOMPROPSHEETUI
</dt> <dd>

dwData1 - Caller-supplied pointer to a COMPROPSHEETUI structure.

dwData2 - On success, receives the number of pages inserted. On failure, receives an ERR\_CPSUI-prefixed error code.

dwData3 - Not used, must be zero.

</dd> </dl>

<dl> <dt>

<span id="PSUIPAGEINSERT_PFNPROPSHEETUI"></span><span id="psuipageinsert_pfnpropsheetui"></span>PSUIPAGEINSERT\_PFNPROPSHEETUI
</dt> <dd>

dwData1 - Caller-supplied pointer to a PFNPROPSHEETUI-typed function.

dwData2 - Caller-supplied 32-bit value, passed to the PFNPROPSHEETUI-typed function for its *lParam* parameter.

dwData3 - Not used, must be zero.

</dd> </dl>

<dl> <dt>

<span id="PSUIPAGEINSERT_PROPSHEETPAGE"></span><span id="psuipageinsert_propsheetpage"></span>PSUIPAGEINSERT\_PROPSHEETPAGE
</dt> <dd>

dwData1 - Caller-supplied pointer to a PROPSHEETPAGE structure.

dwData2 - Not used, must be zero.

dwData3 - Not used, must be zero.

</dd> </dl> </dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Compstui.h (include Compstui.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20INSERTPSUIPAGE_INFO%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




