---
description: You create an enhanced metafile by using the CreateEnhMetaFile function, supplying the appropriate arguments.
ms.assetid: b012e50e-a7f5-4687-9833-38dacc113d77
title: Enhanced Metafile Creation
ms.topic: article
ms.date: 05/31/2018
---

# Enhanced Metafile Creation

You create an enhanced metafile by using the [**CreateEnhMetaFile**](/windows/desktop/api/Wingdi/nf-wingdi-createenhmetafilea) function, supplying the appropriate arguments. The system uses these arguments to maintain picture dimensions, determine whether the metafile should be stored on a disk or in memory, and so on.

To maintain picture dimensions across output devices, [**CreateEnhMetaFile**](/windows/desktop/api/Wingdi/nf-wingdi-createenhmetafilea) requires the resolution of the reference device. This *reference device* is the device on which the picture first appeared, and the *reference DC* is the *device context* associated with the reference device. When calling the **CreateEnhMetaFile** function, you must supply a handle that identifies this DC. You can get this handle by calling the [**GetDC**](/windows/desktop/api/Winuser/nf-winuser-getdc) or [**CreateDC**](/windows/desktop/api/Wingdi/nf-wingdi-createdca) function. You can also specify **NULL** as the handle to use the current display device for the reference device.

Most applications store pictures permanently and therefore create an enhanced metafile that is stored on a disk; however, there are some instances when this is not necessary. For example, a word-processing application that provides chart-drawing capabilities could store a user-defined chart in memory as an enhanced metafile and then copy the enhanced metafile bits from memory into the user's document file. An application that requires a metafile that is stored permanently on a disk must supply the file name when it calls [**CreateEnhMetaFile**](/windows/desktop/api/Wingdi/nf-wingdi-createenhmetafilea). If you do not supply a file name, the system automatically treats the metafile as a temporary file and stores it in memory.

You can add an optional text description to a metafile containing information about the picture and the author. An application can display these strings in the File Open dialog box to provide the user with information about metafile content that will help in selecting the appropriate file. If an application includes the text description, it must supply a pointer to the string when it calls [**CreateEnhMetaFile**](/windows/desktop/api/Wingdi/nf-wingdi-createenhmetafilea).

When [**CreateEnhMetaFile**](/windows/desktop/api/Wingdi/nf-wingdi-createenhmetafilea) succeeds, it returns a handle that identifies a special metafile device context. A metafile device context is unique in that it is associated with a file rather than with an output device. When the system processes a GDI function that received a handle to a metafile device context, it converts the GDI function into an enhanced-metafile record and appends the record to the end of the enhanced metafile.

After a picture is complete and the last record is appended to the enhanced metafile, the application can close the file by calling the [**CloseEnhMetaFile**](/windows/desktop/api/Wingdi/nf-wingdi-closeenhmetafile) function. This function closes and deletes the special metafile device context and returns a handle identifying the enhanced metafile.

To delete an enhanced-format metafile or an enhanced-format metafile handle, call the [**DeleteEnhMetaFile**](/windows/desktop/api/Wingdi/nf-wingdi-deleteenhmetafile) function.

 

 



