---
title: IWMDRMNetReceiver ProcessRegistrationResponse method (Wmdrmsdk.h)
description: The ProcessRegistrationResponse method processes a registration response sent by the transmitter in reply to a registration challenge.
ms.assetid: d0260e93-0a5e-494b-a723-bb62206ed55b
keywords:
- ProcessRegistrationResponse method windows Media Format
- ProcessRegistrationResponse method windows Media Format , IWMDRMNetReceiver interface
- IWMDRMNetReceiver interface windows Media Format , ProcessRegistrationResponse method
topic_type:
- apiref
api_name:
- IWMDRMNetReceiver.ProcessRegistrationResponse
api_location:
- Wmdrmsdk.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMDRMNetReceiver::ProcessRegistrationResponse method

The **ProcessRegistrationResponse** method processes a registration response sent by the transmitter in reply to a registration challenge.

## Syntax


```C++
HRESULT ProcessRegistrationResponse(
  [in]  BYTE     *pbRegistrationResponse,
  [in]  DWORD    cbRegistrationResponse,
  [out] IUnknown **ppunkCancellationCookie
);
```



## Parameters

<dl> <dt>

*pbRegistrationResponse* \[in\]
</dt> <dd>

Registration response received from the transmitter.

</dd> <dt>

*cbRegistrationResponse* \[in\]
</dt> <dd>

Size of the registration response in bytes.

</dd> <dt>

*ppunkCancellationCookie* \[out\]
</dt> <dd>

Pointer that receives a pointer to the **IUnknown** interface of an object that identifies this asynchronous call. This interface pointer can be used to cancel the asynchronous call by calling the [**IWMDRMEventGenerator::CancelAsyncOperation**](iwmdrmeventgenerator-cancelasyncoperation.md) method.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## Remarks

This method executes asynchronously; when processing is complete, the MEProximityCompleted event is sent to the **IMFMediaEventGenerator** interface.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdrmsdk.h</dt> </dl> |



## See also

<dl> <dt>

[**IWMDRMNetReceiver Interface**](iwmdrmnetreceiver.md)
</dt> <dt>

[**IWMDRMNetReceiver::GetRegistrationChallenge**](iwmdrmnetreceiver-getregistrationchallenge.md)
</dt> </dl>

 

 





