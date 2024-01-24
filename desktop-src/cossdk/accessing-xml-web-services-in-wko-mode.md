---
description: You can access and use any XML web service, even if that XML web service was not created using COM+ or even Microsoft Windows, as long as the XML Web Service publishes a WSDL description of its syntax.
ms.assetid: 5b21ff0c-f3a5-464b-b927-a7872ac54fe2
title: Accessing XML Web Services in WKO Mode
ms.topic: article
ms.date: 05/31/2018
---

# Accessing XML Web Services in WKO Mode

You can access and use any XML web service, even if that XML web service was not created using COM+ or even Microsoft Windows, as long as the XML Web Service publishes a WSDL description of its syntax. Just create an instance of the component by using the soap:wsdl=URL moniker, where URL is the URL of the WSDL description of the XML web service you want to access. This is the well-known object (WKO) mode of accessing XML web services.

The object's methods can be called without any special considerations. The XML web service is accessed via a SOAP query, and the response is interpreted transparently.

## Component Services Administrative Tool

Does not apply.

## Visual Basic

The following Microsoft Visual Basic code fragment illustrates the use of an XML web service in WKO mode.


```VB
Set Obj = GetObject("soap:wsdl=https://servername/vroot/progID.soap?WSDL")
output = Obj.Method(input)
```



In this code fragment, which illustrates the use of a component of a COM+ application that has been exposed as an XML web service, servername is the fully qualified domain name of the server offering the XML web service; vroot is the IIS virtual root directory from which the XML web service is exposed; and progID is the ProgID of the component you want to use.

## C/C++

The following code fragment illustrates the use of an XML web service in WKO mode.


```C++
HRESULT hr = CoGetObject(
     L"soap:wsdl=https://servername/vroot/progID.soap?WSDL",
     pBindOptions,
     IID_IUnknown,
     (void**)&pIUnknown);
if (FAILED(hr)) throw(hr); 
```



In this code fragment, which illustrates the use of a component of a COM+ application that has been exposed as an XML web service, servername is the fully qualified domain name of the server offering the XML web service; vroot is the IIS virtual root directory from which the XML web service is exposed; and progID is the ProgID of the component you want to use.

## Remarks

When an XML web service is first accessed in WKO mode, COM+ generates a proxy client and compiles it in the background. This run-time generation and the lack of persistent connections in WKO mode results in significantly reduced performance in comparison to CAO mode.

## Related topics

<dl> <dt>

[Accessing XML Web Services in CAO Mode](accessing-xml-web-services-in-cao-mode.md)
</dt> <dt>

[COM+ SOAP Service Overview](com--soap-service-overview.md)
</dt> <dt>

[Creating XML Web Services](creating-xml-web-services.md)
</dt> <dt>

[Securing XML Web Services](securing-xml-web-services.md)
</dt> </dl>

 

 



