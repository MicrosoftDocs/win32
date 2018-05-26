---
Description: The SETRESULT\_INFO structure is used as an input parameter to an applications PFNPROPSHEETUI-typed callback function.
ms.assetid: 54701f88-1145-4a50-bf5a-36be1d88355d
title: SETRESULT\_INFO structure
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SETRESULT\_INFO structure

The SETRESULT\_INFO structure is used as an input parameter to an application's [**PFNPROPSHEETUI**](pfnpropsheetui.md)-typed callback function.

## Syntax


```C++
typedef struct _SETRESULT_INFO {
  WORD    cbSize;
  WORD    wReserved;
  HANDLE  hSetResult;
  LRESULT Result;
} SETRESULT_INFO, *PSETRESULT_INFO;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

CPSUI-supplied size, in bytes, of the SETRESULT\_INFO structure.

</dd> <dt>

**wReserved**
</dt> <dd>

Reserved.

</dd> <dt>

**hSetResult**
</dt> <dd>

CPSUI-supplied handle to an added property sheet page, obtained from the application. For more information, see the following Remarks section.

</dd> <dt>

**Result**
</dt> <dd>

CPSUI-supplied handle to an added property sheet page, obtained from the application. For more information, see the following Remarks section.

</dd> </dl>

## Remarks

When an application calls CPSUI's [**ComPropSheet**](compropsheet.md) function, specifying a function code of [**CPSFUNC\_SET\_RESULT**](print.cpsfunc_set_result), CPSUI calls all registered [**PFNPROPSHEETUI**](pfnpropsheetui.md)-typed functions, specifying a reason of PROPSHEETUI\_REASON\_SET\_RESULT. When specifying this reason, CPSUI also supplies a SETRESULT\_INFO structure.

The values contained in the structure's **hSetResult** and **Result** members are the *lParam1* and *lParam2* values, respectively, that were supplied to CPSUI's **ComPropSheet** function.

Each of the application's PFNPROPSHEETUI-typed functions is called in order, from the one most recently declared to the first one declared, until one of these functions provides a return value of less than one. At that point, CPSUI returns from its **ComPropSheet** function, providing a count of the number of PFNPROPSHEETUI-typed functions that were called.

Typically, an application's PFNPROPSHEETUI-typed function sets the **Result** member of its PROPSHEETUI\_INFO structure to the value received in the SETRESULT\_INFO structure's **Result** member. Then the function returns a value of 1 (or greater), so the next PFNPROPSHEETUI-typed function can also receive it. Each subsequently called function is associated with a page that is the parent of the page associated with the last-called function. A function can modify the contents of SETRESULT\_INFO structure's **Result** member, causing the functions associated with parent pages to receive the new value.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Compstui.h (include Compstui.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20SETRESULT_INFO%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




