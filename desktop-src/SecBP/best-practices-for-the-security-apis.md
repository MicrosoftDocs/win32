---
description: Suggestions for application security assessments for app development of Windows security software and secure software development, including application security testing.
ms.assetid: bb0ddae2-f559-4785-97c7-182fc204fa60
title: Best Practices for the Security APIs
ms.topic: article
ms.date: 05/31/2018
---

# Best Practices for the Security APIs

To help develop secure software, we recommend that you use the following best practices when developing applications. For more information, see [Security Developer Center](https://msdn.microsoft.com/security/default.aspx).

## Security Development Life Cycle

The [Security Development Life Cycle](/previous-versions/ms995349(v=msdn.10)) (SDL) is a process that aligns a series of security-focused activities and deliverables to each phase of software development. These activities and deliverables include:

-   Developing threat models
-   Using code-scanning tools
-   Conducting code reviews and security testing

For more information about the SDL, see the [SDL Blog](https://blogs.msdn.com/sdl/archive/2007/04/26/welcome-to-the-sdl-blog.aspx).

## Threat Models

Conducting a threat model analysis can help you discover potential points of attack in your code. For more information about threat model analysis, see Howard, Michael and LeBlanc, David \[2003\], *Writing Secure Code*, 2d ed., ISBN 0-7356-1722-8, Microsoft Press, Redmond, Washington. (This resource may not be available in some languages and countries.)

## Service Packs and Security Updates

Build and test environments should mirror the same levels of service packs and security updates of the targeted user base. We recommend that you install the latest service packs and security updates for any Microsoft platform or application that is part of your build and test environment and encourage your users to do the same for the finished application environment. For more information about service packs and security updates, see [Microsoft Windows Update](https://www.update.microsoft.com/microsoftupdate/v6/vistadefault.aspx?ln=en-us) and [Microsoft Security](https://www.microsoft.com/security).

## Authorization

You should create applications that require the least possible privilege. Using the least possible privilege reduces the risk of malicious code compromising your computer system. For more information about running code in least possible privilege level, see [Running with Special Privileges](running-with-special-privileges.md).

## More Information

For more information about best practices, see the following topics.



| Topic                                                                                                                        | Description                                                                                                                                                                                |
|------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Running with Special Privileges](running-with-special-privileges.md)<br/>                                            | Discusses security implications of privileges.<br/>                                                                                                                                  |
| [Avoiding Buffer Overruns](avoiding-buffer-overruns.md)<br/>                                                          | Provides information about avoiding buffer overruns.<br/>                                                                                                                            |
| [Control Flow Guard (CFG)](control-flow-guard.md)<br/>                                                                | Discusses memory corruption vulnerabilities.<br/>                                                                                                                                    |
| [Creating a DACL](creating-a-dacl.md)<br/>                                                                            | Shows how to create a discretionary access control list (DACL) by using the [Security Descriptor Definition Language](/windows/desktop/SecAuthZ/security-descriptor-definition-language) (SDDL).<br/> |
| [Handling Passwords](handling-passwords.md)<br/>                                                                      | Discusses security implications of using passwords.<br/>                                                                                                                             |
| [How to Optimize Your MSDN Library Search](how-to-optimize-your-msdn-library-search.md)<br/>                          | Discusses options for searching Security SDK content on MSDN Library.<br/>                                                                                                           |
| [Dynamic Access Control developer extensibility](/previous-versions/windows/desktop/dacx/dynamic-access-control-developer-extensibility-roadmap)<br/> | Basic orientation to some of the developer extensibility points for the new Dynamic Access Control solutions.<br/>                                                                   |



 

 

