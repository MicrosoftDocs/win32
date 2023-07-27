---
description: Debug Output Functions
ms.assetid: dfe44c8c-43ec-461f-952f-b87256b82ee6
title: Debug Output Functions
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Debug Output Functions

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The [DirectShow Base Classes](directshow-base-classes.md) provide several macros for displaying debugging information.



| Function                                               | Description                                                                                          |
|--------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| [**DbgCheckModuleLevel**](dbgcheckmodulelevel.md)     | Checks whether logging is enabled for the given message types and level.                             |
| [**DbgDumpObjectRegister**](dbgdumpobjectregister.md) | Displays information about active objects.                                                           |
| [**DbgInitialise**](dbginitialise.md)                 | Initializes the debug library.                                                                       |
| [**DbgLog**](dbglog.md)                               | Sends a string to the debug output location, if logging is enabled for the specified type and level. |
| [**DbgOutString**](dbgoutstring.md)                   | Sends a string to the debug output location.                                                         |
| [**DbgSetModuleLevel**](dbgsetmodulelevel.md)         | Sets the logging level for one or more message types.                                                |
| [**DbgTerminate**](dbgterminate.md)                   | Cleans up the debug library.                                                                         |
| [**DisplayType**](displaytype.md)                     | Sends information about a media type to the debug output location.                                   |
| [**DumpGraph**](dumpgraph.md)                         | Sends information about a filter graph to the debug output location.                                 |
| [**GuidNames**](guidnames.md)                         | Global array that contains strings representing the GUIDs defined in Uuids.h.                        |
| [**NAME**](name.md)                                   | Generates a debug-only string.                                                                       |
| [**NOTE**](note.md)                                   | Sends a string to the debug output location.                                                         |
| [**REMIND**](remind.md)                               | Generates a reminder at compile time.                                                                |



 

**Registry Keys**

The debug output function in DirectShow use a set of registry keys. The location of these registry keys depends on the version of Windows.

*Prior to Windows Vista*, the debugging keys are located under the following path:

**HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Debug**

In Windows Vista or later, they are located under the following path:

**HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Microsoft**\\**DirectShow**\\**Debug**

For third-party filters, the location depends on which version of the [DirectShow Base Classes](directshow-base-classes.md) was used to build the filter. The version included in the Windows SDK for Windows Vista uses the newer path. Previous versions used the older path.

In the remarks that follow, the label *&lt;DebugRoot&gt;* is used to indicate these two paths. Substitute the correct path, depending on the version of Windows or the version of the base classes.

**Debug Logging**

DirectShow defines several message types, shown in the following table.



| Value                   | Description                                             |
|-------------------------|---------------------------------------------------------|
| LOG\_ERROR              | Error notification.                                     |
| LOG\_LOCKING            | Locking and unlocking of critical sections.             |
| LOG\_MEMORY             | Memory allocation, and object creation and destruction. |
| LOG\_TIMING             | Timing and performance measurements.                    |
| LOG\_TRACE              | General call tracing.                                   |
| CUSTOM1 through CUSTOM5 | Available for custom debug messages                     |



 

Each of the DirectShow debug logging functions specifies a message type and a log level. The debug message is displayed only when the current debugging level for that message type is equal to or greater than the level specified in the logging function. Otherwise, the message is ignored.

For example, the following code outputs the string "This is a debug message" if the LOG\_TRACE level is 3 or higher:

``` syntax
DbgLog((LOG_TRACE, 3, TEXT("This is a debug message")));
```

Every module can set its own debugging level for each message type. (A *module* is a DLL or executable that can be loaded using the **LoadLibrary** function.) A module's debugging levels appear in the registry under the following key:

**HKEY\_LOCAL\_MACHINE**\\**&lt;DebugRoot&gt;**\\**&lt;ModuleName&gt;**\\**&lt;MessageType&gt;**

where *\<Message Type\>* is the message type minus the initial "LOG\_"; for example, **LOCKING** for LOG\_LOCKING messages. When a module is loaded, the debug library finds the module's logging levels in the registry. If the registry keys do not exist, the debug library creates them.

A module can also set its own levels at run time, using the [**DbgSetModuleLevel**](dbgsetmodulelevel.md) function. To send a message to the debug output, call the [**DbgLog**](dbglog.md) macro. The following example creates a level 3 message of type LOG\_TRACE:

You can also specify global logging levels, with the following registry key:


```C++
\HKEY_LOCAL_MACHINE\<DebugRoot>\GLOBAL\<Message Type>
```



The debug library uses whichever level is greater, the global level or the module level.

**Debug Output Location**

The debug output location is determined by another registry key:

**HKEY\_LOCAL\_MACHINE**\\**&lt;DebugRoot&gt;**\\**\<Modile Name\>**\\**LogToFile**

If the value of this key is `Console`, the output goes to the console window. If the value is `Deb`, `Debug`, `Debugger`, or an empty string, the output goes to the debugger window. Otherwise, the output is written to a file specified by the registry key.

Before an executable uses the DirectShow debug library, it must call the [**DbgInitialise**](dbginitialise.md) function. Afterward, it must call the [**DbgTerminate**](dbgterminate.md) function. DLLs do not need to call these functions, because the DLL entry point (defined in the base class library) calls them automatically.

## Related topics

<dl> <dt>

[Debugging Utilities](debugging-utilities.md)
</dt> </dl>

 

 



