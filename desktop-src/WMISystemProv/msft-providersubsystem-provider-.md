---
title: Msft\_ProviderSubSystem Provider
description: The Msft\_ProviderSubSystem provider supports WMI providers.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: A320D703-2538-4769-B117-C89F773A7D28
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Msft\_ProviderSubSystem Provider

This provider supports WMI Self-Instrumentation.

## In this section

<dl> <dt>

[**MSFT\_Providers**](msft-providers.md)
</dt> <dd>

The [**MSFT\_Providers**](msft-providers.md) class contains configuration information for providers.

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

</dd> <dt>

[**MSFT\_WmiCancelNotificationSink**](msft-wmicancelnotificationsink.md)
</dt> <dd>

Generated when an event sink is canceled.

</dd> <dt>

[**MSFT\_WmiConsumerProviderEvent**](msft-wmiconsumerproviderevent.md)
</dt> <dd>

The parent class for all consumer provider events.

</dd> <dt>

[**MSFT\_WmiConsumerProviderLoaded**](msft-wmiconsumerproviderloaded.md)
</dt> <dd>

Defines the successful activation of the event consumer provider COM object.

</dd> <dt>

[**MSFT\_WmiConsumerProviderSinkLoaded**](msft-wmiconsumerprovidersinkloaded.md)
</dt> <dd>

Defines the successful activation of the event consumer provider sink object.

</dd> <dt>

[**MSFT\_WmiConsumerProviderSinkUnloaded**](msft-wmiconsumerprovidersinkunloaded.md)
</dt> <dd>

Defines the successful deactivation of the event consumer provider sink object.

</dd> <dt>

[**MSFT\_WmiConsumerProviderUnloaded**](msft-wmiconsumerproviderunloaded.md)
</dt> <dd>

Defines the successful deactivation of the event consumer provider COM object.

</dd> <dt>

[**MSFT\_WmiEssEvent**](msft-wmiessevent.md)
</dt> <dd>

The parent class for all WMI Eventing SubSystem (ESS) self events.

</dd> <dt>

[**MSFT\_WmiFilterActivated**](msft-wmifilteractivated.md)
</dt> <dd>

Defines the successful activation of a permanent event consumer subscription filter.

</dd> <dt>

[**MSFT\_WmiFilterDeactivated**](msft-wmifilterdeactivated.md)
</dt> <dd>

Defines the successful deactivation of a permanent consumer subscription filter.

</dd> <dt>

[**MSFT\_WmiFilterEvent**](msft-wmifilterevent.md)
</dt> <dd>

The parent class for all permanent event consumer filter events.

</dd> <dt>

[**MSFT\_WmiProvider\_AccessCheck\_Post**](msft-wmiprovider-accesscheck-post.md)
</dt> <dd>

Represents an event generated immediately following completion of the provider's implementation of [**IWbemEventProviderSecurity::AccessCheck**](https://msdn.microsoft.com/library/aa391743).

</dd> <dt>

[**MSFT\_WmiProvider\_AccessCheck\_Pre**](msft-wmiprovider-accesscheck-pre.md)
</dt> <dd>

Represents an event generated immediately prior to calling the provider's implementation of [**IWbemEventProviderSecurity::AccessCheck**](https://msdn.microsoft.com/library/aa391743).

</dd> <dt>

[**MSFT\_WmiProvider\_CancelQuery\_Post**](msft-wmiprovider-cancelquery-post.md)
</dt> <dd>

Represents an event generated immediately following completion of the provider's implementation of [**IWbemEventProviderQuerySink::CancelQuery**](https://msdn.microsoft.com/library/aa391738).

</dd> <dt>

[**MSFT\_WmiProvider\_CancelQuery\_Pre**](msft-wmiprovider-cancelquery-pre.md)
</dt> <dd>

Represents an event generated immediately prior to calling the provider's implementation of [**IWbemEventProviderQuerySink::CancelQuery**](https://msdn.microsoft.com/library/aa391738).

</dd> <dt>

