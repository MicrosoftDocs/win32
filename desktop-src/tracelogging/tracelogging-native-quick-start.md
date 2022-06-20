---
title: TraceLogging C/C++ Quick Start
description:
  The following section describes the basic steps required to add TraceLogging
  to native user-mode code.
ms.assetid: 444DA34B-7949-457D-A3EC-2F0CFBEDD1E2
ms.topic: article
ms.date: 06/06/2022
---

# TraceLogging C/C++ Quick Start

The following section describes the basic steps required to add TraceLogging to
C/C++ user-mode code.

## Prerequisites

- Microsoft Visual Studio 2013 or later.
- Windows 10 Software Development Kit (SDK) is required to write a user-mode
  provider.
- Windows Driver Kit (WDK) for Windows 10 is required to write a kernel-mode
  provider.

> [!IMPORTANT]
> To avoid linker errors for unresolved `EventRegister`,
> `EventWriteTransfer`, or `EventUnregister` functions, link with `advapi32.lib`
> when compiling these examples.

To collect and decode events from these examples, you will need to start a trace
using a tool like tracelog or traceview, run the example, stop the trace using a
tool like tracelog or traceview, and decode the trace using a decoding tool like
tracefmt or traceview. For example, if my provider was defined using GUID
`{0205c616-cf97-5c11-9756-56a2cee02ca7}`, I might view the events from these
examples using Windows SDK tools
[tracelog](/windows-hardware/drivers/devtest/tracelog) and
[tracefmt](/windows-hardware/drivers/devtest/tracefmt) as follows:

- `tracelog -start MyTraceSession -f MyTraceFile.etl -guid #0205c616-cf97-5c11-9756-56a2cee02ca7`
- Run the example.
- `tracelog -stop MyTraceSession`
- `tracefmt -o MyTraceFile.txt MyTraceFile.etl`
- `notepad MyTraceFile.txt`

## SimpleTraceLoggingExample.h

This example header includes the TraceLogging APIs and forward declares the
provider handle that will be used to log events. Any class that wishes to use
TraceLogging will include this header and can then start logging.

```C++
#pragma once

#include <windows.h> // Definitions required by TraceLoggingProvider.h
#include <TraceLoggingProvider.h> // The C/C++ TraceLogging API

// Forward-declare the g_hMyComponentProvider variable that you will use for tracing in this component
TRACELOGGING_DECLARE_PROVIDER(g_hMyComponentProvider);

```

The header file includes `TraceLoggingProvider.h` which defines the C/C++
TraceLogging API. You must include `windows.h` first because it defines
constants used by `TraceLoggingProvider.h`.

The header file forward declares the provider handle `g_hMyComponentProvider`
that you will pass to the TraceLogging APIs to log events. This handle needs to
be accessible to any code that wishes to use TraceLogging.

[**TRACELOGGING_DECLARE_PROVIDER**](/windows/desktop/api/traceloggingprovider/nf-traceloggingprovider-tracelogging_declare_provider)
is a macro that creates an `extern const TraceLoggingHProvider` handle using the
name that you provide, which in the example above is `g_hMyComponentProvider`.
You will allocate the actual provider handle variable in a code file.

## SimpleTraceLoggingExample.cpp

The following example registers the provider, logs an event, and unregisters the
provider.

```C++
#include "SimpleTraceLoggingExample.h"

// Define a handle to a TraceLogging provider
TRACELOGGING_DEFINE_PROVIDER(
    g_hMyComponentProvider,
    "SimpleTraceLoggingProvider",
    // {0205c616-cf97-5c11-9756-56a2cee02ca7}
    (0x0205c616,0xcf97,0x5c11,0x97,0x56,0x56,0xa2,0xce,0xe0,0x2c,0xa7));

void main()
{

    char sampleValue[] = "Sample value";

    // Register the provider
    TraceLoggingRegister(g_hMyComponentProvider);

    // Log an event
    TraceLoggingWrite(g_hMyComponentProvider, // handle to my provider
        "HelloWorldTestEvent",              // Event Name that should uniquely identify your event.
        TraceLoggingValue(sampleValue, "TestMessage")); // Field for your event in the form of (value, field name).

    // Stop TraceLogging and unregister the provider
    TraceLoggingUnregister(g_hMyComponentProvider);
}
```

The example above includes SimpleTraceLoggingExample.h which contains the global
provider variable that your code will use to log events.

The
[**TRACELOGGING_DEFINE_PROVIDER**](/windows/desktop/api/traceloggingprovider/nf-traceloggingprovider-tracelogging_define_provider)
macro allocates storage and defines the provider handle variable. The variable
name that you provide to this macro must match the name you used in the
[**TRACELOGGING_DECLARE_PROVIDER**](/windows/desktop/api/traceloggingprovider/nf-traceloggingprovider-tracelogging_declare_provider)
macro in your header file.

### Register the provider handle

Before you can use the provider handle to log events you must call
[**TraceLoggingRegister**](/windows/desktop/api/traceloggingprovider/nf-traceloggingprovider-traceloggingregister)
to register your provider handle. This is typically done in main() or DLLMain()
but can be done at any time as long as it precedes any attempt to log an event.
If you log an event before registering the provider handle, no error will occur
but the event will not be logged. The following code from the example above
registers the provider handle.

