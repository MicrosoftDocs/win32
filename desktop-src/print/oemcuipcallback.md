---
Description: The OEMCUIPCALLBACK function type is used for defining callback functions that are specified by a user interface plug-in's IPrintOemUI::CommonUIProp method. The structure is defined in printoem.h.
ms.assetid: d740bed2-ba3c-4834-8bda-3512ac8da1d5
title: OEMCUIPCALLBACK callback function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# OEMCUIPCALLBACK callback function

The OEMCUIPCALLBACK function type is used for defining callback functions that are specified by a user interface plug-in's [**IPrintOemUI::CommonUIProp**](iprintoemui-commonuiprop.md) method. The structure is defined in printoem.h.

## Syntax


```C++
LONG APIENTRY OEMCUIPCALLBACK(
   PCPSUICBPARAM pCPSUICBParam,
   POEMCUIPPARAM pOEMCUIPParam
);
```



## Parameters

<dl> <dt>

*pCPSUICBParam* 
</dt> <dd>

Pointer to a [**CPSUICBPARAM**](cpsuicbparam.md) structure.

</dd> <dt>

*pOEMCUIPParam* 
</dt> <dd>

Pointer to an [**OEMCUIPPARAM**](oemcuipparam.md) structure.

</dd> </dl>

## Return value

See the following Remarks section.

## Remarks

A callback function specified by an **IPrintOemUI::CommonUIProp** method is called when a user modifies a printer property sheet. The callback function's purpose is to process user modifications to customized option items.

When a property sheet item is modified, [CPSUI](https://www.bing.com/search?q=CPSUI) calls the printer driver's printer interface DLL. This DLL contains its own callback function, of type [**\_CPSUICALLBACK**](-cpsuicallback.md), which processes option values contained in its own OPTITEM structures. Then the printer interface DLL's callback function calls the user interface plug-in's callback function. If multiple user interface plug-ins are provided, each plug-in's callback function is called, in turn, in the order in which the plug-ins were installed.

The callback function receives a pointer to a [**CPSUICBPARAM**](cpsuicbparam.md) structure. The structure's **Reason** member identifies the event that caused the callback function to be called. The function also receives a pointer to the same [**OEMCUIPPARAM**](oemcuipparam.md) structure that was used when the **IPrintOemUI::CommonUIProp** method specified the callback function's address.

The CPSUICBPARAM structure's **pOptItem** and **pCurItem** members identify the modified option. The callback function can use these pointers, along with the **pOEMOptItems** and **cOEMOptItem** members of the OEMCUIPPARAM structure, to determine if the modified option is one that is owned by the user interface plug-in.

When a callback function is called, it must determine if any of its customized OPTITEM structures are affected by the specified **Reason** value. If they are, the function should process the affected options and return one of the CPSUI\_ACTION-prefixed return values described for the [**\_CPSUICALLBACK**](-cpsuicallback.md) function type. Otherwise it should return CPSUICB\_ACTION\_NONE.

The following additional rules apply to callback function return values:

-   If **Reason** contains CPSUICB\_REASON\_APPLYNOW, then the callback must return either CPSUICB\_ACTION\_ITEMS\_APPLIED or CPSUICB\_ACTION\_NO\_APPLY\_EXIT. In the latter case, the printer driver interface immediately returns to CPSUI without calling any other user interface plug-in's callback function.

-   If **Reason** contains any value except CPSUICB\_REASON\_APPLYNOW, then the return value must be one of the following:<dl> CPSUICB\_ACTION\_REINIT\_ITEMS  
    CPSUICB\_ACTION\_OPTIF\_CHANGED  
    CPSUICB\_ACTION\_NONE  
    </dl>

    These return values are listed in order of decreasing priority. If multiple user interface plug-ins exist, the printer interface DLL calls each one's callback function and saves the highest-priority return value, passing it back to CPSUI.

## Requirements



|                            |                                                                                                                          |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                                       |
| Header<br/>          | <dl> <dt>Printoem.h (include Printoem.h or Compstui.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20OEMCUIPCALLBACK%20callback%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




