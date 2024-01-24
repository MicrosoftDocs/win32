---
description: The Managed Object Format (MOF) compiler parses a file containing MOF statements and adds the classes and class instances defined in the file to the WMI repository.
ms.assetid: 9858da09-fb91-43a4-9817-83b10e2ee08f
ms.tgt_platform: multiple
title: mofcomp
ms.topic: article
ms.date: 05/31/2018
---

# mofcomp

The [*Managed Object Format (MOF)*](gloss-m.md) compiler parses a file containing MOF statements and adds the classes and class instances defined in the file to the WMI repository. MOF files are usually automatically compiled during the installation of the systems with which they are provided, but you can also compile MOF files by using this tool.

For more information about locating and using mofcomp.exe, see [Using WMI Management Tools](/previous-versions/system-center/configuration-manager-2003/cc180468(v=technet.10)). For information about removing classes and instances from the WMI repository, see the [**pragma deleteclass**](pragma-deleteclass.md) preprocessor command.

The following code example shows how to run the MOF compiler on a file.

``` syntax
mofcomp
  [-autorecover]
  [-check]
  [-N:<namespacepath>]
  [-class:createonly | -class:forceupdate | 
   -class:safeupdate | -class:updateonly ] 
  [-instance:updateonly | -instance:createonly]
  [-B:<filename>]
  [-WMI]
  [-P:<Password>]
  [-U:<UserName>]
  [-A:<Authority>]
  [-MOF:<path>] 
  [-MFL:<path>] 
  [-AMENDMENT:<Locale>]
  [-ER:<ResourceName>]
  [-L:<ResourceLocale>] 
  <MOFfile>
```

## Switches

<dl> <dt>

<span id="-autorecover"></span><span id="-AUTORECOVER"></span>**-autorecover**
</dt> <dd>

Adds the named MOF file to the list of files compiled during repository recovery. The list of autorecover MOF files is stored in the registry key:

**HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Microsoft**\\**WBEM**\\**CIMOM\\**

The MOF files listed in this registry entry must reside on the local computer because MOF files that use the **autorecover** command cannot recover MOF files located on a remote computer.

