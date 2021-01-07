---
description: Command-line options for msiexec.exe for Windows Installer 3.0 and earlier. Provides a table showing options, parameters, and descriptions. Examples showing how to install products and other tasks.
ms.assetid: a70d8cc8-af47-4472-aabc-97481d97080d
title: Command-Line Options
ms.topic: article
ms.date: 05/31/2018
---

# Command-Line Options

The executable program that interprets packages and installs products is Msiexec.exe. Note that Msiexec also sets an error level on return that corresponds to [system error codes](/windows/desktop/Debug/system-error-codes). Command-line options are case-insensitive.

The command-line options in the following table are available with Windows Installer  3.0 and earlier versions. The [Standard Installer Command-Line Options](standard-installer-command-line-options.md) are also available beginning with Windows Installer 3.0.



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Option</th>
<th>Parameters</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>/I</strong></td>
<td><em>Package|ProductCode</em></td>
<td>Installs or configures a product.<br/></td>
</tr>
<tr class="even">
<td><strong>/f</strong></td>
<td>[p|o|e|d|c|a|u|m|s|v] <em>Package</em>|<em>ProductCode</em></td>
<td>Repairs a product. This option ignores any property values entered on the command line. The default argument list for this option is 'omus.' This option shares the same argument list as the <a href="reinstallmode.md"><strong>REINSTALLMODE</strong></a> property.<br/> p - Reinstalls only if file is missing.<br/> o - Reinstalls if file is missing or an older version is installed.<br/> e - Reinstalls if file is missing or an equal or older version is installed.<br/> d - Reinstalls if file is missing or a different version is installed.<br/> c - Reinstalls if file is missing or the stored checksum does not match the calculated value. Only repairs files that have <strong>msidbFileAttributesChecksum</strong> in the Attributes column of the <a href="file-table.md">File</a> table.<br/> a - Forces all files to be reinstalled.<br/> u - Rewrites all required user-specific registry entries.<br/> m - Rewrites all required computer-specific registry entries.<br/> s - Overwrites all existing shortcuts.<br/> v - Runs from source and re-caches the local package. Do not use the <strong>v</strong> reinstall option for the first installation of an application or feature.<br/></td>
</tr>
<tr class="odd">
<td><strong>/a</strong></td>
<td><em>Package</em></td>
<td><a href="administrative-installation.md">Administrative installation</a> option. Installs a product on the network.<br/></td>
</tr>
<tr class="even">
<td><strong>/x</strong></td>
<td><em>Package|ProductCode</em></td>
<td>Uninstalls a product.</td>
</tr>
<tr class="odd">
<td><strong>/j</strong></td>
<td>[u|m]<em>Packageor</em><br/> [u|m]<em>Package</em><strong>/t</strong><em>Transform List</em><br/> <em>or</em><br/> [u|m]<em>Package</em><strong>/g</strong><em>LanguageID</em><br/></td>
<td>Advertises a product. This option ignores any property values entered on the command line.<br/> u - Advertises to the current user.<br/> m - Advertises to all users of machine.<br/> g - Language identifier.<br/> t - Applies transform to advertised package.<br/></td>
</tr>
<tr class="even">
<td><strong>/L</strong></td>
<td>[i|w|e|a|r|u|c|m|o|p|v|x|+|!|*] <em>Logfile</em></td>
<td>Writes logging information into a logfile at the specified existing path. The path to the logfile location must already exist. The installer does not create the directory structure for the logfile. Flags indicate which information to log. If no flags are specified, the default is 'iwearmo.'<br/> i - Status messages.<br/> w - Nonfatal warnings.<br/> e - All error messages.<br/> a - Start up of actions.<br/> r - Action-specific records.<br/> u - User requests.<br/> c - Initial UI parameters.<br/> m - Out-of-memory or fatal exit information.<br/> o - Out-of-disk-space messages.<br/> p - Terminal properties.<br/> v - Verbose output.<br/> x - Extra debugging information. <strong>Windows Installer 2.0:</strong> Not supported. The x option is available with Windows Installer version 3.0.3790.2180 and later.<br/> <br/> + - Append to existing file.<br/> ! - Flush each line to the log.<br/> &quot;*&quot; - Wildcard, log all information except for the v and x options. To include the v and x options, specify &quot;/l*vx&quot;.<br/>
<blockquote>
[!Note]<br />
For more information about all the methods that are available for setting the logging mode, see <a href="normal-logging.md">Normal Logging</a> in the <a href="windows-installer-logging.md">Windows Installer Logging</a> section
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td><strong>/m</strong></td>
<td><em>filename</em>
<blockquote>
[!Note]<br />
The length of <em>filename</em> must be no more than eight characters.
</blockquote>
<br/></td>
<td>Generates an SMS status .mif file. Must be used with either the install (-i), remove (-x), administrative installation (-a), or reinstall (-f) options. The ISMIF32.DLL is installed as part of SMS and must be on the path.<br/> The fields of the status mif file are filled with the following information:<br/> Manufacturer - <a href="author-summary.md"><strong>Author</strong></a><br/> Product - <a href="revision-number-summary.md"><strong>Revision Number</strong></a><br/> Version - <a href="subject-summary.md"><strong>Subject</strong></a><br/> Locale - <a href="template-summary.md"><strong>Template</strong></a><br/> Serial Number - not set<br/> Installation - set by ISMIF32.DLL to &quot;DateTime&quot;<br/> InstallStatus - &quot;Success&quot; or &quot;Failed&quot;<br/> Description - Error messages in the following order: 1) Error messages generated by installer. 2) Resource from Msi.dll if installation could not commence or user exit. 3) System error message file. 4) Formatted message: &quot;Installer error %i&quot;, where %i is error returned from Msi.dll.<br/></td>
</tr>
<tr class="even">
<td><strong>/p</strong></td>
<td><em>PatchPackage[;patchPackage2</em> ]</td>
<td>Applies a patch. To apply a patch to an installed administrative image you must combine the following options:<br/> /p <em><PatchPackage>[;patchPackage2 ]</em> /a <em><Package></em><br/></td>
</tr>
<tr class="odd">
<td><strong>/q</strong></td>
<td>n|b|r|f</td>
<td>Sets <a href="user-interface-levels.md">user interface level</a>.<br/> q , qn - No UI<br/> qb - <a href="b-gly.md"><em>Basic UI</em></a>. Use qb! to hide the <strong>Cancel</strong> button.<br/> qr - <a href="r-gly.md"><em>Reduced UI</em></a> with no modal dialog box displayed at the end of the installation.<br/> qf - <a href="f-gly.md"><em>Full UI</em></a> and any authored <a href="fatalerror-dialog.md">FatalError</a>, <a href="userexit-dialog.md">UserExit</a>, or <a href="exit-dialog.md">Exit</a> modal dialog boxes at the end.<br/> qn+ - No UI except for a modal dialog box displayed at the end.<br/> qb+ - <a href="b-gly.md"><em>Basic UI</em></a> with a modal dialog box displayed at the end. The modal box is not displayed if the user cancels the installation. Use qb+! or qb!+ to hide the <strong>Cancel</strong> button.<br/> qb- - <a href="b-gly.md"><em>Basic UI</em></a> with no modal dialog boxes. Please note that /qb+- is not a supported UI level. Use qb-! or qb!- to hide the <strong>Cancel</strong> button.<br/> Note that the ! option is available with Windows Installer 2.0 and works only with basic UI. It is not valid with full UI.<br/></td>
</tr>
<tr class="even">
<td><strong>/?</strong> or <strong>/h</strong></td>
<td> </td>
<td>Displays copyright information for Windows Installer.<br/></td>
</tr>
<tr class="odd">
<td><strong>/y</strong></td>
<td><em>module</em></td>
<td>Calls the system function <strong>DllRegisterServer</strong> to self-register modules passed in on the command line. Specify the full path to the DLL. For example, for MY_FILE.DLL in the current folder you can use:<br/> <strong>msiexec /y .\MY_FILE.DLL</strong><br/> This option is only used for registry information that cannot be added using the registry tables of the .msi file.<br/></td>
</tr>
<tr class="even">
<td><strong>/z</strong></td>
<td><em>module</em></td>
<td>Calls the system function <strong>DllUnRegisterServer</strong> to unregister modules passed in on the command line. Specify the full path to the DLL. For example, for MY_FILE.DLL in the current folder you can use: <br/> <strong>msiexec /z .\MY_FILE.DLL</strong><br/> This option is only used for registry information that cannot be removed using the registry tables of the .msi file.<br/></td>
</tr>
<tr class="odd">
<td><strong>/c</strong></td>

