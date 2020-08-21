---
title: Using RC (The RC Command Line)
description: To start RC, use the following command.
ms.assetid: da087e15-ecb5-4d03-b534-be872cf7d8b6
ms.topic: article
ms.date: 05/31/2018
---

# Using RC (The RC Command Line)

To start RC, use the following command.

**RC** \[*options*\] *script-file*

The *script-file* parameter specifies the name of the resource-definition file that contains the names, types, filenames, and descriptions of the resources to be compiled.

RC can generate separate resource files for applications that have both language-neutral and language-specific resources. Developers can use a [resource configuration file](/windows/desktop/Intl/preparing-resources) or set command-line options to select which resource types and items are non-localizable resources of the [language-neutral (LN) file](/windows/desktop/Intl/mui-resource-management) and which are localizable resources of language-specific MUI files. For more information, see the [Multilingual User Interface](/windows/desktop/Intl/multilingual-user-interface).

The *options* parameter can be one or more of the following command-line options.

## Options

<dl> <dt>

<span id="__"></span>**/?**
</dt> <dd>

Displays a list of command-line options.

</dd> <dt>

<span id="_c"></span><span id="_C"></span>**/c**
</dt> <dd>

Defines a code page used by NLS conversion.

</dd> <dt>

<span id="_d"></span><span id="_D"></span>**/d**
</dt> <dd>

