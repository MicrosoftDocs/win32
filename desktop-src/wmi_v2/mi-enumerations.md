---
title: MI Enumerations
description: WMI provides the following enumerations.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6425D932-3F79-42D8-AC65-7F295FEAD7FC
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MI Enumerations

WMI provides the following enumerations.

## In this section

<dl> <dt>

[**MI\_CallbackMode**](/windows/previous-versions/Mi/ne-mi-_mi_callbackmode?branch=master)
</dt> <dd>

Defines the callback mode for the CIM extensions for **WriteError** and **PromptUser** functions.

</dd> <dt>

[**MI\_CancellationReason**](/windows/previous-versions/Mi/ne-mi-_mi_cancellationreason?branch=master)
</dt> <dd>

Value to pass to an operation cancel request to notify the system of the reason the operation is being canceled. If the service is being shutdown, it may pass one of these values to the provider as well.

</dd> <dt>

[**MI\_DestinationOptions\_ImpersonationType**](/windows/previous-versions/Mi/ne-mi-_mi_destinationoptions_impersonationtype?branch=master)
</dt> <dd>

Used by the DCOM protocol handler to specify how impersonation is done on the server.

</dd> <dt>

[**MI\_ErrorCategory**](/windows/previous-versions/Mi/ne-mi-_mi_errorcategory?branch=master)
</dt> <dd>

This enumeration defines error categories for the CIM extensions.

</dd> <dt>

[**MI\_LocaleType**](/windows/previous-versions/Mi/ne-mi-_mi_localetype?branch=master)
</dt> <dd>

Type of locale is needed when setting and getting locales.

</dd> <dt>

[**MI\_OperationCallback\_ResponseType**](/windows/previous-versions/Mi/ne-mi-_mi_operationcallback_responsetype?branch=master)
</dt> <dd>

If the MI\_CallbackMode is MI\_CALLBACKMODE\_INQUIRE, one of these values can be used in the callback.

</dd> <dt>

[**MI\_PromptType**](/windows/previous-versions/Mi/ne-mi-_mi_prompttype?branch=master)
</dt> <dd>

Defines prompt types for the CIM extensions.

</dd> <dt>

[**MI\_ProviderArchitecture**](/windows/previous-versions/Mi/ne-mi-_mi_providerarchitecture?branch=master)
</dt> <dd>

This enumeration defines the WMI provider architecture used on the server.

</dd> <dt>

[**MI\_Result**](/windows/previous-versions/Mi/ne-mi-_mi_result?branch=master)
</dt> <dd>

Defines function return codes.

</dd> <dt>

[**MI\_SubscriptionDeliveryType**](/windows/previous-versions/Mi/ne-mi-_mi_subscriptiondeliverytype?branch=master)
</dt> <dd>

Differentiates between a push or pull subscription delivery type. This is not supported when using the DCOM protocol.

</dd> <dt>

[**MI\_Type**](/windows/previous-versions/Mi/ne-mi-_mi_type?branch=master)
</dt> <dd>

These values specify the data type of qualifiers, properties, references, parameters, and method return values for the CIM data types.

</dd> </dl>

 

 




