---
description: HTTP revolutionized computer use by allowing people to use a Web browser for easy access to information on a remote server over a network.
ms.assetid: 44f3ff21-4978-4902-aa74-ddeef60881db
title: COM+ SOAP Service Overview
ms.topic: article
ms.date: 05/31/2018
---

# COM+ SOAP Service Overview

HTTP revolutionized computer use by allowing people to use a Web browser for easy access to information on a remote server over a network. XML web services have now revolutionized application development by allowing client applications to easily call remote methods over a network.

It is often useful for a client application to be able to call a method implemented on a remote server. Sometimes the method makes use of volatile information stored on the remote server (for example, a method that returns the current price of the stock corresponding to a given ticker symbol). At other times, the developer wants the ability to upgrade the methods implementation without having to redeploy all the applications that use it.

Like webpages, XML web services are accessed via a web server, such as IIS, using HTTP. However, instead of webpages encoded in HTML, these HTTP packets contain the input and output parameters of calls to a method implemented on the server, encoded in SOAP.

To use an XML web service, you need to know the URL where the service is exposed and the name of the method you want to call, and you must provide the input parameters to the method. [The SOAP 1.1 standard](https://www.w3.org/TR/SOAP/) provides the following example of an HTTP packet containing a remote call to an XML web service at https://www.stockquoteserver.com/StockQuote, which returns the current price of the stock corresponding to a given ticker symbol.

``` syntax
POST /StockQuote HTTP/1.1
Host: www.stockquoteserver.com
Content-Type: text/xml; "charset=utf-8"
Content-Length: nnnn
SOAPAction: "Some-URI"

<SOAP-ENV:Envelope
xmlns:SOAP-ENV="https://schemas.xmlsoap.org/soap/envelope/"
SOAP-ENV:encodingStyle="https://schemas.xmlsoap.org/soap/encoding/">
<SOAP-ENV:Body>
<m:GetLastTradePrice xmlns:m="Some-URI">
<symbol>DIS</symbol>
</m:GetLastTradePrice>
</SOAP-ENV:Body>
</SOAP-ENV:Envelope>
```

As the preceding example illustrates, SOAP is an XML instance that can be embedded in an HTTP request. Similarly, the result is returned as an HTTP packet with a SOAP payload, as shown in the following example.

``` syntax
HTTP/1.1 200 OK
Content-Type: text/xml; "charset=utf-8"
Content-Length: nnnn

<SOAP-ENV:Envelope
xmlns:SOAP-ENV="https://schemas.xmlsoap.org/soap/envelope/"
SOAP-ENV:encodingStyle="https://schemas.xmlsoap.org/soap/encoding//">
<SOAP-ENV:Body>
<m:GetLastTradePriceResponse xmlns:m="Some-URI">
<Price>34.5</Price>
</m:GetLastTradePriceResponse>
</SOAP-ENV:Body>
</SOAP-ENV:Envelope>
```

While it is helpful to have some understanding of the infrastructure that underlies XML web services, COM+ makes it so easy to create and use XML web services that you won't often have to delve to this level.

You can expose the methods in the default interfaces of the configured COM components in any COM+ application as an XML web service. No special programming considerations are necessary when writing the components, except that the methods you want to expose must be in the default interface and the component must be configured (in your server's COM+ catalog). You need not write code to communicate via a network interface or to parse SOAP. For detailed instructions about using the COM+ SOAP service to create an XML web service, see [Creating XML Web Services](creating-xml-web-services.md).

When you expose a COM+ application as an XML web service, detailed information about the syntax of all the methods available from an XML web service is published automatically, using the Web Services Description Language (WSDL). This information is used by clients that use your XML web service.

COM+ provides two ways for you to access and use a remote XML web service, as follows:

-   The *well-known object* (WKO) mode can be used to access any XML web service that publishes its syntax using WSDL, even if that XML web service was not created using COM+ or even Microsoft Windows.
-   The *client-activated object* (CAO) mode can be used only to access XML web services created by exposing COM+ applications. CAO mode increases performance by using persistent connections, a feature not supported by the current SOAP standard.

Both methods allow client applications to call the methods of XML web services remotely in a straightforward fashion, without having to write code to communicate via a network interface or parse SOAP. For details about how to access XML web services in either mode, see [Accessing XML Web Services in CAO Mode](accessing-xml-web-services-in-cao-mode.md) and [Accessing XML Web Services in WKO Mode](accessing-xml-web-services-in-wko-mode.md).

> [!Note]  
> COM+ supports only the SOAP-RPC specification, not the SOAP-Document specification.

 

COM+ makes using XML web services especially easy by allowing you to use existing COM+ applications as XML web services in CAO mode in a completely transparent fashion. If you [export](exporting-a-soap-enabled-application.md) a COM+ application that has been exposed as an XML web service from your server, any client that [imports](importing-a-soap-enabled-application.md) the application can transparently use the server's XML web service whenever the imported application is used. This facility makes the conversion of existing COM+ applications to XML web services and the deployment of those services over a network very easy.

Using XML web services has several unique advantages over alternative implementations of remote procedure calls (RPC), including the following:

-   SOAP is a true cross-platform RPC implementation, which increases interoperability.
-   XML web services support methods with both input and output parameters.
-   XML web services run over HTTP, which can usually penetrate firewalls that might block other RPC implementations.
-   When an XML web service is implemented using COM+, the developer does not have to write any specialized code; this is a tremendous advantage over alternative RPC mechanisms.

> [!Note]  
> XML web services do not support asynchronous or transparently transactional calls. Use the [COM+ Queued Components](com--queued-components.md) service when you require this functionality.

 

## Related topics

<dl> <dt>

[COM+ SOAP Service Security Considerations](com--soap-service-security-considerations.md)
</dt> </dl>

 

 



