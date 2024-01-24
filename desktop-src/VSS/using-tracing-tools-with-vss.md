---
description: To collect tracing information for the VSS infrastructure, you can use the VssTrace tool, the Logman tool, or the Tracelog tool.
ms.assetid: afe2a0ed-1a8e-4f8b-be9e-241d55cd9ef6
title: Using Tracing Tools with VSS
ms.topic: article
ms.date: 05/31/2018
---

# Using Tracing Tools with VSS

To collect tracing information for the VSS infrastructure, you can use the VssTrace tool, the Logman tool, or the Tracelog tool. VssTrace is available in the Microsoft Windows Software Development Kit (SDK) and can be used to trace VSS applications on Windows 7 and later versions of the Windows operating system. Logman is a trace controller for trace events and performance counters; it can also be used to trace VSS applications on Windows 7 and later versions of the Windows operating system. Tracelog is included in the Windows Driver Kit (WDK).

To use tracing tools with [Automated System Recovery (ASR)](using-vss-automated-system-recovery-for-disaster-recovery.md), see [Using Tracing Tools with ASR Applications](using-tracing-tools-with-vss-asr-applications.md).

> [!Note]  
> VssTrace, Logman, and Tracelog all require administrator privilege.

 

For information about each tool, see the following sections:

-   [Using VssTrace](#using-vsstrace)
    -   [VssTrace Command-Line Options](#vsstrace-command-line-options)
-   [Using Logman](#using-logman)
-   [Using Tracelog](#using-tracelog)

## Using VssTrace

To run the VssTrace tool from the command line, use the following syntax:

**vsstrace** *command-line-options*

To display concise command-line help for the VssTrace tool, use the following syntax:

**vsstrace -help**

To display detailed command-line help for the VssTrace tool, use the following syntax:

**vsstrace -help all**

### VssTrace Command-Line Options

The VssTrace tool uses the following command-line options:

<dl> <dt>

<span id="-f_Flags"></span><span id="-f_flags"></span><span id="-F_FLAGS"></span>**-f** *Flags*
</dt> <dd>

Enable the modules whose flags are specified by the *Flags* bitmask. Each flag corresponds to a VSS module. If *Flags* is zero, no modules are enabled. Note that most modules are enabled by default. This option can be combined with the **+***Module* option. For example, **vsstrace -f 0 +WRITER +COORD** disables tracing of all of the modules that are enabled by default and enables tracing of VSS writers and the VSS service. Alternatively, **vsstrace +f 0xffff -COORD** enables tracing of all modules except the VSS service.

> [!Note]  
> If you use the **-f** option together with the **+***Module* option, the **-f** must appear before the **+***Module* option.

 

The following table lists the module name and flag for each available module.

| Module | Flag       | Enabled by default | Items traced                                                                                                                                  |
|--------|------------|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| EXCEPT | 0x00000001 | Yes                | C++ exception handling.                                                                                                                       |
| COORD  | 0x00000002 | Yes                | The VSS service, which is also called the VSS coordinator.                                                                                    |
| SWPRV  | 0x00000004 | Yes                | The VSS System Shadow Copy Provider service.                                                                                                  |
| BUCOMP | 0x00000008 | Yes                | The VSS requester and backup metadata processing.                                                                                             |
| WRITER | 0x00000010 | Yes                | VSS writer operations and VSS hosted writer implementations, such as the Windows Registry writer.                                             |
| VSSAPI | 0x00000020 | Yes                | Miscellaneous functions of the VSS API exported by VSSAPI.DLL.                                                                                |
| HWDIAG | 0x00000040 | Yes                | VSS hardware provider infrastructure and operations.                                                                                          |
| ADMIN  | 0x00000080 | Yes                | VSS command line utilities such as VSSADMIN.EXE and DISKSHADOW.EXE.                                                                           |
| VSSUI  | 0x00000100 | Yes                | The Shadow Copies for Shared Folders configuration user interface (UI). The UI is available only on Windows Server operating systems.         |
| TEST   | 0x00000200 | Yes                | Not applicable. (This tracing module is reserved.)                                                                                            |
| IOCTL  | 0x00000400 | Yes                | Details of FSCTL and IOCTL operations that the VSS service has initiated by calling the [**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol) function. |
| GEN    | 0x00000800 | Yes                | General VSS utility functions, such as allocators, string classes, and registry and volume operations.                                        |
| WRXML  | 0x00001000 | No                 | XML processing for writer metadata. This module has a very high level of noise.                                                               |
| VSSXML | 0x00002000 | No                 | XML processing base classes. This module has a very high level of noise.                                                                      |



 

</dd> <dt>

<span id="_Module"></span><span id="_module"></span><span id="_MODULE"></span>**+***Module*
</dt> <dd>

Enable the module specified by *Module*. More than one module can be enabled at a time. To list the available modules, type **vsstrace –help modules** at the command-line prompt.

</dd> <dt>

<span id="-Module"></span><span id="-module"></span><span id="-MODULE"></span>**-***Module*
</dt> <dd>

Disable the module specified by *Module*. To list the available modules, type **vsstrace –help modules** at the command-line prompt.

</dd> <dt>

<span id="_pid_ProcessId"></span><span id="_pid_processid"></span><span id="_PID_PROCESSID"></span>**+pid** *ProcessId*
</dt> <dd>

Enable the process specified by *ProcessId*. To enable all processes, use "\*" for the value of *ProcessId*. More than one **pid** option can be specified at a time. The order of the options determines which processes are enabled or disabled. For example, to enable only the process whose process identifier is 0xe8c, use **vsstrace -pid \* +pid 0xe8c**.

</dd> <dt>

<span id="-pid_ProcessId"></span><span id="-pid_processid"></span><span id="-PID_PROCESSID"></span>**-pid** *ProcessId*
</dt> <dd>

Disable the process specified by *ProcessId*. To disable all processes, use "\*" for the value of *ProcessId*. More than one **pid** option can be specified at a time. The order of the options determines which processes are enabled or disabled. For example, to disable all processes except the process whose process identifier is 0xe8c, use **vsstrace -pid \* +pid 0xe8c**.

</dd> <dt>

<span id="_tid_ThreadId"></span><span id="_tid_threadid"></span><span id="_TID_THREADID"></span>**+tid** *ThreadId*
</dt> <dd>

Enable the thread specified by *ThreadId*. To enable all threads, use "\*" for the value of *ThreadId*. More than one **tid** option can be specified at a time. The order of the options determines which threads are enabled or disabled. For example, to enable only the thread whose process identifier is 0x31a, use **vsstrace -tid \* +tid 0x31a**.

</dd> <dt>

<span id="-tid_ThreadId"></span><span id="-tid_threadid"></span><span id="-TID_THREADID"></span>**-tid** *ThreadId*
</dt> <dd>

Disable the thread specified by *ThreadId*. To disable all threads, use "\*" for the value of *ThreadId*. More than one **tid** option can be specified at a time. The order of the options determines which threads are enabled or disabled. For example, to disable all threads except the thread whose process identifier is 0x31a, use **vsstrace -tid \* +tid 0x31a**.

</dd> <dt>

<span id="-l_Level"></span><span id="-l_level"></span><span id="-L_LEVEL"></span>**-l** *Level*
</dt> <dd>

Use the tracing level specified by *Level*. The higher the level, the more verbose the trace output. Each level includes all of the lower levels. The default level is 170. The following levels are available.



| Level | Information included in the trace output |
|-------|------------------------------------------|
| 000   | None                                     |
| 020   | Fatal errors                             |
| 030   | Unhandled exceptions                     |
| 040   | Errors                                   |
| 050   | Assertions                               |
| 060   | Warnings                                 |
| 080   | Exception handling                       |
| 100   | Event Log activity                       |
| 120   | General information                      |
| 140   | Code flow                                |
| 160   | Function enter and exit                  |
| 170   | Function return values                   |
| 180   | Function parameters (terse)              |
| 190   | Function parameters (verbose)            |
| 200   | Verbose information level 1              |
| 210   | Verbose information level 2              |
| 220   | Verbose information level 3              |
| 230   | Fast Code Level 1                        |
| 240   | Fast Code Level 2                        |
| 250   | Fast Code Level 3                        |
| 255   | All                                      |



 

</dd> <dt>

<span id="_indent"></span><span id="_INDENT"></span>**+indent**
</dt> <dd>

Indent the formatted trace output at each function and subfunction boundary.

</dd> <dt>

<span id="-indent"></span><span id="-INDENT"></span>**-indent**
</dt> <dd>

Do not indent the formatted trace output.

</dd> <dt>

<span id="-etl_EtlFile"></span><span id="-etl_etlfile"></span><span id="-ETL_ETLFILE"></span>**-etl** *EtlFile*
</dt> <dd>

Convert the Logman output file specified by *EtlFile* into a readable text format.

</dd> <dt>

<span id="-o_OutputFile"></span><span id="-o_outputfile"></span><span id="-O_OUTPUTFILE"></span>**-o** *OutputFile*
</dt> <dd>

Save the tracing information to the output file specified by *OutputFile*. For best performance, the output file should be located on a volume that is not part of the shadow copy.

</dd> <dt>

<span id="-help_HelpOption"></span><span id="-help_helpoption"></span><span id="-HELP_HELPOPTION"></span>**-help** *HelpOption*
</dt> <dd>

Display the command-line help as specified by *HelpOption*. The valid *HelpOption* values are **modules**, **levels**, and **all**. Specifying **modules** causes the modules to be listed. Specifying **levels** causes the available levels to be listed. Specifying **all** causes detailed help to be displayed. If no options are used, concise help is displayed.

</dd> </dl>

## Using Logman

The following procedure describes how to use Logman with your VSS application.

**To use Logman with your VSS application**

1.  Use the following command to start tracing:

    **logman start vss -o** *x:\\***vss.etl -ets -p {9138500e-3648-4edb-aa4c-859e9f7b7c38} 0xfff 170**

    > [!Note]  
    > Replace "x:\\" with the path to the directory where you would like the trace log file to be stored.

     

2.  Use the following command to stop tracing:

    **logman stop vss -ets**

The trace log file is *x:\\*vss.etl.

For more information about the Logman tool, see [Logman](/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/cc753820(v=ws.11)).

## Using Tracelog

The following procedure describes how to use Tracelog.

**To use Tracelog**

1.  Create a text file named vss.ctl that contains only the following text:

    **9138500e-3648-4edb-aa4c-859e9f7b7c38 vss**

2.  Use the following command to start tracing:

    **tracelog -start vss -f** *x:\\***vss.etl -guid vss.ctl -flag 0xff -level 0xaa**

    > [!Note]  
    > Replace "x:\\" with the path to the directory where you would like the trace log file to be stored.

     

3.  Use the following command to stop tracing:

    **tracelog -stop vss**

The trace log file is *x:\\*vss.etl.

For more information about the Tracelog tool, see [Tracelog](https://msdn.microsoft.com/library/ms797927.aspx).

 

 
