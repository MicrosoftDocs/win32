---
title: Saving Profiles
description: Saving Profiles
ms.assetid: 07c1ef16-6696-4314-aed8-58cda464b0db
keywords:
- Windows Media Format SDK,saving profiles
- Windows Media Format SDK,profile saving
- profiles,saving
- profiles,IWMProfileManager interface
- IWMProfileManager,saving profiles
ms.topic: article
ms.date: 05/31/2018
---

# Saving Profiles

You can use the [**IWMProfileManager::SaveProfile**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofilemanager-saveprofile) method to save the contents of a profile object to a string formatted with XML. No methods are provided to store the profile string to a file; you can use the file I/O routines of your choice.

> [!Note]  
> You should never alter the profile string written to a file. Any changes you want to make to a profile should be made programmatically. Changing values in a .prx file can cause unpredictable results.

 

The following example is a function to save a profile to a file using standard C-style file I/O. To compile an application that uses this example, you must include stdio.h in your project.


```C++
HRESULT ProfileToFile(IWMProfileManager* pProfileMgr, 
                      IWMProfile* pProfile)
{
    HRESULT hr = S_OK;

    FILE*   pFile;
    
    WCHAR*  pwszProfileString = NULL;
    DWORD   cchProfileString = 0;

    // Save the profile to a string.
    // First, retrieve the size of the string required.
    hr = pProfileMgr->SaveProfile(pProfile, 
                                  NULL, 
                                  &cchProfileString);
    if(FAILED(hr))
    {
        printf("Could not get the profile string size.");
        return hr;
    }

    // Allocate memory to hold the string.
    pwszProfileString = new WCHAR[cchProfileString];

    if(pwszProfileString == NULL)
    {
        printf("Could not allocate memory for the profile string.");
        return E_OUTOFMEMORY;
    }

    // Retrieve the string.
    hr = pProfileMgr->SaveProfile(pProfile, 
                                  pwszProfileString, 
                                  &cchProfileString);
    if(FAILED(hr))
    {
        printf("Could not save the profile string.");
        return hr;
    }

    // Create the output file.
    pFile = fopen("MyProfile.prx", "w");

    // Write the profile string to the file.
    fprintf(pFile, "%S\n", pwszProfileString);

    // Close the file.
    fclose(pFile);

    delete[] pwszProfileString;

    return S_OK;
}
```



## Related topics

<dl> <dt>

[**Working with Profiles**](working-with-profiles.md)
</dt> </dl>

 

 




