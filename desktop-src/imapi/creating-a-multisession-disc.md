---
title: Creating a Multisession Disc
ms.assetid: 327304c4-fdb9-47c6-9b19-49100b933590
description: "Learn more about: Creating a Multisession Disc"
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Multisession Disc

The [Image Mastering API](about-imapi.md) (IMAPI) supports the addition and removal of files to, or from, the following multisession disc types:

-   CD-R/CD-RW
-   Single-Layer DVD+R/DVD-R
-   DVD+R Dual Layer
-   BD-R
-   DVD-RW/DVD+RW (**Windows 7 Only**)
-   DVD-RAM (**Windows 7 Only**)
-   BD-RE (**Windows 7 Only**)

Creation of a multisession disc using IMAPI consists of the following steps. Each of these documented steps contains the relevant portion of the complete Visual Basic script example provided in the final section.

## Initializing the Disc Recorder

Prior to device initialization, the **MsftDiscMaster2** object provides an enumeration of the optical devices on the system. The [**IDiscMaster2**](/windows/desktop/api/imapi2/nn-imapi2-idiscmaster2) interface provides access to this device enumeration to facilitate the location of the appropriate recording device. The **MsftDiscMaster2** object also provides event notifications when optical devices are added to or removed from a machine.

After locating an optical recorder and retrieving the ID assigned to it, create a new **MsftDiscMaster2** object and initialize the recorder using the specific device ID.

The [**IDiscRecorder2**](/windows/desktop/api/imapi2/nn-imapi2-idiscrecorder2) interface provides access to basic device information such as vendor ID, product ID, product revision, as well as the methods to eject media or close the tray.

> [!Note]  
> The additional constants and dimensions declared in the following sample are used later in the complete sample script located in the final section of this document. These elements are not required for the act of initializing a disc recorder.

 


```VB
' *** CD/DVD disc file system types
Const FsiFileSystemISO9660 = 1
Const FsiFileSystemJoliet  = 2
Const FsiFileSystemUDF102  = 4

WScript.Quit(Main)

Function Main
    Dim Index                ' Index to recording drive.
    Dim Recorder             ' Recorder object
    Dim Path                 ' Directory of files to add
    Dim Stream               ' Data stream for burning device
    
    Index = 0                ' First drive on the system
    Path = "G:\BurnDir"      ' Files to add to the disc

    ' Create a DiscMaster2 object to connect to optical drives.
    Dim DiscMaster
    Set DiscMaster = WScript.CreateObject("IMAPI2.MsftDiscMaster2")

    ' Create a DiscRecorder2 object for the specified burning device.
    Dim UniqueId
    set Recorder = WScript.CreateObject("IMAPI2.MsftDiscRecorder2")
    UniqueId = DiscMaster.Item(Index)
    Recorder.InitializeDiscRecorder(UniqueId)
```



## Creating a Data Writer

The **MsftDiscFormat2Data** object provides the writing method, its properties, as well as the media-specific properties. The [**IDiscFormat2Data**](/windows/desktop/api/imapi2/nn-imapi2-idiscformat2data) interface provides access to this object.

The disc recorder binds to the format writer using the [**IDiscFormat2Data::put\_Recorder**](/windows/desktop/api/imapi2/nf-imapi2-idiscformat2data-put_recorder) property. After the recorder is bound to the format writer, media and write-specific property queries can be performed prior to writing the result image to disc using the [**IDiscFormat2Data::Write**](/windows/desktop/api/imapi2/nf-imapi2-idiscformat2data-write) method.

> [!Note]  
> The client name string specified in the sample code below should be adjusted as appropriate for the specific application.

 


```VB
    ' Create a DiscFormat2Data object and set the recorder
    Dim DataWriter
    Set DataWriter = CreateObject ("IMAPI2.MsftDiscFormat2Data")
    DataWriter.Recorder = Recorder
    DataWriter.ClientName = "IMAPIv2 TEST"
```



## Creating the File System Object

In order to record a new session, a burn image must be generated for it first. A burn image for **ISO9660**, **Joliet** and **UDF** formats consist of file systems of individual files and directories. The **MsftFileSystemImage** object is the file system object that contains the files and directories to be placed on the optical media. The [**IFileSystemImage**](/windows/desktop/api/imapi2fs/nn-imapi2fs-ifilesystemimage) interface provides access to the file system object and settings.


```VB
    ' Create a new file system image object
    Dim FSI
    Set FSI = CreateObject("IMAPI2FS.MsftFileSystemImage")
```



## Importing a File System

Before proceeding, ensure that the disc is not blank by checking the [**IDiscFormat2::get\_MediaHeuristicallyBlank**](/windows/desktop/api/imapi2/nf-imapi2-idiscformat2-get_mediaheuristicallyblank) property.

