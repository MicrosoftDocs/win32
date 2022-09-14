---
description: If you want users of your application, or core DLL, to be capable of changing the language of the user interface, you should consider placing language resources into separate satellite resource DLLs.
ms.assetid: fcadd7e8-cab8-43cb-9c67-af8ebe0e3a5b
title: Using Assemblies with a Multilanguage User Interface
ms.topic: article
ms.date: 05/31/2018
---

# Using Assemblies with a Multilanguage User Interface

If you want users of your application, or core DLL, to be capable of changing the language of the user interface, you should consider placing language resources into separate satellite resource DLLs. For more information about using satellite resource DLLs, see [Multilanguage User Interface (MUI)](/windows/desktop/Intl/multilingual-user-interface).

Each satellite DLL contains the resources for a different language. The core DLL may be provided as an assembly and each of the satellite DLLs may be provided as separate satellite assemblies. In this case, each satellite assembly should have its own self-describing assembly manifest. The satellite assembly's manifest should not describe any dependency on other assemblies. Any dependency of satellite assemblies on other assemblies should instead be described in the core assembly's manifest.

The [Multilanguage User Interface (MUI)](/windows/desktop/Intl/multilingual-user-interface) version of Windows enables users to specify the user-interface language according to their preferences, provided the required language has been added to the system. A core assembly can support multiple languages by using multiple MUI assemblies. In this case, each MUI assembly should have its own manifest and any dependencies on other assemblies should only be described in the core assembly's manifest.

For example, Proseware.Sample.Pop may be a core side-by-side assembly which happens to be dependent on the Proseware.Research.SampleAssembly assembly. If Proseware.Sample.Pop uses MUI to support multiple languages, separate MUI assemblies can be provided for each language. Each MUI assembly should have its own manifest describing this particular satellite resource DLL. The MUI assembly manifests should not include any reference to dependencies on other assemblies. The manifest describing the core assembly, Proseware.Sample.Pop, should describe the dependency of Proseware.Sample.Pop on the Proseware.Research.SampleAssembly assembly.

The attributes of the **assemblyIdentity** element of a satellite assembly are similar to those in the manifest of the base assembly. The **name** attribute should be the same as the base assembly with the addition of "Resources." For example, if the name is "Proseware.Tools.SpellCheck.Runtime-Libraries" in the base assembly, the name in the resource assembly would be "Proseware.Tools.SpellCheck.Runtime-Libraries.Resources." The **language** attribute should identify the language of the resource assembly. The **file** attribute should include the list of files that are resource DLLs.

The following is an example of the manifest for Proseware.Tools.SpellCheck.Runtime-Libraries resources assembly.

``` syntax
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
    <assemblyIdentity
        type="win32"
        name="Proseware.Tools.SpellCheck.Runtime-Libraries.Resources"
        version="6.0.0.0"
        processorArchitecture="X86"
        language="DE"
        publicKeyToken="0000000000000000"
    />
    <file name="sample.dll"/>
</assembly>
```

The base assembly describes an optional dependency on the resource assembly. In this example, if a user is running Windows with the locale designated as German, an application using the Proseware.Tools.SpellCheck assembly would display text in German.

``` syntax
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
    <assemblyIdentity type="win32" 
    name="Proseware.Tools.SpellCheck.Runtime-Libraries"
    version="6.0.0.0" processorArchitecture="x86"
    publicKeyToken="0000000000000000"/>
    <dependency optional="yes">
        <dependentAssembly>
            <assemblyIdentity type="win32" 
                              name="Proseware.Tools.SpellCheck.Runtime-Libraries.Resources" 
                              version="6.0.0.0" 
                              processorArchitecture="x86" 
                              publicKeyToken="0000000000000000" 
                              language="*"
            />
        </dependentAssembly>
    </dependency>
```

 

 
