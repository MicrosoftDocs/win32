---
description: A callback that notifies the host of errors returned by the associated request.
MS-HAID: vspixengine.IPixErrorCallback\_ErrorListCallback\_DWORD\_Issue\_arr\_DWORD\_Issue\_arr
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IPixErrorCallback::ErrorListCallback method
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: B345846D-4853-4F6B-AB79-42265720451D
api_name: 
 - IPixErrorCallback.ErrorListCallback
api_type: 
 - COM
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.ipixerrorcallback_errorlistcallback_dword_issue_arr_dword_issue_arr"></span>IPixErrorCallback::ErrorListCallback method

A callback that notifies the host of errors returned by the associated request.

## Syntax


```C++
HRESULT ErrorListCallback(
   DWORD    count,
   Issue [] count0_errorList,
   DWORD    count,
   Issue [] count0_warningList
);
```

## Parameters

*count*   
The number of errors.

*count0\_errorList*   
The errors.

*count*   
The number of warningns.

*count0\_warningList*   
The warnings.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

<table><colgroup><col  /><col  /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**IPixErrorCallback**](/windows/desktop/direct3dtools/ipixerrorcallback)

 

 