Defines a symbol for the preprocessor that you can test with the [**\#ifdef**](-ifdef.md) directive.

</dd> <dt>

<span id="_fm_mresname"></span><span id="_FM_MRESNAME"></span>**/fm** *mresname*
</dt> <dd>

RC creates one language-neutral .RES file and one language-dependent (MUI) .RES file using *script-file*. This option must be used together with the **/fo** *resname* option. RC names the language-neutral .RES file *resname.res* and names the language-dependent (MUI) .RES file *mresname.res*.

**Windows Server 2003 and Windows XP/2000:** This option is not available without also using the [**LoadMUILibrary**](/windows/desktop/api/muiload/nf-muiload-loadmuilibrarya) and [**FreeMUILibrary**](/windows/desktop/api/muiload/nf-muiload-freemuilibrary) functions on an updated system.

</dd> <dt>

<span id="_fo_resname"></span><span id="_FO_RESNAME"></span>**/fo** *resname*
</dt> <dd>

RC creates a .RES file named *resname* using *script-file*.

If the **/fm** *mresname* option is also set, RC creates one language-neutral .RES file and one language-dependent (MUI) .RES file.

**Windows Server 2003 and Windows XP/2000:** This option is not available without also using the [**LoadMUILibrary**](/windows/desktop/api/muiload/nf-muiload-loadmuilibrarya) and [**FreeMUILibrary**](/windows/desktop/api/muiload/nf-muiload-freemuilibrary) functions on an updated system.

</dd> <dt>

<span id="_g1"></span><span id="_G1"></span>**/g1**
</dt> <dd>

If /g1, is set, RC generates a MUI file if the only localizable resource being included in the MUI file is a version resource. If /g1 is not set, RC will not generate a MUI file if the only localizable resource being included in the MUI file is a version resource.

</dd> <dt>

<span id="_h"></span><span id="_H"></span>**/h**
</dt> <dd>

Displays the list of command-line options.

</dd> <dt>

<span id="_I"></span><span id="_i"></span>**/I**
</dt> <dd>

Searches the specified directory before searching the directories specified by the INCLUDE environment variable.

</dd> <dt>

<span id="_j__loctype"></span><span id="_J__LOCTYPE"></span>**/j** *loctype*
</dt> <dd>

Localizable resource types RC places into the language-dependent (MUI) .RES file. If the **/q** option is also set, this option is ignored, and the information in the RC Configuration file takes precedence.

**Windows Server 2003 and Windows XP/2000:** This option is not available without also using the [**LoadMUILibrary**](/windows/desktop/api/muiload/nf-muiload-loadmuilibrarya) and [**FreeMUILibrary**](/windows/desktop/api/muiload/nf-muiload-freemuilibrary) functions on an updated system.

</dd> <dt>

<span id="_k_overtype"></span><span id="_K_OVERTYPE"></span>**/k** *overtype*
</dt> <dd>

Overlapping resource types that RC places into both the language-neutral .RES and the language-dependent (MUI).RES files. The resource types that are specified by the **/k** option must be a subset of those that are specified by the **/j** option. For example, ?J2 ?J3 ?K3 specifies that RC places resource type 3 in both the language-neutral and language-dependent (MUI) files. If the **/q** option is also set, this option is ignored, and the information in the RC Configuration file takes precedence.

**Windows Server 2003 and Windows XP/2000:** This option is not available without also using the [**LoadMUILibrary**](/windows/desktop/api/muiload/nf-muiload-loadmuilibrarya) and [**FreeMUILibrary**](/windows/desktop/api/muiload/nf-muiload-freemuilibrary) functions on an updated system.

</dd> <dt>

<span id="_l_langid"></span><span id="_L_LANGID"></span>**/l** *langid*
</dt> <dd>

Specifies the default language for compilation. For example, -l409 is equivalent to including the following statement at the top of the resource script file: `LANGUAGE LANG_ENGLISH,SUBLANG_ENGLISH_US`

For more information, see [Language Identifiers](/windows/desktop/Intl/language-identifiers).

</dd> <dt>

<span id="_n"></span><span id="_N"></span>**/n**
</dt> <dd>

Null terminates all strings in the string table.

</dd> <dt>

<span id="_q_Mui.RCConfig"></span><span id="_q_mui.rcconfig"></span><span id="_Q_MUI.RCCONFIG"></span>**/q** *Mui.RCConfig*
</dt> <dd>

An RC configuration file that follows the RC Configuration File format. The RC Configuration File format enables components to self-describe resource information such as resource versioning, MUI file path, resource types and items. This file specifies which resources go into the language-neutral .RES file and which resources go into the language-dependent (MUI) .RES file. This option, and the information provided in the RC Configuration file, override the command line options **/j** and **/k**.

**Windows Server 2003 and Windows XP/2000:** This option is not available without also using the [**LoadMUILibrary**](/windows/desktop/api/muiload/nf-muiload-loadmuilibrarya) and [**FreeMUILibrary**](/windows/desktop/api/muiload/nf-muiload-freemuilibrary) functions on an updated system.

</dd> <dt>

<span id="_r"></span><span id="_R"></span>**/r**
</dt> <dd>

Ignored. Provided for compatibility with existing makefiles.

</dd> <dt>

<span id="_u"></span><span id="_U"></span>**/u**
</dt> <dd>

Undefines a symbol for the preprocessor.

</dd> <dt>

<span id="_v"></span><span id="_V"></span>**/v**
</dt> <dd>

Displays messages that report on the progress of the compiler.

</dd> <dt>

<span id="_x"></span><span id="_X"></span>**/x**
</dt> <dd>

Prevents RC from checking the INCLUDE environment variable when searching for header files or resource files.

</dd> </dl>

## Remarks

Options are not case sensitive, and a hyphen (-) can be used in place of a slash mark (/). You can combine single-letter options if they do not require any additional parameters.

RC will not generate a MUI file in the following cases.

-   No localizable resources exist in the .rc file.
-   The only resource language id specified in the .rc file is neutral (0x0).
-   The .rc file has resources that are specified in more than one language. The exception is if the .rc file contains two languages, and one language is neutral (0x0), RC generates a MUI file.

For more information, see the following topics:

-   [Defining Names for the Preprocessor](defining-names-for-the-preprocessor.md)
-   [Renaming the Compiled Resource File](renaming-the-compiled-resource-file.md)
-   [Searching for Files](searching-for-files.md)
-   [Displaying Progress Messages](displaying-progress-messages.md)
-   [RC Diagnostic Messages](rc-diagnostic-messages.md)

## Related topics

<dl> <dt>

[Multilingual User Interface](/windows/desktop/Intl/multilingual-user-interface)
</dt> </dl>

 

 