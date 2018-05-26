---
Description: Proxy function for the GetEnumerator method.
ms.assetid: b45b240d-7540-4115-ac8b-401aaf400a9d
title: IWICMetadataQueryReader\_GetEnumerator\_Proxy function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IWICMetadataQueryReader\_GetEnumerator\_Proxy function

Proxy function for the [**GetEnumerator**](/windows/win32/Wincodec/nf-wincodec-iwicmetadataqueryreader-getenumerator?branch=master) method.

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

Type: **[**IWICMetadataQueryReader**](/windows/win32/Wincodec/nn-wincodec-iwicmetadataqueryreader?branch=master)\***

Pointer to this [**IWICMetadataQueryReader**](/windows/win32/Wincodec/nn-wincodec-iwicmetadataqueryreader?branch=master) object.

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



|                                     |                                                                                                                                                                  |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2, Windows Vista \[desktop apps only\]<br/>                                                                                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                                                                             |
| DLL<br/>                      | <dl> <dt>Windowscodecs.dll; </dt> <dt>Wincodec.lib</dt> </dl> |



 

 




