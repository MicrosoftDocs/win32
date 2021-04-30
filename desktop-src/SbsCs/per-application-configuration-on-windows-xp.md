---
description: On Windows XP, per-application configuration overrides both default configuration and publisher configuration on a per-application basis.
ms.assetid: 5b55d12d-8805-4820-91af-5ef583de3463
title: Per-application Configuration on Windows XP
ms.topic: article
ms.date: 05/31/2018
---

# Per-application Configuration on Windows XP

On Windows XP, per-application configuration overrides both [default configuration](default-configuration.md) and [publisher configuration](publisher-configuration.md) on a per-application basis. This redirects the dependence of a specific application from one version of a side-by-side assembly to another specified version of the assembly.

> [!Note]  
> Starting with Windows Server 2003, per-application configuration overrides [publisher configuration](publisher-configuration.md) on a per-application basis only if the [application configuration file](application-configuration-files.md) specifies *apply="no"* in **publisherPolicy** and there is a corresponding entry present in the Application Compatibility database. Per-application configuration always overrides the [default configuration](default-configuration.md). For information see [per-application configuration](per-application-configuration.md).

 

A per-application configuration may become necessary if the correct operation of a particular application requires an assembly version that is different than the version normally specified as a default or publisher configuration. For example, a global update of the assembly version by the publisher might fix the assembly but break this particular application. In this case, per-application configuration might be used to enable the application to continue to run with the previous assembly version. Another example, a service pack installation containing an assembly update might use [publisher configuration](publisher-configuration.md) to redirect the dependencies of all applications and assemblies on the system from version 1.0.0.0 to 1.0.1.0. If there is an application that requires version 1.0.0.0 to work correctly, it can be redirected to version 1.0.0.0 by using per-application configuration.

Application administrators can implement a per-application configuration by authoring and installing [application configuration files](application-configuration-files.md). These redirect a specific application from dependence on one version of a side-by-side assembly to dependence on another version. [*Application configuration*](/windows/desktop/Msi/a-gly) files can override [publisher configuration files](publisher-configuration-files.md) and the default configuration specified by [application manifests](application-manifests.md) and [assembly manifests](assembly-manifests.md). The application configuration file includes information used by the loader when [**CreateProcess**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-createprocessa) is called.

To configure an application to override both the application manifest and the publisher configuration, a developer must author an application configuration file. The application configuration file is then deployed and installed into the same folder as the application's executable file. For a listing of the file schema, see [Application Configuration File Schema](application-configuration-file-schema.md).

Note that if your application uses per-application configuration, it will not receive any important security fixes or bug fixes the publisher of the assembly might issue as publisher configuration files. An application that uses per-application configuration may therefore remain unsecure or continue to work incorrectly even after a new assembly with these fixes are applied to the system. For this reason, application developers should never ship an application with a per-application configuration. Per-application configuration should only be used by corporate administrators as a temporary fix when the application is broken by a publisher configuration. In this case, the permanent solution is that the developers of the assembly and the developers of the application will need to work together to ensure that the assemblies with publisher configuration are fully backwards compatible.

The following is an example of an application configuration file. For more information, see [Application Configuration Files](application-configuration-files.md).

``` syntax
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<configuration>
  <windows>
    <assemblyBinding xmlns="urn:schemas-microsoft-com:asm.v1">
      <assemblyIdentity 
          name="Microsoft.Windows.mysampleApp" 
          processorArchitecture="x86" 
          version="1.0.0.0" type="win32"/>
        <dependentAssembly>
          <assemblyIdentity type="win32" 
              name="Microsoft.Windows.SampleAssembly" 
              processorArchitecture="x86" 
              publicKeyToken="0000000000000000"/>
          <bindingRedirect 
              oldVersion="2.0.0.0" 
              newVersion="2.0.1.0"/>
        </dependentAssembly>
    </assemblyBinding>
   </windows>
</configuration>
```

 

 
