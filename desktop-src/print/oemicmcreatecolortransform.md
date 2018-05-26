---
Description: The OEMIcmCreateColorTransform function creates an ICM color transform.
ms.assetid: 995fdac4-e958-4eed-ba3a-7be0349dec59
title: OEMIcmCreateColorTransform function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# OEMIcmCreateColorTransform function

The `OEMIcmCreateColorTransform` function creates an ICM color transform.

## Syntax


```C++
HANDLE APIENTRY OEMIcmCreateColorTransform(
           DHPDEV                                   dhpdev,
           LPLOGCOLORSPACEW                         pLogColorSpace,
  _In_opt_ _reads_bytes_(cjSourceProfile) PVOID     pvSourceProfile,
           ULONG                                    cjSourceProfile,
  _In_     _reads_bytes_(cjDestProfile) PVOID       pvDestProfile,
           ULONG                                    cjDestProfile,
  _In_opt_ _reads_bytes_opt_(cjTargetProfile) PVOID pvTargetProfile,
           ULONG                                    cjTargetProfile,
           POINTL                                   dwReserved
);
```



## Parameters

<dl> <dt>

*dhpdev* 
</dt> <dd></dd> <dt>

*pLogColorSpace* 
</dt> <dd></dd> <dt>

*pvSourceProfile* \[in, optional\]
</dt> <dd></dd> <dt>

*cjSourceProfile* 
</dt> <dd></dd> <dt>

*pvDestProfile* \[in\]
</dt> <dd></dd> <dt>

*cjDestProfile* 
</dt> <dd></dd> <dt>

*pvTargetProfile* \[in, optional\]
</dt> <dd></dd> <dt>

*cjTargetProfile* 
</dt> <dd></dd> <dt>

*dwReserved* 
</dt> <dd></dd> </dl>

## 

### Comments

See [**DrvIcmCreateColorTransform**](display.drvicmcreatecolortransform).

This function is not supported on Windows NT 4.0 and earlier.

Do not directly hook out this drawing function. Instead, implement [**OEMEnableDriver**](oemenabledriver.md) so that it fills in a [**DRVENABLEDATA**](display.drvenabledata) structure listing all of the drawing DDIs to be hooked out.

If you call into the core driver, cast the call using the **PFN\_DrvIcmCreateColorTransform** function pointer.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Printoem.h (include Printoem.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20OEMIcmCreateColorTransform%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




