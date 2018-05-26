---
title: Finding the Filter DLL for a File
description: Finding the Filter DLL for a File
ms.assetid: ed49b019-450c-4c56-9b5c-f406d4f65d35
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Finding the Filter DLL for a File

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The following example, for HTML files, shows how to find the filter DLL for a document.

**To find the filter DLL for a document:**

1.  Determine the persistent handler registered for an extension. Check to see whether the extension for the type of files that the DLL filters has a persistent handler registered under the registry entry **\\HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Classes**. Let this be &lt;*Value1*&gt;.

    ``` syntax
    \HKEY_LOCAL_MACHINE\SOFTWARE\Classes
        .htm
            PersistentHandler
                {EEC97550-47A9-11CF-B952-00AA0051FE20}
    ```

2.  If this entry exists, skip to step 4 and use &lt;*Value1*&gt; there.

    Alternatively, determine the CLSID. If there is not a persistent handler registered for the extension, find the CLSID associated with the document type under the registry entry **\\HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Classes**. Let this be &lt;*Value2*&gt;.

    ``` syntax
    \HKEY_LOCAL_MACHINE\SOFTWARE\Classes
        htmlfile
            = Class for WWW HTML files
            CLSID
                = {25336920-03F9-11CF-8FD0-00AA00686F13}
    ```

3.  Determine the persistent handler. Using &lt;*Value2*&gt;determined in Step 2, find the *PersistentHandler* value for the **\\HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Classes\\CLSID\\&lt;*Value2*&gt;** entry. Let this be &lt;*Value3*&gt;.

    ``` syntax
    \HKEY_LOCAL_MACHINE\SOFTWARE\Classes\CLSID
            {25336920-03F9-11CF-8FD0-00AA00686F13}
                = WWW HTML files
                PersistentHandler
                    = {EEC97550-47A9-11CF-B952-00AA0051FE20}
    ```

4.  Determine the **IFilter** persistent handler GUID. Using &lt;*Value1*&gt; determined in Step 1 or &lt;*Value3*&gt; determined in Step 3, find the **IFilter** *Persistent Handler* GUID for the document type. The value under the registry entry

    **\\HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Classes\\CLSID\\&lt;*Value1 or 3*&gt;\\PersistentAddinsRegistered\\**

    **89BCB740-6119-101A-BCB7-00DD010655AF** yields the *IFilter Persistent Handler GUID* for this document type. Let this be &lt;*Value4*&gt;. 89BCB740-6119-101A-BCB7-00DD010655AF is the **IFilter** interface GUID.

    ``` syntax
    \HKEY_LOCAL_MACHINE\SOFTWARE\Classes\CLSID
            {EEC97550-47A9-11CF-B952-00AA0051FE20}
                 = REG_SZ HTML File Persistent Handler
            PersistentAddinsRegistered
                 {89BCB740-6119-101A-BCB7-00DD010655AF}
                     = REG_SZ {E0CA5340-4534-11CF-B952-00AA0051FE20}
    ```

5.  Determine the filter DLL. Using &lt;*Value4*&gt; determined in Step 4, the filter DLL can be found under the entry

    **\\HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Classes\\CLSID\\&lt;*Value4*&gt;\\InprocServer32**.

    ``` syntax
    \HKEY_LOCAL_MACHINE\SOFTWARE\Classes\CLSID
         {E0CA5340-4534-11CF-B952-00AA0051FE20}
            = REG_SZ HTML Filter
            InprocServer32
                = REG_SZ nlhtml.dll
    ```

In this example, the filter DLL for HTML documents is nlhtml.dll

 

 




