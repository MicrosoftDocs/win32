---
description: Sets a new application callback for the image processing filter to use for forwarding calls.
ms.assetid: 25b86f1d-96c8-4150-9147-13be9b1dd50c
title: IWiaImageFilter::SetNewCallback method (Wia.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWiaImageFilter.SetNewCallback
api_type: 
- COM
api_location: 
- Wia.h
---

# IWiaImageFilter::SetNewCallback method

Sets a new application callback for the image processing filter to use for forwarding calls.

## Syntax


```C++
HRESULT SetNewCallback(
  [in] IWiaTransferCallback pWiaTransferCallback
);
```



## Parameters

<dl> <dt>

*pWiaTransferCallback* \[in\]
</dt> <dd>

Type: **[**IWiaTransferCallback**](-wia-iwiatransfercallback.md)**

Specifies a pointer to the application's [**IWiaTransferCallback**](-wia-iwiatransfercallback.md) interface.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

Do not call this method directly from your application.

The image processing filter is required to release the previously stored application callback interface before setting the new callback.

If *pWiaTransferCallback* is **NULL**, the image processing filter should simply release the old application callback and return S\_OK.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wia.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wia.idl</dt> </dl> |



 

 




