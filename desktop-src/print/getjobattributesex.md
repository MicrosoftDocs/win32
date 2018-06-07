---
Description: Warning  Starting with Windows 10, the APIs which support third-party print providers are deprecated.
ms.assetid: 0715e4d4-665c-42cb-9c74-48c2c558c277
title: GetJobAttributesEx function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetJobAttributesEx function

> \[!Warning\]
>
> Starting with Windows 10, the APIs which support third-party print providers are deprecated. Microsoft does not recommend any investment into third-party print providers. Additionally, on Windows 8 and newer products where the v4 print driver model is available, third-party print providers may not create or manage queues which use v4 print drivers.

 

A print provider's **GetJobAttributesEx** function obtains information about a print job, including N-up and reverse printing options.

## Syntax


```C++
BOOL GetJobAttributesEx(
  _In_  LPWSTR     pPrinterName,
  _In_  LPDEVMODEW pDevmode,
  _In_  DWORD      dwLevel,
  _Out_ LPBYTE     pAttributeInfo,
  _In_  DWORD      nSize,
  _In_  DWORD      dwFlags
);
```



## Parameters

<dl> <dt>

*pPrinterName* \[in\]
</dt> <dd>

Caller-supplied pointer to a NULL-terminated Unicode string that contains the printer name.

</dd> <dt>

*pDevmode* \[in\]
</dt> <dd>

Caller-supplied pointer to a [**DEVMODEW**](https://msdn.microsoft.com/b2369876-9a79-40c8-8d27-c8b9d8e68e6b) structure that is passed to the print processor or printer driver.

</dd> <dt>

*dwLevel* \[in\]
</dt> <dd>

Caller-supplied value that indicates the type of structure pointed to by *pAttributeInfo*, as indicated in the following table. For more information, see Remarks.



| *dwLevel* Value | Structure pointed to by *pAttributeInfo*                  |
|-----------------|-----------------------------------------------------------|
| 1<br/>    | [**ATTRIBUTE\_INFO\_1**](attribute-info-1.md)<br/> |
| 2<br/>    | [**ATTRIBUTE\_INFO\_2**](attribute-info-2.md)<br/> |
| 3<br/>    | [**ATTRIBUTE\_INFO\_3**](attribute-info-3.md)<br/> |
| 4<br/>    | [**ATTRIBUTE\_INFO\_4**](attribute-info-4.md)<br/> |



 

</dd> <dt>

*pAttributeInfo* \[out\]
</dt> <dd>

Caller-supplied pointer to an attribute information structure ([**ATTRIBUTE\_INFO\_1**](attribute-info-1.md), [**ATTRIBUTE\_INFO\_2**](attribute-info-2.md), [**ATTRIBUTE\_INFO\_3**](attribute-info-3.md), or [**ATTRIBUTE\_INFO\_4**](attribute-info-4.md)) that receives information about the print job.

</dd> <dt>

*nSize* \[in\]
</dt> <dd>

Size of the buffer, in bytes, pointed to by *pAttributeInfo*.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

If set by the caller to FILL\_WITH\_DEFAULTS, then the spooler will fill *pAttributeInfo* with default values from level 1 up to the level specified by *dwLevel*.

For example, if *dwLevel* is 4 and FILL\_WITH\_DEFAULTS is specified, *pAttributeInfo* will be filled with the following default member values of [**ATTRIBUTE\_INFO\_4**](attribute-info-4.md):

**dwJobNumberOfPagesPerSide** = 1

**dwDrvNumberOfPagesPerSide** = 1

**dwNupBorderFlags** = 0

**dwJobPageOrderFlags** = 0

**dwDrvPageOrderFlags** = 0

**dwJobNumberOfCopies** = **dmCopies** member of [**DEVMODEW**](https://msdn.microsoft.com/b2369876-9a79-40c8-8d27-c8b9d8e68e6b)

**dwDrvNumberOfCopies** = **dmCopies** member of DEVMODEW

**dwColorOptimization** = 0

**dmPrintQuality** = **dmPrintQuality** member of DEVMODEW

**dmYResolution** = **dmYResolution** member of DEVMODEW

**dwNupDirection** = RIGHT\_THEN\_DOWN

**dwBookletFlags** = BOOKLET\_EDGE\_LEFT

**dwDuplexFlags** = 0

**dwScalingPercentX** = 100

**dwScalingPercentY** = 100

**dwJobHandlingFlags** = 0

See Remarks.

</dd> </dl>

## Return value

**GetJobAttributesEx** returns **TRUE** if it is successful in obtaining the print job attributes; otherwise, it returns **FALSE**.

## Remarks

This function first checks whether the driver supports the attribute level that is indicated by *dwLevel*. If the driver does not support that attribute level, then the function queries the driver for support for the next lower level, (*dwLevel* - 1), and continues to query for progressively lower levels of support until it obtains the level of support provided by the driver. If *dwFlags* is set to FILL\_WITH\_DEFAULTS, then the function fills in the default values for the unsupported levels.

## Requirements



|                            |                                                                                                          |
|----------------------------|----------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                       |
| Version<br/>         | This function is available in the Windows Vista operating system. <br/>                            |
| Header<br/>          | <dl> <dt>Winsplp.h (include Winsplp.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Spoolss.lib</dt> </dl>                   |
| DLL<br/>             | <dl> <dt>Spoolss.dll</dt> </dl>                   |



## See also

<dl> <dt>

[**ATTRIBUTE\_INFO\_3**](attribute-info-3.md)
</dt> <dt>

[**ATTRIBUTE\_INFO\_4**](attribute-info-4.md)
</dt> <dt>

[**DEVMODEW**](https://msdn.microsoft.com/b2369876-9a79-40c8-8d27-c8b9d8e68e6b)
</dt> <dt>

[**GetJobAttributes**](getjobattributes.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GetJobAttributesEx%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





