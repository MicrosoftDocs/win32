---
title: About Platform Update for Windows Vista
description: Provides an overview of the Platform Update for Windows Vista and the Platform Update for Windows Server 2008 and their features.
ms.assetid: ec5f03ae-9454-4964-943f-f97821984254
keywords:
- Platform Update for Windows Server 2008
- Platform Update for Windows Vista
ms.topic: article
ms.date: 05/31/2018
---

# About Platform Update for Windows Vista

The Platform Update for Windows Vista and the Platform Update for Windows Server 2008 are end-user operating system updates that support the use of selected Windows 7 technologies on previous versions of the Windows operating system. The updates include a set of runtime libraries that enable application developers to target current releases, Windows 7 and Windows Server 2008 R2 as well as previous versions, Windows Vista and Windows Server 2008.

## Summary of Supported API by Technology

Each technology that is supported by the Platform Update for Windows Vista and the Platform Update for Windows Server 2008 updates includes a set of API that can be used in an application that targets previous version of Windows.

For more information about using APIs supported by the updates in an application that targets previous versions of Windows, see [Developing Application for Previous Versions of Windows](developing-applications-for-previous-versions-of-windows.md).

> [!Note]  
> Some APIs that are associated with a technology may not be supported and the behavior, performance, or requirements for some supported APIs may vary across Windows versions. For details about the supported API for a specific technology, click the link in one of the summary tables to go to the section about that technology.

 

### Technologies Supported with Platform Update for Windows Vista

For details about the supported API for a specific technology, click the link in one of the summary tables to go to the section about that technology.

The technologies that are supported for Windows Vista and Windows XP with the Platform Update for Windows Vista are shown in the following table.

