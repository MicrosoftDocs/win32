---
Description: The get\_MediaName method gets the media name. Defined media are audio, video, whiteboard, text, and data.
ms.assetid: 4afb24f9-582e-420d-8bda-772a3dc4d96c
title: ITMedia::get_MediaName method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ITMedia::get\_MediaName method

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **get\_MediaName** method gets the media name. Defined media are audio, video, whiteboard, text, and data.

## Syntax


```C++
);
```



## Parameters

<dl> <dt>

*ppMediaName* \[out\]
</dt> <dd>

Pointer to a **BSTR** containing the name of the media, such as audio.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                   | Description                                                     |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Method succeeded.<br/>                                    |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | The *ppMediaName* parameter is not a valid pointer.<br/>  |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory exists to perform the operation.<br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Unspecified error.<br/>                                   |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>     | This method is not yet implemented.<br/>                  |



 

## Remarks

The application must use [**SysFreeString**](https://msdn.microsoft.com/en-us/library/ms221481(v=VS.71).aspx) to free the memory allocated for the *ppMediaName* parameter.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>Sdpblb.h</dt> </dl>   |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Sdpblb.dll</dt> </dl> |



## See also

<dl> <dt>

[**ITMedia**](itmedia.md)
</dt> <dt>

[**ITMedia::put\_MediaName**](itmedia-put-medianame.md)
</dt> </dl>

 

 




