---
description: This document presents common Shell data transfer scenarios and discusses how to implement each one in your application.
ms.assetid: 7fce555c-a93d-4414-9119-7ae9acdd4d89
title: Handling Shell Data Transfer Scenarios
ms.topic: article
ms.date: 05/31/2018
---

# Handling Shell Data Transfer Scenarios

The [Shell Data Object](dataobject.md) document discussed the general approach that is used to transfer Shell data with drag-and-drop or the Clipboard. However, to implement Shell data transfer in your application, you must also understand how to apply these general principles and techniques to the variety of ways that Shell data can be transferred. This document presents common Shell data transfer scenarios and discusses how to implement each one in your application.

- [General Guidelines](#general-guidelines)
- [Copying File Names from the Clipboard to an Application](#copying-file-names-from-the-clipboard-to-an-application)
    - [Extracting the File Names from the Data Object](#extracting-the-file-names-from-the-data-object)
- [Copying the Contents of a Dropped File into an Application](#copying-the-contents-of-a-dropped-file-into-an-application)
    - [Using the CFSTR\_FILECONTENTS Format to Extract Data from a File](/windows)
- [Handling Optimized Move Operations](#handling-optimized-move-operations)
- [Handling Delete-on-Paste Operations](#handling-delete-on-paste-operations)
- [Transfering Data to and from Virtual Folders](#transfering-data-to-and-from-virtual-folders)
    - [Accepting Data from a Virtual Folder](#accepting-data-from-a-virtual-folder)
    - [Transferring Data to and from a NameSpace Extension](#transferring-data-to-and-from-a-namespace-extension)
- [Dropping Files on the Recycle Bin](#dropping-files-on-the-recycle-bin)
- [Creating and Importing Scrap Files](#creating-and-importing-scrap-files)
    - [Round-trip Support](#round-trip-support)
    - [Cached Data Formats](#cached-data-formats)
    - [Delayed Rendering](#delayed-rendering)
- [Dragging and Dropping Shell Objects Asynchronously](#dragging-and-dropping-shell-objects-asynchronously)
    - [Using IASyncOperation/IDataObjectAsyncCapability](#using-iasyncoperationidataobjectasynccapability)

> [!Note]  
> Although each of these scenarios discusses a specific data transfer operation, many of them apply to a variety of related scenarios. For instance, the primary difference between most Clipboard and drag-and-drop transfers is in how the data object arrives at the target. Once the target has a pointer to the data object's [**IDataObject**](/windows/win32/api/objidl/nn-objidl-idataobject) interface, the procedures for extracting information are largely the same for both types of data transfer. However, some of the scenarios are limited to a specific type of operation. Refer to the individual scenario for details.

 

## General Guidelines

Each of the following sections discusses a single, fairly specific data transfer scenario. However, data transfers are often more complex and might involve aspects of several scenarios. You typically do not know, in advance, which scenario you will actually need to handle. Here are a few general guidelines to keep in mind.

For data sources:

- The Shell Clipboard formats, with the exception of [CF\_HDROP](clipboard.md), are not predefined. Each format you want to use must be registered by calling [RegisterClipboardFormat](/windows/win32/api/winuser/nf-winuser-registerclipboardformata).
- The formats in the data objects are provided in the order of preference from the source. Enumerate the data object and pick the first one you can consume.
- Include as many formats as you can support. You generally do not know where the data object will be dropped. This practice improves the odds that the data object will contain a format that the drop target can accept.
- Existing files should be offered with the [CF\_HDROP](clipboard.md) format.
- Offer file-like data with [CFSTR\_FILECONTENTS](clipboard.md)/[CFSTR\_FILEDESCRIPTOR](clipboard.md) formats. This approach allows the target to create a file from a data object without needing to know anything about the underlying data storage. You should normally present the data as an [**IStream**](/windows/win32/api/objidl/nn-objidl-istream) interface. This data transfer mechanism is more flexible than a global memory object and uses much less memory.
- Drag sources should offer the [CFSTR\_SHELLIDLIST](clipboard.md) format when dragging Shell items. Data objects for items can be acquired through either the [**IShellFolder::GetUIObjectOf**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-getuiobjectof) or [**IShellItem::BindToHandler**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellitem-bindtohandler) methods. Data sources can create a standard data object implementation that supports the [CFSTR\_SHELLIDLIST](clipboard.md) format by using [**SHCreateDataObject**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shcreatedataobject).
- Drop targets that want to reason about the items being dragged using the shell item programming model can convert an IDataObject into an [**IShellItemArray**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellitemarray) using [**SHCreateShellItemArrayFromDataObject**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-shcreateshellitemarrayfromdataobject).
- Use standard feedback cursors.
- Support left and right drag.
- Use the data object itself from an embedded object. This approach allows your application to retrieve any extra formats the data object has to offer and avoids creating an extra layer of containment. For instance, an embedded object from server A is dragged from server/container B and dropped on container C. C should create an embedded object of server A, not an embedded object of server B containing an embedded object of server A.
- Remember that the Shell might use [optimized moves](#handling-optimized-move-operations) or [delete-on-paste](#handling-delete-on-paste-operations) operations when moving files. Your application should be able to recognize these operations and respond appropriately.

For data targets:

- The Shell Clipboard formats, with the exception of [CF\_HDROP](clipboard.md), are not predefined. Each format you want to use must be registered by calling [RegisterClipboardFormat](/windows/win32/api/winuser/nf-winuser-registerclipboardformata).
- Implement and register an OLE drop target. Avoid using Windows 3.1 targets or the [**WM\_DROPFILES**](wm-dropfiles.md) message, if possible.
- The formats contained by a data object vary, depending on where the object comes from. Since you generally do not know in advance where a data object comes from, do not assume that a particular format will be present. The data object should enumerate the formats in order of quality, starting with the best. Thus, to get the best available format, applications normally enumerate the available formats and use the first format in the enumeration that they can support.
- Support right-drag. You can customize the drag shortcut menu by creating a [drag-and-drop handler](context-menu-handlers.md).
- If your application will accept existing files, it must be able to handle the [CF\_HDROP](clipboard.md) format.
- In general, applications that accept files should also handle the [CFSTR\_FILECONTENTS](clipboard.md)/[CFSTR\_FILEDESCRIPTOR](clipboard.md) formats. While files from the file system have the [CF\_HDROP](clipboard.md) format, files from providers such as namespace extensions generally use [CFSTR\_FILECONTENTS](clipboard.md)/[CFSTR\_FILEDESCRIPTOR](clipboard.md). Examples include Windows CE folders, File Transfer Protocol (FTP) folders, web folders, and CAB folders. The source normally implements an [**IStream**](/windows/win32/api/objidl/nn-objidl-istream) interface to present data from its storage as a file.
- Remember that the Shell might use [optimized moves](#handling-optimized-move-operations) or [delete-on-paste](#handling-delete-on-paste-operations) operations when moving files. Your application should be able to recognize these operations and respond appropriately.

## Copying File Names from the Clipboard to an Application

**Scenario:** A user selects one or more files in Windows Explorer and copies them to the Clipboard. Your application extracts the file names and pastes them into the document.

This scenario could be used, for instance, to allow a user to create an HTML link by cutting and pasting the file to your application. Your application can then extract the file name from the data object and process it to create an anchor tag.

When a user selects a file in Windows Explorer and copies it to the Clipboard, the Shell creates a data object. It then calls [**OleSetClipboard**](/windows/win32/api/ole2/nf-ole2-olesetclipboard) to place a pointer to the data object's [**IDataObject**](/windows/win32/api/objidl/nn-objidl-idataobject) interface on the Clipboard.

When the user selects the **Paste** command from your application's menu or toolbar:

1.  Call [**OleGetClipboard**](/windows/win32/api/ole2/nf-ole2-olegetclipboard) to retrieve the data object's [**IDataObject**](/windows/win32/api/objidl/nn-objidl-idataobject) interface.
2.  Call [**IDataObject::EnumFormatEtc**](/windows/win32/api/objidl/nf-objidl-idataobject-enumformatetc) to request an enumerator object.
3.  Use the enumerator object's [**IEnumFORMATETC**](/windows/win32/api/objidl/nn-objidl-ienumformatetc) interface to enumerate the formats contained by the data object.

> [!Note]  
> The final two steps in this procedure are included for completeness. They are typically not necessary for simple file transfers. All data objects used for this type of data transfer should contain the [CF\_HDROP](clipboard.md) format, which can be used to determine the names of the files contained by the object. However, for more general data transfers, you should enumerate the formats and select the best one that your application can handle.

 

### Extracting the File Names from the Data Object

The next step is to extract one or more file names from the data object and paste them into your application. Note that the procedure discussed in this section for extracting a file name from a data object applies equally well to drag-and-drop transfers.

The simplest way to retrieve file names from a data object is the [CF\_HDROP](clipboard.md) format:

1.  Call [**IDataObject::GetData**](/windows/win32/api/objidl/nf-objidl-idataobject-getdata). Set the **cfFormat** member of the [**FORMATETC**](/windows/win32/api/objidl/ns-objidl-formatetc) structure to [CF\_HDROP](clipboard.md) and the **tymed** member to [TYMED\_HGLOBAL](dataobject.md). The **dwAspect** member is normally set to DVASPECT\_CONTENT. However, if you need to have the file's path in short (8.3) format, set **dwAspect** to DVASPECT\_SHORT.

    When [**IDataObject::GetData**](/windows/win32/api/objidl/nf-objidl-idataobject-getdata) returns, the **hGlobal** member of the [**STGMEDIUM**](/windows/win32/api/objidl/ns-objidl-ustgmedium-r1) structure points to a global memory object that contains the data.

2.  Create an HDROP variable and set it to the **hGlobal** member of the [**STGMEDIUM**](/windows/win32/api/objidl/ns-objidl-ustgmedium-r1) structure. The HDROP variable is now a handle to a [**DROPFILES**](/windows/desktop/api/shlobj_core/ns-shlobj_core-dropfiles) structure followed by a double null-terminated string containing the fully qualified file paths of the copied files.
3.  Determine how many file paths are in the list by calling [**DragQueryFile**](/windows/desktop/api/Shellapi/nf-shellapi-dragqueryfilea) with the *iFile* parameter set to 0xFFFFFFFF. The function returns the number of file paths in the list. The file path's zero-based index in this list is used in the next step to identify a particular path.
4.  Extract the file paths from the global memory object by calling [**DragQueryFile**](/windows/desktop/api/Shellapi/nf-shellapi-dragqueryfilea) once for each file, with *iFile* set to the file's index.
5.  Process the file paths as needed and paste them into your application.
6.  Call [**ReleaseStgMedium**](/windows/win32/api/ole2/nf-ole2-releasestgmedium) and pass in the pointer to the [**STGMEDIUM**](/windows/win32/api/objidl/ns-objidl-ustgmedium-r1) structure that you passed to [**IDataObject::GetData**](/windows/win32/api/objidl/nf-objidl-idataobject-getdata) in step 1. Once you have released the structure, the HDROP value that you created in step 2 is no longer valid and should not be used.

## Copying the Contents of a Dropped File into an Application

**Scenario:** A user drags one or more files from Windows Explorer and drops them on your application's window. Your application extracts the content of the file (s) and pastes it into the application.

This scenario uses drag-and-drop to transfer the files from Windows Explorer to the application. Prior to the operation, your application must:

1.  Call [RegisterClipboardFormat](/windows/win32/api/winuser/nf-winuser-registerclipboardformata) to register any needed Shell Clipboard formats.
2.  Call [**RegisterDragDrop**](/windows/win32/api/ole2/nf-ole2-registerdragdrop) to register a target window and your application's [**IDropTarget**](/windows/win32/api/oleidl/nn-oleidl-idroptarget) interface.

After the user initiates the operation by selecting one or more files and starting to drag them:

1.  Windows Explorer creates a data object and loads the supported formats into it.
2.  Windows Explorer calls [**DoDragDrop**](/windows/win32/api/ole2/nf-ole2-dodragdrop) to initiate the drag loop.
3.  When the drag image reaches your target window, the system notifies you by calling [**IDropTarget::DragEnter**](/windows/win32/api/oleidl/nf-oleidl-idroptarget-dragenter).
4.  To determine what the data object contains, call the data object's [**IDataObject::EnumFormatEtc**](/windows/win32/api/objidl/nf-objidl-idataobject-enumformatetc) method. Use the enumerator object returned by the method to enumerate the formats contained by the data object. If your application does not want to accept any of these formats, return DROPEFFECT\_NONE. For the purposes of this scenario, your application should ignore any data objects that do not contain formats used to transfer files, such as [CF\_HDROP](clipboard.md).
5.  When the user drops the data, the system calls [**IDropTarget::Drop**](/windows/win32/api/oleidl/nf-oleidl-idroptarget-drop).
6.  Use the [**IDataObject**](/windows/win32/api/objidl/nn-objidl-idataobject) interface to extract the contents of the files.

There are several different ways to extract the contents of a Shell object from a data object. In general, use the following order:

- If the file contains a [CF\_TEXT](clipboard.md) format, the data is ANSI text. You can use the CF\_TEXT format to extract the data, rather than opening the file itself.
- If the file contains a linked or embedded OLE object, the data object contains a CF\_EMBEDDEDOBJECT format. Use standard OLE techniques to extract the data. [Scrap files](#creating-and-importing-scrap-files) always contain a CF\_EMBEDDEDOBJECT format.
- If the Shell object is from the file system, the data object contains a [CF\_HDROP](clipboard.md) format with the names of the files. Extract the file name from [CF\_HDROP](clipboard.md) and call [**OleCreateFromFile**](/windows/win32/api/ole2/nf-ole2-olecreatefromfile) to create a new linked or embedded object. For a discussion of how to retrieve a file name from a [CF\_HDROP](clipboard.md) format, see [Copying File Names from the Clipboard to an Application](#copying-file-names-from-the-clipboard-to-an-application).
- If the data object contains a [CFSTR\_FILEDESCRIPTOR](clipboard.md) format, you can extract a file's contents from the file's [CFSTR\_FILECONTENTS](clipboard.md) format. For a discussion of this procedure, see [Using the CFSTR\_FILECONTENTS Format to Extract Data from a File](/windows).
- Prior to Shell [version 4.71](versions.md), an application indicated that it was transferring a shortcut file type by setting **FD\_LINKUI** in the **dwFlags** member of the [**FILEDESCRIPTOR**](/windows/win32/api/shlobj_core/ns-shlobj_core-filedescriptora) structure. For later versions of the Shell, the preferred way to indicate that shortcuts are being transferred is to use the [CFSTR\_PREFERREDDROPEFFECT](clipboard.md) format set to DROPEFFECT\_LINK. This approach is much more efficient than extracting the **FILEDESCRIPTOR** structure just to check a flag.

If the data extraction process will be lengthy, you might want to do the operation asynchronously on a background thread. Your primary thread can then proceed without unnecessary delays. For a discussion of how to handle asynchronous data extraction, see [Dragging and Dropping Shell Objects Asynchronously](#dragging-and-dropping-shell-objects-asynchronously).

### Using the CFSTR\_FILECONTENTS Format to Extract Data from a File

The [CFSTR\_FILECONTENTS](clipboard.md) format provides a very flexible and powerful way to transfer the contents of a file. It is not even necessary for the data to be stored as a single file. All that is required for this format is that the data object present the data to the target as if it were a file. For instance, the actual data might be a section of a text document or a block of data extracted from a database. The target can treat the data as a file and does not need to know anything about the underlying storage mechanism.

Namespace extensions normally use [CFSTR\_FILECONTENTS](clipboard.md) to transfer data because this format does not assume any particular storage mechanism. A namespace extension can use whatever storage mechanism is convenient, and use this format to present its objects to applications as if they were files.

The data transfer mechanism for [CFSTR\_FILECONTENTS](clipboard.md) is normally [TYMED\_ISTREAM](dataobject.md). Transferring an [**IStream**](/windows/win32/api/objidl/nn-objidl-istream) interface pointer requires much less memory than loading the data into a global memory object, and **IStream** is a simpler way to represent data than [**IStorage**](/windows/win32/api/objidl/nn-objidl-istorage).

A [CFSTR\_FILECONTENTS](clipboard.md) format is always accompanied by a [CFSTR\_FILEDESCRIPTOR](clipboard.md) format. You must examine the contents of this format first. If more than one file is being transferred, the data object will actually contain multiple [CFSTR\_FILECONTENTS](clipboard.md) formats, one for each file. The [CFSTR\_FILEDESCRIPTOR](clipboard.md) format contains the name and attributes of each file, and provides an index value for each file that is needed to extract a particular file's [CFSTR\_FILECONTENTS](clipboard.md) format.

To extract a [CFSTR\_FILECONTENTS](clipboard.md) format:

1.  Extract the [CFSTR\_FILEDESCRIPTOR](clipboard.md) format as a [TYMED\_HGLOBAL](dataobject.md) value.
2.  The **hGlobal** member of the returned [**STGMEDIUM**](/windows/win32/api/objidl/ns-objidl-ustgmedium-r1) structure points to a global memory object. Lock that object by passing the **hGlobal** value to [**GlobalLock**](/windows/win32/api/winbase/nf-winbase-globallock).
3.  Cast the pointer returned by [**GlobalLock**](/windows/win32/api/winbase/nf-winbase-globallock) to a [**FILEGROUPDESCRIPTOR**](/windows/win32/api/shlobj_core/ns-shlobj_core-filegroupdescriptora) pointer. It will point to a **FILEGROUPDESCRIPTOR** structure followed by one or more [**FILEDESCRIPTOR**](/windows/win32/api/shlobj_core/ns-shlobj_core-filedescriptora) structures. Each **FILEDESCRIPTOR** structure contains a description of a file that is contained by one of the accompanying [CFSTR\_FILECONTENTS](clipboard.md) formats.
4.  Examine the [**FILEDESCRIPTOR**](/windows/win32/api/shlobj_core/ns-shlobj_core-filedescriptora) structures to determine which one corresponds to the file you want to extract. The zero-based index of that **FILEDESCRIPTOR** structure is used to identify the file's [CFSTR\_FILECONTENTS](clipboard.md) format. Because the size of a global memory block is not byte-precise, use the structure's **nFileSizeLow** and **nFileSizeHigh** members to determine how many bytes represent the file in the global memory object.
5.  Call [**IDataObject::GetData**](/windows/win32/api/objidl/nf-objidl-idataobject-getdata) with the **cfFormat** member of the [**FORMATETC**](/windows/win32/api/objidl/ns-objidl-formatetc) structure set to the [CFSTR\_FILECONTENTS](clipboard.md) value and the **lIndex** member set to the index that you determined in the previous step. The **tymed** member is typically set to [TYMED\_HGLOBAL](dataobject.md) \| TYMED\_ISTREAM \| TYMED\_ISTORAGE. The data object can then choose its preferred data transfer mechanism.
6.  The [**STGMEDIUM**](/windows/win32/api/objidl/ns-objidl-ustgmedium-r1) structure that [**IDataObject::GetData**](/windows/win32/api/objidl/nf-objidl-idataobject-getdata) returns will contain a pointer to the file's data. Examine the **tymed** member of the structure to determine the data transfer mechanism.
7.  If **tymed** is set to [TYMED\_ISTREAM](dataobject.md) or TYMED\_ISTORAGE, use the interface to extract the data. If **tymed** is set to TYMED\_HGLOBAL, the data is contained in a global memory object. For a discussion of how to extract data from a global memory object, see the *Extracting a global memory object from a data object* section of [Shell Data Object](dataobject.md).
8.  Call [**GlobalLock**](/windows/win32/api/winbase/nf-winbase-globallock) to unlock the global memory object that you locked in step 2.

## Handling Optimized Move Operations

**Scenario:** A file is moved from the file system to a namespace extension using an optimized move.

In a conventional move operation, the target makes a copy of the data and the source deletes the original. This procedure can be inefficient because it requires two copies of the data. With large objects such as databases, a conventional move operation might not even be practical.

With an optimized move, the target uses its understanding of how the data is stored to handle the entire move operation. There is never a second copy of the data, and there is no need for the source to delete the original data. Shell data is well suited to optimized moves because the target can handle the entire operation using the Shell API. A typical example is moving files. Once the target has the path of a file to be moved, it can use [**SHFileOperation**](/windows/desktop/api/Shellapi/nf-shellapi-shfileoperationa) to move it. There is no need for the source to delete the original file.

> [!Note]  
> The Shell normally uses an optimized move to move files. To handle Shell data transfer properly, your application must be capable of detecting and handling an optimized move.

 

Optimized moves are handled in the following way:

1.  The source calls [**DoDragDrop**](/windows/win32/api/ole2/nf-ole2-dodragdrop) with the *dwEffect* parameter set to DROPEFFECT\_MOVE to indicate that the source objects can be moved.
2.  The target receives the DROPEFFECT\_MOVE value through one of its [**IDropTarget**](/windows/win32/api/oleidl/nn-oleidl-idroptarget) methods, indicating that a move is allowed.
3.  The target either copies the object (unoptimized move) or moves the object (optimized move).
4.  The target then tells the source whether it needs to delete the original data.

    An optimized move is the default operation, with the data deleted by the target. To inform the source that an optimized move was performed:

    - - The target sets the *pdwEffect* value it received through its [**IDropTarget::Drop**](/windows/win32/api/oleidl/nf-oleidl-idroptarget-drop) method to some value other than DROPEFFECT\_MOVE. It is typically set to either DROPEFFECT\_NONE or DROPEFFECT\_COPY. The value will be returned to the source by [**DoDragDrop**](/windows/win32/api/ole2/nf-ole2-dodragdrop).
        - The target also calls the data object's [**IDataObject::SetData**](/windows/win32/api/objidl/nf-objidl-idataobject-setdata) method and passes it a [CFSTR\_PERFORMEDDROPEFFECT](clipboard.md) format identifier set to DROPEFFECT\_NONE. This method call is necessary because some drop targets might not set the *pdwEffect* parameter of [**DoDragDrop**](/windows/win32/api/ole2/nf-ole2-dodragdrop) properly. The [CFSTR\_PERFORMEDDROPEFFECT](clipboard.md) format is the reliable way to indicate that an optimized move has taken place.

    If the target did an unoptimized move, the data must be deleted by the source. To inform the source that an unoptimized move was performed:

    - - The target sets the *pdwEffect* value it received through its [**IDropTarget::Drop**](/windows/win32/api/oleidl/nf-oleidl-idroptarget-drop) method to DROPEFFECT\_MOVE. The value will be returned to the source by [**DoDragDrop**](/windows/win32/api/ole2/nf-ole2-dodragdrop).
        - The target also calls the data object's [**IDataObject::SetData**](/windows/win32/api/objidl/nf-objidl-idataobject-setdata) method and passes it a [CFSTR\_PERFORMEDDROPEFFECT](clipboard.md) format identifier set to DROPEFFECT\_MOVE. This method call is necessary because some drop targets might not set the *pdwEffect* parameter of [**DoDragDrop**](/windows/win32/api/ole2/nf-ole2-dodragdrop) properly. The [CFSTR\_PERFORMEDDROPEFFECT](clipboard.md) format is the reliable way to indicate that an unoptimized move has taken place.

5.  The source inspects the two values that can be returned by the target. If both are set to DROPEFFECT\_MOVE, it completes the unoptimized move by deleting the original data. Otherwise, the target did an optimized move and the original data has been deleted.

## Handling Delete-on-Paste Operations

**Scenario:** One or more files are cut from a folder in Windows Explorer and pasted into a namespace extension. Windows Explorer leaves the files highlighted until it receives feedback on the outcome of the paste operation.

Traditionally, when a user cuts data it immediately disappears from view. This might not be efficient, and it can lead to usability problems if the user becomes concerned about what has happened to the data. An alternative approach is to use a delete-on-paste operation.

With a delete-on-paste operation, the selected data is not immediately removed from view. Instead, the source application marks it as selected, perhaps by changing the font or background color. After the target application has pasted the data, it notifies the source about the outcome of the operation. If the target performed an [optimized move](#handling-optimized-move-operations), the source can simply update its display. If the target performed a normal move, the source must also delete its copy of the data. If the paste fails, the source application restores the selected data to its original appearance.

> [!Note]  
> The Shell normally uses delete-on-paste when a cut/paste operation is used to move files. Delete-on-paste operations with Shell objects normally use an [optimized move](#handling-optimized-move-operations) to move the files. To handle Shell data transfer properly, your application must be capable of detecting and handling delete-on-paste operations.

 

The essential requirement for delete-on-paste is that the target must report the outcome of the operation to the source. However, standard Clipboard techniques cannot be used to implement delete-on-paste because they do not provide a way for the target to communicate with the source. Instead, the target application uses the data object's [**IDataObject::SetData**](/windows/win32/api/objidl/nf-objidl-idataobject-setdata) method to report the outcome to the data object. The data object can then communicate with the source through a private interface.

The basic procedure for a delete-on-paste operation is as follows:

1.  The source marks the screen display of the selected data.
2.  The source creates a data object. It indicates a cut operation by adding the [CFSTR\_PREFERREDDROPEFFECT](clipboard.md) format with a data value of DROPEFFECT\_MOVE.
3.  The source places the data object on the Clipboard using [**OleSetClipboard**](/windows/win32/api/ole2/nf-ole2-olesetclipboard).
4.  The target retrieves the data object from the Clipboard using [**OleGetClipboard**](/windows/win32/api/ole2/nf-ole2-olegetclipboard).
5.  The target extracts the [CFSTR\_PREFERREDDROPEFFECT](clipboard.md) data. If it is set to only DROPEFFECT\_MOVE, the target can either do an optimized move or simply copy the data.
6.  If the target does not do an optimized move, it calls the [**IDataObject::SetData**](/windows/win32/api/objidl/nf-objidl-idataobject-setdata) method with the [CFSTR\_PERFORMEDDROPEFFECT](clipboard.md) format set to DROPEFFECT\_MOVE.
7.  When the paste is complete, the target calls the [**IDataObject::SetData**](/windows/win32/api/objidl/nf-objidl-idataobject-setdata) method with the [CFSTR\_PASTESUCCEEDED](clipboard.md) format set to DROPEFFECT\_MOVE.
8.  When the source's [**IDataObject::SetData**](/windows/win32/api/objidl/nf-objidl-idataobject-setdata) method is called with the [CFSTR\_PASTESUCCEEDED](clipboard.md) format set to DROPEFFECT\_MOVE, it must check to see if it also received the [CFSTR\_PERFORMEDDROPEFFECT](clipboard.md) format set to DROPEFFECT\_MOVE. If both formats are sent by the target, the source will have to delete the data. If only the [CFSTR\_PASTESUCCEEDED](clipboard.md) format is received, the source can simply remove the data from its display. If the transfer fails, the source updates the display to its original appearance.

## Transfering Data to and from Virtual Folders

**Scenario:** A user drags an object from or drops it on a virtual folder.

Virtual folders contain objects that are generally not part of the file system. Some virtual folders, such as the Recycle Bin, can represent data that is stored on the hard disk but not as ordinary file system objects. Some can represent stored data that is on a remote system, such as a handheld PC, or an FTP site. Others, such as the Printers folder, contain objects that do not represent stored data at all. While some virtual folders are part of the system, developers can also create and install custom virtual folders by implementing a namespace extension.

Regardless of the type of data or how it is stored, the folder and file objects that are contained by a virtual folder are presented by the Shell as if they were normal files and folders. It is the responsibility of the virtual folder to take whatever data it contains and present it to the Shell appropriately. This requirement means that virtual folders normally support drag-and-drop and Clipboard data transfers.

There are thus two groups of developers who need to be concerned with data transfer to and from virtual folders:

- Developers whose applications need to accept data that is transferred from a virtual folder.
- Developers whose namespace extensions need to properly support data transfer.

### Accepting Data from a Virtual Folder

Virtual folders can represent virtually any type of data and can store that data in any way they choose. Some virtual folders might actually contain normal file system files and folders. Others might, for instance, pack all their objects into a single document or database.

When a file system object is transferred to an application, the data object normally contains a [CF\_HDROP](clipboard.md) format with the object's fully qualified path. Your application can extract this string and use the normal file system functions to open the file and extract its data. However, because virtual folders typically do not contain normal file system objects, they generally do not use [CF\_HDROP](clipboard.md).

Instead of [CF\_HDROP](clipboard.md), data is normally transferred from virtual folders with the [CFSTR\_FILEDESCRIPTOR](clipboard.md)/[CFSTR\_FILECONTENTS](clipboard.md) formats. The [CFSTR\_FILECONTENTS](clipboard.md) format has two advantages over [CF\_HDROP](clipboard.md):

- No particular method of data storage is assumed.
- The format is more flexible. It supports three data transfer mechanisms: a global memory object, an [**IStream**](/windows/win32/api/objidl/nn-objidl-istream) interface, or an [**IStorage**](/windows/win32/api/objidl/nn-objidl-istorage) interface.

Global memory objects are rarely used to transfer data to or from virtual objects because the data must be copied into memory in its entirety. Transferring an interface pointer requires almost no memory and is much more efficient. With very large files, an interface pointer might be the only practical data transfer mechanism. Typically, data is represented by an [**IStream**](/windows/win32/api/objidl/nn-objidl-istream) pointer, because that interface is somewhat more flexible than [**IStorage**](/windows/win32/api/objidl/nn-objidl-istorage). The target extracts the pointer from the data object and uses the interface methods to extract the data.

For further discussion of how to handle the [CFSTR\_FILEDESCRIPTOR](clipboard.md)/[CFSTR\_FILECONTENTS](clipboard.md) formats, see [Using the CFSTR\_FILECONTENTS Format to Extract Data from a File](/windows).

### Transferring Data to and from a NameSpace Extension

When you implement a namespace extension, you will normally want to support drag-and-drop capabilities. Follow the recommendations for drop sources and targets discussed in [General Guidelines](#general-guidelines). In particular, a namespace extension must:

- Be able to handle the [CFSTR\_FILEDESCRIPTOR](clipboard.md)/[CFSTR\_FILECONTENTS](clipboard.md) formats. These two formats are normally used to transfer objects to and from namespace extensions.
- Be able to handle [optimized moves](#handling-optimized-move-operations). The Shell expects that Shell objects will be moved with an optimized move.
- Be able to handle a [delete-on-paste](#handling-delete-on-paste-operations) operation. The Shell uses delete-on-paste when objects are moved from the Shell with a cut/paste operation.
- Be able to handle data transfer through an [**IStream**](/windows/win32/api/objidl/nn-objidl-istream) or [**IStorage**](/windows/win32/api/objidl/nn-objidl-istorage) interface. Data transfer to or from a virtual folder is normally handled by transferring one of these two interface pointers, typically an **IStream** pointer. The target then calls the interface methods to extract the data:
    - - As a drop source, the namespace extension must extract the data from storage and pass it through this interface to the target.
        - As a drop target, a namespace extension must accept data from a source through this interface and store it properly.

## Dropping Files on the Recycle Bin

**Scenario:** The user drops a file on the **Recycle Bin**. Your application or namespace extension deletes the original file.

The Recycle Bin is a virtual folder that is used as a repository for files that are no longer needed. As long as the Recycle Bin has not been emptied, the user can later recover the file and return it to the file system.

For the most part, transferring Shell objects to the Recycle Bin works much like any other folder. However, when a user drops a file on the **Recycle Bin**, the source needs to delete the original, even if the feedback from the folder indicates a copy operation. Normally, a drop source has no way of knowing which folder its data object has been dropped on. However, for Windows 2000 and later systems, when a data object is dropped on the **Recycle Bin**, the Shell will call the data object's [**IDataObject::SetData**](/windows/win32/api/objidl/nf-objidl-idataobject-setdata) method with a [CFSTR\_TARGETCLSID](clipboard.md) format set to the Recycle Bin's class identifier (CLSID) (CLSID\_RecycleBin). To handle the Recycle Bin case properly, your data object should be able to recognize this format and communicate the information to the source through a private interface.

> [!Note]  
> When [**IDataObject::SetData**](/windows/win32/api/objidl/nf-objidl-idataobject-setdata) is called with a [CFSTR\_TARGETCLSID](clipboard.md) format set to CLSID\_RecycleBin, the data source should close any open handles to the objects that are being transferred before returning from the method. Otherwise, you might create sharing violations.

 

## Creating and Importing Scrap Files

**Scenario:** A user drags some data from an OLE application's data file and drops it on the desktop or Windows Explorer.

Windows allows users to drag an object from an OLE application's data file and drop it on the desktop or a file system folder. This operation creates a *scrap file*, which contains the data or a link to the data. The file name is taken from the short name registered for the CLSID of the object and the [CF\_TEXT](clipboard.md) data. For the Shell to create a scrap file containing data, the application's [**IDataObject**](/windows/win32/api/objidl/nn-objidl-idataobject) interface must support the CF\_EMBEDSOURCE Clipboard format. To create a file containing a link, **IDataObject** must support the CF\_LINKSOURCE format.

There are also three optional features that an application can implement to support scrap files:

- Round-trip support
- Cached data formats
- Delayed rendering

### Round-trip Support

A *round trip* involves transferring a data object to another container and then back to the original document. For instance, a user could transfer a group of cells from a spreadsheet to the desktop, creating a scrap file with the data. If the user then transfers the scrap back to the spreadsheet, the data needs to be integrated into the document as it was before the original transfer.

When the Shell creates the scrap file, it represents the data as an embedding object. When the scrap is transferred to another container, it is transferred as an embedding object, even if it is being returned to the original document. Your application is responsible for determining the data format contained in the scrap and putting the data back into its native format if necessary.

To establish the format of the embedded object, determine its CLSID by retrieving the object's CF\_OBJECTDESCRIPTOR format. If the CLSID indicates a data format that belongs to the application, it should transfer the native data instead of calling [**OleCreateFromData**](/windows/win32/api/ole2/nf-ole2-olecreatefromdata).

### Cached Data Formats

When the Shell creates a scrap file, it checks the registry for the list of available formats. By default, there are two formats available: CF\_EMBEDSOURCE and CF\_LINKSOURCE. However, there are a number of scenarios where applications might need to have scrap files in different formats:

- To allow scraps to be transferred to non-OLE containers, which cannot accepted embedded object formats.
- To allow suites of applications to communicate with a private format.
- To make round trips easier to handle.

Applications can add formats to the scrap by caching them in the registry. There are two types of cached formats:

- Priority cache formats. For these formats, the data is copied in its entirety into the scrap from the data object.
- Delay-rendered formats. For these formats, the data object is not copied to the scrap. Instead, rendering is delayed until a target requests the data. Delay-rendering is discussed in more detail in the next section.

To add a priority cache or delay-rendered format, create a **DataFormat** subkey under the **CLSID** key of the application that is the source of the data. Under that subkey, create a **PriorityCacheFormats** or **DelayRenderFormats** subkey. For each priority cache or delay-rendered format, create a numbered subkey starting with zero. Set the value of this key to either a string with the registered name of the format or a \#X value, where X represents the format number of a standard Clipboard format.

The following sample shows cached formats for two applications. The MyProg1 application has the rich-text format as a priority cache format, and a private format "My Format" as a delay-rendered format. The MyProg2 application has the CF\_BITMAP format (\#8") as a priority cache format.

```
HKEY_CLASSES_ROOT
   CLSID
      {GUID}
         (Default) = MyProg1
         DataFormats
            PriorityCacheFormats
               0
                  (Default) = Rich Text Format
            DelayRenderFormats
               0
                  (Default) = My Format
      {GUID}
         (Default) = MyProg2
         DataFormats
            PriorityCacheFormats
               0
                  (Default) = #8
```

Additional formats can be added by creating additional numbered subkeys.

### Delayed Rendering

A delayed rendering format allows an application to create a scrap file but delay the expense of rendering the data until it is requested by a target. The [**IDataObject**](/windows/win32/api/objidl/nn-objidl-idataobject) interface of a scrap will offer the delayed rendering formats to the target along with native and cached data. If the target requests a delayed rendering format, the Shell will run the application and provide the data to the target from the active object.

> [!Note]  
> Because delayed rendering is somewhat risky, it should be used with caution. It will not work if the server is not available, or on applications that are not OLE-enabled.

 

## Dragging and Dropping Shell Objects Asynchronously

**Scenario:** A user transfers a large block of data from source to target. To avoid blocking both applications for a significant amount of time, the target extracts the data asynchronously.

Normally, drag-and-drop is a synchronous operation. In brief:

1.  The drop source calls [**DoDragDrop**](/windows/win32/api/ole2/nf-ole2-dodragdrop) and blocks its primary thread until the function returns. Blocking the primary thread normally blocks UI processing.
2.  After the target's [**IDropTarget::Drop**](/windows/win32/api/oleidl/nf-oleidl-idroptarget-drop) method is called, the target extracts the data from the data object on its primary thread. This procedure normally blocks the target's UI processing for the duration of the extraction process.
3.  Once the data has been extracted, the target returns the [**IDropTarget::Drop**](/windows/win32/api/oleidl/nf-oleidl-idroptarget-drop) call, the system returns [**DoDragDrop**](/windows/win32/api/ole2/nf-ole2-dodragdrop), and both threads can proceed.

In short, synchronous data transfer can block the primary threads of both applications for a significant amount of time. In particular, both threads must wait while the target extracts the data. For small amounts of data, the time required to extract data is small and synchronous data transfer works quite well. However, synchronously extracting large amounts of data can cause lengthy delays and interfere with the UI of both target and source.

The [**IAsyncOperation**](/previous-versions//bb776309(v=vs.85))/[**IDataObjectAsyncCapability**](/windows/desktop/api/Shldisp/nn-shldisp-idataobjectasynccapability) interface is an optional interface that can be implemented by a data object. It gives the drop target the ability to extract data from the data object asynchronously on a background thread. Once data extraction is handed off to the background thread, the primary threads of both applications are free to proceed.

### Using IASyncOperation/IDataObjectAsyncCapability

> [!Note]  
> The interface was originally named [**IAsyncOperation**](/previous-versions//bb776309(v=vs.85)), but this was later changed to [**IDataObjectAsyncCapability**](/windows/desktop/api/Shldisp/nn-shldisp-idataobjectasynccapability). Otherwise, the two interfaces are identical.

 

The purpose of [**IAsyncOperation**](/previous-versions//bb776309(v=vs.85))/[**IDataObjectAsyncCapability**](/windows/desktop/api/Shldisp/nn-shldisp-idataobjectasynccapability) is to allow the drop source and drop target to negotiate whether data can be extracted asynchronously. The following procedure outlines how the drop source uses the interface:

1.  Create a data object that exposes [**IAsyncOperation**](/previous-versions//bb776309(v=vs.85))/[**IDataObjectAsyncCapability**](/windows/desktop/api/Shldisp/nn-shldisp-idataobjectasynccapability).
2.  Call [**SetAsyncMode**](/windows/desktop/api/Shldisp/nf-shldisp-idataobjectasynccapability-setasyncmode) with *fDoOpAsync* set to **VARIANT\_TRUE** to indicate that an asynchronous operation is supported.
3.  After [**DoDragDrop**](/windows/win32/api/ole2/nf-ole2-dodragdrop) returns, call [**InOperation**](/windows/desktop/api/Shldisp/nf-shldisp-idataobjectasynccapability-inoperation):
    - If [**InOperation**](/windows/desktop/api/Shldisp/nf-shldisp-idataobjectasynccapability-inoperation) fails or returns **VARIANT\_FALSE**, a normal synchronous data transfer has taken place and the data extraction process is finished. The source should do any cleanup that is required, and proceed.
    - If [**InOperation**](/windows/desktop/api/Shldisp/nf-shldisp-idataobjectasynccapability-inoperation) returns **VARIANT\_TRUE**, the data is being extracted asynchronously. Cleanup operations should be handled by [**EndOperation**](/windows/desktop/api/Shldisp/nf-shldisp-idataobjectasynccapability-endoperation).
4.  Release the data object.
5.  When the asynchronous data transfer is complete, the data object normally notifies the source through a private interface.

The following procedure outlines how the drop target uses the [**IAsyncOperation**](/previous-versions//bb776309(v=vs.85))/[**IDataObjectAsyncCapability**](/windows/desktop/api/Shldisp/nn-shldisp-idataobjectasynccapability) interface to extract data asynchronously:

1.  When the system calls [**IDropTarget::Drop**](/windows/win32/api/oleidl/nf-oleidl-idroptarget-drop), call [**IDataObject::QueryInterface**](/windows/win32/api/unknwn/nf-unknwn-iunknown-queryinterface(q)) and request an [**IAsyncOperation**](/previous-versions//bb776309(v=vs.85))/[**IDataObjectAsyncCapability**](/windows/desktop/api/Shldisp/nn-shldisp-idataobjectasynccapability) interface (IID\_IAsyncOperation/IID\_IDataObjectAsyncCapability) from the data object.
2.  Call [**GetAsyncMode**](/windows/desktop/api/Shldisp/nf-shldisp-idataobjectasynccapability-getasyncmode). If the method returns **VARIANT\_TRUE**, the data object supports asynchronous data extraction.
3.  Create a separate thread to handle data extraction and call [**StartOperation**](/windows/desktop/api/Shldisp/nf-shldisp-idataobjectasynccapability-startoperation).
4.  Return the [**IDropTarget::Drop**](/windows/win32/api/oleidl/nf-oleidl-idroptarget-drop) call, as you would for a normal data transfer operation. [**DoDragDrop**](/windows/win32/api/ole2/nf-ole2-dodragdrop) will return and unblock the drop source. Do not call [**IDataObject::SetData**](/windows/win32/api/objidl/nf-objidl-idataobject-setdata) to indicate the outcome of an optimized move or delete-on-paste operation. Wait until the operation is finished.
5.  Extract the data on the background thread. The target's primary thread is unblocked and free to proceed.
6.  If the data transfer was an [optimized move](#handling-optimized-move-operations) or [delete-on-paste](#handling-delete-on-paste-operations) operation, call [**IDataObject::SetData**](/windows/win32/api/objidl/nf-objidl-idataobject-setdata) to indicate the outcome.
7.  Notify the data object that extraction is finished by calling [**EndOperation**](/windows/desktop/api/Shldisp/nf-shldisp-idataobjectasynccapability-endoperation).

 

 
