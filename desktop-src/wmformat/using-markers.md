---
title: Using Markers
description: Using Markers
ms.assetid: b801c985-4ec7-441e-9f8a-40c69b1299a9
keywords:
- Windows Media Format SDK,markers
- Advanced Systems Format (ASF),markers
- ASF (Advanced Systems Format),markers
- Advanced Systems Format (ASF),seeking to markers
- ASF (Advanced Systems Format),seeking to markers
- markers,about
- markers,adding
- markers,removing
- markers,retrieving
- markers,seeking
ms.topic: article
ms.date: 05/31/2018
---

# Using Markers

A *marker* is a named point within an ASF file. Each marker consists of a name and an associated time, measured as an offset from the start of the file. An application can use markers to assign names to various points within the content, display those names to the user, and then seek to the marker positions. An application can add or remove markers from an existing ASF file.

The [**IWMHeaderInfo**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmheaderinfo) interface contains methods for working with markers. The metadata editor object supports adding and removing markers. The writer and reader objects can retrieve markers but cannot add or remove markers.

## Adding Markers

To add a marker, query the metadata editor for the **IWMHeaderInfo** interface. Then call the [**IWMHeaderInfo::AddMarker**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmheaderinfo-addmarker) method, specifying the marker name as a wide-character string and the time in 100-nanosecond units. The time must not exceed the file duration. Two markers can have the same time.

The following example adds several markers to a file:


```C++
IWMMetadataEditor *pEdit = 0;
IWMHeaderInfo     *pInfo = 0;

// Create the metadata editor object.

WMCreateEditor(&pEdit);
pEdit->Open(L"C:\\example.wmv");
pEdit->QueryInterface(IID_IWMHeaderInfo, (void**)&pInfo);

// Add the markers. Note that we add the last ones first. Do this when possible
// for improved performance when writing the markers to the file.
hr = pInfo->AddMarker(L"End",  520000000);   // 52 sec.
hr = pInfo->AddMarker(L"Segue",  350000000); // 35 sec.
hr = pInfo->AddMarker(L"Intro",  15000000);  // 1.5 sec.

// Commit changes and clean up.

pEdit->Flush();
pEdit->Close(); 
pInfo->Release();
pEdit->Release();

```



## Removing Markers

To remove a marker, call [**IWMHeaderInfo::RemoveMarker**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmheaderinfo-removemarker), specifying the index of the marker to remove. Markers are automatically sorted in increasing time order, so index 0 is always the first marker. Note that calling **RemoveMarker** changes the index numbers of any markers that follow. The following code, where *pInfo* is a pointer to an **IWMHeaderInfo** interface, removes all the markers from a file:


```C++
WORD count = 0;
pInfo->GetMarkerCount(&count);
while (count--)
{
    pInfo->RemoveMarker(0);
}

```



## Retrieving Markers

To retrieve the name and time of a marker, perform the following steps:

1.  Call the [**IWMHeaderInfo::GetMarkerCount**](/previous-versions/windows/desktop/api/wmsdkidl/nf-wmsdkidl-iwmheaderinfo-getmarkercount) method to determine how many markers the file contains.
2.  Retrieve the size of the string needed to contain the marker name. To do so, call the [**IWMHeaderInfo::GetMarker**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmheaderinfo-getmarker) method. Specify the index of the marker to retrieve, and **NULL** for the string buffer (the *pwszMarkerName* parameter). The method returns the length of the string, including the terminating '\\0' character, in the *pcchMarkerNameLen* parameter.
3.  Allocate a wide-character string to receive the name.
4.  Call **GetMarker** again, but this time pass the address of the string in the *pwszMarkerName* parameter. The method writes the marker name into the string, and returns the marker time in the *pcnsMarkerTime* parameter.

The following code loops through every marker in order and retrieves the name and time:


```C++
WORD cMarkers = 0;
HRESULT hr = pInfo->GetMarkerCount(&cMarkers);

WCHAR *wszName = 0;
WORD  len = 0;
for (WORD iMarker = 0; iMarker < cMarkers; ++iMarker)
{
    QWORD rtTime = 0;
    WORD req_len = 0;
    hr = pInfo->GetMarker(iMarker, 0, &req_len, &rtTime);
    
    // Reallocate if necessary.
    if (len < req_len)
    {
        delete[] wszName;
        wszName = new WCHAR[req_len];
        len = req_len;
    }
    hr = pInfo->GetMarker(iMarker, wszName, &req_len, &rtTime);
    // Display the name...
}
delete[] wszName;

```



## Seeking to a Marker

To start playback from a marker location, call the reader object's [**IWMReaderAdvanced2::StartAtMarker**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreaderadvanced2-startatmarker) method, specifying the index of the marker. The remaining parameters are identical to those for the [**IWMReader::Start**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreader-start) method. The following example queries the reader for the [**IWMReaderAdvanced2**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreaderadvanced2) interface and seeks to the first marker.


```C++
IWMReaderAdvanced2 *pReader2 = 0
WORD iMarkerIndex = 0;
hr = pReader->QueryInterface(IID_IWMReaderAdvanced2, (void**)&pReader2);
if (SUCCEEDED(hr))
{
    hr = pPlayer2->StartAtMarker(iMarkerIndex, 0, 1.0, 0);
    pPlayer2->Release();
}

```



## Related topics

<dl> <dt>

[**IWMHeaderInfo Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmheaderinfo)
</dt> <dt>

[**IWMReaderAdvanced2::StartAtMarker**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreaderadvanced2-startatmarker)
</dt> <dt>

[**Working with Metadata**](working-with-metadata.md)
</dt> </dl>

 

 




