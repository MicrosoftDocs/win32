---
Description: SignTool is a Windows command-line tool for code signing, date stamping files, creating Windows digital signatures, and for verifying digital signatures.
ms.assetid: aa59cb35-5fba-4ce8-97ea-fc767c83f88e
title: SignTool
ms.topic: article
ms.date: 05/31/2018
---

# SignTool

The SignTool tool is a command-line tool that digitally signs files, verifies signatures in files, or time stamps files. For information about why signing files is important, see [Introduction to Code Signing](cryptography-tools.md). The tool is installed in the \\Bin folder of the Microsoft Windows Software Development Kit (SDK) installation path.

SignTool is available as part of the Windows SDK, which you can download from <http://go.microsoft.com/fwlink/p/?linkid=84091>.

**Windows Server 2008 R2 and Windows 7:  **

If you are using the [**WinVerifyTrust**](/windows/desktop/api/Wintrust/nf-wintrust-winverifytrust) function to verify multiple embedded signatures or support strong cryptography policy, you must include the following files:

-   Microsoft.Windows.Build.Signing.wintrust.dll.manifest
-   Wintrust.dll (downlevel version)

If you want to perform dual signing and make SHA256 catalogs, you must include those files and the following additional files:

-   Makecat.exe
-   Makecat.exe.manifest
-   Microsoft.Windows.Build.Signing.mssign32.dll.manifest
-   Mssign32.dll (downlevel version)
-   Signtool.exe
-   Signtool.exe.manifest

Here is the syntax for SignTool:

**signtool** \[*Command*\]\[*Options*\]\[*FileName* …\]

The following commands are supported by SignTool. 

| Command        | Description                                                                                                                                                                                                |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **catdb**      | Adds or removes a catalog file to or from a catalog database.<br/>                                                                                                                                   |
| **sign**       | Digitally signs files.<br/>                                                                                                                                                                          |
| **signwizard** | This command is not supported.<br/> **Windows Vista and earlier:** Launches the signing wizard. Only a single file can be specified for the file name command-line parameter.<br/> <br/> |
| **timestamp**  | Time stamps files.<br/>                                                                                                                                                                              |
| **verify**     | Verifies the digital signature of files.<br/>                                                                                                                                                        |



 

The following options apply to the **catdb** command. 

| Catdb option  | Description                                                                                                                                                                                                                                                                                                                     |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **/d**        | Specifies that the default catalog database be updated. If neither the **/d** nor **/g** option is used, SignTool updates the system component and driver database.<br/>                                                                                                                                                  |
| **/g** *GUID* | Specifies that the catalog database identified by the GUID be updated.<br/>                                                                                                                                                                                                                                               |
| **/r**        | Removes the specified catalog from the catalog database. If this option is not specified, SignTool will add the specified catalog to the catalog database.<br/>                                                                                                                                                           |
| **/u**        | Specifies that a unique name be automatically generated for the added catalog files. If necessary, the catalog files are renamed to prevent name conflicts with existing catalog files. If this option is not specified, SignTool overwrites any existing catalog that has the same name as the catalog being added.<br/> |



 

> [!Note]  
> Catalog databases are used for automatic lookup of catalog files.

 

