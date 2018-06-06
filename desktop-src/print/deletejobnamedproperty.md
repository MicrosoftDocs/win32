---
Description: Deletes the named property for the specified print job on the specified printer.
ms.assetid: 14F8C0A2-0D19-446E-8C2B-530A3AEDA879
title: DeleteJobNamedProperty function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DeleteJobNamedProperty function

Deletes the named property for the specified print job on the specified printer.

## Syntax


```C++
 WINAPI DeleteJobNamedProperty(
  _In_ HANDLE hPrinter,
  _In_ DWORD  JobId,
  _In_ PCWSTR pszName
);
```



## Parameters

<dl> <dt>

*hPrinter* \[in\]
</dt> <dd>

A handle to the printer object of interest. Use the [OpenPrinter](https://www.bing.com/search?q=OpenPrinter), [**OpenPrinter2**](https://msdn.microsoft.com/e2370ae4-4475-4ccc-a6f9-3d33d1370054), or the [**AddPrinter**](https://msdn.microsoft.com/ffc4fee8-46c6-47ad-803d-623bf8efdefd) function to retrieve a printer handle.

</dd> <dt>

*JobId* \[in\]
</dt> <dd>

Identifier that specifies the print job. You obtain a print job identifier by calling the [**AddJob**](https://msdn.microsoft.com/cfafa874-6022-4bf4-bf3d-096213eb0c98) function or the [**StartDoc**](oemstartdoc.md) function.

</dd> <dt>

*pszName* \[in\]
</dt> <dd>

Name of the property that will be deleted.

</dd> </dl>

## Return value

If the operation succeeds, the function returns **ERROR\_SUCCESS.**

## Requirements



|                            |                                                                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                                                                         |
| Header<br/>          | <dl> <dt>Winspool.h (include Winspool.h)</dt> </dl>                                                 |
| Library<br/>         | <dl> <dt>WinSpool.lib</dt> </dl>                                                                    |
| DLL<br/>             | <dl> <dt>Spoolss.dll; </dt> <dt>WinSpool.drv</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20DeleteJobNamedProperty%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




