---
Description: 'Proxy function for the RemoveMetadataByName method.'
ms.assetid: 'fb86766e-234d-4e39-9d4b-7814d50a3867'
title: 'IWICMetadataQueryWriter\_RemoveMetadataByName\_Proxy function'
---

# IWICMetadataQueryWriter\_RemoveMetadataByName\_Proxy function

Proxy function for the [**RemoveMetadataByName**](-wic-codec-iwicmetadataquerywriter-removemetadatabyname.md) method.

## Syntax


```C++
HRESULT IWICMetadataQueryWriter_RemoveMetadataByName_Proxy(
  _In_ IWICMetadataQueryWriter *THIS_PTR,
  _In_ LPCWSTR                 wzName
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICMetadataQueryWriter**](-wic-codec-iwicmetadataquerywriter.md)\***

Pointer to this [**IWICMetadataQueryWriter**](-wic-codec-iwicmetadataquerywriter.md) object.

</dd> <dt>

*wzName* \[in\]
</dt> <dd>

Type: **LPCWSTR**

The name of the metadata item to remove.

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



 

 