The following options apply to the **sign** command. 

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Sign option</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>/a</strong></td>
<td>Selects the best signing certificate automatically. If this option is not present, SignTool expects to find only one valid signing certificate.<br/></td>
</tr>
<tr class="even">
<td><strong>/ac</strong> <em>FileName</em></td>
<td>Specifies a file that contains an additional certificate to add to the signature block.<br/></td>
</tr>
<tr class="odd">
<td><strong>/as</strong></td>
<td>Appends this signature. If no primary signature is present, this signature is made the primary signature.<br/></td>
</tr>
<tr class="even">
<td><strong>/c</strong> <em>CertTemplateName</em></td>
<td>Specifies the Certificate Template Name (a Microsoft extension) for the signing certificate.<br/></td>
</tr>
<tr class="odd">
<td><strong>/csp</strong> <em>CSPName</em></td>
<td>Specifies the <a href="https://msdn.microsoft.com/en-us/library/ms721572(v=VS.85).aspx"><em>cryptographic service provider</em></a> (CSP) that contains the <a href="https://msdn.microsoft.com/en-us/library/ms721603(v=VS.85).aspx"><em>private key</em></a> container.<br/></td>
</tr>
<tr class="even">
<td><strong>/d</strong> <em>Desc</em></td>
<td>Specifies a description of the signed content.<br/></td>
</tr>
<tr class="odd">
<td><strong>/dg</strong> <em>Path</em></td>
<td>Generates the to be signed digest and the unsigned PKCS7 files. The output digest and PKCS7 files will be: <em>Path</em>\<em>FileName.dig</em> and <em>Path</em>\<em>FileName.p7u</em>. To output an additional XML file, see <strong>/dxml</strong>.<br/></td>
</tr>
<tr class="even">
<td><strong>/di</strong> <em>Path</em></td>
<td>Creates the signature by ingesting the signed digest to the unsigned PKCS7 file. The input signed digest and unsigned PKCS7 files should be: <em>Path</em>\<em>FileName.dig.signed</em> and <em>Path</em>\<em>FileName.p7u</em>. <br/></td>
</tr>
<tr class="odd">
<td><strong>/dlib</strong> <em>DLL</em></td>
<td>Specifies the DLL implementing the <code>AuthenticodeDigestSign</code> function to sign the digest with. This option is equivalent to using <strong>SignTool</strong> separately with the <strong>/dg</strong>, <strong>/ds</strong>, and <strong>/di</strong> switches, except this option invokes all three as one atomic operation. <br/></td>
</tr>
<tr class="even">
<td><strong>/dmdf</strong> <em>FileName</em></td>
<td>When used with the <strong>/dg</strong> option, passes the file’s contents to the <code>AuthenticodeDigestSign</code> function without modification.<br/></td>
</tr>
<tr class="odd">
<td><strong>/ds</strong></td>
<td>Signs the digest only. The input file should be the digest generated by the <strong>/dg</strong> option. The output file will be: <em>File.signed</em>.<br/></td>
</tr>
<tr class="even">
<td><strong>/du</strong> <em>URL</em></td>
<td>Specifies a URL for expanded description of the signed content.<br/></td>
</tr>
<tr class="odd">
<td><strong>/dxml</strong></td>
<td>When used with the <strong>/dg</strong> option, produces an XML file. The output file will be: <em>Path</em>\<em>FileName.dig.xml</em>.<br/></td>
</tr>
<tr class="even">
<td><strong>/f</strong> <em>SignCertFile</em></td>
<td>Specifies the signing certificate in a file. Only the Personal Information Exchange (PFX) file format is supported. You can use the PVK2PFX.exe tool to convert SPC and PVK files to PFX format.<br/> If the file is in PFX format protected by a password, use the <strong>/p</strong> option to specify the password. If the file does not contain private keys, use the <strong>/csp</strong> and <strong>/k</strong> options to specify the CSP and private key container name, respectively.<br/></td>
</tr>
<tr class="odd">
<td><strong>/i</strong> <em>IssuerName</em></td>
<td>Specifies the name of the issuer of the signing certificate. This value can be a substring of the entire issuer name.<br/></td>
</tr>
<tr class="even">
<td><strong>/fd</strong></td>
<td>Specifies the file digest algorithm to use to create file signatures. The default algorithm is <a href="https://msdn.microsoft.com/en-us/library/ms721625(v=VS.85).aspx"><em>Secure Hash Algorithm</em></a> (SHA-1).<br/> <strong>Windows Vista and earlier:</strong> This flag is not supported.<br/></td>
</tr>
<tr class="odd">
<td><strong>/j</strong> <em>DLL</em></td>
<td>This flag is not supported.<br/> <strong>Windows Vista and earlier:</strong> Specifies the name of a DLL that provides attributes of the signature.<br/></td>
</tr>
<tr class="even">
<td><strong>/jp</strong> <em>ParameterName</em></td>
<td>This flag is not supported.<br/> <strong>Windows Vista and earlier:</strong> Specifies a parameter that is passed to the DLL specified by the <strong>/j</strong> command.<br/></td>
</tr>
<tr class="odd">
<td><strong>/kc</strong> <em>Name</em></td>
<td>Specifies the key that contains the name of the private key.<br/></td>
</tr>
<tr class="even">
<td><strong>/n</strong> <em>SubjectName</em></td>
<td>Specifies the name of the subject of the signing certificate. This value can be a substring of the entire subject name.<br/></td>
</tr>
<tr class="odd">
<td><strong>/nph</strong></td>
<td>If supported, suppresses page hashes for executable files. The default behavior is determined by the <strong>SIGNTOOL_PAGE_HASHES</strong> environment variable and by the Wintrust.dll version. This option is ignored for non-PE files.<br/></td>
</tr>
<tr class="even">
<td><strong>/p</strong> <em>Password</em></td>
<td>Specifies the password to use when opening a PFX file. A PFX file can be specified by using the <strong>/f</strong> option. For information about protecting passwords, see <a href="https://msdn.microsoft.com/en-us/library/ms717799(v=VS.85).aspx">Handling Passwords</a>.<br/></td>
</tr>
<tr class="odd">
<td><strong>/p7</strong> <em>Path</em></td>
<td>Specifies that for each specified content file, a PKCS #7 file is produced. The produced PKCS #7 file is named <em>Path</em>\<em>FileName</em>.p7.<br/></td>
</tr>
<tr class="even">
<td><strong>/p7ce</strong> <em>Value</em></td>
<td>Specifies options for the signed PKCS #7 content. Set <em>Value</em> to &quot;Embedded&quot; to embed the signed content in the PKCS #7 file, or set <em>Value</em> to &quot;DetachedSignedData&quot; to produce the signed data portion of a detached PKCS #7 file. If this option is not used, then the default choice is &quot;Embedded&quot;.<br/></td>
</tr>
<tr class="odd">
<td><strong>/p7co</strong> <em>OID</em></td>
<td>Specifies the <a href="https://msdn.microsoft.com/en-us/library/ms721599(v=VS.85).aspx"><em>object identifier</em></a> (OID) that identifies the signed PKCS #7 content.<br/></td>
</tr>
<tr class="even">
<td><strong>/ph</strong></td>
<td>If supported, generates page hashes for executable files. This option is ignored for non-PE files.<br/></td>
</tr>
<tr class="odd">
<td><strong>/r</strong> <em>RootSubjectName</em></td>
<td>Specifies the name of the subject of the root certificate that the signing certificate must chain to. This value can be a substring of the entire subject name of the root certificate.<br/></td>
</tr>
<tr class="even">
<td><strong>/s</strong> <em>StoreName</em></td>
<td>Specifies the store to open when searching for the certificate. If this option is not specified, the My store is opened.<br/></td>
</tr>
<tr class="odd">
<td><strong>/sha1</strong> <em>Hash</em></td>
<td>Specifies the SHA1 hash of the signing certificate.<br/></td>
</tr>
<tr class="even">
<td><strong>/sm</strong></td>
<td>Specifies that a computer store, instead of a user store, be used.<br/></td>
</tr>
<tr class="odd">
<td><strong>/snk</strong> <em>FileName</em></td>
<td>This flag is not supported.<br/> <strong>Windows Vista and earlier:</strong> Specifies the SNK file that contains the strong name private key.<br/></td>
</tr>
<tr class="even">
<td><strong>/sncsp</strong> <em>Name</em></td>
<td>This flag is not supported.<br/> <strong>Windows Vista and earlier.:</strong> Specifies the CSP that contains the strong name private key container.<br/></td>
</tr>
<tr class="odd">
<td><strong>/snkc</strong> <em>Name</em></td>
<td>This flag is not supported.<br/> <strong>Windows Vista and earlier:</strong> Specifies the key that contains the name of the strong name private key.<br/></td>
</tr>
<tr class="even">
<td><strong>/snks</strong> {<strong>1</strong>|<strong>2</strong>}</td>
<td>This flag is not supported.<br/> <strong>Windows Vista and earlier:</strong> Specifies which strong name private key to use. If this argument is not used, the default value 2 is assumed.<br/> The following values are supported:<br/> <br/> <dl> <dt><span id="1"></span>1</dt> <dd> AT_KEYEXCHANGE<br/> </dd> <dt><span id="2__default_"></span><span id="2__DEFAULT_"></span>2 (default)</dt> <dd> AT_SIGNATURE<br/> </dd> </dl> <br/></td>
</tr>
<tr class="odd">
<td><strong>/t</strong> <em>URL</em></td>
<td>Specifies the URL of the time stamp server. If this option is not present, then the signed file will not be time stamped. A warning is generated if time stamping fails.<br/></td>
</tr>
<tr class="even">
<td><strong>/td</strong> <em>alg</em></td>
<td>Used with the <strong>/tr</strong> switch to request a digest algorithm used by the RFC 3161 time stamp server.<br/>
<blockquote>
[!Note]<br />
The <strong>/td</strong> switch must be declared after the <strong>/tr</strong> switch, not before. If the <strong>/td</strong> switch is declared before the <strong>/tr</strong> switch, the timestamp that is returned is from an SHA1 algorithm instead of the intended SHA256 algorithm.
</blockquote>
<br/> <br/> <strong>Windows Vista and earlier:</strong> This flag is not supported.<br/> <br/></td>
</tr>
<tr class="odd">
<td><strong>/tr</strong> <em>URL</em></td>
<td>Specifies the RFC 3161 time stamp server's URL. If this option (or <strong>/t</strong>) is not specified, the signed file will not be time stamped. A warning is generated if time stamping fails. This switch cannot be used with the <strong>/t</strong> switch.<br/> <strong>Windows Vista and earlier:</strong> This flag is not supported.<br/> <br/></td>
</tr>
<tr class="even">
<td><strong>/u</strong> <em>Usage</em></td>
<td>Specifies the <a href="https://msdn.microsoft.com/en-us/library/ms721575(v=VS.85).aspx"><em>enhanced key usage</em></a> (EKU) that must be present in the signing certificate. The usage value can be specified by OID or string. The default usage is &quot;Code Signing&quot; (1.3.6.1.5.5.7.3.3).<br/></td>
</tr>
<tr class="odd">
<td><strong>/uw</strong></td>
<td>Specifies using &quot;Windows System Component Verification&quot; (1.3.6.1.4.1.311.10.3.6).<br/></td>
</tr>
</tbody>
</table>



 

