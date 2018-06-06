---
Description: The IPrintOemUni::TTYGetInfo method enables a rendering plug-in to supply Unidrv with information relevant to text-only printers.
ms.assetid: 0df8c555-4298-47e7-a6a7-43f101620e04
title: IPrintOemUni::TTYGetInfo method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrintOemUni::TTYGetInfo method

The `IPrintOemUni::TTYGetInfo` method enables a rendering plug-in to supply Unidrv with information relevant to text-only printers.

## Syntax


```C++
HRESULT TTYGetInfo(
   PDEVOBJ pdevobj,
   DWORD   dwInfoIndex,
   PVOID   pOutputBuf,
   DWORD   dwSize,
   DWORD   *pcbcNeeded
);
```



## Parameters

<dl> <dt>

*pdevobj* 
</dt> <dd>

Caller-supplied pointer to a [**DEVOBJ**](devobj.md) structure.

</dd> <dt>

*dwInfoIndex* 
</dt> <dd>

Caller-supplied constant identifying the type of information being requested. The following constant values are defined:

<dl> <dt>

<span id="OEMTTY_INFO_CODEPAGE"></span><span id="oemtty_info_codepage"></span>OEMTTY\_INFO\_CODEPAGE
</dt> <dd>

The *pOutputBuf* parameter points to a DWORD in which the method should return the number of the code page to be used.

</dd> </dl>

<dl> <dt>

<span id="OEMTTY_INFO_MARGINS"></span><span id="oemtty_info_margins"></span>OEMTTY\_INFO\_MARGINS
</dt> <dd>

The *pOutputBuf* parameter points to a RECT structure in which the method should return page margin widths, in tenths of millimeters (for example, 20 represents 2 mm). If the entire page is printable, all margin values must be 0.

</dd> </dl>

<dl> <dt>

<span id="OEMTTY_INFO_NUM_UFMS_"></span><span id="oemtty_info_num_ufms_"></span>OEMTTY\_INFO\_NUM\_UFMS 
</dt> <dd>

The *pOutputBuf* parameter points to a DWORD in which the method should return the number of resource IDs of the [*UFMs*](wdkgloss.u#wdkgloss-unidrv-font-metrics--ufm-) for 10, 12, and 17 CPI fonts. To actually obtain these resource IDs, perform a query using OEMTTY\_INFO\_UFM\_IDS.

</dd> </dl>

<dl> <dt>

<span id="OEMTTY_INFO_UFM_IDS_"></span><span id="oemtty_info_ufm_ids_"></span>OEMTTY\_INFO\_UFM\_IDS 
</dt> <dd>

The *pOutputBuf* parameter points to an array of DWORDs of sufficient size to hold the number of resource IDs of the UFMs for 10, 12, and 17 CPI fonts. (This number is obtained by using OEMTTY\_INFO\_NUM\_UFMS in a query.) The method should return the resource IDs of the [*UFMs*](wdkgloss.u#wdkgloss-unidrv-font-metrics--ufm-) for 10,12, and 17 CPI fonts.

</dd> </dl> </dd> <dt>

*pOutputBuf* 
</dt> <dd>

Caller-supplied pointer to a buffer to receive the requested information.

</dd> <dt>

*dwSize* 
</dt> <dd>

Caller-supplied size, in bytes, of the buffer pointed to by *pOutputBuf*.

</dd> <dt>

*pcbcNeeded* 
</dt> <dd>

Caller-supplied pointer to a location to receive the number of bytes written into the buffer pointed to by *pOutputBuf*. If the number of bytes required is smaller than the number specified by *dwSize*, the method should supply the required size and return E\_FAIL.

</dd> </dl>

## Return value

The method must return one of the following values.



| Return code                                                                               | Description                               |
|-------------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | The operation succeeded.<br/>       |
| <dl> <dt>**E\_FAIL**</dt> </dl>    | The operation failed.<br/>          |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl> | The method is not implemented.<br/> |



 

## Remarks

The `IPrintOemUni::TTYGetInfo` method is optional. If a rendering plug-in implements this method, the plug-in's [**IPrintOemUni::GetImplementedMethod**](iprintoemuni-getimplementedmethod.md) method must return S\_OK when it receives "TTYGetInfo" as input.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemUni::TTYGetInfo%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




