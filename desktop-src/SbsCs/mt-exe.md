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
					<tr>
						<th>Option</th>
						<th>Description</th>
					</tr>
					<tr>
						<td>-manifest</td>
						<td><p>Specifies the name of the manifest file. To modify a single manifest, specify one  manifest file name.  For example, component.manifest.</p> <p>To merge multiple  manifests, specify the names of the source manifests here.  Specify  the name of the updated manifest with either the <i>-out</i>, <i>-outputresource</i>, or <i>-updateresource</i>  options.  For example, the following command line requests an operation that merges two  manifests,    man1.manifest and man2.manifest, into a new manifest, man3.manifest.</p><p><i>mt.exe -manifest man1.manifest man2.manifest -out:man3.manifest</i></p><p>No colon (:) is required with the <i>-manifest</i> option.</p></td>
					</tr>
					<tr>
						<td>-identity</td>
						<td><p>Provides the attributes values of the <strong>assemblyIdentity</strong> element of the manifest. The argument of the <i>-identity</i> option is a string value containing the attribute values in fields separated by commas.  Provide the value of the <strong>name</strong> attribute in the first field, without including a "name=" substring. All the remaining fields specify the attributes and their values using the form: &lt;attribute name&gt;=&lt;attribute_value&gt;.</p><p>For example, to update the <strong>assemblyIdentity</strong> element of the manifest with the following information:</p><p>&lt;assemblyIdentity type="win32"
                    name="Microsoft.Windows.SampleAssembly"
                    version="6.0.0.0" processorArchitecture="x86"
                    publicKeyToken="a5aaf5ba15723d5"/&gt; </p><p>include  the following <i>-identity</i> option on the command line:</p><p><i>-identity:</i>"Microsoft.Windows.SampleAssembly, processorArchitecture=x86, version=6.0.0.0, type=win32, publicKeyToken=a5aaf5ba15723d5"</p></td>
					</tr>
					<tr>
						<td>-rgs </td>
						<td><p>Specifies the name of the registration script (.rgs) file. The <i>-dll  </i>option is required to use the <i>-rgs</i> option.</p> </td>
					</tr>
					<tr>
						<td>-tlb </td>
						<td><p>Specifies the name of the type library (.tlb) file.  The <i>-dll  </i>option is required to use the <i>-tlb</i> option.</p> </td>
					</tr>
					<tr>
						<td>-dll </td>
						<td><p>Specifies the name of the dynamic-link library (DLL) file. The <i>-dll  </i>option is required by <i>mt.exe </i> if the <i>-rgs</i> or <i>-tlb</i> options are used. Specify the name of the DLL you intend to eventually build from the .rgs or .tlb files.</p><p>For example, the following command requests an operation that generates a manifest from .rgs and .tlb files.</p><p><i>mt.exe -rgs:testreg1.rgs -tlb:testlib1.tlb -dll:test.dll -replacements:rep.manifest -identity:"Microsoft.Windows.SampleAssembly, processorArchitecture=x86, version=6.0.0.0, type=win32, publicKeyToken=a5aaf5ba15723d5" -out:rgstlb.manifest</i> </p> </td>
					</tr>
					<tr>
						<td>-replacements </td>
						<td><p>Specifies the file that contains values for the replaceable string in the .rgs file.</p> </td>
					</tr>
					<tr>
						<td>-managedassemblyname </td>
						<td><p>Generates a manifest from the specified managed assembly.  Use with the <i>-nodependency</i> option to generate a manifest without dependency elements. Use with the <i>-category</i> option to generate a manifest with category tags. For example, if managed.dll is a managed assembly, the following command line generates the out.manifest from managed.dll.</p><p><i>mt.exe -managedassemblyname:managed.dll -out:out.manifest </i></p> </td>
					</tr>
					<tr>
						<td>-nodependency </td>
						<td><p>Specifies an operation that generates a manifest without dependency elements.  The <i>-nodependency</i> option requires the <i>-managedassemblyname</i> option. For example, if managed.dll is a managed assembly, the following command line generates the out.manifest from managed.dll without dependency information.</p><p><i>mt.exe -managedassemblyname:managed.dll -out:out.manifest -nodependency</i></p> </td>
					</tr>
					<tr>
						<td>-category </td>
						<td><p>Specifies an operation that generates a manifest with category tags. The <i>-category</i> option requires the <i>-managedassemblyname</i> option. For example, if managed.dll is a managed assembly, the following command line generates the out.manifest from managed.dll with category tags.</p><p><i>mt.exe -managedassemblyname:managed.dll -out:out.manifest -category</i></p> </td>
					</tr>
					<tr>
						<td>-nologo</td>
						<td><p>Specifies an operation that is  run without displaying standard Microsoft copyright data. If  <i>mt.exe</i> runs as part of a build process,  this option can be used to prevent writing unwanted information into the log files. </p></td>
					</tr>
					<tr>
						<td>-out </td>
						<td><p>Specifies the name of the updated manifest.  If this is a single-manifest operation,  and the <i>-out</i> option is omitted, the  original manifest is modified. </p></td>
					</tr>
					<tr>
						<td>-inputresource </td>
						<td><p>Specifies an operation performed on a manifest obtained from a resource of type RT_MANIFEST.  If  the <i>-inputresource</i> option is used without specifying  the resource identifier, &lt;resource_id&gt;, the operation uses the value CREATEPROCESS_MANIFEST_RESOURCE. </p><p>For example, the following command requests an operation that merges a manifest from a DLL, dll_with_manifest.dll, and a  manifest file, man2.manifest.  The merged manifests are received by a manifest in the resource file of another DLL, dll_with_merged_manifests. </p><p><i>mt.exe -inputresource:dll_with_manifest.dll;#1 -manifest man2.manifest -outputresource:dll_with_merged_manifest.dll;#3</i></p><p>To extract the manifest from a DLL, specify the DLL file name.  For example, the following command extracts the manifest from lib1.dll and  man3.manifest receives the extracted manifest.</p><p><i>mt.exe -inputresource:lib.dll;#1 -out:man3.manifest</i></p></td>
					</tr>
					<tr>
						<td>-outputresource </td>
						<td><p>Specifies an operation that generates a manifest to be received by  a resource of type RT_MANIFEST.  If  the <i>-outputresource</i> option is used without specifying the resource identifier, &lt;resource_id&gt;, the operation uses the value CREATEPROCESS_MANIFEST_RESOURCE. </p></td>
					</tr>
					<tr>
						<td>-updateresource </td>
						<td><p>Specifies an operation that is equivalent to using the <i>-inputresource</i>  and <i>-outputresource</i> options with identical arguments. For example, the following command requests an operation that computes a hash of the files at the specified  path and updates the manifest of a resource of a portable executable (PE).</p><p><i>mt.exe -updateresource:dll_with_manifest.dll;#1 -hashupdate:f:\files</i>.</p> </td>
					</tr>
					<tr>
						<td>-hashupdate </td>
						<td><p>Computes the hash value of the files at the specified paths and updates the value of the <strong>hash</strong> attribute of the <strong>File</strong> element with this value. </p><p>For example, the following command requests an operation that merges two manifest files, man1.manifest and man2.manifest, and updates the value of the <strong>hash</strong> attribute of the <strong>File</strong> element in the manifest that receives the merged information, merged.manifest.</p><p><i>mt.exe -manifest man1.manifest man2.manifest -hashupdate:d:\filerepository -out:merged.manifest</i></p><p>If the paths to the files are not specified, the operation searches location of the manifest specified to receive the update. For example,  the following command requests an operation that computes the updated hash value using files found by searching the location of updated.manifest.</p><p><i>mt.exe -manifest yourComponent.manifest -hashupdate -out:updated.manifest</i></p></td>
					</tr>
					<tr>
						<td>-validate_manifest </td>
						<td><p>Specifies an operation that performs a syntax check of the conformance of the manifest with the manifest schema.  For example, the following command requests a  check to validate the conformance of man1.manifest with its schema. </p><p><i>mt.exe -manifest man1.manifest -validate_manifest</i></p> </td>
					</tr>
					<tr>
						<td>-validate_file_hashes </td>
						<td><p>Specifies an operation that validates the hash values of the <strong>File</strong> elements of the manifest. For example, the following command requests an operation that validates the hash values of all the  <strong>File</strong> elements of the man1.manifest.</p><p><i>mt.exe -manifest man1.manifest -validate_file_hashes:"c;\files"</i></p> </td>
					</tr>
					<tr>
						<td>-canonicalize </td>
						<td><p>Specifies an operation to update the manifest to canonical form. For example, the following command updates man1.manifest to canonical form.</p><p><i>mt.exe -manifest man1.manifest</i></p> </td>
					</tr>
					<tr>
						<td>-check_for_duplicates </td>
						<td><p>Specifies an operation that checks the manifest for duplicate elements. For example, the following command checks man1.manifest for duplicate elements.</p><p><i>mt.exe -man1.manifest -check_for_duplicates</i></p> </td>
					</tr>					
					<tr>
						<td>-makecdfs</td>
						<td><p>Generates .cdf files to make catalogs.  For example, to the following command requests an operation that updates the hash value and generates a .cdf file.</p><p><i>mt.exe -manifest comp1.manifest -hashupdate -makecdfs -out:updated.manifest</i></p></td>
					</tr>
					<tr>
						<td>-verbose</td>
						<td>Displays verbose debugging information. </td>
					</tr>
					<tr>
						<td>-?</td>
						<td>When run with -?, or with no options and arguments, Mt.exe displays help text.</td>
					</tr>
				</table>



 

## Related topics

<dl> <dt>

[Side-by-Side Assembly Development Tools](side-by-side-assembly-development-tools.md)
</dt> </dl>

 

