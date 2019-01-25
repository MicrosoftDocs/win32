---
title: Creating the ServiceInfo Document Dynamically
description: Creating the ServiceInfo Document Dynamically
ms.assetid: 96937b04-f705-49f6-8ddf-25c98a51dc9a
keywords:
- Windows Media Player online stores,creating ServiceInfo document
- online stores,creating ServiceInfo document
- type 1 online stores,creating ServiceInfo document
- type 2 online stores,creating ServiceInfo document
- Windows Media Player online stores,dynamically creating ServiceInfo document
- online stores,dynamically creating ServiceInfo document
- type 1 online stores,dynamically creating ServiceInfo document
- type 2 online stores,dynamically creating ServiceInfo document
- Windows Media Player online stores,ServiceInfo document
- online stores,ServiceInfo document
- type 1 online stores,ServiceInfo document
- type 2 online stores,ServiceInfo document
- dynamically creating ServiceInfo document
- creating ServiceInfo document
- ServiceInfo document
ms.topic: article
ms.date: 05/31/2018
---

# Creating the ServiceInfo Document Dynamically

You can use ASP to create your ServiceInfo document. This can give you greater flexibility in your online store by using the following techniques:

-   Dynamically generating the host name for URLs.
-   Changing URLs for localization based on locale and geoid parameters.
-   Dynamically appending query string parameters from the ServiceInfo URL to other URLs, such as the navigate page URL.

The following example code shows a simple ASP page that dynamically creates a ServiceInfo document:


```C++
<%
    Dim sHost
    Dim sLocale

    sHost = Request.ServerVariables("HTTP_HOST")
    sLocale = Request.QueryString("locale")
%>

<?xml version="1.0" encoding="utf-8"?>
<ServiceInfo Version="1.00" Key="MyCommerceService">
    <FriendlyName>My Online Store</FriendlyName>
    <ServiceTask1
        URL = "https://<%= sHost %>/service/html/Music.asp">
    </ServiceTask1>
    <ServiceTask2
        URL = "https://<%= sHost %>/service/html/Video.asp">
    </ServiceTask2>
    <ServiceTask3
        URL = "https://<%= sHost %>/service/html/Radio.asp">
    </ServiceTask3>
    <Navigate
        BaseURL = "https://<%= sHost %>/service/html/navigate.asp?myloc<%= sLocale %>">
    </Navigate>
</ServiceInfo>
```



The preceding example code uses ASP to retrieve the host name from the web server and dynamically create the URLs in the document. The code also retrieves the *locale* query string parameter from the ServiceInfo request and appends it to the URL for the navigate page.

## Related topics

<dl> <dt>

[**Information Common to Type 1 and Type 2 Online Stores**](information-common-to-type-1-and-type-2-online-stores.md)
</dt> <dt>

[**Navigation for Type 2 Online Stores**](navigation-for-type-2-online-stores.md)
</dt> <dt>

[**ServiceInfo Document for a Type 1 Online Store**](serviceinfo-document-for-a-type-1-online-store.md)
</dt> <dt>

[**ServiceInfo Document for a Type 2 Online Store**](serviceinfo-document-for-a-type-2-online-store.md)
</dt> <dt>

[**ServiceInfo Document**](serviceinfo-document.md)
</dt> </dl>

 

 




