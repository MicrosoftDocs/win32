---
title: Packaging
description: This topic describes the Packaging APIs, which provide support for applications that produce or consume Open Packaging Conventions \ 8211;compliant files, called packages.
ms.assetid: 77df9cb2-757e-4b07-9c1c-73af0df4702f
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Packaging

This topic describes the Packaging APIs, which provide support for applications that produce or consume Open Packaging Conventions compliant files, called packages.

This topic contains the following sections.

-   [Purpose](#purpose)
-   [What is Packaging?](#what-is-packaging)
-   [Developer Audience](#developer-audience)
    -   [Prerequisites](#prerequisites)
-   [Additional Resources and Related Technologies](#additional-resources-and-related-technologies)
-   [Section Contents](#section-contents)
-   [Related topics](#related-topics)

## Purpose

The Windows 7 Packaging feature is a set of COM-based API that provides support for accessing, modifying, and saving packages by using C and C++.

## What is Packaging?

Packaging can be more easily understood through an analogy with real world filing systems. People and businesses need to organize their information. Often, this information is tracked by using paperwork that is stored in folders, which are, in turn, stored in filing cabinets. For each person and business, someone had to design a system that would allow information to be quickly accessed when needed.

A personalized filing system provides great advantages for someone who understands how the system works, but when someone new needs to access the system, how do they know where to find the information that they need? Suddenly, the personalized filing system becomes less convenient. Applications face similar challenges in organizing data: what information is most important and how can developers ensure that it is easily accessible?

The *ECMA-376 OpenXML, 1st Edition, Part 2: Open Packaging Conventions (OPC)* specification provides an answer to this question. A package, as described in the *OPC*, enables different applications to access key information from an OPC based file in a standardized way. A package resembles a filing cabinet whose basic organization is known to all the people and businesses that interact with it.

Examples of ZIP-based package formats include:


    -   Office Word 2007 documents (.docx)
    -   Office Excel 2007 worksheets (.xlsx)
    -   Office PowerPoint 2007 presentations (.pptx)
-   XPS documents (.xps)

## Developer Audience

The Packaging APIs are designed for the following classes of developers:

-   Developers who create applications that interact with packages.
-   Developers who create tools or add-ons that interact with packages.

### Prerequisites

To use the Packaging API, you must have a practical understanding of the technologies in the following table:



| Technology                                                                                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|-------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [COM Programming](https://www.bing.com/search?q=COM Programming)                                                    | As a COM-based API set, the Packaging API relies on you to perform tasks such as error handling, resource management, and synchronization. For an introduction to COM programming, see [COM Programming](https://www.bing.com/search?q=COM Programming).<br/>                                                                                                                                                                                                                                  |
| OPC specification of the [ECMA-376 OpenXML](http://go.microsoft.com/fwlink/p/?linkid=123375) standard | The OPC provides in-depth information and supplements the descriptions and requirements provided in the Packaging API documentation. For a summary of key ideas in the specification, see [Open Packaging Conventions Fundamentals](open-packaging-conventions-overview.md). For more in-depth information, see 1st edition, Part 2 of the [ECMA-376 OpenXML](http://go.microsoft.com/fwlink/p/?linkid=123375) (http://go.microsoft.com/fwlink/p/?linkid=123375) standard.<br/> |



 

## Additional Resources and Related Technologies

Although not required to use the Packaging API, knowledge of the following technologies will advance your understanding of the Packaging API.



| Technology                                                                          | Description                                                                                                                                                                                                                                                                                                                                                |
|-------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [System.IO.Packaging](https://www.bing.com/search?q=System.IO.Packaging)                                        | The managed Packaging API implementation. For a summary of key differences between this and the managed API, see [Differences between the Native and Managed APIs](differences-between-the-native-and-managed-apis.md). For in-depth information about the managed implementation, see [System.IO.Packaging](https://www.bing.com/search?q=System.IO.Packaging).<br/>           |
| [XPS Document API](https://msdn.microsoft.com/library/windows/desktop/dd316976)                                               | The native implementation of the XML Paper Specification (XPS) (an OPC-based format), which is built on the Packaging APIs. For in-depth information, see [XPS Document API](https://msdn.microsoft.com/library/windows/desktop/dd316976).<br/>                                                                                                                                                |
| [XPS Digital Signature API](https://msdn.microsoft.com/library/windows/desktop/dd372947)                             | The native implementation of XPS Digital Signature requirements,which is built on the Packaging APIs. For in-depth information, see [XPS Digital Signature API](https://msdn.microsoft.com/library/windows/desktop/dd372947).<br/>                                                                                                                                                    |
| [Extensible Markup Language (XML)](http://go.microsoft.com/fwlink/p/?linkid=146591) | If your application interacts with XML markup that is acessed by calling a Packaging API, you will find it easier to develop applications if you are familiar with XML markup. For more information, see [Extensible Markup Language (XML)](http://go.microsoft.com/fwlink/p/?linkid=146591) (http://go.microsoft.com/fwlink/p/?linkid=146591).<br/> |



 

## Section Contents



| Topic                                                              | Description                                                                                                                                        |
|--------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| [Packaging API Programming Guide](packaging-programming-guide.md) | This section contains conceptual topics that describe how to use the Windows 7 Packaging APIs.                                                     |
| [Packaging API Reference](packaging-programming-reference.md)     | The topics in this section provide information about the Packaging APIs.                                                                           |
| [Packaging API Samples](packaging-programming-samples.md)         | The topics in this section briefly describe the sample programs that accompany the Microsoft Windows Software Development Kit (SDK) for Windows 7. |
| [*Packaging API Glossary*](packaging-glossary.md)                 | This topic provides definitions for Packaging API terms.                                                                                           |



 

## Related topics

<dl> <dt>

**Overviews**
</dt> <dt>

[Getting Started with the Packaging API](packaging-api-overview.md)
</dt> <dt>

**External Resources**
</dt> <dt>

[ECMA-376 OpenXML](http://go.microsoft.com/fwlink/p/?linkid=123375)
</dt> </dl>

 

 