[**MSFT\_WmiProvider\_ComServerLoadOperationEvent**](msft-wmiprovider-comserverloadoperationevent.md)
</dt> <dd>

Defines the successful activation of a COM server instance associated with the provider registration.

</dd> <dt>

[**MSFT\_WmiProvider\_ComServerLoadOperationFailureEvent**](msft-wmiprovider-comserverloadoperationfailureevent.md)
</dt> <dd>

Defines the unsuccessful activation of a COM server instance associated with the provider registration.

</dd> <dt>

[**Msft\_WmiProvider\_Counters**](msft-wmiprovider-counters.md)
</dt> <dd>

Exposes approximate counts of WMI internal operation calls across all providers.

</dd> <dt>

[**MSFT\_WmiProvider\_CreateClassEnumAsyncEvent\_Post**](msft-wmiprovider-createclassenumasyncevent-post.md)
</dt> <dd>

Represents an event generated immediately following completion of the provider's implementation of [**IWbemServices::CreateClassEnumAsync**](https://msdn.microsoft.com/library/aa392096).

</dd> <dt>

[**MSFT\_WmiProvider\_CreateClassEnumAsyncEvent\_Pre**](msft-wmiprovider-createclassenumasyncevent-pre.md)
</dt> <dd>

Represents an event generated immediately prior to calling the provider's implementation of [**IWbemServices::CreateClassEnumAsync**](https://msdn.microsoft.com/library/aa392096).

</dd> <dt>

[**MSFT\_WmiProvider\_CreateInstanceEnumAsyncEvent\_Post**](msft-wmiprovider-createinstanceenumasyncevent-post.md)
</dt> <dd>

Represents an event generated immediately following completion of the provider's implementation of [**IWbemServices::CreateInstanceEnumAsync**](https://msdn.microsoft.com/library/aa392098).

</dd> <dt>

[**MSFT\_WmiProvider\_CreateInstanceEnumAsyncEvent\_Pre**](msft-wmiprovider-createinstanceenumasyncevent-pre.md)
</dt> <dd>

Represents an event generated immediately prior to calling the provider's implementation of [**IWbemServices::CreateInstanceEnumAsync**](https://msdn.microsoft.com/library/aa392098).

</dd> <dt>

[**MSFT\_WmiProvider\_DeleteClassAsyncEvent\_Post**](msft-wmiprovider-deleteclassasyncevent-post.md)
</dt> <dd>

Represents an event generated immediately following completion of the provider's implementation of [**IWbemServices::DeleteClassAsync**](https://msdn.microsoft.com/library/aa392100)

</dd> <dt>

[**MSFT\_WmiProvider\_DeleteClassAsyncEvent\_Pre**](msft-wmiprovider-deleteclassasyncevent-pre.md)
</dt> <dd>

Represents an event generated immediately prior to calling the provider's implementation of [**IWbemServices::DeleteClassAsync**](https://msdn.microsoft.com/library/aa392100).

</dd> <dt>

[**MSFT\_WmiProvider\_DeleteInstanceAsyncEvent\_Post**](msft-wmiprovider-deleteinstanceasyncevent-post.md)
</dt> <dd>

Represents an event generated immediately following completion of the provider's implementation of [**IWbemServices::DeleteInstanceAsync**](https://msdn.microsoft.com/library/aa392102).

</dd> <dt>

[**MSFT\_WmiProvider\_DeleteInstanceAsyncEvent\_Pre**](msft-wmiprovider-deleteinstanceasyncevent-pre.md)
</dt> <dd>

Represents an event generated immediately prior to calling the provider's implementation of [**IWbemServices::DeleteInstanceAsync**](https://msdn.microsoft.com/library/aa392102).

</dd> <dt>

[**MSFT\_WmiProvider\_ExecMethodAsyncEvent\_Post**](msft-wmiprovider-execmethodasyncevent-post.md)
</dt> <dd>

represents an event generated immediately following completion of the provider's implementation of [**IWbemServices::ExecMethodAsync**](https://msdn.microsoft.com/library/aa392104).

</dd> <dt>

