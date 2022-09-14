---
description: This article provides an index of documentation about the available Win32 APIs for Windows features and technologies.
ms.assetid: FF115416-220F-4FCD-8690-F9C0890CD6CC
title: Desktop app technologies
ms.topic: article
ms.date: 05/31/2018
---

# Desktop app technologies

This section provides in-depth guidance and code examples about Windows features that are available to desktop applications by using the Win32 API.

## In this section

| Topic | Description  |  
|----------------------------------|---|
| [Accessibility](accessibility/accessibility.md) | Provides guidance for Windows developers designing accessible applications, assistive technology developers building tools such as screen readers and magnifiers, and software test engineers creating automated scripts for testing Windows applications. |
| [Desktop user interface](windows-application-ui-development.md) | Provides information that enables you to develop graphical user interfaces for your apps, including features such as windows and messages, resources, and controls. |
| [Desktop environment](user-interface.md) | Provides guidance for integrating and extending the desktop user-facing features of Windows, including the Taskbar, the desktop, and File Explorer. |
| [Application installation and servicing](application-installing-and-servicing.md) | Provides information about using APIs and services provided by Windows to install, manage, and service your desktop apps. |
| [Audio and video](audio-and-video.md) | Provides guidance about using audio and video features provided by Windows. |
| [Data access and storage](data-access-and-storage.md) | Provides information about data access and storage features you can use in your desktop applications, including file system management and cloud sync engines.  |
| [Devices](devices.md) | Describes APIs for interacting with devices and sensors. |
| [Diagnostics](diagnostics.md) | Provides guidance about debugging and error handling, performance profiling, network monitoring, and other diagnostics features. |
| [Documents and printing](printdocs/documents-and-printing.md) | Describes the documents and printing features of Windows that enable applications to save, view, and print.  |
| [Graphics and gaming](graphics-and-multimedia.md) | Provides information about graphics and gaming features of Windows, including DirectX and digital imaging.  |
| [Networking and Internet](networking.md) | Provides guidance about the networking and Internet-related features of Windows, including network management, HTTP APIs, and Remote Procedure Call (RPC). |
| [Security and identity](security.md) | Provides information about authentication, authorization, cryptography, and other security features of Windows. |
| [System services](system-services.md) | Provides guidance about fundamental OS features such as process and threads, services, dynamic-link libraries, COM, the registry, and more. |
| [AI and machine learning](/windows/ai/) | Transform your Windows application with the power of artificial intelligence. Windows AI empowers you and your business to achieve more by providing intelligent solutions to complex problems. |

<!--
<br/>

| User Interface and accessibility | System services and fundamentals  |  Audio, video, and graphics  |
|----------------------------------|---|----|
| [Desktop User Interface](windows-application-ui-development.md)<br/>[Windows and messages](winmsg/windowing.md)<br/>[Desktop Window Manager](dwm/dwm-overview.md)<br/>[Menus and other resources](menurc/resources.md)<br/>[Dialog boxes](dlgbox/dialog-boxes.md)<br/>[Data exchange](dataxchg/data-exchange.md)<br/>[High DPI](hidpi/high-dpi-desktop-application-development-on-windows.md)<br/>[Windows controls (Win32)](controls/window-controls.md)<br/>[Desktop environment and shell](user-interface.md)<br/>[Windows Property System](properties/windows-properties-system.md)<br/>[Accessibility](accessibility.md) | [System services](system-services.md)<br/>[Component Object Model (COM)](com/component-object-model--com--portal.md)<br/>[COM+](cossdk/component-services-portal.md)<br/>[Structured storage](stg/structured-storage-start-page.md)<br/>[Dynamic-link libraries](dlls/dynamic-link-libraries.md)<br/>[Interprocess communications](ipc/interprocess-communications.md)<br/>[Memory management](memory/memory-management.md)<br/>[Power management](power/power-management-portal.md)<br/>[Processes and threads](procthread/processes-and-threads.md)<br/>[Services](services/services.md)<br/>[Synchronization](sync/synchronization.md)<br/>[Windows system information](sysinfo/windows-system-information.md) | [Audio and video technologies](audio-and-video.md)<br/>[Core Audio APIs](coreaudio/core-audio-apis-in-windows-vista.md)<br/>[DirectShow](directshow/directshow.md)<br/>[Windows Multimedia](multimedia/windows-multimedia-start-page.md)<br/>[Graphics and gaming technologies](graphics-and-multimedia.md)<br/>[DirectX](directx.md)<br/>[Direct2D](direct2d/direct2d-portal.md)<br/>[Direct3D](direct3d.md)<br/>[Windows GDI](gdi/windows-gdi.md)<br/>[GDI+](gdiplus/-gdiplus-gdi-start.md)<br/>[OpenGL](opengl/opengl.md)<br/>[Windows Imaging Component](wic/-wic-lh.md) |

