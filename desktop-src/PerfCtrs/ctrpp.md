---
Description: The CTRPP tool is a pre-processor that parses and validates your counters manifest.
ms.assetid: 3939f6a1-0a94-429d-a71e-b37f045fea13
title: CTRPP
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CTRPP
api_type: 
- NA
api_location: 
---

# CTRPP

The CTRPP tool is a pre-processor that parses and validates your counters manifest. The tool also generates code that you use to provide your counter data. You should use the generated code as a starting point when developing your provider instead of trying to generate this code yourself.

``` syntax
ctrpp -o filename -rc filename [-legacy] [-MemoryRoutines] [-NotificationCallback] 
[-prefix prefix] [-ch filename] [-backcompat] [-summary path] [-sumPath path] manifest
```

## Arguments

<dl> <dt>

<span id="-backcompat"></span><span id="-BACKCOMPAT"></span>**-backcompat**
</dt> <dd>

Used by kernel-mode drivers to generate code that is compatible with operating systems prior to Windows 7. Although the provider will run without failing on operating systems prior to Windows 7, the provider will not provide counter data.

</dd> <dt>

<span id="-ch_filename"></span><span id="-CH_FILENAME"></span>**-ch filename**
</dt> <dd>

Creates a header file that assigns symbols to the counter set names and GUIDs for each counter set in the manifest.

</dd> <dt>

<span id="-legacy"></span><span id="-LEGACY"></span>**-legacy**
</dt> <dd>

Generates code using the Windows Vista code templates. The tool generates the following files:

-   .h
-   .c
-   .rc
-   \_r.h

The .h file contains the provider GUID, a counter set GUID and [**PERF\_COUNTERSET\_INFO**](/windows/desktop/api/Perflib/ns-perflib-_perf_counterset_info) block for each counter set defined in the manifest, the function declarations for the initialization, cleanup, and notification (if specified) functions, and the provider handle that is used when starting and stopping the provider.

The .c file contains the **PerfAutoInitialize** function, the **PerfAutoCleanup** function, and the default implementation of the notification callback function. You can include the rest of your provider implementation in this file or another file.

The **PerfAutoInitialize** function calls the [**PerfStartProvider**](/windows/desktop/api/Perflib/nf-perflib-perfstartprovider) function to register the provider and the [**PerfSetCounterSetInfo**](/windows/desktop/api/Perflib/nf-perflib-perfsetcountersetinfo) function to initialize each counter set. If you specify the **-MemoryRoutines** or **-NotificationCallback** arguments, the **PerfAutoInitialize** function will call the [**PerfStartProviderEx**](/windows/desktop/api/Perflib/nf-perflib-perfstartproviderex) function instead of calling **PerfStartProvider**.

The **PerfAutoCleanup** function calls [**PerfStopProvider**](/windows/desktop/api/Perflib/nf-perflib-perfstopprovider) to remove the provider's registration from the list of registered providers and frees all resources associated with the provider.

Your provider calls the **PerfAutoInitialize** and **PerfAutoCleanup** functions.

