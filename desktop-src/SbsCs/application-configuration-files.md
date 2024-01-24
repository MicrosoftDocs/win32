---
description: An application configuration file is an XML file used to control assembly binding.
ms.assetid: b7453f2b-52a4-4af9-8410-ebbb430ada67
title: Application Configuration Files
ms.topic: article
ms.date: 05/31/2018
---

# Application Configuration Files

An application configuration file is an XML file used to control assembly binding. It can redirect an application from using one version of a side-by-side assembly to another version of the same assembly. This is called [per-application configuration](per-application-configuration.md). An application configuration file applies only to a specific application manifest and dependent assemblies. Isolated components compiled with an embedded ISOLATIONAWARE\_MANIFEST\_RESOURCE\_ID manifest require a separate application configuration file. Manifests managed with [**CreateActCtx**](/windows/desktop/api/Winbase/nf-winbase-createactctxa) require a separate application configuration file.

The redirection specified by an application configuration file can override the assembly versions specified by [application manifests](application-manifests.md) and [publisher configuration files](publisher-configuration-files.md). For example, if a publisher configuration file specifies that all references to an assembly be redirected from version 1.0.0.0 to 1.1.0.0, an application configuration file can be used to redirect a particular application to use version 1.0.0.0. An application configuration file applies only to the specified application manifest and dependent assemblies.

For a complete listing of the XML schema, see [Application Configuration File Schema](application-configuration-file-schema.md).

Application configuration files have the elements and attributes shown in the following table.



| Element               | Attributes                | Required |
|-----------------------|---------------------------|----------|
| **configuration**     |                           | Yes      |
| **windows**           |                           | Yes      |
| **publisherPolicy**   |                           | Yes      |
|                       | **apply**                 | Yes      |
| **runtime**           |                           | No       |
| **assemblyBinding**   |                           | Yes      |
| **probing**           |                           | No       |
|                       | **privatePath**           | Yes      |
| **dependency**        |                           | No       |
| **dependentAssembly** |                           | Yes      |
| **assemblyIdentity**  |                           | Yes      |
|                       | **type**                  | Yes      |
|                       | **name**                  | Yes      |
|                       | **language**              | No       |
|                       | **processorArchitecture** | Yes      |
|                       | **version**               | Yes      |
|                       | **publicKeyToken**        | No       |
| **bindingRedirect**   |                           | Yes      |
|                       | **oldVersion**            | Yes      |
|                       | **newVersion**            | Yes      |



 

## File Location

Application configuration files must be installed in the same location as the application's [application manifest](application-manifests.md).

## File Name Syntax

The name of an application configuration file is the name of the application executable followed by .config.

For example, an application configuration file that refers to Example.exe or Example.dll would use the file name syntax shown in the following example. You can omit the field for <*resource ID*> if installing the configuration file as a separate file or if the resource ID is 1.

**example.exe.<*resource ID*>.config**

**example.dll.<*resource ID*>.config**

## Elements

Names of elements and attributes are case-sensitive. The values of elements and attributes are all case-insensitive, except for the value of the type attribute.

<span id="configuration"></span><span id="CONFIGURATION"></span>

### configuration

A container element for the **windows** and **runtime** elements of an application configuration file. Required.

<span id="windows"></span><span id="WINDOWS"></span>

### windows

Includes the parts of the application configuration file that apply to the redirection of Win32 assemblies.

> [!Note]  
> The author of an application should not include a configuration file with a **windows** subelement as part of their application. This may be permitted if the configuration file's only purpose is to enable the **privatePath** functionality of a **probing** element. The **probing** element is unavailable on systems earlier than Windows Server 2008 R2 and Windows 7.

<span id="publisherPolicy"></span><span id="publisherpolicy"></span><span id="PUBLISHERPOLICY"></span>

### publisherPolicy

Specifies whether to apply publisher policy.

This element has the attributes shown in the following table.



| Attribute | Description                                                                                                                     |
|-----------|---------------------------------------------------------------------------------------------------------------------------------|
| **apply** | A value of "yes" applies the publisher policy. This is the default setting. The value "no" does not apply the publisher policy. |

<span id="runtime"></span><span id="RUNTIME"></span>

### runtime

Includes the parts of the application configuration file that apply to redirection of .Net assemblies.

<span id="assemblyBinding"></span><span id="assemblybinding"></span><span id="ASSEMBLYBINDING"></span>

### assemblyBinding

Includes the redirection information for the application and the assembly affected by this application configuration file. The first subelement of **assemblyBinding** must be an **assemblyIdentity** that identifies the application.

Starting with Windows Server 2008 R2 and Windows 7 an **assemblyBinding** element can include a **probing** subelement.

<span id="probing"></span><span id="PROBING"></span>

### probing

An optional subelement of an **assemblyBinding** element that extends the search for assemblies into additional directories. The additional directories are not required to be subdirectories of the directory of the assembly.

> [!Note]  
> This element is unavailable on systems earlier than Windows Server 2008 R2 and Windows 7 and can only be used within a **windows** element.

This element has the attributes shown in the following table.

