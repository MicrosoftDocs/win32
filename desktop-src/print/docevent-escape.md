---
Description: The DOCEVENT\_ESCAPE structure is a container for values used as parameters for the ExtEscape function.
ms.assetid: 54ac7c45-63a1-4003-8250-524e6f9e8d06
title: DOCEVENT\_ESCAPE structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# DOCEVENT\_ESCAPE structure

The DOCEVENT\_ESCAPE structure is a container for values used as parameters for the **ExtEscape** function.

## Syntax


```C++
typedef struct _DOCEVENT_ESCAPE {
  int   iEscape;
  int   cjInput;
  PVOID pvInData;
} DOCEVENT_ESCAPE, *PDOCEVENT_ESCAPE;
```



## Members

<dl> <dt>

**iEscape**
</dt> <dd>

Specifies the value of the **ExtEscape** function's *nEscape* parameter.

</dd> <dt>

**cjInput**
</dt> <dd>

Specifies the value of the **ExtEscape** function's *cbInput* parameter.

</dd> <dt>

**pvInData**
</dt> <dd>

Specifies the value of the **ExtEscape** function's *lpszInData* parameter.

</dd> </dl>

## Remarks

The DOCEVENT\_ESCAPE structure is defined for Windows XP and later.

This structure is used in conjunction with a call to [**DrvDocumentEvent**](drvdocumentevent.md) or [**IPrintOemUI2::DocumentEvent**](iprintoemui2-documentevent.md), in which the *iEsc* parameter is set to DOCUMENTEVENT\_ESCAPE. Before calling either of these functions, the caller must fill in the members of this structure.

Refer to the Microsoft Windows SDK documentation for a description of the **ExtEscape** function and the three parameters that correspond to the members of this structure.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Winddiui.h (include Winddiui.h)</dt> </dl> |



## See also

<dl> <dt>

[**DrvDocumentEvent**](drvdocumentevent.md)
</dt> <dt>

[**IPrintOemUI2::DocumentEvent**](iprintoemui2-documentevent.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20DOCEVENT_ESCAPE%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





