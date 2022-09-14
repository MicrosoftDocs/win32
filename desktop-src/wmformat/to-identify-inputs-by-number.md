---
title: To Identify Inputs By Number
description: To Identify Inputs By Number
ms.assetid: f468f74d-7eed-4819-957d-241903f44d2d
keywords:
- Advanced Systems Format (ASF),identifying inputs by number
- ASF (Advanced Systems Format),identifying inputs by number
- profiles,identifying inputs by number
ms.topic: article
ms.date: 05/31/2018
---

# To Identify Inputs By Number

Every sample you pass to the writer must be associated with an input number. Each input number corresponds to one or more streams in the profile that the writer is using to write the file. In a profile, media sources are identified by a connection name. The writer associates an input number with each connection name when you set the profile for the writer. Before you can pass samples to the writer, you must determine what data each input is expecting. You cannot assume that the inputs will be in the same order as the streams in a profile, even if this is often the case. Therefore, the only reliable way to match inputs with streams is to compare the connection name of the input with the connection name of the stream.

To identify the connection names and corresponding input numbers for a loaded profile, perform the following steps:

1.  Create a writer object and set a profile to use. For more information about setting profiles in the writer, see [To Use Profiles with the Writer](to-use-profiles-with-the-writer.md). You should know the connection names used for the streams in the profile. You can get the connection name from within the profile by getting the stream configuration object for each stream and calling [**IWMStreamConfig::GetConnectionName**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmstreamconfig-getconnectionname). For more information about profiles and stream configuration objects, see [Working with Profiles](working-with-profiles.md).
2.  Retrieve the total number of inputs by calling [**IWMWriter::GetInputCount**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriter-getinputcount).
3.  Loop through all of the inputs, performing the following steps for each.
    -   Retrieve the [**IWMInputMediaProps**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwminputmediaprops) interface for the input by calling [**IWMWriter::GetInputProps**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriter-getinputprops).
    -   Retrieve the connection name that corresponds to the input number by calling [**IWMInputMediaProps::GetConnectionName**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwminputmediaprops-getconnectionname). After you have the connection name, you know the streams that are associated with the input numbers assigned by the writer.

The following example code displays the connection name for each input. For more information about using this code, see [Using the Code Examples](using-the-code-examples.md).


```C++
HRESULT GetNamesForInputs(IWMWriter* pWriter)
{
    DWORD    cInputs  = 0;
    HRESULT  hr       = S_OK;
    WCHAR*   pwszName = NULL;
    WORD     cchName  = 0;

    IWMInputMediaProps* pProps = NULL;

    // Get the total number of inputs for the file.
    hr = pWriter->GetInputCount(&cInputs);
    GOTO_EXIT_IF_FAILED(hr);

    // Loop through all supported inputs.
    for (DWORD inputIndex = 0; inputIndex < cInputs; inputIndex++)
    {
        // Get the input properties for the input.
        hr = pWriter->GetInputProps(inputIndex, &pProps);  
        GOTO_EXIT_IF_FAILED(hr);

        // Get the size of the connection name.
        hr = pProps->GetConnectionName(0, &cchName);
        GOTO_EXIT_IF_FAILED(hr);

        if (cchName > 0)
        {
            // Allocate memory for the connection name.
            pwszName = new WCHAR[cchName];
            if (wszName == NULL)
            {
                hr = E_OUTOFMEMORY;
                goto Exit;
            }

            // Get the connection name.
            hr = pProps->GetConnectionName(pwszName, &cchName);
            GOTO_EXIT_IF_FAILED(hr);
            
            // Display the name.
            printf("Input # %d = %S\n", pwszName);
        } // end if

        // Clean up for next iteration.
        SAFE_ARRAY_DELETE(pwszName);
        SAFE_RELEASE(pProps);
    } // end for inputIndex

Exit:
    SAFE_ARRAY_DELETE(pwszName);
    SAFE_RELEASE(pProps);
    return hr;
}

```



## Related topics

<dl> <dt>

[**IWMWriter Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmwriter)
</dt> <dt>

[**Writing ASF Files**](writing-asf-files.md)
</dt> </dl>

 

 