| Attribute       | Description                                                                                                                                                                                                                                   |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **privatePath** | Specifies the [relative paths](/windows/desktop/FileIO/naming-a-file) of subdirectories of the application's base directory that might contain assemblies. A maximum of nine subdirectory paths can be specified. Delimit each subdirectory path with a semicolon. |

You can use the double-dots special specifier in a path to denote the parent directory of the current directory. No more than two levels above the current directory can be specified using double-dots. Do not use triple-dots. For example, an application using the following **probing** element checks additional directories for an assembly.

``` XML
<probing privatePath="bin;..\bin2\subbin;bin3"/>
```

<span id="dependency"></span><span id="DEPENDENCY"></span>

### dependency
A container element for at least one **dependentAssembly**. Every **dependentAssembly** can be inside exactly one **dependency**. This element has no attributes. Optional.

<span id="dependentAssembly"></span><span id="dependentassembly"></span><span id="DEPENDENTASSEMBLY"></span>

### dependentAssembly

The first subelement must be an **assemblyIdentity** element that identifies the side-by-side assembly being redirected by the application configuration file. A **dependentAssembly** has no attributes.

<span id="assemblyIdentity"></span><span id="assemblyidentity"></span><span id="ASSEMBLYIDENTITY"></span>

### assemblyIdentity

As the first subelement of an **assemblyBinding** element, **assemblyIdentity** describes and uniquely identifies an application. The application configuration file redirects the binding of this application to side-by-side assemblies. For example, the following **assemblyIdentity** indicates that the application configuration file affects the binding of the application mysampleApp to side-by-side assemblies. The assemblies being redirected would be identified in a **dependentAssembly**.

``` XML
<assemblyIdentity processorArchitecture="X86" name="Microsoft.Windows.mysampleApp" type="win32" version="1.0.0.0"/>
```

As the first subelement of a **dependentAssembly** element, **assemblyIdentity** describes a side-by-side assembly on which the application depends. The application configuration file reconfigures the identity of this required assembly. For example, the following **assemblyIdentity** and **bindingRedirect** reconfigures a dependency on Microsoft.Windows.SampleAssembly from version 2.0.0.0 to version 2.1.0.0.

``` XML
<dependency>
      <dependentAssembly>
         <assemblyIdentity type="win32"
          name="Microsoft.Windows.SampleAssembly"
          processorArchitecture="x86"
          publicKeyToken="0000000000000000"/>
         <bindingRedirect oldVersion="2.0.0.0" newVersion="2.1.0.0"/>
      </dependentAssembly>
</dependency>
```

Note that every **assemblyIdentity** included in a **dependentAssembly** must exactly match the **assemblyIdentity** in the assembly's own [assembly manifest](assembly-manifests.md).

The **assemblyIdentity** element has the following attributes. It has no subelements.

| Attribute                 | Description                                                                                                                                                                                                                                                                                                          |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **type**                  | The value must be win32 (lower case). Required.                                                                                                                                                                                                                                                                      |
| **name**                  | The name attribute identifies the application being affected by the application configuration file or the assembly being redirected. Use the following format for the name: Organization.Division.Name. Required. For example: Microsoft.Windows.MysampleApp or Microsoft.Windows.MysampleAsm.<br/>            |
| **language**              | Identifies the language. Optional. For an **assemblyIdentity** referring to an assembly, if the assembly is language-specific, specify the DHTML language code. If the assembly is for worldwide use (language neutral) set the value as "\*".<br/>                                                            |
| **processorArchitecture** | Specifies the processor running the application.                                                                                                                                                                                                                                                                     |
| **version**               | Specifies the version of the application or assembly. Use four-part version syntax: mmmm.nnnn.oooo.pppp. Required.                                                                                                                                                                                                   |
| **publicKeyToken**        | For an **assemblyIdentity** referring to an assembly, a 16-character hexadecimal string representing the last 8 bytes of the SHA-1 hash of the public key under which the assembly is signed. The public key used to sign the catalog must be 2048 bits or greater. Required for all shared side-by-side assemblies. |

<span id="bindingRedirect"></span><span id="bindingredirect"></span><span id="BINDINGREDIRECT"></span>

### bindingRedirect

The **bindingRedirect** element contains redirection information for the binding of the assembly. Each **bindingRedirect** must be included in exactly one **dependentAssembly**. The four-part version syntax of the new version and the old version must specify the same major and minor versions.

This element has the attributes shown in the following table.

| Attribute      | Description                                                                                                                                                                                                                           |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **oldVersion** | Specifies the assembly version being overridden and redirected. Use the four-part version syntax nnnnn.nnnnn.nnnnn.nnnnn. Specify a range of versions by a dash without spaces. For example, 2.14.3.0 or 2.14.3.0 2.16.0.0. Required. |
| **newVersion** | Specifies the replacement assembly version. Use four-part version syntax nnnnn.nnnnn.nnnnn.nnnnn.                                                                                                                                     |

## Remarks

Application configuration files do not specify files.

## Example

``` XML
<bindingRedirect oldVersion="1.0.0.0" newVersion="1.0.10.0"/>
<bindingRedirect oldVersion="1.0.50.2011-1.0.60.65535" newVersion="1.0.70.0"/>
```
