---
title: INapSystemHealthValidationRequest GetSoHRequest method (NapSystemHealthValidator.h)
description: Allows System Health Validators (SHVs) to retrieve and validate the SoHRequest information sent by their System Health Agent (SHA) counterparts on the client.
ms.assetid: e06e07c6-7305-4171-b94e-19c360e94c67
keywords:
- GetSoHRequest method NAP
- GetSoHRequest method NAP , INapSystemHealthValidationRequest interface
- INapSystemHealthValidationRequest interface NAP , GetSoHRequest method
topic_type:
- apiref
api_name:
- INapSystemHealthValidationRequest.GetSoHRequest
api_location:
- qshvhost.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapSystemHealthValidationRequest::GetSoHRequest method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapSystemHealthValidationRequest::GetSoHRequest** method allows System Health Validators (SHVs) to retrieve and validate the [**SoHRequest**](/windows/win32/api/naptypes/ns-naptypes-soh) information sent by their System Health Agent (SHA) counterparts on the client.

## Syntax


```C++
HRESULT GetSoHRequest(
  [out] SoHRequest **sohRequest,
  [out] BOOL       *napSystemGenerated
);
```



## Parameters

<dl> <dt>

*sohRequest* \[out\]
</dt> <dd>

A pointer to a pointer to an [**SoHRequest**](/windows/win32/api/naptypes/ns-naptypes-soh) structure.

</dd> <dt>

*napSystemGenerated* \[out\]
</dt> <dd>

A **BOOL** that is **TRUE** if the SoH was created by the NapAgent on behalf of the SHA and **FALSE** otherwise. It is primarily used to indicate an SHA failure to the SHV.

</dd> </dl>

## Return value

Other COM-specific error codes also may be returned.



| Return code                                                                                     | Description                                                        |
|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**S\_OK** </dt> </dl>           | Operation succeeded.<br/>                                    |
| <dl> <dt>**E\_ACCESSDENIED** </dt> </dl> | Permissions error, access denied.<br/>                       |
| <dl> <dt>**E\_OUTOFMEMORY** </dt> </dl>  | System resource limit, could not perform the operation.<br/> |



 

## Remarks

The *sohRequest* parameter may return **NULL** if the client did not send an [**SoHRequest**](/windows/win32/api/naptypes/ns-naptypes-soh) to the SHV. In that scenario the SHV can populate an **SoHResponse** with the error code of [**NAP\_E\_MISSING\_SOH**](nap-error-constants.md).

If the *napSystemGenerated* parameter is **TRUE**, the format of *SoHRequest* is as follows:

-   [**sohAttributeTypeSystemHealthId**](sohattributetype-enum.md)= <id>
-   [**sohAttributeTypeFailureCategory**](sohattributetype-enum.md)= [**failureCategoryClientComponent**](/windows/win32/api/naptypes/ne-naptypes-failurecategory)
-   [**sohAttributeTypeErrorCodes**](sohattributetype-enum.md) = [**<sha-failure-error-code>**](nap-error-constants.md)

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                    |
| Header<br/>                   | <dl> <dt>NapSystemHealthValidator.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>NapSystemHealthValidator.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Qshvhost.dll</dt> </dl>                 |



## See also

<dl> <dt>

[**INapSystemHealthValidationRequest**](inapsystemhealthvalidationrequest.md)
</dt> </dl>

 

 





