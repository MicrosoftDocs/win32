---
description: This topic describes two utilities used to build MUI applications.
ms.assetid: 8ba94001-fc46-41e0-a071-0dc500a20753
title: Resource Utilities
ms.topic: article
ms.date: 05/31/2018
---

# Resource Utilities

This topic describes two utilities used to build MUI applications. While MUIRCT is a MUI-specific tool, MUI also makes use of the standard Windows RC Compiler utility. Instructions for using these utilities are provided in [Localizing Resources and Building the Application](localizing-resources-and-building-the-application.md).

## MUIRCT Utility

MUIRCT (Muirct.exe) is a command line utility for splitting a standard executable file into an LN file and language-specific (that is, localizable) resource files. Each of the resulting files contains resource configuration data for file association. MUIRCT is included in the Microsoft Windows SDK for Windows Vista.

> [!Note]  
> Starting with Windows Vista, the Win32 resource loader is updated to load resources from language-specific files as well as from LN files.

 

### MUIRCT Usages

1.  Split binary into main binary and mui file based on rc\_config file.

    `Muirct -q rc_config [-c checksum_file [-b LangID]] [-x LangID] [-g LangId]     [-f] [-m] [-v level] source_file [output_LN_file] [output_MUI_file]`

2.  Extract checksum from checksum\_file and insert it in output\_file.

    `Muirct -c checksum_file [-b LangID] -e output_file`

3.  Calculate checksum based on checksum\_file and insert it in output\_file.

    `Muirct  -c checksum_file [-b LangID] -q rc_config  -z output_file`

4.  Dump resource configuration data contents from input\_file.

    `Muirct -d input_file`

### MUIRCT Syntax

MUIRCT can take direction from command line switches and/or from a resource configuration file, specified using the -q switch.


```C++
muirct [-h|-?] [ -c checksum_file] [-b langid]  ]
     [-g langid] [-q resource configuration file<RCF>] [-v level] [-x langid]
     [-e output_file]  [-z output_file] [-f] [-d MUI'ized file] [-m file_version]

source_filename [language_neutral_filename] [mui_filename]
```



**Switches and Arguments**




