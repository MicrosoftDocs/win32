---
Description: 'Returns a string that describes the status code.'
ms.assetid: 'd3007f3e-46e1-4ab6-8ce3-c4e38f87ce61'
title: 'IWiaErrorHandler::GetStatusDescription method'
---

# IWiaErrorHandler::GetStatusDescription method

Returns a string that describes the status code.

## Syntax


```C++
HRESULT GetStatusDescription(
  [in]  IUnknown *punkItem,
  [in]  HRESULT  hrStatus,
  [in]  LONG     cbResLength,
  [in]  BYTE     *pbData,
  [out] BSTR     *pbstrDescription
);
```



## Parameters

<dl> <dt>

*punkItem* \[in\]
</dt> <dd>

Type: **[IUnknown](com.iunknown)\***

Pointer to the [IUnknown](com.iunknown) of the item being transferred. This object minimally implements [**IWiaItem2**](-wia-iwiaitem2.md) and [**IWiaDataTransfer**](-wia-iwiadatatransfer.md).

</dd> <dt>

*hrStatus* \[in\]
</dt> <dd>

Type: **HRESULT**

**HRESULT** that is the status code received by [**BandedDataCallback**](-wia-iwiadatacallback-bandeddatacallback.md).

</dd> <dt>

*cbResLength* \[in\]
</dt> <dd>

Type: **LONG**

**LONG** that is the size of the data referred to by *pbData*.

</dd> <dt>

*pbData* \[in\]
</dt> <dd>

Type: **BYTE\***

Pointer to the data buffer as received by [**BandedDataCallback**](-wia-iwiadatacallback-bandeddatacallback.md).

</dd> <dt>

*pbstrDescription* \[out\]
</dt> <dd>

Type: **BSTR\***

**BSTR** that receives a description of the status or error encountered during the data transfer. This parameter cannot be **NULL**. The caller must free the string using [SysFreeString](http://msdn.microsoft.com/en-US/library/ms221481.aspx), and the implementor must allocate the string using [SysAllocString](http://msdn.microsoft.com/en-US/library/ms221458.aspx).

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                             | Description                                                        |
|-----------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>    | *pbstrDescription* contains a valid **BSTR** pointer. <br/>  |
| <dl> <dt>**S\_FALSE**</dt> </dl> | *hrStatus* is unknown and no description is available. <br/> |



 

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                   |
| Header<br/>                   | <dl> <dt>Wia.h</dt> </dl>       |
| IDL<br/>                      | <dl> <dt>Wia.idl</dt> </dl>     |
| Library<br/>                  | <dl> <dt>Wiaguid.lib</dt> </dl> |



 

 




