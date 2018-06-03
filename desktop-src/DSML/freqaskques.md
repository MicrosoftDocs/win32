---
title: Frequently Asked Questions
description: Answers to some of the more common Frequently Asked Questions.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: d586b412-1500-4a6c-a014-48d4f3defc4e
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- FAQ DSML
- Frequently Asked Questions DSML
- DSML Services for Windows, FAQs
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Frequently Asked Questions

The following is a list of answers to some of the more common Frequently Asked Questions:

-   What can I do with DSML Services for Windows?

    You can perform virtually all LDAP operations as defined in RFC 2251 against DSML V2 using a valid DSML request payload.

-   Do I need a server running Windows Server 2003 to run DSML Services for Windows?

    No, DSML Services for Windows can run on servers running either Windows Server 2003, Standard Edition or Windows 2000 Server.

-   Is DSML Services for Windows included in Windows Server 2003?

    No, DSML Services for Windows is not part of Windows Server 2003. DSML Services for Windows can be downloaded as a stand-alone application.

-   Can I run DSML Services for Windows against Active Directory running on Windows 2000?

    Yes.

-   How do I configure DSML Services for Windows to make it secure?

    DSML Services for Windows uses IIS for security. Per the DSML V2 specification, DSML Services for Windows does not have its own security model and assumes that authentication happens out-of-band and before DSML Services for Windows processes requests.

-   Which object model can I use to access DSML Services for Windows?

    You can use any object model or API sets that allow you to transmit an HTTP request and receive an HTTP response, for example, the **IXmlHttpRequest** API call. DSML Services for Windows does not have a specific object model that transmits and receives the DSML payload over SOAP, and then translates the DSML response back to the object model.

 

 




