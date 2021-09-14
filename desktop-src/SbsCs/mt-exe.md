---
description: The Mt.exe file is a tool that generates signed files and catalogs. It is available in the Microsoft Windows Software Development Kit (SDK). Mt.exe requires that the file referenced in the manifest be present in the same directory as the manifest.
ms.assetid: 37f010ee-2658-4547-9871-c913201042de
title: Mt.exe
ms.topic: article
ms.date: 05/31/2018
---

# Mt.exe

The Mt.exe file is a tool that generates signed files and catalogs. It is available in the Microsoft Windows Software Development Kit (SDK). Mt.exe requires that the file referenced in the manifest be present in the same directory as the manifest.

Mt.exe generates hashes using the CryptoAPI implementation of the Secure Hash Algorithm (SHA-1). For more information about hash algorithms, see [Hash and Signature Algorithms](/windows/desktop/SecCrypto/hash-and-signature-algorithms). Hashes are inserted as a hexadecimal string into the **file** tags in the manifest. The tool currently only generates SHA-1 hashes, although files in manifests may use other hashing schemes.

Mt.exe uses Makecat.exe to generate catalog files (.cat) from catalog definition files (.cdf). This tool fills out a standard template CDF with the name and location of your manifest. You can use this with Makecat.exe to generate the assembly catalog.

The version of Mt.exe provided in recent versions of the Windows SDK can also be used to generate manifests for managed assemblies and unmanaged side-by-side assemblies.

## Syntax

```console
mt.exe [-manifest:<component1.manifest><component2.manifest>] [-identity:<identity string>] 
[-rgs:<file1.rgs>] [-tlb:<file2.tlb>] [-dll:<file3.dll>] [-replacements:<XML filename>]
[-managedassemblyname:<managed assembly>] [-nodependency] [-category] [-out:<output manifest name>]
[-inputresource:<file4>;[#]<resource_id>] [-outputresource:<file5>;[#]<resource_id>] 
[-updateresource:<file6>;[#]<resource_id>] [-hashupdate[:<path to files>]] [-makecdfs] [-validate_manifest]
[-validate_file_hashes:<path to files>] [-canonicalize] [-check_for_duplicates] [-nologo] [-verbose]
```

## Command Line Options

Mt.exe uses the following case-insensitive command line options.



