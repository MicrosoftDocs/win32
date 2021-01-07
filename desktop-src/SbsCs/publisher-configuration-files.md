---
description: A publisher configuration file is an XML file that globally redirects applications and assemblies from using one version of a side-by-side assembly to another version of the same assembly.
ms.assetid: b10752af-80a7-4027-b525-90333d0d010a
title: Publisher Configuration Files
ms.topic: article
ms.date: 05/31/2018
---

# Publisher Configuration Files

A publisher configuration file is an XML file that globally redirects applications and assemblies from using one version of a side-by-side assembly to another version of the same assembly. Typically, the publisher of the assembly issues a compatible update or security fix on a per-assembly basis by issuing a publisher configuration file to be installed along with a service pack update. This is referred to as [publisher configuration](publisher-configuration.md). For more information about this type of [configuration](configuration.md) see Publisher Configuration.

Publisher configuration files have the following elements and attributes. For a complete listing of the XML schema, see [Publisher Configuration File Schema](publisher-configuration-file-schema.md).



| Element               | Attributes                | Required |
|-----------------------|---------------------------|----------|
| **assembly**          |                           | Yes      |
|                       | **manifestVersion**       | Yes      |
| **assemblyIdentity**  |                           | Yes      |
|                       | **type**                  | Yes      |
|                       | **name**                  | Yes      |
|                       | **language**              | No       |
|                       | **processorArchitecture** | No       |
|                       | **version**               | Yes      |
|                       | **publicKeyToken**        | No       |
| **dependency**        |                           | No       |
| **dependentAssembly** |                           | No       |
| **bindingRedirect**   |                           | Yes      |
|                       | **oldVersion**            | Yes      |
|                       | **newVersion**            | Yes      |



 

## File Location

Publisher configuration files must be installed in the WinSxS folder. They are commonly installed as a separate file but publisher configuration files can also be included as a resource in a DLL. A publisher configuration file cannot be included as a resource in an EXE file. An EXE file may include an [application manifest](application-manifests.md) as a resource.

## File Name Syntax

The file name of a publisher configuration file has the form *policy*.*major*.*minor*.*assemblyname* where *major* and *minor* refer to the major and minor parts of the [assembly version](assembly-versions.md) that is being affected. The *assemblyname* refers to the name of the assembly.

For example, a publisher configuration file for version 6.0 of the Microsoft.Windows.Common-Controls assembly would have the following name:

<dl> policy.6.0.Microsoft.Windows.Common-Controls  
</dl>

Do not use policy configuration files to increment the major or minor version of an assembly. For example, do not redirect version 6.0.0.0 to 7.0.0.0 or 6.1.0.0. When an application references an assembly version, such as 6.0.0.0, side-by-side checks for the presence of any policy configuration files with the specified major and minor versions, e.g. 6.0. The application is then redirected to another version of the assembly, for example 6.0.1.0. If a publisher configuration file increments the major or minor version of an assembly, subsequent redirection of the assembly may require issuing multiple policy configuration files.

## Elements

<dl> <dt>

<span id="assembly"></span><span id="ASSEMBLY"></span>**assembly**
</dt> <dd>

A container element. Its first subelement must be an **assemblyIdentity**. Required.

The assembly element must be in the namespace **urn:schemas-microsoft-com:asm.v1**. Child elements of the assembly must also be in this namespace, by inheritance or by tagging.

The **assembly** element has the following attributes.



| Attribute           | Description                                           |
|---------------------|-------------------------------------------------------|
| **manifestVersion** | The **manifestVersion** attribute must be set to 1.0. |



 

</dd> <dt>

<span id="assemblyIdentity"></span><span id="assemblyidentity"></span><span id="ASSEMBLYIDENTITY"></span>**assemblyIdentity**
</dt> <dd>

Describes and uniquely identifies a side-by-side assembly.

As the first subelement of an **assembly** element, the **assemblyIdentity** describes the side-by-side assembly that is having one or more of its assembly dependencies changed. The publisher configuration file redirects the dependencies of the assembly identified. For example, the following **assemblyIdentity** indicates that the publisher configuration file affects the dependencies of the x86 Microsoft.Windows.Pop 6.0.0.0 assembly.

``` syntax
<assemblyIdentity 
     type="win32-policy" 
     publicKeyToken="0000000000000000" 
     name="policy.6.0.Microsoft.Windows.Pop" 
     version="2.1.0.0" 
     processorArchitecture="x86"/>
```

As the first subelement of a **dependentAssembly** element, **assemblyIdentity** describes a side-by-side assembly dependency. The publisher configuration file reconfigures the identity of this required side-by-side assembly. The change is specified in a **bindingRedirect**. For example, the following **assemblyIdentity** changes any dependency on Microsoft.Windows.SampleAssembly version 2.0.0.0 to a dependency on Microsoft.Windows.SampleAssembly version 2.0.1.0.

