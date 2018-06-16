---
Description: Shell clipboard formats are used to identify the type of Shell data being transferred through the clipboard.
ms.assetid: fb8ce5d3-3215-4e05-a916-4d4a803464d2
title: Shell Clipboard Formats
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Shell Clipboard Formats

Shell clipboard formats are used to identify the type of Shell data being transferred through the clipboard. Most Shell clipboard formats identify a type of data, such as a list of file names or pointers to item identifier lists (PIDLs). However, some formats are used for communication between source and target. They can expedite the data transfer process by supporting Shell operations such as [optimized move](datascenarios.md) and [delete\_on\_paste](datascenarios.md). Shell data is always contained in a [data object](dataobject.md) that uses a [**FORMATETC**](https://msdn.microsoft.com/en-us/library/ms682177(v=VS.85).aspx) structure as a more general way to characterize data. The structure's **cfFormat** member is set to the clipboard format for the particular item of data. The other members provide additional information, such as the data transfer mechanism. The data is contained in an accompanying [**STGMEDIUM**](https://msdn.microsoft.com/en-us/library/ms683812(v=VS.85).aspx) structure.

> [!Note]  
> Standard clipboard format identifiers have the form CF\_*XXX*. A common example is CF\_TEXT, which is used for transferring ANSI text data. These identifiers have predefined values and can be used directly with [**FORMATETC**](https://msdn.microsoft.com/en-us/library/ms682177(v=VS.85).aspx) structures. With the exception of [CF\_HDROP](https://docs.microsoft.com/windows), Shell format identifiers are not predefined. With the exception of DragWindow, they have the form CFSTR\_*XXX*. To differentiate these values from predefined formats, they are often referred to as simply *formats*. However, unlike predefined formats, they must be registered by both source and target before they can be used to transfer data. To register a Shell format, include the Shlobj.h header file and pass the CFSTR\_*XXX* format identifier to [RegisterClipboardFormat](http://go.microsoft.com/fwlink/p/?linkid=215068). This function returns a valid clipboard format value, which can then be used as the **cfFormat** member of a **FORMATETC** structure.

 

The Shell clipboard formats are organized here into three groups, based on how they are used.

-   [Formats for Transferring File System Objects](#formats-for-transferring-file-system-objects)
    -   [CF\_HDROP](https://docs.microsoft.com/windows)
    -   [CFSTR\_FILECONTENTS](https://docs.microsoft.com/windows)
    -   [CFSTR\_FILEDESCRIPTOR](https://docs.microsoft.com/windows)
    -   [CFSTR\_FILENAME](https://docs.microsoft.com/windows)
    -   [CFSTR\_FILENAMEMAP](https://docs.microsoft.com/windows)
    -   [CFSTR\_MOUNTEDVOLUME](https://docs.microsoft.com/windows)
    -   [CFSTR\_SHELLIDLIST](https://docs.microsoft.com/windows)
    -   [CFSTR\_SHELLIDLISTOFFSET](https://docs.microsoft.com/windows)
-   [Formats for Transferring Virtual Objects](#formats-for-transferring-virtual-objects)
    -   [CFSTR\_NETRESOURCES](https://docs.microsoft.com/windows)
    -   [CFSTR\_PRINTERGROUP](https://docs.microsoft.com/windows)
    -   [CFSTR\_INETURL](https://docs.microsoft.com/windows)
    -   [CFSTR\_SHELLURL (deprecated)](https://docs.microsoft.com/windows)
-   [Formats for Communication Between Source and Target](#formats-for-communication-between-source-and-target)
    -   [CFSTR\_INDRAGLOOP](https://docs.microsoft.com/windows)
    -   [CFSTR\_LOGICALPERFORMEDDROPEFFECT](https://docs.microsoft.com/windows)
    -   [CFSTR\_PASTESUCCEEDED](https://docs.microsoft.com/windows)
    -   [CFSTR\_PERFORMEDDROPEFFECT](https://docs.microsoft.com/windows)
    -   [CFSTR\_PREFERREDDROPEFFECT](https://docs.microsoft.com/windows)
    -   [CFSTR\_TARGETCLSID](https://docs.microsoft.com/windows)
    -   [CFSTR\_UNTRUSTEDDRAGDROP](https://docs.microsoft.com/windows)
    -   [DragWindow](#dragwindow)

## Formats for Transferring File System Objects

These formats are used to transfer one or more files or other Shell objects.

-   [CF\_HDROP](https://docs.microsoft.com/windows)
-   [CFSTR\_FILECONTENTS](https://docs.microsoft.com/windows)
-   [CFSTR\_FILEDESCRIPTOR](https://docs.microsoft.com/windows)
-   [CFSTR\_FILENAME](https://docs.microsoft.com/windows)
-   [CFSTR\_FILENAMEMAP](https://docs.microsoft.com/windows)
-   [CFSTR\_MOUNTEDVOLUME](https://docs.microsoft.com/windows)
-   [CFSTR\_SHELLIDLIST](https://docs.microsoft.com/windows)
-   [CFSTR\_SHELLIDLISTOFFSET](https://docs.microsoft.com/windows)

### CF\_HDROP

This clipboard format is used when transferring the locations of a group of existing files. Unlike the other Shell formats, it is predefined, so there is no need to call [RegisterClipboardFormat](http://go.microsoft.com/fwlink/p/?linkid=215068). The data consists of an [**STGMEDIUM**](https://msdn.microsoft.com/en-us/library/ms683812(v=VS.85).aspx) structure that contains a global memory object. The structure's **hGlobal** member points to a [**DROPFILES**](/windows/desktop/api/shlobj_core/ns-shlobj_core-_dropfiles) structure as its **hGlobal** member.

The **pFiles** member of the [**DROPFILES**](/windows/desktop/api/shlobj_core/ns-shlobj_core-_dropfiles) structure contains an offset to a double **null**-terminated character array that contains the file names. If you are extracting a CF\_HDROP format from a data object, you can use [**DragQueryFile**](/windows/desktop/api/Shellapi/nf-shellapi-dragqueryfilea) to extract individual file names from the global memory object. If you are creating a CF\_HDROP format to place in a data object, you will need to construct the file name array.

The file name array consists of a series of strings, each containing one file's fully qualified path, including the terminating **NULL** character. An additional **null** character is appended to the final string to terminate the array. For example, if the files c:\\temp1.txt and c:\\temp2.txt are being transferred, the character array looks like this:


```C++
c:\temp1.txt'\0'c:\temp2.txt'\0''\0'
```



> [!Note]  
> In this example, '\\0' is used to represent the **null** character, not the literal characters that should be included.

 

If the object was copied to the clipboard as part of a drag-and-drop operation, the **pt** member of the [**DROPFILES**](/windows/desktop/api/shlobj_core/ns-shlobj_core-_dropfiles) structure contains the coordinates of the point where the object was dropped. You can use [**DragQueryPoint**](/windows/desktop/api/Shellapi/nf-shellapi-dragquerypoint) to extract the cursor coordinates.

If this format is present in a data object, an OLE drag loop simulates [**WM\_DROPFILES**](wm-dropfiles.md) functionality with non-OLE drop targets. This is important if your application is the source of a drag-and-drop operation on a Windows 3.1 system.

### CFSTR\_FILECONTENTS

This format identifier is used with the [CFSTR\_FILEDESCRIPTOR](https://docs.microsoft.com/windows) format to transfer data as if it were a file, regardless of how it is actually stored. The data consists of an [**STGMEDIUM**](https://msdn.microsoft.com/en-us/library/ms683812(v=VS.85).aspx) structure that represents the contents of one file. The file is normally represented as a stream object, which avoids having to place the contents of the file in memory. In that case, the **tymed** member of the **STGMEDIUM** structure is set to TYMED\_ISTREAM, and the file is represented by an [**IStream**](https://msdn.microsoft.com/en-us/library/Aa380034(v=VS.85).aspx) interface. The file can also be a storage or global memory object (TYMED\_ISTORAGE or TYMED\_HGLOBAL). The associated CFSTR\_FILEDESCRIPTOR format contains a [**FILEDESCRIPTOR**](https://msdn.microsoft.com/en-us/library/Bb773288(v=VS.85).aspx) structure for each file that specifies the file's name and attributes.

The target treats the data associated with a CFSTR\_FILECONTENTS format as if it were a file. When the target calls [**IDataObject::GetData**](https://msdn.microsoft.com/en-us/library/ms678431(v=VS.85).aspx) to extract the data, it specifies a particular file by setting the **lindex** member of the [**FORMATETC**](https://msdn.microsoft.com/en-us/library/ms682177(v=VS.85).aspx) structure to the zero-based index of the file's [**FILEDESCRIPTOR**](https://msdn.microsoft.com/en-us/library/Bb773288(v=VS.85).aspx) structure in the accompanying [CFSTR\_FILEDESCRIPTOR](https://docs.microsoft.com/windows) format. The target then uses the returned interface pointer or global memory handle to extract the data.

### CFSTR\_FILEDESCRIPTOR

This format identifier is used with the [CFSTR\_FILECONTENTS](https://docs.microsoft.com/windows) format to transfer data as a group of files. These two formats are the preferred way to transfer Shell objects that are not stored as file-system files. For example, these formats can be used to transfer a group of email messages as individual files, even though each email is actually stored as a block of data in a database. The data consists of an [**STGMEDIUM**](https://msdn.microsoft.com/en-us/library/ms683812(v=VS.85).aspx) structure that contains a global memory object. The structure's **hGlobal** member points to a [**FILEGROUPDESCRIPTOR**](https://msdn.microsoft.com/en-us/library/Bb773290(v=VS.85).aspx) structure that is followed by an array containing one [**FILEDESCRIPTOR**](https://msdn.microsoft.com/en-us/library/Bb773288(v=VS.85).aspx) structure for each file in the group. For each **FILEDESCRIPTOR** structure, there is a separate CFSTR\_FILECONTENTS format that contains the contents of the file. To identify a particular file's CFSTR\_FILECONTENTS format, set the **lIndex** value of the [**FORMATETC**](https://msdn.microsoft.com/en-us/library/ms682177(v=VS.85).aspx) structure to the zero-based index of the file's **FILEDESCRIPTOR** structure.

The CFSTR\_FILEDESCRIPTOR format is commonly used to transfer data as if it were a group of files, regardless of how it is actually stored. From the target's perspective, each CFSTR\_FILECONTENTS format represents a single file and is treated accordingly. However, the source can store the data in any way it chooses. While a CSFTR\_FILECONTENTS format might correspond to a single file, it could also, for example, represent data extracted by the source from a database or text document.

### CFSTR\_FILENAME

This format identifier is used to transfer a single file. The data consists of an [**STGMEDIUM**](https://msdn.microsoft.com/en-us/library/ms683812(v=VS.85).aspx) structure that contains a global memory object. The structure's **hGlobal** member points to a single **null**-terminated string containing the file's fully qualified file path. This format has been superseded by [CF\_HDROP](https://docs.microsoft.com/windows), but it is supported for backward compatibility with Windows 3.1 applications.

### CFSTR\_FILENAMEMAP

This format identifier is used when a group of files in [CF\_HDROP](https://docs.microsoft.com/windows) format is being renamed as well as transferred. The data consists of an [**STGMEDIUM**](https://msdn.microsoft.com/en-us/library/ms683812(v=VS.85).aspx) structure that contains a global memory object. The structure's **hGlobal** member points to a double **null**-terminated character array. This array contains a new name for each file, in the same order that the files are listed in the accompanying CF\_HDROP format. The format of the character array is the same as that used by CF\_HDROP to list the transferred files.

### CFSTR\_MOUNTEDVOLUME

This format identifier is used to transfer a path on a mounted volume. It is similar to [CF\_HDROP](https://docs.microsoft.com/windows), but it contains only a single path and can handle the longer path strings that might be needed to represent a path when the volume is mounted on a folder. The data consists of an [**STGMEDIUM**](https://msdn.microsoft.com/en-us/library/ms683812(v=VS.85).aspx) structure that contains a global memory object. The structure's **hGlobal** member points to a single **null**-terminated string containing the fully qualified file path. The path string must end with a '\\' character, followed by the terminating **NULL**.

Prior to Windows 2000, volumes could be mounted only on drive letters. For Windows 2000 and later systems with an NTFS formatted drive, you can also mount volumes on empty folders. This feature allows a volume to be mounted without taking up a drive letter. The mounted volume can use any currently supported format, including FAT, FAT32, NTFS, and CDFS.

You can add pages to a Drive Properties property sheet by implementing a [property sheet handler](propsheet-handlers.md). If the volume is mounted on a drive letter, the Shell passes path information to the handler with the [CF\_HDROP](https://docs.microsoft.com/windows) format. With Windows 2000 and later systems, the CF\_HDROP format is used when a volume is mounted on a drive letter, just as with earlier systems. However, if a volume is mounted on a folder, the [CFSTR\_MOUNTEDVOLUME](https://docs.microsoft.com/windows) format identifier is used instead of CF\_HDROP.

If only drive letters will be used to mount volumes, only [CF\_HDROP](https://docs.microsoft.com/windows) will be used, and existing property sheet handlers will work as they did with earlier systems. However, if you want your handler to display a page for volumes that are mounted on folders as well as drive letters, the handler must be able to understand both the CSFTR\_MOUNTEDVOLUME and CF\_HDROP formats.

### CFSTR\_SHELLIDLIST

This format identifier is used when transferring the locations of one or more existing namespace objects. It is used in much the same way as [CF\_HDROP](https://docs.microsoft.com/windows), but it contains PIDLs instead of file system paths. Using PIDLs allows the CFSTR\_SHELLIDLIST format to handle virtual objects as well as file system objects. The data is an [**STGMEDIUM**](https://msdn.microsoft.com/en-us/library/ms683812(v=VS.85).aspx) structure that contains a global memory object. The structure's **hGlobal** member points to a [**CIDA**](/windows/desktop/api/shlobj_core/ns-shlobj_core-_ida) structure.

The **aoffset** member of the [**CIDA**](/windows/desktop/api/shlobj_core/ns-shlobj_core-_ida) structure is an array containing offsets to the beginning of the [**ITEMIDLIST**](/windows/desktop/api/Shtypes/ns-shtypes-_itemidlist) structure for each PIDL that is being transferred. To extract a particular PIDL, first determine its index. Then, add the **aoffset** value that corresponds to that index to the address of the **CIDA** structure.

The first element of **aoffset** contains an offset to the fully qualified PIDL of a parent folder. If this PIDL is empty, the parent folder is the desktop. Each of the remaining elements of the array contains an offset to one of the PIDLs to be transferred. All of these PIDLs are relative to the PIDL of the parent folder.

The following two macros can be used to retrieve PIDLs from a [**CIDA**](/windows/desktop/api/shlobj_core/ns-shlobj_core-_ida) structure. The first takes a pointer to the structure and retrieves the PIDL of the parent folder. The second takes a pointer to the structure and retrieves one of the other PIDLs, identified by its zero-based index.


```C++
#define GetPIDLFolder(pida) (LPCITEMIDLIST)(((LPBYTE)pida)+(pida)->aoffset[0])

#define GetPIDLItem(pida, i) (LPCITEMIDLIST)(((LPBYTE)pida)+(pida)->aoffset[i+1])
```



> [!Note]  
> The value that is returned by these macros is a pointer to the PIDL's [**ITEMIDLIST**](/windows/desktop/api/Shtypes/ns-shtypes-_itemidlist) structure. Since these structures vary in length, you must determine the end of the structure by walking through each of the **ITEMIDLIST** structure's [**SHITEMID**](/windows/desktop/api/Shtypes/ns-shtypes-_shitemid) structures until you reach the two-byte **NULL** that marks the end.

 

### CFSTR\_SHELLIDLISTOFFSET

This format identifier is used with formats such as [CF\_HDROP](https://docs.microsoft.com/windows), [CFSTR\_SHELLIDLIST](https://docs.microsoft.com/windows), and [CFSTR\_FILECONTENTS](https://docs.microsoft.com/windows) to specify the position of a group of objects following a transfer. The data consists of an [**STGMEDIUM**](https://msdn.microsoft.com/en-us/library/ms683812(v=VS.85).aspx) structure that contains a global memory object. The structure's **hGlobal** member points to an array of [**POINT**](https://msdn.microsoft.com/en-us/library/Dd162805(v=VS.85).aspx) structures. The first structure specifies the screen coordinates, in pixels, of the upper-left corner of the rectangle that encloses the group. The remainder of the structures specify the locations of the individual objects relative to the group's position. They must be in the same order as that used to list the objects in the associated format.

## Formats for Transferring Virtual Objects

The CFSTR\_SHELLIDLIST format can be used to transfer both file system and virtual objects. However, there are also several specialized formats for transferring particular types of virtual objects.

-   [CFSTR\_NETRESOURCES](https://docs.microsoft.com/windows)
-   [CFSTR\_PRINTERGROUP](https://docs.microsoft.com/windows)
-   [CFSTR\_INETURL](https://docs.microsoft.com/windows)
-   [CFSTR\_SHELLURL (deprecated)](https://docs.microsoft.com/windows)

### CFSTR\_NETRESOURCES

This format identifier is used when transferring network resources, such as a domain or server. The data is an [**STGMEDIUM**](https://msdn.microsoft.com/en-us/library/ms683812(v=VS.85).aspx) structure that contains a global memory object. The structure's **hGlobal** member points to a [**NRESARRAY**](/windows/desktop/api/shlobj_core/ns-shlobj_core-_nresarray) structure. The **nr** member of that structure indicates a [**NETRESOURCE**](https://msdn.microsoft.com/en-us/library/Aa385353(v=VS.85).aspx) structure whose **lpRemoteName** member contains a **null**-terminated string identifying the network resource. The drop target can then use the data with any of the [Windows Networking (WNet)](https://msdn.microsoft.com/en-us/library/Aa385406(v=VS.85).aspx) API functions, such as [**WNetAddConnection**](https://msdn.microsoft.com/en-us/library/Aa385410(v=VS.85).aspx), to perform network operations on the object.

### CFSTR\_PRINTERGROUP

This format identifier is used when transferring the friendly names of printers. The data is an [**STGMEDIUM**](https://msdn.microsoft.com/en-us/library/ms683812(v=VS.85).aspx) structure that contains a global memory object. The structure's **hGlobal** member points to a string in the same format as that used with [CF\_HDROP](https://docs.microsoft.com/windows). However, the **pFiles** member of the [**DROPFILES**](/windows/desktop/api/shlobj_core/ns-shlobj_core-_dropfiles) structure contains one or more friendly names of printers instead of file paths.

### CFSTR\_INETURL

This format identifier replaces [CFSTR\_SHELLURL (deprecated)](https://docs.microsoft.com/windows). If you want your application to manipulate clipboard URLs, use CFSTR\_INETURL instead of CFSTR\_SHELLURL (deprecated). This format gives the best clipboard representation of a single URL. If UNICODE is not defined, the application retrieves the CF\_TEXT/CFSTR\_SHELLURL version of the URL. If UNICODE is defined, the application retrieves the CF\_UNICODE version of the URL.

### CFSTR\_SHELLURL (deprecated)

> [!Note]  
> This format identifier has been deprecated; use CFSTR\_INETURL instead.

 

## Formats for Communication Between Source and Target

These format identifiers allow communication between source and target. The formats accompany the data and give applications a greater degree of control over move-copy-paste or drag-and-drop operations involving Shell objects.

-   [CFSTR\_INDRAGLOOP](https://docs.microsoft.com/windows)
-   [CFSTR\_LOGICALPERFORMEDDROPEFFECT](https://docs.microsoft.com/windows)
-   [CFSTR\_PASTESUCCEEDED](https://docs.microsoft.com/windows)
-   [CFSTR\_PERFORMEDDROPEFFECT](https://docs.microsoft.com/windows)
-   [CFSTR\_PREFERREDDROPEFFECT](https://docs.microsoft.com/windows)
-   [CFSTR\_TARGETCLSID](https://docs.microsoft.com/windows)
-   [CFSTR\_UNTRUSTEDDRAGDROP](https://docs.microsoft.com/windows)
-   [DragWindow](#dragwindow)

### CFSTR\_INDRAGLOOP

This format identifier is used by a data object to indicate whether it is in a drag-and-drop loop. The data is an [**STGMEDIUM**](https://msdn.microsoft.com/en-us/library/ms683812(v=VS.85).aspx) structure that contains a global memory object. The structure's **hGlobal** member points to a **DWORD** value. If the **DWORD** value is nonzero, the data object is within a drag-and-drop loop. If the value is set to zero, the data object is not within a drag-and-drop loop.

Some drop targets might call [**IDataObject::GetData**](https://msdn.microsoft.com/en-us/library/ms678431(v=VS.85).aspx) and attempt to extract data while the object is still within the drag-and-drop loop. Fully rendering the object for each such occurrence might cause the drag cursor to stall. If the data object supports [CFSTR\_INDRAGLOOP](https://docs.microsoft.com/windows), the target can instead use that format to check the status of the drag-and-drop loop and avoid memory intensive rendering of the object until it is actually dropped. The formats that are memory intensive to render should still be included in the [**FORMATETC**](https://msdn.microsoft.com/en-us/library/ms682177(v=VS.85).aspx) enumerator and in calls to [**IDataObject::QueryGetData**](https://msdn.microsoft.com/en-us/library/ms680637(v=VS.85).aspx). If the data object does not set CFSTR\_INDRAGLOOP, it should act as if the value is set to zero.

### CFSTR\_LOGICALPERFORMEDDROPEFFECT

[Version 5.0.](versions.md)This format identifier allows a drop source to call the data object's [**IDataObject::GetData**](https://msdn.microsoft.com/en-us/library/ms678431(v=VS.85).aspx) method to determine the outcome of a Shell data transfer. The data is an [**STGMEDIUM**](https://msdn.microsoft.com/en-us/library/ms683812(v=VS.85).aspx) structure that contains a global memory object. The structure's **hGlobal** member points to a DWORD containing a [**DROPEFFECT**](https://msdn.microsoft.com/en-us/library/ms693457(v=VS.85).aspx) value.

The [CFSTR\_PERFORMEDDROPEFFECT](https://docs.microsoft.com/windows) format identifier was intended to allow the target to indicate to the data object what operation actually took place. However, the Shell uses [optimized moves](datascenarios.md) for file system objects whenever possible. In that case, the Shell normally sets the CFSTR\_PERFORMEDDROPEFFECT value to DROPEFFECT\_NONE, to indicate to the data object that the original data has been deleted. Thus, the source cannot use the CFSTR\_PERFORMEDDROPEFFECT value to determine which operation has taken place. While most sources do not need this information, there are some exceptions. For instance, even though optimized moves eliminate the need for a source to delete any data, the source might still need to update a related database to indicate that the files have been moved or copied.

If a source needs to know which operation took place, it can call the data object's [**IDataObject::GetData**](https://msdn.microsoft.com/en-us/library/ms678431(v=VS.85).aspx) method and request the CFSTR\_LOGICALPERFORMEDDROPEFFECT format. This format essentially reflects what happens from the user's point of view after the operation is complete. If a new file is created and the original file is deleted, the user sees a move operation and the format's data value is set to DROPEFFECT\_MOVE. If the original file is still there, the user sees a copy operation and the format's data value is set to DROPEFFECT\_COPY. If a link was created, the format's data value will be DROPEFFECT\_LINK.

### CFSTR\_PASTESUCCEEDED

This format identifier is used by the target to inform the data object, through its [**IDataObject::SetData**](https://msdn.microsoft.com/en-us/library/ms686626(v=VS.85).aspx) method, that a delete-on-paste operation succeeded. The data is an [**STGMEDIUM**](https://msdn.microsoft.com/en-us/library/ms683812(v=VS.85).aspx) structure that contains a global memory object. The structure's **hGlobal** member points to a **DWORD** containing a [**DROPEFFECT**](https://msdn.microsoft.com/en-us/library/ms693457(v=VS.85).aspx) value. This format is used to notify the data object that it should complete the cut operation and delete the original data, if necessary. For more information, see [Delete-on-Paste Operations](datascenarios.md).

### CFSTR\_PERFORMEDDROPEFFECT

This format identifier is used by the target to inform the data object through its [**IDataObject::SetData**](https://msdn.microsoft.com/en-us/library/ms686626(v=VS.85).aspx) method of the outcome of a data transfer. The data is an [**STGMEDIUM**](https://msdn.microsoft.com/en-us/library/ms683812(v=VS.85).aspx) structure that contains a global memory object. The structure's **hGlobal** member points to a **DWORD** set to the appropriate [**DROPEFFECT**](https://msdn.microsoft.com/en-us/library/ms693457(v=VS.85).aspx) value, normally DROPEFFECT\_MOVE or DROPEFFECT\_COPY.

This format is normally used when the outcome of an operation can be either move or copy, such as in an [optimized move](datascenarios.md) or delete-on-paste operation. It provides a reliable way for the target to tell the data object what actually happened. It was introduced because the value of *pdwEffect* returned by [**DoDragDrop**](https://msdn.microsoft.com/en-us/library/ms678486(v=VS.85).aspx) did not reliably indicate which operation had taken place. The [CFSTR\_PERFORMEDDROPEFFECT](https://docs.microsoft.com/windows) format is the reliable way to indicate that an unoptimized move has taken place.

### CFSTR\_PREFERREDDROPEFFECT

This format identifier is used by the source to specify whether its preferred method of data transfer is move or copy. A drop target requests this format by calling the data object's [**IDataObject::GetData**](https://msdn.microsoft.com/en-us/library/ms678431(v=VS.85).aspx) method. The data is an [**STGMEDIUM**](https://msdn.microsoft.com/en-us/library/ms683812(v=VS.85).aspx) structure that contains a global memory object. The structure's **hGlobal** member points to a **DWORD** value. This value is set to DROPEFFECT\_MOVE if a move operation is preferred or DROPEFFECT\_COPY if a copy operation is preferred.

This feature is used when a source can support either a move or copy operation. It uses the [CFSTR\_PREFERREDDROPEFFECT](https://docs.microsoft.com/windows) format to communicate its preference to the target. Because the target is not obligated to honor the request, the target must call the source's [**IDataObject::SetData**](https://msdn.microsoft.com/en-us/library/ms686626(v=VS.85).aspx) method with a [CFSTR\_PERFORMEDDROPEFFECT](https://docs.microsoft.com/windows) format to tell the data object which operation was actually performed.

With a [delete-on-paste](datascenarios.md) operation, the CFSTR\_PREFERREDDROPFORMAT format is used to tell the target whether the source did a cut or copy. With a drag-and-drop operation, you can use CFSTR\_PREFERREDDROPFORMAT to specify the Shell's action. If this format is not present, the Shell performs a default action, based on context. For instance, if a user drags a file from one volume and drops it on another volume, the Shell's default action is to copy the file. By including a CFSTR\_PREFERREDDROPFORMAT format in the data object, you can override the default action and explicitly tell the Shell to copy, move, or link the file. If the user chooses to drag with the right button, CFSTR\_PREFERREDDROPFORMAT specifies the default command on the [drag-and-drop](context-menu-handlers.md) shortcut menu. The user is still free to choose other commands on the menu.

Before Microsoft Internet Explorer 4.0, an application indicated that it was transferring shortcut file types by setting FD\_LINKUI in the **dwFlags** member of the [**FILEDESCRIPTOR**](https://msdn.microsoft.com/en-us/library/Bb773288(v=VS.85).aspx) structure. Targets then had to use a potentially time-consuming call to [**IDataObject::GetData**](https://msdn.microsoft.com/en-us/library/ms678431(v=VS.85).aspx) to find out if the FD\_LINKUI flag was set. Now, the preferred way to indicate that shortcuts are being transferred is to use the CFSTR\_PREFERREDDROPEFFECT format set to DROPEFFECT\_LINK. However, for backward compatibility with older systems, sources should still set the FD\_LINKUI flag.

### CFSTR\_TARGETCLSID

This format identifier is used by a target to provide its CLSID to the source. The data is an [**STGMEDIUM**](https://msdn.microsoft.com/en-us/library/ms683812(v=VS.85).aspx) structure that contains a global memory object. The structure's **hGlobal** member points to the CLSID GUID of the drop target.

This format is used primarily to allow objects to be deleted by dragging them to the Recycle Bin. When an object is dropped in the Recycle Bin, the source's [**IDataObject::SetData**](https://msdn.microsoft.com/en-us/library/ms686626(v=VS.85).aspx) method is called with a CFSTR\_TARGETCLSID format set to the Recycle Bin's CLSID (CLSID\_RecycleBin). The source can then delete the original object.

### CFSTR\_UNTRUSTEDDRAGDROP

This format identifier is used by Windows Internet Explorer and the Windows Shell to provide a mechanism through which to block or prompt for drag-and-drop operations originating from Internet Explorer in conjunction with the [**URLACTION\_SHELL\_ENHANCED\_DRAGDROP\_SECURITY**](https://www.bing.com/search?q=**URLACTION\_SHELL\_ENHANCED\_DRAGDROP\_SECURITY**) flag.

**CFSTR\_UNTRUSTEDDRAGDROP** is added by the source of a drag-and-drop operation to specify that the data object might contain untrustworthy data. The data is represented by an [**STGMEDIUM**](https://msdn.microsoft.com/en-us/library/ms683812(v=VS.85).aspx) structure that contains a global memory object. The structure's **hGlobal** member points to a **DWORD** set to an appropriate [**URL Action**](https://www.bing.com/search?q=**URL+Action**) flag to cause a policy check through the [**IInternetSecurityManager::ProcessUrlAction**](https://www.bing.com/search?q=**IInternetSecurityManager::ProcessUrlAction**) method, using the [**PUAF\_ENFORCERESTRICTED**](https://www.bing.com/search?q=**PUAF\_ENFORCERESTRICTED**) flag.

### DragWindow

This format is used in a drag-and-drop operation to identify an object's drag image (window) so that its visual information can be updated dynamically. When an object is dragged over a drop target, an application updates its [**DROPDESCRIPTION**](/windows/desktop/api/shlobj_core/ns-shlobj_core-dropdescription) structure in response to the [**IDropTarget::DragOver**](https://msdn.microsoft.com/en-us/library/ms680129(v=VS.85).aspx) or [**IDropSource::GiveFeedback**](https://msdn.microsoft.com/en-us/library/ms693723(v=VS.85).aspx) method. The **DROPDESCRIPTION** is updated with a new [**DROPIMAGETYPE**](/windows/desktop/api/shlobj_core/ne-shlobj_core-dropimagetype) value that indicates the decoration to be applied to the drag window's visual; for instance, an indication that the file is being copied rather than moved or that the object cannot be dropped to that location. However, until the object receives a [**DDWM\_UPDATEWINDOW**](ddwm-updatewindow.md) message, the visuals are not updated. This format provides the **HWND** of the recipient drag window to the sender of the **DDWM\_UPDATEWINDOW** message.

The clipboard data is of type [**TYMED\_HGLOBAL**](https://msdn.microsoft.com/en-us/library/ms691227(v=VS.85).aspx). It is a **DWORD** representation of an **HWND**. The data can be passed to the **ULongToHandle** function, defined in Basetsd.h, to provide a 64-bit **HWND** for use on 64-bit Windows.

This format does not require the inclusion of Shlobj.h.

 

 



