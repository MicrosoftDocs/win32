---
title: IConnectionBrokerClient GetTargetInfo method (Cbclient.h)
description: Requests information about the target computer where the connection should be redirected.
ms.assetid: 43970B06-8CBD-4204-94AE-090A63918A90
ms.tgt_platform: multiple
keywords:
- GetTargetInfo method Remote Desktop Services
- GetTargetInfo method Remote Desktop Services , IConnectionBrokerClient interface
- IConnectionBrokerClient interface Remote Desktop Services , GetTargetInfo method
topic_type:
- apiref
api_name:
- IConnectionBrokerClient.GetTargetInfo
api_location:
- Cbclient.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IConnectionBrokerClient::GetTargetInfo method

Requests information about the target computer where the connection should be redirected. This method is used by the redirector to get redirection information for the incoming connection request.

## Syntax


```C++
HRESULT GetTargetInfo(
  [in]  CB_CONNECTION_INFO       *pConnectionInfo,
  [in]  DWORD                    Reserved,
  [in]  HANDLE                   hStatusEvent,
  [out] CB_TARGET_INFO           *pTargetInfo,
  [out] DWORD                    *pResult,
  [out] IConnectionBrokerRequest **ppCbReq
);
```



## Parameters

<dl> <dt>

*pConnectionInfo* \[in\]
</dt> <dd>

The address of a [**CB\_CONNECTION\_INFO**](cb-connection-info.md) structure that contains information about the incoming connection request.

</dd> <dt>

*Reserved* \[in\]
</dt> <dd>

This parameter is reserved for future use and must be zero.

</dd> <dt>

*hStatusEvent* \[in\]
</dt> <dd>

The handle of an event that will get set whenever there is an update to the progress of the request. You are responsible for creating and closing this event.

</dd> <dt>

*pTargetInfo* \[out\]
</dt> <dd>

The address of a [**CB\_TARGET\_INFO**](cb-target-info.md) structure that receives information about the target computer where the incoming connection should be redirected. Because this is an asynchronous method, this memory must remain available until the request is complete. For more information, see Remarks.

</dd> <dt>

*pResult* \[out\]
</dt> <dd>

The address of a **DWORD** variable that receives a result code. Because this is an asynchronous method, this memory must remain available until the request is complete. For more information, see Remarks.

This result code will be one of the following values.

<dt>

0
</dt> <dd>

Success.

</dd> <dt>

0x0000400
</dt> <dd>

The destination computer could not be found.

</dd> <dt>

0x0000401
</dt> <dd>

The destination computer is not available.

</dd> <dt>

0x0000402
</dt> <dd>

Error loading destination computer.

</dd> <dt>

0x0000403
</dt> <dd>

Error bringing destination computer online.

</dd> <dt>

0x0000404
</dt> <dd>

Error redirecting to destination computer.

</dd> <dt>

0x0000405
</dt> <dd>

Error waking virtual machine.

</dd> <dt>

0x0000406
</dt> <dd>

Error booting virtual machine.

</dd> <dt>

0x0000407
</dt> <dd>

Error finding the IP address of the virtual machine.

</dd> <dt>

0x0000408
</dt> <dd>

The session broker could not find any available computers in the pool.

</dd> <dt>

0x0000409
</dt> <dd>

The session broker canceled the connection.

</dd> <dt>

0x0000410
</dt> <dd>

The session broker could not validate the connection settings.

</dd> </dl> </dd> <dt>

*ppCbReq* \[out\]
</dt> <dd>

The address of an [**IConnectionBrokerRequest**](iconnectionbrokerrequest.md) interface pointer that you use to obtain status updates for an asynchronous operation. This interface is used in conjunction with the *hStatusEvent* parameter to wait for and get the results of this asynchronous operation.

</dd> </dl>

## Return value

Returns **E\_PENDING** if the asynchronous request is created. Otherwise, it returns an **HRESULT** error code.

## Remarks

This method is asynchronous. The *pTargetInfo* and *pResult* parameters must remain valid until the [**IConnectionBrokerRequest::CheckStatus**](iconnectionbrokerrequest-checkstatus.md) method obtains **CB\_STATUS\_REQUEST\_COMPLETED**.

For more information about how to use this method, see [How to use the Remote Desktop Connection Broker client API](use-the-remote-desktop-connection-broker-client-api.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Header<br/>                   | <dl> <dt>Cbclient.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Cbclient.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Cbclient.dll</dt> </dl> |



## See also

<dl> <dt>

[**IConnectionBrokerClient**](iconnectionbrokerclient.md)
</dt> </dl>

 

 





