---
description: WMI has several scripting helper objects that supply the conversions required by scripts.
ms.assetid: 832660b7-2992-4d1f-af16-7b8f0477b187
ms.tgt_platform: multiple
title: Scripting Helper Objects
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Scripting Helper Objects

WMI has several scripting helper objects that supply the conversions required by scripts.

WMI scripting helper objects include:

-   [**SWbemDateTime**](swbemdatetime.md)
-   [**SWbemObjectPath**](swbemobjectpath.md)
-   [**Win32\_SecurityDescriptorHelper**](/previous-versions/windows/desktop/secrcw32prov/win32-securitydescriptorhelper)

The helper objects break down composite data structures so that a script is not required to parse the structure to obtain any of the pieces. For example, the **WMI DATETIME** structure cannot be displayed directly, and is different from other Windows datetime data structures, such as **VT\_DATE**.

## SWbemDateTime

The [**SWbemDateTime**](swbemdatetime.md) object provides properties that parse out the day, month, year, time of day, and so on. It also provides conversion methods to convert the Windows Management Instrumentation (WMI) datetime to and from the **VT\_Date** and [**FILETIME**](/windows/desktop/api/minwinbase/ns-minwinbase-filetime) formats. For Internet Explorer (IE) security settings, the **SWbemDateTime** object is the only WMI scripting object that is marked safe for initialization and safe for scripting. For more information and examples of date and time conversions, see [Dates and Times](https://www.microsoft.com/technet/scriptcenter/scripts/default.mspx) and the article on TechNet ScriptCenter [It's About Time (Oh, and About Dates, too)](https://www.microsoft.com/technet/technetmag/issues/2006/07/ScriptingGuy/default.aspx).

## SWbemObjectPath

The properties of [**SWbemObjectPath**](swbemobjectpath.md) supply the absolute path of an object, but also break out the parts of the WMI path, such as server, namespace, class, or relative path. The object allows you to set the security of the path, obtain the key values of the objects representing the path, determine if an object is a singleton, and so on. For more information about working with WMI object paths, see [Describing the Location of a WMI Object](describing-the-location-of-a-wmi-object.md).

## Win32\_SecurityDescriptorHelper

The [**Win32\_SecurityDescriptorHelper**](/previous-versions/windows/desktop/secrcw32prov/win32-securitydescriptorhelper) class converts the security descriptor of a securable object from one format to another.

Many objects, such as printers, WMI namespaces, registry keys, or DCOM applications, have security descriptors that control access to the object. You can use WMI to discover or change who has access to these objects by getting or setting the security descriptor associated with the object.

However, different methods may obtain security descriptors in a binary byte array, [Security Descriptor Definition Language](/windows/desktop/SecAuthZ/security-descriptor-string-format) (SDDL) format, or as an instance of [**Win32\_SecurityDescriptor**](/previous-versions/windows/desktop/secrcw32prov/win32-securitydescriptor). The binary byte array form of a security descriptor should not be manipulated except by the C++ methods designed for [Security Descriptor Operations](/windows/desktop/SecAuthZ/security-descriptor-operations). Descriptors in SDDL are in strings, but are still awkward to manipulate. The easiest format to manipulate is **Win32\_SecurityDescriptor**, because it contains embedded objects for trustee, ACE, and SID. For more information about the structure of security descriptors in WMI, see [WMI Security Descriptor Objects](wmi-security-descriptor-objects.md). For more information about how to do conversions, see [Changing Access Security on Securable Objects](changing-access-security-on-securable-objects.md).

## Related topics

<dl> <dt>

[Scripting in WMI](/windows/desktop/WmiSdk/creating-a-wmi-script)
</dt> </dl>

 

 
