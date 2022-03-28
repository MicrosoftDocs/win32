---
description: The procedure for implementing a namespace extension is similar to that for any other in-process Component Object Model (COM) object.
title: Implementing the Basic Folder Object Interfaces
ms.topic: article
ms.date: 05/31/2018
ms.assetid: a45b8011-5355-429b-8935-4a7bdb5d2316
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# Implementing the Basic Folder Object Interfaces

The procedure for implementing a namespace extension is similar to that for any other in-process Component Object Model (COM) object. All extensions must support three primary interfaces that provide Windows Explorer with the basic information needed to display the extension's folders in the tree view. However, to make full use of the capabilities of Windows Explorer, your extension must also expose one or more optional interfaces that support more sophisticated features, such as shortcut menus or drag-and-drop, and provide a folder view.

This document discusses how to implement the primary and optional interfaces that Windows Explorer calls for information about the contents of your extension. For a discussion of how to implement a folder view and how to customize Windows Explorer, see [Implementing a Folder View](../lwef/nse-folderview.md).

- [Basic Implementation and Registration](#basic-implementation-and-registration)
    - [Registering an Extension](#registering-an-extension)
- [Handling PIDLs](#handling-pidls)
    - [Creating an SHITEMID Structure](#creating-an-shitemid-structure)
    - [Constructing a PIDL](#constructing-a-pidl)
    - [Interpreting PIDLs](#interpreting-pidls)
- [Implementing the Primary Interfaces](#implementing-the-primary-interfaces)
    - [IPersistFolder Interface](#ipersistfolder-interface)
    - [IShellFolder Interface](#ishellfolder-interface)
    - [IEnumIDList Interface](#ienumidlist-interface)
- [Implementing the Optional Interfaces](#implementing-the-optional-interfaces)
    - [IExtractIcon](#iextracticon)
    - [IContextMenu](#icontextmenu)
    - [IQueryInfo](#iqueryinfo)
    - [IDataObject and IDropTarget](#idataobject-and-idroptarget)
- [Working With the Default Shell Folder View Implementation](#working-with-the-default-shell-folder-view-implementation)

## Basic Implementation and Registration

As an in-process COM server, your DLL must expose several standard functions and interfaces:

- [**DllCanUnloadNow**](/windows/win32/api/combaseapi/nf-combaseapi-dllcanunloadnow)
- [**DllGetClassObject**](/windows/win32/api/combaseapi/nf-combaseapi-dllgetclassobject)
- [**IClassFactory**](/windows/win32/api/unknwn/nn-unknwn-iclassfactory)
- [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown)

These functions and interfaces are implemented in the same way as they are for most other COM objects. For details, see the [COM documentation](../com/the-component-object-model.md).

### Registering an Extension

As with all COM objects, you must create a class identifier (CLSID) GUID for your extension. Register the object by creating a subkey of **HKEY\_CLASSES\_ROOT**\\**CLSID** named for the CLSID of your extension. The DLL should be registered as an in-process server and should specify the apartment threading model. You can customize the behavior of an extension's root folder by adding a variety of subkeys and values to the extension's CLSID key.

Several of these values apply only to extensions with virtual junction points. These values do not apply to extensions whose junction points are file system folders. For further discussion, see [Specifying a Namespace Extension's Location](nse-junction.md). To modify the behavior of an extension with a virtual junction point, add one or more of the following values to the extension's CLSID key:

-   WantsFORPARSING. The parsing name for an extension with a virtual junction point will normally have the form ::{*GUID*}. Extensions of this type normally contain virtual items. However, some extensions, such as My Documents, actually correspond to file system folders, even though they have virtual junction points. If your extension represents file system objects in this way, you can set the WantsFORPARSING value. Windows Explorer will then request your root folder's parsing name by calling the folder object's [**IShellFolder::GetDisplayNameOf**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-getdisplaynameof) method with *uFlags* set to **SHGDN\_FORPARSING** and *pidl* set to a single empty pointer to an item identifier list (PIDL). An empty PIDL contains only a terminator. Your method should then return the root folder's ::{*GUID*} parsing name.
-   HideFolderVerbs. The verbs registered under **HKEY\_CLASSES\_ROOT**\\**Folder** normally are associated with all extensions. They appear on the extension's shortcut menu and can be invoked by [**ShellExecute**](/windows/desktop/api/Shellapi/nf-shellapi-shellexecutea). To prevent any of these verbs from being associated with your extension, set the HideFolderVerbs value.
-   HideAsDelete. If a user attempts to delete your extension, Windows Explorer will instead hide the extension.
-   HideAsDeletePerUser. This value has the same effect as HideAsDelete but on a per-user basis. The extension is hidden only for those users who have attempted to delete it. The extension is visible to all other users.
-   QueryForOverlay. Set this value to indicate that the root folder's icon can have an icon overlay. The folder object must support the [**IShellIconOverlay**](/windows/win32/api/shlobj_core/nn-shlobj_core-ishelliconoverlay) interface. Before Windows Explorer displays the root folder's icon, it will request an overlay icon by calling one of the two **IShellIconOverlay** methods with *pidlItem* set to an empty PIDL.

The remaining values and subkeys apply to all extensions:

-   To specify the display name of the extension's junction point folder, set the default value of the extension's CLSID subkey to an appropriate string.
-   When the cursor hovers over a folder, an infotip is typically displayed that describes the contents of the folder. To provide an infotip for your extension's root folder, create an InfoTip **REG\_SZ** value for the extension's CLSID key, and set it to an appropriate string.
-   To specify a custom icon for your extension's root folder, create a subkey of the extension's CLSID subkey named **DefaultIcon**. Set the default value of **DefaultIcon** to a **REG\_SZ** value containing the name of the file that contains the icon, followed by a comma, followed by a minus sign, followed by the index of the icon in that file.
-   By default, the shortcut menu of your extension's root folder will contain the items defined under **HKEY\_CLASSES\_ROOT\\Folder**. The **Delete**, **Rename**, and **Properties** items are added if you have set the appropriate SFGAO\_XXX flags. You can add other items to the root folder's shortcut menu, or override existing items, much as you would for a [file type](fa-file-types.md). Create a **Shell** subkey under the extension's CLSID key, and define commands as discussed in [Extending Shortcut Menus](context.md).
-   If you need a more flexible way to handle the root folder's shortcut menu, you can implement a [shortcut menu handler](context-menu-handlers.md). To register the shortcut menu handler, create a **ShellEx** key under the extension's CLSID key. Register the handler's CLSID as you would for a conventional [Creating Shell Extension Handlers](handlers.md).
-   To add a page to the root folder's Properties property sheet, give the folder the **SFGAO\_HASPROPSHEET** attribute and implement a [property sheet handler](propsheet-handlers.md). To register the property sheet handler, create a **ShellEx** key under the extension's CLSID key. Register the handler's CLSID as you would for a conventional [Creating Shell Extension Handlers](handlers.md).
-   To specify the attributes of the root folder, add a **ShellFolder** subkey to the extension's CLSID subkey. Create an Attributes value, and set it to the appropriate combination of [**SFGAO\_XXX**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-getattributesof) flags.

The following table lists some commonly used attributes for root folders.



| Flag                | Value      | Description                                                                                                                                                                                                                                                                                                       |
|---------------------|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SFGAO\_FOLDER       | 0x20000000 | The extension's root folder contains one or more items.                                                                                                                                                                                                                                                           |
| SFGAO\_HASSUBFOLDER | 0x80000000 | The extension's root folder contains one or more subfolders. Windows Explorer will place a plus sign ( + ) next to the folder icon.                                                                                                                                                                               |
| SFGAO\_CANDELETE    | 0x00000020 | The extension's root folder can be deleted by the user. The folder's shortcut menu will have a **Delete** item. This flag should be set for junction points that are placed under one of the [virtual folders](nse-junction.md).                                                                                 |
| SFGAO\_CANRENAME    | 0x00000010 | The extension's root folder can be renamed by the user. The folder's shortcut menu will have a **Rename** item.                                                                                                                                                                                                   |
| SFGAO\_HASPROPSHEET | 0x00000040 | The extension's root folder has a **Properties** property sheet. The folder's shortcut menu will have a **Properties** item. To provide the property sheet, you must implement a [property sheet handler](propsheet-handlers.md). Register the handler under the extension's CLSID key, as discussed previously. |



 

The following example shows the CLSID registry entry for an extension with a display name of MyExtension. The extension has a custom icon that is contained in the extension's DLL with an index of 1. The **SFGAO\_FOLDER**, **SFGAO\_HASSUBFOLDER**, and **SFGAO\_CANDELETE** attributes are set.

```
HKEY_CLASSES_ROOT
   CLSID
      {Extension CLSID}
         (Default) = MyExtension
         InfoTip = Some appropriate text
      DefaultIcon
         (Default) = c:\MyDir\MyExtension.dll,-1
      InProcServer32
         (Default) = c:\MyDir\MyExtension.dll
         ThreadingModel = Apartment
      ShellFolder
         Attributes = 0xA00000020
```

## Handling PIDLs

Every item in the Shell namespace must have a unique PIDL. Windows Explorer assigns a PIDL to your root folder and passes the value to your extension during initialization. Your extension is then responsible for assigning a properly constructed PIDL to each of its objects and providing those PIDLs to Windows Explorer on request. When the Shell uses a PIDL to identify one of your extension's objects, your extension must be able to interpret the PIDL and identify the particular object. Your extension must also assign a [**display name**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-setnameof) and a *parsing name* to each object. Because PIDLs are used by virtually every folder interface, extensions commonly implement a single *PIDL manager* to handle all these tasks.

The term PIDL is short for an [**ITEMIDLIST**](/windows/desktop/api/Shtypes/ns-shtypes-itemidlist) structure or a pointer to such a structure, depending on context. As declared, an **ITEMIDLIST** structure has a single member, an [**SHITEMID**](/windows/desktop/api/Shtypes/ns-shtypes-shitemid) structure. An object's **ITEMIDLIST** structure is actually a packed array of two or more **SHITEMID** structures. The order of these structures defines a path through the namespace, in much the same way that c:\\MyDirectory\\MyFile defines a path through the file system. Typically, an object's PIDL will consist of a series of **SHITEMID** structures that correspond to the folders that define the namespace path, followed by the object's **SHITEMID** structure, followed by a terminator.

The terminator is an [**SHITEMID**](/windows/desktop/api/Shtypes/ns-shtypes-shitemid) structure, with the *cb* member set to **NULL**. The terminator is necessary because the number of **SHITEMID** structures in an object's PIDL depends on the location of the object in the Shell namespace, and the starting point of the path. In addition, the size of the various **SHITEMID** structures can vary. When you receive a PIDL, you have no simple way of determining its size or even the total number of **SHITEMID** structures. Instead, you must "walk" the packed array, structure by structure, until you reach the terminator.

To create a PIDL, your application needs to:

1.  Create an [**SHITEMID**](/windows/desktop/api/Shtypes/ns-shtypes-shitemid) structure for each of its objects.
2.  Assemble the relevant [**SHITEMID**](/windows/desktop/api/Shtypes/ns-shtypes-shitemid) structures into a PIDL.

### Creating an SHITEMID Structure

An object's [**SHITEMID**](/windows/desktop/api/Shtypes/ns-shtypes-shitemid) structure uniquely identifies the object within its folder. In fact, a type of PIDL used by many of the [**IShellFolder**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishellfolder) methods consists of just the object's **SHITEMID** structure, followed by a terminator. The definition of an **SHITEMID** structure is:


```C++
typedef struct _SHITEMID { 
    USHORT cb; 
    BYTE   abID[1]; 
} SHITEMID, * LPSHITEMID;
```



The *abID* member is the object's identifier. Because the length of *abID* is not defined and can vary, the *cb* member is set to the size of the [**SHITEMID**](/windows/desktop/api/Shtypes/ns-shtypes-shitemid) structure, in bytes.

Because neither the length nor the content of *abID* is standardized, you can use any scheme you want to assign *abID* values to your objects. The only requirement is that you cannot have two objects in the same folder with identical values. However, for performance reasons, your [**SHITEMID**](/windows/desktop/api/Shtypes/ns-shtypes-shitemid) structure should be **DWORD**-aligned. In other words, you should construct your *abID* values such that *cb* is an integral multiple of 4.

Typically, *abID* points to an extension-defined structure. In addition to the object's ID, this structure is often used to hold a variety of related information, such as the object's type or attributes. Your extension's folder objects can then quickly extract the information from the PIDL instead of having to query for it.

> [!Note]  
> One of the most important aspects of designing a data structure for a PIDL is to make the structure persistable and transportable. In the context of PIDLs, the meaning of these terms is:
>
> -   Persistable. The system frequently places PIDLs in various types of long-term storage, such as shortcut files. It can then recover these PIDLs from storage later, possibly after the system has been rebooted. A PIDL that has been recovered from storage must still be valid and meaningful to your extension. This requirement means, for instance, that you should not use pointers or handles in your PIDL structure. PIDLs containing this type of data will normally be meaningless when the system later recovers them from storage.
> -   Transportable. A PIDL must remain meaningful when transported from one computer to another. For example, a PIDL can be written to a shortcut file, copied to a floppy disk, and transported to another computer. That PIDL should still be meaningful to your extension running on the second computer. For instance, to ensure that your PIDLs are transportable, use either ANSI or Unicode characters explicitly. Avoid data types such as **TCHAR** or **LPTSTR**. If you use those data types, a PIDL created on a computer running a Unicode version of your extension will not be readable by an ANSI version of that extension running on a different computer.

 

The following declaration shows a simple example of a data structure.


```C++
typedef struct tagMYPIDLDATA {
  USHORT cb;
  DWORD dwType;
  WCHAR wszDisplayName[40];
} MYPIDLDATA, *LPMYPIDLDATA;
```



The **cb** member is set to the size of the **MYPIDLDATA** structure. This member makes **MYPIDLDATA** a valid [**SHITEMID**](/windows/desktop/api/Shtypes/ns-shtypes-shitemid) structure, in and of itself. The rest of the members are equivalent to the **abID** member of an **SHITEMID** structure and hold private data. The **dwType** member is an extension-defined value that indicates the type of object. For this example, **dwType** is set to **TRUE** for folders and **FALSE** otherwise. This member allows you, for instance, to quickly determine whether the object is a folder or not. The **wszDisplayName** member contains the object's display name. Since you would not assign the same display name to two different objects in the same folder, the display name also serves as the object ID. In this example, **wszDisplayName** is set to 40 characters to guarantee that the **SHITEMID** structure will be **DWORD**-aligned. To limit the size of your PIDLs, you can instead use a variable-length character array and adjust the value of cb accordingly. Pad the display string with enough '\\0' characters to maintain the structure's **DWORD** alignment. Other members that might be useful to put in the structure include the object's size, attributes, or parsing name.

### Constructing a PIDL

Once you have defined [**SHITEMID**](/windows/desktop/api/Shtypes/ns-shtypes-shitemid) structures for your objects, you can then use them to construct a PIDL. PIDLs can be constructed for a variety of purposes, but most tasks use one of two types of PIDL. The simplest, a single-level PIDL, identifies the object relative to its parent folder. This type of PIDL is used by many of the [**IShellFolder**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishellfolder) methods. A single-level PIDL contains the object's **SHITEMID** structure, followed by a terminator. A fully qualified PIDL defines a path through the namespace hierarchy from the desktop to the object. This type of PIDL starts at the desktop and contains one **SHITEMID** structure for each folder in the path, followed by the object and the terminator. A fully qualified PIDL uniquely identifies the object within the entire Shell namespace.

The simplest way to construct a PIDL is to work directly with the [**ITEMIDLIST**](/windows/desktop/api/Shtypes/ns-shtypes-itemidlist) structure itself. Create an **ITEMIDLIST** structure, but allocate enough memory to hold all the [**SHITEMID**](/windows/desktop/api/Shtypes/ns-shtypes-shitemid) structures. The address of this structure will point to the initial **SHITEMID** structure. Define values for the members of this initial structure, and then append as many additional **SHITEMID** structures as you need, in the appropriate order. The following procedure outlines how to create a single-level PIDL. It contains two **SHITEMID** structures—a **MYPIDLDATA** structure followed by a terminator:

1.  Use the [**CoTaskMemAlloc**](/windows/win32/api/combaseapi/nf-combaseapi-cotaskmemalloc) function to allocate memory for the PIDL. Allocate enough memory for your private data plus a **USHORT** (two bytes) for the terminator. Cast the result to LPMYPIDLDATA.
2.  Set the cb member of the first **MYPIDLDATA** structure to the size of that structure. For this example, you would set **cb** to sizeof(MYPIDLDATA). If you want to use a variable-length structure, you will have to calculate the value of **cb**.
3.  Assign appropriate values to the private data members.
4.  Calculate the address of the next [**SHITEMID**](/windows/desktop/api/Shtypes/ns-shtypes-shitemid) structure. Cast the address of the current MYPIDLDATA structure to LPBYTE, and add that value to the value of **cb** determined in step 3.
5.  In this case, the next [**SHITEMID**](/windows/desktop/api/Shtypes/ns-shtypes-shitemid) structure is the terminator. Set the structure's **cb** member to zero.

For longer PIDLs, allocate sufficient memory and repeat steps 3-5 for each additional [**SHITEMID**](/windows/desktop/api/Shtypes/ns-shtypes-shitemid) structure.

The following sample function takes an object's type and display name and returns the object's single-level PIDL. The function assumes that the display name, including its terminating **null** character, does not exceed the number of characters declared for the **MYPIDLDATA** structure. If that assumption turns out to be erroneous, the [**StringCbCopyW**](/windows/win32/api/strsafe/nf-strsafe-stringcbcopya) function will truncate the display name. The **g\_pMalloc** variable is an [**IMalloc**](/windows/win32/api/objidlbase/nn-objidlbase-imalloc) pointer created elsewhere and stored in a global variable.


```C++
LPITEMIDLIST CreatePIDL(DWORD dwType, LPCWSTR pwszDisplayName)
{
    LPMYPIDLDATA   pidlOut;
    USHORT         uSize;

    pidlOut = NULL;

    //Calculate the size of the MYPIDLDATA structure.
    uSize = sizeof(MYPIDLDATA);

    // Allocate enough memory for the PIDL to hold a MYPIDLDATA structure 
    // plus the terminator
    pidlOut = (LPMYPIDLDATA)m_pMalloc->Alloc(uSize + sizeof(USHORT));

    if(pidlOut)
    {
       //Assign values to the members of the MYPIDLDATA structure
       //that is the PIDL's first SHITEMID structure
       pidlOut->cb = uSize;
       pidlOut->dwType = dwType;
       hr = StringCbCopyW(pidlOut->wszDisplayName, 
                          sizeof(pidlOut->wszDisplayName), pwszDisplayName);
       
       // TODO: Add error handling here to verify the HRESULT returned 
       // by StringCbCopyW.

       //Advance the pointer to the start of the next SHITEMID structure.
       pidlOut = (LPMYPIDLDATA)((LPBYTE)pidlOut + pidlOut->cb);

       //Create the terminating null character by setting cb to 0.
       pidlOut->cb = 0;
    }

    return pidlOut;
```



A fully qualified PIDL must have [**SHITEMID**](/windows/desktop/api/Shtypes/ns-shtypes-shitemid) structures for every object from the desktop to your object. Your extension receives a fully qualified PIDL for your root folder when the Shell calls [**IPersistFolder::Initialize**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ipersistfolder-initialize). To construct a fully qualified PIDL for an object, take the PIDL that the Shell has assigned to your root folder, and append the **SHITEMID** structures that are needed to take you from the root folder to the object.

### Interpreting PIDLs

When the Shell or an application calls one of your extension's interfaces to request information about an object, it will usually identify the object by a PIDL. Some methods, such as [**IShellFolder::GetUIObjectOf**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-getuiobjectof), use PIDLs that are relative to the parent folder and are straightforward to interpret. However, your extension will probably also receive fully qualified PIDLs. Your PIDL manager must then determine which of your objects that PIDL is referring to.

What complicates the task of associating an object with a fully qualified PIDL is that one or more of the initial [**SHITEMID**](/windows/desktop/api/Shtypes/ns-shtypes-shitemid) structures in the PIDL might belong to objects that lie outside your extension in the Shell namespace. You have no way of interpreting the meaning of the *abID* member of those structures. What your extension must do is to "walk" the list of **SHITEMID** structures, until you reach the structure that corresponds to your root folder. From then on, you will know how to interpret the information in the **SHITEMID** structures.

To walk the PIDL, take the first *cb* value and add it to the address of the PIDL to advance the pointer to the start of the next [**SHITEMID**](/windows/desktop/api/Shtypes/ns-shtypes-shitemid) structure. It then will be pointing to that structure's *cb* member, which you can use to advance the pointer to the start of the next **SHITEMID** structure, and so on. Each time you advance the pointer, examine the **SHITEMID** structure to determine whether you have reached the root of your extension's namespace.

## Implementing the Primary Interfaces

As with all COM objects, implementing an extension is largely a matter of implementing a collection of interfaces. This section discusses the three primary interfaces that must be implemented by all extensions. They are used for initialization and to provide Windows Explorer with basic information about the contents of the extension. These interfaces, plus a [folder view](../lwef/nse-folderview.md), are all that is required for a functional extension. However, to fully exploit the features of Windows Explorer, most extensions also implement one or more of the optional interfaces.

### IPersistFolder Interface

The [**IPersistFolder**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ipersistfolder) interface is called to initialize a new folder object. The [**IPersistFolder::Initialize**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ipersistfolder-initialize) method assigns a fully qualified PIDL to the new object. Store this PIDL for later use. For instance, a folder object must use this PIDL to construct fully qualified PIDLs for the object's children. The folder object's creator can also call [**IPersist::GetClassID**](/windows/win32/api/objidl/nf-objidl-ipersist-getclassid) to request the object's CLSID.

Typically, a folder object is created and initialized by its parent folder's [**IShellFolder::BindToObject**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-bindtoobject) method. However, when a user browses into your extension, Windows Explorer creates and initializes the extension's root folder object. The PIDL that the root folder object receives through [**IPersistFolder::Initialize**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ipersistfolder-initialize) contains the path from the desktop to the root folder that you will need to construct fully qualified PIDLs for your extension.

### IShellFolder Interface

The Shell treats an extension as a hierarchically ordered collection of folder objects. The [**IShellFolder**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishellfolder) interface is the core of any extension implementation. It represents a folder object and provides Windows Explorer with much of the information needed to display the contents of the folder.

[**IShellFolder**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishellfolder) is typically the only folder interface other than [**IPersistFolder**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ipersistfolder) that is directly exposed by a folder object. While Windows Explorer uses a variety of required and optional interfaces to obtain information about the contents of the folder, it obtains pointers to those interfaces through **IShellFolder**.

Windows Explorer obtains the CLSID of your extension's root folder in a variety of ways. For details, see [Specifying a Namespace Extension's Location](nse-junction.md) or [Displaying a Self-Contained View of a Namespace Extension](nse-view.md). Windows Explorer then uses that CLSID to create and initialize an instance of the root folder and query for an [**IShellFolder**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishellfolder) interface. Your extension creates a folder object to represent the root folder and returns the object's **IShellFolder** interface. Much of the remainder of the interaction between your extension and Windows Explorer then takes place through **IShellFolder**. Windows Explorer calls **IShellFolder** to:

-   Request an object that can enumerate the contents of the root folder.
-   Obtain various types of information about the contents of the root folder.
-   Request an object that exposes one of the optional interfaces. Those interfaces can then be queried for additional information, such as icons or shortcut menus.
-   Request a folder object that represents a subfolder of the root folder.

When a user opens a subfolder of the root folder, Windows Explorer calls [**IShellFolder::BindToObject**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-bindtoobject). Your extension creates and initializes a new folder object to represent the subfolder and returns its [**IShellFolder**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishellfolder) interface. Windows Explorer then calls this interface for various types of information, and so on until the user decides to navigate elsewhere in the Shell namespace or close Windows Explorer.

The remainder of this section briefly discusses the more important [**IShellFolder**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishellfolder) methods and how to implement them.

### EnumObjects

Before displaying the contents of a folder in the tree view, Windows Explorer must first determine what the folder contains by calling the [**IShellFolder::EnumObjects**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-enumobjects) method. This method creates a standard OLE enumeration object that exposes an [**IEnumIDList**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ienumidlist) interface and returns that interface pointer. The **IEnumIDList** interface allows Windows Explorer to obtain the PIDLs of all the objects contained by the folder. These PIDLs are then used to obtain information about the objects contained by the folder. For further details, see [IEnumIDList Interface](#ienumidlist-interface).

> [!Note]  
> The [**IEnumIDList::Next**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ienumidlist-next) method should only return PIDLs that are relative to the parent folder. The PIDL should contain only the object's [**SHITEMID**](/windows/desktop/api/Shtypes/ns-shtypes-shitemid) structure, followed by a terminator.

 

### CreateViewObject

Before the contents of a folder are displayed, Windows Explorer calls this method to request a pointer to an [**IShellView**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellview) interface. This interface is used by Windows Explorer to manage the folder view. Create a folder view object and return its **IShellView** interface.

The [**IShellFolder::CreateViewObject**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-createviewobject) method is also called to request one of the optional interfaces, such as [**IContextMenu**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-icontextmenu), for the folder itself. Your implementation of this method should create an object that exposes the requested interface and returns the interface pointer. If Windows Explorer needs an optional interface for one of the objects contained by the folder, it will call [**IShellFolder::GetUIObjectOf**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-getuiobjectof).

### GetUIObjectOf

While basic information about the contents of a folder is available through the [**IShellFolder**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishellfolder) methods, your extension can also provide Windows Explorer with various kinds of additional information. For instance, you can specify icons for the contents of a folder or an object's shortcut menu. Windows Explorer calls the [**IShellFolder::GetUIObjectOf**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-getuiobjectof) method to attempt to retrieve additional information about an object that is contained by a folder. Windows Explorer specifies which object it wants the information for, and the IID of the relevant interface. The folder object then creates an object that exposes the requested interface and returns the interface pointer.

If your extension allows users to transfer objects with drag-and-drop or the clipboard, Windows Explorer will call [**IShellFolder::GetUIObjectOf**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-getuiobjectof) to request an [**IDataObject**](/windows/win32/api/objidl/nn-objidl-idataobject) or [**IDropTarget**](/windows/win32/api/oleidl/nn-oleidl-idroptarget) interface. For details, see [Transferring Shell Objects with Drag-and-Drop and the Clipboard](dragdrop.md).

Windows Explorer calls [**IShellFolder::CreateViewObject**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-createviewobject) when it wants the same sort of information about the folder itself.

### BindToObject

Windows Explorer calls the [**IShellFolder::BindToObject**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-bindtoobject) method when a user attempts to open one of your extension's subfolders. If *riid* is set to IID\_IShellFolder, you should create and initialize a folder object that represents the subfolder and return the object's [**IShellFolder**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishellfolder) interface.

> [!Note]  
> At present, Windows Explorer calls this method only to request an [**IShellFolder**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishellfolder) interface. However, do not assume that this will always be the case. You should always check the value of *riid* before proceeding.

 

### GetDisplayNameOf

Windows Explorer calls the [**IShellFolder::GetDisplayNameOf**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-getdisplaynameof) method to convert the PIDL of one of the folder's objects into a name. That PIDL must be relative to the object's parent folder. In other words, it must contain a single non-**NULL** [**SHITEMID**](/windows/desktop/api/Shtypes/ns-shtypes-shitemid) structure. Because there is more than one possible way to name objects, Windows Explorer specifies the type of name by setting one or more [**SHGDNF**](/windows/win32/api/shobjidl_core/ne-shobjidl_core-_shgdnf) flags in the *uFlags* parameter. One of two values, **SHGDN\_NORMAL** or **SHGDN\_INFOLDER**, will be set to specify whether the name should be relative to the folder or relative to the desktop. One of the other three values, **SHGDN\_FOREDITING**, **SHGDN\_FORADDRESSBAR**, or **SHGDN\_FORPARSING**, can be set to specify what the name will be used for.

You must return the name in the form of an [**STRRET**](/windows/desktop/api/Shtypes/ns-shtypes-strret) structure. If **SHGDN\_FOREDITING**, **SHGDN\_FORADDRESSBAR**, and **SHGDN\_FORPARSING** are not set, return the object's display name. If the **SHGDN\_FORPARSING** flag is set, Windows Explorer is requesting a parsing name. Parsing names are passed to [**IShellFolder::ParseDisplayName**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-parsedisplayname) to obtain an object's PIDL, even though it might be located one or more levels below the current folder in the namespace hierarchy. For example, the parsing name of a file system object is its path. You can pass the fully qualified path of any object in the file system to the desktop's **IShellFolder::ParseDisplayName** method, and it will return the object's fully qualified PIDL.

While parsing names are text strings, they do not necessarily have to include the display name. You should assign parsing names based on what will work most efficiently when [**IShellFolder::ParseDisplayName**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-parsedisplayname) is called. For instance, many of the Shell's virtual folders are not part of the file system and do not have a fully qualified path. Instead, each folder is assigned a GUID and the parsing name takes the form ::{GUID}. Regardless of what scheme you use, it should be able to reliably "round trip." For instance, if a caller passes a parsing name to **IShellFolder::ParseDisplayName** to retrieve an object's PIDL, and then passes that PIDL to [**IShellFolder::GetDisplayNameOf**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-getdisplaynameof) with the **SHGDN\_FORPARSING** flag set, the caller should recover the original parsing name.

### GetAttributesOf

Windows Explorer calls the [**IShellFolder::GetAttributesOf**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-getattributesof) method to determine the attributes of one or more items contained by a folder object. The value of *cidl* gives the number of items in the query, and *aPidl* points to a list of their PIDLs.

Because testing for some attributes can be time consuming, Windows Explorer typically restricts the query to a subset of the available flags by setting their values in *rfgInOut*. Your method should test for only those attributes whose flags are set in *rfgInOut*. Leave the valid flags set and clear the remainder. If more than one item is included in the query, set only those flags that apply to all items.

> [!Note]  
> The attributes must be properly set for an item to be correctly displayed. For instance, if an item is a folder that contains subfolders, you must set the **SFGAO\_HASSUBFOLDER** flag. Otherwise, Windows Explorer will not display a + next to the item's icon in the tree view.

 

### ParseDisplayName

The [**IShellFolder::ParseDisplayName**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-parsedisplayname) method is in some sense a mirror image of [**IShellFolder::GetDisplayNameOf**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-getdisplaynameof). The most common use of this method is to convert an object's parsing name into the associated PIDL. The parsing name can refer to any object that lies below the folder in the namespace hierarchy. The returned PIDL is relative to the folder object that exposes the method and is usually not fully qualified. In other words, although the PIDL can contain several [**SHITEMID**](/windows/desktop/api/Shtypes/ns-shtypes-shitemid) structures, the first will either be that of the object itself or the first subfolder in the path from the folder to the object. The caller will have to append this PIDL to the folder's fully qualified PIDL to obtain a fully qualified PIDL for the object.

[**IShellFolder::ParseDisplayName**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-parsedisplayname) can also be called to request an object's attributes. Because determining all the applicable attributes can be time consuming, the caller will set only those [**SFGAO\_XXX**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-getattributesof) flags that represent information that the caller is interested in. You should determine which of those attributes are true for the object, and clear the remaining flags.

### IEnumIDList Interface

When Windows Explorer needs to enumerate the objects that are contained by a folder, it calls [**IShellFolder::EnumObjects**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-enumobjects). The folder object must create an enumeration object that exposes the [**IEnumIDList**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ienumidlist) interface and return that interface pointer. Windows Explorer will then typically use **IEnumIDList** to enumerate the PIDLs of all the objects contained by the folder.

[**IEnumIDList**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ienumidlist) is a standard OLE enumeration interface and is implemented in the usual way. Remember, however, that the PIDLs that you return must be relative to the folder and contain only the object's [**SHITEMID**](/windows/desktop/api/Shtypes/ns-shtypes-shitemid) structure and a terminator.

## Implementing the Optional Interfaces

There are a number of optional Shell interfaces that your extension's folder objects can support. Many of them, such as [**IExtractIcon**](/windows/win32/api/shlobj_core/nn-shlobj_core-iextracticona), allow you to customize various aspects of the way the user views your extension. Others, such as [**IDataObject**](/windows/win32/api/objidl/nn-objidl-idataobject), allow your extension to support features such as drag-and-drop.

None of the optional interfaces are exposed directly by a folder object. Instead, Windows Explorer calls one of two [**IShellFolder**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishellfolder) methods to request an interface:

-   Windows Explorer calls a folder object's [**IShellFolder::GetUIObjectOf**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-getuiobjectof) to request an interface for one of the objects contained by the folder.
-   Windows Explorer calls a folder object's [**IShellFolder::CreateViewObject**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-createviewobject) to request an interface for the folder itself.

To provide the information, the folder object creates an object that exposes the requested interface and returns the interface pointer. Windows Explorer then calls that interface to retrieve the needed information. This section discusses the most commonly used optional interfaces.

### IExtractIcon

Windows Explorer requests an [**IExtractIcon**](/windows/win32/api/shlobj_core/nn-shlobj_core-iextracticona) interface before it displays the contents of a folder. The interface allows your extension to specify custom icons for the objects that are contained by the folder. Otherwise, the standard file and folder icons will be used. To provide a custom icon, create an icon extraction object that exposes **IExtractIcon** and return a pointer to that interface. For further discussion, see the **IExtractIcon** reference documentation or [Creating Icon Handlers](./how-to-create-icon-handlers.md).

### IContextMenu

When a user right-clicks an object, Windows Explorer requests an [**IContextMenu**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-icontextmenu) interface. To provide shortcut menus for your objects, create a menu handler object and return its **IContextMenu** interface.

The procedures for creating a menu handler object are very similar to those used to create a menu handler Shell extension. For details, see [Creating Context Menu Handlers](context-menu-handlers.md) or the [**IContextMenu**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-icontextmenu), [**IContextMenu2**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-icontextmenu2), or [**IContextMenu3**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-icontextmenu3) reference.

### IQueryInfo

Windows Explorer calls the [**IQueryInfo**](/windows/win32/api/shlobj_core/nn-shlobj_core-iqueryinfo) interface to retrieve an infotip text string.

### IDataObject and IDropTarget

When your objects are displayed by Windows Explorer, a folder object has no direct way to know when a user is attempting to cut, copy, or drag an object. Instead, Windows Explorer requests an [**IDataObject**](/windows/win32/api/objidl/nn-objidl-idataobject) interface. To allow the object to be transferred, create a data object and return a pointer to its **IDataObject** interface.

Similarly, a user might attempt to drop a data object on a Windows Explorer representation of one of your objects, such as an icon or address bar path. Windows Explorer then requests an [**IDropTarget**](/windows/win32/api/oleidl/nn-oleidl-idroptarget) interface. To allow the data object to be dropped, create an object that exposes an **IDropTarget** interface and return the interface pointer.

Handling data transfer is one of the trickier aspects of writing namespace extensions. For a detailed discussion, see [Transferring Shell Objects with Drag-and-Drop and the Clipboard](dragdrop.md).

## Working With the Default Shell Folder View Implementation

Data sources that use the default Shell folder view object (DefView) must implement these interfaces:

- [**IShellFolder**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishellfolder)
- [**IShellFolder2**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellfolder2)
- [**IPersistFolder**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ipersistfolder)
- [**IPersistFolder2**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ipersistfolder2)

Optionally, they can also implement [**IPersistFolder3**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ipersistfolder3).

 

 
