---
Description: 'Warning  Starting with Windows 10, the APIs which support third-party print providers are deprecated.'
ms.assetid: '54a5009d-9893-4766-b9fd-7e7474b55949'
title: InitializePrintProvidor function
---

# InitializePrintProvidor function

> \[!Warning\]
>
> Starting with Windows 10, the APIs which support third-party print providers are deprecated. Microsoft does not recommend any investment into third-party print providers. Additionally, on Windows 8 and newer products where the v4 print driver model is available, third-party print providers may not create or manage queues which use v4 print drivers.

 

A print provider's **InitializePrintProvidor** function initializes the provider and supplies the print spooler with the provider's entry points.

## Syntax


```C++
BOOL InitializePrintProvidor(
  _Out_    LPPRINTPROVIDOR pPrintProvidor,
  _In_     DWORD           cbPrintProvidor,
  _In_opt_ LPWSTR          pFullRegistryPath
);
```



## Parameters

<dl> <dt>

*pPrintProvidor* \[out\]
</dt> <dd>

Caller-supplied address of a [**PRINTPROVIDOR**](printprovidor.md) structure, to be filled in by the print provider.

</dd> <dt>

*cbPrintProvidor* \[in\]
</dt> <dd>

Caller-supplied size, in bytes, of the PRINTPROVIDOR structure pointed to by *pPrintProvidor*.

</dd> <dt>

*pFullRegistryPath* \[in, optional\]
</dt> <dd>

Caller-supplied pointer to a string representing the full registry path to the provider's registry entry.

</dd> </dl>

## Return value

If the operation succeeds, the function should return **TRUE**. Otherwise the function should return **FALSE**.

## Remarks

Print providers are required to define an **InitializePrintProvidor** function, which is the first function called by the spooler after the provider has been loaded. The function must fill the supplied [**PRINTPROVIDOR**](printprovidor.md) structure with pointers to the provider's defined functions (see [Functions Defined by Print Providers](print.functions_defined_by_print_providers)). The function can also perform other provider-specific initialization operations.

## Requirements



|                            |                                                                                                          |
|----------------------------|----------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                       |
| Header<br/>          | <dl> <dt>Winsplp.h (include Winsplp.h)</dt> </dl> |



## See also

<dl> <dt>

[**PRINTPROVIDOR**](printprovidor.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20InitializePrintProvidor%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





