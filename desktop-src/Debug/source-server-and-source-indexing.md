---
description: Source server enables a client to retrieve the exact version of the source files that were used to build an application.
ms.assetid: c7bf51ce-7fb4-49aa-ad33-e551b2c8362b
title: Source Server
ms.topic: article
ms.date: 05/31/2018
---

# Source Server

Source server enables a client to retrieve the exact version of the source files that were used to build an application. Because the source code for a module can change between versions and over a course of years, it is important to look at the source code as it existed when the version of the module in question was built.

Source server retrieves the appropriate files from source control. To use source server, the application must have been source indexed.

## Source Indexing

The source indexing system is a collection of executable files and Perl scripts. The Perl scripts require Perl 5.6 or greater.

Generally, binaries are source indexed during the build process after the application has been built. The information needed by source server is stored in the PDB files.

Source server currently ships with scripts that should work with the following source-control systems.

-   Team Foundation Server
-   Perforce
-   Visual SourceSafe
-   CVS
-   Subversion

You can also create a custom script to index your code for a different source-control system.

The following table lists the source server tools.



| Tool        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Srcsrv.ini  | This file is the master list of all source control servers. Each entry has the following format:*MYSERVER*=*serverinfo*<br/> When using Perforce, the server info consists of the full network path to the server, followed by a colon, followed by the port number it uses. For example:<br/> MYSERVER=machine.corp.company.com:1666<br/> This file can be installed on the computer running the debugger. When source server starts, it looks at Srcsrv.ini for values; these values will override the information contained in the PDB file. This enables users to configure a debugger to use an alternate source control server at debug time.<br/> For more information, see the example Srcsrv.ini installed with the source server tools.<br/> |
| Ssindex.cmd | This script builds the list of files checked into source control along with the version information of each file. It stores a subset of this information in the .pdb files generated when you built the application. The script uses one of the following Perl modules to interface with source control: P4.pm (Perforce) or Vss.pm (Visual Source Safe).For more information, run the script with the -? or -?? (verbose help) option or examine the script.<br/>                                                                                                                                                                                                                                                                                                             |
| Srctool.exe | This utility lists all files indexed within a .pdb file. For each file, it lists the full path, source control server, and version number of the file. You can use this information to retrieve files without using the source server.For more information, run the utility with the /? option.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Pdbstr.exe  | This utility is used by the indexing scripts to insert the version control information into the "srcsrv" alternate stream of the target .pdb file. It can also read any stream from a .pdb file. You can use this information to verify that the indexing scripts are working properly.For more information, run the utility with the /? option.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                          |



 

## Retrieving the Source File

The DbgHelp API provides access to source server functionality through the [**SymGetSourceFile**](/windows/desktop/api/Dbghelp/nf-dbghelp-symgetsourcefile) function. To retrieve the name of the source file to be retrieved, call the [**SymEnumSourceFiles**](/windows/desktop/api/DbgHelp/nf-dbghelp-symenumsourcefiles) or [**SymGetLineFromAddr64**](/windows/desktop/api/Dbghelp/nf-dbghelp-symgetlinefromaddr) function.

## Using Source Server with a Debugger

To use the source server with WinDbg, KD, NTSD, or CDB, ensure that you have installed a recent version of the Debugging Tools for Windows package (version 6.3 or later). Then, include srv\* in the .srcpath command as follows:

**\.srcpath srv\*;**_c:\\mysource_

Note that this example also includes a traditional source path. If the debugger cannot retrieve the file from the source server, it will search the specified path.

If a source file is retrieved by the source server, it will remain on your hard drive after the debugging session is over. Source files are stored locally in the src subdirectory of the Debugging Tools for Windows installation directory.

## Source Server Data Blocks

Source server relies on two blocks of data within the PDB file.

-   Source file list. Building a module automatically creates a list of fully qualified paths to the source files used to build the module.
-   Data block. Indexing the source as described previously adds an alternate stream to the PDB file named "srcsrv". The script that inserts this data is dependent on the specific build process and source control system in use.

In the language specification version 1, the data block is divided into three sections: ini, variables, and source files. It has the following syntax.

``` syntax
SRCSRV: ini ------------------------------------------------ 
VERSION=1
VERCTRL=<source_control_str>
DATETIME=<date_time_str>
SRCSRV: variables ------------------------------------------ 
SRCSRVTRG=%sdtrg% 
SRCSRVCMD=%sdcmd% 
SRCSRVENV=var1=string1\bvar2=string2 
DEPOT=//depot 
SDCMD=sd.exe -p %fnvar%(%var2%) print -o %srcsrvtrg% -q %depot%/%var3%#%var4%
SDTRG=%targ%\%var2%\%fnbksl%(%var3%)\%var4%\%fnfile%(%var1%) 
WIN_SDKTOOLS= sserver.microsoft.com:4444 
SRCSRV: source files --------------------------------------- 
<path1>*<var2>*<var3>*<var4> 
<path2>*<var2>*<var3>*<var4> 
<path3>*<var2>*<var3>*<var4> 
<path4>*<var2>*<var3>*<var4> 
SRCSRV: end ------------------------------------------------
```

