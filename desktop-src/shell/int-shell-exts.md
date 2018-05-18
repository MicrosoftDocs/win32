---
Description: 'Much of the implementation of a Shell extension handler object is dictated by its type. There are, however, some common elements. This topic discusses those aspects of implementation that are shared by all Shell extension handlers.'
ms.assetid: 'ce21ca0f-157c-4f69-bcf9-dc259c3bac80'
title: Initializing Shell Extension Handlers
---

# Initializing Shell Extension Handlers

Much of the implementation of a Shell extension handler object is dictated by its type. There are, however, some common elements. This topic discusses those aspects of implementation that are shared by all Shell extension handlers.

All Shell extension handlers are in-process Component Object Model (COM) objects. They must be assigned a GUID and registered as described in [Registering Shell Extension Handlers](handlers.md). They are implemented as DLLs and must export the following standard functions:

-   [**DllMain**](base.dllmain). The standard entry point to the DLL.
-   [**DllGetClassObject**](com.dllgetclassobject). Exposes the object's class factory.
-   [**DllCanUnloadNow**](com.dllcanunloadnow). COM calls this function to determine whether the object is serving any clients. If not, the system can unload the DLL and free the associated memory.

Like all COM objects, Shell extension handlers must implement an [**IUnknown**](com.iunknown) interface and a [class factory](com.implementing_iclassfactory). Most must also implement either an [**IPersistFile**](com.ipersistfile) or [**IShellExtInit**](ishellextinit.md) interface in Windows XP or earlier. These were replaced by [**IInitializeWithStream**](iinitializewithstream.md), [**IInitializeWithItem**](iinitializewithitem.md) and [**IInitializeWithFile**](iinitializewithfile.md) in Windows Vista. The Shell uses these interfaces to initialize the handler.

The [**IPersistFile**](com.ipersistfile) interface must be implemented by the following:

-   Icon handlers
-   Data handlers
-   Drop handlers

The [**IShellExtInit**](ishellextinit.md) interface must be implemented by the following:

-   Shortcut menu handlers
-   Drag-and-drop handlers
-   Property sheet handlers

The following subjects are discussed in the remainder of this topic:

-   [Implementing IPersistFile](#implementing-ipersistfile)
-   [Implementing IShellExtInit](#implementing-ishellextinit)
-   [Infotip Customization](#infotip-customization)
-   [Related topics](#related-topics)

## Implementing IPersistFile

The [**IPersistFile**](com.ipersistfile) interface is designed to permit an object to be loaded from or saved to a disk file. It has six methods in addition to [**IUnknown**](com.iunknown), five of its own, and the [**GetClassID**](com.ipersist_getclassid) method that it inherits from [**IPersist**](com.ipersist). With Shell extensions, **IPersist** is used only to initialize a Shell extension handler object. Because there is typically no need to read from or write to the disk, only the **GetClassID** and [**Load**](com.ipersistfile_load) methods require a nontoken implementation.

The Shell calls [**GetClassID**](com.ipersist_getclassid) first, and the function returns the class identifier (CLSID) of the extension handler object. The Shell then calls [**Load**](com.ipersistfile_load) and passes in two values. The first, *pszFile*, is a Unicode string with the name of the file or folder that Shell is about to operate on. The second is *dwMode*, which indicates the file access mode. Because there is normally no need to access files, *dwMode* is typically zero. The method stores these values as needed for later reference.

The following code fragment illustrates how a typical Shell extension handler implements the [**GetClassID**](com.ipersist_getclassid) and [**Load**](com.ipersistfile_load) methods. It is designed to handle either ANSI or Unicode. CLSID\_SampleExtHandler is the extension handler object's GUID, and CSampleShellExtension is the name of the class used to implement the interface. The **m\_szFileName** and **m\_dwMode** variables are private variables that are used to store the file's name and access flags.


```C++
class CSampleShellExtension : public IPersistFile
{
    // Method declarations not included

    private:
    WCHAR m_szFileName[MAX_PATH];    // The file name
    DWORD m_dwMode;                  // The file access mode
}

IFACEMETHODIMP CSampleShellExtension::GetClassID(__out CLSID *pCLSID)
{
    *pCLSID = CLSID_SampleExtHandler;
}

IFACEMETHODIMP CSampleShellExtension::Load(PCWSTR pszFile, DWORD dwMode)
{
    m_dwMode = dwMode;
    return StringCchCopy(m_szFileName, ARRAYSIZE(m_szFileName), pszFile); 
}

// The implementation sample is continued in the next section.
```



## Implementing IShellExtInit

The [**IShellExtInit**](ishellextinit.md) interface has only one method, [**IShellExtInit::Initialize**](ishellextinit-initialize.md), in addition to [**IUnknown**](com.iunknown). The method has three parameters that the Shell can use to pass in various types of information. The values passed in depend on the type of handler, and some can be set to **NULL**.

-   *pidlFolder* holds a folder's pointer to an item identifier list (PIDL). This is an absolute PIDL. For property sheet extensions, this value is **NULL**. For shortcut menu extensions, it is the PIDL of the folder that contains the item whose shortcut menu is being displayed. For nondefault drag-and-drop handlers, it is the PIDL of the target folder.
-   *pDataObject* holds a pointer to a data object's [**IDataObject**](com.idataobject) interface. The data object holds one or more file names in [CF\_HDROP](dragdrop.md) format.
-   *hRegKey* holds a registry key for the file object or folder type.

The [**IShellExtInit::Initialize**](ishellextinit-initialize.md) method stores the file name, [**IDataObject**](com.idataobject) pointer, and registry key as needed for later use. The following code fragment illustrates an implementation of **IShellExtInit::Initialize**. For simplicity, this example assumes that the data object contains only a single file. In general, the data object might contain multiple files, each of which will need to be extracted.


```C++
// This code continues the CSampleShellExtension sample shown in the
// "Implementing IPersistFile" section above.

class CSampleShellExtension : public IShellExtInit
{
    // Method declarations not included
    
    private:
    // IDList of the folder for extensions invoked on the folder, such as 
    // background context menu handlers or nondefault drag-and-drop handlers. 
    PIDLIST_ABSOLUTE m_pidlFolder;
    
    // The data object contains an expression of the items that the handler is 
    // being initialized for. Use SHCreateShellItemArrayFromDataObject to 
    // convert this object to an array of items. Use SHGetItemFromObject if you
    // are only interested in a single Shell item. If you need a file system
    // path, use IShellItem::GetDisplayName(SIGDN_FILESYSPATH, ...).
    IDataObject *m_pdtobj;
    
    // For context menu handlers, the registry key provides access to verb 
    // instance data that might be stored there. This is a rare feature to use 
    // so most extensions do not need this variable.
    HKEY m_hRegKey;             
}
    
// This method must be very efficient. Do not do any unnecessary work here.
// Use Initialize to acquire resources that will be used later.

IFACEMETHODIMP CSampleShellExtension::Initialize(__in_opt PCIDLIST_ABSOLUTE pidlFolder,
                                                 __in_opt IDataObject *pDataObject, 
                                                 __in_opt HKEY hRegKey) 
{ 
    // In some cases, handlers are initialized multiple times. Therefore, 
    // clear any previous state here.
    CoTaskMemFree(m_pidlFolder);
    m_pidlFolder = NULL;
    
    if (m_pdtobj)
    { 
        m_pdtobj->Release(); 
    }
    
    if (m_hRegKey)
    {
        RegCloseKey(m_hRegKey);
        m_hRegKey = NULL;
    }
    
    // Capture the inputs for use later.
    HRESULT hr = S_OK;
    
    if (pidlFolder)
    {
        m_pidlFolder = ILClone(pidlFolder);   // Make a copy to use later.
        hr = m_pidlFolder ? S_OK : E_OUTOFMEMORY;
    }
    
    if (SUCCEEDED(hr))
    {
        // If a data object pointer was passed into the method, save it and
        // extract the file name. 
        if (pDataObject) 
        { 
            m_pdtobj = pDataObject; 
            m_pdtobj->AddRef(); 
        }
    
        // It is uncommon to use the registry handle, but if you need it,
        // duplicate it now.
        if (hRegKey)
        {
            LSTATUS const result = RegOpenKeyEx(hRegKey, NULL, 0, KEY_READ, &amp;m_hRegKey); 
            hr = HRESULT_FROM_WIN32(result);
        }
    }
    
    return hr;
}
```



## Infotip Customization

There are two ways to customize infotips. One way is to implement an object that supports [**IQueryInfo**](iqueryinfo.md) and then register the object under the proper subkey in the registry (see below). Alternatively, you can specify either a fixed string or a list of certain file properties to be displayed.

To display a fixed string for a namespace extension, create a subkey called **InfoTip** beneath the CLSID key of your namespace extension. Set the data of that subkey to be the string you want to be displayed.

```
HKEY_CLASSES_ROOT
   CLSID
      {CLSID}
         InfoTip = InfoTip string for your namespace extension
```

To display a fixed string for a file type, create a subkey called **InfoTip** beneath the **ProgID** key of the file type for which you want to supply infotips. Set the data of that subkey to be the string you want to be displayed.

```
HKEY_CLASSES_ROOT
   ProgID
      InfoTip = InfoTip string for all files of this type
```

If you want the Shell to show certain file properties in the infotip for a specific file type, create a subkey called **InfoTip** beneath the **ProgID** key of that file type. Set the data of that subkey to be a semicolon-delineated list of canonical property names or {fmtid}, pid pairs where *propname* is a canonical property name and *{fmtid},pid* is a [**FMTID/PID pair**](shcolumnid-str.md).

```
HKEY_CLASSES_ROOT
   ProgID
      InfoTip = propname;propname;{fmtid},pid;{fmtid},pid
```

The following property names can be used.



| Property Name    | Description                   | Retrieved From                                                                            |
|------------------|-------------------------------|-------------------------------------------------------------------------------------------|
| Author           | Author of the document        | [**PIDSI\_AUTHOR**](stg.the_summary_information_property_set)                             |
| Title            | Title of the document         | [**PIDSI\_TITLE**](stg.the_summary_information_property_set)                              |
| Subject          | Subject summary               | [**PIDSI\_SUBJECT**](stg.the_summary_information_property_set)                            |
| Comment          | Document comments             | [**PIDSI\_COMMENT**](stg.the_summary_information_property_set) or folder/drive properties |
| PageCount        | Number of pages               | [**PIDSI\_PAGECOUNT**](stg.the_summary_information_property_set)                          |
| Name             | Friendly name                 | Standard folder view                                                                      |
| OriginalLocation | Location of original file     | Briefcase folder and Recycle Bin folder                                                   |
| DateDeleted      | Date file was deleted         | Recycle Bin folder                                                                        |
| Type             | Type of file                  | Standard folder details view                                                              |
| Size             | Size of file                  | Standard folder details view                                                              |
| SyncCopyIn       | Same as OriginalLocation      | Same as OriginalLocation                                                                  |
| Modified         | Date last modified            | Standard folder details view                                                              |
| Created          | Date created                  | Standard folder details view                                                              |
| Accessed         | Date last accessed            | Standard folder details view                                                              |
| InFolder         | Directory containing the file | Document search results                                                                   |
| Rank             | Quality of search match       | Document search results                                                                   |
| FreeSpace        | Available storage space       | Disk drives                                                                               |
| NumberOfVisits   | Number of visits              | Favorites folder                                                                          |
| Attributes       | File Attributes               | Standard folder details view                                                              |
| Company          | Company name                  | [**PIDDSI\_COMPANY**](stg.the_documentsummaryinformation_and_userdefined_property_sets)   |
| Category         | Document category             | [**PIDDSI\_CATEGORY**](stg.the_documentsummaryinformation_and_userdefined_property_sets)  |
| Copyright        | Media copyright               | [**PIDMSI\_COPYRIGHT**](stg.the_documentsummaryinformation_and_userdefined_property_sets) |
| HTMLInfoTipFile  | HTML InfoTip file             | Desktop.ini file for folder                                                               |



 

## Related topics

<dl> <dt>

[Registering Shell Extension Handlers](reg-shell-exts.md)
</dt> </dl>

 

 



