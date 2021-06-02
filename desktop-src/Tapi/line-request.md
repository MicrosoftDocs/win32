---
description: The TAPI LINE\_REQUEST message is sent to report the arrival of a new request from another application.
ms.assetid: d4dbba0d-8225-48d7-a66b-b189fdae70a8
title: LINE_REQUEST message (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINE\_REQUEST message

The TAPI **LINE\_REQUEST** message is sent to report the arrival of a new request from another application.


```C++
            
```



## Parameters

<dl> <dt>

*hDevice* 
</dt> <dd>

Not used.

</dd> <dt>

*dwCallbackInstance* 
</dt> <dd>

The registration instance of the application specified on [**lineRegisterRequestRecipient**](/windows/desktop/api/Tapi/nf-tapi-lineregisterrequestrecipient).

</dd> <dt>

*dwParam1* 
</dt> <dd>

The request mode of the newly pending request. This parameter uses the [**LINEREQUESTMODE\_ constants**](linerequestmode--constants.md).

</dd> <dt>

*dwParam2* 
</dt> <dd>

The conditions for this parameter are, if *dwParam1* is set to LINEREQUESTMODE\_DROP, *dwParam2* contains the *hWnd* of the application requesting the drop. Otherwise, *dwParam2* is unused.

</dd> <dt>

*dwParam3* 
</dt> <dd>

If *dwParam1* is set to LINEREQUESTMODE\_DROP, the low-order word of *dwParam3* contains the *wRequestID* as specified by the application that requested the drop. Otherwise, *dwParam3* is unused.

</dd> </dl>

## Return value

No return value.

## Remarks

The **LINE\_REQUEST** message is sent to the highest priority application that has registered for the corresponding request mode. This message indicates the arrival of an Assisted Telephony request of the specified request mode. If *dwParam1* is LINEREQUESTMODE\_MAKECALL, the application can invoke [**lineGetRequest**](/windows/desktop/api/Tapi/nf-tapi-linegetrequest) using the corresponding request mode to receive the request. If *dwParam1* is LINEREQUESTMODE\_DROP, the message contains all of the data the request recipient requires to perform the request.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



## See also

<dl> <dt>

[**lineGetRequest**](/windows/desktop/api/Tapi/nf-tapi-linegetrequest)
</dt> <dt>

[**lineRegisterRequestRecipient**](/windows/desktop/api/Tapi/nf-tapi-lineregisterrequestrecipient)
</dt> <dt>

[**tapiRequestMakeCall**](/windows/desktop/api/Tapi/nf-tapi-tapirequestmakecall)
</dt> </dl>

 

 




