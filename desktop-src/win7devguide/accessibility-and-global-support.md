---
title: Accessibility and Global Support
description: The Windows 7 platform makes it easier to build solutions that are accessible to more users and that meet or exceed accessibility compliance standards.
ms.assetid: bcad2f00-7885-461c-a2dc-0a0a176962b4
ms.topic: article
ms.date: 05/31/2018
---

# Accessibility and Global Support

The Windows 7 platform makes it easier to build solutions that are accessible to more users and that meet or exceed accessibility compliance standards. The assistive technology vendor (ATV) community can now build solutions for a broader variety of client applications, and application developers will find it easier to build and validate accessible user interfaces.

Windows 7 also makes supporting multiple global languages easier than in previous versions of Windows. From the time a user selects a language and location, Windows 7 presents dates, numbers, calendars, collations, and other information using the cultural conventions that customers expect.

## Windows Automation

Windows 7 delivers a rich, standards-based automation layer that is extended for native applications. It builds on Microsoft Active Accessibility and Microsoft UI Automation. It's also designed to work with industry standards such as the W3C Web ARIA (Accessible Rich Internet Application) and *Section 508 Specifications*.

UI Automation offers improved performance by introducing faster unmanaged automation proxies for Microsoft Win32 controls and legacy Microsoft Active Accessibility (*MSAA*) applications, and better and faster UI Automation event and proxy registrations. New extensibility features extend control patterns, properties, and custom events. (See [Windows Automation API: Overview](../winauto/windows-automation-api-overview.md).)

## Accessibility Support Tools

The UI Accessibility Checker is a convenient graphical user interface tool that enables developers and testers to rapidly verify whether their UI conforms to key accessibility requirements, such as *MSAA* (which verifies child-parent relationships or bounding rectangles) and UI Automation programmatic access, event generation, layout, and keyboard navigation. (See [UI Accessibility Checker](https://www.codeplex.com/AccCheck).)

UIA Verify is a test automation framework that facilitates manual and automated testing of the UI Automation provider implementation of a control or application. These two new tools enable developers to test accessibility implementations and functionality in applications that use either *MSAA* or UI Automation. Both tools are available via [CodePlex](https://www.codeplex.com/), a web site that Microsoft created to host open-source projects and to better serve the developer community.

## Improved Multi-Language User Interface Support and Linguistic Services

Windows 7 provides developers with a standard method to prepare their applications for the international market by delivering an improved multi-language user interface support and linguistic services that they can use in their applications.

Extended Linguistic Services is a new feature in Windows 7 that allows developers to use the same small set of APIs to leverage a variety of advanced linguistic functionality. By using Extended Linguistic ServicesAPIs in Windows 7, developers can auto-detect the language of any piece of Unicode text and use that information to help make smarter user experience choices for customers around the world. Extended Linguistic Services also offers built in transliteration support that converts text from one writing system to another. For example, developers can now auto-convert text between simplified and traditional Chinese to help people communicate with each other across linguistic boundaries. By using Extended Linguistic ServicesAPIs, developers will be able to use existing Extended Linguistic Services as well as pick up new services in the future without learning new code. (See [Extended Linguistic Services](../intl/extended-linguistic-services.md).)

 

 
