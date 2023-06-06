---
description: An application manifest is an XML file that describes and identifies the shared and private side-by-side assemblies that an application should bind to at run time.
ms.assetid: c5016251-db7a-4edc-9be9-3acb03d495f8
title: Application manifests
ms.topic: article
ms.date: 10/08/2020
ms.custom: 19H1
---

# Application manifests

An application manifest (also known as a side-by-side application manifest, or a *fusion* manifest) is an XML file that describes and identifies the shared and private side-by-side assemblies that an application should bind to at run time. These should be the same assembly versions that were used to test the application. Application manifests might also describe metadata for files that are private to the application.

For a complete listing of the XML schema, see [Manifest file schema](manifest-file-schema.md).

Application manifests have the following elements and attributes.

| Element                                                                     | Attributes                | Required |
|-----------------------------------------------------------------------------|---------------------------|----------|
| [**assembly**](#assembly)                                                   |                           | Yes      |
|                                                                             | **manifestVersion**       | Yes      |
| [**noInherit**](#noInherit)                                                 |                           | No       |
| [**assemblyIdentity**](#assemblyIdentity)                                   |                           | Yes      |
|                                                                             | **type**                  | Yes      |
|                                                                             | **name**                  | Yes      |
|                                                                             | **language**              | No       |
|                                                                             | **processorArchitecture** | No       |
|                                                                             | **version**               | Yes      |
|                                                                             | **publicKeyToken**        | No       |
| [**compatibility**](#compatibility)                                         |                           | No       |
| [**application**](#application)                                             |                           | No       |
| [**supportedOS**](#supportedOS)                                             | **Id**                    | No       |
| [**maxversiontested**](#maxversiontested)                                   | **Id**                    | No       |
| [**dependency**](#dependency)                                               |                           | No       |
| [**dependentAssembly**](#dependentAssembly)                                 |                           | No       |
| [**file**](#file)                                                           |                           | No       |
|                                                                             | **name**                  | No       |
|                                                                             | **hashalg**               | No       |
|                                                                             | **hash**                  | No       |
| [**activeCodePage**](#activeCodePage)                                       |                           | No       |
| [**autoElevate**](#autoElevate)                                             |                           | No       |
| [**disableTheming**](#disableTheming)                                       |                           | No       |
| [**disableWindowFiltering**](#disableWindowFiltering)                       |                           | No       |
| [**dpiAware**](#dpiAware)                                                   |                           | No       |
| [**dpiAwareness**](#dpiAwareness)                                           |                           | No       |
| [**gdiScaling**](#gdiScaling)                                               |                           | No       |
| [**highResolutionScrollingAware**](#highResolutionScrollingAware)           |                           | No       |
| [**longPathAware**](#longPathAware)                                         |                           | No       |
| [**printerDriverIsolation**](#printerDriverIsolation)                       |                           | No       |
| [**ultraHighResolutionScrollingAware**](#ultraHighResolutionScrollingAware) |                           | No       |
| [**msix**](#msix)                                                           |                           | No       |
| [**heapType**](#heaptype)                                                   |                           | No       |
| [**trustInfo**](#trustinfo)                                                   |                           | No       |

## File location

If possible, you should embed the application manifest as a resource in your application's `.exe` file or `.dll`. If you can't do that, then you can place the application manifest file in the same directory as the `.exe` or `.dll`.

For more info, see [Installing side-by-side assemblies](installing-side-by-side-assemblies.md).

## File name

By convention an application manifest should have the same name as your app's executable file, with the `.manifest` extension appended to it.

For example, an application manifest that refers to `example.exe` or `example.dll` should use the following file name syntax (if *resource ID* is 1, then you can omit the <*resource ID*> segment of the syntax).

**example.exe.<*resource ID*>.manifest**

**example.dll.<*resource ID*>.manifest**

## Elements

Names of elements and attributes are case-sensitive. The values of elements and attributes are case-insensitive, except for the value of the type attribute.

<span id="assembly"></span><span id="ASSEMBLY"></span>

### assembly

A container element. Its first subelement must be a **noInherit** or **assemblyIdentity** element. Required.

The **assembly** element must be in the namespace `urn:schemas-microsoft-com:asm.v1`. Child elements of the assembly must also be in this namespace, by inheritance or by tagging.

The **assembly** element has the following attributes.

| Attribute           | Description                                           |
|---------------------|-------------------------------------------------------|
| **manifestVersion** | The **manifestVersion** attribute must be set to `1.0`. |

<span id="noInherit"></span><span id="noinherit"></span><span id="NOINHERIT"></span>

### noInherit

Include this element in an application manifest to set the [activation contexts](activation-contexts.md) generated from the manifest with the "no inherit" flag. When this flag is not set in an activation context, and the activation context is active, it is inherited by new threads in the same process, windows, window procedures, and [Asynchronous Procedure Calls](/windows/desktop/Sync/asynchronous-procedure-calls). Setting this flag prevents the new object from inheriting the active context.

The **noInherit** element is optional and typically omitted. Most assemblies do not work correctly using a no-inherit activation context because the assembly must be explicitly designed to manage the propagation of their own activation context. The use of the **noInherit** element requires that any dependent assemblies referenced by the application manifest have a **noInherit** element in their [assembly manifest](assembly-manifests.md).

If **noInherit** is used in a manifest, it must be the first subelement of the **assembly** element. The **assemblyIdentity** element should come immediately after the **noInherit** element. If **noInherit** is not used, **assemblyIdentity** must be the first subelement of the **assembly** element. The **noInherit** element has no child elements. It is not a valid element in [assembly manifests](assembly-manifests.md).

<span id="assemblyIdentity"></span><span id="assemblyidentity"></span><span id="ASSEMBLYIDENTITY"></span>

### assemblyIdentity

As the first subelement of an **assembly** element, **assemblyIdentity** describes and uniquely identifies the application owning this application manifest. As the first subelement of a **dependentAssembly** element, **assemblyIdentity** describes a side-by-side assembly required by the application. Note that every assembly referenced in the application manifest requires an **assemblyIdentity** that exactly matches the **assemblyIdentity** in the referenced assembly's own assembly manifest.

The **assemblyIdentity** element has the following attributes. It has no subelements.

| Attribute                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                       |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **type**                  | Specifies the application or assembly type. The value must be `win32` and all in lower case. Required.                                                                                                                                                                                                                                                                                                                              |
| **name**                  | Uniquely names the application or assembly. Use the following format for the name: `Organization.Division.Name`. For example `Microsoft.Windows.mysampleApp`. Required.                                                                                                                                                                                                                                                               |
| **language**              | Identifies the language of the application or assembly. If the application or assembly is language-specific, specify the DHTML language code. In the **assemblyIdentity** of an application intended for worldwide use (language neutral) omit the language attribute.<br/>In an **assemblyIdentity** of an assembly intended for worldwide use (language neutral) set the value of language to `\*`. Optional.                    |
| **processorArchitecture** | Specifies the processor. Valid values include `x86`, `amd64`, `arm` and `arm64`. You can also specify `\*`, which ensures that all platforms are targeted. Optional.                                                                                                                                                                                                                                                            |
| **version**               | Specifies the application or assembly version. Use the four-part version format: `mmmmm.nnnnn.ooooo.ppppp`. Each of the parts separated by periods can be 0-65535 inclusive. For more information, see [Assembly Versions](assembly-versions.md). Required.                                                                                                                                                                        |
| **publicKeyToken**        | A 16-character hexadecimal string representing the last 8 bytes of the SHA-1 hash of the public key under which the application or assembly is signed. The public key used to sign the catalog must be 2048 bits or greater. Required for all shared side-by-side assemblies.                                                                                                                                                     |

<span id="compatibility"></span><span id="COMPATIBILITY"></span>

### compatibility

Contains at least one **application**. It has no attributes. Optional. Application manifests without a compatibility element default to Windows Vista compatibility on Windows 7.

<span id="application"></span><span id="APPLICATION"></span>

### application

Contains at least one **supportedOS** element. Starting in Windows 10, version 1903, it can also contain one optional **maxversiontested** element. It has no attributes. Optional.

<span id="supportedOS"></span><span id="supportedos"></span><span id="SUPPORTEDOS"></span>

### supportedOS

The **supportedOS** element has the following attribute. It has no subelements.

| Attribute | Description   |
|-----------|-----------------------|
| **Id**    | Set the Id attribute to **{e2011457-1546-43c5-a5fe-008deee3d3f0}** to run the application using Vista functionality. This can enable an application designed for Windows Vista to run on a later operating system. <br/> Set the Id attribute to **{35138b9a-5d96-4fbd-8e2d-a2440225f93a}** to run the application using Windows 7 functionality.<br/> Applications that support Windows Vista, Windows 7, and Windows 8 functionality do not require separate manifests. In this case, add the GUIDs for all the Windows operating systems.<br/> For info about the **Id** attribute behavior in Windows, see the [Windows 8 and Windows Server 2012 Compatibility Cookbook](https://www.microsoft.com/download/details.aspx?id=27416).<br/> The following GUIDs correspond with the indicated operating systems:<br/> **{8e0f7a12-bfb3-4fe8-b9a5-48fd50a15a9a}** -> Windows 10, Windows 11, Windows Server 2016, Windows Server 2019 and Windows Server 2022<br/> **{1f676c76-80e1-4239-95bb-83d0f6d0da78}** -> Windows 8.1 and Windows Server 2012 R2<br/> **{4a2f28e3-53b9-4441-ba9c-d69d4a4a6e38}** -> Windows 8 and Windows Server 2012<br/> **{35138b9a-5d96-4fbd-8e2d-a2440225f93a}** -> Windows 7 and Windows Server 2008 R2<br/> **{e2011457-1546-43c5-a5fe-008deee3d3f0}** -> Windows Vista and Windows Server 2008<br/> You can test this on Windows 7 or Windows 8.x by running Resource Monitor (resmon), going to the CPU tab, right-clicking on the column labels, "Select Column...", and check "Operating System Context". On Windows 8.x, you can also find this column available in the Task Manager (taskmgr). The content of the column shows the highest value found or "Windows Vista" as the default. <br/> |

<span id="maxVersionTested"></span><span id="maxversiontested"></span><span id="MAXVERSIONTESTED"></span>

### maxversiontested

The **maxversiontested** element specifies the versions of Windows that the application was tested against starting with the minimum OS version the application supports up to the maximum version. The complete set of versions can be found [here](https://developer.microsoft.com/windows/downloads/sdk-archive/). This is intended to be used by desktop applications that use [XAML Islands](/windows/apps/desktop/modernize/xaml-islands) and that are not deployed in an MSIX package. This element is supported in Windows 10, version 1903, and later versions.

The **maxversiontested** element has the following attribute. It has no subelements.

| Attribute | Description    |
|-----------|----------------|
| **Id**    | Set the Id attribute to a 4-part version string that specifies the maximum version of Windows that the application was tested against. For example, "10.0.18226.0". |

<span id="dependency"></span><span id="DEPENDENCY"></span>

### dependency

Contains at least one **dependentAssembly**. It has no attributes. Optional.

<span id="dependentAssembly"></span><span id="dependentassembly"></span><span id="DEPENDENTASSEMBLY"></span>

### dependentAssembly

The first subelement of **dependentAssembly** must be an **assemblyIdentity** element that describes a side-by-side assembly required by the application. Every **dependentAssembly** must be inside exactly one **dependency**. It has no attributes.

<span id="file"></span><span id="FILE"></span>

### file

Specifies files that are private to the application. Optional.

The **file** element has the attributes shown in the following table.

| Attribute   | Description                                                                                             |
|-------------|---------------------------------------------------------------------------------------------------------|
| **name**    | Name of the file. For example, Comctl32.dll.                                                            |
| **hashalg** | Algorithm used to create a hash of the file. This value should be SHA1.                                 |
| **hash**    | A hash of the file referred to by name. A hexadecimal string of length depending on the hash algorithm. |

<span id="activeCodePage"></span><span id="activecodepage"></span><span id="ACTIVECODEPAGE"></span>

### activeCodePage

On Windows 10, this element forces a process to use UTF-8 as the process code page. For more information, see [Use the UTF-8 code page](/windows/uwp/design/globalizing/use-utf8-code-page). On Windows 10, the only valid value for **activeCodePage** is **UTF-8**.

Starting in Windows 11, this element also allows selection of either the legacy non-UTF-8 code page, or code pages for a specific locale for legacy application compatibility. Modern applications are strongly encouraged to use Unicode. On Windows 11, **activeCodePage** may also be set to the value **Legacy** or a locale name such as **en-US** or **ja-JP**.

- On machines configured to a UTF-8 system active code page, **Legacy** will revert the process to the system locale code pages. If the system locale does not have defined code pages, then Windows-1252/437 will be used. The **Legacy** codepage setting is only supported in Fusion manifests and only beginning with Windows 11.
- When a locale name such as **en-US** is supplied, then the process code page will be set appropriately for that locale code page. For example, Windows-1252 and 437 for en-US, or 932 for ja-JP.

This element was first added in Windows 10 version 1903 (May 2019 Update). You can declare this property and target/run on earlier Windows builds, but you must handle legacy code page detection and conversion as usual. This element has no attributes. 

The following example demonstrates how to use this element to force the current process to use UTF-8 as the process code page.

```XML
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0" xmlns:asmv3="urn:schemas-microsoft-com:asm.v3">
 ...
  <asmv3:application>
    <asmv3:windowsSettings xmlns="http://schemas.microsoft.com/SMI/2019/WindowsSettings"> 
      <activeCodePage>UTF-8</activeCodePage> 
    </asmv3:windowsSettings>
  </asmv3:application>
 ...
</assembly>
```

<span id="autoElevate"></span><span id="autoelevate"></span><span id="AUTOELEVATE"></span>

### autoElevate

Specifies whether auto elevate is enabled. **TRUE** indicates that it is enabled. It has no attributes.
The executable file must be digitally signed by Windows Publisher. For internal use.

<span id="disableTheming"></span><span id="disabletheming"></span><span id="DISABLETHEMING"></span>

### disableTheming

Specifies whether giving UI elements a theme is disabled. **TRUE** indicates disabled. It has no attributes.

<span id="disableWindowFiltering"></span><span id="disablewindowfiltering"></span><span id="DISABLEWINDOWFILTERING"></span>

### disableWindowFiltering

Specifies whether to disable window filtering. **TRUE** disables window filtering so you can enumerate immersive windows from the desktop. **disableWindowFiltering** was added in Windows 8 and has no attributes.

```XML
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0" xmlns:asmv3="urn:schemas-microsoft-com:asm.v3">
 ...
  <asmv3:application>
    <asmv3:windowsSettings xmlns="http://schemas.microsoft.com/SMI/2011/WindowsSettings">
      <disableWindowFiltering>true</disableWindowFiltering>
    </asmv3:windowsSettings>
  </asmv3:application>
 ...
</assembly>
```

<span id="dpiAware"></span><span id="dpiaware"></span><span id="DPIAWARE"></span>

### dpiAware

Specifies whether the current process is dots per inch (dpi) aware.

**Windows 10, version 1607:** The **dpiAware** element is ignored if the **dpiAwareness** element is present. You can include both elements in a manifest if you want to specify a different behavior for Windows 10, version 1607 than for an earlier version of the operating system.

The following table describes the behavior that results based upon the presence of the **dpiAware** element and the text that it contains. The text within the element is not case-sensitive.

| State of the **dpiAware** element | Description     |
|-----------------------------------|---------|
| Absent                            | The current process is dpi unaware by default. You can programmatically change this setting by calling the [**SetProcessDpiAwareness**](/windows/desktop/api/shellscalingapi/nf-shellscalingapi-setprocessdpiawareness) or [**SetProcessDPIAware**](/windows/desktop/api/winuser/nf-winuser-setprocessdpiaware) function.                                                                                                                                                            |
| Contains "true"                   | The current process is system dpi aware.                                                                                                                                                                                                                                                                                                                                                          |
| Contains "false"                  | **Windows Vista, Windows 7 and Windows 8:** The behavior is the same as when the **dpiAware** is absent.<br/> **Windows 8.1 and Windows 10:** The current process is dpi unaware, and you cannot programmatically change this setting by calling the [**SetProcessDpiAwareness**](/windows/desktop/api/shellscalingapi/nf-shellscalingapi-setprocessdpiawareness) or [**SetProcessDPIAware**](/windows/desktop/api/winuser/nf-winuser-setprocessdpiaware) function.<br/> |
| Contains "true/pm"                | **Windows Vista, Windows 7 and Windows 8:** The current process is system dpi aware.<br/> **Windows 8.1 and Windows 10:** The current process is per-monitor dpi aware.<br/>                                                                                                                                                                                                          |
| Contains "per monitor"            | **Windows Vista, Windows 7 and Windows 8:** The behavior is the same as when the **dpiAware** is absent.<br/> **Windows 8.1 and Windows 10:** The current process is per-monitor dpi aware.<br/>                                                                                                                                                                                      |
| Contains any other string         | **Windows Vista, Windows 7 and Windows 8:** The behavior is the same as when the **dpiAware** is absent.<br/> **Windows 8.1 and Windows 10:** The current process is dpi unaware, and you cannot programmatically change this setting by calling the [**SetProcessDpiAwareness**](/windows/desktop/api/shellscalingapi/nf-shellscalingapi-setprocessdpiawareness) or [**SetProcessDPIAware**](/windows/desktop/api/winuser/nf-winuser-setprocessdpiaware) function.<br/> |

For more information about dpi awareness settings, see [High DPI Desktop Application Development on Windows](/windows/win32/hidpi/high-dpi-desktop-application-development-on-windows).

**dpiAware** has no attributes.

```XML
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0" xmlns:asmv3="urn:schemas-microsoft-com:asm.v3">
 ...
  <asmv3:application>
    <asmv3:windowsSettings xmlns="http://schemas.microsoft.com/SMI/2005/WindowsSettings">
      <dpiAware>true</dpiAware>
    </asmv3:windowsSettings>
  </asmv3:application>
 ...
</assembly>
```

<span id="dpiAwareness"></span><span id="dpiawareness"></span><span id="DPIAWARENESS"></span>

### dpiAwareness

Specifies whether the current process is dots per inch (dpi) aware.

The minimum version of the operating system that supports the **dpiAwareness** element is Windows 10, version 1607. For versions that support the **dpiAwareness** element, the **dpiAwareness** overrides the **dpiAware** element. You can include both elements in a manifest if you want to specify a different behavior for Windows 10, version 1607 than for an earlier version of the operating system.

The **dpiAwareness** element can contain a single item or a list of comma-separated items. In the latter case, the first (leftmost) item in the list recognized by the operating system is used. In this way, you can specify different behaviors supported in future Windows operating system versions.

The following table describes the behavior that results based upon the presence of the **dpiAwareness** element and the text that it contains in its leftmost recognized item. The text within the element is not case-sensitive.

| **dpiAwareness** element status:        | Description                          |
|-----------------------------------------|-------------------------------------------|
| Element is absent                       | The **dpiAware** element specifies whether the process is dpi aware.                                                                                                                                                                   |
| Contains no recognized items            | The current process is dpi unaware by default. You can programmatically change this setting by calling the [**SetProcessDpiAwareness**](/windows/desktop/api/shellscalingapi/nf-shellscalingapi-setprocessdpiawareness) or [**SetProcessDPIAware**](/windows/desktop/api/winuser/nf-winuser-setprocessdpiaware) function. |
| First recognized item is "system"       | The current process is system dpi aware.                                                                                                                                                                                               |
| First recognized item is "permonitor"   | The current process is per-monitor dpi aware.                                                                                                                                                                                          |
| First recognized item is "permonitorv2" | The current process uses the per-monitor-v2 dpi awareness context. This item will only be recognized on Windows 10 version 1703 or later.                                                                                              |
| First recognized item is "unaware"      | The current process is dpi unaware. You cannot programmatically change this setting by calling the [**SetProcessDpiAwareness**](/windows/desktop/api/shellscalingapi/nf-shellscalingapi-setprocessdpiawareness) or [**SetProcessDPIAware**](/windows/desktop/api/winuser/nf-winuser-setprocessdpiaware) function.      |

For more information about dpi awareness settings supported by this element, see [DPI\_AWARENESS](/windows/desktop/api/windef/ne-windef-dpi_awareness) and [DPI\_AWARENESS\_CONTEXT](/windows/desktop/hidpi/dpi-awareness-context).

**dpiAwareness** has no attributes.

```XML
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0" xmlns:asmv3="urn:schemas-microsoft-com:asm.v3">
 ...
  <asmv3:application>
    <asmv3:windowsSettings xmlns="http://schemas.microsoft.com/SMI/2016/WindowsSettings">
      <dpiAwareness>PerMonitorV2, unaware</dpiAwareness>
    </asmv3:windowsSettings>
  </asmv3:application>
 ...
</assembly>
```

<span id="gdiScaling"></span><span id="gdiscaling"></span><span id="GDISCALING"></span>

### gdiScaling

Specifies whether GDI scaling is enabled. The minimum version of the operating system that supports the **gdiScaling** element is Windows 10 version 1703.

The GDI (graphics device interface) framework can apply DPI scaling to primitives and text on a per-monitor basis without updates to the application itself. This can be useful for GDI applications no longer being actively updated.

Non-vector graphics (such as bitmaps, icons, or toolbars) cannot be scaled by this element. In addition, graphics and text appearing within bitmaps dynamically constructed by applications also cannot be scaled by this element.

**TRUE** indicates that this element is enabled. It has no attributes.


```XML
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0" xmlns:asmv3="urn:schemas-microsoft-com:asm.v3">
 ...
  <asmv3:application>
    <asmv3:windowsSettings xmlns="http://schemas.microsoft.com/SMI/2017/WindowsSettings">
      <gdiScaling>true</gdiScaling>
    </asmv3:windowsSettings>
  </asmv3:application>
 ...
</assembly>
```

<span id="highResolutionScrollingAware"></span><span id="highresolutionscrollingaware"></span><span id="HIGHRESOLUTIONSCROLLINGAWARE"></span>

### highResolutionScrollingAware

Specifies whether high-resolution-scrolling aware is enabled. **TRUE** indicates that it is enabled. It has no attributes.

<span id="longPathAware"></span><span id="longpathaware"></span><span id="LONGPATHAWARE"></span>

### longPathAware

Enables long paths that exceed **MAX_PATH** in length. This element is supported in Windows 10, version 1607, and later. For more information, see [this article](../fileio/maximum-file-path-limitation.md).

```XML
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0" xmlns:asmv3="urn:schemas-microsoft-com:asm.v3">
 ...
  <asmv3:application>
    <asmv3:windowsSettings xmlns:ws2="http://schemas.microsoft.com/SMI/2016/WindowsSettings">
      <ws2:longPathAware>true</ws2:longPathAware>
    </asmv3:windowsSettings>
  </asmv3:application>
 ...
</assembly>
```

<span id="printerDriverIsolation"></span><span id="printerdriverisolation"></span><span id="PRINTERDRIVERISOLATION"></span>

### printerDriverIsolation

Specifies whether printer driver isolation is enabled. **TRUE** indicates that it is enabled. It has no attributes. Printer driver isolation improves the reliability of the Windows print service by enabling printer drivers to run in processes that are separate from the process in which the print spooler runs. Support for printer driver isolation started in Windows 7 and Windows Server 2008 R2. An app can declare printer driver isolation in its app manifest to isolate itself from the printer driver and improve its reliability. That is, the app won't crash if the printer driver has an error.


```XML
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0" xmlns:asmv3="urn:schemas-microsoft-com:asm.v3">
 ...
  <asmv3:application>
    <asmv3:windowsSettings xmlns="http://schemas.microsoft.com/SMI/2011/WindowsSettings">
      <printerDriverIsolation>true</printerDriverIsolation>
    </asmv3:windowsSettings>
  </asmv3:application>
 ...
</assembly>
```

<span id="ultraHighResolutionScrollingAware"></span><span id="ultrahighresolutionscrollingaware"></span><span id="ULTRAHIGHRESOLUTIONSCROLLINGAWARE"></span>

### ultraHighResolutionScrollingAware

Specifies whether ultra-high-resolution-scrolling aware is enabled. **TRUE** indicates that it is enabled. It has no attributes.

<span id="msix"></span><span id="MSIX"></span>

### msix

Specifies the identity info of a package with external location for the current application (see [Grant package identity by packaging with external location](/windows/apps/desktop/modernize/grant-identity-to-nonpackaged-apps)). This element is supported in Windows 10, version 2004, and later versions.

The **msix** element must be in the namespace `urn:schemas-microsoft-com:msix.v1`. It has the attributes shown in the following table.

| Attribute   | Description                                                                                             |
|-------------|---------------------------------------------------------------------------------------------------------|
| **publisher**    | Describes the publisher information. This value must match the **Publisher** attribute in the [Identity](/uwp/schemas/appxpackage/uapmanifestschema/element-identity) element in the package manifest of your packaged app with external location. |
| **packageName** | Describes the contents of the package. This value must match the **Name** attribute in the [Identity](/uwp/schemas/appxpackage/uapmanifestschema/element-identity) element in the package manifest of your packaged app with external location.    |
| **applicationId**    | The unique identifier of the application. This value must match the **Id** attribute in the [Application](/uwp/schemas/appxpackage/uapmanifestschema/element-application) element in the package manifest of your packaged app with external location.  |

```xml
<?xml version="1.0" encoding="utf-8"?>
<assembly manifestVersion="1.0" xmlns="urn:schemas-microsoft-com:asm.v1">
  <assemblyIdentity version="1.0.0.0" name="Contoso.PhotoStoreApp"/>
  <msix xmlns="urn:schemas-microsoft-com:msix.v1"
          publisher="CN=Contoso"
          packageName="ContosoPhotoStore"
          applicationId="ContosoPhotoStore"
        />
</assembly>
```

### heapType

Overrides the default heap implementation for the [Win32 heap APIs](../Memory/heap-functions.md) to use.

* The value **SegmentHeap** indicates that segment heap will be used. Segment heap is a modern heap implementation that will generally reduce your overall memory usage. This element is supported in Windows 10, version 2004 (build 19041) and later.
* All other values are ignored.

This element has no attributes.

```XML
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0" xmlns:asmv3="urn:schemas-microsoft-com:asm.v3">
 ...
  <asmv3:application>
    <asmv3:windowsSettings xmlns="http://schemas.microsoft.com/SMI/2020/WindowsSettings">
      <heapType>SegmentHeap</heapType>
    </asmv3:windowsSettings>
  </asmv3:application>
 ...
</assembly>
```

### trustInfo

All UAC-compliant apps should have a requested execution level added to the application manifest. Requested execution levels specify the privileges required for an app. For more information, see [How User Account Control (UAC) Affects Your Application](/cpp/security/how-user-account-control-uac-affects-your-application). 

The requested execution level is specified with the **level** attribute of the **requestedExecutionLevel** descendent of the **trustInfo** element. Allowed values for **level** are:

| Value | Description |
|-------|-------------|
| asInvoker | The application runs at the same permission level as the process that started it. You can elevate the application to a higher permission level by selecting **Run as Administrator**. |
| requireAdministrator | The application runs using administrator permissions. The user who starts the application must be a member of the Administrators group. If the opening process isn't running with administrative permissions, the system prompts for credentials. |
| highestAvailable  |  The application runs at the highest permission level that it can. If the user who starts the application is a member of the Administrators group, this option is the same as `level='requireAdministrator'`. If the highest available permission level is higher than the level of the opening process, the system prompts for credentials. |

Setting the level to 'highestAvailable' ensures that the application will run successfully with both users who are members of the Administrators group and those who are not. If the application can only function with administrative access to the system, then marking the app with a requested execution level of 'requireAdministrator' ensures that the system identifies this program as an administrative app and performs the necessary elevation steps.

By default, the Visual C++ linker embeds a UAC fragment into the manifest of an application with an execution level of 'asInvoker'.

The **requestedExecutionLevel** element also has an attribute **uiAccess**. Set this value to true if you want the application to bypass user interface protection levels and drive input to higher-permission windows on the desktop; otherwise, `uiAccess='false'`. Defaults to uiAccess='false'. Set this argument to `uiAccess='true'` only for user interface accessibility applications. For more informatiom, see [Security Considerations for Assistive Technologies](/windows/win32/winauto/uiauto-securityoverview).

Specifying **requestedExecutionLevel** node will disable file and registry virtualization. If you want to utilize File and Registry Virtualization for backward compatibility then omit the **requestedExecutionLevel** node.

```xml
<trustInfo xmlns="urn:schemas-microsoft-com:asm.v2">
  <security>
    <requestedPrivileges xmlns="urn:schemas-microsoft-com:asm.v3">
      <requestedExecutionLevel level="asInvoker" uiAccess="false" />
    </requestedPrivileges>
  </security>
</trustInfo>
```

## Example

The following is an example of an application manifest for an application named MySampleApp.exe. The application consumes the SampleAssembly side-by-side assembly.

``` syntax
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">

  <compatibility xmlns="urn:schemas-microsoft-com:compatibility.v1"> 
      <application> 
            <!-- Windows 10 and Windows 11 -->
            <supportedOS Id="{8e0f7a12-bfb3-4fe8-b9a5-48fd50a15a9a}"/>
            <!-- Windows 8.1 -->
            <supportedOS Id="{1f676c76-80e1-4239-95bb-83d0f6d0da78}"/>
            <!-- Windows 8 -->
            <supportedOS Id="{4a2f28e3-53b9-4441-ba9c-d69d4a4a6e38}"/>
            <!-- Windows 7 -->
            <supportedOS Id="{35138b9a-5d96-4fbd-8e2d-a2440225f93a}"/>
            <!-- Windows Vista -->
            <supportedOS Id="{e2011457-1546-43c5-a5fe-008deee3d3f0}"/> 
      </application> 
  </compatibility>

  <assemblyIdentity type="win32" 
                    name="myOrganization.myDivision.mySampleApp" 
                    version="6.0.0.0" 
                    processorArchitecture="x86" 
                    publicKeyToken="0000000000000000"
  />
  <dependency>
    <dependentAssembly>
      <assemblyIdentity type="win32" 
                        name="Proseware.Research.SampleAssembly" 
                        version="6.0.0.0" 
                        processorArchitecture="x86" 
                        publicKeyToken="0000000000000000" 
                        language="*"
      />
    </dependentAssembly>
  </dependency>
</assembly>
```
