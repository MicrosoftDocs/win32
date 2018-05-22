---
title: MI Enumerations
description: WMI provides the following enumerations.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '6425D932-3F79-42D8-AC65-7F295FEAD7FC'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
---

# MI Enumerations

WMI provides the following enumerations.

## In this section

<dl> <dt>

[**MI\_CallbackMode**](mi-callbackmode.md)
</dt> <dd>

Defines the callback mode for the CIM extensions for **WriteError** and **PromptUser** functions.

</dd> <dt>

[**MI\_CancellationReason**](mi-cancellationreason.md)
</dt> <dd>

Value to pass to an operation cancel request to notify the system of the reason the operation is being canceled. If the service is being shutdown, it may pass one of these values to the provider as well.

</dd> <dt>

[**MI\_DestinationOptions\_ImpersonationType**](mi-destinationoptions-impersonationtype.md)
</dt> <dd>

Used by the DCOM protocol handler to specify how impersonation is done on the server.

</dd> <dt>

[**MI\_ErrorCategory**](mi-errorcategory.md)
</dt> <dd>

This enumeration defines error categories for the CIM extensions.

</dd> <dt>

[**MI\_LocaleType**](mi-localetype.md)
</dt> <dd>

Type of locale is needed when setting and getting locales.

</dd> <dt>

[**MI\_OperationCallback\_ResponseType**](mi-operationcallback-responsetype.md)
</dt> <dd>

If the MI\_CallbackMode is MI\_CALLBACKMODE\_INQUIRE, one of these values can be used in the callback.

</dd> <dt>

[**MI\_PromptType**](mi-prompttype.md)
</dt> <dd>

Defines prompt types for the CIM extensions.

</dd> <dt>

[**MI\_ProviderArchitecture**](mi-providerarchitecture.md)
</dt> <dd>

This enumeration defines the WMI provider architecture used on the server.

</dd> <dt>

[**MI\_Result**](mi-result.md)
</dt> <dd>

Defines function return codes.

</dd> <dt>

[**MI\_SubscriptionDeliveryType**](mi-subscriptiondeliverytype.md)
</dt> <dd>

Differentiates between a push or pull subscription delivery type. This is not supported when using the DCOM protocol.

</dd> <dt>

[**MI\_Type**](mi-type.md)
</dt> <dd>

These values specify the data type of qualifiers, properties, references, parameters, and method return values for the CIM data types.

</dd> </dl>

 

 