The following option applies to the **timestamp** command. 

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Timestamp option</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>/t</strong> <em>URL</em></td>
<td>Required. Specifies the URL of the time stamp server. The file being time stamped must have previously been signed.<br/></td>
</tr>
<tr class="even">
<td><strong>/td</strong> <em>index</em></td>
<td>Used with the <strong>/tr</strong> switch to request a digest algorithm used by the RFC 3161 time stamp server.<br/>
<blockquote>
[!Note]<br />
The <strong>/td</strong> switch must be declared after the <strong>/tr</strong> switch, not before. If the <strong>/td</strong> switch is declared before the <strong>/tr</strong> switch, the timestamp that is returned is from an SHA1 algorithm instead of the intended SHA256 algorithm.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="odd">
<td><strong>/tp</strong> <em>alg</em></td>
<td>Adds a timestamp to the signature at <em>index</em>.<br/></td>
</tr>
<tr class="even">
<td><strong>/tr</strong> <em>URL</em></td>
<td>Specifies the RFC 3161 time stamp server's URL. The file being time stamped must have previously been signed. Either the <strong>/tr</strong> or the <strong>/t</strong> option is required.<br/></td>
</tr>
<tr class="odd">
<td><strong>/p7</strong> <em>Path</em></td>
<td>Adds a timestamp to PKCS #7 files.<br/></td>
</tr>
</tbody>
</table>



 

