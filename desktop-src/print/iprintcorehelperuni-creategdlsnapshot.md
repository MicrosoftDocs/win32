---
Description: 'The IPrintCoreHelperUni::CreateGDLSnapshot method creates a GDL snapshot of the driver configuration file based on the current configuration.'
ms.assetid: '3dd9c7f9-27d4-45d2-8692-4270818c1823'
title: 'IPrintCoreHelperUni::CreateGDLSnapshot method'
---

# IPrintCoreHelperUni::CreateGDLSnapshot method

The `IPrintCoreHelperUni::CreateGDLSnapshot` method creates a GDL snapshot of the driver configuration file based on the current configuration.

## Syntax


```C++
HRESULT CreateGDLSnapshot(
  [in]  PDEVMODE pDevmode,
  [in]  DWORD    cbSize,
  [in]  DWORD    dwFlags,
  [out] LPSTREAM *ppSnapshotStream
);
```



## Parameters

<dl> <dt>

*pDevmode* \[in\]
</dt> <dd>

A pointer to a [**DEVMODEW**](display.devmodew) structure. If this pointer is provided, `IPrintCoreHelperUni::CreateGDLSnapshot` should use the DEVMODEW structure that is pointed to by *pDevmode* instead of the default or current DEVMODEW structure. If this method is called from the plug-in provider, there is no default DEVMODEW structure and the *pDevmode* parameter is required.

</dd> <dt>

*cbSize* \[in\]
</dt> <dd>

The size, in bytes, of the DEVMODEW structure that is pointed to by the *pDevmode* parameter.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Reserved for system use. This parameter must be set to zero.

</dd> <dt>

*ppSnapshotStream* \[out\]
</dt> <dd>

A pointer to a stream that supplies the XML version of the GDL snapshot.

</dd> </dl>

## Return value

`IPrintCoreHelperUni::CreateGDLSnapshot` should return S\_OK if the operation succeeds. Otherwise, this method should return a standard COM error code.

## Remarks

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



## See also

<dl> <dt>

[**IPrintCoreHelperUni**](iprintcorehelperuni-interface.md)
</dt> <dt>

[**IPrintCoreHelperUni::CreateDefaultGDLSnapshot**](iprintcorehelperuni-createdefaultgdlsnapshot.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintCoreHelperUni::CreateGDLSnapshot%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





