---
Description: Autocompletion expands strings that have been partially entered in an edit control into complete strings.
title: Using Autocomplete
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using Autocomplete

Autocompletion expands strings that have been partially entered in an [edit control](https://msdn.microsoft.com/library/windows/desktop/bb775458) into complete strings. For example, when a user starts to enter a URL in the Address edit control that is embedded in the Windows Internet Explorer toolbar, autocompletion expands the string into one or more complete URL options that are consistent with the existing partial string. A partial URL string such as "mic" might be expanded to "http://www.microsoft.com" or "http://www.microsoft.com/windows". Autocompletion is typically used with edit controls or with controls that have an embedded edit control, such as the [ComboBoxEx](https://msdn.microsoft.com/library/windows/desktop/bb775740) control.

## Adding Autocomplete Functionality to Your Application

An application can add autocomplete functionality to an edit control in two ways:

-   [**SHAutoComplete**](https://msdn.microsoft.com/library/windows/desktop/bb759862) is a simple function that can autocomplete a file path or URL.
-   [**IAutoComplete**](/windows/desktop/api/Shldisp/nn-shldisp-iautocomplete) interface is exposed by the autocomplete object (CLSID\_AutoComplete). It allows applications to initialize, enable, and disable the object. **IAutoComplete** allows more control over autocomplete sources, including the ability to add a custom source. The remainder of this topic discusses the use of **IAutoComplete**. See [How To Enable Autocomplete Manually](how-to-enable-autocomplete-manually.md) for specific usage examples.

## Autocomplete Modes

When using [**IAutoComplete**](/windows/desktop/api/Shldisp/nn-shldisp-iautocomplete), autocompletion can display the completed string in two modes: autoappend and autosuggest. The modes are independent; you can enable either or both. To specify the mode, call [**IAutoComplete2::SetOptions**](/windows/desktop/api/Shldisp/nf-shldisp-iautocomplete2-setoptions).

<dl> <dt>

<span id="Autoappend"></span><span id="autoappend"></span><span id="AUTOAPPEND"></span>Autoappend
</dt> <dd>

In autoappend mode, autocompletion appends the remainder of the most likely candidate string to the existing characters, highlighting the appended characters. If the user continues to enter characters, they are added to the existing partial string. If the user adds a character that is identical to the next highlighted character, the highlighting for that character is turned off. The remaining characters will still be highlighted. If the user adds a character that does not match the next highlighted character, autocompletion attempts to generate a new candidate string based on the larger partial string and appends the remainder of the new candidate string to the current partial string. If no candidate string can be found, only the typed characters appear and the edit box behaves as it would without autocompletion. This process continues until the user accepts a string.

</dd> <dt>

<span id="Autosuggest"></span><span id="autosuggest"></span><span id="AUTOSUGGEST"></span>Autosuggest
</dt> <dd>

In autosuggest mode, autocompletion displays a drop-down list, with one or more suggested complete strings, beneath the edit control. The user can select one of the suggested strings or continue typing. As typing progresses, the drop-down list might be modified based on the current partial string. If you set the ACO\_SEARCH flag in [**IAutoComplete2::SetOptions**](/windows/desktop/api/Shldisp/nf-shldisp-iautocomplete2-setoptions), autocomplete provides an option, at the bottom of the drop-down list, to search for the current partial string. This option is displayed even if there are no suggested strings. If the user selects the search option, your application should launch a search engine to assist the user.

</dd> </dl>

## Using Predefined Autocomplete Sources

Autocompletion depends on having a source that provides it with strings to match against the user's partial string. You have the option of providing a custom autocomplete source, but several of the most common sources are provided by the system.

<dl> <dt>

<span id="CLSID_ACLHistory"></span><span id="clsid_aclhistory"></span><span id="CLSID_ACLHISTORY"></span>CLSID\_ACLHistory
</dt> <dd>

An autocomplete source that matches against the URL list in the user's History list.

</dd> <dt>

<span id="CLSID_ACLMRU"></span><span id="clsid_aclmru"></span>CLSID\_ACLMRU
</dt> <dd>

An autocomplete source that matches against the URL list in the user's Recently Used list.

</dd> <dt>

<span id="CLSID_ACListISF"></span><span id="clsid_aclistisf"></span><span id="CLSID_ACLISTISF"></span>CLSID\_ACListISF
</dt> <dd>

An autocomplete source that matches against items in the Shell namespace: files on the user's computer as well as items in virtual folders such as Control Panel.

</dd> </dl>

There are occasions when, rather than immediately freeing the resources, you might want to retain the interface pointers to the various objects involved in autocomplete. In particular, this is done when you want to adjust the autocomplete behavior dynamically. The most common instance of this occurs when using the CLSID\_ACListISF object, which autocompletes from the Shell namespace and has the option ([**ACLO\_CURRENTDIR**](https://msdn.microsoft.com/en-us/library/Bb776375(v=VS.85).aspx)) of enumerating from the current directory as well. For example, when you navigate to a new folder, Internet Explorer changes the Address bar's current directory and therefore the settings need to be changed dynamically. There are two ways to specify the directory that the CLSID\_ACListISF object should treat as the current directory:

-   [**IPersistFolder**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ipersistfolder) specifies the directory through an [**ITEMIDLIST**](/windows/desktop/api/Shtypes/ns-shtypes-_itemidlist).
-   [**ICurrentWorkingDirectory**](https://msdn.microsoft.com/en-us/library/Bb775996(v=VS.85).aspx) specifies the directory through a path string.

In the following, assume that **pal** is a pointer to the [**IACList**](https://msdn.microsoft.com/en-us/library/Bb776378(v=VS.85).aspx) interface of a CLSID\_ACListISF object:

-   Using [**IPersistFolder**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ipersistfolder):

    To tell the CLSID\_ACListISF object that a particular [**ITEMIDLIST**](/windows/desktop/api/Shtypes/ns-shtypes-_itemidlist) should be treated as the current directory, you can use the object's [**IPersistFolder**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ipersistfolder) interface. Since an **ITEMIDLIST** can refer to a virtual folder, this method is more flexible than using [**ICurrentWorkingDirectory**](https://msdn.microsoft.com/en-us/library/Bb775996(v=VS.85).aspx).

    Note that the following examples use the templatized QueryInterface, which allows for a simplified parameter list.

    ```C++
    IPersistFolder *ppf;

    hr = pal2->QueryInterface(IID_PPV_ARGS(&ppf));   
    if (SUCCEEDED(hr))
    {
        hr = ppf->Initialize(pidlCurrentDirectory);
        ppf->Release();
    }
    ```

    

-   Using [**ICurrentWorkingDirectory**](https://msdn.microsoft.com/en-us/library/Bb775996(v=VS.85).aspx):

    To give the CLSID\_ACListISF object a path as the current directory, you can use the object's [**ICurrentWorkingDirectory**](https://msdn.microsoft.com/en-us/library/Bb775996(v=VS.85).aspx) interface.

    ```C++
    WCHAR pwszDirectory[MAX_PATH] = L"C:\\Program Files";
    ICurrentWorkingDirectory *pcwd;

    hr = pal2->QueryInterface(IID_PPV_ARGS(&pcwd));    
    if (SUCCEEDED(hr))
    {
        hr = pcwd->SetDirectory(pwszDirectory);
        pcwd->Release();
    }
    ```

    

 

 



