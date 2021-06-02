---
description: Extended Linguistic Services (ELS) is implemented as a dynamic-link library (DLL) that provides a variety of linguistic support functionality for text that the application specifies.
ms.assetid: 23d4e42a-a5bb-467c-a8b9-6a57ae39daa0
title: About Extended Linguistic Services
ms.topic: article
ms.date: 05/31/2018
---

# About Extended Linguistic Services

Extended Linguistic Services (ELS) is implemented as a dynamic-link library (DLL) that provides a variety of linguistic support functionality for text that the application specifies. The technology includes the ELS platform and plug-ins for several predefined linguistic service types accessible to the application through the platform.

> [!Note]  
> The ELS module is installed automatically with Windows 7 and later.

 

## ELS Platform

The ELS platform is the interface between your application and the ELS services. It provides a simple way to implement several kinds of linguistic functionality through the same API, which allows the application to access and use specific services. For more information about the API, see [Extended Linguistic Services Reference.](extended-linguistic-services-reference.md)

> [!Note]  
> When the application calls any of the ELS API functions, the platform allocates memory and resources as needed for communication with the services. The application is responsible for calling the platform again to free these resources.

 

The platform runs inside the application virtual memory space, and all allocated memory is part of this space. Thus your application only needs to link to the ELS component DLL (Elscore.dll) by linking to Elscore.lib or by dynamically loading Elscore.dll.

## ELS Services

For Windows 7 and later, the ELS platform supports only the following predefined services.

-   [Microsoft Language Detection](microsoft-language-detection.md)
-   [Microsoft Script Detection](microsoft-script-detection.md)
-   [Transliteration services](transliteration-services.md)

> [!Note]  
> Future versions of ELS will support additional services provided by Microsoft or service providers.

 

Each service is associated with a service category describing what the service does. The category is represented by a nonlocalizable string. It is used by applications to enumerate available services. The current service categories are:

-   "Language Detection"
-   "Script Detection"
-   "Transliteration"

The platform uses service metadata to enumerate the services requested by the application. Properties such as the service globally unique identifier (GUID), supported input and output languages and scripts, and the service category can be used by the application to enumerate the desired ELS services.

Each ELS service is implemented as a plug-in supported by a DLL that can be installed on the operating system so that the ELS platform can detect and use it. Services can expose their own subservices, if required.

## Main ELS Operations

This section describes the main operations supported by the ELS platform. The platform supports both synchronous and asynchronous calling modes. The asynchronous calling mode uses an application thread pool to schedule threads for processing requests.

> [!Note]  
> Since the platform supports an asynchronous mode, ELS services do not have to implement this type of functionality on their own.

 

### Service Enumeration

The ELS platform loads and manages all ELS services, making operation transparent to the application. The application enumerates the available services by calling [**MappingGetServices**](/windows/desktop/api/Elscore/nf-elscore-mappinggetservices). For programming instructions, see [Enumerating and Freeing Services](enumerating-and-freeing-services.md).

> [!Note]  
> It is advisable for performance reasons to have your application enumerate the available services only once. The ELS platform checks the services again on the next enumeration to ensure that its enumeration results are always current.

 

### Text Recognition

After service enumeration, the application calls the [**MappingRecognizeText**](/windows/desktop/api/Elscore/nf-elscore-mappingrecognizetext) function to use a particular ELS service to map any text range of input text to output text. An example of text recognition is the use of a language detection service that receives a text segment and detects its most probable language.

After the service has recognized the text, [**MappingRecognizeText**](/windows/desktop/api/Elscore/nf-elscore-mappingrecognizetext) returns with a [**MAPPING\_PROPERTY\_BAG**](/windows/desktop/api/Elscore/ns-elscore-mapping_property_bag) structure populated with output data and properties produced by the service. To avoid memory leaks, the application must free the property bag by calling [**MappingFreePropertyBag**](/windows/desktop/api/Elscore/nf-elscore-mappingfreepropertybag) for each time that the [**MappingRecognizeText**](/windows/desktop/api/Elscore/nf-elscore-mappingrecognizetext) returns S\_OK. Usually the application does this either when it finishes using the output data or when the output data is no longer relevant because the input region of text has been modified, for example, edited or deleted. When the property bag is released, **MappingFreePropertyBag** returns.

Programming instructions for text recognition are provided in [Requesting Text Recognition](requesting-text-recognition.md).

### Service Termination

When your application no longer requires ELS services, it calls [**MappingFreeServices**](/windows/desktop/api/Elscore/nf-elscore-mappingfreeservices) before it terminates. For more information, see [Enumerating and Freeing Services](enumerating-and-freeing-services.md).

### Versioning

Future versions of ELS will allow the ELS services to be updated. The application will be able to check the version numbers of the [**MAPPING\_SERVICE\_INFO**](/windows/desktop/api/Elscore/ns-elscore-mapping_service_info) structure to detect any changes in the services.

> [!Note]  
> Your ELS application should not make the assumption that different versions of the same service can retrieve exactly the same results.

 

 

 



