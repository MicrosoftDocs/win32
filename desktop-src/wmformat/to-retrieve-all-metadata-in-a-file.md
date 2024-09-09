---
title: To Retrieve All Metadata in a File
description: To Retrieve All Metadata in a File
ms.assetid: c1de58d7-25a8-4416-9ee9-6ebe641ed640
keywords:
- Windows Media Format SDK,retrieving metadata
- Advanced Systems Format (ASF),retrieving metadata
- ASF (Advanced Systems Format),retrieving metadata
- metadata,retrieving all
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# To Retrieve All Metadata in a File

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following code example is a function that displays all the metadata in a file. In order to use the function, you must pass it a pointer to the [**IWMHeaderInfo3**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmheaderinfo3) interface of a metadata editor object, reader object, synchronous reader object, or writer object. You must also include the Stdio.h header file somewhere in your project. For more information about how to use this example, see [Using the Code Examples](using-the-code-examples.md).

For clarity, this example does not display the values of binary and GUID attributes. For binary attributes, you should check to see if the attribute name matches any of the known complex metadata attributes. If it does, you should format your output according to the structure used for that attribute. Similarly, GUID attribute values can be displayed in a number of ways. You can choose to display each member of the structure one at a time or convert the structure to a string and display it as one value.


```C++
HRESULT ShowAllAttributes(IWMHeaderInfo3* pHeaderInfo)
{
    HRESULT hr          = S_OK;
    
    WORD    cAttributes = 0;
    WCHAR*  pwszName    = NULL;
    WORD    cchName     = 0;
    BYTE*   pbValue     = NULL;
    DWORD   cbValue     = 0;
    WORD    langIndex   = 0;
    WORD    attIndex    = 0;

    WMT_ATTR_DATATYPE attType;

    // Get the total number of attributes in the file.

    hr = pHeaderInfo->GetAttributeCountEx(0xFFFF, &cAttributes);
    GOTO_EXIT_IF_FAILED(hr);

    // Loop through all the attributes, retrieving and displaying each.

    for(attIndex = 0; attIndex < cAttributes; attIndex++)
    {
        // Get the required buffer lengths for the name and value.

        hr = pHeaderInfo->GetAttributeByIndexEx(0xFFFF,
                                                attIndex,
                                                NULL,
                                                &cchName,
                                                NULL,
                                                NULL,
                                                NULL,
                                                &cbValue);
        GOTO_EXIT_IF_FAILED(hr);

        // Allocate the buffers.

        pwszName = new WCHAR[cchName];
        if(pwszName == NULL)
        {
            hr = E_OUTOFMEMORY;
            goto Exit;
        }

        pbValue = new BYTE[cbValue];
        if(pbValue == NULL)
        {
            hr = E_OUTOFMEMORY;
            goto Exit;
        }

        // Get the attribute.

        hr = pHeaderInfo->GetAttributeByIndexEx(0xFFFF,
                                                attIndex,
                                                pwszName,
                                                &cchName,
                                                &attType,
                                                &langIndex,
                                                pbValue,
                                                &cbValue);
        GOTO_EXIT_IF_FAILED(hr);

        // Display the attribute global index and name.

        printf("%3d - %S (Language %d):\n\t ", attIndex, pwszName, langIndex);

        // Display the attribute depending upon type.

        switch(attType)
        {
        case WMT_TYPE_DWORD:
        case WMT_TYPE_QWORD:
        case WMT_TYPE_WORD:
            printf("%d\n\n", (DWORD) *pbValue);
            break;
        case WMT_TYPE_STRING:
            printf("%S\n\n", (WCHAR*) pbValue);
            break;
        case WMT_TYPE_BINARY:
            printf("<binary value>\n\n");
            break;
        case WMT_TYPE_BOOL:
            printf("%s\n\n", ((BOOL) *pbValue == TRUE) ? "True" : "False");
            break;
        case WMT_TYPE_GUID:
            printf("<GUID value>\n\n", (DWORD) *pbValue);
            break;
        }

        // Release allocated memory for the next pass.

        SAFE_ARRAY_DELETE(pwszName);
        SAFE_ARRAY_DELETE(pbValue);
        cchName = 0;
        cbValue = 0;
    } // End for attIndex.

Exit:
    SAFE_ARRAY_DELETE(pwszName);
    SAFE_ARRAY_DELETE(pbValue);
    return hr;
}

```



## Related topics

<dl> <dt>

[**Retrieving Metadata Attributes**](retrieving-metadata-attributes.md)
</dt> </dl>

 

 




