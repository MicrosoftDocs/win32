---
title: Checking Media Support
description: The following script examines characteristics of the media loaded in the disc device.
ms.assetid: 05d88612-ff4c-4894-b838-a1d76923430c
ms.topic: article
ms.date: 05/31/2018
---

# Checking Media Support

The following script examines characteristics of the media loaded in the disc device. More specifically, it checks the media type and the current state of the media, as well as recorder and media compatibility. This script can be adapted to verify compatibility and state issues before using the media.


```VB
' This script examines characteristics of the media loaded in the disc device.

' Copyright (C) Microsoft Corp. 2006

Option Explicit

' *** IMAPI2 Media Types 
Const IMAPI_MEDIA_TYPE_UNKNOWN            = 0  ' Media not present OR
                                               ' is unrecognized
Const IMAPI_MEDIA_TYPE_CDROM              = 1  ' CD-ROM
Const IMAPI_MEDIA_TYPE_CDR                = 2  ' CD-R
Const IMAPI_MEDIA_TYPE_CDRW               = 3  ' CD-RW
Const IMAPI_MEDIA_TYPE_DVDROM             = 4  ' DVD-ROM
Const IMAPI_MEDIA_TYPE_DVDRAM             = 5  ' DVD-RAM
Const IMAPI_MEDIA_TYPE_DVDPLUSR           = 6  ' DVD+R
Const IMAPI_MEDIA_TYPE_DVDPLUSRW          = 7  ' DVD+RW
Const IMAPI_MEDIA_TYPE_DVDPLUSR_DUALLAYER = 8  ' DVD+R dual layer
Const IMAPI_MEDIA_TYPE_DVDDASHR           = 9  ' DVD-R
Const IMAPI_MEDIA_TYPE_DVDDASHRW          = 10 ' DVD-RW
Const IMAPI_MEDIA_TYPE_DVDDASHR_DUALLAYER = 11 ' DVD-R dual layer
Const IMAPI_MEDIA_TYPE_DISK               = 12 ' Randomly writable

' *** IMAPI2 Data Media States
Const IMAPI_FORMAT2_DATA_MEDIA_STATE_UNKNOWN            = 0
Const IMAPI_FORMAT2_DATA_MEDIA_STATE_INFORMATIONAL_MASK = 15    
Const IMAPI_FORMAT2_DATA_MEDIA_STATE_UNSUPPORTED_MASK   = 61532 '0xfc00
Const IMAPI_FORMAT2_DATA_MEDIA_STATE_OVERWRITE_ONLY     = 1
Const IMAPI_FORMAT2_DATA_MEDIA_STATE_BLANK              = 2
Const IMAPI_FORMAT2_DATA_MEDIA_STATE_APPENDABLE         = 4     
Const IMAPI_FORMAT2_DATA_MEDIA_STATE_FINAL_SESSION      = 8
Const IMAPI_FORMAT2_DATA_MEDIA_STATE_DAMAGED            = 1024 '0x400
Const IMAPI_FORMAT2_DATA_MEDIA_STATE_ERASE_REQUIRED     = 2048 '0x800
Const IMAPI_FORMAT2_DATA_MEDIA_STATE_NON_EMPTY_SESSION  = 4096 '0x1000
Const IMAPI_FORMAT2_DATA_MEDIA_STATE_WRITE_PROTECTED    = 8192 '0x2000
Const IMAPI_FORMAT2_DATA_MEDIA_STATE_FINALIZED          = 16384 '0x4000
Const IMAPI_FORMAT2_DATA_MEDIA_STATE_UNSUPPORTED_MEDIA  = 32768 '0x8000


WScript.Quit(Main)

Function Main
    Dim Index                ' Index to recording drive.
    Dim recorder             ' Recorder object
    Dim Stream               ' Data stream for burning device
    
    Index = 1                ' Second drive on the system

    ' Create a DiscMaster2 object to connect to CD/DVD drives.
    Dim g_DiscMaster
    Set g_DiscMaster = WScript.CreateObject("IMAPI2.MsftDiscMaster2")

    ' Create a DiscRecorder object for the specified burning device.
    Dim uniqueId
    set recorder = WScript.CreateObject("IMAPI2.MsftDiscRecorder2")
    uniqueId = g_DiscMaster.Item(index)
    recorder.InitializeDiscRecorder( uniqueId )

    ' Define the new disc format and set the recorder
    Dim dataWriter
    Set dataWriter = CreateObject ("IMAPI2.MsftDiscFormat2Data")
    dataWriter.recorder = recorder

    Dim boolResult
    boolResult = dataWriter.IsRecorderSupported(recorder)
    If boolResult = True then
        WScript.Echo "--- Current recorder IS supported. ---"
    else
        WScript.Echo "Current recorder IS NOT supported."
    end if

    boolResult = dataWriter.IsCurrentMediaSupported(recorder)
    If boolResult = True then
        WScript.Echo "--- Current media IS supported. ---"
    else
        WScript.Echo "Current media IS NOT supported."
    end if

    WScript.Echo "ClientName = " & dataWriter.ClientName

    ' Check a few CurrentMediaStatus possibilities. Each status
    ' is associated with a bit and some combinations are legal.
    Dim curMediaStatus
    curMediaStatus = dataWriter.CurrentMediaStatus
    WScript.Echo "Checking Current Media Status"
    
    if IMAPI_FORMAT2_DATA_MEDIA_STATE_UNKNOWN AND curMediaStatus then
        WScript.Echo "    Media state is unknown."
    end if

    if IMAPI_FORMAT2_DATA_MEDIA_STATE_OVERWRITE_ONLY AND curMediaStatus then
        WScript.Echo "    Currently, only overwriting is supported."
    end if
    
    if IMAPI_FORMAT2_DATA_MEDIA_STATE_APPENDABLE AND curMediaStatus then
        WScript.Echo "    Media is currently appendable."
    end if
    
    if IMAPI_FORMAT2_DATA_MEDIA_STATE_FINAL_SESSION AND curMediaStatus then
        WScript.Echo "    Media is in final writing session."
    end if
    
    if IMAPI_FORMAT2_DATA_MEDIA_STATE_DAMAGED AND curMediaStatus then
        WScript.Echo "    Media is damaged."
    end if
    
    Dim mediaType
    mediaType = dataWriter.CurrentPhysicalMediaType
    WScript.Echo "Current Media Type"
    DisplayMediaType(MediaType)

    WScript.Echo 
    WScript.Echo "----- Finished -----"
    Main = 0
End Function

Sub DisplayMediaType(dMediaType)
    Select Case dmediaType 
        Case IMAPI_MEDIA_TYPE_UNKNOWN
            WScript.Echo "    Empty device or an unknown disc type."
        
        Case IMAPI_MEDIA_TYPE_CDROM
            WScript.Echo "    CD-ROM"
        
        Case IMAPI_MEDIA_TYPE_CDR
            WScript.Echo "    CD-R"
        
        Case IMAPI_MEDIA_TYPE_CDRW
            WScript.Echo "    CD-RW"
        
        Case IMAPI_MEDIA_TYPE_DVDROM
            WScript.Echo "    Read-only DVD drive and/or disc"
        
        Case IMAPI_MEDIA_TYPE_DVDRAM
            WScript.Echo "    DVD-RAM"
        
        Case IMAPI_MEDIA_TYPE_DVDPLUSR
            WScript.Echo "    DVD+R"
        
        Case IMAPI_MEDIA_TYPE_DVDPLUSRW
            WScript.Echo "    DVD+RW"
        
        Case IMAPI_MEDIA_TYPE_DVDPLUSR_DUALLAYER
            WScript.Echo "    DVD+R Dual Layer media"
        
        Case IMAPI_MEDIA_TYPE_DVDDASHR
            WScript.Echo "    DVD-R"
        
        Case IMAPI_MEDIA_TYPE_DVDDASHRW
            WScript.Echo "    DVD-RW"
        
        Case IMAPI_MEDIA_TYPE_DVDDASHR_DUALLAYER
            WScript.Echo "    DVD-R Dual Layer media"
        
        Case IMAPI_MEDIA_TYPE_DISK
            WScript.Echo "    Randomly-writable, hardware-defect " _
                + "managed media type "
            WScript.Echo "    that reports the ""Disc"" profile " _
                + "as current."
        End Select
End Sub
```



## Related topics

<dl> <dt>

[Using IMAPI](using-imapi.md)
</dt> <dt>

[**IMAPI\_MEDIA\_PHYSICAL\_TYPE**](/windows/desktop/api/imapi2/ne-imapi2-imapi_media_physical_type)
</dt> <dt>

[**IDiscMaster2**](/windows/desktop/api/imapi2/nn-imapi2-idiscmaster2)
</dt> <dt>

[**IDiscRecorder2**](/windows/desktop/api/imapi2/nn-imapi2-idiscrecorder2)
</dt> <dt>

[**IDiscFormat2Data**](/windows/desktop/api/imapi2/nn-imapi2-idiscformat2data)
</dt> </dl>

 

 




