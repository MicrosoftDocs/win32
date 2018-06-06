---
Description: Warning  Starting with Windows 10, the APIs which support third-party print providers are deprecated.
ms.assetid: 06affa2e-d22c-4d24-8c5f-6ef52e3051fa
title: GetJobAttributes function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetJobAttributes function

> \[!Warning\]
>
> Starting with Windows 10, the APIs which support third-party print providers are deprecated. Microsoft does not recommend any investment into third-party print providers. Additionally, on Windows 8 and newer products where the v4 print driver model is available, third-party print providers may not create or manage queues which use v4 print drivers.

 

A print provider's **GetJobAttributes** function gets information about a print job.

## Syntax


```C++
BOOL GetJobAttributes(
  _In_  LPWSTR            pPrinterName,
  _In_  LPDEVMODEW        pDevmode,
  _Out_ PATTRIBUTE_INFO_3 pAttributeInfo
);
```



## Parameters

<dl> <dt>

*pPrinterName* \[in\]
</dt> <dd>

Caller-supplied pointer to a NULL-terminated Unicode string containing the printer name.

</dd> <dt>

*pDevmode* \[in\]
</dt> <dd>

Caller-supplied pointer to a [**DEVMODEW**](https://msdn.microsoft.com/b2369876-9a79-40c8-8d27-c8b9d8e68e6b) structure that is passed to the print processor or printer driver.

</dd> <dt>

*pAttributeInfo* \[out\]
</dt> <dd>

Caller-supplied pointer to an [**ATTRIBUTE\_INFO\_3**](attribute-info-3.md) structure that receives information about the print job.

</dd> </dl>

## Return value

**GetJobAttributes** returns **TRUE** if it is successful in obtaining the print job attributes; otherwise it returns **FALSE**.

## Remarks

## Requirements



|                            |                                                                                                              |
|----------------------------|--------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                           |
| Version<br/>         | This function is available in Microsoft Windows Server 2003 and later operating system versions. <br/> |
| Header<br/>          | <dl> <dt>Winsplp.h (include Winsplp.h)</dt> </dl>     |
| Library<br/>         | <dl> <dt>Spoolss.lib</dt> </dl>                       |
| DLL<br/>             | <dl> <dt>Spoolss.dll</dt> </dl>                       |



## See also

<dl> <dt>

[**DEVMODEW**](https://msdn.microsoft.com/b2369876-9a79-40c8-8d27-c8b9d8e68e6b)
</dt> <dt>

[**ATTRIBUTE\_INFO\_3**](attribute-info-3.md)
</dt> <dt>

[**GetJobAttributesEx**](getjobattributesex.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GetJobAttributes%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





