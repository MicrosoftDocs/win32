---
Description: Proxy function for the Commit method.
ms.assetid: 5b3b90ad-9d67-4fbd-b01e-c7478df8dd45
title: IWICFastMetadataEncoder\_Commit\_Proxy function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IWICFastMetadataEncoder\_Commit\_Proxy function

Proxy function for the [**Commit**](/windows/win32/Wincodec/nf-wincodec-iwicfastmetadataencoder-commit?branch=master) method.

## Syntax


```C++
HRESULT IWICFastMetadataEncoder_Commit_Proxy(
  _In_ IWICFastMetadataEncoder *THIS_PTR
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICFastMetadataEncoder**](/windows/win32/Wincodec/nn-wincodec-iwicfastmetadataencoder?branch=master)\***

Pointer to this [**IWICFastMetadataEncoder**](/windows/win32/Wincodec/nn-wincodec-iwicfastmetadataencoder?branch=master) object.

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



 

 