After creating the **MsftFileSystemImage** object, the [**IFileSystemImage::put\_MultisessionInterfaces**](/windows/desktop/api/imapi2fs/nf-imapi2fs-ifilesystemimage-put_multisessioninterfaces) property should be initialized prior to a call to either the [**IFileSystemImage::ImportFileSystem**](/windows/desktop/api/imapi2fs/nf-imapi2fs-ifilesystemimage-importfilesystem) or [**IFileSystemImage::ImportSpecificFileSystem**](/windows/desktop/api/imapi2fs/nf-imapi2fs-ifilesystemimage-importspecificfilesystem) method to import the file system from the last recorded session. These methods will automatically populate the **MsftFileSystemImage** object with information describing the previously recorded files and directories.

> [!Note]  
> The [**IFileSystemImage::put\_MultisessionInterfaces**](/windows/desktop/api/imapi2fs/nf-imapi2fs-ifilesystemimage-put_multisessioninterfaces) property is typically initialized with the multisession interfaces provided by the data writer via the [**IDiscFormat2Data::get\_MultisessionInterfaces**](/windows/desktop/api/imapi2fs/nf-imapi2fs-ifilesystemimage-get_multisessioninterfaces) property.

 

Attempts to set the **IFileSystemImage::put\_MultisessionInterfaces** property will fail if IMAPI does not support multisession for the currently inserted media or the media cannot be appended for some other reason (e.g. because it is closed).

If the previous burn session contained more than one file system type, the [**IFileSystemImage::ImportFileSystem**](/windows/desktop/api/imapi2fs/nf-imapi2fs-ifilesystemimage-importfilesystem) method will import information from the most advanced file system type present. For example, in the example provided in this topic, UDF is the imported file system. However, use of the [**IFileSystemImage::ImportSpecificFileSystem**](/windows/desktop/api/imapi2fs/nf-imapi2fs-ifilesystemimage-importspecificfilesystem) method allows the specific selection of the file system to import.

> [!Note]  
> The [**IFileSystemImage::IdentifyFileSystemsOnDisc**](/windows/desktop/api/imapi2fs/nf-imapi2fs-ifilesystemimage-identifyfilesystemsondisc) method can be used to determine which file systems are available on the disc.

 


```VB
    ' Import the last session, if the disc is not empty, or initialize
    ' the file system, if the disc is empty
    If Not DataWriter.MediaHeuristicallyBlank _
    Then
        On Error Resume Next
        FSI.MultisessionInterfaces = DataWriter.MultisessionInterfaces
        If Err.Number <> 0 _
        Then
            WScript.Echo "Multisession is not supported for this disc"
            Main = 1
            Exit Function
        End If
        On Error Goto 0

        WScript.Echo "Importing data from the previous session..."
        FSI.ImportFileSystem()
    Else 
        FSI.ChooseImageDefaults(Recorder)
    End If
```



## Adding or Removing Files to the File System

After creating the file system object and importing the file system from the previous session, call the [**IFileSystemImage::CreateFileItem**](/windows/desktop/api/imapi2fs/nf-imapi2fs-ifilesystemimage-createfileitem) and [**IFileSystemImage::CreateDirectoryItem**](/windows/desktop/api/imapi2fs/nf-imapi2fs-ifilesystemimage-createdirectoryitem) methods to create new file and directory objects, respectively. The file and directory objects provide specific details about the files and directories. Alternatively, the [**IFsiDirectoryItem::AddTree**](/windows/desktop/api/imapi2fs/nf-imapi2fs-ifsidirectoryitem-addtree) method of a directory object, represented via the [**IFsiDirectoryItem**](/windows/desktop/api/imapi2fs/nn-imapi2fs-ifsidirectoryitem) interface, can be used to add existing files and directories from another storage device (i.e. a hard drive).

The event handler update method available for [**IFileSystemImage**](/windows/desktop/api/imapi2fs/nn-imapi2fs-ifilesystemimage) identifies the current file being added to the file system image, the number of sectors already copied, and the total number of sectors to be copied.

To remove existing files and directories from the file system, use the [**IFsiDirectoryItem::Remove**](/windows/desktop/api/imapi2fs/nf-imapi2fs-ifsidirectoryitem-remove) and [**IFsiDirectoryItem::RemoveTree**](/windows/desktop/api/imapi2fs/nf-imapi2fs-ifsidirectoryitem-removetree) methods of the directory objects represented via the [**IFsiDirectoryItem**](/windows/desktop/api/imapi2fs/nn-imapi2fs-ifsidirectoryitem) interface. The [**IFileSystemImage::get\_Root**](/windows/desktop/api/imapi2fs/nf-imapi2fs-ifilesystemimage-get_root) property is used to get a pointer to the root directory of the file system and the **IFsiDirectoryItem** interface to traverse through the directory tree.

> [!Note]  
> Files and directories removed via the [**IFsiDirectoryItem::Remove**](/windows/desktop/api/imapi2fs/nf-imapi2fs-ifsidirectoryitem-remove) and [**IFsiDirectoryItem::RemoveTree**](/windows/desktop/api/imapi2fs/nf-imapi2fs-ifsidirectoryitem-removetree) methods are not physically removed from the disc, and advanced software can easily recover the deleted information.

 