<br/>

| Networking and Internet | Data access and storage  |  Devices, documents, and printing  |
|----------------------------------|---|----|
| [Networking and Internet overview](networking.md)<br/>[Remote Procedure Call](rpc/rpc-start-page.md)<br/>[Delivery optimization](delivery_optimization/delivery-optimization-portal.md)<br/>[Network interfaces](network-interfaces.md)<br/>[Network management](netmgmt/network-management.md)<br/>[Network share management](netshare/network-share-management.md)<br/>[Windows networking](wnet/windows-networking-wnet-.md)<br/>[Windows Sockets 2](winsock/windows-sockets-start-page-2.md)<br/>[Wireless networking](wireless-networking.md) | [Data access and storage overview](data-access-and-storage.md)<br/>[Local file systems](fileio/file-systems.md)<br/>[Distributed File System](dfs/distributed-file-system.md)<br/>[Projected File System](projfs/projected-file-system.md)<br/>[Cloud sync engines](cfapi/cloud-files-api-portal.md)<br/>[Virtual Storage](VStor/virtual-storage.md)<br/>[Background Intelligent Transfer Service](bits/background-intelligent-transfer-service-portal.md)<br/>[Backup](backup.md) | [Devices overview](devices.md)<br/>[Communications resources](devio/communications-resources.md)<br/>[Location API](locationapi/windows-location-api-portal.md)<br/>[Sensor API](sensorsapi/portal.md)<br/>[UPnP APIs](upnp/universal-plug-and-play-start-page.md)<br/>[Windows Portable Devices](windows-portable-devices.md)<br/>[Documents and printing](printdocs/documents-and-printing.md) |

<br/>

| Security and identity | Diagnostics and testing  |  Packaging and installation  |
|----------------------------------|---|----|
| [Security and identity overview](security.md)<br/>[Antimalware Scan Interface](amsi/antimalware-scan-interface-portal.md)<br/>[Authentication](secauthn/authentication-portal.md)<br/>[Authorization](secauthz/authorization-portal.md)<br/>[Certificate Enrollment API](seccertenroll/certenroll-portal.md)<br/>[Cryptography (CNG)](seccng/cng-portal.md)<br/>[Rights Management](SrvNodes/rights-management.md)<br/>[Security Management](secmgmt/management-portal.md)<br/>[TPM Base Services](tbs/tpm-base-services-portal.md)<br/>[Windows Biometric Framework](secbiomet/biometric-service-api-portal.md) | [Diagnostics overview](diagnostics.md)<br/>[Debugging and error handling](debugging-and-error-handling.md)<br/>[Network Monitor](netmon2/network-monitor.md)<br/>[System Monitor](sysmon/system-monitor-portal.md)<br/>[Performance counters](perfctrs/performance-counters-portal.md)<br/>[Windows error reporting](wer/windows-error-reporting.md)<br/>[Windows events](events/windows-events.md)<br/>[TraceLogging](tracelogging/trace-logging-portal.md)<br/>[Debugging tools for Windows](/windows-hardware/drivers/debugger/index) | [MSIX packaging](/windows/msix)<br/>[Application install and servicing](application-installing-and-servicing.md)<br/>[Side-by-side assemblies](sbscs/isolated-applications-and-side-by-side-assemblies-portal.md)<br/>[Packaging and query of UWP apps](appxpkg/appx-portal.md)<br/>[Windows Installer](msi/windows-installer-portal.md)<br/>[Desktop Application Program](appxpkg/windows-desktop-application-program.md)<br/>[Windows containers](/virtualization/windowscontainers/about/) |

