---
title: IInternetTransport HandsOffCallback method
description: Forces the transport to release the callback interface that was passed into the InitNew method of the transport (for example, InitNew).
ms.assetid: 'b7f76b03-bbb2-4373-8167-5e7c6260e719'
keywords: ["HandsOffCallback method Windows Mail (formerly Outlook Express)", "HandsOffCallback method Windows Mail (formerly Outlook Express) , IInternetTransport interface", "IInternetTransport interface Windows Mail (formerly Outlook Express) , HandsOffCallback method"]
topic_type:
- apiref
api_name:
- IInternetTransport.HandsOffCallback
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IInternetTransport::HandsOffCallback method

\[**IInternetTransport::HandsOffCallback** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Forces the transport to release the callback interface that was passed into the **InitNew** method of the transport (for example, [**InitNew**](oe-ismtptransport-initnew.md)).

## Syntax


```C++
HRESULT HandsOffCallback();
```



## Parameters

This method has no parameters.

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                             | Description                                                               |
|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>    | Indicates that the callback interface was released. <br/>           |
| <dl> <dt>**S\_FALSE**</dt> </dl> | Indicates that no callback interface is currently registered. <br/> |



 

## Remarks

After this method is called, no more calls can be made to the callback function. This method is provided so that clients can resolve possible circular references.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





