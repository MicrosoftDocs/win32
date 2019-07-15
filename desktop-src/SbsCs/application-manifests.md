---
Description: An application manifest is an XML file that describes and identifies the shared and private side-by-side assemblies that an application should bind to at run time.
ms.assetid: c5016251-db7a-4edc-9be9-3acb03d495f8
title: Application Manifests
ms.topic: article
ms.date: 04/19/2019
ms.custom: 19H1
---

# Application Manifests

An application manifest is an XML file that describes and identifies the shared and private side-by-side assemblies that an application should bind to at run time. These should be the same assembly versions that were used to test the application. Application manifests may also describe metadata for files that are private to the application.

For a complete listing of the XML schema, see [Manifest File Schema](manifest-file-schema.md).

Application manifests have the following elements and attributes.



| Element                               | Attributes                | Required |
|---------------------------------------|---------------------------|----------|
| **assembly**                          |                           | Yes      |
|                                       | **manifestVersion**       | Yes      |
| **noInherit**                         |                           | No       |
| **assemblyIdentity**                  |                           | Yes      |
|                                       | **type**                  | Yes      |
|                                       | **name**                  | Yes      |
|                                       | **language**              | No       |
|                                       | **processorArchitecture** | No       |
|                                       | **version**               | Yes      |
|                                       | **publicKeyToken**        | No       |
| **compatibility**                     |                           | No       |
| **application**                       |                           | No       |
| **supportedOS**                       | **Id**                    | No       |
| **maxversiontested**                  | **Id**                    | No       |
| **dependency**                        |                           | No       |
| **dependentAssembly**                 |                           | No       |
| **file**                              |                           | No       |
|                                       | **name**                  | No       |
|                                       | **hashalg**               | No       |
|                                       | **hash**                  | No       |
| **autoElevate**                       |                           | No       |
| **disableTheming**                    |                           | No       |
| **disableWindowFiltering**            |                           | No       |
| **dpiAware**                          |                           | No       |
| **dpiAwareness**                      |                           | No       |
| **gdiScaling**                        |                           | No       |
| **highResolutionScrollingAware**      |                           | No       |
| **magicFutureSetting**                |                           | No       |
| **printerDriverIsolation**            |                           | No       |
| **ultraHighResolutionScrollingAware** |                           |          |



 

## File Location

Application manifests should be included as a resource in the application's EXE file or DLL.

For more information, see [Installing Side-by-side Assemblies](installing-side-by-side-assemblies.md).

## File Name Syntax

The name of an application manifest file is the name of the application's executable followed by .manifest.

For example, an application manifest that refers to Example.exe or Example.dll would use the following file name syntax. You can omit the <*resource ID*> field if resource ID is 1.

<dl> example.exe.<resource ID>.manifest  
example.dll.<resource ID>.manifest  
</dl>

## Elements

Names of elements and attributes are case-sensitive. The values of elements and attributes are case-insensitive, except for the value of the type attribute.

<dl> <dt>

<span id="assembly"></span><span id="ASSEMBLY"></span>**assembly**
</dt> <dd>

A container element. Its first subelement must be a **noInherit** or **assemblyIdentity** element. Required.

The **assembly** element must be in the namespace "urn:schemas-microsoft-com:asm.v1". Child elements of the assembly must also be in this namespace, by inheritance or by tagging.

The **assembly** element has the following attributes.



| Attribute           | Description                                           |
|---------------------|-------------------------------------------------------|
| **manifestVersion** | The **manifestVersion** attribute must be set to 1.0. |



 

</dd> <dt>

<span id="noInherit"></span><span id="noinherit"></span><span id="NOINHERIT"></span>**noInherit**
</dt> <dd>