All text is interpreted literally, except for text enclosed in percent signs (%). Text enclosed in percent signs is treated as a variable name to be resolved recursively, unless it is one of the following functions:

<dl> <dt>

<span id="_fnvar___"></span><span id="_FNVAR___"></span>%fnvar%()
</dt> <dd>

The parameter text should be enclosed in percent signs and treated as a variable to be expanded.

</dd> <dt>

<span id="_fnbksl___"></span><span id="_FNBKSL___"></span>%fnbksl%()
</dt> <dd>

All forward slashes (/) in the parameter text should be replaced with backward slashes (\\).

</dd> <dt>

<span id="_fnfile___"></span><span id="_FNFILE___"></span>%fnfile%()
</dt> <dd>

All path information in the parameter text should be stripped out, leaving only the file name.

</dd> </dl>

The ini section contains variables that describe the requirements. The indexing script can add any number of variables to this section. The following are examples:

<dl> <dt>

<span id="VERSION"></span><span id="version"></span>VERSION
</dt> <dd>

The language specification version. This variable is required.

</dd> <dt>

<span id="VERCTL"></span><span id="verctl"></span>VERCTL
</dt> <dd>

A string that describes the source control product. This variable is optional.

</dd> <dt>

<span id="DATETIME"></span><span id="datetime"></span>DATETIME
</dt> <dd>

A string that indicates the date and time the PDB file was processed. This variable is optional.

</dd> </dl>

The variables section contains variables that describe how to extract a file from source control. It can also be used to define commonly used text as variables to reduce the size of the data block.

<dl> <dt>

<span id="SRCSRVTRG"></span><span id="srcsrvtrg"></span>SRCSRVTRG
</dt> <dd>

Describes how to build the target path for the extracted file. This is a required variable.

</dd> <dt>

<span id="SRCSRVCMD"></span><span id="srcsrvcmd"></span>SRCSRVCMD
</dt> <dd>

Describes how to build the command to extract the file from source control. This includes the name of the executable file and its command-line parameters. This is a required variable.

</dd> <dt>

<span id="SRCSRVENV"></span><span id="srcsrvenv"></span>SRCSRVENV
</dt> <dd>

A string that lists environment variables to be created during the file extraction. Separate multiple entries with a backspace character (\\b). This is an optional variable.

</dd> </dl>

The source files section contains an entry for each source file that has been indexed. The contents of each line are interpreted as variables with the names VAR1, VAR2, VAR3, and so on until VAR10. The variables are separated by asterisks. VAR1 must specify the fully qualified path to the source file as listed elsewhere in the PDB file. For example, the following line:

``` syntax
c:\proj\src\file.cpp*TOOLS_PRJ*tools/mytool/src/file.cpp*3
```

is interpreted as follows:

``` syntax
VAR1=c:\proj\src\file.cpp
VAR2=TOOLS_PRJ
VAR3=tools/mytool/src/file.cpp
VAR4=3
```

In this example, VAR4 is a version number. However, most source control systems support labeling files in such a way that the source state for a given build can be restored. Therefore, you could alternately use the label for the build. The sample data block could be modified to contain a variable such as the following:

``` syntax
LABEL=BUILD47
```

Then, presuming the source control system uses the at sign (@) to indicate a label, you could modify the SRCSRVCMD variable as follows:

**sd.exe -p %fnvar%(%var2%) print -o %srcsrvtrg% -q %depot%/%var3%@%label%**

## How Source Server Works

The source server client is implemented in Symsrv.dll. The client does not extract information directly from the PDB file; it uses a symbol handler such as the one implemented in Dbghelp.dll. It is essentially a recursive variable substitution engine that creates a command line that can be used to extract the proper source file from the source control system. Your code should not call Symsrv.dll directly. To integrate its functionality into your application, use the [**SymGetSourceFile**](/windows/desktop/api/Dbghelp/nf-dbghelp-symgetsourcefile) function.

The first version of source server works as follows. This behavior may change in future versions.

