---
description: Per-application configuration redirects the dependence of a particular application from one version of a side-by-side assembly to another version of the assembly.
ms.assetid: b7988385-c87e-443c-8ec3-84ab3c172eab
title: Per-application Configuration
ms.topic: article
ms.date: 05/31/2018
---

# Per-application Configuration

Per-application configuration redirects the dependence of a particular application from one version of a side-by-side assembly to another version of the assembly. A per-application configuration may become necessary if the correct operation of a particular application requires an assembly version that is different than the version normally specified as a [default configuration](default-configuration.md) or [publisher configuration](publisher-configuration.md). For example, a global update of the assembly version by the publisher might fix the assembly but break this particular application. In this case, per-application configuration might be used to enable the application to continue to run with the previous assembly version.

Starting with Windows Server 2003, per-application configuration always overrides the [default configuration](default-configuration.md) on a per-application basis. Per-application configuration overrides [publisher configuration](publisher-configuration.md) on a per-application basis only if the [application configuration file](application-configuration-files.md) specifies *apply="no"* in **publisherPolicy** and there is a corresponding entry present in the Application Compatibility database.

> [!Note]  
> On Windows XP, per-application configuration overrides both [default configuration](default-configuration.md) and [publisher configuration](publisher-configuration.md) on a per-application basis. For information, see [Per-application Configuration on Windows XP](per-application-configuration-on-windows-xp.md).

 

Starting with Windows Server 2003, a per-application configuration will override a [publisher configuration](publisher-configuration.md) if the [application configuration file](application-configuration-files.md) specifies *apply="yes"* in **publisherPolicy** and the EnableAppConfig flag is set for the application in the Application Compatibility database. This capability to override a publisher configuration using a per-application configuration enables the application to be run in Safemode. For more information about the Application Compatibility database and Safemode, see the Windows Application Compatibility Toolkit. You can obtain the Windows Application Compatibility Toolkit from [https://www.microsoft.com/downloads](https://www.microsoft.com/Downloads/).

> [!Note]  
> If you ship components with an [application configuration file](application-configuration-files.md) (.config file) that specifies *apply="no"* in **publisherPolicy**, this will cause the generation of the activation context to fail. The per-application configuration will be ignored if you ship components with a .config file specifying *apply="yes"* in **publisherPolicy**.

 

Application administrators can implement a per-application configuration by authoring and installing application configuration files and updating the application compatibility database. The application configuration file should then be deployed and installed into the same folder as the application's executable file. For a listing of the file schema, see [Application Configuration File Schema](application-configuration-file-schema.md). The application compatibility database must be distributed as described in the Application Compatibility Toolkit.

> [!Note]  
> If your application runs in Safemode, it will not receive any important security fixes or bug fixes the publisher of the assembly might issue as publisher configuration files. An application that uses per-application configuration may therefore remain unsecure or continue to work incorrectly even after a new assembly with these fixes are applied to the system. For this reason, application developers should never ship an application with a per-application configuration. Per-application configuration should only be used by corporate administrators as a temporary fix when the application is broken by a publisher configuration. In this case, the permanent solution is that the developers of the assembly and the developers of the application will need to work together to ensure that the assemblies with publisher configuration are fully backwards compatible.

 

The following is an example of an application configuration file. For more information, see Application Configuration Files.

``` syntax
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<configuration>
 <windows>
  <assemblyBinding xmlns="urn:schemas-microsoft-com:asm.v1">
   <assemblyIdentity  processorArchitecture="X86" name="Microsoft.Windows.mysampleApp" type="win32" version="1.0.0.0"/>
   <publisherPolicy apply="no"/>                     
   <dependentAssembly>
    <assemblyIdentity type="win32" processorArchitecture="x86" name="Microsoft.Windows.SampleAssembly" publicKeyToken="0000000000000000"/>
    <bindingRedirect oldVersion="2.0.0.0" newVersion="2.0.1.0"/>
   </dependentAssembly>
  </assemblyBinding>
 </windows>
</configuration>
```

The application administrator should add the required entries to the Application Compatibility database. Download and install the Windows Application Compatibility Toolkit 2.6 from [https://www.microsoft.com/downloads](https://www.microsoft.com/Downloads/). Create a new custom or update your existing database using the Compatibility Administrator as outlined in the toolkit. The Compatibility Fix you want to choose for the compatibility layer for your application is EnableAppConfig. You must always test applications before installing a new compatibility database.

 

 