Include this element in an application manifest to set the [activation contexts](activation-contexts.md) generated from the manifest with the "no inherit" flag. When this flag is not set in an activation context, and the activation context is active, it is inherited by new threads in the same process, windows, window procedures, and [Asynchronous Procedure Calls](https://docs.microsoft.com/windows/desktop/Sync/asynchronous-procedure-calls). Setting this flag prevents the new object from inheriting the active context.

The **noInherit** element is optional and typically omitted. Most assemblies do not work correctly using a no-inherit activation context because the assembly must be explicitly designed to manage the propagation of their own activation context. The use of the **noInherit** element requires that any dependent assemblies referenced by the application manifest have a **noInherit** element in their [assembly manifest](assembly-manifests.md).

If **noInherit** is used in a manifest, it must be the first subelement of the **assembly** element. The **assemblyIdentity** element should come immediately after the **noInherit** element. If **noInherit** is not used, **assemblyIdentity** must be the first subelement of the **assembly** element. The **noInherit** element has no child elements. It is not a valid element in [assembly manifests](assembly-manifests.md).

</dd> <dt>

<span id="assemblyIdentity"></span><span id="assemblyidentity"></span><span id="ASSEMBLYIDENTITY"></span>**assemblyIdentity**
</dt> <dd>

As the first subelement of an **assembly** element, **assemblyIdentity** describes and uniquely identifies the application owning this application manifest. As the first subelement of a **dependentAssembly** element, **assemblyIdentity** describes a side-by-side assembly required by the application. Note that every assembly referenced in the application manifest requires an **assemblyIdentity** that exactly matches the **assemblyIdentity** in the referenced assembly's own assembly manifest.

The **assemblyIdentity** element has the following attributes. It has no subelements.



| Attribute                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                       |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **type**                  | Specifies the application or assembly type. The value must be Win32 and all in lower case. Required.                                                                                                                                                                                                                                                                                                                              |
| **name**                  | Uniquely names the application or assembly. Use the following format for the name: Organization.Division.Name. For example Microsoft.Windows.mysampleApp. Required.                                                                                                                                                                                                                                                               |
| **language**              | Identifies the language of the application or assembly. Optional. If the application or assembly is language-specific, specify the DHTML language code. In the **assemblyIdentity** of an application intended for worldwide use (language neutral) omit the language attribute.<br/> In an **assemblyIdentity** of an assembly intended for worldwide use (language neutral) set the value of language to "\*".<br/> |
| **processorArchitecture** | Specifies the processor. The valid values are x86 for 32-bit Windows and ia64 for 64-bit Windows. Optional.                                                                                                                                                                                                                                                                                                                       |
| **version**               | Specifies the application or assembly version. Use the four-part version format: mmmmm.nnnnn.ooooo.ppppp. Each of the parts separated by periods can be 0-65535 inclusive. For more information, see [Assembly Versions](assembly-versions.md). Required.                                                                                                                                                                        |
| **publicKeyToken**        | A 16-character hexadecimal string representing the last 8 bytes of the SHA-1 hash of the public key under which the application or assembly is signed. The public key used to sign the catalog must be 2048 bits or greater. Required for all shared side-by-side assemblies.                                                                                                                                                     |



 

</dd> <dt>

<span id="compatibility"></span><span id="COMPATIBILITY"></span>**compatibility**
</dt> <dd>

Contains at least one **application**. It has no attributes. Optional. Application manifests without a compatibility element default to Windows Vista compatibility on Windows 7.

</dd> <dt>

<span id="application"></span><span id="APPLICATION"></span>**application**
</dt> <dd>

Contains at least one **supportedOS** element. Starting in Windows 10, version 1903, it can also contain one optional **maxversiontested** element. It has no attributes. Optional.

</dd> <dt>

<span id="supportedOS"></span><span id="supportedos"></span><span id="SUPPORTEDOS"></span>**supportedOS**
</dt> <dd>

The **supportedOS** element has the following attribute. It has no subelements.



| Attribute | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Id**    | Set the Id attribute to **{e2011457-1546-43c5-a5fe-008deee3d3f0}** to run the application using Vista functionality. This can enable an application designed for Windows Vista to run on a later operating system. <br/> Set the Id attribute to **{35138b9a-5d96-4fbd-8e2d-a2440225f93a}** to run the application using Windows 7 functionality.<br/> Applications that support Windows Vista, Windows 7, and Windows 8 functionality do not require separate manifests. In this case, add the GUIDs for all the Windows operating systems.<br/> For info about the **Id** attribute behavior in Windows, see the [Windows 8 and Windows Server 2012 Compatibility Cookbook](https://www.microsoft.com/download/details.aspx?id=27416).<br/> The following GUIDs correspond with the indicated operating systems:<br/> **{8e0f7a12-bfb3-4fe8-b9a5-48fd50a15a9a}** -> Windows 10 and Windows Server 2016<br/> **{1f676c76-80e1-4239-95bb-83d0f6d0da78}** -> Windows 8.1 and Windows Server 2012 R2<br/> **{4a2f28e3-53b9-4441-ba9c-d69d4a4a6e38}** -> Windows 8 and Windows Server 2012<br/> **{35138b9a-5d96-4fbd-8e2d-a2440225f93a}** -> Windows 7 and Windows Server 2008 R2<br/> **{e2011457-1546-43c5-a5fe-008deee3d3f0}** -> Windows Vista and Windows Server 2008<br/> You can test this on Windows 7 or Windows 8.x by running Resource Monitor (resmon), going to the CPU tab, right-clicking on the column labels, "Select Column...", and check "Operating System Context". On Windows 8.x, you can also find this column available in the Task Manager (taskmgr). The content of the column shows the highest value found or "Windows Vista" as the default. <br/> |
</dd> <dt>

<span id="maxVersionTested"></span><span id="maxversiontested"></span><span id="MAXVERSIONTESTED"></span>**maxversiontested**
</dt> <dd>

The **maxversiontested** element specifies the maximum version of Windows that the application was tested against. This is intended to be used by desktop applications that are not deployed in an MSIX package. This element is supported in Windows 10, version 1903, and later versions.

The **maxversiontested** element has the following attribute. It has no subelements.

| Attribute | Description    |
|-----------|----------------|
| **Id**    | Set the Id attribute to a 4-part version string that specifies the maximum version of Windows that the application was tested against. For example, "10.0.18226.0". |
</dd> <dt>

<span id="dependency"></span><span id="DEPENDENCY"></span>**dependency**
</dt> <dd>

Contains at least one **dependentAssembly**. It has no attributes. Optional.

</dd> <dt>

<span id="dependentAssembly"></span><span id="dependentassembly"></span><span id="DEPENDENTASSEMBLY"></span>**dependentAssembly**
</dt> <dd>

The first subelement of **dependentAssembly** must be an **assemblyIdentity** element that describes a side-by-side assembly required by the application. Every **dependentAssembly** must be inside exactly one **dependency**. It has no attributes.

</dd> <dt>

<span id="file"></span><span id="FILE"></span>**file**
</dt> <dd>

Specifies files that are private to the application. Optional.

The **file** element has the attributes shown in the following table.



| Attribute   | Description                                                                                             |
|-------------|---------------------------------------------------------------------------------------------------------|
| **name**    | Name of the file. For example, Comctl32.dll.                                                            |
| **hashalg** | Algorithm used to create a hash of the file. This value should be SHA1.                                 |
| **hash**    | A hash of the file referred to by name. A hexadecimal string of length depending on the hash algorithm. |



 

</dd> <dt>

<span id="autoElevate"></span><span id="autoelevate"></span><span id="AUTOELEVATE"></span>**autoElevate**
</dt> <dd>

Specifies whether auto elevate is enabled. **TRUE** indicates that it is enabled. It has no attributes.

</dd> <dt>

<span id="disableTheming"></span><span id="disabletheming"></span><span id="DISABLETHEMING"></span>**disableTheming**
</dt> <dd>

Specifies whether giving UI elements a theme is disabled. **TRUE** indicates disabled. It has no attributes.

</dd> <dt>

<span id="disableWindowFiltering"></span><span id="disablewindowfiltering"></span><span id="DISABLEWINDOWFILTERING"></span>**disableWindowFiltering**
</dt> <dd>

Specifies whether to disable window filtering. **TRUE** disables window filtering so you can enumerate immersive windows from the desktop. **disableWindowFiltering** was added in Windows 8 and has no attributes.


```XML
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0" xmlns:asmv3="urn:schemas-microsoft-com:asm.v3" >
 ...
  <asmv3:application>
    <asmv3:windowsSettings xmlns="https://schemas.microsoft.com/SMI/2011/WindowsSettings">
      <disableWindowFiltering>true</disableWindowFiltering>
    </asmv3:windowsSettings>
  </asmv3:application>
 ...
</assembly>
```



</dd> <dt>

<span id="dpiAware"></span><span id="dpiaware"></span><span id="DPIAWARE"></span>**dpiAware**
</dt> <dd>

Specifies whether the current process is dots per inch (dpi) aware.

**Windows 10, version 1607:** The **dpiAware** element is ignored if the **dpiAwareness** element is present. You can include both elements in a manifest if you want to specify a different behavior for Windows 10, version 1607 than for an earlier version of the operating system.

The following table describes the behavior that results based upon the presence of the **dpiAware** element and the text that it contains. The text within the element is not case-sensitive.



| State of the **dpiAware** element | Description                                                                                                                                                                                                                                                                                                                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Absent                            | The current process is dpi unaware by default. You can programmatically change this setting by calling the [**SetProcessDpiAwareness**](https://docs.microsoft.com/windows/desktop/api/shellscalingapi/nf-shellscalingapi-setprocessdpiawareness) or [**SetProcessDPIAware**](https://docs.microsoft.com/windows/desktop/api/winuser/nf-winuser-setprocessdpiaware) function.                                                                                                                                                            |
| Contains "true"                   | The current process is system dpi aware.                                                                                                                                                                                                                                                                                                                                                          |
| Contains "false"                  | **Windows Vista, Windows 7 and Windows 8:** The behavior is the same as when the **dpiAware** is absent.<br/> **Windows 8.1 and Windows 10:** The current process is dpi unaware, and you cannot programmatically change this setting by calling the [**SetProcessDpiAwareness**](https://docs.microsoft.com/windows/desktop/api/shellscalingapi/nf-shellscalingapi-setprocessdpiawareness) or [**SetProcessDPIAware**](https://docs.microsoft.com/windows/desktop/api/winuser/nf-winuser-setprocessdpiaware) function.<br/> |
| Contains "true/pm"                | **Windows Vista, Windows 7 and Windows 8:** The current process is system dpi aware.<br/> **Windows 8.1 and Windows 10:** The current process is per-monitor dpi aware.<br/>                                                                                                                                                                                                          |
| Contains "per monitor"            | **Windows Vista, Windows 7 and Windows 8:** The behavior is the same as when the **dpiAware** is absent.<br/> **Windows 8.1 and Windows 10:** The current process is per-monitor dpi aware.<br/>                                                                                                                                                                                      |
| Contains any other string         | **Windows Vista, Windows 7 and Windows 8:** The behavior is the same as when the **dpiAware** is absent.<br/> **Windows 8.1 and Windows 10:** The current process is dpi unaware, and you cannot programmatically change this setting by calling the [**SetProcessDpiAwareness**](https://docs.microsoft.com/windows/desktop/api/shellscalingapi/nf-shellscalingapi-setprocessdpiawareness) or [**SetProcessDPIAware**](https://docs.microsoft.com/windows/desktop/api/winuser/nf-winuser-setprocessdpiaware) function.<br/> |



 

For more information about dpi awareness settings, see [Comparison of DPI Awareness Levels](https://msdn.microsoft.com/library/windows/desktop/mt843498(v=vs.85).aspx(d=robot)).

**dpiAware** has no attributes.


```XML
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0" xmlns:asmv3="urn:schemas-microsoft-com:asm.v3" >
 ...
  <asmv3:application>
    <asmv3:windowsSettings xmlns="https://schemas.microsoft.com/SMI/2005/WindowsSettings">
      <dpiAware>true</dpiAware>
    </asmv3:windowsSettings>
  </asmv3:application>
 ...
</assembly>
```



</dd> <dt>

<span id="dpiAwareness"></span><span id="dpiawareness"></span><span id="DPIAWARENESS"></span>**dpiAwareness**
</dt> <dd>

Specifies whether the current process is dots per inch (dpi) aware.

The minimum version of the operating system that supports the **dpiAwareness** element is Windows 10, version 1607. For versions that support the **dpiAwareness** element, the **dpiAwareness** overrides the **dpiAware** element. You can include both elements in a manifest if you want to specify a different behavior for Windows 10, version 1607 than for an earlier version of the operating system.

The **dpiAwareness** element can contain a single item or a list of comma-separated items. In the latter case, the first (leftmost) item in the list recognized by the operating system is used. In this way, you can specify different behaviors supported in future Windows operating system versions.

The following table describes the behavior that results based upon the presence of the **dpiAwareness** element and the text that it contains in its leftmost recognized item. The text within the element is not case-sensitive.



| **dpiAwareness** element status:        | Description                                                                                                                                                                                                                            |
|-----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Element is absent                       | The **dpiAware** element specifies whether the process is dpi aware.                                                                                                                                                                   |
| Contains no recognized items            | The current process is dpi unaware by default. You can programmatically change this setting by calling the [**SetProcessDpiAwareness**](https://docs.microsoft.com/windows/desktop/api/shellscalingapi/nf-shellscalingapi-setprocessdpiawareness) or [**SetProcessDPIAware**](https://docs.microsoft.com/windows/desktop/api/winuser/nf-winuser-setprocessdpiaware) function. |
| First recognized item is "system"       | The current process is system dpi aware.                                                                                                                                                                                               |
| First recognized item is "permonitor"   | The current process is per-monitor dpi aware.                                                                                                                                                                                          |
| First recognized item is "permonitorv2" | The current process uses the per-monitor-v2 dpi awareness context. This item will only be recognized on Windows 10 version 1703 or later.                                                                                              |
| First recognized item is "unaware"      | The current process is dpi unaware. You**cannot** programmatically change this setting by calling the [**SetProcessDpiAwareness**](https://docs.microsoft.com/windows/desktop/api/shellscalingapi/nf-shellscalingapi-setprocessdpiawareness) or [**SetProcessDPIAware**](https://docs.microsoft.com/windows/desktop/api/winuser/nf-winuser-setprocessdpiaware) function.      |



 

For more information about dpi awareness settings supported by this element, see [DPI\_AWARENESS](https://docs.microsoft.com/windows/desktop/api/windef/ne-windef-dpi_awareness) and [DPI\_AWARENESS\_CONTEXT](https://docs.microsoft.com/windows/desktop/hidpi/dpi-awareness-context).

**dpiAwareness** has no attributes.


```XML
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0" xmlns:asmv3="urn:schemas-microsoft-com:asm.v3" >
 ...
  <asmv3:application>
    <asmv3:windowsSettings xmlns="https://schemas.microsoft.com/SMI/2016/WindowsSettings">
      <dpiAwareness>PerMonitorV2, unaware</dpiAwareness>
    </asmv3:windowsSettings>
  </asmv3:application>
 ...
</assembly>
```



</dd> <dt>

<span id="gdiScaling"></span><span id="gdiscaling"></span><span id="GDISCALING"></span>**gdiScaling**
</dt> <dd>

Specifies whether GDI scaling is enabled. The minimum version of the operating system that supports the **gdiScaling** element is Windows 10 version 1703.

The GDI (graphics device interface) framework can apply DPI scaling to primitives and text on a per-monitor basis without updates to the application itself. This can be useful for GDI applications no longer being actively updated.

Non-vector graphics (such as bitmaps, icons, or toolbars) cannot be scaled by this element. In addition, graphics and text appearing within bitmaps dynamically constructed by applications also cannot be scaled by this element.

**TRUE** indicates that this element is enabled. It has no attributes.


```XML
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0" xmlns:asmv3="urn:schemas-microsoft-com:asm.v3" >
 ...
  <asmv3:application>
    <asmv3:windowsSettings xmlns="https://schemas.microsoft.com/SMI/2017/WindowsSettings">
      <gdiScaling>true</gdiScaling>
    </asmv3:windowsSettings>
  </asmv3:application>
 ...
</assembly>
```



</dd> <dt>

<span id="highResolutionScrollingAware"></span><span id="highresolutionscrollingaware"></span><span id="HIGHRESOLUTIONSCROLLINGAWARE"></span>**highResolutionScrollingAware**
</dt> <dd>

Specifies whether high-resolution-scrolling aware is enabled. **TRUE** indicates that it is enabled. It has no attributes.

</dd> <dt>

<span id="magicFutureSetting"></span><span id="magicfuturesetting"></span><span id="MAGICFUTURESETTING"></span>**magicFutureSetting**
</dt> <dd>

Specifies whether magic-future setting is enabled. **TRUE** indicates that it is enabled. It has no attributes.

</dd> <dt>

<span id="printerDriverIsolation"></span><span id="printerdriverisolation"></span><span id="PRINTERDRIVERISOLATION"></span>**printerDriverIsolation**
</dt> <dd>

Specifies whether printer driver isolation is enabled. **TRUE** indicates that it is enabled. It has no attributes. Printer driver isolation improves the reliability of the Windows print service by enabling printer drivers to run in processes that are separate from the process in which the print spooler runs. Support for printer driver isolation started in Windows 7 and Windows Server 2008 R2. An app can declare printer driver isolation in its app manifest to isolate itself from the printer driver and improve its reliability. That is, the app won't crash if the printer driver has an error.


```XML
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0" xmlns:asmv3="urn:schemas-microsoft-com:asm.v3" >
 ...
  <asmv3:application>
    <asmv3:windowsSettings xmlns="https://schemas.microsoft.com/SMI/2011/WindowsSettings">
      <printerDriverIsolation>true</printerDriverIsolation>
    </asmv3:windowsSettings>
  </asmv3:application>
 ...
</assembly>
```



</dd> <dt>

<span id="ultraHighResolutionScrollingAware"></span><span id="ultrahighresolutionscrollingaware"></span><span id="ULTRAHIGHRESOLUTIONSCROLLINGAWARE"></span>**ultraHighResolutionScrollingAware**
</dt> <dd>

Specifies whether ultra-high-resolution-scrolling aware is enabled. **TRUE** indicates that it is enabled. It has no attributes.

</dd> </dl>

## Example

The following is an example of an application manifest for an application named MySampleApp.exe. The application consumes the SampleAssembly side-by-side assembly.

``` syntax
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">

  <compatibility xmlns="urn:schemas-microsoft-com:compatibility.v1"> 
      <application> 
        <!--This Id value indicates the application supports Windows Vista functionality -->
          <supportedOS Id="{e2011457-1546-43c5-a5fe-008deee3d3f0}"/> 
        <!--This Id value indicates the application supports Windows 7 functionality-->
          <supportedOS Id="{35138b9a-5d96-4fbd-8e2d-a2440225f93a}"/>
        <!--This Id value indicates the application supports Windows 8 functionality-->
          <supportedOS Id="{4a2f28e3-53b9-4441-ba9c-d69d4a4a6e38}"/>
        <!--This Id value indicates the application supports Windows 8.1 functionality-->
          <supportedOS Id="{1f676c76-80e1-4239-95bb-83d0f6d0da78}"/>
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
                        processorArchitecture="X86" 
                        publicKeyToken="0000000000000000" 
                        language="*"
      />
    </dependentAssembly>
  </dependency>
</assembly>
```

 

 