The following options apply to the **verify** command. 

| Verify option                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|---------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **/a**                          | Specifies that all methods can be used to verify the file. First, the catalog databases are searched to determine whether the file is signed in a catalog. If the file is not signed in any catalog, SignTool attempts to verify the file's embedded signature. This option is recommended when verifying files that may or may not be signed in a catalog. Examples of files that may or may not be signed include Windows files or drivers.<br/> |
| **/ad**                         | Finds the catalog by using the default catalog database.<br/>                                                                                                                                                                                                                                                                                                                                                                                      |
| **/all**                        | Verifies all signatures in a file with multiple signatures.<br/>                                                                                                                                                                                                                                                                                                                                                                                   |
| **/as**                         | Finds the catalog by using the system component (driver) catalog database.<br/>                                                                                                                                                                                                                                                                                                                                                                    |
| **/ag** *CatDBGUID*             | Finds the catalog in the catalog database identified by the **GUID**.<br/>                                                                                                                                                                                                                                                                                                                                                                         |
| **/c** *CatFile*                | Specifies the catalog file by name.<br/>                                                                                                                                                                                                                                                                                                                                                                                                           |
| **/d**                          | Print the description and description URL.<br/> **Windows Vista and earlier:** This flag is not supported.<br/> <br/>                                                                                                                                                                                                                                                                                                                  |
| **/ds** *Index*                 | Verifies the signature at a certain position.<br/>                                                                                                                                                                                                                                                                                                                                                                                                 |
| **/hash**{**SHA1**\|**SHA256**} | Specifies an optional hash algorithm to use when searching for a file in a catalog.<br/>                                                                                                                                                                                                                                                                                                                                                           |
| **/kp**                         | Performs the verification by using the x64 kernel-mode driver signing policy.<br/>                                                                                                                                                                                                                                                                                                                                                                 |
| **/ms**                         | Uses multiple verification semantics. This is the default behavior of a [**WinVerifyTrust**](/windows/desktop/api/Wintrust/nf-wintrust-winverifytrust) call.<br/>                                                                                                                                                                                                                                                                                                                        |
| **/o** *Version*                | Verifies the file by operating system version. The version parameter is of the form:<br/> *PlatformID***:***VerMajor***.***VerMinor***.***BuildNumber*<br/> The use of the */o* switch is recommended. If */o* is not specified SignTool may return unexpected results. For example, if you do not include the */o* switch, then system catalogs that validate correctly on an older OS may not validate correctly on a newer OS.<br/> |
| **/p7**                         | Verify PKCS \#7 files. No existing policies are used for PKCS \#7 validation. The signature is checked and a chain is built for the signing certificate.<br/>                                                                                                                                                                                                                                                                                      |
| **/pa**                         | Specifies that the Default Authentication Verification Policy is used. If the **/pa** option is not specified, SignTool uses the Windows Driver Verification Policy. This option cannot be used with the **catdb** options.<br/>                                                                                                                                                                                                                   |
| **/pg** *PolicyGUID*            | Specifies a verification policy by **GUID**. The **GUID** corresponds to the ActionID of the verification policy. This option cannot be used with the **catdb** options.<br/>                                                                                                                                                                                                                                                                      |
| **/ph**                         | Print and verify page hash values.<br/> **Windows Vista and earlier:** This flag is not supported.<br/> <br/>                                                                                                                                                                                                                                                                                                                          |
| **/r** *RootSubjectName*        | Specifies the name of the subject of the root certificate that the signing certificate must chain to. This value can be a substring of the entire subject name of the root certificate.<br/>                                                                                                                                                                                                                                                       |
| **/tw**                         | Specifies that a warning is generated if the signature is not time stamped.<br/>                                                                                                                                                                                                                                                                                                                                                                   |



 

