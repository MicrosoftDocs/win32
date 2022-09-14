---
title: INapSystemHealthValidator Validate method (NapSystemHealthValidator.h)
description: The NAP system to validate the SoHRequest received from a client.
ms.assetid: d67dc2c8-f18c-4e06-a51e-a538ca75c3f1
keywords:
- Validate method NAP
- Validate method NAP , INapSystemHealthValidator interface
- INapSystemHealthValidator interface NAP , Validate method
topic_type:
- apiref
api_name:
- INapSystemHealthValidator.Validate
api_location:
- NapSystemHealthValidator.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapSystemHealthValidator::Validate method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapSystemHealthValidator::Validate** method is defined by the SHV developer and called by the NAP system to validate the [**SoHRequest**](/windows/win32/api/naptypes/ns-naptypes-soh) received from a client.

## Syntax


```C++
HRESULT Validate(
  [in] INapSystemHealthValidationRequest *request,
  [in] UINT32                            hintTimeOutInMsec,
  [in] INapServerCallback                *callback
);
```



## Parameters

<dl> <dt>

*request* \[in\]
</dt> <dd>

A COM pointer to an [**INapSystemHealthValidationRequest**](inapsystemhealthvalidationrequest.md) object that identifies the validation request object.

</dd> <dt>

*hintTimeOutInMsec* \[in\]
</dt> <dd>

The duration, in milliseconds, of the communication timeout period. The System Health Validator (SHV) should respond within this amount of time; otherwise the response is dropped.

> [!Note]  
> The default timeout for all SHVs is 2000 milliseconds. Using a value other than the default will change the timeout for all registered SHVs.

 

</dd> <dt>

*callback* \[in\]
</dt> <dd>

A pointer to the callback object [**INapServerCallback**](inapservercallback.md). This callback pointer is used by the SHVs when they return **E\_PENDING** from the call to **INapSystemHealthValidator::Validate**. This is used for asynchronous validation. The SHVs are expected to respond within the *hintTimeOutInMsec* time or else the response will be dropped.

</dd> </dl>

## Return value

If any other error code is returned, then the system assumes serverComponent failure has occurred, and the appropriate mapping is done to pass/fail.



| Return code                                                                                                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                       | Indicates that the validator has set an SoHResponse on the 'request' object.<br/>                                                                                                                                                                                                                                                                                                                                                                                                        |
| <dl> <dt>**E\_PENDING**</dt> </dl>                  | Indicates that OnComplete() will be called on a separate thread.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                    |
| <dl> <dt>**RPC\_S\_SERVER\_UNAVAILABLE**</dt> </dl> | Indicates that the System Health Validator (SHV) process terminated without the NapServer actually releasing a reference to it. The NapServer will try to re-create a new reference to the SHV and will reexecute the Validate call once. If the creation of the object or the re-executed Validate fails, the SHV is removed from the list of loaded SHVs. The only way this SHV can now be reloaded is to unregister and reregister the SHV again, or when the NapServer restarts<br/> |



 

## Remarks

In order to support intrusion detection, SHVs will be asked to validate the client machine regardless of whether the client sent an [**SoHRequest**](/windows/win32/api/naptypes/ns-naptypes-soh) intended for the SHV.

The SHV must do the following:

-   Retrieve the [**SoHRequest**](/windows/win32/api/naptypes/ns-naptypes-soh) from *request* by calling [**request.GetSoHRequest()**](inapsystemhealthvalidationrequest-getsohrequest-method.md).
-   If the [**SoHRequest**](/windows/win32/api/naptypes/ns-naptypes-soh) packet is null:
    -   If the SHV is an intrusion detection system, populate an [**SoHRequest**](/windows/win32/api/naptypes/ns-naptypes-soh) packet with the appropriate [**NAP error code**](nap-error-constants.md) as to why the client machine is malicious.
    -   All other SHVs should populate an [**SoHRequest**](/windows/win32/api/naptypes/ns-naptypes-soh) packet with an error code of [**NAP\_E\_MISSING\_SOH**](nap-error-constants.md).
-   If *napSystemGenerated* is **TRUE** from the call to [**request.GetSoHRequest()**](inapsystemhealthvalidationrequest-getsohrequest-method.md), the SHV should expect an [**SoH**](/windows/win32/api/naptypes/ns-naptypes-soh) packet with the following 3 TLVs: [**sohAttributeTypeSystemHealthId**](sohattributetype-enum.md), **sohAttributeTypeFailureCategory**, **sohAttributeTypeErrorCodes**. This **SoHRequest** is generated by the NapAgent on behalf of the System Health Agent (SHA) since there was an error in retrieving a request packet from the SHA.
-   Validate the [**SoHRequest**](/windows/win32/api/naptypes/ns-naptypes-soh) packet.
    -   If the [**SoHRequest**](/windows/win32/api/naptypes/ns-naptypes-soh) is malformed, then construct a **SoHResponse** packet with error code [**NAP\_E\_INVALID\_PACKET**](nap-error-constants.md).
    -   If the SHV is only using cached information to validate the [**SoHRequest**](/windows/win32/api/naptypes/ns-naptypes-soh) packet (i.e. no I/O is performed), then it can construct the **SoHResponse**, set it on the object in *request* and return **S\_OK**.
    -   If the SHV is performing I/O in order to talk to its back-end servers to validate the client's health, then it must queue up the I/O and return this function with **E\_PENDING**. In this case, the SHV must call [**callback.OnComplete()**](inapservercallback-oncomplete-method.md) on a separate thread within the timeout period, *hintTimeOutInMsec*. Otherwise, the SHV's response will be dropped.
-   Do not return any other error other than those listed above. If any other error code is returned by the SHV (eg. some system error), the packet will be discarded.

An SHV must return either an **sohAttributeTypeComplianceResultCodes** or **sohAttributeTypeFailureCategory** TLV in its [**SoHRequest**](/windows/win32/api/naptypes/ns-naptypes-soh).

-   [**sohAttributeTypeComplianceResultCodes TLV**](sohattributetype-enum.md): If the SHV could validate the health of the client (i.e. healthy or unhealthy), this TLV is returned.
-   [**sohAttributeTypeFailureCategory TLV**](sohattributetype-enum.md): If there was any component or communication failure on the client or server, it must be indicated by this TLV. This TLV will further be mapped to healthy or unhealthy depending upon the SHV's configuration. For more details, see the [**INapServerManagement**](inapservermanagement.md) interface and the [**FailureCategoryMapping**](/windows/win32/api/naptypes/ns-naptypes-failurecategorymapping) structure.

The SHV must not hold references to *request* or *callback* once the asyncronous call completes.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                    |
| Header<br/>                   | <dl> <dt>NapSystemHealthValidator.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>NapSystemHealthValidator.idl</dt> </dl> |



## See also

<dl> <dt>

[**INapSystemHealthValidator**](inapsystemhealthvalidator.md)
</dt> </dl>

 

 





