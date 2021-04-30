---
description: Parental Controls Samples
ms.assetid: 19dac95c-2279-4bf9-a58c-dd30177c0c9d
title: Parental Controls Samples
ms.topic: article
ms.date: 05/31/2018
---

# Parental Controls Samples

Sample code for Parental Controls is available under path <installation directory>\\Windows\\<version number>\\Samples\\Security\\ParentalControls. The samples are as follows:

## Utilities

Helper functionality for basic COM management, SID string operations, and WMI read and write functionality. All of the other samples depend on this project unless otherwise specified.

## ComplianceAPI

Command-line driven console application demonstrating how to use the Compliance API to retrieve a key subset of settings for a user.

## ComplianceApp

Simple console application demonstrating use of the Compliance API to check for logging required and specific restrictions. If time restrictions are enabled, the application also waits for the impending logout events.

## UIExtensibility

Command-line driven console application demonstrating use of the WMI APIs and WPC schema to list, query, add, modify, and delete UI Extensibility link entries.

Example command line for sample:

"D:\\WPC\\Samples\\Security\\ParentalControls\\UIExtensibility\\debug\\UIExtensibility" add /g:{FD59BB7F-54AB-11DB-9666-00E08161165F} /c:0 /n:D:/WPC/Samples/Security/ParentalControls/UiExtRC/debug/UiExtRC.dll,-101 /s:D:/WPC/Samples/Security/ParentalControls/UiExtRC/debug/UiExtRC.dll,-103 /i:D:/WPC/Samples/Security/ParentalControls/UiExtRC/debug/UiExtRC.dll,-104 /d:D:/WPC/Samples/Security/ParentalControls/UiExtRC/debug/UiExtRC.dll,-106 /e:c:\\windows\\Notepad.exe

where UiExtRC is a simple resource DLL with string resources for ID's 101 and 103, and 24x24 pixel 32-bit with alpha bitmaps for resources 104 and 106.

## WebExtensibility

Command-line driven console application demonstrating how to use the WMI APIs and WPC schema to list, add, and delete HTTP application or URL exemption entries, and to set and reset a Web Content Filter override with the FilterID and FilterName properties.

Access to the read-only HTTP application and URL exemption lists is not shown, but the code to read the lists would be the same as for the read/write case except for modification of the WMI parameter.

 

 