-   The client calls the **SrcSrvInit** function with the target path to be used as a base for all source file extractions. It stores this path in the TARG variable.
-   The client extracts the Srcsrv stream from the PDB when the module PDB is loaded and calls the **SrcSrvLoadModule** function to pass the data block to source server.
-   When Dbghelp retrieves a source file, the client calls the **SrcSrvGetFile** function to retrieve the source files from source control.
-   Source server searches the source file entries in the data block for an entry that matches the requested file. It fills VAR1 to VAR*n* with the contents of the source file entry. Next, it expands the SRCSRVTRG variable using VAR1 to VAR*n*. If the file is already in this location, it returns the location to the caller. Otherwise, it expands the SRCSRVCMD variable to build the command needed to retrieve the file from source control and copy it to the target location. Finally, it executes this command.

## Creating a Source Control Provider Module

The source server includes provider modules for Perforce (p4.pm) and Visual Source Safe (vss.pm). To create your own provider module, you must implement the following set of interfaces.

<dl> <dt>

<span id="_module__SimpleUsage__"></span><span id="_module__simpleusage__"></span><span id="_MODULE__SIMPLEUSAGE__"></span>**$module::SimpleUsage()**
</dt> <dd>

Purpose: Displays simple module usage information to STDOUT.

Parameters: None

Return value: None

</dd> <dt>

<span id="_module__VerboseUsage__"></span><span id="_module__verboseusage__"></span><span id="_MODULE__VERBOSEUSAGE__"></span>**$module::VerboseUsage()**
</dt> <dd>

Purpose: Displays in-depth module usage information to STDOUT.

Parameters: None

Return value: None

</dd> <dt>

<span id="_objref____module__new__CommandArguments_"></span><span id="_objref____module__new__commandarguments_"></span><span id="_OBJREF____MODULE__NEW__COMMANDARGUMENTS_"></span>**$objref = $module::new(\@CommandArguments)**
</dt> <dd>

Purpose: Initializes an instance of the provider module.

Parameters: All @ARGV arguments that were not recognized by SSIndex.cmd as being general arguments.

Return value: A reference that can be used in later operations.

</dd> <dt>

<span id="_objref-_GatherFileInformation__SourcePath___ServerHashReference_"></span><span id="_objref-_gatherfileinformation__sourcepath___serverhashreference_"></span><span id="_OBJREF-_GATHERFILEINFORMATION__SOURCEPATH___SERVERHASHREFERENCE_"></span>**$objref->GatherFileInformation($SourcePath, $ServerHashReference)**
</dt> <dd>

Purpose: Enables the module to gather the required source indexing information for the directory specified by the $SourcePath parameter. The module should not assume that this entry will be called only once for each object instance, as SSIndex.cmd may call it multiple times for different paths.

Parameters: (1) The local directory containing the source to be indexed. (2) A reference to a hash containing all of the entries from the specified Srcsrv.ini file.

Return value: None

</dd> <dt>

<span id="__VariableHashReference___FileEntry_____objref-_GetFileInfo__LocalFile_"></span><span id="__variablehashreference___fileentry_____objref-_getfileinfo__localfile_"></span><span id="__VARIABLEHASHREFERENCE___FILEENTRY_____OBJREF-_GETFILEINFO__LOCALFILE_"></span>**($VariableHashReference, $FileEntry) = $objref->GetFileInfo($LocalFile)**
</dt> <dd>

Purpose: Provides the necessary information to extract a single, specific file from the source control system.

Parameters: A fully qualified file name

Return value: (1) A hash reference of the variables necessary to interpret the returned $FileEntry. SSIndex.cmd caches these variables for every source file used by a single debug file to reduce the amount of information written to the source index stream. (2) The file entry to be written to the source index stream to allow SrcSrv.dll to extract this file from source control. The exact format of this line is specific to the source control system.

</dd> <dt>

<span id="_TextString____objref-_LongName__"></span><span id="_textstring____objref-_longname__"></span><span id="_TEXTSTRING____OBJREF-_LONGNAME__"></span>**$TextString = $objref->LongName()**
</dt> <dd>

Purpose: Provides a descriptive string to identify the source control provider to the end user.

Parameters: None

Return value: The descriptive name of the source control system.

</dd> <dt>

<span id="_StreamVariableLines____objref-_SourceStreamVariables__"></span><span id="_streamvariablelines____objref-_sourcestreamvariables__"></span><span id="_STREAMVARIABLELINES____OBJREF-_SOURCESTREAMVARIABLES__"></span>**@StreamVariableLines = $objref->SourceStreamVariables()**
</dt> <dd>

Purpose: Enables the source control provider to add source control specific variables to the source stream for each debug file. The sample modules use this method for writing the required EXTRACT\_CMD and EXTRACT\_TARGET variables.

Parameters: None

Return value: The list of entries for the source stream variables.

</dd> </dl>

 

 




