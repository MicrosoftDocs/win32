---
description: On Windows Server 2003, WinHTTP is implemented as a side-by-side assembly, and must be linked to as such. Note that this does not apply to Windows Vista and later.
ms.assetid: 524d926d-4d8a-4576-96fd-c533517ba28e
title: Using WinHTTP as a Side-by-side Assembly
ms.topic: article
ms.date: 05/31/2018
---

# Using WinHTTP as a Side-by-side Assembly

On Windows Server 2003, WinHTTP is implemented as a side-by-side assembly, and must be linked to as such. Note that this does not apply to Windows Vista and later.

## Side-by-side Assemblies

Starting with Microsoft Windows XP, a side-by-side assemblies mechanism was provided to control run-time linking to avoid dynamic-link-library (DLL) versioning conflicts. For information about side-by-side assemblies, see [About Isolated Applications and Side-by-side Assemblies](/windows/desktop/SbsCs/about-isolated-applications-and-side-by-side-assemblies).

To use this mechanism to link to WinHTTP version 5.1 on Windows Server 2003, an application must incorporate a manifest that specifies WinHTTP as a dependent assembly. See [Using Side-by-side Assemblies](/windows/desktop/SbsCs/using-side-by-side-assemblies) for more information about how to do this.

## A Sample WinHTTP Application Manifest

The sample manifest below illustrates an application manifest that can be used for linking to WinHTTP.

All attributes except "type" of the "<assembly><assemblyIdentity>" must be modified as appropriate for your particular application. The same goes for the contents of the "&lt;description&gt;" element.

In addition, make sure that the "processorArchitecture" attribute of the "<dependentAssembly><assemblyIdentity>" matches the "processorArchitecture" attribute of the "<assembly><assemblyIdentity>". Below, for example, both are set to "x86".

All values not specific to your application should take the forms shown below.

``` syntax
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
  <assemblyIdentity
                    version="1.0.0.0"
                    processorArchitecture="x86"
                    name="Microsoft.Windows.Sample"
                    type="win32" />
  <description>Sample WinHttp Application</description>
  <dependency>
    <dependentAssembly>
      <assemblyIdentity 
                    type="win32" 
                    name="Microsoft.Windows.WinHTTP" 
                    version="5.1.0.0"
                    processorArchitecture="x86" 
                    publicKeyToken="6595b64144ccf1df"
                    language="*" />
    </dependentAssembly>
  </dependency>
</assembly>
```

 

 
