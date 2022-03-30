---
description: The data object is central to all Shell data transfers.
ms.assetid: c63d339e-ac62-4da1-b5ce-22d45a6a3413
title: Shell Data Object
ms.topic: article
ms.date: 05/31/2018
---

# Shell Data Object

The data object is central to all Shell data transfers. It is primarily a container to hold the transferred data. However, the target can also communicate with the data object to facilitate some specialized types of Shell data transfer such as optimized moves. This topic provides a general discussion of how Shell data objects work, how they are constructed by a source, and how they are handled by a target. For a detailed discussion of how to use data objects to transfer different types of Shell data, see [Handling Shell Data Transfer Scenarios](datascenarios.md).

- [How Data Objects Work](#how-data-objects-work)
    - [Clipboard Formats](#clipboard-formats)
    - [FORMATETC Structure](#formatetc-structure)
    - [STGMEDIUM structure](#stgmedium-structure)
- [How a Source Creates a Data Object](#how-a-source-creates-a-data-object)
    - [How to Add a Global Memory Object to a Data Object](#how-to-add-a-global-memory-object-to-a-data-object)
    - [Implementing IDataObject](#implementing-idataobject)
    - [Implementing IDropSource](#implementing-idropsource)
- [How a Target Handles a Data Object](#how-a-target-handles-a-data-object)
    - [Extracting Shell Data from a Data Object](#extracting-shell-data-from-a-data-object)
    - [Implementing IDropTarget](#implementing-idroptarget)
- [Using the Drag-and-Drop Helper Object](#using-the-drag-and-drop-helper-object)
    - [Using the IDragSourceHelper Interface](#using-the-idragsourcehelper-interface)
    - [Using the IDropTargetHelper Interface](#using-the-idroptargethelper-interface)

## How Data Objects Work

Data objects are Component Object Model (COM) objects, created by the data source to transfer data to a target. They typically carry more than one item of data. There are two reasons for this practice:

- While almost any type of data can be transferred with a data object, the source typically does not know what kind of data the target can accept. For instance, the data might be a portion of a formatted text document. While the target might be able to handle complex formatting information, it might also be able to accept only ANSI text. For this reason, data objects often include the same data in several different formats. The target can then extract the data in a format that it can handle.
- Data objects can also contain auxiliary data items that are not versions of source data. This type of data item typically provides additional information about the data transfer operation. For instance, the Shell uses auxiliary data items to indicate whether a file is to be copied or moved.

### Clipboard Formats

Each item of data in a data object has an associated format, usually called a *clipboard format*. There are a number of standard clipboard formats, declared in Winuser.h, that correspond to commonly used types of data. Clipboard formats are integers, but they are normally referred to by their equivalent name, which has the form CF\_*XXX*. For instance, the clipboard format for ANSI text is CF\_TEXT.

Applications can extend the range of available clipboard formats by defining private formats. To define a private format, an application calls [RegisterClipboardFormat](/windows/win32/api/winuser/nf-winuser-registerclipboardformata) with a string that identifies the format. The unsigned integer that the function returns is a valid format value that can be used just like a standard clipboard format. However, both source and target must register the format in order to use it. With one exception—[CF\_HDROP](clipboard.md)—the clipboard formats used to transfer Shell data are defined as private formats. They must be registered by the source and target before they can be used. For a description of the available Shell clipboard formats, see Shell Clipboard Formats.

Although there are some exceptions, data objects normally contain only one item of data for each clipboard format they support. This one-to-one correlation between format and data allows the format value to be used as an identifier for the associated data item. In fact, when discussing the contents of a data object, a particular item of data is typically called a "format" and is referred to by its format name. For example, phrases such as "Extract the CF\_TEXT format..." are typically used when discussing a data object's ANSI text data item.

When the drop target receives the pointer to the data object, the drop target enumerates the available formats to determine what types of data are available. It then requests one or more of the available formats and extracts the data. The specific way that the target extracts Shell data from a data object varies with the format; this is discussed in detail in [How a Target Handles a Data Object](#how-a-target-handles-a-data-object).

With simple clipboard data transfers, the data is placed in a global memory object. The address of that object is placed on the Clipboard, along with its format. The clipboard format tells the target what kind of data it will find at the associated address. While simple clipboard transfers are easy to implement:

- Data objects provide a much more flexible way to transfer data.
- Data objects are better suited for transferring large amounts of data.
- Data objects must be used to transfer data with a drag-and-drop operation.

For these reasons, all Shell data transfers use data objects. With data objects, clipboard formats are not used directly. Instead, data items are identified with a generalization of the clipboard format, a [**FORMATETC**](/windows/win32/api/objidl/ns-objidl-formatetc) structure.

### FORMATETC Structure

The [**FORMATETC**](/windows/win32/api/objidl/ns-objidl-formatetc) structure is an extended version of a clipboard format. As used for Shell data transfers, the **FORMATETC** structure has the following characteristics:

- A data item is still identified by its clipboard format, in the **cfFormat** member.
- Data transfer is not limited to global memory objects. The **tymed** member is used to indicate the data transfer mechanism contained in the associated [**STGMEDIUM**](/windows/win32/api/objidl/ns-objidl-ustgmedium-r1) structure. It is set to one of the [**TYMED\_XXX**](/windows/win32/api/objidl/ne-objidl-tymed) values.
- The Shell uses the **lIndex** member with its [CFSTR\_FILECONTENTS](clipboard.md) format to allow a data object to contain more than one data item per format. For a discussion of how to use this format, see the *Using the CFSTR\_FILECONTENTS Format to Extract Data from a File* section of [Handling Shell Data Transfer Scenarios](datascenarios.md).
- The **dwAspect** member is typically set to DVASPECT\_CONTENT. However, there are three values defined in Shlobj.h that can be used for Shell data transfer. 

    | Value               | Description                                                                                       |
    |---------------------|---------------------------------------------------------------------------------------------------|
    | DVASPECT\_COPY      | Used to indicate that the format represents a copy of the data.                                   |
    | DVASPECT\_LINK      | Used to indicate that the format represents a shortcut to the data.                               |
    | DVASPECT\_SHORTNAME | Used with the CF\_HDROP format to request a file path with the names shortened to the 8.3 format. |

    

     

- The **ptd** member is not used for Shell data transfers and is normally set to **NULL**.

### STGMEDIUM structure

The [**STGMEDIUM**](/windows/win32/api/objidl/ns-objidl-ustgmedium-r1) structure provides access to the data being transferred. Three data transfer mechanisms are supported for Shell data:

- A global memory object.
- An [**IStream**](/windows/win32/api/objidl/nn-objidl-istream) interface.
- An [**IStorage**](/windows/win32/api/objidl/nn-objidl-istorage) interface.

The **tymed** member of the [**STGMEDIUM**](/windows/win32/api/objidl/ns-objidl-ustgmedium-r1) structure is a [**TYMED\_XXX**](/windows/win32/api/objidl/ne-objidl-tymed) value that identifies the data transfer mechanism. The second member is a pointer that is used by the target to extract the data. The pointer can be one of a variety of types, depending on the **tymed** value. The three **tymed** values that are used for Shell data transfers are summarized in the following table, along with their corresponding **STGMEDIUM** member name.



| tymed Value     | Member name | Description                                                                                                                                                                                                                                                                                                       |
|-----------------|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TYMED\_HGLOBAL  | **hGlobal** | A pointer to a global memory object. This pointer type is typically used for transferring small amounts of data. For instance, the Shell uses global memory objects to transfer short text strings such as file names or URLs.                                                                                    |
| TYMED\_ISTREAM  | **pstm**    | A pointer to an [**IStream**](/windows/win32/api/objidl/nn-objidl-istream) interface. This pointer type is preferred for most Shell data transfers because it requires relatively little memory compared to TYMED\_HGLOBAL. Also, the TYMED\_ISTREAM data transfer mechanism does not require the source to store its data in any particular way. |
| TYMED\_ISTORAGE | **pstg**    | A pointer to an [**IStorage**](/windows/win32/api/objidl/nn-objidl-istorage) interface. The target calls the interface methods to extract the data. Like TYMED\_ISTREAM, this pointer type requires relatively little memory. However, because TYMED\_ISTORAGE is less flexible than TYMED\_ISTREAM, it is not as commonly used.                  |



 

## How a Source Creates a Data Object

When a user initiates a Shell data transfer, the source is responsible for creating a data object and loading it with data. The following procedure summarizes the process:

1.  Call [RegisterClipboardFormat](/windows/win32/api/winuser/nf-winuser-registerclipboardformata) to obtain a valid clipboard format value for each Shell format that will be included in the data object. Remember that [CF\_HDROP](clipboard.md) is already a valid clipboard format and does not need to be registered.
2.  For each format to be transferred, either put the associated data into a global memory object or create an object that provides access to that data through an [**IStream**](/windows/win32/api/objidl/nn-objidl-istream) or [**IStorage**](/windows/win32/api/objidl/nn-objidl-istorage) interface. The **IStream** and **IStorage** interfaces are created using standard COM techniques. For a discussion of how to handle global memory objects, see [How to Add a Global Memory Object to a Data Object](#how-to-add-a-global-memory-object-to-a-data-object).
3.  Create [**FORMATETC**](/windows/win32/api/objidl/ns-objidl-formatetc) and [**STGMEDIUM**](/windows/win32/api/objidl/ns-objidl-ustgmedium-r1) structures for each format.
4.  Instantiate a data object.
5.  Load the data into the data object by calling the [**IDataObject::SetData**](/windows/win32/api/objidl/nf-objidl-idataobject-setdata) method for each supported format and passing in the format's [**FORMATETC**](/windows/win32/api/objidl/ns-objidl-formatetc) and [**STGMEDIUM**](/windows/win32/api/objidl/ns-objidl-ustgmedium-r1) structures.
6.  With clipboard data transfers, call [**OleSetClipboard**](/windows/win32/api/ole2/nf-ole2-olesetclipboard) to place a pointer to the data object's [**IDataObject**](/windows/win32/api/objidl/nn-objidl-idataobject) interface on the Clipboard. For drag-and-drop transfers, initiate a *drag loop* by calling [**DoDragDrop**](/windows/win32/api/ole2/nf-ole2-dodragdrop). The **IDataObject** pointer will be passed to the drop target when the data is dropped, ending the drag loop.

The data object is now ready to be transferred to the target. For clipboard data transfers, the object is simply held until the target requests it by calling [**OleGetClipboard**](/windows/win32/api/ole2/nf-ole2-olegetclipboard). For drag-and-drop data transfers, the data object is responsible for creating an icon to represent the data and moving it as the user moves the cursor. While the object is in the drag loop, the source receives status information through its [**IDropSource**](/windows/win32/api/oleidl/nn-oleidl-idropsource) interface. For further discussion, see [Implementing IDropSource](#implementing-idropsource).

The source receives no notification if the data object is retrieved from the Clipboard by a target. When an object is dropped on a target by a drag-and-drop operation, the [**DoDragDrop**](/windows/win32/api/ole2/nf-ole2-dodragdrop) function that was called to initiate the drag loop will return.

### How to Add a Global Memory Object to a Data Object

Many of the Shell data formats are in the form of a global memory object. Use the following procedure to create a format containing a global memory object and load it into the data object:

1.  Create a [**FORMATETC**](/windows/win32/api/objidl/ns-objidl-formatetc) structure. Set the **cfFormat** member to the appropriate clipboard format value and the **tymed** member to TYMED\_HGLOBAL.
2.  Create an [**STGMEDIUM**](/windows/win32/api/objidl/ns-objidl-ustgmedium-r1) structure. Set the **tymed** member to TYMED\_HGLOBAL.
3.  Create a global memory object by calling [**GlobalAlloc**](/windows/win32/api/winbase/nf-winbase-globalalloc) to allocate a suitably sized block of memory.
4.  Assign the block of data to be transferred to the address returned by [**GlobalAlloc**](/windows/win32/api/winbase/nf-winbase-globalalloc).
5.  Assign the global memory object's address to the **hGlobal** member of the [**STGMEDIUM**](/windows/win32/api/objidl/ns-objidl-ustgmedium-r1) structure.
6.  Load the format into the data object by calling [**IDataObject::SetData**](/windows/win32/api/objidl/nf-objidl-idataobject-setdata) and passing in the [**FORMATETC**](/windows/win32/api/objidl/ns-objidl-formatetc) and [**STGMEDIUM**](/windows/win32/api/objidl/ns-objidl-ustgmedium-r1) structures created in the previous steps.

The following sample function creates a global memory object containing a **DWORD** value and loads it into a data object. The **pdtobj** parameter is a pointer to the data object's [**IDataObject**](/windows/win32/api/objidl/nn-objidl-idataobject) interface, **cf** is the clipboard format value, and **dw** is the data value.


```C++
STDAPI DataObj_SetDWORD(IDataObject *pdtobj, UINT cf, DWORD dw)
{
    FORMATETC fmte = {(CLIPFORMAT) cf, 
                      NULL, 
                      DVASPECT_CONTENT, 
                      -1, 
                      TYMED_HGLOBAL};
    STGMEDIUM medium;

    HRESULT hres = E_OUTOFMEMORY;
    DWORD *pdw = (DWORD *)GlobalAlloc(GPTR, sizeof(DWORD));
    
    if (pdw)
    {
        *pdw = dw;       
        medium.tymed = TYMED_HGLOBAL;
        medium.hGlobal = pdw;
        medium.pUnkForRelease = NULL;

        hres = pdtobj->SetData(&fmte, &medium, TRUE);
 
        if (FAILED(hres))
            GlobalFree((HGLOBAL)pdw);
    }
    return hres;
}
```



### Implementing IDataObject

[**IDataObject**](/windows/win32/api/objidl/nn-objidl-idataobject) is a data object's primary interface. It must be implemented by all data objects. It is used by both source and target for a variety of purposes, including:

- Loading data into the data object.
- Extracting data from the data object.
- Determining what types of data are in the data object.
- Providing feedback to the data object on outcome of the data transfer.

[**IDataObject**](/windows/win32/api/objidl/nn-objidl-idataobject) supports a number of methods. This section discusses how to implement the three most important methods for Shell data objects, [SetData](#setdata-method), [EnumFormatEtc](#enumformatetc-method), and [GetData](#getdata-method). For a discussion of the other methods, see the **IDataObject** reference.

### SetData method

The primary function of the [**IDataObject::SetData**](/windows/win32/api/objidl/nf-objidl-idataobject-setdata) method is to allow the source to load data into the data object. For each format to be included, the source creates a [**FORMATETC**](/windows/win32/api/objidl/ns-objidl-formatetc) structure to identify the format and an [**STGMEDIUM**](/windows/win32/api/objidl/ns-objidl-ustgmedium-r1) structure to hold a pointer to the data. The source then calls the object's **IDataObject::SetData** method and passes in the format's **FORMATETC** and **STGMEDIUM** structures. The method must store this information so that it is available when the target calls [**IDataObject::GetData**](/windows/win32/api/objidl/nf-objidl-idataobject-getdata) to extract data from the object.

However, when transferring files, the Shell often puts the information for each file to be transferred into a separate [CFSTR\_FILECONTENTS](clipboard.md) format. To distinguish the different files, the **lIndex** member of each file's [**FORMATETC**](/windows/win32/api/objidl/ns-objidl-formatetc) structure is set to an index value that identifies the particular file. Your [**IDataObject::SetData**](/windows/win32/api/objidl/nf-objidl-idataobject-setdata) implementation must be capable of storing multiple CFSTR\_FILECONTENTS formats that differ only by their **lIndex** members.

While the cursor is over the target window, the target can use the [drag-and-drop helper object](#using-the-drag-and-drop-helper-object) to specify the drag image. The drag-and-drop helper object calls [**IDataObject::SetData**](/windows/win32/api/objidl/nf-objidl-idataobject-setdata) to load private formats into the data object that are used for cross-process support. To support the drag-and-drop helper object, your **IDataObject::SetData** implementation must be able to accept and store arbitrary private formats.

After the data has been dropped, some types of Shell data transfer require the target to call [**IDataObject::SetData**](/windows/win32/api/objidl/nf-objidl-idataobject-setdata) to provide the data object with information about the outcome of the drop operation. For example, when moving files with an optimized move operation, the target normally deletes the original files, but it is not required to do so. The target informs the data object whether it deleted the files by calling **IDataObject::SetData** with a [CFSTR\_LOGICALPERFORMEDDROPEFFECT](clipboard.md) format. There are several other [Shell Clipboard Formats](clipboard.md) that are also used by the target to pass information to the data object. Your **IDataObject::SetData** implementation must be able to recognize these formats and respond appropriately. For further discussion, see [Handling Shell Data Transfer Scenarios](datascenarios.md).

### EnumFormatEtc method

When the target receives a data object, it commonly calls [**FORMATETC**](/windows/win32/api/objidl/ns-objidl-formatetc) to determine what formats the object contains. The method creates an OLE enumeration object and returns a pointer to the object's [**IEnumFORMATETC**](/windows/win32/api/objidl/nn-objidl-ienumformatetc) interface. The target then uses the interface to enumerate the available formats.

An enumeration object should always enumerate the available formats in order of quality, starting with the best. The relative quality of formats is defined by the drop source. In general, the highest-quality formats contain the richest and most complete data. For instance, a 24-bit color image would normally be considered higher quality than a gray-scale version of that image. The reason for enumerating formats in order of their quality is that targets typically enumerate until they get to a format that they support, and then they use that format to extract the data. For this procedure to produce the best available format that the target can support, the formats must be enumerated in order of their quality.

An enumeration object for Shell data is implemented in much the same way as for other types of data transfer, with one notable exception. Because data objects typically contain only one data item per format, they normally enumerate every format that is passed to [**IDataObject::SetData**](/windows/win32/api/objidl/nf-objidl-idataobject-setdata). However, as discussed in the [SetData method](#setdata-method) section, Shell data objects can contain multiple [CFSTR\_FILECONTENTS](clipboard.md) formats.

Because the purpose of [**IDataObject::EnumFormatEtc**](/windows/win32/api/objidl/nf-objidl-idataobject-enumformatetc) is to allow the target to determine what types of data are present, there is no need to enumerate more than one [CFSTR\_FILECONTENTS](clipboard.md) format. If the target needs to know how many of these formats the data object contains, the target can retrieve that information from the accompanying CFSTR\_FILEDESCRIPTOR format. For further discussion of how to implement **IDataObject::EnumFormatEtc**, see the method's reference documentation.

### GetData method

The target calls [**IDataObject::GetData**](/windows/win32/api/objidl/nf-objidl-idataobject-getdata) to extract a particular data format. The target specifies the format by passing in the appropriate [**FORMATETC**](/windows/win32/api/objidl/ns-objidl-formatetc) structure. **IDataObject::GetData** returns the format's [**STGMEDIUM**](/windows/win32/api/objidl/ns-objidl-ustgmedium-r1) structure.

The target can set the **tymed** member of the [**FORMATETC**](/windows/win32/api/objidl/ns-objidl-formatetc) structure to a specific TYMED\_*XXX* value to specify which data transfer mechanism it will use to extract the data. However, the target can also make a more generic request and let the data object decide. To ask the data object to select the data transfer mechanism, the target sets all the TYMED\_*XXX* values that it supports. [**IDataObject::GetData**](/windows/win32/api/objidl/nf-objidl-idataobject-getdata) selects one of these data transfer mechanisms and returns the appropriate [**STGMEDIUM**](/windows/win32/api/objidl/ns-objidl-ustgmedium-r1) structure. For instance, **tymed** is commonly set to TYMED\_HGLOBAL \| TYMED\_ISTREAM \| TYMED\_ISTORAGE to request any of the three Shell data transfer mechanisms.

> [!Note]  
> Because there can be multiple [CFSTR\_FILECONTENTS](clipboard.md) formats, the **cfFormat** and **tymed** members of the [**FORMATETC**](/windows/win32/api/objidl/ns-objidl-formatetc) structure are not sufficient to indicate which [**STGMEDIUM**](/windows/win32/api/objidl/ns-objidl-ustgmedium-r1) structure [**IDataObject::GetData**](/windows/win32/api/objidl/nf-objidl-idataobject-getdata) should return. For the CFSTR\_FILECONTENTS format, **IDataObject::GetData** must also examine the **FORMATETC** structure's **lIndex** member in order to return the correct **STGMEDIUM** structure.

 

The [CFSTR\_INDRAGLOOP](clipboard.md) format is placed in data objects to allow targets to check the status of the drag-and-drop loop while avoiding memory intensive rendering of the object's data. The format's data is a **DWORD** value that is set to a nonzero value if the data object is within a drag loop. The format's data value is set to zero if the data has been dropped. If a target requests this format and it has not been loaded by the source, [**IDataObject::GetData**](/windows/win32/api/objidl/nf-objidl-idataobject-getdata) should respond as if the source had loaded the format with a value of zero.

While the cursor is over the target window, the target can use the [drag-and-drop helper object](#using-the-drag-and-drop-helper-object) to specify the drag image. The drag-and-drop helper object calls [**IDataObject::SetData**](/windows/win32/api/objidl/nf-objidl-idataobject-setdata) to load private formats into the data object that are used for cross-process support. It later calls [**IDataObject::GetData**](/windows/win32/api/objidl/nf-objidl-idataobject-getdata) to retrieve them. To support the drag-and-drop helper object, your Shell Data Object implementation must be able to return arbitrary private formats when they are requested.

### Implementing IDropSource

The source must create an object that exposes an [**IDropSource**](/windows/win32/api/oleidl/nn-oleidl-idropsource) interface. This interface allows the source to update the *drag image* that indicates the current position of the cursor and to provide feedback to the system on how to terminate a drag-and-drop operation. **IDropSource** has two methods: [**GiveFeedback**](/windows/win32/api/oleidl/nf-oleidl-idropsource-givefeedback) and [**QueryContinueDrag**](/windows/win32/api/oleidl/nf-oleidl-idropsource-querycontinuedrag).

### GiveFeedback method

While in the drag loop, a drop source is responsible for keeping track of the cursor position and displaying an appropriate drag image. However, in some cases you might want to change the appearance of the drag image when it is over the drop target's window.

When the cursor enters or leaves the target window and while it is moving over the target window, the system periodically calls the target's [**IDropTarget**](/windows/win32/api/oleidl/nn-oleidl-idroptarget) interface. The target responds with a [**DROPEFFECT**](../com/dropeffect-constants.md) value that is forwarded to the source through the [**GiveFeedback**](/windows/win32/api/oleidl/nf-oleidl-idropsource-givefeedback) method. If appropriate, the source can modify the appearance of the cursor based on the **DROPEFFECT** value. For further details, see the **GiveFeedback** and [**DoDragDrop**](/windows/win32/api/ole2/nf-ole2-dodragdrop) references.

### QueryContinueDrag method

This method is called if the mouse button or keyboard state changes while the data object is in the drag loop. It notifies the source whether the ESC key has been pressed and provides the current state of the keyboard modifier keys, such as CTRL or SHIFT. The [**QueryContinueDrag**](/windows/win32/api/oleidl/nf-oleidl-idropsource-querycontinuedrag) method's return value specifies one of three actions:

- S\_OK. Continue the drag operation
- DRAGDROP\_S\_DROP. Drop the data. The system then calls the target's [**IDropTarget::Drop**](/windows/win32/api/oleidl/nf-oleidl-idroptarget-drop) method.
- DRAGDROP\_S\_CANCEL. Terminate the drag loop without dropping the data. This value is normally returned if the ESCAPE key was pressed.

For further discussion, see the [**QueryContinueDrag**](/windows/win32/api/oleidl/nf-oleidl-idropsource-querycontinuedrag) and [**DoDragDrop**](/windows/win32/api/ole2/nf-ole2-dodragdrop) references.

## How a Target Handles a Data Object

The target receives a data object when it either retrieves the data object from the Clipboard or has it dropped on the target window by the user. The target can then extract data from the data object. If necessary, the target can also notify the data object of the outcome of the operation. Prior to a Shell data transfer, a drop target must prepare itself for the operation:

1.  The target must call [RegisterClipboardFormat](/windows/win32/api/winuser/nf-winuser-registerclipboardformata) to obtain a valid clipboard format value for all Shell formats, other than [CF\_HDROP](clipboard.md), that might be included in the data object. CF\_HDROP is already a valid clipboard format and does not need to be registered.
2.  To support a drag-and-drop operation, the target must implement an [**IDropTarget**](/windows/win32/api/oleidl/nn-oleidl-idroptarget) interface and register a target window. To register a target window, the target calls [**RegisterDragDrop**](/windows/win32/api/ole2/nf-ole2-registerdragdrop) and passes in the window's handle and the **IDropTarget** interface pointer.

For clipboard transfers, the target does not receive any notification that a data object has been placed on the Clipboard. Typically, an application is notified that an object is on the Clipboard by a user action, such as clicking the Paste button on the application's toolbar. The target then retrieves the data object's [**IDataObject**](/windows/win32/api/objidl/nn-objidl-idataobject) pointer from the Clipboard by calling [**OleGetClipboard**](/windows/win32/api/ole2/nf-ole2-olegetclipboard). For drag-and-drop data transfers, the system uses the target's [**IDropTarget**](/windows/win32/api/oleidl/nn-oleidl-idroptarget) interface to provide the target with information about the progress of the data transfer:

- The system calls [**IDropTarget::DragEnter**](/windows/win32/api/oleidl/nf-oleidl-idroptarget-dragenter) when the cursor enters the target window.
- The system periodically calls [**IDropTarget::DragOver**](/windows/win32/api/oleidl/nf-oleidl-idroptarget-dragover) as the cursor passes over the target window, to give the target the current cursor position.
- The system calls [**IDropTarget::DragLeave**](/windows/win32/api/oleidl/nf-oleidl-idroptarget-dragleave) when the cursor leaves the target window.
- The system calls [**IDropTarget::Drop**](/windows/win32/api/oleidl/nf-oleidl-idroptarget-drop) when the user drops the data object on the target window.

For a discussion of how to implement these methods, see [**IDropTarget**](/windows/win32/api/oleidl/nn-oleidl-idroptarget).

When the data is dropped, [**IDropTarget::Drop**](/windows/win32/api/oleidl/nf-oleidl-idroptarget-drop) provides the target with a pointer to the data object's [**IDataObject**](/windows/win32/api/objidl/nn-objidl-idataobject) interface. The target then uses this interface to extract data from the data object.

### Extracting Shell Data from a Data Object

Once a data object has been dropped or retrieved from the Clipboard, the target can extract the data it needs. The first step in the extraction process is typically to enumerate the formats contained by the data object:

- Call [**IDataObject::EnumFormatEtc**](/windows/win32/api/objidl/nf-objidl-idataobject-enumformatetc). The data object creates a standard OLE enumeration object and returns a pointer to its [**IEnumFORMATETC**](/windows/win32/api/objidl/nn-objidl-ienumformatetc) interface.
- Use the [**IEnumFORMATETC**](/windows/win32/api/objidl/nn-objidl-ienumformatetc) methods to enumerate the formats contained by the data object. This operation usually retrieves one [**FORMATETC**](/windows/win32/api/objidl/ns-objidl-formatetc) structure for each format that the object contains. However, the enumeration object normally returns only a single **FORMATETC** structure for the [CFSTR\_FILECONTENTS](clipboard.md) format, regardless of how many such formats are contained by the data object.
- Select one or more formats to be extracted, and store their [**FORMATETC**](/windows/win32/api/objidl/ns-objidl-formatetc) structures.

To retrieve a particular format, pass the associated [**FORMATETC**](/windows/win32/api/objidl/ns-objidl-formatetc) structure to [**IDataObject::GetData**](/windows/win32/api/objidl/nf-objidl-idataobject-getdata). This method returns an [**STGMEDIUM**](/windows/win32/api/objidl/ns-objidl-ustgmedium-r1) structure that provides access to the data. To specify a particular data transfer mechanism, set the **tymed** value of the **FORMATETC** structure to the corresponding TYMED\_*XXX* value. To ask the data object to select a data transfer mechanism, the target sets the TYMED\_*XXX* values for every data transfer mechanism that the target can handle. The data object selects one of these data transfer mechanisms and returns the appropriate **STGMEDIUM** structure.

For most formats, the target can retrieve the data by passing the [**FORMATETC**](/windows/win32/api/objidl/ns-objidl-formatetc) structure that it received when it enumerated the available formats. One exception to this rule is [CFSTR\_FILECONTENTS](clipboard.md). Because a data object can contain multiple instances of this format, the **FORMATETC** structure returned by the enumerator might not correspond to the particular format you want to extract. In addition to specifying the **cfFormat** and **tymed** members, you must also set the **lIndex** member to the file's index value. For further discussion, see the *Using the CFSTR\_FILECONTENTS Format to Extract Data from a File* section of [Handling Shell Data Transfer Scenarios](datascenarios.md)

The data extraction process depends on the type of pointer contained by the returned [**STGMEDIUM**](/windows/win32/api/objidl/ns-objidl-ustgmedium-r1) structure. If the structure contains a pointer to an [**IStream**](/windows/win32/api/objidl/nn-objidl-istream) or [**IStorage**](/windows/win32/api/objidl/nn-objidl-istorage) interface, use the interface methods to extract the data. The process of extracting data from a global memory object is discussed in the next section.

### Extracting a global memory object from a data object

Many of the Shell data formats are in the form of a global memory object. Use the following procedure to extract a format containing a global memory object from a data object and assign its data to a local variable:

1.  Create a [**FORMATETC**](/windows/win32/api/objidl/ns-objidl-formatetc) structure. Set the **cfFormat** member to the appropriate clipboard format value and the **tymed** member to TYMED\_HGLOBAL.
2.  Create an empty [**STGMEDIUM**](/windows/win32/api/objidl/ns-objidl-ustgmedium-r1) structure.
3.  Call [**IDataObject::GetData**](/windows/win32/api/objidl/nf-objidl-idataobject-getdata), and pass in pointers to the [**FORMATETC**](/windows/win32/api/objidl/ns-objidl-formatetc) and [**STGMEDIUM**](/windows/win32/api/objidl/ns-objidl-ustgmedium-r1) structures.

    When [**IDataObject::GetData**](/windows/win32/api/objidl/nf-objidl-idataobject-getdata) returns, the [**STGMEDIUM**](/windows/win32/api/objidl/ns-objidl-ustgmedium-r1) structure will contain a pointer to the global memory object that contains the data.

4.  Assign the data to a local variable by calling [**GlobalLock**](/windows/win32/api/winbase/nf-winbase-globallock) and passing in the **hGlobal** member of the [**STGMEDIUM**](/windows/win32/api/objidl/ns-objidl-ustgmedium-r1) structure.
5.  Call [**GlobalUnlock**](/windows/win32/api/winbase/nf-winbase-globalunlock) to release the lock on the global memory object.
6.  Call [**ReleaseStgMedium**](/windows/win32/api/ole2/nf-ole2-releasestgmedium) to release the global memory object.

> [!Note]  
> You must use [**ReleaseStgMedium**](/windows/win32/api/ole2/nf-ole2-releasestgmedium) to release the global memory object, not [**GlobalFree**](/windows/win32/api/winbase/nf-winbase-globalfree).

 

The following example shows how to extract a **DWORD** value stored as a global memory object from a data object. The **pdtobj** parameter is a pointer to the data object's [**IDataObject**](/windows/win32/api/objidl/nn-objidl-idataobject) interface, **cf** is the clipboard format that identifies the desired data, and **pdwOut** is used to return the data value.


```C++
STDAPI DataObj_GetDWORD(IDataObject *pdtobj, UINT cf, DWORD *pdwOut)
{    STGMEDIUM medium;
   FORMATETC fmte = {(CLIPFORMAT) cf, NULL, DVASPECT_CONTENT, -1, 
       TYMED_HGLOBAL};
    HRESULT hres = pdtobj->GetData(&fmte, &medium);
    if (SUCCEEDED(hres))
   {
       DWORD *pdw = (DWORD *)GlobalLock(medium.hGlobal);
       if (pdw)
       {
           *pdwOut = *pdw;
           GlobalUnlock(medium.hGlobal);
       }
       else
       {
           hres = E_UNEXPECTED;
       }
       ReleaseStgMedium(&medium);
   }
   return hres;
}
```



### Implementing IDropTarget

The system uses the [**IDropTarget**](/windows/win32/api/oleidl/nn-oleidl-idroptarget) interface to communicate with the target while the cursor is over the target window. The target's responses are forwarded to the source through its [**IDropSource**](/windows/win32/api/oleidl/nn-oleidl-idropsource) interface. Depending on the response, the source can modify the icon that represents the data. If the drop target needs to specify the data icon, it can do so by creating a [drag-and-drop helper object](#using-the-drag-and-drop-helper-object).

With conventional drag-and-drop operations, the target informs the data object of the outcome of the operation by setting the *pdwEffect* parameter of [**IDropTarget::Drop**](/windows/win32/api/oleidl/nf-oleidl-idroptarget-drop) to the appropriate [**DROPEFFECT**](../com/dropeffect-constants.md) value. With Shell data objects, the target might also need to call [**IDataObject::SetData**](/windows/win32/api/objidl/nf-objidl-idataobject-setdata). For a discussion of how targets should respond for different data transfer scenarios, see [Handling Shell Data Transfer Scenarios](datascenarios.md).

The following sections briefly discuss how to implement the [**IDropTarget::DragEnter**](/windows/win32/api/oleidl/nf-oleidl-idroptarget-dragenter), [**IDropTarget::DragOver**](/windows/win32/api/oleidl/nf-oleidl-idroptarget-dragover), and [**IDropTarget::Drop**](/windows/win32/api/oleidl/nf-oleidl-idroptarget-drop) methods. For further details, see the reference documentation.

### DragEnter method

The system calls the [**IDropTarget::DragEnter**](/windows/win32/api/oleidl/nf-oleidl-idroptarget-dragenter) method when the cursor enters the target window. Its parameters provide the target with the location of the cursor, the state of keyboard modifier keys such as the CTRL key, and a pointer to the data object's [**IDataObject**](/windows/win32/api/objidl/nn-objidl-idataobject) interface. The target is responsible for using that interface to determine whether it can accept any of the formats contained by the data object. If it can, it normally leaves the value of *pdwEffect* unchanged. If it cannot accept any data from the data object, it sets the *pdwEffect* parameter to DROPEFFECT\_NONE. The system passes the value of this parameter to the data object's [**IDropSource**](/windows/win32/api/oleidl/nn-oleidl-idropsource) interface to allow it to display the appropriate drag image.

Targets should not use the [**IDataObject::GetData**](/windows/win32/api/objidl/nf-objidl-idataobject-getdata) method to render Shell data before it has been dropped. Fully rendering the object's data for each such occurrence might cause the drag cursor to stall. To avoid this problem, some Shell objects contain a [CFSTR\_INDRAGLOOP](clipboard.md) format. By extracting this format, targets can check the status of the drag loop while avoiding memory intensive rendering of the object's data. The format's data value is a **DWORD** that is set to a nonzero value if the data object is within a drag loop. The format's data value is set to zero if the data has been dropped.

If the target can accept data from the data object, it should examine **grfKeyState** to determine whether any modifier keys have been pressed to modify the normal drop behavior. For instance, the default operation is typically a move, but depressing the CTRL key usually indicates a copy operation.

While the cursor is over the target window, the target can use the [drag-and-drop helper object](#using-the-drag-and-drop-helper-object) to replace the data object's drag image with its own. If so, [**IDropTarget::DragEnter**](/windows/win32/api/oleidl/nf-oleidl-idroptarget-dragenter) should call [**IDropTargetHelper::DragEnter**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-idroptargethelper-dragenter) to pass the information contained in the *DragEnter* parameters to the drag-and-drop helper object.

### DragOver method

As the cursor moves within the target window, the system periodically calls the [**IDropTarget::DragOver**](/windows/win32/api/oleidl/nf-oleidl-idroptarget-dragover) method. Its parameters provide the target with the location of the cursor and the state of keyboard modifier keys such as the CTRL key. **IDropTarget::DragOver** has much the same responsibilities as [**IDropTarget::DragEnter**](/windows/win32/api/oleidl/nf-oleidl-idroptarget-dragenter), and the implementations are usually very similar.

If the target is using the drag-and-drop helper object, [**IDropTarget::DragOver**](/windows/win32/api/oleidl/nf-oleidl-idroptarget-dragover) should call [**IDropTargetHelper::DragOver**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-idroptargethelper-dragover) to forward the information contained in the *DragOver* parameters to the drag-and-drop helper object.

### Drop method

The system calls the [**IDropTarget::Drop**](/windows/win32/api/oleidl/nf-oleidl-idroptarget-drop) method to notify the target that the user has dropped the data, typically by releasing the mouse button. **IDropTarget::Drop** has the same parameters as [**IDropTarget::DragEnter**](/windows/win32/api/oleidl/nf-oleidl-idroptarget-dragenter). The target normally responds by extracting one or more formats from the data object. When finished, the target should set the *pdwEffect* parameter to a [**DROPEFFECT**](../com/dropeffect-constants.md) value that indicates the outcome of the operation. For some types of Shell data transfer, the target must also call [**IDataObject::SetData**](/windows/win32/api/objidl/nf-objidl-idataobject-setdata) to pass a format with additional information on the outcome of the operation to the data object. For a detailed discussion, see [Handling Shell Data Transfer Scenarios](datascenarios.md).

If the target is using the drag-and-drop helper object, [**IDropTarget::Drop**](/windows/win32/api/oleidl/nf-oleidl-idroptarget-drop) should call [**IDropTargetHelper::Drop**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-idroptargethelper-drop) to forward the information contained in the [**IDropTargetHelper::DragOver**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-idroptargethelper-dragover) parameters to the drag-and-drop helper object.

## Using the Drag-and-Drop Helper Object

The drag-and-drop helper object (CLSID\_DragDropHelper) is exported by the Shell to allow targets to specify the drag image while it is over the target window. To use the drag-and-drop helper object, create an in-process server object by calling [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) with a class identifier (CLSID) of CLSID\_DragDropHelper. The drag-and-drop helper object exposes two interfaces that are used in the following way:

- The [**IDragSourceHelper**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-idragsourcehelper) interface allows the drop target to specify an icon to represent the data object.
- The [**IDropTargetHelper**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-idroptargethelper) interface allows the drop target to inform the drag-and-drop helper object of the cursor location, and to show or hide the data icon.

### Using the IDragSourceHelper Interface

The [**IDragSourceHelper**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-idragsourcehelper) interface is exposed by the drag-and-drop helper object to allow a drop target to provide the image that will be displayed while the cursor is over the target window. **IDragSourceHelper** provides two alternative ways to specify the bitmap to be used as a drag image:

- Drop targets that have a window can register a DI\_GETDRAGIMAGE window message for it by initializing the drag-and-drop helper object with [**IDragSourceHelper::InitializeFromWindow**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-idragsourcehelper-initializefromwindow). When the target receives a DI\_GETDRAGIMAGE message, the handler puts the drag image bitmap information in the [**SHDRAGIMAGE**](/windows/desktop/api/Shobjidl_core/ns-shobjidl_core-shdragimage) structure that is passed as the message's *lParam* value.
- Windowless drop targets specify a bitmap when they initialize the drag-and-drop helper object with [**IDragSourceHelper::InitializeFromBitmap**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-idragsourcehelper-initializefrombitmap).

### Using the IDropTargetHelper Interface

This interface allows the drop target to notify the drag-and-drop helper object when the cursor enters or leaves the target. While the cursor is over the target window, [**IDropTargetHelper**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-idroptargethelper) allows the target to give the drag-and-drop helper object the information that the target receives through its [**IDropTarget**](/windows/win32/api/oleidl/nn-oleidl-idroptarget) interface.

Four of the [**IDropTargetHelper**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-idroptargethelper) methods—[**IDropTargetHelper::DragEnter**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-idroptargethelper-dragenter), [**IDropTargetHelper::DragLeave**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-idroptargethelper-dragleave), [**IDropTargetHelper::DragOver**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-idroptargethelper-dragover), and [**IDropTargetHelper::Drop**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-idroptargethelper-drop)—are associated with the [**IDropTarget**](/windows/win32/api/oleidl/nn-oleidl-idroptarget) method of the same name. To use the drag-and-drop helper object, each of the **IDropTarget** methods should call the corresponding **IDropTargetHelper** method to forward the information to the drag-and-drop helper object. The fifth **IDropTargetHelper** method, [**IDropTargetHelper::Show**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-idroptargethelper-show), notifies the drag-and-drop helper object to show or hide the drag image. This method is used when dragging over a target window in a low color-depth video mode. It allows the target to hide the drag image while it is painting the window.

 

 