|Option | Purpose |
|-------|-------|
| -h or -? | Shows help screen. | 
| -c | Specifies the input checksum_file from which to extract or calculate the resource checksum. Checksum_file must be a Win32 binary file containing localizable resources. If checksum_file contains resources for more than one language, the -b switch must be used to specify which of these should be used otherwise MUIRCT fails. <br /> | 
| -b | Specifies the language to be used when the checksum_file specified with -c contains resources in multiple languages. This switch can only be used in conjunction with the -c switch. The language identifier can be in decimal or hexadecimal format. MUIRCT fails if the checksum_file contains resources in multiple language and the -b is not specified or if the language specified by the -b switch cannot be found in the checksum_file. <br /> | 
| -g | Specifies the language ID to be included as the ultimate fallback language in the resource configuration data section of the LN file. If the resource loader fails to load a requested .mui file from the thread preferred UI languages, it uses the ultimate fallback language as its last attempt. The LangID value can be specified in decimal or hexadecimal format. For example English (United States) can be specified by -g 0x409 or -g 1033. <br /> | 
| -q | Specifies that the source_file is to be split into the output_LN_file and the output_MUI_file according to the rc_config file layout. The rc_config file is an XML formatted file that specifies which resources will be extracted to the .mui file and which will be left in the LN file. The rc_config can specify the distribution of resource types and individual named items between the output_LN_file and output_MUI_file. The source_file must be a Win32 binary that contains resources in a single language otherwise MUIRCT fails. MUIRCT does not split the file if it is language neutral which is indicated by having only language ID value 0 in the file. The output_LN_file and output_mui_file are the names of the language neutral and .mui file into which the source_file is split. These file names are optional. If they are not specified, MUIRCT appends the extensions .ln and .mui to source_file. Typically you should remove the ".ln" extension before deploying the file. MUIRCT associates the output_LN_file and output_MUI_file by calculating a checksum based on the source_file name and file version and inserting the result into the resource configuration section of each output file. When used in conjunction with the -c switch, the -q switch takes precedence. If the rc_config file supplied with the -q switch contains a checksum MUIRCT ignores the -c switch and inserts the checksum value from the value, rc_config file into the LN and.mui files. If no checksum value is found in the rc_config, MUIRCT calculates the resource checksum based on the behavior of the -c switch. <br /> | 
| -v | Specifies the level of verboseness for logging. Specify 1 to print all basic error messages and operation results. Specify 2 to also include the resource information (type, name, language identifier) included in the .mui file and LN file. The default is -v 1 <br /> | 
| -x | Specifies the language ID with which MUIRCT marks all resource types added to the resource section of the .mui file. The LangID value can be specified in decimal or hexadecimal format. For example English (United States) can be specified by -x 0x409 or -x 1033. <br /> | 
| -e | Extracts the resource checksum contained in the checksum_file provided with the -c switch and inserts it in the specified output_file. When -e is specified, MUIRCT ignores all switches other than the -c switch. In this case the checksum_file must be a Win32 binary file that contains a resource configuration data section with a checksum value. The output_file must be an existing LN file or .mui file. <br /> | 
| -z | Calculates and inserts resource checksum data in the specified output file. MUIRCT bases checksum calculation on the input provided with the -c switch, and the optional -b switch. If you specify an output file for the -z switch that does not exist, MUIRCT exits with a failure.<br /> Example: Calculates the checksum based on localizable resources in Notepad.exe and inserts the checksum into the output file Notepad2.exe.<br /><code>muirct -c notepad.exe -q myprog.rcconfig -z notepad2.exe</code><br /> | 
| -f | Enables creating a .mui file with the version resource being the only localizable resource. By default, MUIRCT does not allow this.<br /> | 
| -d | Locates and displays embedded resource configuration data in the source file. When you specify this switch, MUIRCT ignores all other command line options.<br /> | 
| -m | Specifies the version number to use when calculating the checksum for associating the output_LN_file and output_MUI_file. <br /> | 
| source_filename | Name of the localized binary source file; wildcards cannot be used. This file can only contain resources in one language. If there are resources in multiple languages in the file, MUIRCT fails, unless the -b switch is used. If the file contains resources with language identifiers having value 0 only, MUIRCT does not split the file because a language identifier of 0 indicates a neutral language.<br /> For the -d switch, source_filename is either an LN file or a language-specific resource file for which MUIRCT is to display resource configuration data. <br /> | 
| language_neutral_filename | Optional. Name of LN file. If you do not specify the name of this file, MUIRCT appends a second extension ".ln" to the source file name to use as the language-neutral file name. Typically you should remove the ".ln" extension before deploying the file.<blockquote>[!Note]<br />The LN file should not contain strings or menus. You should remove them manually.</blockquote><br /> | 
| mui_filename | Optional. Name of language-specific resource file. If you do not specify a name, MUIRCT appends a second extension ".mui" to the source file name to use as the file name.Normally, MUIRCT creates a language-specific resource file. However, it does not create a resource file if any of the following conditions exist:<br /><ul><li>No localizable resources are in the original binary file.</li><li>The only resource language found in the original binary file is the neutral language.</li><li>The original binary file has resources for more than one language, not counting the neutral language. If the binary file contains resources for two languages, and one of them is the neutral language, the utility considers the file to be monolingual and creates a language-specific resource file if there are localizable resources.</li></ul> | 




 

### MUIRCT Language Output

MUIRCT chooses the "UltimateFallbackLanguage" attribute value to insert in the LN file resource configuration data based on the following order, from highest priority to lowest:

1.  "UltimateFallbackLanguage" attribute in the source resource configuration file, if one is passed in as input.
2.  The language specified with the -g switch.
3.  Input file language.

MUIRCT picks the "language" attribute value to insert in the .mui file resource configuration data based on the following order:

1.  "language" attribute in the source resource configuration file, if one is passed in as input.
2.  The language specified by the -x switch (force language).
3.  Input file language.

### MUIRCT Checksum Handling

The operating system normally calculates the checksum over the language-specific resources in a file unless you specify the checksum through a resource configuration file. As long as the checksum is the same for the LN file and all associated language-specific resource files, and the language attribute in the resource configuration in the LN and language dependent match, the resource loader can successfully load resources.

MUIRCT supports several methods for placing appropriate checksums in the resource configuration data:

1.  Build an executable for each language, containing both code and resources. After this, use MUIRCT to split each of these files into an LN file and a language-specific resource file. MUIRCT runs multiple times, once to generate a resource file for each language. You can perform the build in the following ways:
    1.  Use the -q switch to specify a checksum value in the resource configuration file. MUIRCT places this value in all the LN files and language-specific resource files produced. You need to adopt a strategy for choosing this value, as described later in this topic.
    2.  Use the -c switch (and, optionally, the -b switch) to choose a single language having resources from which MUIRCT extracts the checksum.
    3.  Use the -z switch to choose a single language having resources from which MUIRCT always extracts the checksum. Apply this checksum after the files have been built using other methods.