<td>Advertises a new instance of the product. Must be used in conjunction with /t. Available starting with the Windows Installer version that is shipped with Windows Server 2003 and Windows XP with Service Pack 1 (SP1).<br/></td>
</tr>
<tr class="even">
<td><strong>/n</strong></td>
<td><em>ProductCode</em></td>
<td>Specifies a particular instance of the product. Used to identify an instance installed using the multiple instance support through a product code changing transforms. Available starting with the Windows Installer version shipped with Windows Server 2003 and Windows XP with SP1. <br/></td>
</tr>
</tbody>
</table>



 

The options /i, /x, /f\[p\|o\|e\|d\|c\|a\|u\|m\|s\|v\], /j\[u\|m\], /a, /p, /y and /z should not be used together. The one exception to this rule is that patching an [administrative installation](administrative-installation.md) requires using both /p and /a. The options /t, /c and /g should only be used with /j. The options /l and /q can be used with /i, /x, /f\[p\|o\|e\|d\|c\|a\|u\|m\|s\|v\], /j\[u\|m\], /a, and /p. The option /n can be used with /i, /f, /x and /p.

To install a product from A:\\Example.msi, install the product as follows:

**msiexec /i A:\\Example.msi**

Only [public properties](public-properties.md) can be modified using the command line. All property names on the command line are interpreted as uppercase but the value retains case sensitivity. If you enter **MyProperty** at a command line, the installer overrides the value of MYPROPERTY and not the value of **MyProperty** in the Property table. For more information, see [About Properties](about-properties.md).

