---
Description: The IPrintCoreHelperUniCreateDefaultGDLSnapshot method gets a GDL snapshot based on the driver default configuration.
ms.assetid: 987c3721-d8a8-4aac-8f42-6eac9b5ccdc5
title: IPrintCoreHelperUniCreateDefaultGDLSnapshot method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IPrintCoreHelperUni::CreateDefaultGDLSnapshot method

The `IPrintCoreHelperUni::CreateDefaultGDLSnapshot` method gets a GDL snapshot based on the driver default configuration.

## Syntax


```C++
HRESULT CreateDefaultGDLSnapshot(
  [in]  DWORD    dwFlags,
  [out] LPSTREAM *ppSnapshotStream
);
```



## Parameters

<dl> <dt>

*dwFlags* \[in\]
</dt> <dd>

This parameter is reserved and must be set to zero.

</dd> <dt>

*ppSnapshotStream* \[out\]
</dt> <dd>

A pointer to a stream that supplies the XML version of the GDL snapshot.

</dd> </dl>

## Return value

`IPrintCoreHelperUni::CreateDefaultGDLSnapshot` should return S\_OK if the operation succeeds. Otherwise, this method should return a standard COM error code.

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

[**IPrintCoreHelperUni::CreateGDLSnapshot**](iprintcorehelperuni-creategdlsnapshot.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintCoreHelperUni::CreateDefaultGDLSnapshot%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





