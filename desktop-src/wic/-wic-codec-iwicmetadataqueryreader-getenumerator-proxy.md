---
description: Proxy function for the GetEnumerator method.
ms.assetid: b45b240d-7540-4115-ac8b-401aaf400a9d
title: IWICMetadataQueryReader_GetEnumerator_Proxy function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWICMetadataQueryReader_GetEnumerator_Proxy
api_type: 
- DllExport
api_location: 
- Windowscodecs.dll
- Wincodec.lib
---

# IWICMetadataQueryReader\_GetEnumerator\_Proxy function

Proxy function for the [**GetEnumerator**](/windows/desktop/api/Wincodec/nf-wincodec-iwicmetadataqueryreader-getenumerator) method.

## Syntax


```C++
HRESULT IWICMetadataQueryReader_GetEnumerator_Proxy(
  _In_  IWICMetadataQueryReader *THIS_PTR,
  _Out_ IEnumString             **ppIEnumString
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICMetadataQueryReader**](/windows/desktop/api/Wincodec/nn-wincodec-iwicmetadataqueryreader)\***

Pointer to this [**IWICMetadataQueryReader**](/windows/desktop/api/Wincodec/nn-wincodec-iwicmetadataqueryreader) object.

</dd> <dt>

*ppIEnumString* \[out\]
</dt> <dd>

Type: **IEnumString\*\***

A pointer that receives a pointer to a metadata enumerator.

</dd> </dl>

## Return value

Type: **HRESULT**

If this function succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2, Windows Vista \[desktop apps only\]<br/>                                                                                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                                                                             |
| DLL<br/>                      | <dl> <dt>Windowscodecs.dll; </dt> <dt>Wincodec.lib</dt> </dl> |



 

 




