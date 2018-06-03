---
title: File API configuration
description: The File API's behavior can be configured through settings in the registry.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 930878C2-D2B4-45F1-885F-64927CEBAC1D
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# File API configuration

The File API's behavior can be configured through settings in the registry.

The File API provides two kinds of protection; native protection and PFile protection.

-   **Native protection** - the file is protected to an AD RMS format based on its MIME type (file name extension).
-   **PFile protection** - the file is protected to the AD RMS Protected File (PFile) format.

For more information about supported file formats, see **File API File Support Details** in this topic.

The following table describes the keys and key values that control encryption.



<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Key/Key Value, Type, Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>HKEY_LOCAL_MACHINE</strong>\<strong>Software</strong>\<strong>Microsoft</strong>\<strong>MSIPC</strong>\<strong>FileProtection</strong><br/> <br/> <strong>Type:</strong> Key<br/> <strong>Description:</strong> Contains general configuration for the File API.<br/></td>
</tr>
<tr class="even">
<td><strong>HKEY_LOCAL_MACHINE</strong>\<strong>Software</strong>\<strong>Microsoft</strong>\<strong>MSIPC</strong>\<strong>FileProtection</strong>\<strong>&lt;EXT&gt;</strong><br/> <br/> <strong>Type:</strong> Key<br/> <strong>Description:</strong> Specifies configuration information for a specific file extension; for example, TXT, JPG, and so on.<br/>
<ul>
<li>The wildcard character, '*', is allowed; however, a setting for a specific extension takes precedence over the wild card setting. The wildcard character does not affect settings for Microsoft Office files; these must be explicitly disabled by file type.</li>
<li>To specify files that do not have an extension, use '.'</li>
<li>Do not specify the '.' character when specifying the key for a specific file extension; for example use <strong>HKEY_LOCAL_MACHINE</strong>\<strong>Software</strong>\<strong>Microsoft</strong>\<strong>MSIPC</strong>\<strong>FileProtection</strong>\<strong>TXT</strong> to specify settings for .txt files. (Do not use <strong>HKEY_LOCAL_MACHINE</strong>\<strong>Software</strong>\<strong>Microsoft</strong>\<strong>MSIPC</strong>\<strong>FileProtection</strong>\<strong>.TXT</strong>).<br/></li>
</ul>
Set the <strong>Encryption</strong> value in the key to specify protection behavior. If the <strong>Encryption</strong> value is not set, the default behavior for the file type is observed.<br/></td>
</tr>
<tr class="odd">
<td><strong>HKEY_LOCAL_MACHINE</strong>\<strong>Software</strong>\<strong>Microsoft</strong>\<strong>MSIPC</strong>\<strong>FileProtection</strong>\<strong>&lt;EXT&gt;</strong>\<strong>Encryption</strong><br/> <br/> <strong>Type:</strong> <strong>REG_SZ</strong><br/> <strong>Description:</strong> Contains one of three values:<br/>
<ul>
<li><p><strong>Off</strong> Encryption is disabled.</p>
<blockquote>
[!Note]<br />
This setting has no bearing on decryption. Any encrypted file, whether encrypted using Native or Pfile protection, can be decrypted, as long as the user has the <strong>EXTRACT</strong> right.
</blockquote>
<p><br/></p></li>
<li><strong>Native</strong> Native encryption is used. For Office files the encrypted file will have the same extension as the original file. For example, a file with the .docx file extension will be encrypted to a file with an extension of .docx. For other files that can have native protection applied, the file will be encrypted to a file with an extension of the format p<em>zzz</em>, where <em>zzz</em> is the original file extension. For example .txt files will be encrypted to a file with an extension of .ptxt. A list of file extensions that can have native protection applied is included below.</li>
<li><p><strong>Pfile</strong> PFile encryption is used. The encrypted file will have .pfile appended to the original extension. For example, after encryption, a .txt file, will have an extension of .txt.pfile.</p>
<blockquote>
[!Note]<br />
This setting has no bearing on Office file formats. For example, if the <strong>HKEY_LOCAL_MACHINE</strong>\<strong>Software</strong>\<strong>Microsoft</strong>\<strong>MSIPC</strong>\<strong>FileProtection</strong>\<strong>DOCX</strong>\<strong>Encryption</strong><br/> value is set to &quot;Pfile , .docx files will still be encrypted using native protection, and the encrypted file will still have a file extension of .docx.
</blockquote>
<p><br/></p></li>
</ul>
Setting any other value or setting no value results in default behavior.<br/></td>
</tr>
</tbody>
</table>



 

**Default behavior for different file formats**

-   **Office files** Native encryption is enabled.
-   **txt, xml, jpg, jpeg, pdf, png, tiff, bmp, gif, giff, jpe, jfif, jif files** Native encryption is enabled (xxx becomes pxxx)
-   **All other files** Encryption is protected file (pfile) enabled (xxx become xxx.pfile)

If encryption is attempted on a file type that is blocked, an [**IPCERROR\_FILE\_ENCRYPT\_BLOCKED**](error-codes.md) error occurs.

### File API - File Support Details

Native support can be added for any file type (extension) . For instance,any extension &lt;ext&gt; (non-office), \*.p&lt;ext&gt; will be used if the admin configuration for that extension is "NATIVE".

**Office files**

-   File extensions: doc, dot, xla, xls, xlt, pps, ppt, docm, docx, dotm, dotx, xlam, xlsb, xlsm, xlsx, xltm, xltx, xps, potm, potx, ppsx, ppsm, pptm, pptx, thmx.
-   Protection type = Native (default): sample.docx is encrypted to sample.docx
-   Protection type = Pfile: For Office files has the same effect as Native.
-   Off: Disables encryption.

**PDF files**

-   Protection type = Native: sample.pdf is encrypted and named sample.ppdf
-   Protection type = Pfile: sample.pdf is encrypted and named sample.pdf.pfile.
-   Off: Disables encryption.

**All other file formats**

-   Protection type = Pfile: sample.*zzz* is encrypted and named sample.*zzz*.pfile; where zzz is the original file extension.
-   Off: Disables encryption.

### Examples

The following settings enable PFile encryption for txt files. Office files will have native protection applied (by default), txt files will have PFile protection applied, and all other files will have protection blocked (by default).

```
HKEY_LOCAL_MACHINE
   Software
      Microsoft
         MSIPC
            FileProtection
               txt
                  Encryption = Pfile
```

The following settings enable PFile encryption for all non-Office files except txt files. Office files will have native protection applied (by default), txt files will have protection blocked, and all other files will have PFile protection applied.

```
HKEY_LOCAL_MACHINE
   Software
      Microsoft
         MSIPC
            FileProtection
               *
                  Encryption = Pfile
               txt
                  Encryption = Off
```

The following settings disable native encryption for docx files. Office files, except for docx files, will have native protection applied (by default) and all other files will have protection blocked (by default).

```
HKEY_LOCAL_MACHINE
   Software
      Microsoft
         MSIPC
            FileProtection
               docx
                  Encryption = Off
```

## Related topics

<dl> <dt>

[Developer notes](developer-notes.md)
</dt> <dt>

[**IPCERROR\_FILE\_ENCRYPT\_BLOCKED**](error-codes.md)
</dt> </dl>

 

 





