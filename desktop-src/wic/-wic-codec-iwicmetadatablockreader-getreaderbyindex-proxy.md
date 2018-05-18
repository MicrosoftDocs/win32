---
Description: 'Proxy function for the GetReaderByIndex method.'
ms.assetid: '9d70b339-9772-4c13-949e-109f354f9986'
title: 'IWICMetadataBlockReader\_GetReaderByIndex\_Proxy function'
---

# IWICMetadataBlockReader\_GetReaderByIndex\_Proxy function

Proxy function for the [**GetReaderByIndex**](-wic-codec-iwicmetadatablockreader-getreaderbyindex.md) method.

## Syntax


```C++
HRESULT IWICMetadataBlockReader_GetReaderByIndex_Proxy(
  _In_  IWICMetadataBlockReader *THIS_PTR,
  _In_  UINT                    nIndex,
  _Out_ IWICMetadataReader      **ppIMetadataReader
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICMetadataBlockReader**](-wic-codec-iwicmetadatablockreader.md)\***

Pointer to this [**IWICMetadataBlockReader**](-wic-codec-iwicmetadatablockreader.md) object.

</dd> <dt>

*nIndex* \[in\]
</dt> <dd>

Type: **UINT**

</dd> <dt>

*ppIMetadataReader* \[out\]
</dt> <dd>

Type: **[**IWICMetadataReader**](-wic-codec-iwicmetadatareader.md)\*\***

</dd> </dl>

## Return value

Type: **HRESULT**

If this function succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

## Requirements



|                                     |                                                                                                                                                                  |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2, Windows Vista \[desktop apps only\]<br/>                                                                                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                                                                             |
| DLL<br/>                      | <dl> <dt>Windowscodecs.dll; </dt> <dt>Wincodec.lib</dt> </dl> |



 

 




