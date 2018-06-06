---
Description: The PROPSHEETUI\_INFO structure is used as an input parameter to PFNPROPSHEETUI-typed functions.
ms.assetid: b21c3ee1-13e8-4796-af45-6ba60e84df4e
title: PROPSHEETUI\_INFO structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# PROPSHEETUI\_INFO structure

The PROPSHEETUI\_INFO structure is used as an input parameter to [**PFNPROPSHEETUI**](pfnpropsheetui.md)-typed functions.

## Syntax


```C++
typedef struct _PROPSHEETUI_INFO {
  WORD            cbSize;
  WORD            Version;
  WORD            Flags;
  WORD            Reason;
  HANDLE          hComPropSheet;
  PFNCOMPROPSHEET pfnComPropSheet;
  LPARAM          lParamInit;
  ULONG_PTR       UserData;
  ULONG_PTR       Result;
} PROPSHEETUI_INFO, *PPROPSHEETUI_INFO;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

CPSUI-supplied size, in bytes, of the PROPSHEETUI\_INFO structure.

</dd> <dt>

**Version**
</dt> <dd>

CPSUI-supplied version number of the PROPSHEETUI\_INFO structure. The current version number is defined by PROPSHEETUI\_INFO\_VERSION in compstui.h.

</dd> <dt>

**Flags**
</dt> <dd>

CPSUI-supplied bit flags. The following flag is defined:



| Flag                         | Description                                                         |
|------------------------------|---------------------------------------------------------------------|
| PSUIINFO\_UNICODE<br/> | If set, the calling application uses Unicode characters.<br/> |



 

</dd> <dt>

**Reason**
</dt> <dd>

CPSUI-supplied constant specifying the action to be performed on the property sheet by the [**PFNPROPSHEETUI**](pfnpropsheetui.md)-typed function to which the PROPSHEETUI\_INFO structure was passed. One of the following constants will be supplied:

-   PROPSHEETUI\_REASON\_DESTROY

-   PROPSHEETUI\_REASON\_GET\_ICON

-   PROPSHEETUI\_REASON\_GET\_INFO\_HEADER

-   PROPSHEETUI\_REASON\_INIT

-   PROPSHEETUI\_REASON\_SET\_RESULT

<dl> <dd>

For information about the meaning of each constant, see the Remarks section of the [**PFNPROPSHEETUI**](pfnpropsheetui.md) description.

</dd> </dl> </dd> <dt>

**hComPropSheet**
</dt> <dd>

CPSUI-supplied handle to a property sheet [group parent](https://www.bing.com/search?q=group+parent). This handle can be passed to CPSUI's [**ComPropSheet**](compropsheet.md) function.

</dd> <dt>

**pfnComPropSheet**
</dt> <dd>

Address of CPSUI's [**ComPropSheet**](compropsheet.md) function.

</dd> <dt>

**lParamInit**
</dt> <dd>

Value received as the *lParam* parameter for the associated PFNPROPSHEETUI-typed function, when the function was first called with a **Reason** of PROPSHEETUI\_REASON\_INIT. For information about what this value can be, see the description of [**PFNPROPSHEETUI**](pfnpropsheetui.md).

This value is supplied by CPSUI, and is valid for all **Reason** values.

</dd> <dt>

**UserData**
</dt> <dd>

Optional, private value or pointer supplied by the associated [**PFNPROPSHEETUI**](pfnpropsheetui.md)-typed function, initially set to zero by CPSUI. If the function stores a value in **UserData**, then for subsequent calls to the function, the stored value or pointer is unchanged unless changed by the function.

</dd> <dt>

**Result**
</dt> <dd>

Result value supplied by the associated [**PFNPROPSHEETUI**](pfnpropsheetui.md)-typed function, initially set to zero by CPSUI. If the function stores a result value in **Result**, then for subsequent calls to the function, the stored value is unchanged unless changed by the function.

If the PFNPROPSHEETUI-typed function's address was specified as an argument to [**CommonPropertySheetUI**](commonpropertysheetui.md), the last value stored in **Result** is returned to **CommonPropertySheetUI** in the location pointed to by its *pResult* argument.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Compstui.h (include Compstui.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20PROPSHEETUI_INFO%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




