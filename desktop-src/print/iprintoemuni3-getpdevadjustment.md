---
Description: The IPrintOemUni3::GetPDEVAdjustment method enables a plug-in to override specific PDEV settings.
ms.assetid: bb7d7248-9520-4bc8-8483-b05b78608fc7
title: IPrintOemUni3::GetPDEVAdjustment method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrintOemUni3::GetPDEVAdjustment method

The `IPrintOemUni3::GetPDEVAdjustment` method enables a plug-in to override specific [*PDEV*](https://www.bing.com/search?q=*PDEV*) settings.

## Syntax


```C++
HRESULT GetPDEVAdjustment(
        PDEVOBJ pdevobj,
        DWORD   dwAdjustType,
        PVOID   pBuf,
        DWORD   cbBuffer,
  [out] BOOL    *pbAdjustmentDone
);
```



## Parameters

<dl> <dt>

*pdevobj* 
</dt> <dd>

Pointer to a [**DEVOBJ**](devobj.md) structure.

</dd> <dt>

*dwAdjustType* 
</dt> <dd>

Specifies the type of adjustment asked for. The following flags are currently supported.



| Flag                                                 | Meaning                                                                                                                                                                                                         |
|------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PDEV\_ADJUST\_GRAPHICS\_RESOLUTION\_TYPE<br/>  | Adjust the graphics resolution setting that is reported in the PDEV structure. For more information, see the [**PDEV\_ADJUST\_GRAPHICS RESOLUTION**](pdev-adjust-graphics-resolution.md) structure.<br/> |
| PDEV\_IMAGEABLE\_ORIGIN\_AREA\_TYPE<br/>       | Adjust the imageable origin area that is reported in the PDEV structure. For more information, see the [**PDEV\_ADJUST\_IMAGEABLE\_ORIGIN\_AREA**](pdev-adjust-imageable-origin-area.md) structure.<br/> |
| PDEV\_ADJUST\_PHYSICAL\_PAPER\_SIZE\_TYPE<br/> | Adjust the physical paper size that is reported in the PDEV structure. For more information, see the [**PDEV\_ADJUST\_PAPER\_PHYSICAL\_SIZE**](pdev-adjust-paper-physical-size.md) structure.<br/>       |



 

</dd> <dt>

*pBuf* 
</dt> <dd>

Pointer to a structure that contains the planned settings that are used if there is no change. These structures are listed in the preceding table. The plug-in can overwrite the settings in the relevant structure.

</dd> <dt>

*cbBuffer* 
</dt> <dd>

Specifies the size, in bytes, of the structure pointed to by *pBuf*.

</dd> <dt>

*pbAdjustmentDone* \[out\]
</dt> <dd>

Pointer to a memory location that the plug-in sets to **TRUE** when it actually changes a value in the buffer. This may be used by the driver for optimizations.

</dd> </dl>

## Return value

The `IPrintOemUni3::GetPDEVAdjustment` method should return S\_OK if it recognizes the adjustment type, and S\_FALSE if it does not. If the method fails, it should return E\_FAIL. The chain of plug-ins is called until either S\_OK or a failure code other than E\_NOTIMPL is returned. That is, the chain of plug-ins is called until the first plug-in that is capable of handling the adjustment is found.

## Remarks

This function is available in Windows Vista and later.

Currently, the Unidrv driver calls `IPrintOemUni3::GetPDEVAdjustment` to adjust the graphics resolution setting, as reported in the PDEV, to adjust the imageable origin area, or to adjust the physical paper size.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



## See also

<dl> <dt>

[**IPrintOemUni3**](iprintoemuni3-interface.md)
</dt> <dt>

[**PDEV\_ADJUST\_GRAPHICS RESOLUTION**](pdev-adjust-graphics-resolution.md)
</dt> <dt>

[**PDEV\_ADJUST\_IMAGEABLE\_ORIGIN\_AREA**](pdev-adjust-imageable-origin-area.md)
</dt> <dt>

[**PDEV\_ADJUST\_PAPER\_MARGIN**](pdev-adjust-paper-margin.md)
</dt> <dt>

[**PDEV\_ADJUST\_PAPER\_PHYSICAL\_SIZE**](pdev-adjust-paper-physical-size.md)
</dt> <dt>

[**PDEV\_HOSTFONT\_ENABLED**](pdev-hostfont-enabled.md)
</dt> <dt>

[**PDEV\_USE\_TRUE\_COLOR**](pdev-use-true-color.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemUni3::GetPDEVAdjustment%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





