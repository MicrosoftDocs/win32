---
Description: The OEMQueryDeviceSupport function returns requested device-specific information.
ms.assetid: 38e1bb07-be98-494b-a9c9-a83edef367e0
title: OEMQueryDeviceSupport function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# OEMQueryDeviceSupport function

The `OEMQueryDeviceSupport` function returns requested device-specific information.

## Syntax


```C++
BOOL APIENTRY OEMQueryDeviceSupport(
        SURFOBJ                     *pso,
        XLATEOBJ                    *pxlo,
        XFORMOBJ                    *pxo,
        ULONG                       iType,
        ULONG                       cjIn,
  _In_  _reads_bytes_(cjIn) PVOID   pvIn,
        ULONG                       cjOut,
  _Out_ _writes_bytes_(cjOut) PVOID pvOut
);
```



## Parameters

<dl> <dt>

*pso* 
</dt> <dd></dd> <dt>

*pxlo* 
</dt> <dd></dd> <dt>

*pxo* 
</dt> <dd></dd> <dt>

*iType* 
</dt> <dd></dd> <dt>

*cjIn* 
</dt> <dd></dd> <dt>

*pvIn* \[in\]
</dt> <dd></dd> <dt>

*cjOut* 
</dt> <dd></dd> <dt>

*pvOut* \[out\]
</dt> <dd></dd> </dl>

## 

### Comments

See [**DrvQueryDeviceSupport**](display.drvquerydevicesupport).

This function is not supported on Windows NT 4.0 and earlier.

Do not directly hook out this function. Instead, implement [**OEMEnableDriver**](oemenabledriver.md) so that it fills in a [**DRVENABLEDATA**](display.drvenabledata) structure listing all of the DDIs to be hooked out.

If you call into the core driver, cast the call using the **PFN\_DrvQueryDeviceSupport** function pointer.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Printoem.h (include Printoem.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20OEMQueryDeviceSupport%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




