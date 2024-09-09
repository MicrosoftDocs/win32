---
title: C/C++ TraceLogging Examples
description: This topic contains C/C++ TraceLogging examples.
ms.assetid: FB0A29B9-D1F7-4F13-AA75-5963A0699F7A
ms.topic: article
ms.date: 06/06/2022
---

# C/C++ TraceLogging Examples

This topic contains C/C++ TraceLogging examples using TraceLoggingWrite.

- [Log simple data types](#log-simple-data-types)
- [Name event fields](#name-event-fields)
- [Log events verbosity level](#log-event-verbosity-level)
- [Log events keywords](#log-event-keywords)
- [Log array event data](#log-array-event-data)
- [Log structure event data](#log-structure-event-data)

These examples assume that you have correctly configured your program for
TraceLogging:

- Included the `TraceLoggingProvider.h` header.
- Defined a `g_hMyComponentProvider` using
  [TRACELOGGING_DEFINE_PROVIDER](/windows/win32/api/traceloggingprovider/nf-traceloggingprovider-tracelogging_define_provider).
- Registered your provider at program startup using
  [TraceLoggingRegister](/windows/win32/api/traceloggingprovider/nf-traceloggingprovider-traceloggingregister).
- Unregistered your provider at program exit using
  [TraceLoggingUnregister](/windows/win32/api/traceloggingprovider/nf-traceloggingprovider-traceloggingunregister).

```c
#include <windows.h>
#include <TraceLoggingProvider.h>
#include <winmeta.h> // Define constants e.g. WINEVENT_LEVEL_VERBOSE

// Define the GUID to use in TraceLoggingProviderRegister
TRACELOGGING_DEFINE_PROVIDER(
    g_hMyComponentProvider,
    "SimpleTraceLoggingProvider",
    // {0205c616-cf97-5c11-9756-56a2cee02ca7}
    (0x0205c616,0xcf97,0x5c11,0x97,0x56,0x56,0xa2,0xce,0xe0,0x2c,0xa7));

// The following example functions are defined later in this topic.
void SimpleDataTypes();
void NamingData();
void LevelsAndKeywords();
void CombineKeywords();
void Arrays();
void Structs();

void main()
{
    // Register the provider
    TraceLoggingRegister(g_hMyComponentProvider);

    // Log events using the g_hMyComponentProvider handle...
    SimpleDataTypes();
    NamingData();
    LevelsAndKeywords();
    CombineKeywords();
    Arrays();
    Structs();

    // Stop TraceLogging and unregister the provider
    TraceLoggingUnregister(g_hMyComponentProvider);
}
```

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

## Log simple data types

This example shows how to log simple data types such as integers, booleans, and
so on.

```C++
void SimpleDataTypes()
{
    UINT8 u8 = 200;
    INT32 i32 = -2000000000;
    UINT32 u32 = 4000000000;
    INT64 i64 = 9000000000000000000;
    float f32 = 3.14f;
    BOOL b = TRUE;
    bool bcpp = true;

    TraceLoggingWrite(
        g_hMyComponentProvider,
        "NumericValues",
        TraceLoggingUInt8(u8, "MyByteValue"),
        TraceLoggingInt32(i32, "MyIntValue"),
        TraceLoggingUInt32(u32, "MyUInt"),
        TraceLoggingHexUInt32(u32, "MyHexValue"),
        TraceLoggingInt64(i64, "MyBigValue"),
        TraceLoggingFloat32(f32, "MyFloat"),
        TraceLoggingBool(b, "MyBool32"),
        TraceLoggingBoolean(bcpp, "MyC++Boolean")
        );

#ifdef __cplusplus

    /*
    TraceLoggingValue() automatically determines the value type (C++ only).
    In many cases, TraceLoggingValue() can be used instead of a more specific macro.
    */

    TraceLoggingWrite(
        g_hMyComponentProvider,
        "NumericValues",
        TraceLoggingValue(u8, "MyByteValue"),
        TraceLoggingValue(i32, "MyIntValue"),
        TraceLoggingValue(u32, "MyUInt"),
        TraceLoggingHexUInt32(u32, "MyHexValue"), // TraceLoggingValue won't format as hexadecimal.
        TraceLoggingValue(i64, "INT64"),
        TraceLoggingValue(f32, "float"),
        TraceLoggingBool(b, "BOOL"), // TraceLoggingValue considers BOOL the same as int.
        TraceLoggingValue(bcpp, "bool (C++)") // But bool is a distinct type so this works ok.
        );

#endif

    /*
    Strings and chars
    */

    TraceLoggingWrite(
        g_hMyComponentProvider,
        "Strings and Chars",
        TraceLoggingString("String1", "String (char)"),
        TraceLoggingWideString(L"LString2", "String (wide char)"),
        TraceLoggingChar('A', "Single char")
        );

    /*
    Other types
    */

    /*
    NOTE: In C, a GUID, FILETIME, or SYSTEMTIME value parameter must be an l-value.
    */

    INT_PTR iptr = 1234;
    UINT_PTR uptr = 4321;
    FILETIME ft;
    SYSTEMTIME st;
    SID const sid1 = { SID_REVISION, 1, 5, { 6 } };
    static const GUID s_TestGuid = { 0x3970f9cf, 0x2c0c, 0x4f11, { 0xb1, 0xcc, 0xe3, 0xa1, 0xe9, 0x95, 0x88, 0x33 } };

    GetSystemTime(&st);
    GetSystemTimeAsFileTime(&ft);

    TraceLoggingWrite(
        g_hMyComponentProvider,
        "Other Types",
        TraceLoggingGuid(s_TestGuid, "GUID"),
        TraceLoggingSystemTime(st, "Current Time (FILETIME)"),
        TraceLoggingPointer(&iptr, "Pointer value"), // Logs the pointer value, not the data.
        TraceLoggingSid(&sid1, "SID")
        TraceLoggingIntPtr(iptr, "INT_PTR"),
        TraceLoggingUIntPtr(uptr, "UINT_PTR")
        );
}
```

### Name event fields

The example shows how to name event fields.

```C++
void NamingData()
{
    UINT32 Cat = 0xCA7;

    /*
    Each of the following four events are equivalent:
    */

    /*
    TraceLogging uses the symbol to automatically name the field "Cat"
    and assign it the value contained in the variable Cat (0xCA7).
    */

    TraceLoggingWrite(
        g_hMyComponentProvider,
        "Cat1",
        TraceLoggingUInt32(Cat) // Field is automatically named "Cat"
        );

    TraceLoggingWrite(
        g_hMyComponentProvider,
        "Cat2",
        TraceLoggingValue(Cat) // Field is automatically named "Cat"
        );


    /*
    Use a different symbol for the value of the event's "Cat" field.
    */

    UINT32 Tiger = Cat;

    /*
    Now we need to explicitly name the datum or we will have events with a
    different field name ("Tiger").
    */

    TraceLoggingWrite(
        g_hMyComponentProvider,
        "Tiger",
        TraceLoggingUInt32(Tiger, "Cat") // Field is explicitly named "Cat".
        );

    TraceLoggingWrite(
        g_hMyComponentProvider,
        "Cat3",
        TraceLoggingValue(Tiger, "Cat") // Field is explicitly named "Cat".
        );
};
```

### Log event verbosity level

This example shows how to log events by verbosity level.

```C++
#include <winmeta.h> // for WINEVENT_LEVEL_* definitions
void LevelsAndKeywords()
{
    /*
    Verbosity levels and event keywords must be compile-time constants.
    If TraceLoggingLevel is not used, the default is 5 (VERBOSE).
    If TraceLoggingKeyword is not used, the defualt is 0 (no categories).

    TraceLoggingLevel accepts values 0-255.
    TraceLoggingKeyword accepts values 0 to UINT64_MAX. Each bit is a category.

    Level and keyword are the primary system for filtering events. All events
    should have a meaningful (non-zero) level and keyword to enable filtering.
    See winmeta.h for predefined verbosity levels and reserved keyword values.
    */

    PCWSTR MyName = L"Joe";
    INT16 MyRank = 99;
    ULONG MySerialNumber = 12345;

    /*
    The following is only logged when session verbosity level is
    WINEVENT_LEVEL_VERBOSE (5) or higher ...
    */

    TraceLoggingWrite(
        g_hMyComponentProvider,
        "Levels",
        TraceLoggingLevel(WINEVENT_LEVEL_VERBOSE),
        TraceLoggingWideString(MyName, "Name"),
        TraceLoggingInt16(MyRank, "Rank"),
        TraceLoggingUInt32(MySerialNumber, "Serial Number")
        );

    /*
    TraceLoggingWrite will not complain if TraceLoggingLevel is invoked more than once.
    However, only the last level will be used.
    The following event is only logged at WINEVENT_LEVEL_VERBOSE or higher...
    */

    TraceLoggingWrite(
        g_hMyComponentProvider,
        "Levels",
        TraceLoggingLevel(WINEVENT_LEVEL_CRITICAL),
        TraceLoggingLevel(WINEVENT_LEVEL_VERBOSE),
        TraceLoggingWideString(MyName, "Name"),
        TraceLoggingInt16(MyRank, "Rank"),
        TraceLoggingUInt32(MySerialNumber, "Serial Number")
        );
}
```

### Log event keywords

This example illustrates how to set event keywords. Event filtering can be done
by level and keyword. For example, scenario completion events or failure events
might be grouped under separate keywords so that you can easily filter those
events.

```C++
void CombineKeywords()
{
    /*
    Keywords can be combined using multiple TraceLoggingKeyword() macros ...
    */

    #define MY_PROVIDER_KEYWORD_BLUE    0x1
    #define MY_PROVIDER_KEYWORD_YELLOW  0x2
    #define MY_PROVIDER_KEYWORD_GREEN   (MY_PROVIDER_KEYWORD_BLUE | MY_PROVIDER_KEYWORD_YELLOW)

    PCWSTR Status = L"Feeling a bit green";

    /*
    These events are equivalent...
    */

    TraceLoggingWrite(
        g_hProvider,
        "Keywords",
        TraceLoggingKeyword(MY_PROVIDER_KEYWORD_GREEN),
        TraceLoggingValue(Status, "Current Status")
        );

    TraceLoggingWrite(
        g_hProvider,
        "Keywords",
        TraceLoggingKeyword(MY_PROVIDER_KEYWORD_BLUE | MY_PROVIDER_KEYWORD_YELLOW),
        TraceLoggingValue(Status, "Current Status")
        );

    TraceLoggingWrite(
        g_hProvider,
        "Keywords",
        TraceLoggingKeyword(MY_PROVIDER_KEYWORD_BLUE),
        TraceLoggingKeyword(MY_PROVIDER_KEYWORD_YELLOW),
        TraceLoggingValue(Status, "Current Status")
        );
}
```

### Log array event data

This example shows how to log arrays as event data.

```C++
void Arrays()
{
    INT32 IntValsFixed[5] = {20, 21, 22, 23, 24};
    UINT cIntVals = 5;
    INT32* IntValsVar = new INT32[cIntVals];

    VERIFY_IS_NOT_NULL(IntValsVar);
    memcpy(IntValsVar, IntValsFixed, sizeof(IntValsFixed));


    /*
    Variable size arrays
    */

    TraceLoggingWrite(
        g_hMyComponentProvider,
        "Variable Size Arrays",
        TraceLoggingInt32Array(IntValsVar, (UINT16)cIntVals, "Variable size int array"),
        TraceLoggingInt32Array(IntValsVar, 5, "Variable size int array")
        );

    /*
    Fixed size arrays

    Fixed size array macros use the "FixedArray" suffix.
    The absence of the suffix indicates a variable sized array.
    */

    TraceLoggingWrite(
        g_hMyComponentProvider,
        "Constant Size Arrays",
        TraceLoggingInt32FixedArray(IntValsFixed, _countof(IntValsFixed), "Constant size int array")
        );

    delete [] IntValsVar;
}
```

### Log structure event data

This example shows how to log structure event data.

```C++
void Structs()
{
    WIN32_FIND_DATA FindData;
    HANDLE hFind = FindFirstFile(".", &FindData);

    VERIFY_IS_TRUE(hFind != INVALID_HANDLE_VALUE);

    /*
    TraceLoggingStruct defines a group of related fields in an event.
    The first parameter, which must be a compile-time constant, indicates
    the number of subsequent fields that are to be considered part of the
    struct.
    */

    TraceLoggingWrite(
        g_hMyComponentProvider,
        "FindFirstFile",
        TraceLoggingStruct(5, "FileData"),
            TraceLoggingString(FindData.cFileName, "Name"),
            TraceLoggingUInt32(FindData.dwFileAttributes, "Attributes"),
            TraceLoggingFileTime(FindData.ftCreationTime, "CreateTime"),
            TraceLoggingUInt32(FindData.nFileSizeHigh, "SizeHigh"),
            TraceLoggingUInt32(FindData.nFileSizeLow, "SizeLow"),
        TraceLoggingPointer(hFind, "Result")
        );

    /*
    ... or ...
    */

#define LogWin32FindData(fd) \
    TraceLoggingStruct(5, "FileData"), \
    TraceLoggingString(((fd).cFileName), "Name"), \
    TraceLoggingUInt32(((fd).dwFileAttributes), "Attributes"), \
    TraceLoggingFileTime(((fd).ftCreationTime), "CreateTime"), \
    TraceLoggingUInt32(((fd).nFileSizeHigh), "SizeHigh"), \
    TraceLoggingUInt32(((fd).nFileSizeLow), "SizeLow")

    TraceLoggingWrite(
        g_hMyComponentProvider,
        "FindFirstFile",
        LogWin32FindData(FindData),
        TraceLoggingPointer(hFind, "Result")
        );

    FindClose(hFind);
}
```
