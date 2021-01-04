---
title: CB_REQUEST_STATUS enumeration (Cbclient.h)
description: Specifies the status of an asynchronous request.
ms.assetid: 35FAC8EA-BA17-405F-AE10-33A816029F62
ms.tgt_platform: multiple
keywords:
- CB_REQUEST_STATUS enumeration Remote Desktop Services
topic_type:
- apiref
api_name:
- CB_REQUEST_STATUS
api_location:
- Cbclient.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CB\_REQUEST\_STATUS enumeration

Specifies the status of an asynchronous request. This enumeration is used with the [**IConnectionBrokerRequest::CheckStatus**](iconnectionbrokerrequest-checkstatus.md) method.

## Syntax


```C++
typedef enum _CB_REQUEST_STATUS { 
  CB_STATUS_INVALID                     = 1,
  CB_STATUS_INITIATING_REQUEST          = 0,
  CB_STATUS_REQUEST_COMPLETED,
  CB_STATUS_REQUEST_FAILED,
  CB_STATUS_REQUEST_ABORTED,
  CB_STATUS_FINDING_DESTINATION,
  CB_STATUS_LOADING_DESTINATION,
  CB_STATUS_BRINGING_SESSION_ONLINE,
  CB_STATUS_REDIRECTING_TO_DESTINATION
} CB_REQUEST_STATUS;
```



## Constants

<dl> <dt>

<span id="CB_STATUS_INVALID"></span><span id="cb_status_invalid"></span>**CB\_STATUS\_INVALID**
</dt> <dd>

The request object is not initialized.

</dd> <dt>

<span id="CB_STATUS_INITIATING_REQUEST"></span><span id="cb_status_initiating_request"></span>**CB\_STATUS\_INITIATING\_REQUEST**
</dt> <dd>

Not used.

</dd> <dt>

<span id="CB_STATUS_REQUEST_COMPLETED"></span><span id="cb_status_request_completed"></span>**CB\_STATUS\_REQUEST\_COMPLETED**
</dt> <dd>

The request is complete.

</dd> <dt>

<span id="CB_STATUS_REQUEST_FAILED"></span><span id="cb_status_request_failed"></span>**CB\_STATUS\_REQUEST\_FAILED**
</dt> <dd>

The request failed.

</dd> <dt>

<span id="CB_STATUS_REQUEST_ABORTED"></span><span id="cb_status_request_aborted"></span>**CB\_STATUS\_REQUEST\_ABORTED**
</dt> <dd>

The request was aborted.

</dd> <dt>

<span id="CB_STATUS_FINDING_DESTINATION"></span><span id="cb_status_finding_destination"></span>**CB\_STATUS\_FINDING\_DESTINATION**
</dt> <dd>

Not used.

</dd> <dt>

<span id="CB_STATUS_LOADING_DESTINATION"></span><span id="cb_status_loading_destination"></span>**CB\_STATUS\_LOADING\_DESTINATION**
</dt> <dd>

Not used.

</dd> <dt>

<span id="CB_STATUS_BRINGING_SESSION_ONLINE"></span><span id="cb_status_bringing_session_online"></span>**CB\_STATUS\_BRINGING\_SESSION\_ONLINE**
</dt> <dd>

Not used.

</dd> <dt>

<span id="CB_STATUS_REDIRECTING_TO_DESTINATION"></span><span id="cb_status_redirecting_to_destination"></span>**CB\_STATUS\_REDIRECTING\_TO\_DESTINATION**
</dt> <dd>

Not used.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                        |
| Header<br/>                   | <dl> <dt>Cbclient.h</dt> </dl> |



## See also

<dl> <dt>

[**IConnectionBrokerRequest::CheckStatus**](iconnectionbrokerrequest-checkstatus.md)
</dt> </dl>

 

 





