---
Description: The IPrintCoreUI2::GetFeatureAttribute method retrieves the feature attribute list or the value of a specific feature attribute.
ms.assetid: 6f3d16a9-bac7-44da-9d16-0f737d12d952
title: IPrintCoreUI2::GetFeatureAttribute method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrintCoreUI2::GetFeatureAttribute method

The `IPrintCoreUI2::GetFeatureAttribute` method retrieves the feature attribute list or the value of a specific feature attribute.

## Syntax


```C++
HRESULT GetFeatureAttribute(
  [in]  POEMUIOBJ poemuiobj,
  [in]  DWORD     dwFlags,
  [in]  PCSTR     pszFeatureKeyword,
  [in]  PCSTR     pszAttribute,
  [out] PDWORD    pdwDataType,
  [out] PBYTE     pbData,
  [in]  DWORD     cbSize,
  [out] PDWORD    pcbNeeded
);
```



## Parameters

<dl> <dt>

*poemuiobj* \[in\]
</dt> <dd>

Pointer to the current context, an [**OEMUIOBJ**](oemuiobj.md) structure.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Is reserved and must be set to zero.

</dd> <dt>

*pszFeatureKeyword* \[in\]
</dt> <dd>

Pointer to a caller-supplied buffer containing an ASCII string specifying the single feature keyword to query for. This value can be obtained from a prior call to [**IPrintCoreUI2::EnumFeatures**](iprintcoreui2-enumfeatures.md).

</dd> <dt>

*pszAttribute* \[in\]
</dt> <dd>

Pointer to a caller-supplied buffer containing an ASCII string specifying the single attribute requested. If this parameter is **NULL**, the caller is requesting a list of all supported feature attribute names, as opposed to specifying a specific feature attribute name.

</dd> <dt>

*pdwDataType* \[out\]
</dt> <dd>

Pointer to a memory location that receives a value specifying the data type of the requested attribute. This value is an enumerator of the [**EATTRIBUTE\_DATATYPE**](eattribute-datatype.md) enumeration, which is defined in printoem.h.

</dd> <dt>

*pbData* \[out\]
</dt> <dd>

Pointer to a caller-supplied buffer that receives the requested data. To simply query for the number of bytes needed to fulfill a request, set this parameter to **NULL**.

</dd> <dt>

*cbSize* \[in\]
</dt> <dd>

Specifies the size, in bytes of the buffer pointed to by `pbData`.

</dd> <dt>

*pcbNeeded* \[out\]
</dt> <dd>

Pointer to a memory location that receives the actual size, in bytes, of the requested data.

</dd> </dl>

## Return value

This method must return one of the following values.



| Return code                                                                                   | Description                                                                                                                                                                                                   |
|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | The method succeeded.<br/>                                                                                                                                                                              |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | The value in *cbSize* was smaller than the number of bytes to be written to the output buffer (the buffer pointed to by *pbData*).<br/> The method was called with *pbData* set to **NULL**.<br/> |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | The method attempted to query for a nonexistent attribute.<br/> The feature keyword was not recognized.<br/> The *poemuiobj* parameter pointed to an invalid context object.<br/>           |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | The method failed<br/>                                                                                                                                                                                  |



 

## Remarks

This method is supported only for Windows XP Pscript5 plug-ins, not for Unidrv plug-ins.

If this method is called with its *pszAttribute* and *pbData* parameters set to **NULL**, the method returns with \**pcbNeeded* set to the number of bytes needed for the list of all supported attribute names for the feature. If the method is called a second time, with *pszAttribute* set to **NULL** and *pbData* pointing to a buffer of the size specified in \**pcbNeeded* in the previous call, the method returns with \**pdwDataType* set to kADT\_ASCII (an enumerator of the [**EATTRIBUTE\_DATATYPE**](eattribute-datatype.md) enumerated type) and *pbData* pointing to a null-delimited list of all supported attribute names for the feature. This list is terminated with two null characters.

To reduce the need to make two calls per data access, pass the method an output buffer of a fixed size (1 KB, for example), and then check the function return value. If the method returns S\_OK, the buffer already contains the data of interest. If the method returns E\_OUTOFMEMORY, the value in \**pcbNeeded* is the buffer size needed to hold the data of interest. The caller should then allocate a buffer of that larger size and proceed with a second call to the method.

For more information, see [Using GetFeatureAttribute](https://www.bing.com/search?q=Using+GetFeatureAttribute).

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



## See also

<dl> <dt>

[**IPrintCoreUI2**](iprintcoreui2-interface.md)
</dt> <dt>

[**OEMUIOBJ**](oemuiobj.md)
</dt> <dt>

[**IPrintCoreUI2::EnumFeatures**](iprintcoreui2-enumfeatures.md)
</dt> <dt>

[**IPrintCoreUI2::GetGlobalAttribute**](iprintcoreui2-getglobalattribute.md)
</dt> <dt>

[**IPrintCoreUI2::GetOptionAttribute**](iprintcoreui2-getoptionattribute.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintCoreUI2::GetFeatureAttribute%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