```VB
    ' Add the directory and its contents to the file system 
    WScript.Echo "Adding " & Path & " directory to the disc..."
    FSI.Root.AddTree Path, false
```



## Constructing a File System Image

The final step is to call [**IFileSystemImage::CreateResultImage**](/windows/desktop/api/imapi2fs/nf-imapi2fs-ifilesystemimage-createresultimage) to create a data stream for the burn image and provide access to it through the [**IFileSystemImageResult**](/windows/desktop/api/imapi2fs/nn-imapi2fs-ifilesystemimageresult) interface. This data stream can either be provided directly to the [**IDiscFormat2Data::Write**](/windows/desktop/api/imapi2/nf-imapi2-idiscformat2data-write) method or be saved to a file for later use.


```VB
    ' Create an image from the file system image object
    Dim Result
    Set Result = FSI.CreateResultImage()
    Stream = Result.ImageStream
```



## Example Summary

The following Visual Basic script example shows how to use IMAPI objects to create multisession discs. The example creates a new session and adds a directory to the disc. For the sake of simplicity, the code does not perform extensive error checking, and assumes the following:

-   A compatible disc device is installed on the system.
-   The disc device is the first drive on the system.
-   A compatible disc is inserted in the disc device.
-   Files to add to the disc are located in "g:\\burndir".

Additional functionality such as extensive error checking, device and media compatibility, event notification, and calculation of free space on the disc can be added to the script.


```VB
' This script adds data files from a single directory tree to a
' disc (a new session is added, if the disc already contains data)

' Copyright (C) Microsoft. All rights reserved.

Option Explicit

' *** CD/DVD disc file system types
Const FsiFileSystemISO9660 = 1
Const FsiFileSystemJoliet  = 2
Const FsiFileSystemUDF102  = 4

WScript.Quit(Main)

Function Main
    Dim Index                ' Index to recording drive.
    Dim Recorder             ' Recorder object
    Dim Path                 ' Directory of files to add
    Dim Stream               ' Data stream for burning device
    
    Index = 0                ' First drive on the system
    Path = "G:\BurnDir"      ' Files to add to the disc

    ' Create a DiscMaster2 object to connect to optical drives.
    Dim DiscMaster
    Set DiscMaster = WScript.CreateObject("IMAPI2.MsftDiscMaster2")

    ' Create a DiscRecorder2 object for the specified burning device.
    Dim UniqueId
    set Recorder = WScript.CreateObject("IMAPI2.MsftDiscRecorder2")
    UniqueId = DiscMaster.Item(Index)
    Recorder.InitializeDiscRecorder(UniqueId)

    ' Create a DiscFormat2Data object and set the recorder
    Dim DataWriter
    Set DataWriter = CreateObject ("IMAPI2.MsftDiscFormat2Data")
    DataWriter.Recorder = Recorder
    DataWriter.ClientName = "IMAPIv2 TEST"

    ' Create a new file system image object
    Dim FSI
    Set FSI = CreateObject("IMAPI2FS.MsftFileSystemImage")

    ' Import the last session, if the disc is not empty, or initialize
    ' the file system, if the disc is empty
    If Not DataWriter.MediaHeuristicallyBlank _
    Then
        On Error Resume Next
        FSI.MultisessionInterfaces = DataWriter.MultisessionInterfaces
        If Err.Number <> 0 _
        Then
            WScript.Echo "Multisession is not supported for this disc"
            Main = 1
            Exit Function
        End If
        On Error Goto 0

        WScript.Echo "Importing data from the previous session..."
        FSI.ImportFileSystem()
    Else 
        FSI.ChooseImageDefaults(Recorder)
    End If

    ' Add the directory and its contents to the file system 
    WScript.Echo "Adding " & Path & " directory to the disc..."
    FSI.Root.AddTree Path, false

    ' Create an image from the file system image object
    Dim Result
    Set Result = FSI.CreateResultImage()
    Stream = Result.ImageStream
    
    ' Write stream to disc using the specified recorder
    WScript.Echo "Writing content to the disc..."
    DataWriter.Write(Stream)

    WScript.Echo "Finished writing content."
    Main = 0
End Function

```



## Related topics

<dl> <dt>

[Using IMAPI](using-imapi.md)
</dt> <dt>

[**IStream**](/windows/desktop/api/objidl/nn-objidl-istream)
</dt> <dt>

[**IDiscMaster2**](/windows/desktop/api/imapi2/nn-imapi2-idiscmaster2)
</dt> <dt>

[**IDiscFormat2Data**](/windows/desktop/api/imapi2/nn-imapi2-idiscformat2data)
</dt> <dt>

[**IFileSystemImage**](/windows/desktop/api/imapi2fs/nn-imapi2fs-ifilesystemimage)
</dt> </dl>

 

 