[**MSFT\_WmiProvider\_ExecMethodAsyncEvent\_Pre**](msft-wmiprovider-execmethodasyncevent-pre.md)
</dt> <dd>

Represents an event generated immediately prior to calling the provider's implementation of [**IWbemServices::ExecMethodAsync**](https://msdn.microsoft.com/library/aa392104).

</dd> <dt>

[**MSFT\_WmiProvider\_ExecQueryAsyncEvent\_Post**](msft-wmiprovider-execqueryasyncevent-post.md)
</dt> <dd>

Represents an event generated immediately following completion of the provider's implementation of [**IWbemServices::ExecQueryAsync**](https://msdn.microsoft.com/library/aa392108).

</dd> <dt>

[**MSFT\_WmiProvider\_ExecQueryAsyncEvent\_Pre**](msft-wmiprovider-execqueryasyncevent-pre.md)
</dt> <dd>

Represents an event generated immediately prior to calling the provider's implementation of [**IWbemServices::ExecQueryAsync**](https://msdn.microsoft.com/library/aa392108).

</dd> <dt>

[**MSFT\_WmiProvider\_GetObjectAsyncEvent\_Post**](msft-wmiprovider-getobjectasyncevent-post.md)
</dt> <dd>

Represents an event generated immediately following completion of the provider's implementation of [**IWbemServices::GetObjectAsync**](https://msdn.microsoft.com/library/aa392110).

</dd> <dt>

[**MSFT\_WmiProvider\_GetObjectAsyncEvent\_Pre**](msft-wmiprovider-getobjectasyncevent-pre.md)
</dt> <dd>

Represents an event generated immediately preceding the provider's implementation of [**IWbemServices::GetObjectAsync**](https://msdn.microsoft.com/library/aa392110).

</dd> <dt>

[**MSFT\_WmiProvider\_InitializationOperationEvent**](msft-wmiprovider-initializationoperationevent.md)
</dt> <dd>

Defines the successful initialization of the provider server instance.

</dd> <dt>

[**MSFT\_WmiProvider\_InitializationOperationFailureEvent**](msft-wmiprovider-initializationoperationfailureevent.md)
</dt> <dd>

Defines the unsuccessful initialization of the provider server instance.

</dd> <dt>

[**MSFT\_WmiProvider\_LoadOperationEvent**](msft-wmiprovider-loadoperationevent.md)
</dt> <dd>

Defines the successful activation and initialization of the provider cache entry.

</dd> <dt>

[**MSFT\_WmiProvider\_LoadOperationFailureEvent**](msft-wmiprovider-loadoperationfailureevent.md)
</dt> <dd>

Defines the unsuccessful activation and initialization of the provider cache entry.

</dd> <dt>

[**MSFT\_WmiProvider\_NewQuery\_Post**](msft-wmiprovider-newquery-post.md)
</dt> <dd>

Represents an event generated immediately following completion of the provider's implementation of [**IWbemEventProviderQuerySink::NewQuery**](https://msdn.microsoft.com/library/aa391739).

</dd> <dt>

[**MSFT\_WmiProvider\_NewQuery\_Pre**](msft-wmiprovider-newquery-pre.md)
</dt> <dd>

Represents an event generated immediately prior to calling the provider's implementation of [**IWbemEventProviderQuerySink::NewQuery**](https://msdn.microsoft.com/library/aa391739).

</dd> <dt>

[**MSFT\_WmiProvider\_OperationEvent**](msft-wmiprovider-operationevent.md)
</dt> <dd>

Contains the root definition of all WMI provider events.

</dd> <dt>

[**MSFT\_WmiProvider\_OperationEvent\_Post**](msft-wmiprovider-operationevent-post.md)
</dt> <dd>

Contains the operation event generated following completion of provider implementation.

</dd> <dt>

[**MSFT\_WmiProvider\_OperationEvent\_Pre**](msft-wmiprovider-operationevent-pre.md)
</dt> <dd>

Contains the operation event generated prior to calling provider implementation.

</dd> <dt>