The .c file includes the [**notification**](/windows/desktop/api/Perflib/nc-perflib-perflibrequest) callback function only if the **callback** attribute of [**provider**](https://msdn.microsoft.com/library/windows/desktop/ee781352) is set to "custom" or you use the **-NotificationCallback** argument. The generated callback includes all the callback cases. You can provide implementation for each case or remove those cases that you do not want to support.

The .rc file contains the localized strings for the counter name and description strings.

The \_r.h file contains string constant definitions.

You can use this argument with only the **-MemoryRoutines** and **-NotificationCallback** arguments.

**Windows Vista:** This argument is not supported.

</dd> <dt>

<span id="-MemoryRoutines"></span><span id="-memoryroutines"></span><span id="-MEMORYROUTINES"></span>**-MemoryRoutines**
</dt> <dd>

Changes the default signature of the [**CounterInitialize**](counterinitialize.md) function to include parameters for specifying the name of your [*AllocateMemory*](/windows/desktop/api/Perflib/nc-perflib-perf_mem_alloc) and [*FreeMemory*](/windows/desktop/api/Perflib/nc-perflib-perf_mem_free) callback functions.

**Windows Vista:** Generates function templates for memory allocation and free routines (you provide the implementation for these routines).

</dd> <dt>

<span id="-NotificationCallback"></span><span id="-notificationcallback"></span><span id="-NOTIFICATIONCALLBACK"></span>**-NotificationCallback**
</dt> <dd>

Changes the default signature of the [**CounterInitialize**](counterinitialize.md) function to include the parameter for specifying the name of your [*ControlCallback*](/windows/desktop/api/Perflib/nc-perflib-perflibrequest) callback function.

This argument is that same as including the **callback** attribute in the [**provider**](https://msdn.microsoft.com/library/windows/desktop/ee781352) element.

**Windows Vista:** Generates function templates for the notification callback (you provide the implementation for this callback).

</dd> <dt>

<span id="-o_filename"></span><span id="-O_FILENAME"></span>**-o** *filename*
</dt> <dd>

Specifies the name of the header file that the tool generates. If you do not specify a path, the file is generated in the current folder. You must specify this argument.

**Windows Vista:** This argument is not supported.

</dd> <dt>

<span id="-prefix"></span><span id="-PREFIX"></span>**-prefix**
</dt> <dd>

Specifies the prefix to use for the global variables and functions defined in the generated header file.

**Windows Vista:** This argument is not supported.

</dd> <dt>

<span id="-rc_filename"></span><span id="-RC_FILENAME"></span>**-rc** *filename*
</dt> <dd>

Specifies the name of the resource file that the tool generates. If you do not specify a path, the file is generated in the current folder. You must specify this argument.

**Windows Vista:** This argument is not supported.

</dd> <dt>

<span id="-summary_path"></span><span id="-SUMMARY_PATH"></span>**-summary path**
</dt> <dd>

Reserved.

</dd> <dt>

<span id="-sumPath_path"></span><span id="-sumpath_path"></span><span id="-SUMPATH_PATH"></span>**-sumPath path**
</dt> <dd>

Reserved.

</dd> <dt>

<span id="manifest"></span><span id="MANIFEST"></span>*manifest*
</dt> <dd>

The manifest that defines your counters. If *manifest* does not include a full path, the tool looks in the current folder.

</dd> </dl>

## Remarks

The names of the files that the tool generates are based on the name of the manifest that you pass to the CTRPP tool. For example, if the manifest name is Perf.man, the tool generates the following files for you.

-   Perf.h
-   Perf.rc

Note that these files include code for each provider included in the manifest.

The .h file contains the initialization and cleanup functions that your provider calls. The initialization function is called [***prefix*CounterInitialize**](counterinitialize.md) and the cleanup function is called [***prefix*CounterCleanup**](countercleanup.md). The function names include the *prefix* string if you specify the **-prefix** argument. The functions are inline functions.

The .h file also includes a counter set GUID and [**PERF\_COUNTERSET\_INFO**](/windows/desktop/api/Perflib/ns-perflib-_perf_counterset_info) block for each counter set defined in the manifest and the symbolic names for the provider, counter sets, and counters (if specified). You specify the symbolic names in the manifest. You can use the symbolic names when you reference the provider, counter set, or counter. For example, when calling the [**PerfCreateInstance**](/windows/desktop/api/Perflib/nf-perflib-perfcreateinstance) function, set the *CounterSetGuid* parameter to the symbolic name.

The .rc file contains the strings for the counter names and descriptions.

You cannot specify the **-legacy** argument with the **-o**, **-rc**, **-ch**, and **-prefix** arguments; they are mutually exclusive.

If you do not specify the **-legacy**, **-o**, **-ch**, or **-rc** arguments, the tool validates the manifest but does not generate any code.

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 




