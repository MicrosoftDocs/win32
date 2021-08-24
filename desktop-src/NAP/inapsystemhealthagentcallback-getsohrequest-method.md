---
title: INapSystemHealthAgentCallback GetSoHRequest method (NapSystemHealthAgent.h)
description: Is called by the NapAgent to query the system health agent's SoH request.
ms.assetid: 4161a3e7-2f7a-40d1-b973-47f991bba5d0
keywords:
- GetSoHRequest method NAP
- GetSoHRequest method NAP , INapSystemHealthAgentCallback interface
- INapSystemHealthAgentCallback interface NAP , GetSoHRequest method
topic_type:
- apiref
api_name:
- INapSystemHealthAgentCallback.GetSoHRequest
api_location:
- NapSystemHealthAgent.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapSystemHealthAgentCallback::GetSoHRequest method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapSystemHealthAgentCallback::GetSoHRequest** method is called by the NapAgent to query the system health agent's SoH request.

## Syntax


```C++
HRESULT GetSoHRequest(
  [in] INapSystemHealthAgentRequest *request
);
```



## Parameters

<dl> <dt>

*request* \[in\]
</dt> <dd>

A COM pointer to an [**INapSystemHealthAgentRequest**](inapsystemhealthagentrequest.md) object that identifies the request object.

</dd> </dl>

## Return value



| Return code                                                                                                                      | Description                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                                             | Indicates success.<br/>                                                                                                                      |
| <dl> <dt>**HRESULT\_FROM\_WIN32(RPC\_S\_SERVER\_UNAVAILABLE)**</dt> </dl> | If this code is returned by your implementation, the NapAgent then removes the SHA from the bound-SHA list and flushes its cache entry.<br/> |



 

When any return value (except **HRESULT\_FROM\_WIN32(RPC\_S\_SERVER\_UNAVAILABLE)**) is returned by your implementation, the NAP system constructs and returns a [**SoHRequest**](/windows/win32/api/naptypes/ns-naptypes-soh) to the corresponding SHV with the following attribute types and values:

-   [**sohAttributeTypeSystemHealthId**](sohattributetype-enum.md)= &lt;id&gt;
-   [**sohAttributeTypeFailureCategory**](sohattributetype-enum.md)= [**failureCategoryClientComponent**](/windows/win32/api/naptypes/ne-naptypes-failurecategory)
-   [**sohAttributeTypeErrorCodes**](sohattributetype-enum.md) = &lt;error-code&gt;

## Remarks

This callback method is declared by the NAP system and is to be implemented by the SHA writer.

This method must process the request and return immediately. Delaying the return of this method negatively impacts system performance and responsiveness, and may cause other parts of the operating system to time out.

Health state monitoring should not be done as part of this call, especially if it is computation intensive and takes a long time. Health state monitoring and SoH computation should be performed in a separate thread or service. The sole function of this method should be to set the SHA's SoH and return.

If it will take a long time for the SHA to generate a SoH, then the cached SoH should be returned to the NapAgent. If there is no cached SoH to return, then the SHA should immediately return a SoH with the following attribute types and values:

-   [**sohAttributeTypeSystemHealthId**](sohattributetype-enum.md)= &lt;id&gt;
-   [**sohAttributeTypeFailureCategory**](sohattributetype-enum.md)= [**failureCategoryClientCommunication**](/windows/win32/api/naptypes/ne-naptypes-failurecategory)
-   [**sohAttributeTypeErrorCodes**](sohattributetype-enum.md) = [**NAP\_E\_NO\_CACHED\_SOH**](nap-error-constants.md)

When the SoH has been generated, the SHA must call [**INapSystemHealthAgentBinding::NotifySoHChange**](inapsystemhealthagentbinding-notifysohchange-method.md) to notify the NapAgent of the system health change.

The NapAgent calls this method to query the system health agent's SoHRequest. The SHA can query the passed [**INapSystemHealthAgentRequest**](inapsystemhealthagentrequest.md) object for parameters that it needs to compute the SoHRequest. The SHA must set the computed SoHRequest on the request object. The SHA must not hold references to the request object once this call has completed.

When this method is called, if there is a SoH in the NapAgent's cache, then it is set on the request object. The SHA can query for it using **GetSoHRequest**. If the SHA does not set a new SoH, then the cached one is used.

For unbound SHAs which are registered with the system, the NAP system constructs and sends a SoHRequest to the corresponding SHV with the following attribute types and values:

-   [**sohAttributeTypeSystemHealthId**](sohattributetype-enum.md)= &lt;id&gt;
-   [**sohAttributeTypeFailureCategory**](sohattributetype-enum.md)= [**failureCategoryClientComponent**](/windows/win32/api/naptypes/ne-naptypes-failurecategory)
-   [**sohAttributeTypeErrorCodes**](sohattributetype-enum.md) = [**NAP\_E\_NOT\_INITIALIZED**](nap-error-constants.md)

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                |
| Header<br/>                   | <dl> <dt>NapSystemHealthAgent.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>NapSystemHealthAgent.idl</dt> </dl> |



## See also

<dl> <dt>

[**INapSystemHealthAgentCallback**](inapsystemhealthagentcallback.md)
</dt> </dl>

 

 





