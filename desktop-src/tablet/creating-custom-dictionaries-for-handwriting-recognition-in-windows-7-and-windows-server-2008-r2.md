---
description: This section explains how to create a custom dictionary for handwriting recognition.
ms.assetid: 83abf534-740c-44a3-bbd4-babb54f2930e
title: Creating Custom Dictionaries for Handwriting Recognition in Windows 7 and Windows Server 2008 R2
ms.topic: article
ms.date: 05/31/2018
---

# Creating Custom Dictionaries for Handwriting Recognition in Windows 7 and Windows Server 2008 R2

This section explains how to create a custom dictionary for handwriting recognition.

In the Windows 7 operating system and the Windows Server 2008 R2 operating system, the accuracy of handwriting recognition can be significantly improved through the use of custom dictionaries. These dictionaries supplement or replace system dictionaries used for handwriting. Support for handwriting recognition is provided through the Ink and Handwriting Services feature that needs to be enabled through Server Manager.

> [!Note]  
> Custom dictionaries can be installed for a language only if the handwriting recognizer for that language is installed.

 

There are two basic steps to setting up a custom dictionary for handwriting:

-   Compile a word list. The compilation creates a compiled custom dictionary (.hwrdict) file.
-   Install the compiled custom dictionary.

## Compiling a Word List

The word list to be compiled must be in plain-text format and should be saved using a Unicode encoding. Other encodings will not work. Each line of the text file is taken as a single entry in the dictionary. Multiword units entries containing one or more spaces are allowed. Spaces at the beginning or end of a line are ignored.

A custom dictionary is compiled from a command line. To compile a dictionary, open a command window, navigate to the folder containing the word list, and then run HwrComp.exe with the command-line options you want to use.

The following example shows the usage syntax for the command-line options.

``` syntax
Usage: hwrcomp       [-lang <localename>] [-type <type>]
    [-comment <comment>]
    [-o <dictfile.hwrdict>]
    <inputfile>
     
```

### Explanation of Options



<table>
<colgroup>
<col  />
<col  />
</colgroup>
<thead>
<tr class="header">
<th>Parameter</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>-lang &lt;localename&gt;</td>
<td>The specified locale name assigned to the compiled custom dictionary file. The argument &lt;localename&gt; has the form language-REGION. An example of this is en-US, which signifies the English language in the United States region. For examples of this form, see [Language Identifier Constants and Strings](/windows/desktop/Intl/language-identifier-constants-and-strings). The following languages are supported for Windows 7 and Windows Server 2008 R2 by this feature: en-US, en-GB, en-CA, en-AU, de-DE, de-CH, fr-FR, es-ES, es-MX, es-AR, it-IT, nl-NL, nl-BE, pt-BR, pt-PT, da-DK, sv-SE, nb-NO, nn-NO, fi-FI, pl-PL, cs-CZ, ru-RU, ro-RO, sr-Latn-CS, sr-Cyrl-CS, ca-ES and hr-HR.<br/></td>
</tr>
<tr class="even">
<td>-type &lt;type&gt;</td>
<td>The option argument &lt;type&gt; is a single-string concatenation of the resource's use as either the main word list (PRIMARY) or as a supplement to the main word list (SECONDARY) followed by the actual word list name to which the resource is applied (such as DICTIONARY or SURNAME). The following are possible values:
<ul>
<li>PRIMARY-CITYNAME-LIST</li>
<li>PRIMARY-COUNTRYNAME-LIST</li>
<li>PRIMARY-COUNTRYSHORTNAME-LIST</li>
<li>PRIMARY-DICTIONARY</li>
<li>PRIMARY-GIVENNAME-LIST</li>
<li>PRIMARY-STATEORPROVINCE-LIST</li>
<li>PRIMARY-STREETNAME-LIST</li>
<li>PRIMARY-SURNAME-LIST</li>
<li>SECONDARY-CITYNAME-LIST</li>
<li>SECONDARY-COUNTRYNAME-LIST</li>
<li>SECONDARY-COUNTRYSHORTNAME-LIST</li>
<li>SECONDARY-DICTIONARY</li>
<li>SECONDARY-EMAILSMTP-LIST</li>
<li>SECONDARY-EMAILUSERNAME-LIST</li>
<li>SECONDARY-GIVENNAME-LIST</li>
<li>SECONDARY-STATEORPROVINCE-LIST</li>
<li>SECONDARY-STREETNAME-LIST</li>
<li>SECONDARY-SURNAME-LIST</li>
<li>SECONDARY-URL-LIST</li>
</ul>
If a type value starts with the prefix PRIMARY, the compiled dictionary, after it is installed, will replace the system dictionary for that language. The value PRIMARY-DICTIONARY represents the main system dictionary for a language.
<blockquote>
[!Note]<br />
Replacing a system dictionary does nothing to the original system dictionary content, as the replacement is in effect only until the custom dictionary has been removed.
</blockquote>
<br/> If a type value starts with the prefix SECONDARY, the compiled dictionary will supplement the system dictionary without replacing it.</td>
</tr>
<tr class="odd">
<td>-comment &lt;comment&gt;</td>
<td>The specified comment is compiled into the dictionary file. The comment must be a single string and no longer than 64 characters.</td>
</tr>
<tr class="even">
<td>-o &lt;dictfile.hwrdict&gt;</td>
<td>Output is written to the file name specified by &lt;dictfile.hwrdict&gt;.<br/> If this option is missing, the output file name is derived from the original input file name, with the input file extension replaced by .hwrdict.<br/></td>
</tr>
</tbody>
</table>



 

