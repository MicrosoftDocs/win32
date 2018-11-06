---
title: File and Stream Handler Installation
description: File and Stream Handler Installation
ms.assetid: 8d007ea4-b75a-4b3f-965f-8091fcd4cb2f
ms.topic: article
ms.date: 05/31/2018
---

# File and Stream Handler Installation

The AVIFile library uses installed stream and file handlers for reading and writing AVI files and streams. A handler is installed when it resides in the Windows SYSTEM directory and the registry contains the following information needed to describe and identify a handler:

-   The 16-byte class identifier for the handler
-   A brief description of the handler
-   The name of the file containing the handler
-   The file extension that a file handler can process
-   File-access and other properties associated with a file handler
-   Four-character codes identifying stream types that a stream handler can process

The AVIFile library queries the registry for handlers that are external to an application when opening files and accessing streams. The result of a successful query returns the filename of a handler that can process the file or stream type specified in the query. The registry lists each handler by creating three entries that have the following form:


```C++
[HKEY_CLASSES_ROOT\Clsid\{00010023-0000-0000-C000-000000000046}] 
@="Wave File reader/writer" 
[HKEY_CLASSES_ROOT\Clsid\{00010023-0000-0000-C000- 
000000000046}\InprocServer32] 
@="wavefile.dll" 
"ThreadingModel"="Apartment" 
[HKEY_CLASSES_ROOT\Clsid\{00010023-0000-0000-C000- 
000000000046}\AVIFile] 
@="3" 
 
```



These entries consist of the following parts.



| Part                                   | Description                                                                                                                                                                              |
|----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HKEY\_CLASSES\_ROOT                    | Identifies the root entry of the registry.                                                                                                                                               |
| Clsid                                  | Identifies this entry as a class identifier.                                                                                                                                             |
| {00010023-0000-0000-C000-000000000046} | Specifies an interface identifier (IID) or class identifier. This value is a unique 16-byte identifier. (The identifier might also be referred to as a GUID or a UUID in other manuals.) |
| Wave File reader/writer                | Specifies a string to describe the handler. This string can be displayed in dialog boxes for selecting stream and file handlers.                                                         |
| InProcServer32                         | Specifies the file (in this example, WAVEFILE.DLL) that can be loaded to handle this class.                                                                                              |
| AVIFile                                | Specifies the properties of a file handler. In this example, the handler can read and write to an AVI file.                                                                              |



 

A file handler can have one or more of its properties stored in the registry. The following constants identify the properties currently associated with a file.



| Constant                        | Description                                                          |
|---------------------------------|----------------------------------------------------------------------|
| AVIFILEHANDLER\_CANACCEPTNONRGB | Indicates that a file handler can process image data other than RGB. |
| AVIFILEHANDLER\_CANREAD         | Indicates that a file handler can open a file with read access.      |
| AVIFILEHANDLER\_CANWRITE        | Indicates that a file handler can open a file with write access.     |



 

When creating a file or stream handler, you can obtain a new identifier by running UUIDGEN.EXE. Always use UUIDGEN.EXE to create a new identifier. The 16-byte hexadecimal number created by this executable will uniquely identify your handler.

The AVIFile library uses additional entries in the registry to identify a class identifier based on the file extension that a file handler can process or a four-character code that a file or stream handler can process. For example, the following entries associate a class identifier with the file extension .WAV and the four-character code "WAVE":


```C++
[HKEY_CLASSES_ROOT\AVIFile\Extensions\WAV] 
@="{00010023-0000-0000-C000-000000000046}" 
[HKEY_CLASSES_ROOT\AVIFile\RIFFHandlers\WAVE] 
@="{00010023-0000-0000-C000-000000000046}" 
 
```



These entries consist of the following parts.



| Part                                   | Description                                                                                       |
|----------------------------------------|---------------------------------------------------------------------------------------------------|
| HKEY\_CLASSES\_ROOT                    | Identifies the root entry of the registry.                                                        |
| AVIFile                                | Identifies this entry as an entry used by AVIFile.                                                |
| Extensions                             | Specifies the file extension (in this example, .WAV) that a file handler can process.             |
| RIFFHandlers                           | Specifies the four-character code (in this example, "WAVE") a file or stream handler can process. |
| {00010023-0000-0000-C000-000000000046} | Specifies an interface identifier (IID) or class identifier.                                      |



 

If you distribute your stream or file handler without a setup application to install it in the user's system, you must include a .REG file so the user can install the handler. The user will use the registry editor to create registry entries for your stream or file handler.

The following example shows the contents of a typical .REG file. The first entry in the following example is the descriptive string for the handler. The second entry identifies the file containing the handler. The third entry identifies the properties of the file handler (in this case, read-only access to files). The fourth entry associates the type of file the handler processes (in this case, files with a .JPG filename extension) with the class identifier.


```C++
[HKEY_CLASSES_ROOT\Clsid\{5C2B8200-E2C8-1068-B1CA-6066188C6002}] 
@="JFIF (JPEG) Files" 
[HKEY_CLASSES_ROOT\Clsid\{5C2B8200-E2C8-1068-B1CA-6066188C6002}]\InprocServer32] 
@="jfiffile.dll" 
[HKEY_CLASSES_ROOT\AVIFile\Extensions\JPG] 
@="{5C2B8200-E2C8-1068-B1CA-6066188C6002}" 
 
```



When creating this file, save it with a .REG extension to identify it as an update file for the registry. Also, substitute a unique IID for the 16-byte code used in the example.

 

 




