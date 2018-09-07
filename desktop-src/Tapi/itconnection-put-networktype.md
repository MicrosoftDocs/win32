---
Description: The put\_NetworkType method sets the network type.
ms.assetid: 747e3133-d103-44dc-b119-5a4cb4ed7f18
title: ITConnection::put_NetworkType method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ITConnection::put\_NetworkType method

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **put\_NetworkType** method sets the network type.

## Syntax


```C++
);
```



## Parameters

<dl> <dt>

*pNetworkType* \[in\]
</dt> <dd>

Pointer to a **BSTR** containing the network type.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                   | Description                                                     |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Method succeeded.<br/>                                    |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | The *pNetworkType* parameter is not valid.<br/>           |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory exists to perform the operation.<br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Unspecified error.<br/>                                   |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>     | This method is not yet implemented.<br/>                  |



 

## Remarks

The application must use [**SysAllocString**](https://msdn.microsoft.com/en-us/library/ms221458(v=VS.71).aspx) to allocate memory for the *pNetworkType* parameter and use [**SysFreeString**](https://msdn.microsoft.com/en-us/library/ms221481(v=VS.71).aspx) to free the memory when the variable is no longer needed.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>Sdpblb.h</dt> </dl>   |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Sdpblb.dll</dt> </dl> |



## See also

<dl> <dt>

[**ITConnection**](itconnection.md)
</dt> <dt>

[**ITConnection::get\_NetworkType**](itconnection-get-networktype.md)
</dt> </dl>

 

 




