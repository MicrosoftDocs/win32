---
title: ISRResGraphEx and IAttributes
description: ISRResGraphEx and IAttributes
ms.assetid: 6eb37da1-5252-4c41-891c-c19cca6fb7d1
ms.topic: article
ms.date: 05/31/2018
---

# ISRResGraphEx and IAttributes

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

The results objects returned by the engine must support the ISRResGraphEx interface and the IAttributes interface. Merely supporting the ISRResGraphEx interface is enough to enable the sound editor to provide word break information, but does not provide the necessary support for phoneme information.

The sound editor requires that engines also support a special DWord attribute, **SRATTR\_PHONESEG**. The editor queries the engines to see IAttributes interface and attempts to set the **SRATTR\_PHONESEG** to 1. If that call succeeds, the sound editor assumes that the engine's results will support the gathering of phoneme-segmentation information from results object.

`#define    SRATTR_PHONESEG    MAKELONG (1, SRVEN_MICROSOFT)`

When a results object is transmitted to the sound editor, it queries that object for its implementation of ISRResGraphEx. ISRResGraphEx contains a member function, DataGet, with type signature

`HRESULT  DataGet  (DWord, dwID, GUID gAttrib, SDATA *psData)`

Where **dwID** is the identifier of the graph object, **gAttrib** is a GUID corresponding to the attribute sought, and **psData** is a pointer to an SDATA object containing the data returned. The engine is responsible for allocating the data stored in **psData** through [**CoTaskMemAlloc**](/windows/desktop/api/combaseapi/nf-combaseapi-cotaskmemalloc). The calling application (in this case the sound editor) is responsible for freeing it through [**CoTaskMemFree**](/windows/desktop/api/combaseapi/nf-combaseapi-cotaskmemfree) when it is finished.

DataGet is required to recognize three predefined GUIDs, which are listed in the SAPI documentation. An engine which returns a success code to the call to **DWORDSet(SRATTR\_PHONESEG, 1)** is also required to recognize a specific GUID, **SRGARC\_PHONEMESEGMENTATION**, when called with a **dwID** that corresponds to an edge in the graph.

`DEFINE_GUID(SRGARC_PHONMESEGMENTATION, 0xd05405b0, 0x1db1, 0x11d2, 0x94, 0x2, 0x0, 0xc0, 0x4f, 0x8e, 0xf4, 0x8f);`

When the call returns, **psData** should point to an array of DWORD-aligned structure of type **PHONESEG**, defined by:

``` syntax
typedef struct tagSRPHONESEG {
   DWORD   dwSize;       // Size of the SRPHONESEG structure + phone data
   QWORD   qwStartTime;  // SAPI timestamp of the start of the seqment
   …QWORD   qwEndTime;    // SAPI timestamp of the end of the seqment
   int      nScore;      // The segment's score
   WCHAR   aPhones[0];   // Array of phone(s) making up the segment
} SRPHONESEG,  *PSRPHONESEG;
```

where **qwStartTime** and **qwEndTime** point to the beginning and end of each phoneme making up the word covered by the edge, and **aPhones** is an array of Unicode characters corresponding to the IPA representation of the phone, which were produced in this segment. (In some languages, there are phonemes which are spelled with more than one IPA phoneme. In English, for instance, the "long I" sound in the word "live" is actually a diphthong, made up of two simpler phonemes concatenated together.) The **aPhones** array should be zero terminated and padded at the end to make each **SRPHONESEG** structure in the array an even multiple of four bytes long.

For example, suppose the word spoken on arc 4 was "made". Then the call to DataGet(4, **SRGARC\_PHONEMESEGMENTATION**, &sd) might return an array of three phoneme segments, /m/ running from **qwStartTime**=328434 bytes to **qwEndTime**=330354 bytes, /1e/ running from **qwStartTime**=330354 bytes to **qwEndTime**=344114 bytes, and /d/ running from **qwStartTime**=344114 bytes to **qwEndTime**=347314 bytes. These would be presented as a packed array of three **SRPHONESEG** structures of sizes 28, 32, and 28 bytes, respectively. Notice that there is some padding at the end of the middle **SRPHONESEG** structure, so that the next item in the array starts at a 4-byte boundary.

The SAPI 4.0 SDK includes a tool (SRFunc) for testing compliance with the SAPI 4.0 spec. Included in that tool is a test for compliance with this set of interfaces. The source code for that tool is a good place to start in order to understand how these interfaces will interact with the sound editor, and to debug the interfaces during development.

 

 