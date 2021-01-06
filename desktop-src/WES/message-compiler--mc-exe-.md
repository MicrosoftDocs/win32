---
title: Message Compiler (MC.exe)
description: Used to compile instrumentation manifests and message text files.
ms.assetid: f9de35f1-6d31-4f4b-b2c4-8474d6fce9e0
keywords:
- Message Compiler (MC.exe) EventLog
topic_type:
- apiref
api_name:
- Message Compiler (MC.exe)
api_type:
- NA
ms.topic: reference
ms.date: 06/03/2020
---

# Message Compiler (MC.exe)

Used to compile instrumentation manifests and message text files. The compiler generates the message resource files to which your application links.

``` syntax
MC [-?aAbcdnouUv] [-m <length>] [-h <path>] [-e <extension>] [-r <path>]
   [-x <path>] [-w <file>] [-W <file>] [-z <basename> ] [-cp <encoding>]
   [-km | -um | -generateProjections | -cs <namespace>]
   [-mof] [-p <prefix>] [-P <prefix>]
   [<filename.man>] [<filename.mc>]
```

-   [Arguments common to both message text files and manifest files](#arguments-common-to-both-message-text-files-and-manifest-files)
-   [Arguments specific to manifest files](#arguments-specific-to-manifest-files)
-   [Arguments specific to generating code that your provider would use to log events](#arguments-specific-to-generating-code-that-your-provider-would-use-to-log-events)
-   [Arguments specific to message text files](#arguments-specific-to-message-text-files)

## Arguments common to both message text files and manifest files

<dl> <dt>

<span id="-_"></span>**-?**
</dt> <dd>

Displays the usage information for the Message Compiler.

</dd> <dt>

<span id="-c"></span><span id="-C"></span>**-c**
</dt> <dd>

Use this argument to have the compiler set the customer bit (bit 28) in all message IDs. For information on the customer bit, see winerror.h.

</dd> <dt>

<span id="-cp"></span><span id="-CP"></span>**-cp** *encoding*
</dt> <dd>

Use this argument to specify the character encoding used for all generated text files. Valid names include "ansi" (default), "utf-8", and "utf-16". The Unicode encodings will add a byte order mark.

</dd> <dt>

<span id="-e_extension"></span><span id="-E_EXTENSION"></span>**-e** *extension*
</dt> <dd>

Use this argument to specify the extension to use for the header file. You can specify up to a three characters extension, not including the period. The default is .h.

</dd> <dt>

<span id="-h_path"></span><span id="-H_PATH"></span>**-h** *path*
</dt> <dd>

Use this argument to specify the folder into which you want the compiler to place the generated header file. The default is the current directory.

</dd> <dt>

<span id="-m_length"></span><span id="-M_LENGTH"></span>**-m** *length*
</dt> <dd>

Use this argument to have the compiler generate a warning if the any message exceeds *length* characters.

</dd> <dt>

<span id="-r_path"></span><span id="-R_PATH"></span>**-r** *path*
</dt> <dd>

Use this argument to specify the folder into which you want the compiler to place the generated resource compiler script (.rc file) and the generated .bin files (binary resources) that the resource compiler script includes. The default is the current directory.

</dd> <dt>

<span id="-z_name"></span><span id="-Z_NAME"></span>**-z** *name*
</dt> <dd>

Use this argument to override the default base name that the compiler uses for the files that it generates. The default is to use the base name of the *filename* input file.

</dd> <dt>

<span id="filename"></span><span id="FILENAME"></span>*filename*
</dt> <dd>

The instrumentation manifest file or message text file. The file must exist in the current directory. You can specify a manifest file, message text file, or both. The file name must include the extension. The convention is to use a .man extension for manifest files and a .mc extension for message text files.

</dd> </dl>

### Arguments specific to manifest files

<dl> <dt>

<span id="-s_path"></span><span id="-S_PATH"></span>**-s** *path*
</dt> <dd>

Use this argument to create a baseline of your instrumentation. Specify the path to the folder that contains your baseline manifest files. For subsequent releases, you would then use the **-t** argument to check the new manifest against the baseline for compatibility issues.

**Prior to MC version 1.12.7051:** Not available

</dd> <dt>

<span id="-t_path"></span><span id="-T_PATH"></span>**-t** *path*
</dt> <dd>

Use this argument when you create a new version of your manifest and want to check it for application compatibility against the baseline that you created using the **-s** argument. The path must point to the folder that contains the .BIN files that the baseline operation created (see the **-s** switch).

**Prior to MC version 1.12.7051:** Not available

</dd> <dt>

<span id="-w_path"></span><span id="-W_PATH"></span>**-w** *path*
</dt> <dd>

The compiler ignores this argument and automatically validates the manifest.

**Prior to MC version 1.12.7051:** Use this argument to specify the folder that contains the Eventman.xsd schema file, which the compiler uses to validate your manifest. The Windows SDK includes the Eventman.xsd schema file in the \\Include folder. If you do not specify this argument, the compiler does not validate your manifest.

</dd> <dt>

<span id="-W_path"></span><span id="-w_path"></span><span id="-W_PATH"></span>**-W** *path*
</dt> <dd>

The compiler ignores this argument.

**Prior to MC version 1.12.7051:** Use this argument to specify the folder that contains the Winmeta.xml file. The Winmeta.xml file contains the recognized input and output types as well as the predefined channels, levels, and opcodes. The Windows SDK includes the Winmeta.xml file in the \\Include folder.

</dd> </dl>

### Arguments specific to generating code that your provider would use to log events

You can use the following compiler arguments to generate kernel-mode or user-mode code that you can use to log events. You can also request that the compiler generate code to support writing events on computers prior to Windows Vista. If your application is written C#, the compiler can generate a C# class that you can use to log events. These arguments are available beginning with MC version 1.12.7051 that ships with the Windows 7 version of the Window SDK.

<dl> <dt>

<span id="-co"></span><span id="-CO"></span>**-co**
</dt> <dd>

Use this argument to have the logging service call your user-defined function for each event that you log (the function is called after the event has been logged). Your user-defined function must have the following signature.


```C++
VOID
pFnUserFunction(
    __in REGHANDLE RegHandle,
    __in PCEVENT_DESCRIPTOR Descriptor,
    __in ULONG EventDataCount,
    __in_ecount(EventDataCount) PEVENT_DATA_DESCRIPTOR EventData
    );
```



You must also include the following directive in your code.

`#define MCGEN_CALLOUT pFnUserFunction`

You should keep your implementation as short as possible to prevent logging issues; the service will not log anymore of your events until the function returns.

You can use this argument with the **-km** or **-um** argument.

</dd> <dt>

<span id="-cs_namespace"></span><span id="-CS_NAMESPACE"></span>**-cs** *namespace*
</dt> <dd>

Use this argument to have the compiler generate a C# class based on the .NET 3.5 [EventProvider](/dotnet/api/system.diagnostics.eventing.eventprovider?view=netframework-3.5&preserve-view=true) class.

</dd> <dt>

<span id="-css_namespace"></span><span id="-CSS_NAMESPACE"></span>**-css** *namespace*
</dt> <dd>

Use this argument to have the compiler generate a static C# class based on the .NET 3.5 [EventProvider](/dotnet/api/system.diagnostics.eventing.eventprovider?view=netframework-3.5&preserve-view=true) class.

</dd> <dt>

<span id="-km"></span><span id="-KM"></span>**-km**
</dt> <dd>

Use this argument to have the compiler generate the kernel-mode code that you would use to log the events defined in your manifest.

</dd> <dt>

<span id="-mof"></span><span id="-MOF"></span>**-mof**
</dt> <dd>

DEPRECATED. Use this argument to have the compiler generate code that you can use to log events on computers prior to Windows Vista. This option also creates a MOF file that contains the MOF classes for each event defined in the manifest. To register the classes in the MOF file so that consumers can decode the events, use the MOF compiler (Mofcomp.exe). For details on using the MOF compiler, see [Managed Object Format](/windows/desktop/WmiSdk/managed-object-format--mof-).

To use this switch, you must adhere to the following restrictions:

-   Every event definition must include the task and opcode attributes
-   Every task must include the eventGuid attribute
-   The template data that the event references cannot contain:
    -   Data items that specify the win:Binary or win:SYSTEMTIME input types
    -   Structures
    -   Variable sized arrays; however, you can specify fixed length arrays
    -   String data types cannot specify the length attribute

You must use this argument with the **-um**, **-cs**, **-css**, or **-km** argument

</dd> <dt>

<span id="-p_prefix"></span><span id="-P_PREFIX"></span>**-p** *prefix*
</dt> <dd>

Use this argument to override the default prefix that the compiler uses for the logging macro names and method names. The default prefix is "EventWrite". The string is case-sensitive.

You can use this argument with the **-um**, **-cs**, **-css**, or **-km** argument.

</dd> <dt>

<span id="-P_prefix"></span><span id="-p_prefix"></span><span id="-P_PREFIX"></span>**-P** *prefix*
</dt> <dd>

Use this argument to remove characters from the beginning of the symbolic name that you specified for the event. The comparison is case-insensitive. The compiler uses the symbolic name to form the logging macro names and method names.

The default name for a logging macro is EventWrite*SymbolName*, where *SymbolName* is the symbolic name that you specified for the event. For example, if you set the symbol attribute of the event to PrinterConnection, the macro name would be EventWritePrinterConnection. To remove Printer from the name, use **-P** **Printer**, which results in EventWriteConnection.

You can use this argument with the **-um**, **-cs**, **-css**, or **-km** argument.

</dd> <dt>

<span id="-um"></span><span id="-UM"></span>**-um**
</dt> <dd>

Use this argument to have the compiler generate the user-mode code that you would use to log the events defined in your manifest.

</dd> </dl>

To have the compiler generate logging code, you must specify the **-um**, **-cs**, **-css**, or **-km** argument; these arguments are mutually exclusive.

To specify where to place the .h, .cs, and .mof files that the compiler generates, use the **-h** argument. If you do not specify the **-h** argument, the files are placed in the current folder.

To specify where to place the .rc file and binary files (that contain the metadata resources) that the compiler generates, use the **-r** argument. If you do not specify the **-r** argument, the files are placed in the current folder.

The compiler uses the base name of the input file as the base name of the files that it generates. To specify a base name, use the **-z** argument.

### Arguments specific to message text files

<dl> <dt>

<span id="-a"></span><span id="-A"></span>**-a**
</dt> <dd>

Use this argument to specify that the *filename* input file contains content in the system-default Windows ANSI code page (CP_ACP). This is the default. Use **-u** for Unicode. If the input file contains a BOM this argument will be ignored.

</dd> <dt>

<span id="-A"></span><span id="-a"></span>**-A**
</dt> <dd>

DEPRECATED. Use this argument to specify that the messages in the output .bin file should be ANSI.

</dd> <dt>

<span id="-b"></span><span id="-B"></span>**-b**
</dt> <dd>

Use this argument to have the compiler use the base name of the *filename* input file for the .bin file names. The default is to use "MSG".

</dd> <dt>

<span id="-d"></span><span id="-D"></span>**-d**
</dt> <dd>

Use this argument to use decimal values for the Severity and Facility constants in the header file instead of hexadecimal values.

</dd> <dt>

<span id="-n"></span><span id="-N"></span>**-n**
</dt> <dd>

Use this argument to specify that messages terminate immediately after the message body. The default is to terminate the message body with a CR/LF.

</dd> <dt>

<span id="-o"></span><span id="-O"></span>**-o**
</dt> <dd>

Use this argument to have the compiler generate an OLE2 header file using **HRESULT** definitions instead of status codes. Using status codes is the default.

</dd> <dt>

<span id="-u"></span><span id="-U"></span>**-u**
</dt> <dd>

Use this argument to specify that the *filename* input file contains UTF-16LE content. The default is ANSI content. If the input file contains a BOM this argument will be ignored.

</dd> <dt>

<span id="-U"></span><span id="-u"></span>**-U**
</dt> <dd>

Use this argument to specify that the messages in the output .bin file should be Unicode. This is the default.

</dd> <dt>

<span id="-v"></span><span id="-V"></span>**-v**
</dt> <dd>

Use this argument to generate verbose output.

</dd> <dt>

<span id="-x_path"></span><span id="-X_PATH"></span>**-x** *path*
</dt> <dd>

Use this argument to specify the folder into which you want the compiler to place the .dbg C include file. The .dbg file maps message IDs to their symbolic names.

</dd> </dl>

## Remarks

The **-A** and **-mof** arguments are deprecated and will be removed in the future.

The compiler accepts as input a manifest (.man) file or a message text (.mc) file and generates the following files:

-   *filename*.h

    A C/C++ header file that contains the event descriptors, provider GUID, and symbol names that you reference in your application.

-   *filename*TEMP.bin

    A binary resource file that contains the provider and event metadata. This is the template resource, which is signified by the TEMP suffix of the base name of the file.

-   Msg00001.bin

    A binary resource file for each language that you specify (for example, if your manifest contains message strings in en-US and fr-FR, the compiler would generate Msg00001.bin and Msg00002.bin).

-   *filename*.rc

    A resource compiler script that contains the statements to include each .bin file as a resource.

For arguments that take a path, the path can be an absolute, relative, or UNC path and it can contain environment variables.

**Prior to MC version 1.12.7051:** The compiler does not allow relative paths or environment variables.

The Windows SDK includes the compiler (mc.exe) in the \\Bin folder.

## Examples

The following example compiles a manifest using the compiler defaults.

``` syntax
mc spooler.man
```

The following example compiles the manifest and places the header and resource files in the specified folders.

``` syntax
mc -h <pathgoeshere> -r <pathgoeshere> spooler.man
```

## Requirements

| Requirement | Value |
|--------------------------|-------------------------------------------------|
| Minimum supported client | Windows 2000 Professional \[desktop apps only\] |
| Minimum supported server | Windows 2000 Server \[desktop apps only\]       |
