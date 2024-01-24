---
description: A publisher configuration file globally redirects applications and assemblies having a dependence on one version of a side-by-side assembly to use another version of the same assembly.
ms.assetid: 9146c81e-8f43-4854-bbc4-1daaeb5fdda8
title: Publisher Configuration
ms.topic: article
ms.date: 05/31/2018
---

# Publisher Configuration

A [publisher configuration file](publisher-configuration-files.md) globally redirects applications and assemblies having a dependence on one version of a side-by-side assembly to use another version of the same assembly. This enables applications and assemblies to use the updated assembly without having to rebuild all of the affected applications.

[Publisher configuration files](publisher-configuration-files.md) may be provided by the publisher of an assembly when issuing a new version of the assembly with compatible bug fixes or security updates. The updated version should be fully backward compatible. A publisher configuration file should never be used to add new features unless the update is fully backward compatible. Publisher configuration files should never be used to increment the major or minor version of an assembly. For example, do not redirect assembly version 6.0.0.0 to 7.0.0.0 or to 6.1.0.0.

Publisher configuration files should only be issued by the publisher of the assembly. Assembly developers should sign shared side-by-side assemblies and publisher configuration files. Use the same key to sign the assembly and the associated publisher configuration files. Publisher configuration files should be signed using the same tools as used for assemblies, see [Assembly Signing Example](assembly-signing-example.md) and [Creating Signed Files and Catalogs](creating-signed-files-and-catalogs.md).

Typically, the new version of an assembly and the associated publisher configuration file will be installed in a service pack update. Publisher configuration files should never be provided with applications as a redistributable because installing a publisher configuration file globally redirects assemblies on the system. If the assembly being updated is provided as a redistributable, the publisher should provide both of the following.

-   A Windows Installer package (.msi file) that includes the new version of the assembly with publisher configuration. This may be installed as a service pack or QFE because in this case the customer has chosen to globally update the system. This version of the package should never be installed by applications.
-   A Windows Installer merge module (.msm file) that only includes the new version of the assembly. This version may be included with applications.

Applications requiring a minimum version of the assembly should state their dependency on the minimum version, if the minimum version is unavailable on a system then the application will fail to start. If it is available as a redistributable then it should be included in the application setup.

For example, installing the following [publisher configuration file](publisher-configuration-files.md) redirects binding from version 2.0.0.0 of the Microsoft.Windows.SampleAssembly to version 2.0.1.0. This adds a new policy, named 1.1.0.0.Policy, under %systemDrive%\\windows\\winsxs\\policies\\x86\_policy.2.0.Microsoft.Windows.SampleAssembly\_75e377300ab7b886\_x-ww\_<*hashvalue*>.

``` syntax
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
   <assemblyIdentity type="win32-policy" publicKeyToken="0000000000000000" name="policy.2.0.Microsoft.Windows.SampleAssembly" version="1.1.0.0" processorArchitecture="x86"/>
   <dependency>
      <dependentAssembly>
         <assemblyIdentity type="win32" name="Microsoft.Windows.SampleAssembly"  processorArchitecture="x86" publicKeyToken="75e377300ab7b886"/>
         <bindingRedirect oldVersion="2.0.0.0" newVersion="2.0.1.0"/>
      </dependentAssembly>
   </dependency>
</assembly>
```

Installing the following publisher configuration file for the same assembly redirects binding from version 2.0.0.0 of the Microsoft.Windows.SampleAssembly to version 2.0.3.0. This adds another policy, named 2.1.0.0.Policy, under %systemDrive%\\windows\\winsxs\\policies\\x86\_policy.2.0.Microsoft.Windows.SampleAssembly\_75e377300ab7b886\_x-ww\_<*hashvalue*>.

``` syntax
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
   <assemblyIdentity type="win32-policy" publicKeyToken="0000000000000000" name="policy.2.0.Microsoft.Windows.SampleAssembly" version="2.1.0.0" processorArchitecture="x86"/>
   <dependency>
      <dependentAssembly>
         <assemblyIdentity type="win32" name="Microsoft.Windows.SampleAssembly"  processorArchitecture="x86" publicKeyToken="75e377300ab7b886"/>
         <bindingRedirect oldVersion="2.0.0.0" newVersion="2.0.3.0"/>
      </dependentAssembly>
   </dependency>
</assembly>
```

 

 