2.  Build an executable containing both code and resources for a single language. After this, use MUIRCT to split the resources between the LN file and the language-specific resource file. Finally, use a binary localization tool to modify the resulting resource file for each language.

The most common convention for checksum handling is to base the checksum on the English (United States) resources. You are free to adopt a different convention, as long as it is consistent for each LN file. For example, it is perfectly acceptable for a software development enterprise to base its checksums in the software it builds on French (France) resources instead of English (United States) resources, as long as all the applications have French (France) resources on which to base the checksums. It is also acceptable to use the resource configuration file to assign an arbitrary hexadecimal value of up to 16 hexadecimal digits as a checksum. This last strategy precludes the effective use of the -z, -c, and -b switches of MUIRCT. It requires adoption of a method using either [**GuidGen**](/previous-versions/windows/embedded/ms924300(v=msdn.10)) or some other tool to generate checksum values. This strategy also requires you to set up a policy for determining when to modify the value when adding new localizable resources.

To apply the English (United States) checksum to all files, you can use any of the checksum handling methods described above. For example, you can generate the LN file and language-specific resource file for English (United States), then use the MUIRCT -d switch to obtain the resulting checksum. You can copy this checksum into your resource configuration file and use the -q switch with MUIRCT to apply the checksum to all other files.

### Use of a Resource Configuration File with MUIRCT

You can specify resource configuration data when using MUIRCT. Whether or not you explicitly supply a resource configuration file, every language-specific resource file has resource configuration data, as does any LN file with an associated resource file. For example:

-   If you use the -q switch to specify a resource configuration file, but there are no localizable resources in your input source file, no language-specific resource file is generated and the resulting LN file does not contain resource configuration data. Also, if the input source file has multilingual resources, then MUIRCT won't split the file.

> [!Note]  
> Currently the behavior of MUIRCT is inconsistent when the neutralResources element of the resource configuration file contains no resourceType elements and the localizedResources element contains strings and menus, for example. In such a case, MUIRCT splits the resources as follows:
>
> -   All resources in the original binary (including strings and menus), plus the MUI resources, are placed in the LN file.
> -   Strings, menus, and MUI resources are placed in the appropriate language-specific resource file.

 

### Examples for Using MUIRCT

**Examples of Standard Usage**


```C++
muirct -q mui.MMF bar.exe barnew.exe barnew.exe.mui

muirct -d myprog.exe.mui
```



**Example of LN File Output Using -d Switch**

Here is an example of the resource configuration data output from an LN file, Shell32.dll, using the -d switch with MUIRCT:


```C++
Signature          -    fecdfecd
Length             -    148
RC Config Version  -    10000
FileType           -    11
SystemAttributes   -    100
UltimateFallback location    -  external
Service Checksum   -    14f44a8d86bef14af26d9a885964c935
Checksum           -    f5b3b7ab330439d6fcc07582c3afb613
MainNameTypes      -    AVI FTR ORDERSTREAM TYPELIB UIFILE XML MUI
MainIDTypes        -    1 2 3 12 14 16 24
MuiNameTypes       -    MUI
MuiIDTypes         -    2 3 4 5 6 9 14 16
UltimateFallbackLanguage   -   en-US
```



**Example of Language-Specific Resource File Output Using -d Switch**

Here is an example of the resource configuration data output from a .mui file, Shell32.dll.mui, using the -d switch for MUIRCT:


```C++
Signature          -    fecdfecd
Length             -     c8
RC Config Version  -    10000
FileType           -    12
SystemAttributes   -    100
Service Checksum   -    14f44a8d86bef14af26d9a885964c935
Checksum           -    f5b3b7ab330439d6fcc07582c3afb613
MainNameTypes      -    MUI
MainIDTypes        -    2 3 4 5 6 9 14 16
Language           -    en-US
```



## RC Compiler Utility

RC Compiler (Rc.exe) is a command line utility for compiling a resource definition script file (.rc extension) into resource files (.res extension). RC Compiler is included in the Windows SDK. This document only explains the use of RC Compiler with MUI-related capabilities of the resource loader. For complete information about the compiler, see [About Resource Files](../menurc/about-resource-files.md).

