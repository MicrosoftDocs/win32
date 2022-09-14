---
title: Adding a Boot Image
description: This example builds on the Burning a Disc Image example by adding code to include a bootable image in the boot section of the disc.
ms.assetid: b23cdbb9-ae0d-4261-965b-56abe865f323
ms.topic: article
ms.date: 05/31/2018
---

# Adding a Boot Image

This example builds on the [Burning a Disc Image](burning-a-disc.md) example by adding code to include a bootable image in the boot section of the disc. The bootable image connects to the file system object that is written to disc. Once attached, the rest of the burning process is identical to the basic burning procedure. The boot image provides system startup using the CD or DVD disc drive.

The example hardcodes the path to the bootable image. Be sure to change the path along with other hardcoded values as appropriate.


```VB
' This script burns a boot image and data files to disc in a 
' single session  using files from a single directory tree. 

'Copyright (C) Microsoft Corp. 2006

Option Explicit

' *** CD/DVD disc file system types
Const FsiFileSystemISO9660 = 1
Const FsiFileSystemJoliet  = 2
Const FsiFileSystemUDF  = 4

WScript.Quit(Main)

Function Main
    Dim index                ' Index to recording drive.
    Dim recorder             ' Recorder object
    Dim path                 ' Directory of files to burn
    Dim stream               ' Data stream for burning device
    Dim bootFile             ' Path and filename of boot image
    
    index = 1                ' Second drive on the system
    path = "g:\BurnDir"      
    bootFile = "g:\BootImg\etfsboot.com"

    ' Create a DiscMaster2 object to connect to CD/DVD drives.
    Dim g_DiscMaster
    Set g_DiscMaster = WScript.CreateObject("IMAPI2.MsftDiscMaster2")

    ' Create a DiscRecorder object for the specified burning device.
    Dim uniqueId
    set recorder = WScript.CreateObject("IMAPI2.MsftDiscRecorder2")
    uniqueId = g_DiscMaster.Item(index)
    recorder.InitializeDiscRecorder( uniqueId )

    ' -------- Adding Boot Image Code -----
    Dim bootOptions    
    WScript.Echo "Creating BootOptions"
    SET bootOptions = WScript.CreateObject("IMAPI2FS.BootOptions")
    bootOptions.Manufacturer = "Microsoft"
    bootOptions.PlatformId   = 0       ' x86 processor
    bootOptions.Emulation    = 0       ' EmulationType.EmulationNone
    
    ' Need a stream for the boot image file 
    Const adFileTypeBinary = 1
    DIM bootStream
    Set bootStream = CreateObject("ADODB.Stream")
    WScript.Echo "Creating IStream for file " + bootFile
    bootStream.Open
    bootStream.Type = adFileTypeBinary
    bootStream.LoadFromFile bootFile
    bootOptions.AssignBootImage(bootStream)
    
    ' Create disc file system image (ISO9660 in this example)
    Dim FSI
    SET FSI = WScript.CreateObject("IMAPI2FS.MsftFileSystemImage")
    FSI.ChooseImageDefaults(Recorder)
   
    ' Add the boot directory and its contents to the file system 
    FSI.BootImageOptions = bootOptions

    ' Add the content directory and files to the file system 
    FSI.root.AddTree path, FALSE

    Dim result
    Set result = FSI.CreateResultImage()
    stream = result.ImageStream

    ' Create and write stream to disc using the specified recorder.
    Dim dataWriter
    Set dataWriter = CreateObject("IMAPI2.MsftDiscFormat2Data")
    dataWriter.recorder = Recorder
    dataWriter.ClientName = "IMAPIv2 TEST"

    dataWriter.write(stream)
    WScript.Echo "----- Finished writing content -----"

    Main = 0
End Function

```



## Related topics

<dl> <dt>

[Using IMAPI](using-imapi.md)
</dt> <dt>

[**IDiscMaster2**](/windows/desktop/api/imapi2/nn-imapi2-idiscmaster2)
</dt> <dt>

[**IDiscFormat2Data**](/windows/desktop/api/imapi2/nn-imapi2-idiscformat2data)
</dt> <dt>

[**IFileSystemImage**](/windows/desktop/api/imapi2fs/nn-imapi2fs-ifilesystemimage)
</dt> </dl>

 

 




