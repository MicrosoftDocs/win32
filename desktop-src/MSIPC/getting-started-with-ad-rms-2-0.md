---
title: Get started
description: The Rights Management Services SDK 2.1 platform enables developers to build applications that leverage RMS information protection via an RMS Server or Azure RMS.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 728113C9-FCF9-4280-BE1D-6AF5C15E449E
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Get started

The Rights Management Services SDK 2.1 platform enables developers to build applications that leverage RMS information protection via an RMS Server or Azure RMS. The platform handles complex security practices such as key management, encryption and decryption processing and, offers a simplified API for easy application development.

## Get started with RMS SDK 2.1

This topic will guide you through the process of setting up and running your rights-enabled application in a testing environment. The following topics discuss how to set up your development environment and are listed such that they suggest an order that you could perform the tasks.

## In this section



| Topic                                                                                                        | Description                                                                                                                                                              |
|--------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Release notes](release-notes--rtm-.md)<br/>                                                          | This topic contains important information about this and previous releases of the RMS SDK 2.1.<br/>                                                                |
| [Install the SDK](create-your-first-rights-aware-application.md)<br/>                                 | This topic guides you through installing the developer tools.<br/>                                                                                                 |
| [Configure Visual Studio](how-to-configure-a-visual-studio-project-to-use-the-ad-rms-sdk-2-0.md)<br/> | This topic contains instructions about how to configure a Visual Studio project to use the RMS SDK 2.1.<br/>                                                       |
| [Developing your application](developing-your-application.md)<br/>                                    | This topic contains essential guidance on the core aspects of an RMS enabled application and can serve as the foundation of your own application development.<br/> |
| [Testing your application](how-to-configure-the-ad-rms-client-2-0.md)<br/>                            | This topic contains instructions about how to setup for your application testing.<br/>                                                                             |
| [Deploy into production](deploying-your-application.md)<br/>                                          | This topic guides you through deployment options for your rights-enabled application.<br/>                                                                         |



 

<dl> Once you've gotten started, check out some of our other [RMS samples](https://msdn.microsoft.com/library/windows/desktop/dn133064). Then, stay current through our [RMS Developer's Corner](http://blogs.msdn.com/b/rms/).  
</dl>

## Why use RMS SDK 2.1 for protecting your content

For developers who want to add RMS support to their new and existing applications, the RMS SDK 2.1 helps make it easier to:

-   Author manageable, compliant and robust RMS-aware applications.
-   Encrypt user data persistently. The data remains encrypted regardless of the environment, device, or operating system.
-   Enforce a rich set of usage restrictions, such as preventing screen captures of your sensitive data.
-   Support enterprise-managed protection policies.
-   Support new authentication mechanisms and encryption algorithms as they become available.

The RMS SDK 2.1 supports a range of important client and server platforms. For more information see, [Supported platforms](supported-platforms.md).

## Core principles

<dl> **Simplicity** Feedback and usage patterns for the AD RMS SDK 1.0 were analyzed, and that data used to simplify or automate the most difficult programming tasks. RMS applications authored using the RMS SDK 2.1 typically require 5 10 times fewer lines of RMS code than RMS applications written using AD RMS SDK 1.0.  
**Write once** RMS SDK 2.1 applications do not need a code change or a recompile to work with the newest RMS features. New RMS features will become available in your existing application as they get added to the RMS server.  
**Consistency** RMS SDK 2.1 helps make it easy to write applications that consistently honor different RMS configurations. It also significantly reduces the amount of RMS user interface you, as the application developer, needs to author, encouraging a consistent look and feel and reducing the need for user education.  
</dl>

## Related topics

<dl> <dt>

[AD RMS samples](https://msdn.microsoft.com/library/windows/desktop/dn133064)
</dt> <dt>

[AD RMS Developer's Corner](http://blogs.msdn.com/b/rms/)
</dt> <dt>

[Install the SDK](create-your-first-rights-aware-application.md)
</dt> <dt>

[IPCHelloWorld - an example application](https://msdn.microsoft.com/library/jj127293)
</dt> <dt>

[Overview](ad-rms-overview.md)
</dt> <dt>

[Supported platforms](supported-platforms.md)
</dt> </dl>

 

 





