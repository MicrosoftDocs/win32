---
description: The SESSION structure contains information about the current session.
ms.assetid: e04571f9-eeb7-4612-8cb2-05aca7b5df06
title: SESSION structure
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SESSION
api_type: 
- NA
api_location: 
---

# SESSION structure

\[This structure contains information required only when using the **DeleteExtractedFiles** and **Extract** functions, which are not supported. This documentation is provided for informational purposes only.\]

The **SESSION** structure contains information about the current session.

## Syntax


```C++
typedef struct {
  ACTION    act;
  HFILELIST hflist;
  BOOL      fAllCabinets;
  BOOL      fOverwrite;
  BOOL      fNoLineFeed;
  BOOL      fSelfExtract;
  long      cbSelfExtractSize;
  long      cbSelfExtractSize;
  int       ahfSelf[cMAX_CAB_FILE_OPEN];
  int       cErrors;
  HFDI      hfdi;
  ERF       erf;
  long      cFiles;
  long      cbTotalBytes;
  PERROR    perr;
  SPILLERR  se;
  long      cbSpill;
  char      achSelf[cbFILE_NAME_MAX];
  char      achMsg[cbMAX_LINE*2];
  char      achLine;
  char      achLocation;
  char      achFile;
  char      achDest;
  char      achCabPath;
  BOOL      fContinuationCabinet;
  BOOL      fShowReserveInfo;
  BOOL      fNextCabCalled;
  CABINET   acab[2];
  char      achZap[cbFILE_NAME_MAX];
  char      achCabinetFile[cbFILE_NAME_MAX];
  int       cArgv;
  char      **pArgv;
  int       fDestructive;
  USHORT    iCurrentFolder;
} SESSION, *PSESSION;
```



## Members

<dl> <dt>

**act**
</dt> <dd>

The action to perform. This member can be one of the values from the following enumerated type.

``` syntax
typedef enum {
    actBAD,         // Invalid action
    actHELP,        // Show help
    actDEFAULT,     // Perform default action based on command line arguments
    actDIRECTORY,   // Force display of cabinet directory
    actEXTRACT,     // Force file extraction
    actCOPY,        // Do single file-to-file copy
} ACTION;  
```

</dd> <dt>

**hflist**
</dt> <dd>

The handle to a list of files specified on the command line. This datatype is declared as follows:

`typedef void *HFILELIST;`

</dd> <dt>

**fAllCabinets**
</dt> <dd>

A flag that indicates whether more than one cabinet file should be processed. If this value is **TRUE**, continuation cabinets are processed.

</dd> <dt>

**fOverwrite**
</dt> <dd>

A flag that indicates whether existing files should be overwritten. If this value is **TRUE**, existing files are overwritten.

</dd> <dt>

**fNoLineFeed**
</dt> <dd>

A flag that indicates whether the last `printf` call has the newline (`\n`) characters. If this value is **TRUE**, the last `printf` call did not include the newline characters.

</dd> <dt>

**fSelfExtract**
</dt> <dd>

A flag that indicates whether a cabinet is self extracting. If this value is **TRUE**, the cabinet is self extracting.

</dd> <dt>

**cbSelfExtractSize**
</dt> <dd>

The length of the executable (.exe) portion of a self-extracting cabinet.

</dd> <dt>

**cbSelfExtractSize**
</dt> <dd>

The length of the CAB portion of a self-extracting cabinet.

</dd> <dt>

**ahfSelf**
</dt> <dd>

The file handles to the cabinet.

`#define cMAX_CAB_FILE_OPEN    2 `

</dd> <dt>

**cErrors**
</dt> <dd>

The count of errors encountered during the extraction session.

</dd> <dt>

**hfdi**
</dt> <dd>

A handle to the FDI context. This datatype is declared as follows:

`typedef void FAR *HFDI; `

</dd> <dt>

**erf**
</dt> <dd>

The FDI error structure. See [**ERF**](/windows/win32/api/fdi_fci_types/ns-fdi_fci_types-erf).

</dd> <dt>

**cFiles**
</dt> <dd>

The count of files processed.

</dd> <dt>

**cbTotalBytes**
</dt> <dd>

The total number of bytes extracted.

</dd> <dt>

**perr**
</dt> <dd>

The pass through FDI.

</dd> <dt>

**se**
</dt> <dd>

The spill file error. This member can be one of the values from the following enumerated type.

``` syntax
typedef enum {
    seNONE,                     // No error
    seNOT_ENOUGH_MEMORY,        // Not enough RAM
    seCANNOT_CREATE,            // Cannot create spill file
    seNOT_ENOUGH_SPACE,         // Not enough space for spill file
} SPILLERR;
```

</dd> <dt>

**cbSpill**
</dt> <dd>

The size of the spill file requested.

</dd> <dt>

**achSelf**
</dt> <dd>

The name of the executable (.exe) file.

`#define cbFILE_NAME_MAX     256`

</dd> <dt>

**achMsg**
</dt> <dd>

The message formatting buffer.

`#define cbMAX_LINE          256`

</dd> <dt>

**achLine**
</dt> <dd>

The line formatting buffer.

</dd> <dt>

**achLocation**
</dt> <dd>

The output directory.

</dd> <dt>

**achFile**
</dt> <dd>

The current file name being extracted.

</dd> <dt>

**achDest**
</dt> <dd>

The forced destination file name.

</dd> <dt>

**achCabPath**
</dt> <dd>

The path to look at for a cabinet file.

</dd> <dt>

**fContinuationCabinet**
</dt> <dd>

A flag that indicates whether the current cabinet is the first one processed. If set to **TRUE**, it is not the first cabinet processed.

</dd> <dt>

**fShowReserveInfo**
</dt> <dd>

A flag that indicates whether reserve information should be provided. If set to **TRUE**, the information is made available.

</dd> <dt>

**fNextCabCalled**
</dt> <dd>

This member provides a way to determine which of the **acab** entries to use if we are processing all files in a cabinet set (**fAllCabinet** is set to **TRUE**).

</dd> <dt>

**acab**
</dt> <dd>

The last two entries in the cabinet set. This structure is defined as follows:

``` syntax
typedef struct {
    char    achCabPath[cbFILE_NAME_MAX];     // Cabinet file path
    char    achCabFilename[cbFILE_NAME_MAX]; // Cabinet file name.ext
    char    achDiskName[cbFILE_NAME_MAX];    // User readable disk label
    USHORT  setID;
    USHORT  iCabinet;
} CABINET;
typedef CABINET *PCABINET;
```

</dd> <dt>

**achZap**
</dt> <dd>

The prefix to strip from the file name.

`#define cbFILE_NAME_MAX     256`

</dd> <dt>

**achCabinetFile**
</dt> <dd>

The current cabinet file.

`#define cbFILE_NAME_MAX     256`

</dd> <dt>

**cArgv**
</dt> <dd>

The default self-extracting argc.

</dd> <dt>

**pArgv**
</dt> <dd>

A pointer to a pointer to the default self-extracting argv\[\].

</dd> <dt>

**fDestructive**
</dt> <dd>

A flag that minimizes the disk space needed when set to **TRUE**.

</dd> <dt>

**iCurrentFolder**
</dt> <dd>

If **fDestructive** is set to **TRUE**, extract only the current folder.

</dd> </dl>

## See also

<dl> <dt>

[**DeleteExtractedFiles**](deleteextractedfiles.md)
</dt> <dt>

[**Extract**](extract.md)
</dt> </dl>

 

 
