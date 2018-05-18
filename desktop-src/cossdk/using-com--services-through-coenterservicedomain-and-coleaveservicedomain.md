---
Description: Using COM+ Services Through CoEnterServiceDomain and CoLeaveServiceDomain
ms.assetid: '763fb01e-5daf-4e9b-8ef1-9ae79c0a84cc'
title: Using COM+ Services Through CoEnterServiceDomain and CoLeaveServiceDomain
---

# Using COM+ Services Through CoEnterServiceDomain and CoLeaveServiceDomain

[**CoEnterServiceDomain**](coenterservicedomain.md) and [**CoLeaveServiceDomain**](coleaveservicedomain.md) are used together to surround an area of code that runs in its own context and can use COM+ services without the need for COM+ components. The COM+ services that are used in this context are configured through the [**CServiceConfig**](cserviceconfig.md) object that is passed in to **CoEnterServiceDomain**. The code that is surrounded by **CoEnterServiceDomain** and **CoLeaveServiceDomain** behaves as though it were a method that is called on an object created within this context.

A scripting application can use this pair of functions to provide run-time support of COM+ services without components. For example, a scripting application can be developed to provide tags that allow the script writers to enter and leave a service domain within the script. When the scripting engine processes the script and encounters the tags, it can call [**CoEnterServiceDomain**](coenterservicedomain.md) with a preconfigured [**CServiceConfig**](cserviceconfig.md) object, run the necessary code, and then call [**CoLeaveServiceDomain**](coleaveservicedomain.md).

## Component Services Administrative Tool

Does not apply.

## Visual Basic

Does not apply.

## C/C++

The following code fragment illustrates how to use COM+ services between calls to [**CoEnterServiceDomain**](coenterservicedomain.md) and [**CoLeaveServiceDomain**](coleaveservicedomain.md). Error handling is omitted for brevity. This code fragment uses the [**CServiceConfig**](cserviceconfig.md) object that was created and configured in [Configuring COM+ Services with CServiceConfig](configuring-com--services-with-cserviceconfig.md).


```C++
// A CServiceConfig object was created as follows:
// hr = CoCreateInstance(CLSID_CServiceConfig, NULL, CLSCTX_INPROC_SERVER, 
//   IID_IUnknown, (void**)&amp;pUnknownCSC);

// Enter the Service Domain.
HRESULT hr = CoEnterServiceDomain(pUnknownCSC);
if (FAILED(hr)) throw(hr);

// Do the work that uses COM+ services here.
//DoMyWork();

// Leave the Service Domain.
CoLeaveServiceDomain(NULL);
```



## Related topics

<dl> <dt>

[**CoEnterServiceDomain**](coenterservicedomain.md)
</dt> <dt>

[**CoLeaveServiceDomain**](coleaveservicedomain.md)
</dt> <dt>

[Configuring COM+ Services with CServiceConfig](configuring-com--services-with-cserviceconfig.md)
</dt> <dt>

[**CServiceConfig**](cserviceconfig.md)
</dt> <dt>

[Using COM+ Services Through CoCreateActivity](using-com--services-through-cocreateactivity.md)
</dt> </dl>

 

 



