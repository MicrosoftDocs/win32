---
description: The names and descriptions of all performance objects and their counters are stored in the registry.
ms.assetid: 6fdaccb0-45bc-48f2-8f63-3df0bdf1dca4
title: Adding Counter Names and Descriptions to the Registry
ms.topic: article
ms.date: 05/31/2018
---

# Adding Counter Names and Descriptions to the Registry

> [!IMPORTANT]
> Due to significant performance and reliability limitations, the method for providing performance counter data that this topic describes may be altered or unavailable in the future. Instead, Microsoft recommends that you use the method described in [Providing Counter Data Using Version 2.0](providing-counter-data-using-version-2-0.md) for creating new performance counters and that you migrate existing performance counters to use that method.

The names and descriptions of all V1 performance objects and their counters must be installed the system. To store names and descriptions for the objects and counters from your [V1 provider](providing-counter-data.md):

- [Create a .h header file](#creating-a-symbolic-constants-h-file) that contains the symbolic constants for the offsets to your objects and counters.
- [Create an initialization (.INI) file](#creating-an-initialization-ini-file) that contains the strings.
- When installing your component, [run the **lodctr** tool](#running-the-lodctr-tool) to install the names and descriptions into the registry.
- When uninstalling your component, run the unlodctr tool to remove the names and descriptions from the registry.

## Creating a symbolic constants (.h) file

Create a .h header file that defines constants (macros) for the offsets to the objects and counters that your provider provides. The .h header is used as input to **lodctr** during installation of your provider, and may also be used by the C/C++ code of your provider.

The constant values must be consecutive, even numbers beginning with zero. Group the constants by objects (i.e. start each group with the object offset, then follow with the offsets of the counters for that object).

The constants in the header determine the order in which the counters are added to the name and help text in the registry. The provider uses the offsets to determine which object is being queried and the index values to use when returning the data. For details, see [Implementing OpenPerformanceData](implementing-openperformancedata.md).

The following shows an example of a symbolic constant file, named CounterOffsets.h, that is used in the [Creating a Performance Extension DLL](creating-a-performance-extension-dll.md) example.

```C++
#ifndef OFFSETS_H
#define OFFSETS_H

// Symbol file that defines constant values for the objects
// and counters that the provider provides. The counters should be
// grouped by object.

#define TRANSFER_OBJECT      0 // First object must be at offset 0.
#define BYTES_SENT           2 // Counters for the object follow.
#define AVAILABLE_BANDWIDTH  4 // Offsets must be even numbers.

// Not required, but for convenience in implementing the Open function:
#define LAST_TRANSFER_OBJECT_COUNTER_OFFSET  AVAILABLE_BANDWIDTH

#define PEER_OBJECT          6 // Second object must be at the next offset.
#define BYTES_SERVED         8 // Counter for the second object.

// Not required, but for convenience in implementing the Open function:
#define LAST_PEER_OBJECT_COUNTER_OFFSET  BYTES_SERVED

#endif // OFFSETS_H
```

## Creating an initialization (.INI) file

The initialization (.INI) file contains the name and help strings for each object and counter defined in your symbol file. The .INI file is used as input to **lodctr** during installation of your provider.

The .INI file should be encoded as UTF-16LE (with byte order mark) and should have the following sections and keys:

```ini
[info]
drivername=ServiceKeyName
symbolfile=SymbolFile.h
trusted=(Unused)

[objects]
<symbol>_<langid>_NAME=(Unused)

[languages]
<langid>=(Unused)

[text]
<symbol>_<langid>_NAME=Name
<symbol>_<langid>_HELP=Description
```

### [info] section

The `[info]` section contains general information about the provider. The section keys are defined as follows:

|Key|Description
|---|-----------
|**DriverName**| Specify the name of the provider's performance key located in the registry under the `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services` key. For information on creating this key, see [Creating the Application's Performance Key](creating-the-applications-performance-key.md).
|**SymbolFile**| Specify the .h header file that contains symbolic values of your provider's objects and counters. During installation (when invoking **lodctr**), the header file must be in the same directory as the .INI file.
|**Trusted**| If you include this key in the `[info]` section, **lodctr** will add a Library Validation Code registry value to your performance key with a binary signature of your performance DLL. When PERFLIB calls your DLL it compares the signature with your DLL to determine if the DLL has been modified. The value of the **Trusted** key is ignored.

The `DriverName` and `SymbolFile` keys are required.

### [objects] section

The `[objects]` section provides a list of the performance objects that the provider supports. This is used to determine whether each symbol from the `[text]` section refers an object or a counter.

For each object (counterset) supported by your provider, add one key named `<symbol>_<langid>_NAME=` to the `[objects]` section, where `<symbol>` is the name of the object and `<langid>` is the language id of one of the supported languages. The value is ignored.

> [!IMPORTANT]
> The `[objects]` section improves the performance of the system. Although the objects section is optional, you should always include this section in your .INI file. If you include this section, your performance DLL is called only if you support the requested object. If you do not include the objects section, your DLL is called for every query because the system does not know which objects your provider supports. If the object section is not included, **lodctr** generates a message in the application event log stating that the .INI file did not contain an objects section. The event identifier of this message is 2000.

### [languages] section

The `[languages]` section provides a list of the language identifiers of each language for which your provider supplies name and help strings. All providers should support `009` (English).

For each supported language, add one key named `<langid>=`. The value is ignored, but for documentation purposes the value is normally set to the name of the corresponding language, e.g. `009=English`.

For most languages, you should use the primary language identifier. The complete list of language identifiers is in the Winnt.h header file, under the heading "Primary Language Ids." Convert the value found in Winnt.h into a sequence of 3 hexadecimal digits by removing the `0x` prefix and adding leading `0` digits until the sequence is 3 digits long. For example, to specify English strings (0x9), use 009. To specify Italian strings (0x10), use 010.

Chinese and Portuguese languages require both the primary and sublanguage identifiers. Use 404, 804, 416, or 816 instead of 004 or 016.

### [text] section

The `[text]` section provides the name and help strings for your objects and counters.

For each object or counter, and for each supported language, you must provide a NAME key (containing the name or title string for your object or counter) and you may optionally provide a HELP key (containing the description or explanation string for your object or counter). The keys should be named `<symbol>_<langid>_NAME` and `<symbol>_<langid>_HELP`, where `<symbol>` is the symbolic constant for the object or counter (as defined in the symbolic constant .h file), and `<langid>` is the language identifier used for this string.

For example, the English strings for a counter with symbol `MY_COUNTER` would be specified as:

```ini
MY_COUNTER_009_NAME=My Counter
MY_COUNTER_009_HELP=Description for My Counter.
```

The text keys can appear in any order. The text strings should not contain formatting characters such as tabs.

### Example INI file

The following is an example of an initialization file that is used in the [Creating a Performance Extension DLL](creating-a-performance-extension-dll.md) sample.

```ini
[info]
drivername=MyApplication
symbolfile=CounterOffsets.h
trusted=

[objects]
TRANSFER_OBJECT_009_NAME=
PEER_OBJECT_009_NAME=

[languages]
009=English
00C=French

[text]

// English strings

TRANSFER_OBJECT_009_NAME=Transfer
TRANSFER_OBJECT_009_HELP=Provides information related to transferring files.

BYTES_SENT_009_NAME=Bytes Sent
BYTES_SENT_009_HELP=Number of bytes sent in the last transfer.

AVAILABLE_BANDWIDTH_009_NAME=Available Bandwidth
AVAILABLE_BANDWIDTH_009_HELP=Available bandwidth on the network, in bytes.

PEER_OBJECT_009_NAME=Peer
PEER_OBJECT_009_HELP=Provides information related to peer-caching.

BYTES_SERVED_009_NAME=Bytes Served
BYTES_SERVED_009_HELP=Number of bytes served from the cache.

// French strings

TRANSFER_OBJECT_00C_NAME=Transfert
TRANSFER_OBJECT_00C_HELP=Fournit des informations liées aux transferts de fichiers.

BYTES_SENT_00C_NAME=Octets Envoyés
BYTES_SENT_00C_HELP=Nombre d'octets envoyés dans le dernier transfert.

AVAILABLE_BANDWIDTH_00C_NAME=Bande Passante Disponible
AVAILABLE_BANDWIDTH_00C_HELP=Bande passante disponible sur le réseau, en octets.

PEER_OBJECT_00C_NAME=Pair
PEER_OBJECT_00C_HELP=Fournit des informations liées é mise en cache homologue.

BYTES_SERVED_00C_NAME=Octets Servis
BYTES_SERVED_00C_HELP=Le nombre d'octets servis du cache.
```

## Running the Lodctr tool

To load the names and help strings defined in your .INI file (during the installation of your provider), run the **lodctr** tool from the folder that contains your .INI file and header file. The tool is included with the computer. You must run **lodctr** with elevated privileges. The parameter to **lodctr** is the path to your .INI file. For example, `lodctr "C:\Program Files\MyCompany\MyProvider\MyProvider.ini"`.

To unload the names and help strings (during uninstall), run the **unlodctr** tool. You must run **unlodctr** with elevated privileges. The parameter to **unlodctr** is the DriverName of your provider (the name of the provider's performance key). For example, `unlodctr "MyProvider"`.

Before running **lodctr**, be sure that your application has an entry under the **Services** key. For details, see [Creating the Application's Performance Key](creating-the-applications-performance-key.md). If the key does not exist, **lodctr** will not update the registry with your names and descriptions.

As an alternative to running **lodctr**, you can call [**LoadPerfCounterTextStrings**](/windows/win32/api/loadperf/nf-loadperf-loadperfcountertextstringsw) (defined in Loadperf.h) from your installation program to load your counter names descriptions. You can then call [**UnloadPerfCounterTextStrings**](/windows/win32/api/loadperf/nf-loadperf-unloadperfcountertextstringsw) during uninstall.

The **lodctr** utility copies the strings from the .INI file to the **Counters** and **Help** registry values under the appropriate language subkeys. If the corresponding language subkey does not exist, the strings for that language are not copied. The utility also updates the **Last Counter** and **Last Help** value. The performance counter names and descriptions are stored in the following location in the registry.

```
HKEY_LOCAL_MACHINE
   \SOFTWARE
      \Microsoft
         \Windows NT
            \CurrentVersion
               \Perflib
                  Last Counter = highest counter index
                  Last Help = highest help index
                  \009
                     Counters = 2 System 4 Memory...
                     Help = 3 The System Object Type...
                  \supported language, other than English
                     Counters = ...
                     Help = ...
```

In addition to adding values under the **PerfLib** key, the **lodctr** tool also adds the following values to the **Services** node for the application. In most cases, the application and provider will have a one-to-one relationship; however, it is possible for a provider to provide counter data for multiple applications, which is why the key is based on the application and not the provider.

```
HKEY_LOCAL_MACHINE
   \SYSTEM
      \CurrentControlSet
         \Services
            \MyApplication
               \Performance
                  First Counter = lowest counter index assigned to provider
                  First Help = lowest help index assigned to provider
                  Last Counter = highest counter index assigned to provider
                  Last Help = highest help index assigned to provider
                  Object List = list of object index values if the .INI includes the [objects] section
                  Library Validation Code = if the [info] section contains a "trusted" key
```
