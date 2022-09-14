---
description: A CryptoAPI tool that creates a catalog file.
ms.assetid: 233b3644-f2a5-4166-bac0-30bf2f54e957
title: MakeCat
ms.topic: article
ms.date: 05/31/2018
---

# MakeCat

The MakeCat tool is a CryptoAPI tool that creates a catalog file. MakeCat is available as part of the Microsoft Windows Software Development Kit (SDK) for Windows 7 and .NET Framework 4.0 and is installed, by default, in the \\Bin folder of the SDK installation path.

The MakeCat tool uses the following command syntax:

**MakeCat** \[**-n**\|**-r**\|**-v**\] *FileName*

## Parameters



| Parameter             | Description                                                                                                                                                              |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **-n**<br/>     | Do not stop on a recoverable error.<br/>                                                                                                                           |
| **-r**<br/>     | Forces MakeCat to end if it encounters recoverable errors. Specifically, it will end when processing the entries in the catalog files section of a .cdf file.<br/> |
| **-v**<br/>     | Verbose. Displays all progress and error messages.<br/>                                                                                                            |
| *FileName*<br/> | Name of the .cdf file to be parsed. For required structure and contents, see Remarks.<br/>                                                                         |



 

## Remarks

The .cdf file must be built with the following specifications.

``` syntax
[CatalogHeader]
Name=Name              
ResultDir=ResultDir   
PublicVersion=[|1]
CatalogVersion = [|1|2]
HashAlgorithms=[|SHA1|SHA256]
PageHashes=[true|false]
EncodingType=Encodingtype 
CATATTR1={type}:{oid}:{value} (optional)
CATATTR2={type}:{oid}:{value} (optional)

[CatalogFiles]
{reference tag}=file path and name
{reference tag}ALTSIPID={guid} (optional)
{reference tag}ATTR1={type}:{oid}:{value} (optional)
{reference tag}ATTR2={type}:{oid}:{value} (optional)
<HASH>kernel32.dll=kernel32.dll
<HASH>ntdll.dll=ntdll.dll
```

> [!Note]  
> The last entry in the .cdf file must always have an explicit newline character at the end of the line.

 

The \[CatalogHeader\] section defines information about the entire catalog file.



| Option                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Name<br/>           | Name of the catalog file, including its extension.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ResultDir<br/>      | Directory where the created .cat file will be placed. If not indicated, the default current directory is used. If the directory does not exist, it is created.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| PublicVersion<br/>  | This option is not supported. <br/> **Windows Server 2008 R2, Windows 7, Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP:** Catalog version. If left blank, the default value, 1, is used.<br/> <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| CatalogVersion<br/> | Catalog version. If the version is not present or is set to 1, then "0x100" is passed to the *dwPublicVersion* parameter of the [**CryptCATOpen**](/windows/desktop/api/Mscat/nf-mscat-cryptcatopen) function, and a version 1 catalog file is created. The HashAlgorithms option must be empty or contain SHA1.<br/> If the version is set to 2, then "0x200" is passed to the *dwPublicVersion* parameter of the [**CryptCATOpen**](/windows/desktop/api/Mscat/nf-mscat-cryptcatopen) function, and a version 2 catalog file is created. The HashAlgorithms option must contain SHA256.<br/> If this option is present but contains any value other than 1 or 2, the MakeCat tool will error out.<br/> **Windows Server 2008 R2, Windows 7, Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP:** This option is not supported.<br/> <br/> |
| HashAlgorithms<br/> | Name of the hashing algorithm used. For more information, see the CatalogVersion option.<br/> **Windows Server 2008 R2, Windows 7, Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP:** This option is not supported.<br/> <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| PageHashes<br/>     | Specifies whether to hash the files listed in the &lt;HASH&gt; option in the \[CatalogFiles\] section<br/> **Windows Server 2008 R2, Windows 7, Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP:** This option is not supported.<br/> <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| EncodingType<br/>   | Type of message encoding used. If left blank, the default EncodingType is PKCS\_7\_ASN\_ENCODING \| X509\_ASN\_ENCODING, 0x00010001. <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |



 

The \[CatalogFiles\] section defines each member of the catalog file with files of various types and attributes of various types in separate groups.



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
<td>reference tag<br/></td>
<td>Text reference to the file. This can include any ASCII text characters except the equal sign (=). The system must be able to reproduce this tag after installation. <br/> Use &lt;HASH&gt; as a prefix of the file name. This results in the tag being the file's hash in ASCII string form. <br/></td>
</tr>
<tr class="even">
<td>file path and name<br/></td>
<td>The file name, including the extension to be parsed and the relative path to the file. Any type of file that can be signed with SignTool can be added to a catalog. For example, file names with the following extensions, among others, can be added to a catalog: .exe, .cab, .cat, .ocx, .dll, and .stl.<br/></td>
</tr>
<tr class="odd">
<td>ALTSIPID<br/></td>
<td>SIP GUID that is to be used for hashing instead of the standard SIP based on file type. This entry is optional. If this entry is omitted, the member will be hashed using the default SIP. If no default installed SIP is found, the Flat SIP will be used.<br/></td>
</tr>
<tr class="even">
<td>guid<br/></td>
<td>Text representation of a GUID.<br/></td>
</tr>
<tr class="odd">
<td>ATTRx<br/></td>
<td>Optional. Attribute or statement about the file or content. There can be any number of attributes, including none.<br/></td>
</tr>
<tr class="even">
<td>type<br/></td>
<td>Defines what type of attribute is being added in the format 0x00000000 (text). This option can be a bitwise-<strong>OR</strong> combination of zero or more of the following values:<br/>
<ul>
<li>0x10000000 Authenticated attribute (signed, included in the hash).</li>
<li>0x20000000 Unauthenticated attribute (unsigned, not included in the hash, not verifiable).</li>
<li>0x01000000 Attribute will not be replicated to SHA1 entries in a CatalogVersion 2 catalog.</li>
<li>0x00010000 Attribute is represented in plaintext. No conversion will be done.</li>
<li>0x00020000 Attribute is represented in base-64 encoding. This is used to represent binary data.</li>
<li>0x00000001 Attribute is a name-value pair. Use the oid option for the name. This attribute is slow; therefore, use this option sparingly.</li>
<li>0x00000002 Attribute is referenced by an <a href="/windows/desktop/SecGloss/o-gly"><em>object identifier</em></a> (OID).</li>
</ul>
<br/></td>
</tr>
<tr class="odd">
<td>oid<br/></td>
<td>The text representation of the attribute's reference key. It is an OID in the form of a text string in dotted quad notation (for example, a.b.c.d) or a text Name.<br/></td>
</tr>
<tr class="even">
<td>value<br/></td>
<td>The text representation of the value of the attribute. The type of text representation used depends on the value of the type option. The EOL characters determine the length.<br/></td>
</tr>
<tr class="odd">
<td>&lt;HASH&gt;<br/></td>
<td>Hashes the specified file.<br/></td>
</tr>
</tbody>
</table>



 

The generated catalog file is unsigned. If it is to be signed prior to transmittal, it is signed by using [SignTool](signtool.md).

 

 
