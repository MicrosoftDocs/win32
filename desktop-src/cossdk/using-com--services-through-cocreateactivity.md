---
description: The CoCreateActivity function is used to submit batch work to the COM+ system. It allows script-based applications to support an application-wide COM+ service configuration.
ms.assetid: af734507-516c-43f1-9c5e-c77cde1b8008
title: Using COM+ Services Through CoCreateActivity
ms.topic: article
ms.date: 05/31/2018
---

# Using COM+ Services Through CoCreateActivity

The [**CoCreateActivity**](/windows/desktop/api/ComSvcs/nf-comsvcs-cocreateactivity) function is used to submit batch work to the COM+ system. It allows script-based applications to support an application-wide COM+ service configuration.

The desired COM+ services are configured through a [**CServiceConfig**](cserviceconfig.md) object that is passed in to the function. The function creates an activity object and returns the [**IServiceActivity**](/windows/desktop/api/ComSvcs/nn-comsvcs-iserviceactivity) interface of that object. The batch work can be submitted either synchronously or asynchronously, by using the [**SynchronousCall**](/windows/desktop/api/ComSvcs/nf-comsvcs-iserviceactivity-synchronouscall) or [**AsynchronousCall**](/windows/desktop/api/ComSvcs/nf-comsvcs-iserviceactivity-asynchronouscall) methods of **IServiceActivity**, respectively. A pointer to an [**IServiceCall**](/windows/desktop/api/ComSvcs/nn-comsvcs-iservicecall) interface is passed in to each of these methods, and the batch work is implemented by the developer in the [**OnCall**](/windows/desktop/api/ComSvcs/nf-comsvcs-iservicecall-oncall) method of the **IServiceCall** interface.

## Component Services Administrative Tool

Does not apply.

## Visual Basic

Does not apply.

## C/C++

The following code fragment illustrates how to use COM+ services through [**CoCreateActivity**](/windows/desktop/api/ComSvcs/nf-comsvcs-cocreateactivity). Error handling is omitted for brevity. This code fragment uses the [**CServiceConfig**](cserviceconfig.md) object that was created and configured in [Configuring COM+ Services with CServiceConfig](configuring-com--services-with-cserviceconfig.md).


```C++
// A CServiceConfig object was created as follows:
// hr = CoCreateInstance(CLSID_CServiceConfig, NULL, CLSCTX_INPROC_SERVER,
//   IID_IUnknown, (void**)&pUnknownCSC);

// Create the activity for our services.
HRESULT hr = CoCreateActivity(pUnknownCSC, IID_IServiceActivity, (void**)&pActivity);
if (FAILED(hr)) throw(hr);

// Do the batch work synchronously.
// The batch work is implemented in pServiceCall->OnCall().
hr = pActivity->SynchronousCall(pServiceCall);
if (FAILED(hr)) throw(hr);

```



## Related topics

<dl> <dt>

[**CoCreateActivity**](/windows/desktop/api/ComSvcs/nf-comsvcs-cocreateactivity)
</dt> <dt>

[Configuring COM+ Services with CServiceConfig](configuring-com--services-with-cserviceconfig.md)
</dt> <dt>

[**CServiceConfig**](cserviceconfig.md)
</dt> <dt>

[Using COM+ Services Through CoEnterServiceDomain and CoLeaveServiceDomain](using-com--services-through-coenterservicedomain-and-coleaveservicedomain.md)
</dt> </dl>

 

 



