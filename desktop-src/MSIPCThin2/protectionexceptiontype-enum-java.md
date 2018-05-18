---
title: ProtectionExceptionType enum
description: Maps the numeric error codes in the SDK to the relevant exception type, enabling the developer to check and handle the error code accordingly.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '61A777F5-1479-4D34-B831-D56AEF71A207'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["ProtectionExceptionType enum"]
topic_type:
- apiref
api_name:
- ProtectionExceptionType enum
api_type:
- NA
---

# ProtectionExceptionType enum

Maps the numeric error codes in the SDK to the relevant exception type, enabling the developer to check and handle the error code accordingly.

## Signature

``` syntax
public enum ProtectionExceptionType
```

## Types



| Exception                                                 | Error                                                                |
|-----------------------------------------------------------|----------------------------------------------------------------------|
| **DeviceRejectedException**<br/>                    | **SDK\_ERROR\_DEVICE\_REJECTED**<br/>                          |
| **GeneralException**<br/>                           | **SDK\_ERROR\_GENERAL**<br/>                                   |
| **CommunicationException**<br/>                     | **SDK\_ERROR\_COMMUNICATION**<br/>                             |
| **NoConsumptionRightsException**<br/>               | **SDK\_ERROR\_NO\_CONSUMPTION\_RIGHTS**<br/>                   |
| **InvalidParameterException**<br/>                  | **SDK\_ERROR\_INVALID\_PARAMETER**<br/>                        |
| **UnsupportedSDKVersionException**<br/>             | **SDK\_ERROR\_UNSUPPORTED\_SDK\_VERSION**<br/>                 |
| **ServiceNotAvailableException**<br/>               | **SDK\_ERROR\_SERVICE\_NOT\_AVAILABLE**<br/>                   |
| **InvalidPLException**<br/>                         | **SDK\_ERROR\_INVALID\_PL**<br/>                               |
| **UserRightsExpiredException**<br/>                 | **SDK\_ERROR\_USER\_RIGHTS\_EXPIRED**<br/>                     |
| **OnPremServersNotSupportedException**<br/>         | **SDK\_ERROR\_ON\_PREM\_SERVER\_NOT\_SUPPPORTED**<br/>         |
| **NoPublishingRightsException**<br/>                | **SDK\_ERROR\_NO\_PUBLISHING\_RIGHT**<br/>                     |
| **ServiceNotEnabledException**<br/>                 | **SDK\_ERROR\_REST\_SERVICE\_NOT\_ENABLED**<br/>               |
| **FailedAuthenticationException**<br/>              | **SDK\_AUTH\_ERROR**<br/>                                      |
| **InvalidDnsLookupResultException**<br/>            | **SDK\_ERROR\_INVALID\_PARAMETER**<br/>                        |
| **OfflineOnlyRequiresInternetException**<br/>       | **SDK\_ERROR\_OFFLINE\_ONLY\_REQUIRE\_INTERNET**<br/>          |
| **InvalidCertificateException**<br/>                | **SDK\_ERROR\_INVALID\_CERTIFICATE**<br/>                      |
| **UserCancellationException**<br/>                  | **SDK\_ERROR\_USER\_CANCELLED**<br/>                           |
| **NoConsumptionRightsContentRevokedException**<br/> | **SDK\_ERROR\_NO\_CONSUMPTION\_RIGHTS\_CONTENT\_REVOKED**<br/> |



 

## Defined in

ProtectionExceptionType.java

## Supported Platforms



|                                             |                                         |
|---------------------------------------------|-----------------------------------------|
| **Minimum supported OS version**<br/> | Android 4.0.3 (API level 15)<br/> |



 

## Package

com.microsoft.rightsmanagement.exceptions

## Thread Safety

Members of this class are not guaranteed to be thread safe.

 

 





