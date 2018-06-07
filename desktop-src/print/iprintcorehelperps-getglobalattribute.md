---
Description: The IPrintCoreHelperPS::GetGlobalAttribute method retrieves the global attribute list or the value of a specific global attribute.
ms.assetid: 4243ac31-83a7-47b5-8406-9d9537fbeb11
title: IPrintCoreHelperPS::GetGlobalAttribute method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrintCoreHelperPS::GetGlobalAttribute method

The **IPrintCoreHelperPS::GetGlobalAttribute** method retrieves the global attribute list or the value of a specific global attribute.

## Syntax


```C++
HRESULT GetGlobalAttribute(
  [in]  PCSTR  pszAttribute,
  [out] PDWORD pdwDataType,
  [out] PBYTE  pbData,
  [out] PDWORD pcbSize
);
```



## Parameters

<dl> <dt>

*pszAttribute* \[in\]
</dt> <dd>

A pointer to a caller-supplied buffer that contains an ANSI string that specifies the requested attribute. If this parameter is **NULL**, the caller is requesting a list of all of the supported global attribute names instead of specifying a specific global attribute name.

</dd> <dt>

*pdwDataType* \[out\]
</dt> <dd>

A pointer to variable that receives a value that specifies the data type of the requested attribute. This value is an enumerator of the [**EATTRIBUTE\_DATATYPE**](eattribute-datatype.md) enumeration type, which is defined in printoem.h.

</dd> <dt>

*pbData* \[out\]
</dt> <dd>

A pointer to a callee-allocated buffer containing the requested data. Upon completion of this method, the caller does not need to release this buffer.

</dd> <dt>

*pcbSize* \[out\]
</dt> <dd>

A pointer to a variable that specifies the size, in bytes, of the buffer that is pointed to by the *pbData* parameter.

</dd> </dl>

## Return value

**IPrintCoreHelperPS::GetGlobalAttribute** should return one of the following values.



| Return code                                                                                   | Description                                                                                                                               |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | The method succeeded.<br/>                                                                                                          |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | The method failed.<br/>                                                                                                             |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | The method attempted to query for a nonexistent attribute.<br/>                                                                     |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | The value in *pcbSize* was smaller than the number of bytes to be written to the output buffer that is pointed to by *pbData*.<br/> |



 

## Remarks

If **IPrintCoreHelperPS::GetGlobalAttribute** is called with its *pszAttribute* and *pbData* parameters set to **NULL**, the method returns with \**pcbSize* set to the number of bytes that are needed for the list of all of the supported global attribute names. If this method is called a second time, with *pszAttribute* set to **NULL** and *pbData* pointing to a buffer of the size that was specified in \**pcbSize* in the previous call, the method returns with \**pdwDataType* set to kADT\_ASCII (an enumerator of the [**EATTRIBUTE\_DATATYPE**](eattribute-datatype.md) enumeration type) and *pbData* pointing to a NULL-delimited list of all of the supported global attribute names. This list is terminated with two null characters.

For more information about **IPrintCoreHelperPS::GetGlobalAttribute**, see [Using GetGlobalAttribute](https://www.bing.com/search?q=Using+GetGlobalAttribute).

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



## See also

<dl> <dt>

[**IPrintCoreHelperPS**](iprintcorehelperps-interface.md)
</dt> <dt>

[**IPrintCoreHelperPS::GetFeatureAttribute**](iprintcorehelperps-getfeatureattribute.md)
</dt> <dt>

[**IPrintCoreHelperPS::GetOptionAttribute**](iprintcorehelperps-getoptionattribute.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintCoreHelperPS::GetGlobalAttribute%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





