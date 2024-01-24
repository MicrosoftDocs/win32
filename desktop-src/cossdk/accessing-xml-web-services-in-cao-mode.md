---
description: If the XML web service you want to access was created by exposing a COM+ application, consider accessing it in client-activated object (CAO) mode, which avoids the run-time generation of a proxy and increases performance by using persistent connections.
ms.assetid: 471de0fa-3429-45f8-abe2-aff0cf6fb350
title: Accessing XML Web Services in CAO Mode
ms.topic: article
ms.date: 05/31/2018
---

# Accessing XML Web Services in CAO Mode

If the XML web service you want to access was created by exposing a COM+ application, consider accessing it in client-activated object (CAO) mode, which avoids the run-time generation of a proxy and increases performance by using persistent connections. To access an XML web service in CAO mode, first [export](exporting-a-soap-enabled-application.md) the corresponding SOAP-enabled application from your server in proxy mode and then [import](importing-a-soap-enabled-application.md) the application into the client from which you want to access the application as an XML web service. The application's components can then be instantiated on the client just like the components of local applications—for example, using **GetObject** and [**CoCreateInstance**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstance).

## User Interface

Does not apply.

## Visual Basic

The following Visual Basic code fragment illustrates the use of a component of a COM+ application that has been exposed as an XML web service in CAO mode.


```VB
Set Obj = GetObject("progID")
output = Obj.Method(input)
```



## C/C++

The following code fragment illustrates the use of a component of a COM+ application that has been exposed as an XML web service in CAO mode.


```C++
HRESULT hr = CoCreateInstance(
     CLSID_CObject,  // CLSID of the server component
     NULL,
     pBindOptions,
     IID_IUnknown,
     (void**)&pIUnknown);
if (FAILED(hr)) throw(hr);
```



## Related topics

<dl> <dt>

[Accessing XML Web Services in WKO Mode](accessing-xml-web-services-in-wko-mode.md)
</dt> <dt>

[COM+ SOAP Service Overview](com--soap-service-overview.md)
</dt> <dt>

[Creating XML Web Services](creating-xml-web-services.md)
</dt> <dt>

[Securing XML Web Services](securing-xml-web-services.md)
</dt> </dl>

 

 