To install a product with PROPERTY set to VALUE, use the following syntax on the command line. You can put the property anywhere except between an option and its argument.

Correct syntax:

**msiexec /i A:\\Example.msi PROPERTY=VALUE**

Incorrect syntax:

**msiexec /i PROPERTY=VALUE A:\\Example.msi**

Property values that are literal strings must be enclosed in quotation marks. Include any white spaces in the string between the marks.

**msiexec /i A:\\Example.msi PROPERTY="Embedded White Space"**

To clear a public property by using the command line, set its value to an empty string.

**msiexec /i A:\\Example.msi PROPERTY=""**

For sections of text set apart by literal quotation marks, enclose the section with a second pair of quotation marks.

**msiexec /i A:\\Example.msi PROPERTY="Embedded ""Quotes"" White Space"**

The following example shows a complicated command line.

**msiexec /i testdb.msi INSTALLLEVEL=3 /l\* msi.log COMPANYNAME="Acme ""Widgets"" and ""Gizmos."""**

The following example shows advertisement options. Note that switches are not case-sensitive.

**msiexec /JM msisample.msi /T transform.mst /LIME logfile.txt**

The following example shows you how to install a new instance of a product to be advertised. This product is authored to support multiple instance transforms.

**msiexec /JM msisample.msi /T :instance1.mst;customization.mst /c /LIME logfile.txt**

The following example shows how to patch an instance of a product that is installed using multiple instance transforms.

**msiexec /p msipatch.msp;msipatch2.msp /n {00000001-0002-0000-0000-624474736554} /qb**

When you apply patches to a specific product, the /i and /p options cannot be specified together in a command line. In this case, you can apply patches to a product as follows.

**msiexec /i A:\\Example.msi PATCH=msipatch.msp;msipatch2.msp /qb**

The [**PATCH**](patch.md) property cannot be set in a command line, when /p option is used. If the **PATCH** property is set when the /p option is used, the value of **PATCH** property is ignored and overwritten.

 

