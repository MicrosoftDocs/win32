---
title: com.microsoft.rightsmanagement.exceptions
description: Provides a set of classes and enumerations that represent exceptions that occur during RMS operations.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '6606411D-65A9-48AF-B325-80D493C27B2C'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
---

# com.microsoft.rightsmanagement.exceptions

Provides a set of classes and enumerations that represent exceptions that occur during RMS operations.

## In this section

<dl> <dt>

[**CommunicationException class**](communicationexception-class-java.md)
</dt> <dd>

Thrown when the device has no connection to the internet.

</dd> <dt>

[**DeviceRejectedException class**](devicerejectedexception-class-java.md)
</dt> <dd>

Implements a device rejected exception passed from the server.

</dd> <dt>

[**DnsLookupException class**](dnslookupexception-class-java.md)
</dt> <dd>

Thrown when the SDK has received an invalid DNS lookup message.

</dd> <dt>

[**FailedAuthenticationException class**](failedauthenticationexception-class-java.md)
</dt> <dd>

Signals that authentication failure has occurred. Extends the [**ProtectionException**](protectionexception-class-java.md) class.

</dd> <dt>

[**GeneralException class**](generalexception-class-java.md)
</dt> <dd>

A general exception used to wrap exceptions with a simplified error message. Extends the [**ProtectionException**](protectionexception-class-java.md) class.

This exception will prompt you, stating that an error has occurred and allowing you to send logging information to the Rights Management Service.

</dd> <dt>

[**InvalidCertificateException class**](invalidcertificateexception-class.md)
</dt> <dd>

Thrown when the SDK has received an invalid certificate. Extends the [**ProtectionException**](protectionexception-class-java.md) class.

</dd> <dt>

[**InvalidParameterException class**](invalidparameterexception-class-java.md)
</dt> <dd>

Signals an invalid parameter exception has occurred. Extends the [**ProtectionException**](protectionexception-class-java.md) class.

This exception will prompt you, stating that an error has occurred and allowing you to send logging information to the Rights Management Service.

</dd> <dt>

[**InvalidPLException class**](invalidplexception-class-java.md)
</dt> <dd>

Thrown when the publishing license that was supplied is corrupted. Extends the [**ProtectionException**](protectionexception-class-java.md) class.

This exception will prompt you, stating that an error has occurred and allowing you to send logging information to the Rights Management Service.

</dd> <dt>

[**NoConsumptionRightsContentRevokedException class**](noconsumptionrightscontentrevokedexception-class-java.md)
</dt> <dd>

Signals that the user does not have consumption rights over the protected content. Extends the [**ProtectionException**](protectionexception-class-java.md) class.

</dd> <dt>

[**NoConsumptionRightsException class**](noconsumptionrightsexception-class-java.md)
</dt> <dd>

Signals that the user does not have consumption rights over the protected content. Extends the [**ProtectionException**](protectionexception-class-java.md) class.

</dd> <dt>

[**NoPublishingRightsException class**](nopublishingrightsexception-class-java.md)
</dt> <dd>

Thrown when the user rights over the protected content have expired. Extends the [**ProtectionException**](protectionexception-class-java.md) class.

</dd> <dt>

[**OfflineOnlyRequiresInternetException class**](offlineonlyrequiresinternetexception-class-java.md)
</dt> <dd>

Thrown when communication is needed but the OFFLINE\_ONLY flag is set in consumption scenarios. Extends the [**ProtectionException**](protectionexception-class-java.md) class.

</dd> <dt>

[**OnPremServersNotSupportedException class**](onpremserversnotsupportedexception-class-java.md)
</dt> <dd>

Thrown when the SDK has tried to consume content published by an on-premises server. Extends the [**ProtectionException**](protectionexception-class-java.md) class.

</dd> <dt>

[**ProtectionException class**](protectionexception-class-java.md)
</dt> <dd>

Signals that a protection exception of some kind has occurred. This class is the general class used for exceptions produced by failed or interrupted RMS operations.

</dd> <dt>

[**ServiceNotAvailableException class**](servicenotavailableexception-class-java.md)
</dt> <dd>

Implements an exception which is used when a retry can help in solving the error which occurred Extends the [**ProtectionException**](protectionexception-class-java.md) class.

</dd> <dt>

[**RestServiceNotEnabledException class**](restservicenotenabledexception-class-java.md)
</dt> <dd>

Thrown if the user has an Office 365 account, but the company has not provisioned or enabled RMSO; or if the company has provisioned RMSO, but has not enabled the REST service for any of the AD RMS clients. Extends the [**ProtectionException**](protectionexception-class-java.md) class.

</dd> <dt>

[**UnsupportedSDKVersionException class**](unsupportedsdkversionexception-class-java.md)
</dt> <dd>

The operation is not supported by the version of the SDK. Extends the [**ProtectionException**](protectionexception-class-java.md) class.

</dd> <dt>

[**UserRightsExpiredException class**](userrightsexpiredexception-class-java.md)
</dt> <dd>

Thrown when the user rights over the protected content have expired. Extends the [**ProtectionException**](protectionexception-class-java.md) class.

</dd> <dt>

[**UserCancellationException class**](usercancellationexception-class-java.md)
</dt> <dd>

Signals that the user has canceled an operation. Extends the [**ProtectionException**](protectionexception-class-java.md) class.

</dd> <dt>

[**ProtectionExceptionType enum**](protectionexceptiontype-enum-java.md)
</dt> <dd>

Maps the numeric error codes in the SDK to the relevant exception type, enabling the developer to check and handle the error code accordingly.

</dd> </dl>

 

 




