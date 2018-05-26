---
Description: Using COM+ Services Through CoEnterServiceDomain and CoLeaveServiceDomain
ms.assetid: 763fb01e-5daf-4e9b-8ef1-9ae79c0a84cc
title: Using COM+ Services Through CoEnterServiceDomain and CoLeaveServiceDomain
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using COM+ Services Through CoEnterServiceDomain and CoLeaveServiceDomain

[**CoEnterServiceDomain**](/windows/win32/ComSvcs/nf-comsvcs-coenterservicedomain?branch=master) and [**CoLeaveServiceDomain**](/windows/win32/ComSvcs/nf-comsvcs-coleaveservicedomain?branch=master) are used together to surround an area of code that runs in its own context and can use COM+ services without the need for COM+ components. The COM+ services that are used in this context are configured through the [**CServiceConfig**](/windows/win32/ComSvcs/?branch=master) object that is passed in to **CoEnterServiceDomain**. The code that is surrounded by **CoEnterServiceDomain** and **CoLeaveServiceDomain** behaves as though it were a method that is called on an object created within this context.

A scripting application can use this pair of functions to provide run-time support of COM+ services without components. For example, a scripting application can be developed to provide tags that allow the script writers to enter and leave a service domain within the script. When the scripting engine processes the script and encounters the tags, it can call [**CoEnterServiceDomain**](/windows/win32/ComSvcs/nf-comsvcs-coenterservicedomain?branch=master) with a preconfigured [**CServiceConfig**](/windows/win32/ComSvcs/?branch=master) object, run the necessary code, and then call [**CoLeaveServiceDomain**](/windows/win32/ComSvcs/nf-comsvcs-coleaveservicedomain?branch=master).

## Component Services Administrative Tool

Does not apply.

## Visual Basic

Does not apply.

## C/C++

The following code fragment illustrates how to use COM+ services between calls to [**CoEnterServiceDomain**](/windows/win32/ComSvcs/nf-comsvcs-coenterservicedomain?branch=master) and [**CoLeaveServiceDomain**](/windows/win32/ComSvcs/nf-comsvcs-coleaveservicedomain?branch=master). Error handling is omitted for brevity. This code fragment uses the [**CServiceConfig**](/windows/win32/ComSvcs/?branch=master) object that was created and configured in [Configuring COM+ Services with CServiceConfig](configuring-com--services-with-cserviceconfig.md).


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

[**CoEnterServiceDomain**](/windows/win32/ComSvcs/nf-comsvcs-coenterservicedomain?branch=master)
</dt> <dt>

[**CoLeaveServiceDomain**](/windows/win32/ComSvcs/nf-comsvcs-coleaveservicedomain?branch=master)
</dt> <dt>

[Configuring COM+ Services with CServiceConfig](configuring-com--services-with-cserviceconfig.md)
</dt> <dt>

[**CServiceConfig**](/windows/win32/ComSvcs/?branch=master)
</dt> <dt>

[Using COM+ Services Through CoCreateActivity](using-com--services-through-cocreateactivity.md)
</dt> </dl>

 

 



