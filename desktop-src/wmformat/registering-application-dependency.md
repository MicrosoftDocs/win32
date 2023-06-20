---
title: Registering Application Dependency (Windows Media Format 11 SDK)
description: Learn how to register your application with runtime components of APIs provided by the Windows Media Format 11 SDK.
ms.assetid: 09f63519-5c65-4784-9ea4-4fbecfa6d4aa
keywords:
- Windows Media Format SDK,registering application dependencies
- registering application dependencies
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Registering Application Dependency (Windows Media Format 11 SDK)

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Applications that use APIs provided by the Windows Media Format SDK or Windows Media Player SDK are dependent upon the run-time components of those technologies. You can register your application as being dependent on those components as part of your application setup.

When you register your application, you can choose one of two levels of dependency: blocking, or dependent. When one or more applications are registered with a blocking dependency on one of the run-time components, the component will be blocked from a rollback to a previous version. Dependent applications that are not registered as blocking, do not block rollback. Instead, before the rollback is performed, the user is prompted with a message stating that applications are dependent on the component.

To register your application, you must set a value in the registry that identifies your application. The registry value to set depends on the component on which your application is dependent. You can also set two additional values per dependency to provide extra information about your application.

The following registry values are used to register dependence on the Windows Media Format SDK runtime:

-   HKEY\_CLASSES\_ROOT\\Software\\Microsoft\\WindowsMedia\\Setup\\*REF\_TYPE*\\App, "*APP*", "*APP\_STRING*"
-   HKEY\_CLASSES\_ROOT\\Software\\Microsoft\\WindowsMedia\\Setup\\*REF\_TYPE*\\Descriptor, "*APP*", "*REF\_DESCRIPTOR*"
-   HKEY\_CLASSES\_ROOT\\Software\\Microsoft\\WindowsMedia\\Setup\\*REF\_TYPE*\\Version, "*APP*", "*WMF\_VERSION*"

The following registry value are used to register dependence on Windows Media Player SDK runtime:

-   HKEY\_CLASSES\_ROOT\\Software\\Microsoft\\MediaPlayer\\Setup\\*REF\_TYPE*\\App, "*APP*", "*APP\_STRING*"
-   HKEY\_CLASSES\_ROOT\\Software\\Microsoft\\MediaPlayer\\Setup\\*REF\_TYPE*\\Descriptor, "*APP*", "*REF\_DESCRIPTOR*"
-   HKEY\_CLASSES\_ROOT\\Software\\Microsoft\\MediaPlayer\\Setup\\*REF\_TYPE*\\Version, "*APP*", "*WMP\_VERSION*"

The following variables are used in the registry values listed above:

*REF\_TYPE*

Replace with BlockingRefCounts for blocking dependency, or with DependentRefCounts for non-blocking dependency.

*APP*

Name or short descriptor of your application. This string will not be used in messages displayed for the user. This value is the identifier used in all three registry values associated with each of the run-time components.

*APP\_STRING*

Descriptor of your application. This string may be used in messages displayed for the user.

*REF\_DESCRIPTOR*

Description of how your application uses the component. This value can include a maximum of 256 characters.

*WMP\_VERSION*

Version of Windows Media Player required by your application.

*WMF\_VERSION*

Version of the Windows Media Format SDK required by your application.

The following three example registry values demonstrate how to configure the values for your application:

-   HKEY\_CLASSES\_ROOT\\Software\\Microsoft\\WindowsMedia\\Setup\\DependentRefCounts\\App, "SouthridgeVideo", "Southridge Video Player"
-   HKEY\_CLASSES\_ROOT\\Software\\Microsoft\\WindowsMedia\\Setup\\DependentRefCounts\\Descriptor, "SouthridgeVideo", "Southridge Video Player uses the Windows Media Format SDK to play video files."
-   HKEY\_CLASSES\_ROOT\\Software\\Microsoft\\WindowsMedia\\Setup\\DependentRefCounts\\Version, "SouthridgeVideo", "9.0.0.2600"

## Related topics

<dl> <dt>

[**Project Considerations**](project-considerations.md)
</dt> </dl>

 

 




