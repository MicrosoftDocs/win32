---
Description: Configuring COM+ Services with CServiceConfig
ms.assetid: c44743a8-8b91-4e2a-9ba4-4cb6ae787999
title: Configuring COM+ Services with CServiceConfig
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Configuring COM+ Services with CServiceConfig

The [**CServiceConfig**](/windows/win32/ComSvcs/?branch=master) class is used to configure the COM+ services that can be used without components. It aggregates the free-threaded marshaler, so it can be used in different apartments. To configure an individual service, you must call [**QueryInterface**](https://msdn.microsoft.com/library/windows/desktop/ms682521) for the interface associated with the service and then call methods on that interface to establish the appropriate configuration. The following table describes the interfaces that are implemented through the **CServiceConfig** class.



| Interface                                                                         | Description                                                                                                                                                                                              |
|-----------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IServiceInheritanceConfig**](/windows/win32/ComSvcs/nn-comsvcs-iserviceinheritanceconfig?branch=master)<br/>         | The default interface for the class. It is used to quickly initialize many of the COM+ services.<br/>                                                                                              |
| [**IServiceComTIIntrinsicsConfig**](/windows/win32/ComSvcs/nn-comsvcs-iservicecomtiintrinsicsconfig?branch=master)<br/> | Used to configure the COM Transaction Integrator (COMTI) intrinsics information. COMTI allows developers to integrate mainframe-based transaction programs with component-based applications.<br/> |
| [**IServiceIISIntrinsicsConfig**](/windows/win32/ComSvcs/nn-comsvcs-iserviceiisintrinsicsconfig?branch=master)<br/>     | Used to configure the Internet Information Services (IIS) intrinsics information.<br/>                                                                                                             |
| [**IServicePartitionConfig**](/windows/win32/ComSvcs/nn-comsvcs-iservicepartitionconfig?branch=master)<br/>             | Used to configure how COM+ partitions are used with the services.<br/>                                                                                                                             |
| [**IServiceSxSConfig**](/windows/win32/ComSvcs/nn-comsvcs-iservicesxsconfig?branch=master)<br/>                         | Used to configure side-by-side assemblies.<br/>                                                                                                                                                    |
| [**IServiceSynchronizationConfig**](/windows/win32/ComSvcs/nn-comsvcs-iservicesynchronizationconfig?branch=master)<br/> | Used to configure COM+ synchronization services.<br/>                                                                                                                                              |
| [**IServiceThreadPoolConfig**](/windows/win32/ComSvcs/nn-comsvcs-iservicethreadpoolconfig?branch=master)<br/>           | Used to configure the thread pool for the COM+ service. The thread pool can be configured only when using the [**CoCreateActivity**](/windows/win32/ComSvcs/nf-comsvcs-cocreateactivity?branch=master) function.<br/>                          |
| [**IServiceTrackerConfig**](/windows/win32/ComSvcs/nn-comsvcs-iservicetrackerconfig?branch=master)<br/>                 | Used to configure the Tracker property. Tracker is a reporting mechanism used by monitoring code to watch which code is running when.<br/>                                                         |
| [**IServiceTransactionConfig**](/windows/win32/ComSvcs/nn-comsvcs-iservicetransactionconfig?branch=master)<br/>         | Used to configure the COM+ transaction service.<br/>                                                                                                                                               |



 

## Component Services Administrative Tool

Does not apply.

## Visual Basic

Does not apply.

## C/C++

The following code fragment illustrates how to create and configure a [**CServiceConfig**](/windows/win32/ComSvcs/?branch=master) object to use COM+ transactions.


```C++
// Create a CServiceConfig object.
HRESULT hr = CoCreateInstance(CLSID_CServiceConfig, NULL, CLSCTX_INPROC_SERVER, 
  IID_IUnknown, (void**)&amp;pUnknownCSC);
if (FAILED(hr)) throw(hr);

// Query for the IServiceInheritanceConfig interface.
hr = pUnknownCSC->QueryInterface(IID_IServiceInheritanceConfig, 
  (void**)&amp;pInheritanceConfig);
if (FAILED(hr)) throw(hr);

// Inherit the current context before using transactions.
hr = pInheritanceConfig->ContainingContextTreatment(CSC_Inherit);
if (FAILED(hr)) throw(hr);

// Query for the IServiceTransactionConfig interface.
hr = pUnknownCSC->QueryInterface(IID_IServiceTransactionConfig, 
  (void**)&amp;pTransactionConfig);
if (FAILED(hr)) throw(hr);

// Configure transactions to always create a new one.
hr = pTransactionConfig->ConfigureTransaction(CSC_NewTransaction);
if (FAILED(hr)) throw(hr);

// Set the isolation level of the transactions to ReadCommitted.
hr = pTransactionConfig->IsolationLevel( 
  COMAdminTxIsolationLevelReadCommitted);
if (FAILED(hr)) throw(hr);

// Set the transaction time-out to 1 minute.
hr = pTransactionConfig->TransactionTimeout(60);
if (FAILED(hr)) throw(hr);

```



## Related topics

<dl> <dt>

[**CServiceConfig**](/windows/win32/ComSvcs/?branch=master)
</dt> <dt>

[Using COM+ Services Through CoCreateActivity](using-com--services-through-cocreateactivity.md)
</dt> <dt>

[Using COM+ Services Through CoEnterServiceDomain and CoLeaveServiceDomain](using-com--services-through-coenterservicedomain-and-coleaveservicedomain.md)
</dt> </dl>

 

 