| Technology                                                                                    | Windows Vista | Windows XP |
|-----------------------------------------------------------------------------------------------|---------------|------------|
| [Windows Automation API](#windows-automation-api)                                             | Yes           | Yes        |
| [Windows Graphics, Imaging and XPS Library](#windows-graphics-imaging-and-xps-library)        | Yes           | No         |
| [Windows Ribbon and Animation Manager Library](#windows-ribbon-and-animation-manager-library) | Yes           | No         |
| [Windows Portable Devices Platform](#windows-portable-devices-platform)                       | Yes           | No         |



 

### Technologies Supported with Platform Update for Windows Server 2008

For details about the supported API for a specific technology, click the link in one of the summary tables to go to the section about that technology.

The technologies that are supported for Windows Server 2008 and Windows Server 2003 with the Platform Update for Windows Server 2008 are shown in the following table.

| Technology                                                                                    | Windows Server 2008 | Windows Server 2003 |
|-----------------------------------------------------------------------------------------------|---------------------|---------------------|
| [Windows Automation API](#windows-automation-api)                                             | Yes                 | Yes                 |
| [Windows Graphics, Imaging and XPS Library](#windows-graphics-imaging-and-xps-library)        | Yes                 | No                  |
| [Windows Ribbon and Animation Manager Library](#windows-ribbon-and-animation-manager-library) | Yes                 | No                  |
| [Windows Portable Devices Platform](#windows-portable-devices-platform)                       | No                  | No                  |



 

## Descriptions of Supported API by Technology

For details about the supported API for a specific technology, click the link in one of the summary tables to go to the section about that technology.

-   [Windows Automation API](#windows-automation-api)
-   [Windows Graphics, Imaging and XPS Library](#windows-graphics-imaging-and-xps-library)
-   [Windows Ribbon and Animation Manager Library](#windows-ribbon-and-animation-manager-library)
-   [Windows Portable Devices Platform](#windows-portable-devices-platform)

### Windows Automation API

Windows Automation API 3.0 is a set of DLLs and API elements that enable Assistive Technology (AT) products to provide better computer access for individuals who have physical or cognitive difficulties, impairments, or disabilities. Additionally, because Windows Automation API 3.0 enables applications to access and manipulate the user interface (UI) elements of other applications, it is an ideal technology for implementing automated testing tools.

Microsoft Active Accessibility (MSAA) and UI Automation are similar in that both provide a means for exposing and collecting information about user interface elements and controls to support user interface accessibility and software test automation. UI Automation is a Windows implementation of the UI Automation specification. It is a newer technology that addresses many of the limitations of MSAA.

For more information about the Windows Automation API 3.0, see [Windows Automation API: Overview](/windows/desktop/WinAuto/windows-automation-api-overview).

The Platform Update for Windows Vista and the Platform Update for Windows Server 2008 support the following Windows Automation API 3.0:

-   [Microsoft Active Accessibility (MSAA)](#microsoft-active-accessibility-msaa)
-   [UI Automation](#ui-automation)

### Windows Editions Eligible for the Updates

The Platform Update for Windows Vista and the Platform Update for Windows Server 2008 enable Windows Automation API 3.0 support on the editions of Windows shown in the following table.



<table>
<thead>
<tr class="header">
<th>Windows Version</th>
<th>Editions Eligible for Update</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Windows Vista</td>
<td><dl> Starter with SP2 (x86)<br />
Home Basic with SP2 (x86 and amd64)<br />
Home Premium with SP2 (x86 and amd64)<br />
Business with SP2 (x86 and amd64)<br />
Enterprise with SP2 (x86 and amd64)<br />
Ultimate with SP2 (x86 and amd64)<br />
</dl></td>
</tr>
<tr class="even">
<td>Windows XP</td>
<td><dl> Windows XP Home with SP3 (x86)<br />
Windows XP Professional with SP3 (x86)<br />
</dl></td>
</tr>
<tr class="odd">
<td>Windows Server 2008</td>
<td><dl> Windows Server 2008 with SP2 (x86 and amd64)<br />
</dl></td>
</tr>
<tr class="even">
<td>Windows Server 2003</td>
<td><dl> Windows Server 2003 with SP2 (x86 and amd64)<br />
</dl></td>
</tr>
</tbody>
</table>



 

### Microsoft Active Accessibility (MSAA)

Microsoft Active Accessibility (MSAA) is a legacy technology that was first introduced with Windows 95. It is a set of APIs that improves the way Assistive Technology (AT) products work with applications running on Microsoft Windows. The API provide programming interfaces and methods for exposing information about user interface elements.

For more information about Microsoft Active Accessibility, see the [Technical Overview](/windows/desktop/WinAuto/technical-overview).

### Supported Microsoft Active Accessibility API Elements

All APIs are supported on previous versions of Windows that are eligible for the Platform Update for Windows Vista or the Platform Update for Windows Server 2008.

### UI Automation

UI Automation is a newer technology that implements the UI Automation specification and addresses many of the limitations of Microsoft Active Accessibility. It is a set of APIs that provides programmatic access to the user interface elements of applications. The provided API help Assistive Technology products and automated testing tools access, identify, and manipulate the standard and custom UI elements of an application.

For more information about UI Automation, see [Windows Automation API: UI Automation](../winauto/entry-uiauto-win32.md).

### Supported UI Automation API Elements

All APIs are supported on previous versions of Windows that are eligible for the Platform Update for Windows Vista or the Platform Update for Windows Server 2008.

### Running UI Automation on Previous Windows Versions

Because of differences in how the common controls and the Windows standard controls are implemented on different Windows versions, there might be slight differences in the information that the UI Automation proxies retrieve for these controls from one version to another.

### Windows Graphics, Imaging and XPS Library

The Platform Update for Windows Vista supports the following Windows 7 APIs from the Windows Graphics, Imaging, and XPS Library:

-   [Direct2D](#direct2d)
-   [Direct3D](#direct3d)
-   [DirectWrite](#directwrite)
-   [Packaging](#packaging)
-   [Windows Imaging Component](#windows-imaging-component)
-   [XPS Document](#xps-document)
-   [XPS Print](#xps-print)

### Windows Editions Eligible for the Updates

The Platform Update for Windows Vista and the Platform Update for Windows Server 2008 enable Windows Graphics, Imaging, and XPS Library support on the editions of Windows shown in the following table.



<table>
<thead>
<tr class="header">
<th>Windows Version</th>
<th>Editions Eligible for Update</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Windows Vista</td>
<td><dl> Starter with SP2 (x86)<br />
Home Basic with SP2 (x86 and amd64)<br />
Home Premium with SP2 (x86 and amd64)<br />
Business with SP2 (x86 and amd64)<br />
Enterprise with SP2 (x86 and amd64)<br />
Ultimate with SP2 (x86 and amd64)<br />
</dl></td>
</tr>
<tr class="even">
<td>Windows Server 2008</td>
<td><dl> Windows Server 2008 with SP2 (x86 and amd64)<br />
</dl></td>
</tr>
</tbody>
</table>



 

### Direct2D

The Direct2D API is a new hardware-accelerated, immediate-mode 2-D graphics API that provides high performance and high quality rendering for 2-D geometry, bitmaps, and text. The Direct2D API is designed to interoperate well with existing code that uses GDI, GDI+, or Direct3D.

For more information about Direct2D, see [About Direct2D](/windows/desktop/Direct2D/direct2d-overview).

### Supported Direct2D API Elements

All APIs are supported on previous versions of Windows that are eligible for the Platform Update for Windows Vista or the Platform Update for Windows Server 2008.

### Running Direct2D on Previous Windows Versions

If the WDDM 1.1 driver is missing on Windows Vista, the performance of Direct2D/GDI interoperability degrades.

### Direct3D

The Platform Update for Windows Vista provides BGRA surface support for Direct3D10 and Direct3D10.1 code-paths. Direct3D10Level9 enables Direct3D10 functionality to work on Direct3D9 hardware. Direct3D WARP10 is a performant software rasterizer for Direct3D10 applications. Direct3D11, the latest version of Direct3D, provides new capabilities such as improved multithreading support, tessellation, DirectCompute functionality, and dynamic shader linkage.

If you create applications that use Direct3D, the [DirectX SDK](/previous-versions/windows/apps/hh452744(v=win.10)) (https://msdn.microsoft.com/directx/aa937788.aspx) is required.

For more information about Direct3D, see [Direct3D](/previous-versions/windows/apps/hh452744(v=win.10)) (https://msdn.microsoft.com/directx/default.aspx).

### Supported Direct3D API Elements

All APIs are supported on previous versions of Windows that are eligible for the Platform Update for Windows Vista or the Platform Update for Windows Server 2008.

### DirectWrite

The DirectWrite API is a new text API that provides multiple layers of functionality, including text layout, script processing, glyph rendering, and the font system. DirectWrite uses OpenType fonts and sub-pixel ClearType rendering to enhance the text experience provided by applications. Text rendering is hardware-accelerated when used with Direct2D.

For more information about DirectWrite, see [Introducing DirectWrite](/windows/desktop/DirectWrite/introducing-directwrite).

### Supported DirectWrite API Elements

All APIs are supported on previous versions of Windows that are eligible for the Platform Update for Windows Vista or the Platform Update for Windows Server 2008.

### Running DirectWrite on Previous Windows Versions

The following behavioral issues may affect the use of DirectWrite API on previous Windows versions:

-   Scripts new to Windows 7 may not render entirely correctly on previous Windows versions.
-   Locales not available in previous Windows versions fall back to default behavior.
-   The ClearType Tuner is not available on previous Windows versions.
-   GDI interoperability has a higher memory cost in some scenarios on previous Windows versions.

### Packaging

The Platform Update for Windows Vista supports a limited subset of the Packaging APIs that are needed to perform tasks with the XPS Document API in unmanaged applications.

For more information about Packaging APIs, please see the [Packaging API Overview](/previous-versions/windows/desktop/opc/packaging-api-overview).

### Supported Packaging API Elements

Only the following Packaging interfaces are supported:

-   IOpcUri
-   IOpcPartUri
-   IOpcFactory (only the following methods are supported)
    -   CreatePackageRootUri
    -   CreatePartUri
    -   CreateStreamOnFile

Supported Packaging APIs can be used to create streams over files as well as to create and interact with package-based URI.

### Running Packaging API on Previous Windows Versions

The behavior and performance of supported Packaging interfaces and methods are the same on all supported platforms.

If an application attempts to instantiate or call an unsupported Packaging interface or method, the attempt will fail. If the call is to an unsupported [**IOpcFactory**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcfactory) method, the E\_NOTIMPL error code will be returned.

### Windows Imaging Component

New features for the Windows Imaging Component (WIC) include enhanced security, support for high color, and better metadata interoperability. In addition, the Windows Imaging Component broadens its standards compliance by providing support for progressive image decoding, expanded PNG features, GIF metadata, , HD Photo updates, and metadata that spans APPn segments.

For more information about the Windows Imaging Component, see the [Windows Imaging Component Overview](/windows/desktop/wic/-wic-about-windows-imaging-codec).

### Supported WIC API Elements

All APIs are supported on previous versions of Windows that are eligible for the Platform Update for Windows Vista or the Platform Update for Windows Server 2008.

### XPS Document

The XPS Document APIs support the creating, modifying, and saving of XPS Documents in unmanaged applications

For more information about XPS Document APIs, please see the [XPS Document Programming Guide.](/previous-versions//dd372978(v=vs.85))

### Supported XPS Document API Elements

Only the [XPS Digital Signatures](/previous-versions/windows/desktop/dd372947(v=vs.85)) interfaces are not supported on down-level OS versions.

### XPS Print

The XPS Print APIs support the printing of XPS documents from Windows-based applications.

For more information about XPS Print APIs, please see the [XpsPrint API](/windows/desktop/printdocs/xpsprint-api).

### Supported XPS Print API Elements

All APIs are supported on previous versions of Windows that are eligible for the Platform Update for Windows Vista or the Platform Update for Windows Server 2008.

### Windows Ribbon and Animation Manager Library

The Platform Update for Windows Vista supports the following Windows 7 APIs from the Windows Ribbon and Animation Library:

-   [Windows Ribbon Framework](#windows-ribbon-and-animation-manager-library)
-   [Windows Animation Manager](#windows-animation-manager)

### Windows Editions Eligible for the Updates

The Platform Update for Windows Vista and the Platform Update for Windows Server 2008 enable Windows Ribbon and Animation Manager Library support on the editions of Windows shown in the following table.



<table>
<thead>
<tr class="header">
<th>Windows Version</th>
<th>Editions Eligible for Update</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Windows Vista</td>
<td><dl> Starter with SP2 (x86)<br />
Home Basic with SP2 (x86 and amd64)<br />
Home Premium with SP2 (x86 and amd64)<br />
Business with SP2 (x86 and amd64)<br />
Enterprise with SP2 (x86 and amd64)<br />
Ultimate with SP2 (x86 and amd64)<br />
</dl></td>
</tr>
<tr class="even">
<td>Windows Server 2008</td>
<td><dl> Windows Server 2008 with SP2 (x86 and amd64)<br />
</dl></td>
</tr>
</tbody>
</table>



 

### Windows Ribbon Framework

The Windows Ribbon (Ribbon) framework is a rich command presentation system that provides a modern alternative to the layered menus, toolbars, and task panes of traditional Windows applications.

The framework is a collection of Microsoft Win32 APIs that provide a host of new user interface capabilities for Windows developers and includes both the Ribbon and a context menu system.

For more information about the Ribbon framework, see [Introducing the Windows Ribbon Framework](../windowsribbon/windowsribbon-introduction.md).

### Supported Ribbon Framework API Elements

All APIs are supported on previous versions of Windows that are eligible for the Platform Update for Windows Vista or the Platform Update for Windows Server 2008.

### Windows Animation Manager

The Windows Animation Manager (Windows Animation) is a programmatic interface that supports the animation of visual elements of Windows applications. Windows Animation is designed to simplify the development and maintenance of animation sequences and to enable developers to implement animations that are consistent and intuitive. Windows Animation can be used with any graphics platform including Direct2D, Direct3D, or GDI+.

Windows Animation is a single-threaded COM API that provides everything a developer needs to create, manage, and drive UI animation.

For more information about the Windows Animation Manager, see [Introducing Windows Animation](/windows/desktop/UIAnimation/introducing-windows-animation-manager).

### Supported Animation Manager API Elements

All APIs are supported on previous versions of Windows that are eligible for the Platform Update for Windows Vista or the Platform Update for Windows Server 2008.

### Windows Portable Devices Platform

The Platform Update for Windows Vista supports the Windows 7 extensions to the Windows Portable Devices (WPD) platform. This feature enables computers to communicate with attached media and storage devices. WPD provides a flexible, robust way for computers to communicate with digital cameras, music players, mobile phones, and many other types of connected devices.

For more information about Windows Portable Devices, see [Windows Portable Devices](/windows-hardware/drivers/portable/) (https://docs.microsoft.com/windows-hardware/drivers/portable/).

### Windows Editions Eligible for the Updates

The Platform Update for Windows Vista and the Platform Update for Windows Server 2008 enable Windows Portable Devices (WPD) support on the editions of Windows shown in the following table.



<table>
<thead>
<tr class="header">
<th>Windows Version</th>
<th>Editions Eligible for Update</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Windows Vista</td>
<td><dl> Starter with SP2 (x86)<br />
Home Basic with SP2 (x86 and amd64)<br />
Home Premium with SP2 (x86 and amd64)<br />
Business with SP2 (x86 and amd64)<br />
Enterprise with SP2 (x86 and amd64)<br />
Ultimate with SP2 (x86 and amd64)<br />
</dl></td>
</tr>
</tbody>
</table>



 

### Supported WPD API Elements

The following table identifies the features that are supported for the Windows 7, Windows Vista, and Windows Vista with Platform Update for Windows Vista versions of the Windows operating system.

| WPD Feature                    | Windows 7 | Windows Vista | Windows Vista with Platform Update for Windows Vista |
|--------------------------------|-----------|---------------|------------------------------------------------------|
| MTP over USB                   | Yes       | Yes           | Yes                                                  |
| MTP over IP                    | Yes       | Yes           | Yes                                                  |
| MTP over Bluetooth             | Yes       | No            | Yes                                                  |
| WPD and MTP Device Services    | Yes       | No            | Yes                                                  |
| WPD Automation                 | Yes       | No            | No                                                   |
| Multi-function/Multi-transport | Yes       | No            | No                                                   |
| Device Stage                   | Yes       | No            | No                                                   |
| Device Sync Platform           | Yes       | No            | No                                                   |



 

For editions of Windows 7 and Windows Vista that do not have Microsoft Windows Media Player installed by default (the N and KN editions), you must install the [Windows Media Format 11 SDK]( ../audio-and-video.md) (https://msdn.microsoft.com/windows/bb190326.aspx) to enable WPD functionality. For more information, see the [Knowledge Base article](https://support.microsoft.com/kb/953693) (https://go.microsoft.com/fwlink/p/?linkid=158715), which was originally published as a resolution for Windows Vista.

## Related topics

<dl> <dt>

[Platform Update for Windows Vista](platform-update-for-windows-vista-portal.md)
</dt> <dt>

**Overviews**
</dt> <dt>

[About Platform Update for Windows Vista](platform-update-for-windows-vista-overview.md)
</dt> <dt>

[Knowledge Base article about the Platform Update for Windows Vista (KB 971644)](https://support.microsoft.com/kb/971644)
</dt> </dl>

 

 