---
title: App packager (MakeAppx.exe)
description: App packager (MakeAppx.exe) creates an app package from files on disk or extracts the files from an app package to disk.
ms.assetid: 9B7BF420-8E19-4BFD-B378-D09E61F68A39
ms.topic: article
ms.date: 05/31/2018
---

# App packager (MakeAppx.exe)

> [!Note]  
> For UWP guidance on using this tool, see [Create an app package with the MakeAppx.exe tool](/windows/msix/package/create-app-package-with-makeappx-tool).

 

App packager (MakeAppx.exe) creates an app package from files on disk or extracts the files from an app package to disk. Starting with Windows 8.1, App packager also creates an app package bundle from app packages on disk or extracts the app packages from an app package bundle to disk. It is included in Microsoft Visual Studio and the Windows Software Development Kit (SDK) for Windows 8 or Windows Software Development Kit (SDK) for Windows 8.1 and newer. Visit [Downloads for developers]( https://msdn.microsoft.com/windows/apps/br229516.aspx) to get them.

The MakeAppx.exe tool is typically found in operating system version specific locations:

- C:\Program Files (x86)\Windows Kits\10\bin\<build number>\<architecture>\makeappx.exe

Where \<architecture> = x86, x64, arm, ar64 or chpe. Alternatively, it may be located in:

C:\Program Files (x86)\Windows Kits\10\App Certification Kit\makeappx.exe



-   [To create a package using a directory structure](#to-create-a-package-using-a-directory-structure)
-   [To create a package using a mapping file](#to-create-a-package-using-a-mapping-file)
-   [To sign the package using SignTool](#to-sign-the-package-using-signtool)
-   [To extract files from a package](#to-extract-files-from-a-package)
-   [To create a package bundle using a directory structure](#to-create-a-package-bundle-using-a-directory-structure)
-   [To create a package bundle using a mapping file](#to-create-a-package-bundle-using-a-mapping-file)
-   [To extract packages from a bundle](#to-extract-packages-from-a-bundle)
-   [To encrypt a package with a key file](#to-encrypt-a-package-with-a-key-file)
-   [To encrypt a package with a global test key](#to-encrypt-a-package-with-a-global-test-key)
-   [To decrypt a package with a key file](#to-decrypt-a-package-with-a-key-file)
-   [To decrypt a package with a global test key](#to-decrypt-a-package-with-a-global-test-key)
-   [Usage](#usage)

## Using App packager

> [!Note]  
> Relative paths are supported throughout the tool.

 

### To create a package using a directory structure

Place the AppxManifest.xml in the root of a directory containing all of the payload files for your app. An identical directory structure is created for the app package, and will be available when the package is extracted at deployment time.

1.  Place all files in a single directory structure, creating subdirectories as desired.

2.  Create a valid package manifest, AppxManifest.xml, and place it in the root directory.

3.  Run this command:

    **MakeAppx pack /d** *input\_directorypath* **/p** _filepath_**.appx**

### To create a package using a mapping file

1.  Create a valid package manifest, AppxManifest.xml.

2.  Create a mapping file. The first line contains the string **\[Files\]**, and the lines that follow specify the source (disk) and destination (package) paths in quoted strings.

    ``` syntax
    [Files]
    "C:\MyApp\StartPage.htm"     "default.html"
    "C:\MyApp\readme.txt"        "doc\readme.txt"
    "\\MyServer\path\icon.png"   "icon.png"
    "MyCustomManifest.xml"       "AppxManifest.xml"
    ```

3.  Run this command:

    **MakeAppx pack /f** *mapping\_filepath* **/p** _filepath_**.appx**

### To sign the package using SignTool

1.  Create the certificate. The publisher listed in the manifest must match the publisher subject information of the signing certificate. For more info about creating a signing certificate, see [How to create an app package signing certificate](how-to-create-a-package-signing-certificate.md).

2.  Run SignTool.exe to sign the package:

    **SignTool sign /a /v /fd** *hashAlgorithm* **/f** *certFileName* _filepath_**.appx**

    The *hashAlgorithm* must match the hash algorithm used to create the blockmap when the app was packaged. With the MakeAppx packaging utility, the default Appx blockmap hash algorithm is **SHA256**. Run SignTool.exe specifying **SHA256** as the file digest (/fd) algorithm:

    **SignTool sign /a /v /fd SHA256 /f** *certFileName* _filepath_**.appx**

    For more info about how to sign packages, see [How to sign an app package using SignTool](how-to-sign-a-package-using-signtool.md).

### To extract files from a package

1.  Run this command:

    **MakeAppx unpack /p** _file_**.appx /d** *output\_directory*

2.  The unpacked package has the same structure as the installed package.

### To create a package bundle using a directory structure

We use the **bundle** command to create an app bundle at \<output bundle name\> by adding all packages from \<content directory\> (including subfolders). If \<content directory\> contains a bundle manifest, AppxBundleManifest.xml, it is ignored.

1.  Place all packages in a single directory structure, creating subdirectories as desired.

2.  Run this command:

    **MakeAppx bundle /d** *input\_directorypath* **/p** _filepath_**.appxbundle**

### To create a package bundle using a mapping file

We use the **bundle** command to create an app bundle at \<output bundle name\> by adding all packages from a list of packages within \<mapping file\>. If \<mapping file\> contains a bundle manifest, AppxBundleManifest.xml, it is ignored.

1.  Create a \<mapping file\>. The first line contains the string **\[Files\]**, and the lines that follow specify the packages to add to the bundle. Each package is described by a pair of paths in quotation marks, separated by spaces or tabs. The pair of paths represents the package's source (on disk) and destination (in bundle). All destination package names must have the .appx extension.

    ``` syntax
        [Files]
        "C:\MyApp\MyApp_x86.appx"                 "MyApp_x86.appx"
        "C:\Program Files (x86)\ResPack.appx"    "resources\resPack.appx"
        "\\MyServer\path\ResPack.appx"           "Respack.appx"
        "my app files\respack.appx"              "my app files\respack.appx"
    ```

2.  Run this command:

    **MakeAppx bundle /f** *mapping\_filepath* **/p** _filepath_**.appxbundle**

### To extract packages from a bundle

1.  Run this command:

    **MakeAppx unbundle /p** _bundle\_name_**.appxbundle /d** *output\_directory*

2.  The unpacked bundle has the same structure as the installed package bundle.

### To encrypt a package with a key file

1.  Create a key file. Key files must begin with a line containing the string "\[Keys\]" followed by lines describing the keys to encrypt the package with. Each key is described by a pair of strings in quotation marks, separated by spaces or tabs. The first string represents the key ID and the second string represents the encryption key in hexadecimal form.

    ``` syntax
        [Keys]
        "0"                 "1AC4CDCFF1924D2885A0607269787BA6BF09B7FFEBF74ED4B9D86E423CF9186B"
    ```

2.  Run this command:

    **MakeAppx.exe encrypt /p** _package\_name_**.appx /ep** _encrypted\_package\_name_**.eappx /kf** _keyfile\_name_**.txt**

3.  The input package will be encrypted into the specified encrypted package using the provided key file.

### To encrypt a package with a global test key

1.  Run this command:

    **MakeAppx.exe encrypt /p** _package\_name_**.appx /ep** _encrypted\_package\_name_**.eappx /kt**

2.  The input package will be encrypted into the specified encrypted package using the global test key.

### To decrypt a package with a key file

1.  Create a key file. Key files must begin with a line containing the string "\[Keys\]" followed by lines describing the keys to encrypt the package with. Each key is described by a pair of strings in quotation marks, separated by spaces or tabs. The first string represents the base64 encoded 32-byte key ID and the second string represents the base64 encoded 32-byte encryption key.

    ``` syntax
        [Keys]
        "OWVwSzliRGY1VWt1ODk4N1Q4R2Vqc04zMzIzNnlUREU="                 "MjNFTlFhZGRGZEY2YnVxMTBocjd6THdOdk9pZkpvelc="
    ```

2.  Run this command:

    **MakeAppx.exe decrypt /p** _package\_name_**.appx /ep** _unencrypted\_package\_name_**.eappx /kf** _keyfile\_name_**.txt**

3.  The input package will be decrypted into the specified unencrypted package using the provided key file.

### To decrypt a package with a global test key

1.  Run this command:

    **MakeAppx.exe decrypt /p** _package\_name_**.appx /ep** _unencrypted\_package\_name_**.eappx /kt**

2.  The input package will be decrypted into the specified unencrypted package using the global test key.

## Usage

The command line argument **/p** is always required, with either **/d**, **/f**, or **/ep**. Note that **/d**, **/f**, and **/ep** are mutually exclusive.

**MakeAppx pack \[options\]** **/p** *\<output package name\>* **/d** *\<content directory\>*

**MakeAppx pack \[options\]** **/p** *\<output package name\>* **/f** *\<mapping file\>*

**MakeAppx unpack \[options\]** **/p** *\<input package name\>* **/d** *\<output directory\>*

**MakeAppx bundle \[options\]** **/p** *\<output bundle name\>* **/d** *\<content directory\>*

**MakeAppx bundle \[options\]** **/p** *\<output bundle name\>* **/f** *\<mapping file\>*

**MakeAppx unbundle \[options\]** **/p** *\<input bundle name\>* **/d** *\<output directory\>*

**MakeAppx encrypt \[options\]** **/p** *\<input package name\>* **/ep** *\<output package name\>*

**MakeAppx decrypt \[options\]** **/p** *\<input package name\>* **/ep** *\<output package name\>*

## Command-line Syntax

Here is the command-line common usage syntax for MakeAppx.

**MakeAppx \[pack\|unpack\|bundle\|unbundle\|encrypt\|decrypt\]** \[**/h** **/kf** **/kt** **/l** **/o** **/no** **/nv** **/v** **/pfn** **/?**\]

**MakeAppx** packs or unpacks the files in a package, bundles or unbundles the packages in a bundle, or encrypts or decrypts the app package or bundle in the specified input directory or mapping file. Here is the list of parameters that apply to **MakeAppx pack**, **MakeAppx unpack**, **MakeAppx bundle**, **MakeAppx unbundle**, **MakeAppx encrypt**, or **MakeAppx decrypt**.

<dl> <dt>

<span id="_l"></span><span id="_L"></span>**/l**
</dt> <dd>

This option is used for localized packages. The default validation trips on localized packages. This option disables only that specific validation, without requiring that all validation be disabled.

</dd> <dt>

<span id="_o"></span><span id="_O"></span>**/o**
</dt> <dd>

Overwrite the output file if it exists. If you don't specify this option or the **/no** option, the user is asked whether they want to overwrite the file.

You can't use this option with **/no**.

</dd> <dt>

<span id="_no"></span><span id="_NO"></span>**/no**
</dt> <dd>

Prevents an overwrite of the output file if it exists. If you don't specify this option or the **/o** option, the user is asked whether they want to overwrite the file.

You can't use this option with **/o**.

</dd> <dt>

<span id="_nv"></span><span id="_NV"></span>**/nv**
</dt> <dd>

Skip semantic validation. If you don't specify this option, the tool performs a full validation of the package.

</dd> <dt>

<span id="_v"></span><span id="_V"></span>**/v**
</dt> <dd>

Enable verbose logging output to the console.

</dd> <dt>

<span id="__"></span>**/?**
</dt> <dd>

Display help text.

</dd> </dl>

**MakeAppx pack** , **MakeAppx unpack** , **MakeAppx bundle**, **MakeAppx unbundle**, **MakeAppx encrypt**, and **MakeAppx decrypt** are mutually exclusive commands. Here are the command-line parameters that apply specifically to each command:

**MakeAppx pack** \[**h**\]

Creates a package.

<dl> <dt>

<span id="_h_algorithm"></span><span id="_H_ALGORITHM"></span>**/h** *algorithm*
</dt> <dd>

Specifies the hash algorithm to use when creating the block map. Here are valid values for *algorithm*:

<dl> <dd>SHA256 (default)</dd> <dd>SHA384</dd> <dd>SHA512</dd> </dl>

You can't use this option with the **unpack** command.

</dd> </dl>

**MakeAppx unpack** \[**pfn**\]

Extracts all files in the specified package to the specified output directory. The output has the same directory structure as the package.

<dl> <dt>

<span id="_pfn"></span><span id="_PFN"></span>**/pfn**
</dt> <dd>

Specifies a directory named with the package full name. This directory is created under the provided output location. You can't use this option with the **pack** command.

</dd> </dl>

**MakeAppx unbundle** \[**pfn**\]

Unpacks all packages to a subdirectory under the specified output path, named after the bundle full name. The output has the same directory structure as the installed package bundle.

<dl> <dt>

<span id="_pfn"></span><span id="_PFN"></span>**/pfn**
</dt> <dd>

Specifies a directory named with the package bundle full name. This directory is created under the provided output location. You can't use this option with the **bundle** command.

</dd> </dl>

**MakeAppx encrypt** \[**kf**, **kt**\]

Creates an encrypted app package from the specified input app package at the specified output package.

<dl> <dt>

<span id="_kf__key_file_"></span><span id="_KF__KEY_FILE_"></span>**/kf** *\<key file\>*
</dt> <dd>

Encrypts the package or bundle using the key from the specified key file. You can't use this option with **kt**.

</dd> <dt>

<span id="_kt"></span><span id="_KT"></span>**/kt**
</dt> <dd>

Encrypts the package or bundle using the global test key. You can't use this option with **kf**.

</dd> </dl>

**MakeAppx decrypt** \[**kf**, **kt**\]

Creates an unencrypted app package from the specified input app package at the specified output package.

<dl> <dt>

<span id="_kf__key_file_"></span><span id="_KF__KEY_FILE_"></span>**/kf** *\<key file\>*
</dt> <dd>

Decrypts the package or bundle using the key from the specified key file. You can't use this option with **kt**.

</dd> <dt>

<span id="_kt"></span><span id="_KT"></span>**/kt**
</dt> <dd>

Decrypts the package or bundle using the global test key. You can't use this option with **kf**.

</dd> </dl>

## Semantic validation performed by MakeAppx

MakeAppx performs limited semantic validation that is designed to catch the most common deployment errors and help ensure that the app package is valid.

This validation ensures that:

-   All files referenced in the package manifest are included in the app package.
-   An application does not have two identical keys.
-   An application does not register for a forbidden protocol from this list: SMB , FILE, MS-WWA-WEB, MS-WWA.

This semantic validation is not complete, and packages built by MakeAppx are not guaranteed to be installable.

 

 
