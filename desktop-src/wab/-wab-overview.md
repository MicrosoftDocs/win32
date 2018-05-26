---
title: About Windows Address Book
description: Windows provides an address book for storing contact information.
ms.assetid: 16aefb03-359e-44c2-a87d-595e6a4e4451
keywords:
- Windows Address Book (WAB),about
- WAB (Windows Address Book),about
- address books
- Wab.exe
- Windows Address Book (WAB),registering applications
- WAB (Windows Address Book),registering applications
- WAB API
- registering applications to use WAB API
- WAB32.dll
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# About Windows Address Book

New applications should not use this set of interfaces. These interfaces exist for backward compatibility with legacy applications. These interfaces will be unavailable in the future.

> [!Note]  
> In Windows Vista, Windows Contacts replaces Windows Address Book (WAB). For more information about this new mechanism for storing and retrieving contact information, see [Windows Contacts](_wincontacts_entry_point).

 

Windows provides an address book for storing contact information. The WAB is an application and service that enables users to keep track of people. The WAB has a local database and user interface for finding and editing information about people, and it can query network directory servers using Lightweight Directory Access Protocol (LDAP). Other applications can use the WAB. For example, Microsoft Outlook uses the WAB as its e-mail address book.

The following topics are discussed in this document.

-   [WAB Application](#wab-application)
-   [Using the WAB API](#using-the-wab-api)
    -   [Registering Your Application to Use WAB](#registering-your-application-to-use-wab)
    -   [Loading the WAB32.dll](#loading-the-wab32dll)
    -   [Creating an Instance of WAB](#creating-an-instance-of-wab)
-   [Related topics](#related-topics)

## WAB Application

The Wab.exe program is included with Windows 98 and later. This address book application enables you to:

-   Create contact entries.
-   Store contact information locally.
-   Search for entries in your contact database.
-   Edit your contact information.
-   Add contacts from e-mail messages. When you receive e-mail you can add the sender's contact information.
-   Import contacts from other programs.

When you invoke Wab.exe, it creates and searches the file named Username.wab which is found in the Application Data directory. For specific information on using the Wab.exe program, see the Knowledge Base Article Q164531 and the Electronic Mail section of the Windows 98 Resource Kit.

## Using the WAB API

The WAB provides an API that enables other applications to directly use its database and user interface services; therefore, you can write programs that include address books. The WAB  API is based on MAPI, but the WAB does not use or require MAPI. The WAB interfaces support many of the methods used by MAPI, and because they inherit from [IUnknown](33f1d79a-33fc-4ce5-a372-e08bda378332), they have the standard AddRef, Release, and QueryInterface methods. The WAB also has functions that provide access to the object interfaces.

### Registering Your Application to Use WAB

If you want to use the WAB, you must register your application to use the Wab32.dll as a shared DLL. Registering Wab32.dll as a shared DLL prevents it from being inadvertently uninstalled while your application is running. To accomplish the registration, you must increment the reference count of the Wab32.dll in the SharedDLLs section of the registry.


```
HKLM\Software\Microsoft\Windows\CurrentVersion\SharedDLLs
```



The steps to increment the reference count are:

1.  Find the path to the WAB  DLL.
    -   Look in the registry under:
        ```
        HKLM\Software\Microsoft\WAB\DLLPath
        ```

        

    -   The default value under this key gives the path of any WAB  DLL installed on the computer.
    -   This DLL path is defined in Wabapi.h as WAB\_DLL\_PATH\_KEY.
    -   If you include Wabapi.h in your application, use WAB\_DLL\_PATH\_KEY as the name of the key to open.
2.  Find the WAB  DLL path key.
    -   Look in the registry under:
        ```
        HKLM\Software\Microsoft\Windows\CurrentVersion\
        SharedDLLs
        ```

        

    -   Find the value &lt;Full WAB32 Path&gt;.
    -   Increment the reference count by one and save the incremented value back to the registry.
3.  WAB  DLL path key not found.
    -   If the value &lt;Full WAB32 Path&gt; does not exist, create the value using the Registry API. The value is a **DWORD** representing the number of clients registered to use the WAB.
    -   Increment the reference count by one and save the incremented value back to the registry.

### Loading the WAB32.dll

With Microsoft Internet Explorer 4.0 or later, Wab32.dll is set in the registry at


```
 
HKLM\Software\Microsoft\WAB\DLLPath 
```



Load the DLL at run time only if the key is not in the registry, if the path set in the key is invalid, or if you are using a version of Windows Internet Explorer earlier than Internet Explorer 4.0.

If you need to load the DLL, call [LoadLibrary](_win32_loadlibrary).

### Creating an Instance of WAB

To use WAB in your application, you must create and initialize the first instance of IWABObject. The following code sample demonstrates how to do this.


```C++
LPWABOPEN lpfnWABOpen = NULL;  // Defined in Wabapi.h.
HINSTANCE hinstWAB = NULL;

// Initialize <tla rid="tla_wab" /> and get an instance
// of IWABObject.

HRESULT InitWAB (LPWABOBJECT *lppWABObject, LPADRBOOK 
*lppAdrBook)
{
   HRESULT hr = E_FAIL;
   hinstWAB = LoadLibrary_WABDll();
   {
      if (hinstWAB)
         {
            lpfnWABOpen = (LPWABOPEN) GetProcAddress
               (hinstWAB, "WABOpen");
            if (lpfnWABOpen)
               hr = lpfnWABOpen (lppAdrBook, lppWABObject,
                 NULL, 0);
         }    
   }
   return hr;
}
```



## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[Extending the WAB Toolbar and Context Menu Actions](-wab-extending-context-menus.md)
</dt> <dt>

[Extending the WAB Property Sheets](-wab-extending-prop-sheets.md)
</dt> <dt>

[WAB and Multi-User/Multi-Identity Profiles](-wab-multiprofiles.md)
</dt> <dt>

[UNICODE Support in WAB](-wab-unicode.md)
</dt> <dt>

[Importing and Exporting Named Properties Through vCards](-wab-vcardprops.md)
</dt> <dt>

[Windows Address Book Interfaces](-wab-interfaces.md)
</dt> <dt>

[Windows Address Book Functions](-wab-functions.md)
</dt> <dt>

[Windows Address Book Structures](-wab-structures.md)
</dt> <dt>

[Windows Address Book Enumerated Types](-wab-enums.md)
</dt> </dl>

 

 




