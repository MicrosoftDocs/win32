---
title: StoClien Operations
description: The StoClien sample demonstrates how the client uses structured storage. The following summarizes the StoClien operations.
ms.assetid: 55498665-520b-4a83-a3d1-22d3ed15863e
keywords:
- StoClien Operations
ms.topic: article
ms.date: 05/31/2018
---

# StoClien Operations

The [StoClien](structured-storage-client-sample--stoclien-.md) sample demonstrates how the client uses structured storage. The following summarizes the StoClien operations.

The [StoClien](structured-storage-client-sample--stoclien-.md) application window client area is used for visual display of freeform drawing created with a mouse or tablet device. To draw with the mouse, press and hold the left mouse button while moving the mouse. Releasing the left mouse button ends the drawing of a line.

Here is a summary of operations from the standpoint of Stoclien.exe as a COM client of the Stoserve.dll COM server:

<dl> <dt>

<span id="File_Open"></span><span id="file_open"></span><span id="FILE_OPEN"></span>File/Open
</dt> <dd>

Shows the Open dialog box to obtain a name and path for an existing paper drawing file to open. A default .PAP file name extension for these files is assumed. If changes were made to the existing drawing when this menu item is chosen, a separate dialog will first be shown asking the user if the current drawing should be saved into its associated compound file.

</dd> <dt>

<span id="File_Save"></span><span id="file_save"></span><span id="FILE_SAVE"></span>File/Save
</dt> <dd>

Saves the current drawing into its associated compound file.

</dd> <dt>

<span id="File_Save_As"></span><span id="file_save_as"></span><span id="FILE_SAVE_AS"></span>File/Save As
</dt> <dd>

Shows the Save As dialog box to obtain a name and path for a new paper drawing file to create. The current drawing becomes the saved content of the new file, and the new file becomes the new associated compound file for the drawing.

</dd> <dt>

<span id="File_Exit"></span><span id="file_exit"></span><span id="FILE_EXIT"></span>File/Exit
</dt> <dd>

Exits [StoClien](structured-storage-client-sample--stoclien-.md).

</dd> <dt>

<span id="Draw_Drawing_On"></span><span id="draw_drawing_on"></span><span id="DRAW_DRAWING_ON"></span>Draw/Drawing On
</dt> <dd>

Turns on drawing between the [StoClien](structured-storage-client-sample--stoclien-.md) client and the COPaper object in the server. This command locks the COPaper object for exclusive use by this client and prevents other clients from accessing the same COPaper instance in the server.

</dd> <dt>

<span id="Draw_Drawing_Off"></span><span id="draw_drawing_off"></span><span id="DRAW_DRAWING_OFF"></span>Draw/Drawing Off
</dt> <dd>

Turns off drawing between the [StoClien](structured-storage-client-sample--stoclien-.md) client and the COPaper object in the server. This command unlocks the COPaper for exclusive use by this client and allows other clients to access the same COPaper instance in the server.

</dd> <dt>

<span id="Draw_Redraw"></span><span id="draw_redraw"></span><span id="DRAW_REDRAW"></span>Draw/Redraw
</dt> <dd>

Redraws in the client the current drawing data held in the COPaper object in the server.

</dd> <dt>

<span id="Draw_Erase"></span><span id="draw_erase"></span><span id="DRAW_ERASE"></span>Draw/Erase
</dt> <dd>

Erases the current drawing content and clears the window image. Menu Selection: Pen/Color Shows the Choose Color dialog box to obtain a new pen color for drawing.

</dd> <dt>

<span id="Pen_Medium"></span><span id="pen_medium"></span><span id="PEN_MEDIUM"></span>Pen/Medium
</dt> <dd>

Chooses the medium width for drawing. A check mark on this menu choice indicates that medium is the current pen width.

</dd> <dt>

<span id="Pen_Thick"></span><span id="pen_thick"></span><span id="PEN_THICK"></span>Pen/Thick
</dt> <dd>

Chooses the thick width for drawing. A check mark on this menu choice indicates that thick is the current pen width.

</dd> <dt>

<span id="Pen_Thin"></span><span id="pen_thin"></span><span id="PEN_THIN"></span>Pen/Thin
</dt> <dd>

Chooses the thin width for drawing. A check mark on this menu choice indicates that thin is the current pen width.

</dd> <dt>

<span id="Sink_Connect"></span><span id="sink_connect"></span><span id="SINK_CONNECT"></span>Sink/Connect
</dt> <dd>

Connects the COPaperSink IPaperSink interface to the COPaper object PaperSink connection point. Repainting of the current drawing image in [StoClien](structured-storage-client-sample--stoclien-.md) relies on the sink connection. A check mark on this menu choice indicates that repainting is connected.

</dd> <dt>

<span id="Sink_Disconnect"></span><span id="sink_disconnect"></span><span id="SINK_DISCONNECT"></span>Sink/Disconnect
</dt> <dd>

Disconnects the COPaperSink IPaperSink interface from the COPaper object PaperSink connection point. Repainting of the current drawing image in [StoClien](structured-storage-client-sample--stoclien-.md) relies on the sink connection. A check mark on this menu choice indicates that repainting is disconnected.

</dd> <dt>

<span id="Help_StoClien_Tutorial"></span><span id="help_stoclien_tutorial"></span><span id="HELP_STOCLIEN_TUTORIAL"></span>Help/StoClien Tutorial
</dt> <dd>

Opens the STOCLIEN.HTM tutorial file in the Web browser.

</dd> <dt>

<span id="Help_StoServe_Tutorial"></span><span id="help_stoserve_tutorial"></span><span id="HELP_STOSERVE_TUTORIAL"></span>Help/StoServe Tutorial
</dt> <dd>

Opens the STOSERVE.HTM tutorial file in the Web browser.

</dd> <dt>

<span id="Help_Read_Source_File"></span><span id="help_read_source_file"></span><span id="HELP_READ_SOURCE_FILE"></span>Help/Read Source File
</dt> <dd>

Displays the Open dialog box so you can open a source file from this lesson or another one in the Windows Notepad.

</dd> <dt>

<span id="Help_About_StoClien"></span><span id="help_about_stoclien"></span><span id="HELP_ABOUT_STOCLIEN"></span>Help/About StoClien
</dt> <dd>

Displays the About dialog box for this application.

</dd> </dl>

The [StoClien](structured-storage-client-sample--stoclien-.md) sample uses many of the utility classes and services provided by [APPUTIL](./using-visual-studio.md). For more information about [APPUTIL](./using-visual-studio.md), see the [APPUTIL](./using-visual-studio.md) library source code in the sibling [APPUTIL](./using-visual-studio.md) directory and Apputil.md in the main tutorial directory. For more information about [APPUTIL](./using-visual-studio.md), see [How to Build Samples](how-to-build-samples.md).

 

 