[**MSFT\_WmiProvider\_ProvideEvents\_Post**](msft-wmiprovider-provideevents-post.md)
</dt> <dd>

Represents an event generated immediately following completion of the provider's implementation of [**IWbemEventProvider::ProvideEvents**](https://msdn.microsoft.com/library/aa391744).

</dd> <dt>

[**MSFT\_WmiProvider\_ProvideEvents\_Pre**](msft-wmiprovider-provideevents-pre.md)
</dt> <dd>

Represents an event generated immediately prior to calling the provider's implementation of [**IWbemEventProvider::ProvideEvents**](https://msdn.microsoft.com/library/aa391744).

</dd> <dt>

[**MSFT\_WmiProvider\_PutClassAsyncEvent\_Post**](msft-wmiprovider-putclassasyncevent-post.md)
</dt> <dd>

Represents an event generated immediately following completion of the provider's implementation of [**IWbemServices::PutClassAsync**](https://msdn.microsoft.com/library/aa392114).

</dd> <dt>

[**MSFT\_WmiProvider\_PutClassAsyncEvent\_Pre**](msft-wmiprovider-putclassasyncevent-pre.md)
</dt> <dd>

Represents an event generated immediately prior to calling the provider's implementation of [**IWbemServices::PutClassAsync**](https://msdn.microsoft.com/library/aa392114).

</dd> <dt>

[**MSFT\_WmiProvider\_PutInstanceAsyncEvent\_Post**](msft-wmiprovider-putinstanceasyncevent-post.md)
</dt> <dd>

Represents an event generated immediately following completion of the provider's implementation of [**IWbemServices::PutInstanceAsync**](https://msdn.microsoft.com/library/aa392116).

</dd> <dt>

[**MSFT\_WmiProvider\_PutInstanceAsyncEvent\_Pre**](msft-wmiprovider-putinstanceasyncevent-pre.md)
</dt> <dd>

Represents an event generated immediately prior to calling the provider's implementation of [**IWbemServices::PutInstanceAsync**](https://msdn.microsoft.com/library/aa392116).

</dd> <dt>

[**MSFT\_WmiProvider\_UnloadOperationEvent**](msft-wmiprovider-unloadoperationevent.md)
</dt> <dd>

Defines the removal of the provider cache entry.

</dd> <dt>

[**MSFT\_WmiProviderEvent**](msft-wmiproviderevent.md)
</dt> <dd>

The parent class for all consumer provider events.

</dd> <dt>

[**MSFT\_WmiRegisterNotificationEvent**](msft-wmiregisternotificationevent.md)
</dt> <dd>

Represents the creation of an event sink for notification for an event query.

</dd> <dt>

[**MSFT\_WmiRegisterNotificationSink**](msft-wmiregisternotificationsink.md)
</dt> <dd>

TBD

</dd> <dt>

[**MSFT\_WmiThreadPoolThreadCreated**](msft-wmithreadpoolthreadcreated.md)
</dt> <dd>

TBD

</dd> <dt>

[**MSFT\_WmiThreadPoolThreadDeleted**](msft-wmithreadpoolthreaddeleted.md)
</dt> <dd>

TBD

</dd> <dt>

[**MSFT\_WmiSelfEvent**](msft-wmiselfevent.md)
</dt> <dd>

Represents events occurring in the WMI service itself.

</dd> <dt>

[**MSFT\_WmiThreadPoolCreated**](msft-wmithreadpoolcreated.md)
</dt> <dd>

Provides notification when a thread is created in the WMI Event SubSystem (ESS).

</dd> <dt>

[**MSFT\_WmiThreadPoolDeleted**](msft-wmithreadpooldeleted.md)
</dt> <dd>

Provides notification when a thread is deleted in the WMI Event SubSystem (ESS).

</dd> <dt>

[**MSFT\_WmiThreadPoolEvent**](msft-wmithreadpoolevent.md)
</dt> <dd>

Provides notification of thread events in the WMI Event SubSystem (ESS).

</dd> </dl>

 

 