-->

<!--
:::row:::
    :::column:::
        ![User Interface and accessibility](/media/illustrations/bcs-partner-advanced-management-add-user-1.svg?branch=master)
        ### User Interface and accessibility
        * [Desktop User Interface](windows-application-ui-development.md)
        * [Windows and messages](winmsg/windowing.md)
        * [Desktop Window Manager](dwm/dwm-overview.md)
        * [Dialog boxes](dlgbox/dialog-boxes.md)
        * [Menus and other resources](menurc/resources.md)
        * [Data exchange](dataxchg/data-exchange.md)
        * [High DPI](hidpi/high-dpi-desktop-application-development-on-windows.md)
        * [Windows controls (Win32)](controls/window-controls.md)
        * [Desktop environment and shell](user-interface.md)
        * [Windows Property System](properties/windows-properties-system.md)
        * [Accessibility](accessibility.md)
    :::column-end:::
    :::column:::
        ![System and fundamentals](/media/illustrations/biztalk-get-started-get-started.svg?branch=master)
        ### System services and fundamentals
        * [System services](system-services.md)
        * [Component Object Model (COM)](com/component-object-model--com--portal.md)
        * [COM+](cossdk/component-services-portal.md)
        * [Structured storage](stg/structured-storage-start-page.md)
        * [Dynamic-link libraries](dlls/dynamic-link-libraries.md)
        * [Interprocess communications](ipc/interprocess-communications.md)
        * [Memory management](memory/memory-management.md)
        * [Power management](power/power-management-portal.md)
        * [Processes and threads](procthread/processes-and-threads.md)
        * [Services](services/services.md)
        * [Synchronization](sync/synchronization.md)
        * [Windows system information](sysinfo/windows-system-information.md)
    :::column-end:::
    :::column:::
        ![Audio, video, and graphics](/media/illustrations/virtualization-containers-samples.svg?branch=master)
        ### Audio, video, and graphics
        * [Audio and video technologies](audio-and-video.md)
        * [Core Audio APIs](coreaudio/core-audio-apis-in-windows-vista.md)
        * [DirectShow](directshow/directshow.md)
        * [Windows Multimedia](multimedia/windows-multimedia-start-page.md)
        * [Graphics and gaming technologies](graphics-and-multimedia.md)
        * [DirectX](directx.md)
        * [Direct2D](direct2d/direct2d-portal.md)
        * [Direct3D](direct3d.md)
        * [Windows GDI](gdi/windows-gdi.md)
        * [GDI+](gdiplus/-gdiplus-gdi-start.md)
        * [OpenGL](opengl/opengl.md)
        * [Windows Imaging Component](wic/-wic-lh.md)
    :::column-end:::
