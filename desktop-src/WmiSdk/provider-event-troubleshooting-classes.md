---
Description: The following table lists the classes for WMI provider event troubleshooting. Each class is associated with the WMI provider event to which it is coupled.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5acfc8f4-9b3b-4ff4-a8ed-7378334a8ddb
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: Provider Event Troubleshooting Classes
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Provider Event Troubleshooting Classes

The following table lists the classes for WMI provider event troubleshooting. Each class is associated with the WMI provider event to which it is coupled.



| Class                                                                                                                            | Description                                                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**MSFT\_WmiProvider\_AccessCheck\_Post**](https://msdn.microsoft.com/library/aa392545)                                      | Event class instance generated immediately following completion of the provider's implementation of [**IWbemEventProviderSecurity::AccessCheck**](/windows/desktop/api/Wbemprov/nf-wbemprov-iwbemeventprovidersecurity-accesscheck).   |
| [**MSFT\_WmiProvider\_AccessCheck\_Pre**](https://msdn.microsoft.com/library/aa392546)                                        | Event class instance generated immediately prior to calling the provider's implementation of [**IWbemEventProviderSecurity::AccessCheck**](/windows/desktop/api/Wbemprov/nf-wbemprov-iwbemeventprovidersecurity-accesscheck).          |
| [**MSFT\_WmiProvider\_CancelQuery\_Post**](https://msdn.microsoft.com/library/aa392547)                                      | Event class instance generated immediately following completion of the provider's implementation of [**IWbemEventProviderQuerySink::CancelQuery**](/windows/desktop/api/Wbemprov/nf-wbemprov-iwbemeventproviderquerysink-cancelquery). |
| [**MSFT\_WmiProvider\_CancelQuery\_Pre**](https://msdn.microsoft.com/library/aa392548)                                        | Event class instance generated immediately prior to calling the provider's implementation of [**IWbemEventProviderQuerySink::CancelQuery**](/windows/desktop/api/Wbemprov/nf-wbemprov-iwbemeventproviderquerysink-cancelquery).        |
| [**MSFT\_WmiProvider\_ComServerLoadOperationEvent**](https://msdn.microsoft.com/library/aa392549)                 | Event class instance generated for COM server instance activation.                                                                                                                               |
| [**MSFT\_WmiProvider\_ComServerLoadOperationFailureEvent**](https://msdn.microsoft.com/library/aa392550)   | Event class instance generated for COM server instance activation failure.                                                                                                                       |
| [**MSFT\_WmiProvider\_CreateClassEnumAsyncEvent\_Post**](https://msdn.microsoft.com/library/aa392552)          | Event class instance generated immediately following completion of the provider's implementation of [**IWbemServices::CreateClassEnumAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-createclassenumasync).           |
| [**MSFT\_WmiProvider\_CreateClassEnumAsyncEvent\_Pre**](https://msdn.microsoft.com/library/aa392553)            | Event class instance generated immediately prior to calling the provider's implementation of [**IWbemServices::CreateClassEnumAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-createclassenumasync).                  |
| [**MSFT\_WmiProvider\_CreateInstanceEnumAsyncEvent\_Post**](https://msdn.microsoft.com/library/aa392554)    | Event class instance generated immediately following completion of the provider's implementation of [**IWbemServices::CreateInstanceEnumAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-createinstanceenumasync).     |
| [**MSFT\_WmiProvider\_CreateInstanceEnumAsyncEvent\_Pre**](https://msdn.microsoft.com/library/aa392556)      | Event class instance generated immediately prior to calling the provider's implementation of [**IWbemServices::CreateInstanceEnumAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-createinstanceenumasync).            |
| [**MSFT\_WmiProvider\_DeleteClassAsyncEvent\_Post**](https://msdn.microsoft.com/library/aa392557)                  | Event class instance generated immediately following completion of the provider's implementation of [**IWbemServices::DeleteClassAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-deleteclassasync).                   |
| [**MSFT\_WmiProvider\_DeleteClassAsyncEvent\_Pre**](https://msdn.microsoft.com/library/aa392558)                    | Event class instance generated immediately prior to calling the provider's implementation of [**IWbemServices::DeleteClassAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-deleteclassasync).                          |
| [**MSFT\_WmiProvider\_DeleteInstanceAsyncEvent\_Post**](https://msdn.microsoft.com/library/aa392559)            | Event class instance generated immediately following completion of the provider's implementation of [**IWbemServices::DeleteInstanceAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-deleteinstanceasync).             |
| [**MSFT\_WmiProvider\_DeleteInstanceAsyncEvent\_Pre**](https://msdn.microsoft.com/library/aa392560)              | Event class instance generated immediately prior to calling the provider's implementation of [**IWbemServices::DeleteInstanceAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-deleteinstanceasync).                    |
| [**MSFT\_WmiProvider\_ExecMethodAsyncEvent\_Post**](https://msdn.microsoft.com/library/aa392561)                    | Event class instance generated immediately following completion of the provider's implementation of [**IWbemServices::ExecMethodAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-execmethodasync).                     |
| [**MSFT\_WmiProvider\_ExecMethodAsyncEvent\_Pre**](https://msdn.microsoft.com/library/aa392562)                      | Event class instance generated immediately prior to calling the provider's implementation of [**IWbemServices::ExecMethodAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-execmethodasync).                            |
| [**MSFT\_WmiProvider\_ExecQueryAsyncEvent\_Post**](https://msdn.microsoft.com/library/aa392563)                      | Event class instance generated immediately following completion of the provider's implementation of [**IWbemServices::ExecQueryAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-execqueryasync).                       |
| [**MSFT\_WmiProvider\_ExecQueryAsyncEvent\_Pre**](https://msdn.microsoft.com/library/aa392564)                        | Event class instance generated immediately prior to calling the provider's implementation of [**IWbemServices::ExecQueryAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-execqueryasync).                              |
| [**MSFT\_WmiProvider\_GetObjectAsyncEvent\_Post**](https://msdn.microsoft.com/library/aa392565)                      | Event class instance generated immediately following completion of the provider's implementation of [**IWbemServices::GetObjectAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-getobjectasync).                       |
| [**MSFT\_WmiProvider\_GetObjectAsyncEvent\_Pre**](https://msdn.microsoft.com/library/aa392566)                        | Event class instance generated immediately prior to calling the provider's implementation of [**IWbemServices::GetObjectAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-getobjectasync).                              |
| [**MSFT\_WmiProvider\_InitializationOperationEvent**](https://msdn.microsoft.com/library/aa392567)               | Event class instance generated for successful initialization of the provider server instance.                                                                                                    |
| [**MSFT\_WmiProvider\_InitializationOperationFailureEvent**](https://msdn.microsoft.com/library/aa392568) | Event class instance generated for failed initialization of the provider server instance.                                                                                                        |
| [**MSFT\_WmiProvider\_LoadOperationEvent**](https://msdn.microsoft.com/library/aa392569)                                   | Event class instance generated or successful activation and initialization of the provider cache entry.                                                                                          |
| [**MSFT\_WmiProvider\_LoadOperationFailureEvent**](https://msdn.microsoft.com/library/aa392570)                     | Event class instance generated for failed activation and initialization of the provider cache entry.                                                                                             |
| [**MSFT\_WmiProvider\_NewQuery\_Post**](https://msdn.microsoft.com/library/aa392571)                                            | Event class instance generated immediately following completion of the provider's implementation of [**IWbemEventProviderQuerySink::NewQuery**](/windows/desktop/api/Wbemprov/nf-wbemprov-iwbemeventproviderquerysink-newquery).       |
| [**MSFT\_WmiProvider\_NewQuery\_Pre**](https://msdn.microsoft.com/library/aa392572)                                              | Event class instance generated immediately prior to calling the provider's implementation of [**IWbemEventProviderQuerySink::NewQuery**](/windows/desktop/api/Wbemprov/nf-wbemprov-iwbemeventproviderquerysink-newquery).              |
| [**MSFT\_WmiProvider\_OperationEvent**](https://msdn.microsoft.com/library/aa392573)                                           | Base class for WMI provider troubleshooting event classes.                                                                                                                                       |
| [**MSFT\_WmiProvider\_OperationEvent\_Post**](https://msdn.microsoft.com/library/aa392577)                                | Base class for troubleshooting events following completion of provider implementation.                                                                                                           |
| [**MSFT\_WmiProvider\_OperationEvent\_Pre**](https://msdn.microsoft.com/library/aa392580)                                  | Base class for troubleshooting events prior to calling provider implementation.                                                                                                                  |
| [**MSFT\_WmiProvider\_ProvideEvents\_Post**](https://msdn.microsoft.com/library/aa392582)                                  | Event class instance generated immediately following completion of the provider's implementation of [**IWbemEventProvider::ProvideEvents**](/windows/desktop/api/Wbemprov/nf-wbemprov-iwbemeventprovider-provideevents).               |
| [**MSFT\_WmiProvider\_ProvideEvents\_Pre**](https://msdn.microsoft.com/library/aa392586)                                    | Event class instance generated immediately prior to calling the provider's implementation of [**IWbemEventProvider::ProvideEvents**](/windows/desktop/api/Wbemprov/nf-wbemprov-iwbemeventprovider-provideevents).                      |
| [**MSFT\_WmiProvider\_PutClassAsyncEvent\_Post**](https://msdn.microsoft.com/library/aa392588)                        | Event class instance generated immediately following completion of the provider's implementation of [**IWbemServices::PutClassAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-putclassasync).                         |
| [**MSFT\_WmiProvider\_PutClassAsyncEvent\_Pre**](https://msdn.microsoft.com/library/aa392590)                          | Event class instance generated immediately prior to calling the provider's implementation of [**IWbemServices::PutClassAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-putclassasync).                                |
| [**MSFT\_WmiProvider\_PutInstanceAsyncEvent\_Post**](https://msdn.microsoft.com/library/aa392595)                  | Event class instance generated immediately following completion of the provider's implementation of [**IWbemServices::PutInstanceAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-putinstanceasync).                   |
| [**MSFT\_WmiProvider\_PutInstanceAsyncEvent\_Pre**](https://msdn.microsoft.com/library/aa392598)                    | Event class instance generated immediately prior to calling the provider's implementation of [**IWbemServices::PutInstanceAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-putinstanceasync).                          |
| [**MSFT\_WmiProvider\_UnloadOperationEvent**](https://msdn.microsoft.com/library/aa392601)                               | Event class instance generated for removal of the provider cache entry.                                                                                                                          |



 

## Related topics

<dl> <dt>

[WMI Troubleshooting](wmi-troubleshooting.md)
</dt> <dt>

WMI Troubleshooting
</dt> <dt>

[Receiving a WMI Event](receiving-a-wmi-event.md)
</dt> </dl>

 

 



