---
description: Security (Windows 7 and Windows Server 2008 R2 Application Quality Cookbook)
ms.assetid: 87331C1D-F468-4CA4-92BD-D4E5D4E930BC
title: Security (Windows 7 and Windows Server 2008 R2 Application Quality Cookbook)
ms.topic: article
ms.date: 05/31/2018
---

# Security (Windows 7 and Windows Server 2008 R2 Application Quality Cookbook)

Starting with Windows Internet Explorer 7, Windows Internet Explorer runs in a security context called *Protected Mode* when users run it on the Windows Vista operating system or a later version. This mode runs Internet Explorer in a lower-privilege setting than a standard user application so certain functionality is limited, especially ActiveX controls and certain types of plug-ins. For more information about Protected Mode in Internet Explorer and its impact on compatibility, see [Understanding and Working in Protected Mode Internet Explorer](/previous-versions/windows/internet-explorer/ie-developer/) in the MSDN Library.

By default, Windows Internet Explorer 8 also enables Data Execution Prevention (DEP), which helps applications avoid running arbitrary code in online attacks. However, some add-ons might not use this security feature (for example, any add-ons that are not designed to run only code that is located in memory that has been specifically marked as executable, such as applications that are built by using an older version of the ActiveX Template Library (ATL) framework).

Internet Explorer 8 also protects users against potential security vulnerabilities that use scripts. For example, you cannot navigate from a URL in a less trusted zone to a URL in a more trusted zone except through explicit user interaction. You also cannot hide certain elements of the browser’s user interface (such as the address bar) in an un-trusted (Internet) zone.

## Related topics

<dl> <dt>

[Design Updates that Impact Compatibility between Browsers](design-updates-that-impact-compatibility-between-browsers.md)
</dt> </dl>

 

 
