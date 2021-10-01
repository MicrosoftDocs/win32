---
description: A callback that notifies the host of a canceled request by using a cookie that uniquely identifies the request.
MS-HAID: vspixengine.INewFramesCallback\_CancelUsingCookie\_DWORD
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: INewFramesCallback::CancelUsingCookie method
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: 36176554-BB4F-40CB-AB7B-4957DA84BAA8
api_name: 
 - INewFramesCallback.CancelUsingCookie
api_type: 
 - COM
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.inewframescallback_cancelusingcookie_dword"></span>INewFramesCallback::CancelUsingCookie method

A callback that notifies the host of a canceled request by using a cookie that uniquely identifies the request.

## Syntax


```C++
HRESULT CancelUsingCallback(
   IUnknown * requestCallback
);
```

## Parameters

*requestCookie*   
The cookie which uniquely idenfies the cancelled request.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

<table><colgroup><col  /><col  /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**INewFramesCallback**](/windows/desktop/direct3dtools/inewframescallback)

 

 
