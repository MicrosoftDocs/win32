---
Description: The IPrintOemPS2::GetPDEVAdjustment method enables a plug-in to override specific PDEV settings.
ms.assetid: 8dc4252f-72d5-47ae-9f43-8006aa71c29d
title: IPrintOemPS2::GetPDEVAdjustment method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrintOemPS2::GetPDEVAdjustment method

The `IPrintOemPS2::GetPDEVAdjustment` method enables a plug-in to override specific [*PDEV*](https://msdn.microsoft.com/139a10e9-203b-499b-9291-8537eae9189c) settings.

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

Specifies the type of adjustment asked for. The following flags are currently supported:



| Flag                                         | Meaning                                                                                                                                                     |
|----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PDEV\_ADJUST\_PAPER\_MARGIN\_TYPE<br/> | Adjust the paper margin setting that is reported in the PDEV. See the [**PDEV\_ADJUST\_PAPER\_MARGIN**](pdev-adjust-paper-margin.md) structure.<br/> |
| PDEV\_HOSTFONT\_ENABLED\_TYPE<br/>     | Enable or disable the Hostfont support feature. See the [**PDEV\_HOSTFONT\_ENABLED**](pdev-hostfont-enabled.md) structure.<br/>                      |
| PDEV\_USE\_TRUE\_COLOR\_TYPE<br/>      | Enable or disable color output for monochrome and color printers. See the [**PDEV\_USE\_TRUE\_COLOR**](pdev-use-true-color.md) structure.<br/>       |



 

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

The `IPrintOemPS2::GetPDEVAdjustment` method should return S\_OK if it recognizes the adjustment type, and S\_FALSE if it does not. If the method fails, it should return E\_FAIL. The chain of plug-ins is called until either S\_OK or a failure code other than E\_NOTIMPL is returned. That is, the chain of plug-ins is called until the first plug-in that is capable of handling the adjustment is found.

## Remarks

This function is available in Windows XP and later.

Currently, the Pscript5 driver calls `IPrintOemPS2::GetPDEVAdjustment` to adjust the paper margin setting, as reported in the PDEV, to enable or disable the Hostfont feature, or to turn PostScript color output on or off.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



## See also

<dl> <dt>

[**IPrintOemPS2**](iprintoemps2-interface.md)
</dt> <dt>

[**PDEV\_ADJUST\_PAPER\_MARGIN**](pdev-adjust-paper-margin.md)
</dt> <dt>

[**PDEV\_HOSTFONT\_ENABLED**](pdev-hostfont-enabled.md)
</dt> <dt>

[**PDEV\_USE\_TRUE\_COLOR**](pdev-use-true-color.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemPS2::GetPDEVAdjustment%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