The following display options apply to all SignTool commands. 

| Global option | Description                                                                                          |
|---------------|------------------------------------------------------------------------------------------------------|
| **/debug**    | Displays debugging information.<br/>                                                           |
| **/q**        | Displays no output on successful execution and minimal output for failed execution.<br/>       |
| **/v**        | Displays verbose output for successful execution, failed execution, and warning messages.<br/> |



 

The SignTool **verify** command determines whether the signing certificate was issued by a trusted authority, whether the signing certificate has been revoked, and, optionally, whether the signing certificate is valid for a specific policy.

SignTool returns an exit code of zero for successful execution, one for failed execution, and two for execution that completed with warnings. If the SignTool encounters an unhandled exception, however, the return value is undefined.

The following command line shows signing a file automatically using the best certificate.

**signtool sign** **/a** *MyFile.exe*

> [!Note]  
> When signing an executable file that is larger than approximately 300 megabytes for use on a computer running Windows XP with Service Pack 2 (SP2) and later, you should use catalog signing with the [MakeCat](makecat.md) tool rather than use the SignTool tool. Depending on the available system resources of the computer on which the file is verified, some applications may not be able to verify the binary signature of a large file. For more information, see KB article [922225](http://go.microsoft.com/fwlink/p/?linkid=84540).

 

 

 