```C++
// Define the GUID to use in TraceLoggingProviderRegister
TRACELOGGING_DEFINE_PROVIDER(
    g_hMyComponentProvider,
    "SimpleTraceLoggingProvider",
    // {0205c616-cf97-5c11-9756-56a2cee02ca7}
    (0x0205c616,0xcf97,0x5c11,0x97,0x56,0x56,0xa2,0xce,0xe0,0x2c,0xa7));

void main()
{
    char sampleValue[] = "Sample value";

    // Register the provider
    TraceLoggingRegister(g_hMyComponentProvider);
```

### Log a Tracelogging event

After the provider is registered, the following code logs a simple event.

```C++
    // Log an event
    TraceLoggingWrite(g_hMyComponentProvider, // handle to my provider
        "HelloWorldTestEvent",              // Event Name that should uniquely identify your event.
        TraceLoggingValue(sampleValue, "TestMessage")); // Field for your event in the form of (value, field name).
```

The
[**TraceLoggingWrite**](/windows/desktop/api/traceloggingprovider/nf-traceloggingprovider-traceloggingwrite)
macro accepts up to ninety-nine arguments. The event name is stored in UTF-8
format. You must not use embedded `'\0'` characters in the event name or field
names. There are no other limits on permitted characters, though some event
decoders or event processors might have their own limitations.

Each argument following the event name must be wrapped inside of a
[TraceLogging Wrapper Macro](tracelogging-wrapper-macros.md). If you are using
C++, you can use the `TraceLoggingValue` wrapper macro to automatically deduce
the type of the argument. If you are writing in C or if you want more control
over the field type, you must use type-specific field macros such as
`TraceLoggingInt32`, `TraceLoggingUnicodeString`, `TraceLoggingString`, etc.

In addition to logging single events you can also group events by activity by
using the
[**TraceLoggingWriteActivity**](/windows/desktop/api/traceloggingprovider/nf-traceloggingprovider-traceloggingwriteactivity)
or
[**TraceLoggingWriteStart**](/windows/desktop/api/traceloggingactivity/nf-traceloggingactivity-traceloggingwritestart)/[**TraceLoggingWriteStop**](/windows/desktop/api/traceloggingactivity/nf-traceloggingactivity-traceloggingwritestop)
macros found in TraceLoggingActivity.h. Activities correlate events and are
useful for scenarios that have a beginning and an end. For example, you might
use an activity to measure a scenario that starts with the launch of an
application, includes the time it takes for the splash screen becomes available,
and ends when the initial screen of the application becomes visible.

Activities capture single events and nest other activities that occur between
the start and end of that activity. Activities have per-process scope and must
be passed from thread to thread to properly nest multi-threaded events.

The scope of a provider handle is limited to the module (DLL, EXE, or SYS file)
in which it is defined. The handle should not be passed to other DLLs. If a
[**TraceLoggingWrite**](/windows/desktop/api/traceloggingprovider/nf-traceloggingprovider-traceloggingwrite)
macro is invoked in A.DLL using a provider handle defined in B.DLL, it may cause
problems. The safest and most efficient way to meet this requirement is to just
always directly reference the global provider handle and never pass the provider
handle as a parameter.

### Unregister the provider

Before your component unloads, you must unregister the TraceLogging provider.
This is especially important for DLLs and drivers. A crash is likely if a DLL or
a driver unloads without unregistering the provider.

The following code unregisters the provider:

```C++
// Stop TraceLogging and unregister the provider
TraceLoggingUnregister(g_hMyComponentProvider);
```

## Compatibility

Depending on its configuration, TraceLoggingProvider.h can be
backwards-compatible (resulting program will run onWindows Vista or later), or
can be optimized for later OS versions. TraceLoggingProvider.h uses WINVER
(user-mode) and NTDDI_VERSION (kernel-mode) to determine whether it should be
compatible with earlier OS versions or be optimized for newer OS versions.

For user-mode, if you include `<windows.h>` before setting WINVER, `<windows.h>`
sets WINVER to the SDK's default target OS version. If WINVER is set to 0x602 or
higher, `TraceLoggingProvider.h` optimizes its behavior for Windows 8 or later
and your app will not run on earlier versions of Windows. If you need your
program to run on Vista or Windows 7, be sure to set WINVER to the appropriate
value before including `<windows.h>`.

Similarly, if you include `<wdm.h>` before setting NTDDI_VERSION, `<wdm.h>` sets
NTDDI_VERSION to a default value. If NTDDI_VERSION is set to 0x06040000 or
higher, TraceLoggingProvider.h optimizes its behavior for Windows 10 and your
driver will not work on earlier versions of Windows.

This behavior can be controlled direction by setting
`TLG_HAVE_EVENT_SET_INFORMATION` before including `TraceLoggingProvider.h`.
Refer to the comments in the `TraceLoggingProvider.h` header for details on the
`TLG_HAVE_EVENT_SET_INFORMATION` macro.

## Summary and next steps

To see how to capture and view TraceLogging data using the Windows Performance
Tools (WPT), see
[Record and Display TraceLogging Events](tracelogging-record-and-display-tracelogging-events.md).

See [C/C++ Tracelogging Examples](tracelogging-c-cpp-tracelogging-examples.md)
for more C++ TraceLogging examples.
