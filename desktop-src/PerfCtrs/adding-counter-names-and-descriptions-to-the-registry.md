---
Description: The names and descriptions of all performance objects and their counters are stored in the registry.
ms.assetid: 6fdaccb0-45bc-48f2-8f63-3df0bdf1dca4
title: Adding Counter Names and Descriptions to the Registry
ms.topic: article
ms.date: 05/31/2018
---

# Adding Counter Names and Descriptions to the Registry

The names and descriptions of all performance objects and their counters are stored in the registry. To store names and descriptions for your objects and counters:

-   [Create a .h header file](#creating-a-symbolic-constants-h-file) that contains the symbolic constants for the offsets to your objects and counters
-   [Create an initialization (.INI) file](#creating-an-initialization-ini-file) that contains the strings
-   [Run the **lodctr** tool](#running-the-lodctr-tool), included with the computer, to load the names and descriptions into the registry

## Creating a symbolic constants (.h) file

Create a .h header file that defines constants for the offsets to the objects and counters that your provider provides. The constant values must be consecutive, even numbers beginning with zero. Group the constants by objects. The constants determine the order in which the counters are added to the name and help text in the registry. The provider uses the offsets to determine which object is being queried and the index values to use when returning the data. For details, see [Implementing OpenPerformanceData](implementing-openperformancedata.md).

The following shows an example of a symbolic constant file, named CounterOffsets.h that is used in the [Creating a Performance Extension DLL](creating-a-performance-extension-dll.md) example.


```C++
#ifndef _OFFSETS_H
#define _OFFSETS_H

// Symbol file that defines constant values for the objects
// and counters that the provider provides. The counters should be
// grouped by object.

#define TRANSFER_OBJECT      0
#define BYTES_SENT           2
#define AVAILABLE_BANDWIDTH  4

#define LAST_TRANSFER_OBJECT_COUNTER_OFFSET  AVAILABLE_BANDWIDTH

#define PEER_OBJECT          6
#define BYTES_SERVED         8

#define LAST_PEER_OBJECT_COUNTER_OFFSET  BYTES_SERVED

#endif
```



## Creating an initialization (.INI) file

The initialization (.INI) file contains the name and help strings for each object and counter defined in your symbol file. The .INI file is used as input to **lodctr** and has the following format:

``` syntax
// Information about the application that is providing the counter data.
// You must specify the DriverName and SymbolFile keys. The Trusted key is
// optional.
[info]
drivername=Application_Name
symbolfile=SymbolFile.h
trusted=

// List of performance objects that the provider supports. Value is ignored.
// Specify the object's symbolic constant for only one language identifier
// if the object supports more than one language.
[objects] 
symbol_langid_NAME=  // Performance object name string

// Specify one key for each language supported. Value is ignored.
[languages] 
langid=              // Language identifier, for example, for English use 009

// Name and description of each counter or object.
[text]  
symbol_langid_NAME=Name         // Counter name string 
symbol_langid_HELP=Description  // Help description string 
```

Although the objects section is optional, you are encourage to include this section in your .INI file. If you include this section, your performance DLL is called only if you support the requested object. If you do not include the objects section, your DLL is called for each query because the system does not know which objects you support. Also, if the object section is not included, **lodctr** generates a message in the application event log stating that the .INI file did not contain an objects section. The event identifier of this message is 2000.

The keys are defined as follows:



| Key                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **DriverName**                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Specify the name of the application's performance key located under the **HKEY\_LOCAL\_MACHINE**\\**SYSTEM**\\**CurrentControlSet**\\**Services** key. For information on creating this key, see [Creating the Application's Performance Key](creating-the-applications-performance-key.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **SymbolFile**                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Specify the .h header file that contains symbolic values of your provider's objects and counters. The header file must be in the same directory as the .INI file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Trusted**                                                                                                                                                                                                                                                                                                                                                                                                                                                       | No value. If you include this key, **lodctr** adds a Library Validation Code registry value to your performance key. The data value is a binary signature of your performance DLL. When PERFLIB calls your DLL it compare the signature with your DLL to determine if it can trust it.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Langid**                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Specify the language identifier of each language for which you are providing name and help text. To specify most languages, use the primary language identifier only. The complete list of language identifiers is in the Winnt.h header file, under the heading "Primary Language Ids." Convert the hex value found in Winnt.h into a sequence of characters that omit the  x.  For example, to specify English strings (0x09), use 009. To specify French strings (0x0C), use 00C. Note also that you can not specify Microsoft Locale ID here (e.g. 1033 for English-US.) To specify Chinese and Portuguese text, use both the primary and sublanguage identifiers. If you specify the primary identifier only, **lodctr** uses 804 (simplified Chinese) and 416 (Portuguese), respectively.**Windows Server 2003 and Windows XP:** Specify only the primary language identifier for Portuguese.<br/> <br/> |
| <dl> <dt><span id="symbol_langid_NAME"></span><span id="symbol_langid_name"></span><span id="SYMBOL_LANGID_NAME"></span>***symbol*\_*langid*\_NAME**</dt> <dd></dd> <dt><span id="symbol_langid_HELP"></span><span id="symbol_langid_help"></span><span id="SYMBOL_LANGID_HELP"></span>***symbol*\_*langid*\_HELP**</dt> <dd></dd> </dl> | Specify the text for your objects and counters. *Symbol* is the symbolic constant defined in *SymbolFile*. *Langid* is the language identifier of the text. NAME and HELP identify the text as either the name of the counter or the help text associated with the counter. The HELP text is optional, but you are encourage to provide it. The text keys can appear in any order. The length of the text strings is arbitrary. The text strings should not contain formatting characters.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                      |



 

The following is an example of an initialization file that is used in the [Creating a Performance Extension DLL](creating-a-performance-extension-dll.md) example.


```C++
// Initialization file example

[info]
drivername=MyApplication
symbolfile=CounterOffsets.h
trusted=

[objects]
TRANSFER_OBJECT_009_NAME=
PEER_OBJECT_009_NAME=

[languages] 
009=English
012=French

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

TRANSFER_OBJECT_012_NAME=Transfert
TRANSFER_OBJECT_012_HELP=Fournit des informations lio?=es aux transferts de fichiers.

BYTES_SENT_012_NAME=Octets Envoyo?=s
BYTES_SENT_012_HELP=Nombre d'octets envoyo?=s dans le dernier transfert.

AVAILABLE_BANDWIDTH_012_NAME=Bande Passante Disponible
AVAILABLE_BANDWIDTH_012_HELP=Bande passante disponible sur le ro?=seau, en octets.

PEER_OBJECT_012_NAME=Pair
PEER_OBJECT_012_HELP=Fournit des informations lio?=es o?= mise en cache homologue.

BYTES_SERVED_012_NAME=Octets Servis
BYTES_SERVED_012_HELP=Le nombre d'octets servis du cache.
```



## Running the Lodctr tool

To load the names and help strings defined in your .INI file, run the **lodctr** tool from the folder that contains your .INI file and header file. The tool is included with the computer. You must run **lodctr** with elevated privileges. For details on using the **lodctr** tool, see Help and Support Center.

The **lodctr** utility copies the strings from the .INI file to the **Counters** and **Help** registry values under the appropriate language subkeys. If the language subkey does not exist, the strings for that language are not copied. The utility also updates the **Last Counter** and **Last Help** values.

Before running **lodctr**, be sure that your application has an entry under the **Services** key. For details, see [Creating the Application's Performance Key](creating-the-applications-performance-key.md). If the key does not exist, **lodctr** will not update the registry with your names and descriptions.

As an option to running **lodctr**, you can call [**LoadPerfCounterTextStrings**](/windows/desktop/api/Loadperf/nf-loadperf-loadperfcountertextstringsa) (defined in Loadperf.h) from your installation program to load your counter names descriptions.

The performance counter names and descriptions are stored in the following location in the registry.

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
                  Library Validation Code = if the [info] section contains a trustedkey
```

 

 