### Defaults

If no parameters are specified, the default option values are

-lang \<current input language\> -type SECONDARY-DICTIONARY

### Examples

The following compiles the input file mylist1.txt, applies the default option values, and creates the output file mylist1.hwrdict.

``` syntax
hwrcomp mylist1.txt
```

In contrast, the following compiles mylist1.txt into myrsrc1.hwrdict, but assigns "English (US)" (en-US) as the language and SECONDARY-DICTIONARY as the type.

``` syntax
hwrcomp -lang en-US -type SECONDARY-DICTIONARY -o myrsrc1 mylist1.txt 
```

## Installing a Compiled Custom Dictionary

HwrComp.exe creates a .hwrdict file, which is in a binary format usable by a handwriting recognizer. This file can be installed on any computer running Windows 7 or Windows Server 2008 R2 that supports handwriting recognition. A dictionary is installed either for just the current user or for all users on a machine.

A compiled custom dictionary file can be installed from the command line using the tool HwrReg.exe. This tool is useful if you wish to override some of the configuration values that either are compiled into the file or are the default values. There are two ways to run HwrReg.exe: in check/install mode and in list/remove mode.

### Running HwrReg.exe in Check/Install Mode

This mode is for custom dictionary files that have not yet been installed. The following shows the usage syntax for the command-line options.

``` syntax
Usage: hwrreg        [-check]
    [-lang <localename>] 
    [-scope {all|me}]
    [-noprompt] 
    <dictfile.hwrdict>
```

### Explanation of Options



| Parameter                | Description                                                                                                                                                                                                                                                                                                                                                                        |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| -check                   | The dictionary file is verified without being installed. The  check option displays the file's comment, plus the registration information that would be used to install the file. This option is useful for verifying registration information before the installation is performed. <br/> If this option is missing, HwrReg.exe installs the custom dictionary.<br/>  |
|  lang &lt;localename&gt; | The dictionary file is verified without being installed. The  check option displays the file's comment, plus the registration information that would be used to install the file. This option is useful for verifying registration information before the installation is performed. <br/> If this option is missing, HwrReg.exe installs the custom dictionary. <br/> |
|  scope {all\|me}         | The custom dictionary is installed either for all users ( scope all) or for just the current user ( scope me). Installing with  scope all requires the command to be run in an elevated command prompt; otherwise, an error code will be returned. <br/> If this option is missing, the installation is scoped to just the current user.<br/>                          |
|  noprompt                | HwrReg.exe does not prompt for confirmation. This can be useful when running hwrReg.exe from a script. <br/>                                                                                                                                                                                                                                                                 |



 

The following example installs the custom dictionary myrsrc1.hwrdict for language "Danish (Denmark)" (da DK), with the default scope of just the current user.

``` syntax
hwrreg -lang da-DK myrsrc1.hwrdict 
```

### Running HwrReg.exe in List/Remove Mode

This mode either lists or removes installed custom dictionaries. The following shows the usage syntax for the command-line options.

``` syntax
Usage: hwrreg        [-lang <localename>] 
    [-scope {all|me}] 
    [-type <type>]
    -list | -remove
```

### Explanation of Options



| Parameter                | Description                                                                                                                                                                                                                                                                                                                                                                    |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  lang &lt;localename&gt; | The dictionaries registered for only this locale name are listed or removed. The argument &lt;localename&gt; has the form language REGION. For examples of this form, see [Language Identifier Constants and Strings](/windows/desktop/Intl/language-identifier-constants-and-strings). <br/> If this option is missing, dictionaries for all languages are listed or removed.<br/> |
|  scope {all\|me}         | The custom dictionary is installed either for all users ( scope all) or for just the current user ( scope me). Installing with  scope all requires the command to be run in an elevated command prompt; otherwise, an error code will be returned. <br/> If this option is missing, the installation is scoped to just the current user.<br/>                      |
|  type &lt;type&gt;       | Lists or removes only dictionaries that are registered with the specified type.<br/> If this option is missing, all dictionary types are listed or removed. Installing or removing a custom dictionary of another type (such as PRIMARY-COUNTRYNAME-LIST) may affect handwriting recognition in other contexts. <br/>                                              |
|  list                    | Lists all installed dictionaries that match the other options.<br/> If this option is missing, the option  remove must be specified.<br/>                                                                                                                                                                                                                          |
|  remove                  | Prompts for removal of any dictionary that matches the other options.<br/> If this option is missing, the option  list must be specified.<br/>                                                                                                                                                                                                                     |



 

### Examples

The following lists dictionaries that have language "English (US)" (en US) and type PRIMARY DICTIONARY and that are installed for just the current user.

``` syntax
hwrreg -list -lang en-US -type PRIMARY-DICTIONARY
                  
```

Similarly, the following removes dictionaries that match the same criteria.

``` syntax
hwrreg -remove -lang en-US -type PRIMARY-DICTIONARY
                  
```

## General Notes on Custom Dictionaries

-   If you install two custom dictionaries that have the same type, language, and scope, the second installation will overwrite the first.
-   If you install two custom dictionaries with the same type and language, but with different scopes (one for all users, and one for the current user), the dictionary installed for the current user takes precedence, and the dictionary installed for all users is ignored.

 