:::row-end:::
:::row:::
    :::column:::
        ![Networking and Internet](/media/illustrations/teams-voice-deployment.svg?branch=master)
        ### Networking and Internet
        * [Networking and Internet overview](networking.md)
        * [Remote Procedure Call](rpc/rpc-start-page.md)
        * [Delivery Optimization](delivery_optimization/delivery-optimization-portal.md)
        * [Network interfaces](network-interfaces.md)
        * [Network Management](netmgmt/network-management.md)
        * [Network Share Management](netshare/network-share-management.md)
        * [Windows Networking](wnet/windows-networking-wnet-.md)
        * [Windows Sockets 2](winsock/windows-sockets-start-page-2.md)
        * [Wireless Networking](wireless-networking.md)
    :::column-end:::
    :::column:::
        ![Data access and storage](/media/illustrations/azure-architecture-patterns.svg?branch=master)
        ### Data access and storage
        * [Data access and storage overview](data-access-and-storage.md)
        * [Local File Systems](fileio/file-systems.md)
        * [Distributed File System](dfs/distributed-file-system.md)
        * [Projected File System](projfs/projected-file-system.md)
        * [Cloud Sync Engines](cfapi/cloud-files-api-portal.md)
        * [Virtual Storage](VStor/virtual-storage.md)
        * [Background Intelligent Transfer Service](bits/background-intelligent-transfer-service-portal.md)
        * [Backup](backup.md)
    :::column-end:::
    :::column:::
        ![Devices, documents, and printing](/media/illustrations/virtualization-hperv-server-doc-archive.svg?branch=master)
        ### Devices, documents, and printing
        * [Devices overview](devices.md)
        * [Communications Resources](devio/communications-resources.md)
        * [Location API](locationapi/windows-location-api-portal.md)
        * [Sensor API](sensorsapi/portal.md)
        * [UPnP APIs](upnp/universal-plug-and-play-start-page.md)
        * [Windows Portable Devices](windows-portable-devices.md)
        * [Documents and Printing](printdocs/documents-and-printing.md)
    :::column-end:::
:::row-end:::
:::row:::
    :::column:::
        ![Security and identity](/media/illustrations/bcs-partner-advanced-management-password-3.svg?branch=master)
        ### Security and identity
        * [Security and identity overview](security.md)
        * [Antimalware Scan Interface](amsi/antimalware-scan-interface-portal.md)
        * [Authentication](secauthn/authentication-portal.md)
        * [Authorization](secauthz/authorization-portal.md)
        * [Certificate Enrollment API](seccertenroll/certenroll-portal.md)
        * [Cryptography (CNG)](seccng/cng-portal.md)
        * [Rights Management](SrvNodes/rights-management.md)
        * [Security Management](secmgmt/management-portal.md)
        * [TPM Base Services](tbs/tpm-base-services-portal.md)
        * [Windows Biometric Framework](secbiomet/biometric-service-api-portal.md)
    :::column-end:::
    :::column:::
        ![Diagnostics and testing](/media/illustrations/team-services-dev-ops-test.svg?branch=master)
        ### Diagnostics and testing
        * [Diagnostics overview](diagnostics.md)
        * [Debugging and error handling](debugging-and-error-handling.md)
        * [Network Monitor](netmon2/network-monitor.md)
        * [System Monitor](sysmon/system-monitor-portal.md)
        * [Performance counters](perfctrs/performance-counters-portal.md)
        * [Windows error reporting](wer/windows-error-reporting.md)
        * [Windows events](events/windows-events.md)
        * [TraceLogging](tracelogging/trace-logging-portal.md)
        * [Debugging tools for Windows](/windows-hardware/drivers/debugger/index)
    :::column-end:::
    :::column:::
        ![Packaging and installation](/media/illustrations/biztalk-host-integration-install-configure.svg?branch=master)
        ### Packaging and installation
        * [MSIX packaging and deployment](/windows/msix)
        * [Application Installation and Servicing](application-installing-and-servicing.md)
        * [Isolated Applications and Side-by-side Assemblies](sbscs/isolated-applications-and-side-by-side-assemblies-portal.md)
        * [Packaging, deployment, and query of UWP apps](appxpkg/appx-portal.md)
        * [Windows Installer](msi/windows-installer-portal.md)
        * [Windows Desktop Application Program](appxpkg/windows-desktop-application-program.md)
        * [Windows containers](/virtualization/windowscontainers/about/)
    :::column-end:::
:::row-end:::
-->