<table>
<colgroup>
<col  />
<col  />
</colgroup>
<thead>
<tr class="header">
<th>Option</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>-manifest</td>
<td>Specifies the name of the manifest file. To modify a single manifest, specify one manifest file name. For example, component.manifest.<br/> To merge multiple manifests, specify the names of the source manifests here. Specify the name of the updated manifest with either the <strong>-out</strong>, <strong>-outputresource</strong>, or <strong>-updateresource</strong> options. For example, the following command line requests an operation that merges two manifests, man1.manifest and man2.manifest, into a new manifest, man3.manifest.<br/> <strong>mt.exe -manifest man1.manifest man2.manifest -out:man3.manifest</strong><br/>
<blockquote>
[!Note]<br />
No colon (:) is required with the <strong>-manifest</strong> option.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="even">
<td>-identity</td>
<td>Provides the attributes values of the <strong>assemblyIdentity</strong> element of the manifest. The argument of the <strong>-identity</strong> option is a string value containing the attribute values in fields separated by commas. Provide the value of the <strong>name</strong> attribute in the first field, without including a &quot;name=&quot; substring. All the remaining fields specify the attributes and their values using the form: <em><attribute name></em>=<em><attribute_value></em>.<br/> For example, to update the <strong>assemblyIdentity</strong> element of the manifest with the following information:<br/> <assemblyIdentity type=&quot;win32&quot; name=&quot;Microsoft.Windows.SampleAssembly&quot; version=&quot;6.0.0.0&quot; processorArchitecture=&quot;x86&quot; publicKeyToken=&quot;a5aaf5ba15723d5&quot;/> <br/> include the following <strong>-identity</strong> option on the command line:<br/> <strong>-identity:</strong>&quot;Microsoft.Windows.SampleAssembly, processorArchitecture=x86, version=6.0.0.0, type=win32, publicKeyToken=a5aaf5ba15723d5&quot;<br/></td>
</tr>
<tr class="odd">
<td>-rgs</td>
<td>Specifies the name of the registration script (.rgs) file. The <strong>-dll</strong> option is required to use the <strong>-rgs</strong> option.<br/></td>
</tr>
<tr class="even">
<td>-tlb</td>
<td>Specifies the name of the type library (.tlb) file. The <strong>-dll</strong> option is required to use the <strong>-tlb</strong> option.<br/></td>
</tr>
<tr class="odd">
<td>-dll</td>
<td>Specifies the name of the dynamic-link library (DLL) file. The <strong>-dll</strong> option is required by <strong>mt.exe</strong> if the <strong>-rgs</strong> or <strong>-tlb</strong> options are used. Specify the name of the DLL you intend to eventually build from the .rgs or .tlb files.<br/> For example, the following command requests an operation that generates a manifest from .rgs and .tlb files.<br/> <strong>mt.exe -rgs:testreg1.rgs -tlb:testlib1.tlb -dll:test.dll -replacements:rep.manifest -identity:&quot;Microsoft.Windows.SampleAssembly, processorArchitecture=x86, version=6.0.0.0, type=win32, publicKeyToken=a5aaf5ba15723d5&quot; -out:rgstlb.manifest</strong><br/></td>
</tr>
<tr class="even">
<td>-replacements</td>
<td>Specifies the file that contains values for the replaceable string in the .rgs file.<br/></td>
</tr>
<tr class="odd">
<td>-managedassemblyname</td>
<td>Generates a manifest from the specified managed assembly. Use with the <strong>-nodependency</strong> option to generate a manifest without dependency elements. Use with the <strong>-category</strong> option to generate a manifest with category tags. For example, if managed.dll is a managed assembly, the following command line generates the out.manifest from managed.dll.<br/> <strong>mt.exe -managedassemblyname:managed.dll -out:out.manifest</strong> <br/></td>
</tr>
<tr class="even">
<td>-nodependency</td>
<td>Specifies an operation that generates a manifest without dependency elements. The <strong>-nodependency</strong> option requires the <strong>-managedassemblyname</strong> option. For example, if managed.dll is a managed assembly, the following command line generates the out.manifest from managed.dll without dependency information.<br/> <strong>mt.exe -managedassemblyname:managed.dll -out:out.manifest -nodependency</strong><br/></td>
</tr>
<tr class="odd">
<td>-category</td>
<td>Specifies an operation that generates a manifest with category tags. The <strong>-category</strong> option requires the <strong>-managedassemblyname</strong> option. For example, if managed.dll is a managed assembly, the following command line generates the out.manifest from managed.dll with category tags.<br/> <strong>mt.exe -managedassemblyname:managed.dll -out:out.manifest -category</strong><br/></td>
</tr>
<tr class="even">
<td>-nologo</td>
<td>Specifies an operation that is run without displaying standard Microsoft copyright data. If <strong>mt.exe</strong> runs as part of a build process, this option can be used to prevent writing unwanted information into the log files. <br/></td>
</tr>
<tr class="odd">
<td>-out</td>
<td>Specifies the name of the updated manifest. If this is a single-manifest operation, and the <strong>-out</strong> option is omitted, the original manifest is modified. <br/></td>
</tr>
<tr class="even">
<td>-inputresource</td>
<td>Specifies an operation performed on a manifest obtained from a resource of type RT_MANIFEST. If the <strong>-inputresource</strong> option is used without specifying the resource identifier, <em><resource_id></em>, the operation uses the value CREATEPROCESS_MANIFEST_RESOURCE. <br/> For example, the following command requests an operation that merges a manifest from a DLL, dll_with_manifest.dll, and a manifest file, man2.manifest. The merged manifests are received by a manifest in the resource file of another DLL, dll_with_merged_manifests. <br/> <strong>mt.exe -inputresource:dll_with_manifest.dll;#1 -manifest man2.manifest -outputresource:dll_with_merged_manifest.dll;#3</strong><br/> To extract the manifest from a DLL, specify the DLL file name. For example, the following command extracts the manifest from lib1.dll and man3.manifest receives the extracted manifest.<br/> <strong>mt.exe -inputresource:lib.dll;#1 -out:man3.manifest</strong><br/></td>
</tr>
<tr class="odd">
<td>-outputresource</td>
<td>Specifies an operation that generates a manifest to be received by a resource of type RT_MANIFEST. If the <strong>-outputresource</strong> option is used without specifying the resource identifier, <em><resource_id></em>, the operation uses the value CREATEPROCESS_MANIFEST_RESOURCE. <br/></td>
</tr>
<tr class="even">
<td>-updateresource</td>
<td>Specifies an operation that is equivalent to using the <strong>-inputresource</strong> and <strong>-outputresource</strong> options with identical arguments. For example, the following command requests an operation that computes a hash of the files at the specified path and updates the manifest of a resource of a portable executable (PE).<br/> <strong>mt.exe -updateresource:dll_with_manifest.dll;#1 -hashupdate:f:\files</strong>.<br/></td>
</tr>
<tr class="odd">
<td>-hashupdate</td>
<td>Computes the hash value of the files at the specified paths and updates the value of the <strong>hash</strong> attribute of the <strong>File</strong> element with this value. <br/> For example, the following command requests an operation that merges two manifest files, man1.manifest and man2.manifest, and updates the value of the <strong>hash</strong> attribute of the <strong>File</strong> element in the manifest that receives the merged information, merged.manifest.<br/> <strong>mt.exe -manifest man1.manifest man2.manifest -hashupdate:d:\filerepository -out:merged.manifest</strong><br/> If the paths to the files are not specified, the operation searches location of the manifest specified to receive the update. For example, the following command requests an operation that computes the updated hash value using files found by searching the location of updated.manifest.<br/> <strong>mt.exe -manifest yourComponent.manifest -hashupdate -out:updated.manifest</strong><br/></td>
</tr>
<tr class="even">
<td>-validate_manifest</td>
<td>Specifies an operation that performs a syntax check of the conformance of the manifest with the manifest schema. For example, the following command requests a check to validate the conformance of man1.manifest with its schema. <br/> <strong>mt.exe -manifest man1.manifest -validate_manifest</strong><br/></td>
</tr>
<tr class="odd">
<td>-validate_file_hashes</td>
<td>Specifies an operation that validates the hash values of the <strong>File</strong> elements of the manifest. For example, the following command requests an operation that validates the hash values of all the <strong>File</strong> elements of the man1.manifest.<br/> <strong>mt.exe -manifest man1.manifest -validate_file_hashes:&quot;c;\files&quot;</strong><br/></td>
</tr>
<tr class="even">
<td>-canonicalize</td>
<td>Specifies an operation to update the manifest to canonical form. For example, the following command updates man1.manifest to canonical form.<br/> <strong>mt.exe -manifest man1.manifest</strong><br/></td>
</tr>
<tr class="odd">
<td>-check_for_duplicates</td>
<td>Specifies an operation that checks the manifest for duplicate elements. For example, the following command checks man1.manifest for duplicate elements.<br/> <strong>mt.exe -man1.manifest -check_for_duplicates</strong><br/></td>
</tr>
<tr class="even">
<td>-makecdfs</td>
<td>Generates .cdf files to make catalogs. For example, to the following command requests an operation that updates the hash value and generates a .cdf file.<br/> <strong>mt.exe -manifest comp1.manifest -hashupdate -makecdfs -out:updated.manifest</strong><br/></td>
</tr>
<tr class="odd">
<td>-verbose</td>
<td>Displays verbose debugging information.</td>
</tr>
<tr class="even">
<td>-?</td>
<td>When run with -?, or with no options and arguments, Mt.exe displays help text.</td>
</tr>
</tbody>
</table>



 

## Related topics

<dl> <dt>

[Side-by-Side Assembly Development Tools](side-by-side-assembly-development-tools.md)
</dt> </dl>

 

