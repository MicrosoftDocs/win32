---
description: Multilingual User Interface (MUI) is a technology that provides users a localized user interface for globalized applications and user interface language resource management in the Windows operating system.
ms.assetid: 1982931c-fce9-418f-a35d-439b7b886fd9
title: About Multilingual User Interface
ms.topic: article
ms.date: 05/31/2018
---

# About Multilingual User Interface

Multilingual User Interface (MUI) is a technology that provides users a localized user interface for globalized applications and user interface language resource management in the Windows operating system. Support is provided for adding MUI functionality to globalized applications to run on Windows Vista and later, as well as many pre-Windows Vista operating systems. The MUI localization and resource management models enhance development, testing, and support for world-ready software.

Features of MUI technology include:

-   Simplified language management for software localization. MUI allows the language settings for the operating system to be changed to a supported language according to user preferences.
-   An innovative resource technology based on the splitting of the application code binary from language resource files. You can add resources for an additional language without needing to recompile or relink your application. Additional localized resources become optional add-ins.
-   Complete application programming interface (API). Windows Vista and later expose the MUI API for you to use in adding MUI functionality to globalized applications. Language management functions enable your applications to support a wide variety of user interface languages. The API also includes resource loading functions that enable the resource loader to load resources on Windows Vista and later, as well as pre-Windows Vista operating systems.
-   A set of language pack management tools that provide flexibility in international deployment image management. These tools are not targeted at developers and thus are not covered in the SDK. More information can be found in the Windows Automated Installation Kit available on Technet.

The most visible benefit of MUI is that multiple users can share the same workstation and view the user interface in different languages. Corporations and OEMs will benefit from the capability they have to roll out, support, and maintain multilingual images with a single installation. But perhaps the main benefit of MUI comes in the efficiencies gained when developing, building and servicing your application. You can ship one core functionality binary applicable to all platforms, independent of UI language, which significantly reduces development and testing efforts. If you have to issue an update or a service pack, it will apply to all supported languages with no additional engineering effort. Later support for additional languages becomes a localization project instead of a full software development project.

This section covers the following topics:

-   [Understanding MUI](understanding-mui.md)
-   [Availability of MUI](availability-of-mui.md)
-   [MUI Resource Management](mui-resource-management.md)
-   [User Interface Language Management](user-interface-language-management.md)
-   [Development of MUI Applications](development-of-mui-applications.md)
-   [Application Deployment](application-deployment.md)

 

 



