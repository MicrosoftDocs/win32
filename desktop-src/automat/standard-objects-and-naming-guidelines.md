---
title: Standard Objects and Naming Guidelines
description: This section describes the standard ActiveX objects, and discusses naming guidelines for creating objects that are unique to applications, especially user-interactive applications that support a multiple-document interface (MDI).
ms.assetid: 59a730c9-1068-4d02-9509-8c4cdd3b5d9e
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Standard Objects and Naming Guidelines

This section describes the standard ActiveX objects, and discusses naming guidelines for creating objects that are unique to applications, especially user-interactive applications that support a multiple-document interface (MDI). If an ActiveX object is not user-interactive or supports only a single-document interface (SDI), the standards and guidelines should be adapted as appropriate.

-   *Standard objects* comprise a set of objects defined by Automation. You can use them as appropriate to your application. The objects described in [Using Standard Objects](using-standard-objects.md) are oriented toward document-based, user-interactive applications. Other applications (such as noninteractive database servers) may have different requirements.

-   *Naming guidelines* are recommendations meant to improve consistency across applications. See [Naming Conventions](naming-conventions.md) for these recommendations.

-   *Programmability interfaces* provide access to an object's containing document and containing application. [Accessing the Containing Document](accessing-the-containing-document.md) and [Accessing the Containing Application](accessing-the-containing-application.md) describe the standards for exposing these interfaces.

This section also provides examples in a hypothetical syntax derived from Visual Basic. The standards and guidelines are subject to change.

## In this section



| Topic                                                                   | Description                                                                                                                            |
|-------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| [Using Standard Objects](using-standard-objects.md)<br/>         | Describes the standard objects.<br/>                                                                                             |
| [Naming Conventions](naming-conventions.md)<br/>                 | Choose names for exposed objects, properties, and methods that can be easily understood by users of the application.<br/>        |
| [Programmability Interfaces](programmability-interfaces.md)<br/> | Embeddable objects, including ActiveX controls, often require access to the programmability interfaces of their containers.<br/> |



 

## Related topics

<dl> <dt>

[Automation Programming Reference](automation-programming-reference.md)
</dt> </dl>

 

 