RC Compiler allows you to build, from a single set of sources, an LN file and a separate language-specific resource file. As for MUIRCT, the files are associated by resource configuration data.

### RC Compiler Syntax as Used for MUI Resources

RC Compiler switches are defined in detail in [Using RC](../menurc/using-rc-the-rc-command-line-.md). This section only defines the switches used to build MUI resources. Remember that each switch is case-insensitive. Resource types are assumed to be language-neutral unless otherwise indicated.


```C++
rc [-h|-?] -fm mui_res_name [-q rc_config_file_name] [-g langid] [-g1 ] [-g2 version]
```



**Switches and Arguments**



|Option|Function|
|----|----| 
| -h or -? | Shows help screen. | 
| -fm | Uses the specified resource file for language-specific resources. Normally the resource compiler creates a language-specific resource file. However, it does not create the file if any of the following conditions exist:<br /><ul><li>There are no localizable resources in the .rc file.</li><li>The only resource language found in the .rc file is the neutral language.</li><li>The .rc file has resources for more than one language, not counting the neutral language. If the .rc file contains resources for two languages, and one of them is the neutral language, the compiler considers the file to be monolingual. If there are any localizable resources, the compiler creates a language-specific resource file.</li></ul> | 
| -q | Uses the specified resource configuration file to obtain the resource types to place in the language-specific resource file and the LN file. For more information, see <a href="preparing-a-resource-configuration-file.md">Preparing a Resource Configuration File</a>. As an alternative to this switch, you can use the -j and -k switches, but it is preferred to use a resource configuration file. <br /> By using the -q switch with a resource configuration file, you can implement an item-based split and provide attributes that will end up with the binary resource configuration in the LN and language-specific resource file. This split is not possible using the -j and -k switches.<blockquote>[!Note]<br />The RC Compiler split process does not work properly if you store resources and version information in different resource configuration files. In this case, RC Compiler does not split the version information. Therefore a linker error occurs during linking of the language-specific resource file because the file does not have version resources.</blockquote><br /><br /> | 
| -g | Specifies the ultimate <a href="language-identifiers.md">fallback language</a> identifier in hexadecimal.<br /> | 
| -g1 | Creates a MUI .res file even if the VERSION resource is the only localizable content. By default, RC Compiler does not produce a .res file if VERSION is the only localizable resource.<br /> | 
| -g2 | Specifies the custom version number to use when calculating the checksum.<br /> | 
| mui_res_name | Resource file for language-specific resources.<br /> | 
| rc_config_file_name | Resource configuration file.<br /> | 
| langid | Language identifier.<br /> | 
| version | Custom version number, in a format such as "6.2.0.0".<br /> | 




 

### Example for Using RC Compiler to Build MUI Resources

To illustrate RC Compiler operation with MUI resources, let's examine the following command line, for the resource file Myfile.rc:


```C++
rc -fm myfile_res.res -q myfile.rcconfig myfile.rc
```



This command line causes RC Compiler to do the following:

-   Create the language-specific resource file Myfile\_res.res and a language-neutral resource file that defaults to Myfile.res, based on the name of the .rc file.
-   Add the 2 (item 5 6 7 8 9 10 11 12), 4, 5, 6, 9, 11, 16, 23, 240, 1024 MY\_TYPE resource types to the language-specific .res file if they are in the .rc file.
-   Add resource type 16, along with any other resource types described in the resource file to the language-neutral .res file and to the language-specific .res file. Note that, in this example, resource type 16 is being added in two places.
-   Choose the "UltimateFallbackLanguage" attribute value to insert into the LN file resource configuration data based on the following criteria, ordered from highest priority to lowest:
    -   "UltimateFallbackLanguage" attribute in the resource configuration file if one is passed in as input.
    -   Language attribute value to insert in the resource configuration data based on the RC Compiler language order (language-neutral and language-specific resource file language). Considerations include language in the .rc file, language value of the -gl switch, and identifier 0x0409 for English (United States).

## Remarks

If you include any ICON(3), DIALOG(5), STRING(6), or VERSION(16) resource type in the neutralResources element, then you have to duplicate that entry in the localizedResources element in the resource configuration file.

## Related topics

<dl> <dt>

[Multilingual User Interface Reference](multilingual-user-interface-reference.md)
</dt> <dt>

[MUI Resource Management](mui-resource-management.md)
</dt> <dt>

[Localizing Resources and Building the Application](localizing-resources-and-building-the-application.md)
</dt> </dl>

 

 
