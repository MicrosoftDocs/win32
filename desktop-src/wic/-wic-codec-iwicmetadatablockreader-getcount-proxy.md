---
Description: Proxy function for the GetCount method.
ms.assetid: 441bbbaf-5a6a-4d1e-bb8d-f79af6aa2708
title: IWICMetadataBlockReader\_GetCount\_Proxy function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IWICMetadataBlockReader\_GetCount\_Proxy function

Proxy function for the [**GetCount**](/windows/win32/Wincodecsdk/nf-wincodecsdk-iwicmetadatablockreader-getcount?branch=master) method.

## Syntax


```C++
HRESULT IWICMetadataBlockReader_GetCount_Proxy(
  _In_  IWICMetadataBlockReader *THIS_PTR,
  _Out_ UINT                    *pcCount
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICMetadataBlockReader**](/windows/win32/Wincodecsdk/nn-wincodecsdk-iwicmetadatablockreader?branch=master)\***

Pointer to this [**IWICMetadataBlockReader**](/windows/win32/Wincodecsdk/nn-wincodecsdk-iwicmetadatablockreader?branch=master) object.

</dd> <dt>

*pcCount* \[out\]
</dt> <dd>

Type: **UINT\***

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



 

 