> [!Note]  
> To ensure that all your WMI class definitions for managed objects are restored to the [*WMI repository*](gloss-w.md) if WMI has a failure and restarts, use the [**\#pragma autorecover**](pragma-autorecover.md) preprocessor instruction in your [*Managed Object Format*](gloss-m.md) (MOF) file.

 

</dd> <dt>

<span id="-check"></span><span id="-CHECK"></span>**-check**
</dt> <dd>

Requests that the compiler perform a syntax check only and print appropriate error messages. No other switch can be used with this switch. When this switch is used, no connection to Windows Management Instrumentation (WMI) is established and no modifications to the WMI repository are made.

</dd> <dt>

<span id="-N__namespacepath_"></span><span id="-n__namespacepath_"></span><span id="-N__NAMESPACEPATH_"></span>**-N:<***namespacepath***>**
</dt> <dd>Requests that the compiler load the MOF file into the namespace specified as *namespacepath*. The compiled MOF is loaded into the default Mofcomp namespace, root\\default, unless this switch is used. You can also insert the preprocessor command **\#pragma namespace ("***namespace path***")** in the MOF file to achieve the same effect. If both the **-N:** switch and the \#<a href="pragma-namespace.md">pragma namespace</a> command are used, \#**pragma namespace** **autorecover** takes priority. In this case, the only way to compile the MOF into another namespace is to edit the MOF file and change the \#**pragma namespace** command. A remote computer can be specified using \\\\machinename\\root\\default.</dd> <dt>

<span id="-class_createonly"></span><span id="-CLASS_CREATEONLY"></span>**-class:createonly**
</dt> <dd>

Requests that the compiler not make any changes to existing classes. When this switch is used, the compile operation terminates if a class specified in the MOF file already exists.

</dd> <dt>

<span id="-class_forceupdate"></span><span id="-CLASS_FORCEUPDATE"></span>**-class:forceupdate**
</dt> <dd>

Forces updates of classes when conflicting child classes exist. For example, suppose a class qualifier is defined in a child class and the base class tries to add the same qualifier. In **-class:forceupdate** mode, the MOF compiler resolves this conflict by deleting the conflicting qualifier in the child class. If the child class has instances, the forced update fails.

</dd> <dt>

<span id="-class_safeupdate"></span><span id="-CLASS_SAFEUPDATE"></span>**-class:safeupdate**
</dt> <dd>

Allows updates of classes even if there are child classes, as long as the change does not cause conflicts with child classes. For example, this flag allows adding a new property to the base class that was not previously mentioned in child classes. If the child classes have instances, the update fails.

</dd> <dt>

<span id="-class_updateonly"></span><span id="-CLASS_UPDATEONLY"></span>**-class:updateonly**
</dt> <dd>

Requests that the compiler not create any new classes. When this switch is used, the compile operation terminates if a class specified in the MOF file does not exist.

</dd> <dt>

<span id="-instance_updateonly"></span><span id="-INSTANCE_UPDATEONLY"></span>**-instance:updateonly**
</dt> <dd>

Requests that the compiler not create any new instances. When this switch is used, the compile operation terminates if an instance specified in the MOF file does not exist.

</dd> <dt>

<span id="-instance_createonly"></span><span id="-INSTANCE_CREATEONLY"></span>**-instance:createonly**
</dt> <dd>

Requests that the compiler not make any changes to existing instances. When this switch is used, the compile operation terminates if an instance specified in the MOF file already exists.

</dd> <dt>

<span id="-B__filename_"></span><span id="-b__filename_"></span><span id="-B__FILENAME_"></span>**-B:<***filename***>**
</dt> <dd>

Requests that the compiler create a binary version of the MOF file with the name *filename* without making any modifications to the WMI repository.

If you use the **-B:<***filename***>** option to create a binary MOF file, only default qualifier flavors are stored in the WMI repository.

Binary MOF format is the intermediate format for combining a WDM-driver with the MOF as a resource. The binary MOF represents classes and instances just as a text MOF file does and is compressed before it is stored on disk.

</dd> <dt>

<span id="-WMI"></span><span id="-wmi"></span>**-WMI**
</dt> <dd>

Requests that the compiler perform a WMI syntax check. The **-B:** switch must be used with this switch. The **-WMI** switch is only used for building binary MOF files for use by WDM device drivers. This switch invokes a separate binary MOF file checker, which runs after the binary MOF file is created.

</dd> <dt>

<span id="-P__Password_"></span><span id="-p__password_"></span><span id="-P__PASSWORD_"></span>**-P:<***Password***>**
</dt> <dd>

Specifies *Password* as the password for the computer user to enter when logging on.

</dd> <dt>

<span id="-U__UserName_"></span><span id="-u__username_"></span><span id="-U__USERNAME_"></span>**-U:<***UserName***>**
</dt> <dd>

Specifies *UserName* as the name of the user logging on.

</dd> <dt>

<span id="-A__Authority_"></span><span id="-a__authority_"></span><span id="-A__AUTHORITY_"></span>**-A:<***Authority***>**
</dt> <dd>

Specifies *Authority* as the authority (domain name) to use when logging on to WMI.

</dd> <dt>

<span id="-MOF__path_"></span><span id="-mof__path_"></span><span id="-MOF__PATH_"></span>**-MOF:<***path***>**
</dt> <dd>

Name of the language neutral output. Used with the **-AMENDMENT** switch to specify the name of the language-neutral MOF file that will be generated.

</dd> <dt>

<span id="-MFL__path_"></span><span id="-mfl__path_"></span><span id="-MFL__PATH_"></span>**-MFL:<***path***>**
</dt> <dd>

Name of the language specific output. Used with the **-AMENDMENT** switch to specify the name of the language-specific MOF file that will be generated.

</dd> <dt>

<span id="-AMENDMENT__Locale_"></span><span id="-amendment__locale_"></span><span id="-AMENDMENT__LOCALE_"></span>**-AMENDMENT:<***Locale***>**
</dt> <dd>

Splits the MOF file into language-neutral and -specific versions. The MOF compiler creates a language-neutral form of the MOF file that has all amended qualifiers removed. A localized version of the MOF file is also created with an MFL file name extension. The *Locale* parameter specifies the name of the child namespace that contains the localized class definitions. The format of the *Locale* parameter is MS\_xxx where xxx is the hexadecimal value of the Windows LCID. For example, the locale for American English is MS\_409.

</dd> <dt>

<span id="-ER__ResourceName_"></span><span id="-er__resourcename_"></span><span id="-ER__RESOURCENAME_"></span>**-ER <***ResourceName***>**
</dt> <dd>

Extracts binary MOF from a named resource. This switch gets the binary MOF from the class in the WMI repository while the -B switch creates the binary MOF format from a MOF file.

</dd> <dt>

<span id="-L__ResourceLocale_"></span><span id="-l__resourcelocale_"></span><span id="-L__RESOURCELOCALE_"></span>**-L:<***ResourceLocale***>**
</dt> <dd>

Optional. Extracts the localized MOF descriptions from the binary MOF when used with -ER switch.

</dd> <dt>

<span id="_MOFfile_"></span><span id="_moffile_"></span><span id="_MOFFILE_"></span>**<***MOFfile***>**
</dt> <dd>

Name of the file to parse.

</dd> </dl>

## Return Values

As its first operation, the MOF compiler performs a syntax check on the MOF file. If the compiler finds any errors, it prints an error message and the process terminates.

The MOF compiler can return the following values:

<dl> <dt>

<span id="0"></span>0
</dt> <dd>

MOF compile operation was successful.

</dd> <dt>

<span id="1"></span>1
</dt> <dd>

The MOF compiler could not connect with the WMI server. This is either because of a semantic error such as an incompatibility with the existing WMI repository or an actual error such as the failure of the WMI server to start.

</dd> <dt>

<span id="2"></span>2
</dt> <dd>

One or more command-line switches were not valid.

</dd> <dt>

<span id="3"></span>3
</dt> <dd>

A MOF syntax error occurred.

</dd> </dl>

If the MOF file is parsed correctly, but an attempt is made to perform an operation that is forbidden by a command-line switch, the compiler returns an error code generated by WMI instead of any of the return codes listed in the list preceding. For example, a WMI error code is returned when the **-instance:updateonly** switch is specified and the MOF file attempts to create an instance.

If the [**\#pragma autorecover**](pragma-autorecover.md) preprocessor statement is not in the file, then the following warning is returned:

``` syntax
WARNING: FileYourMof.Mof does not contain #PRAGMA AUTORECOVER.
If the WMI repository is rebuilt in the future, the contents of this 
MOF file   will not be included in the new WMI repository.
To include this MOF file when the WMI Repository is automatically 
reconstructed, place the #PRAGMA AUTORECOVER statement on the first 
line of the MOF file.
```

## Remarks

The MOF Compiler is available in the %Windir%\\System32\\wbem directory. You must specify the MOF file as the parameter of the MOF Compiler. You can also specify an Autorecover switch if you want the MOF file to be automatically recompiled if the CIM Repository ever has to be automatically recovered. For more information, type **Mofcomp /?** at the command prompt.

A MOF file that uses the Unicode character set contains a signature as the first two bytes of the file. This signature is either U+FFFE or U+FEFF, depending on the byte ordering of the file.

When no errors occur in the parsing process, the MOF compiler connects to the WMI server running on the local computer unless the **-check** switch is specified. Classes and instances defined in the MOF file are added to the WMI repository.

When an error occurs in updating the WMI repository, the compiler makes no attempt to return the repository to its state before the compiler began processing.

**Windows 8:** When installing a provider, mofcomp treats the \[Key\] and \[Static\] qualifiers as true if they are present, regardless of their actual values. Other qualifiers are treated as false if they are present but not explicitly set to true.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |



## See also

<dl> <dt>

[**pragma namespace**](pragma-namespace.md)
</dt> <dt>

[Compiling MOF Files](compiling-mof-files.md)
</dt> <dt>

[Compiling Localized MOF Files](compiling-localized-mof-files.md)
</dt> <dt>

[Registering a Provider](registering-a-provider.md)
</dt> <dt>

[**IMOFCompiler::CompileFile**](/windows/desktop/api/Wbemcli/nf-wbemcli-imofcompiler-compilefile)
</dt> </dl>

 

