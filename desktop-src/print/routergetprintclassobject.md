---
Description: The RouterGetPrintClassObject function enumerates the list of print providers, searching for the print provider with the specified name and interface ID.
ms.assetid: e2df591d-59bd-4aae-ac1b-8fdf01da3ea7
title: RouterGetPrintClassObject function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# RouterGetPrintClassObject function

The `RouterGetPrintClassObject` function enumerates the list of print providers, searching for the print provider with the specified name and interface ID.

## Syntax


```C++
HRESULT RouterGetPrintClassObject(
  _In_  PCWSTR pPrinter,
  _In_  REFIID riid,
  _Out_ VOID   **ppv
);
```



## Parameters

<dl> <dt>

*pPrinter* \[in\]
</dt> <dd>

A pointer to a null-terminated string that contains the name of the printer or print server.

</dd> <dt>

*riid* \[in\]
</dt> <dd>

The identifier of the requested COM interface.

</dd> <dt>

*ppv* \[out\]
</dt> <dd>

A pointer to a variable that supplies the address of the COM interface requested in the *iid* parameter.

</dd> </dl>

## Return value

This function returns S\_OK on success, and a standard COM error code otherwise.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prnasntp.h (include Prnasntp.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Spoolss.lib</dt> </dl>                     |
| DLL<br/>             | <dl> <dt>Spoolss.dll</dt> </dl>                     |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20RouterGetPrintClassObject%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




