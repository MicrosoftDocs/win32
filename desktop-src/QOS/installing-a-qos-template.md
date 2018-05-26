---
title: Installing a QOS Template
description: Under certain circumstances, such as when available QOS templates do not fit required or desired QOS parameters, an application may want to install a QOS template of its own.
ms.assetid: 145928bf-fc4c-4794-840e-334045554706
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Installing a QOS Template

Under certain circumstances, such as when available QOS templates do not fit required or desired QOS parameters, an application may want to install a QOS template of its own. By installing a QOS template that is tailored specifically to its needs, the application can benefit from easier and more consistent implementation of QOS parameter requests.

Note that the installation of a QOS template requires administrative privilege. The process of installing a QOS template is contained within the [**WSCInstallQOSTemplate**](wscinstallqostemplate.md) function. Essentially, a successful call to **WSCInstallQOSTemplate** installs a QOS template and associates the template with the name provided in the lpQOSName parameter. Once the QOS template is installed with **WSCInstallQOSTemplate**, it can be applied to a connection through the use of the [**WSAGetQOSByName**](https://msdn.microsoft.com/library/windows/desktop/ms741587) function.

 

 




