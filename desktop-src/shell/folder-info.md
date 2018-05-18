---
Description: 'The Getting a Folder''s ID section discussed two approaches to getting a namespace object''s pointer to an item identifier list (PIDL).'
ms.assetid: 'c99a2f6c-3144-41ec-ad97-59a30bfec9ab'
title: Getting Information About the Contents of a Folder
---

# Getting Information About the Contents of a Folder

The [Getting a Folder's ID](folder-id.md) section discussed two approaches to getting a namespace object's pointer to an item identifier list (PIDL). One obvious question is: Once you have a PIDL, what can you do with it? A related question is: What if neither approach works, or is suitable for your application? The answer to both questions requires taking a closer look at how the namespace is implemented. The key is the [**IShellFolder**](ishellfolder.md) interface.

-   [Using the IShellFolder Interface](#using-the-ishellfolder-interface)
-   [Enumerating the Contents of a Folder](#enumerating-the-contents-of-a-folder)
-   [Determining Display Names and Other Properties](#determining-display-names-and-other-properties)
-   [Getting a Pointer to a Subfolder's IShellFolder Interface](#getting-a-pointer-to-a-subfolders-ishellfolder-interface)
-   [Determining an Object's Parent Folder](#determining-an-objects-parent-folder)

## Using the IShellFolder Interface

Earlier in this documentation, namespace folders were referred to as objects. Although, at that point, the term was used in a loose sense, it is actually true in a strict sense as well. Every namespace folder is represented by a Component Object Model (COM) object. Each folder object exposes a number of interfaces that can be used for a wide variety of tasks. Some interfaces that are optional may not be exposed by all folders. However, all folders must expose the fundamental interface, [**IShellFolder**](ishellfolder.md).

The first step in using a folder object is to retrieve a pointer to its [**IShellFolder**](ishellfolder.md) interface. In addition to providing access to the object's other interfaces, **IShellFolder** exposes a group of methods that handle a number of common tasks, several of which are discussed in this section.

To retrieve a pointer to a namespace object's [**IShellFolder**](ishellfolder.md) interface, you must first call [**SHGetDesktopFolder**](shgetdesktopfolder.md). This function returns a pointer to the **IShellFolder** interface of the namespace root, the desktop. Once you have the desktop's **IShellFolder** interface, there a variety of ways to proceed.

If you already have the PIDL of the folder you are interested in—for instance, by calling [**SHGetFolderLocation**](shgetfolderlocation.md)—you can retrieve its [**IShellFolder**](ishellfolder.md) interface by calling the desktop's [**IShellFolder::BindToObject**](ishellfolder-bindtoobject.md) method. If you have the path of a file system object, you must first obtain its PIDL by calling the desktop's [**IShellFolder::ParseDisplayName**](ishellfolder-parsedisplayname.md) method and then call **IShellFolder::BindToObject**. If neither of these approaches is applicable, you can use other **IShellFolder** methods to navigate the namespace. For more information, see [Navigating the Namespace](navigate.md).

## Enumerating the Contents of a Folder

The first thing you usually want to do with a folder is to find out what it contains. You must first call the folder's [**IShellFolder::EnumObjects**](ishellfolder-enumobjects.md) method. The folder will create a standard OLE enumeration object and return its [**IEnumIDList**](ienumidlist.md) interface. This interface exposes four standard methods—[**Clone**](ienumidlist-clone.md), [**Next**](ienumidlist-next.md), [**Reset**](ienumidlist-reset.md), and [**Skip**](ienumidlist-skip.md)—that can be used to enumerate the contents of the folder.

The basic procedure for enumerating a folder's contents is:

1.  Call the folders [**IShellFolder::EnumObjects**](ishellfolder-enumobjects.md) method to retrieve a pointer to an enumeration object's [**IEnumIDList**](ienumidlist.md) interface.
2.  Pass an unallocated PIDL to [**IEnumIDList::Next**](ienumidlist-next.md). **Next** takes care of allocating the PIDL, but the application must deallocate it when it is no longer needed. When **Next** returns, the PIDL will contain just the object's item ID and the terminating **NULL** characters. In other words, it is a single-level PIDL, relative to the folder, not a fully qualified PIDL.
3.  Repeat step 2 until [**Next**](ienumidlist-next.md) returns S\_FALSE to indicate that all items have been enumerated.
4.  Call **IEnumIDList::Release** to release the enumeration object.

> [!Note]  
> It is important to keep track of whether you are working with a full or relative PIDL. Some functions and methods will accept either, but others will only take one or the other.

 

The remaining three [**IEnumIDList**](ienumidlist.md) methods ([**Reset**](ienumidlist-reset.md), [**Skip**](ienumidlist-skip.md), and [**Clone**](ienumidlist-clone.md)) are useful if you need to do repeated enumerations of the folder. They allow you to reset the enumeration, skip one or more objects, and make a copy of the enumeration object to preserve its state.

## Determining Display Names and Other Properties

Once you have enumerated all the PIDLs that are contained by a folder, you can find out what sort of objects they represent. The [**IShellFolder**](ishellfolder.md) interface provides a number of useful methods, two of which are discussed here. Other **IShellFolder** methods and other Shell folder interfaces are discussed later.

One of the most useful properties is the object's display name. To retrieve the display name of an object, pass its PIDL to [**IShellFolder::GetDisplayNameOf**](ishellfolder-getdisplaynameof.md). Although the object can be located anywhere below the parent folder in the namespace, its PIDL must be relative to the folder.

[**IShellFolder::GetDisplayNameOf**](ishellfolder-getdisplaynameof.md) returns the display name as part of of a [**STRRET**](strret.md) structure. Because extracting the display name from a **STRRET** structure can be a little tricky, the Shell provides two functions that do the job for you, [**StrRetToStr**](strrettostr.md) and [**StrRetToBuf**](strrettobuf.md). Both functions take a **STRRET** structure, and return the display name as a normal string. They differ only in how the string is allocated.

In addition to its display name, an object can have a number of attributes, such as whether it is a folder or whether it can be moved. You can retrieve an object's attributes by passing its PIDL to [**IShellFolder::GetAttributesOf**](ishellfolder-getattributesof.md). The complete list of attributes is quite large, so you should see the reference for details. Note that the PIDL that you pass to **GetAttributesOf** must be single-level. In particular, **IShellFolder::GetAttributesOf** will accept the PIDLs returned by [**IEnumIDList::Next**](ienumidlist-next.md). You can pass in an array of PIDLs, and **GetAttributesOf** will return those attributes that all objects in the array have in common.

If you have an object's fully qualified path or PIDL, [**SHGetFileInfo**](shgetfileinfo.md) provides a simple way to retrieve information about an object that is sufficient for many purposes. **SHGetFileInfo** takes a fully qualified path or PIDL, and returns a variety of information about the object including:

-   The object's display name
-   The object's attributes
-   Handles to the object's icons
-   A handle to the system image list
-   The path of the file containing the object's icon

## Getting a Pointer to a Subfolder's IShellFolder Interface

You can determine whether your folder contains any subfolders by calling [**IShellFolder::GetAttributesOf**](ishellfolder-getattributesof.md) and checking to see if the SFGAO\_FOLDER flag is set. If an object is a folder, you can bind to it, which provides you with a pointer to its [**IShellFolder**](ishellfolder.md) interface.

To bind to a subfolder, call the parent folder's [**IShellFolder::BindToObject**](ishellfolder-bindtoobject.md) method. This method takes the subfolder's PIDL and returns a pointer to its [**IShellFolder**](ishellfolder.md) interface. Once you have this pointer, you can use the **IShellFolder** methods to enumerate the subfolders contents, determine their properties, and so on.

## Determining an Object's Parent Folder

If you have an object's PIDL, you may need a handle to one of the interfaces exposed by its parent folder. For example, if you want to determine the display name associated with a PIDL by using [**IShellFolder::GetDisplayNameOf**](ishellfolder-getdisplaynameof.md), you must first retrieve the [**IShellFolder**](ishellfolder.md) interface of the object's parent. It is possible to do this with the techniques discussed in the previous sections. However, a much simpler approach is to use the Shell function, [**SHBindToParent**](shbindtoparent.md). This function takes the fully qualified PIDL of an object and returns a specified interface pointer on the parent folder. Optionally, it also returns the item's single-level PIDL for use in methods such as [**IShellFolder::GetAttributesOf**](ishellfolder-getattributesof.md).

The following sample console application retrieves the PIDL of the System special folder and returns its display name.


```
#include <shlobj.h>
#include <shlwapi.h>
#include <iostream.h>
#include <objbase.h>

int main()
{
    IShellFolder *psfParent = NULL;
    LPITEMIDLIST pidlSystem = NULL;
    LPCITEMIDLIST pidlRelative = NULL;
    STRRET strDispName;
    TCHAR szDisplayName[MAX_PATH];
    HRESULT hr;

    hr = SHGetFolderLocation(NULL, CSIDL_SYSTEM, NULL, NULL, &amp;pidlSystem);

    hr = SHBindToParent(pidlSystem, IID_IShellFolder, (void **) &amp;psfParent, &amp;pidlRelative);

    if(SUCCEEDED(hr))
    {
        hr = psfParent->GetDisplayNameOf(pidlRelative, SHGDN_NORMAL, &amp;strDispName);
        hr = StrRetToBuf(&amp;strDispName, pidlSystem, szDisplayName, sizeof(szDisplayName));
        cout << "SHGDN_NORMAL - " <<szDisplayName << '\n';
    }

    psfParent->Release();
    CoTaskMemFree(pidlSystem);

    return 0;
}
```



The application first uses [**SHGetFolderLocation**](shgetfolderlocation.md) to retrieve the System folder's PIDL. It then calls [**SHBindToParent**](shbindtoparent.md), which returns a pointer to the parent folder's [**IShellFolder**](ishellfolder.md) interface, and the System folder's PIDL relative to its parent. It then uses the parent folder's [**IShellFolder::GetDisplayNameOf**](ishellfolder-getdisplaynameof.md) method to retrieve the display name of the System folder. Because **GetDisplayNameOf** returns a [**STRRET**](strret.md) structure, [**StrRetToBuf**](strrettobuf.md) is used to convert the display name into a normal string. After displaying the display name, the interface pointers are released and the System PIDL freed. Note that you must not free the relative PIDL returned by **SHBindToParent**.

 

 



