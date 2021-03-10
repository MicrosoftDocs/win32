---
description: The following example discusses how to generate a signed side-by-side assembly consisting of the assembly manifest, the verification catalog, and the assembly files.
ms.assetid: fa95f292-36e6-4e88-8a0d-aa8bd08def2b
title: Assembly Signing Example
ms.topic: article
ms.date: 05/31/2018
---

# Assembly Signing Example

The following example discusses how to generate a signed side-by-side assembly consisting of the assembly manifest, the verification catalog, and the assembly files. Shared side-by-side assemblies should be signed. The operating system verifies the assembly signature before installing a shared assembly to the global side-by-side store (WinSxS). This makes it difficult to spoof the publisher of the side-by-side assembly.

Note that changing the assembly files or the contents of the manifest after generating the assembly catalog invalidates the catalog and the assembly. If you must update the assembly files or manifest after creating and signing the catalog, you must again sign the assembly and generate a new catalog.

Start with the assembly files, assembly manifest, and the certificate file you will use to sign the assembly. The certificate file must be 2048 bits or larger. You are not required to use a trusted certificate. The certificate is used only to verify that the assembly has not been damaged.

Run the [Pktextract.exe](pktextract-exe.md) utility provided in the Microsoft Windows Software Development Kit (SDK) to extract the public key token from the certificate file. For Pktextract to work properly, the certificate file must be present in the same directory as the utility. Use the extracted public key token value to update the **publicKeyToken** attribute of the **assemblyIdentity** element in the manifest file.

Here is an example of a manifest file named MySampleAssembly.manifest. The MySampleAssembly assembly contains only one file, MYFILE.DLL. Note that the value for the **publicKeyToken** attribute of the **assemblyIdentity** element has been updated with the value of the public key token.

``` syntax
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
    <assemblyIdentity 
        type="win32" 
        name="Microsoft.Windows.MySampleAssembly" 
        version="1.0.0.0" 
        processorArchitecture="x86"         
        publicKeyToken="0000000000000000"/>
    <file name="myfile.dll"/>
</assembly>
```

Next run the [Mt.exe](mt-exe.md) utility provided in the Windows SDK. The assembly files must be located in the same directory as the manifest. In this example this is the MySampleAssembly directory. Call Mt.exe for the example as follows:

**c:\\ MySampleAssembly>mt.exe -manifest MySampleAssembly.manifest -hashupdate -makecdfs**

Here is how the example manifest looks after running Mt.exe. Notice that running Mt.exe with the hashupdate option adds the SHA-1 hash of the file. Do not change this value.

``` syntax
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
    <assemblyIdentity 
        type="win32" 
        name=" Microsoft.Windows.MySampleAssembly" 
        version="1.0.0.0" 
        processorArchitecture="x86"         
        publicKeyToken="0000000000000000"/>
    <file name="myfile.dll"
hash="a1d362d6278557bbe965a684ac7adb4e57427a29" hashalg="SHA1"/>
</assembly>
```

Running Mt.exe with the -makecdfs option generates a file named MySampleAssembly.manifest.cdf that describes the contents of the security catalog that will be used to validate the manifest.

The next step is to run Makecat.exe over this .cdf to create the security catalog for the assembly. The call to Makecat.exe for this example would appear as follows:

**c:\\MySampleAssembly>makecat MySampleAssembly.manifest.cdf**

The final step is to run SignTool.exe to sign the catalog file with the certificate. This should be the same certificate that was used in the preceding to generate the public key token. For more information about SignTool.exe see the [**SignTool**](../seccrypto/signtool.md) topic. The call to **SignTool** for the example would appear as follows:

**c:\\MySampleAssembly>signtool sign /f \<fullpath>mycompany.pfx /du https:\//www.mycompany.com/MySampleAssembly /t https:\//timestamp.digicert.com MySampleAssembly.cat**

If you have an authenticated digital certificate, and your certification authority uses the PVK file format to store the private key, you can use the PVK Digital Certificate Files Importer (pvkimprt.exe) to import the key into your cryptographic service provider (CSP). This utility enables you to export to the industry standard format of PFX/P12. For more information about the PVK Digital Certificate Files Importer, see the Deployment Resources section of the MSDN library or contact your certification authority. You may be able to obtain pvkimprt.exe from https://office.microsoft.com/downloads/2000/pvkimprt.aspx.

See also, [Creating Signed Files and Catalogs](creating-signed-files-and-catalogs.md).

 

 