``` syntax
<dependency>
      <dependentAssembly>
         <assemblyIdentity 
type="win32" 
name="Microsoft.Windows.SampleAssembly"  
processorArchitecture="x86"
publicKeyToken="0000000000000000"/>
         <bindingRedirect oldVersion="2.0.0.0" newVersion="2.0.1.0"/>
      </dependentAssembly>
</dependency>
```

The **assemblyIdentity** element has the following attributes. It has no sub-elements.



| Attribute                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **type**                  | Specifies the assembly type. Required. In the **assemblyIdentity** for the assembly being affected, the value of the **type** attribute must be set to win32-policy. The value win32-policy must be in all lowercase letters.<br/> In the **assemblyIdentity** for the changing assembly dependency, the value of the **type** attribute must be set to win32. The value win32 must be in all lowercase letters.<br/>                                                                                                                                                                                                             |
| **name**                  | Uniquely names an assembly. Required. In the **assemblyIdentity** for the assembly being affected, name has the form *policy*.*major*.*minor*.*assemblyname* where *major* and *minor* refer to the major and minor parts of the [assembly version](assembly-versions.md).<br/> In the **assemblyIdentity** for the changing assembly dependency, name has the form Organization.Division.Name. For example, Microsoft.Windows.MysampleApp.<br/>                                                                                                                                                                                 |
| **language**              | Identifies the language of the assembly. Optional. In the **assemblyIdentity** for the assembly being affected, if the assembly is language-specific, specify the DHTML language code. If the assembly is for worldwide use (language neutral), omit this attribute.<br/> In the **assemblyIdentity** for the changing assembly dependency, if the assembly is language-specific, specify the DHTML language code. If the assembly is for worldwide use (language neutral) set the value as "\*".<br/>                                                                                                                            |
| **processorArchitecture** | Specifies the processor running the application.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **version**               | Specifies the assembly version. Use four-part version syntax: mmmm.nnnn.oooo.pppp Required only in the DEF-context **assemblyIdentity**. Do not specify the version attribute in the REF-context **assemblyIdentity**.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **publicKeyToken**        | A 16-character hexadecimal string representing the last 8 bytes of the SHA-1 hash of the public key under which the assembly is signed. The public key used to sign the catalog must be 2048 bits or greater. A publicKeyToken is required for all shared side-by-side assemblies. The publicKeyToken used for the publisher configuration file should be the same key used for the signed assembly. Publisher configuration files can be signed using the same tools as used with assemblies, see [Assembly Signing Example](assembly-signing-example.md) and [Creating Signed Files and Catalogs](creating-signed-files-and-catalogs.md). |



 

</dd> <dt>

<span id="dependency"></span><span id="DEPENDENCY"></span>**dependency**
</dt> <dd>

An optional container element for at least one **dependentAssembly**. It has no attributes.

</dd> <dt>

<span id="dependentAssembly"></span><span id="dependentassembly"></span><span id="DEPENDENTASSEMBLY"></span>**dependentAssembly**
</dt> <dd>

Every **dependentAssembly** must be inside exactly one **dependency**. A **dependentAssembly** has no attributes. The first subelement of **dependentAssembly** must be an **assemblyIdentity** for the side-by-side assembly being reconfigured by the publisher configuration.

</dd> <dt>

<span id="bindingRedirect"></span><span id="bindingredirect"></span><span id="BINDINGREDIRECT"></span>**bindingRedirect**
</dt> <dd>

The **bindingRedirect** element contains redirection information for the binding of the assembly.

This element has the attributes shown in the following table.



| Attribute      | Description                                                                                                                                                                                                                           |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **oldVersion** | Specifies the assembly version being overridden and redirected. Use the four-part version syntax nnnnn.nnnnn.nnnnn.nnnnn. Specify a range of versions by a dash with no spaces. For example, 2.14.3.0 or 2.14.3.0 2.16.0.0. Required. |
| **newVersion** | Specifies the replacement assembly version. Use four-part version syntax nnnnn.nnnnn.nnnnn.nnnnn.                                                                                                                                     |



 

</dd> </dl>

## Remarks

Publisher configuration files do not specify files. Note that language-specific policy files are separate from the publisher configuration file.

## Example

``` syntax
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
<assemblyIdentity type="win32-policy" publicKeyToken="0000000000000000" name="policy.6.0.Proseware.Research.SampleAssembly" version="1.0.1.0" language="en-us" processorArchitecture="x86"/>
<dependency>
<dependentAssembly>
<assemblyIdentity type="win32" publicKeyToken="0000000000000000" name="Proseware.Research.SampleAssembly" language="en-us" processorArchitecture="x86"/>
<bindingRedirect oldVersion="1.0.0.0" newVersion="1.0.1.0"/>
</dependentAssembly>
</dependency>
</assembly>
```

 

 




