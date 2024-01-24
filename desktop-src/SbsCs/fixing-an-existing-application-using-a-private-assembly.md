---
description: Beginning with Windows XP, you can create a private assembly and make it available to a specific application.
ms.assetid: 08cebffc-6856-4dac-8600-5e7fecb5c69b
title: Fix an Existing Application Using a Private Assembly
ms.topic: article
ms.date: 05/31/2018
---

# Fixing an Existing Application Using a Private Assembly

Beginning with Windows XP, you can create a private assembly and make it available to a specific application. This capability can be used to fix an application that becomes incompatible with an update. An example would be an application that becomes incompatible with the latest version of MSVCRT.DLL after upgrading the operating system. In this case, you do not have the option of replacing the system version because MSVCRT.DLL is a Windows Protected File. Rather than having to rewrite the application to work with the new version of MSVCRT, you can create a private assembly for MSVCRT and install this in your application folder. Note that not every shared component is a suitable candidate for a private side-by-side assembly, and some components have licensing restrictions about where their components can be installed. The component needs to meet the criteria for a side-by-side component. Ask the publisher of the component if they can provide a suitable assembly.

The private assembly's manifest and the application's manifest should both be installed in the same folder as the application's executable. When the application runs, it consults the application manifest and load the version of MSVCRT that is private to the application.

For this example, the private assembly would include both MSVCRT.DLL and MSVCIRT.DLL as in the following assembly manifest:

``` syntax
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
    <assemblyIdentity type="win32"
      name="Microsoft.Windows.PrivateCPlusPlusRuntime" 
version="6.0.0.0" 
processorArchitecture="x86"/>
    <file name="msvcrt.dll"/>
    <file name="msvcirt.dll"/>
</assembly>
```

The following is an example of a possible application manifest.

``` syntax
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0"> 
<assemblyIdentity 
    version="1.0.0.0" 
    processorArchitecture="x86" 
    name="APPLICATION" 
    type="win32" 
/> 
<description>Description of Application</description> 
<dependency> 
    <dependentAssembly> 
       <assemblyIdentity 
           type="win32"
           name="Microsoft.Windows.PrivateCPlusPlusRuntime" 
           version="6.0.0.0" 
           processorArchitecture="x86"/> 
    </dependentAssembly> 
</dependency> 
</assembly>
```

 

 



