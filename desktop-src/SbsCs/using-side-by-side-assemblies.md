---
description: Use the following procedure to develop a new application, or update an existing application, to use the side-by-side assemblies available from Microsoft or other side-by-side assembly publishers.
ms.assetid: da6b6767-8a30-4a76-a030-615067a2cb17
title: Using Side-by-side Assemblies
ms.topic: article
ms.date: 05/31/2018
---

# Using Side-by-side Assemblies

Use the following procedure to develop a new application, or update an existing application, to use the [side-by-side assemblies](about-side-by-side-assemblies-.md) available from Microsoft or other side-by-side assembly publishers. For a list of the side-by-side assemblies currently provided by Microsoft, see [Supported Microsoft Side-by-side Assemblies](supported-microsoft-side-by-side-assemblies.md). Note that the application must be run on at least Windows XP to install the assemblies as side-by-side assemblies. For more information, see [Guidelines for Creating Side-by-side Assemblies](guidelines-for-creating-side-by-side-assemblies.md).

**To add a side-by-side assembly to an application**

1.  Identify the side-by-side assemblies that your application requires. Starting with Windows XP, these side-by-side assemblies and their assembly manifests are installed with the operating system but are not globally registered.
2.  Use an XML editor to create an [application manifest](application-manifests.md). See the example application manifest below. For more information, see [Application Manifests](application-manifests.md) in the [Manifest Files Reference](manifest-files-reference.md).
3.  Enter attribute values in the [*DEF-context assemblyIdentity*](d-sbscs-gly.md) subelement of the application manifest that uniquely defines the application. For more information about the DEF-context **assemblyIdentity**, see [Application Manifests](application-manifests.md).
4.  If the assembly contains any dependent assemblies, enter attribute values into the corresponding [*REF-context assemblyIdentity*](r-sbscs-gly.md) subelements of the application manifest. For more information about the REF-context **assemblyIdentity**, see [Application Manifests](application-manifests.md).

    ``` syntax
    <dependentAssembly>
      <assemblyIdentity type="win32"
                        name="Microsoft.Windows.SampleAssembly"
                        version="6.0.0.0" processorArchitecture="x86"
                        publicKeyToken="a5aaf5ba15723d5"/>
    ```

5.  You may include the application manifest in the application's binary executable header file.

    In this case, also add the following line to the application header file:

    <dl> CREATEPROCESS\_MANIFEST\_RESOURCE\_ID RT\_MANIFEST "YourApp.exe.manifest"  
    </dl>

    As an alternative, you can place a separate manifest file in the same directory as your application's executable file. The operating system loads the manifest from the file system first, and then checks the resource section of the executable. The file system version takes precedence.

6.  [Shared assemblies](/windows/desktop/Msi/shared-assemblies) should be installed using the [Windows Installer](../msi/windows-installer-portal.md) version 2.0. Author a Windows Installer package as described in [How Do I Install Win32 Assemblies for Side-by-side Sharing on Windows XP?](../msi/installing-win32-assemblies-for-side-by-side-sharing-on-windows-xp.md).
7.  [Private assemblies](/windows/desktop/Msi/private-assemblies) can be installed using the [Windows Installer](../msi/windows-installer-portal.md) version 2.0. Author a Windows Installer package as described in [How Do I Install Win32 Assemblies for the Private Use of an Application on Windows XP?](../msi/installing-win32-assemblies-for-the-private-use-of-an-application-on-windows-xp.md). You can also use any other installer to copy a private assembly and its manifest into the same folder as the application's executable file.
8.  Test your application to ensure the results. Note that your test computer should not have the side-by-side assembly registered.
9.  Deploy your application or update as a Windows Installer package.

## Example Application Manifest

The following is an example of an application manifest:

``` syntax
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
  <assemblyIdentity type="win32" name="Microsoft.Windows.mysampleapp" version="1.0.0.0" processorArchitecture="x86"/>
  <dependency>
    <dependentAssembly>
      <assemblyIdentity type="win32" name="Microsoft.Windows.SampleAssembly" version="6.0.0.0" processorArchitecture="x86" publicKeyToken="a5aaf5ba15723d5"/>
    </dependentAssembly>
  </dependency>
  <dependency>
    <dependentAssembly>
      <assemblyIdentity type="win32" name="Microsoft.Tools.MyPrivateDll" version="2.5.0.0" processorArchitecture="x86"/>
    </dependentAssembly>
  </dependency>
</assembly>
```

 

 
