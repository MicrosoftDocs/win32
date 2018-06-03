---
Description: Implementation of converting from a text ink object (tInk) to ink.
ms.assetid: 9365da4c-3667-49f0-838f-f099d28dab44
title: Converting a Text Ink Object to Ink
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Converting a Text Ink Object to Ink

Implementation of converting from a text ink object (tInk) to ink.

## To convert from a text ink object to ink

1.  Use the [IPersistStream](https://www.bing.com/search?q=IPersistStream) interface to write the contents of the text ink object out to a stream. The text ink object uses ink serialized format to write to the steam.
2.  Read the contents of the stream into a BYTE array.
3.  Use the [**InkDisp**](/windows/desktop/api/msinkaut/) object's [**Load**](/windows/desktop/api/msinkaut/) method to load the contents of the stream into the **InkDisp** object.

## Text Ink Object to Ink Object Example

The following code fragment converts a text ink object to ink.

First, the code obtains a text ink object.


```C++
/* Create a variable to hold the text ink object */
CComPtr<IInkObject *> spITextInk;

/* Obtain the text ink object */
```



Then, the code creates a pointer for the stream that holds the contents of the text ink object.


```C++
// Create a Stream pointer to hold the saved object
CComPtr<IStream *> spStream = NULL; 
```



Then, the code obtains the [IPersistStream](https://www.bing.com/search?q=IPersistStream) interface from the text ink object.


```C++
// Declare the IPersistStream to be used for retrieving the saved data from the text ink
CComPtr<IPersistStream *> spIPersistStream = NULL;
// Get the actual IPersistStream interface off of the TextInk
HRESULT hr = pITextInk->QueryInterface(IID_IPersistStream, (void **)&amp;spIPersistStream);
ASSERT(SUCCEEDED(hr) &amp;&amp; spIPersistStream);
```



Then, the code uses the [IPersistStream](https://www.bing.com/search?q=IPersistStream) interface to save the contents of the text ink object to the stream.


```C++
if( SUCCEEDED(hr) &amp;&amp; pIPersistStream )
{
    // Create the stream 
    if( SUCCEEDED(hr=CreateStreamOnHGlobal(NULL, TRUE, &amp;spStream)) &amp;&amp; spStream )
    {
        // Save the TextInk through IPersistStream Interface to the IStream
        hr = spIPersistStream->Save(spStream, FALSE);
    }
}
```



Then, the code creates an [**InkCollector**](/windows/desktop/api/msinkaut/) object, creates an [**InkDisp**](/windows/desktop/api/msinkaut/) object for the **InkCollector**, attaches the **InkCollector** to the application window, and enables ink collection on the **InkCollector**.


```C++
// Now create an InkCollector object along with InkDisp Object
if( SUCCEEDED(hr) &amp;&amp; spStream)
{
    CComPtr<IInkCollector *> spIInkCollector;
    CComPtr<IInkDisp *> spIInkDisp = NULL;

    // Create the InkCollector object.
    hr = CoCreateInstance(CLSID_InkCollector, 
        NULL, CLSCTX_INPROC_SERVER, 
        IID_IInkCollector, 
        (void **) &amp;spIInkCollector);
    if (FAILED(hr)) 
        return -1;

    // Get a pointer to the Ink object
    hr = spIInkCollector->get_Ink(&amp;spIInkDisp);
    if (FAILED(hr)) 
        return -1;

    // Tell InkCollector the window to collect ink in
    hr = spIInkCollector->put_hWnd((long)hwnd);
    if (FAILED(hr)) 
        return -1;

    // Enable ink input in the window
    hr = spIInkCollector->put_Enabled(VARIANT_TRUE);
    if (FAILED(hr)) 
        return -1;
```



Then, the code retrieves the size of the stream and creates a safe array to hold the contents of the stream.


```C++
    // Now create a variant data type based on the IStream data
    const LARGE_INTEGER li0 = {0, 0};
    ULARGE_INTEGER uli = {0,0};

    // Find the size of the stream
    hr = spStream->Seek(li0, STREAM_SEEK_END, &amp;uli);
    ASSERT(0 == uli.HighPart);
    DWORD dwSize = uli.LowPart;

    // Set uli to point to the beginning of the stream.
    hr=spStream->Seek(li0, STREAM_SEEK_SET, &amp;uli);
    ASSERT(SUCCEEDED(hr));

    // Create a safe array to hold the stream contents
    if( SUCCEEDED(hr) )
    {
        VARIANT vtData;
        VariantInit(&amp;vtData);
        vtData.vt = VT_ARRAY | VT_UI1;

        vtData.parray = ::SafeArrayCreateVector(VT_UI1, 0, dwSize);
        if (vtData.parray)
        {
```



Finally, the code accesses the safe array and uses the [**InkDisp**](/windows/desktop/api/msinkaut/) object's [**Load**](/windows/desktop/api/msinkaut/) method to load the ink from the array.


```C++
            DWORD dwRead = 0;
            LPBYTE pbData = NULL; 

            if (SUCCEEDED(::SafeArrayAccessData(vtData.parray, (void**)&amp;pbData)))
            {
                // Read the data from the stream to the varian data and load that into an InkDisp object
                if (TRUE == spStream->Read(pbData, uli.LowPart, &amp;dwRead)
                    &amp;&amp; SUCCEEDED(spIInkDisp->Load(vtData)))
                {
                    hr = S_OK;
                }
                ::SafeArrayUnaccessData(vtData.parray);
            }
            ::SafeArrayDestroy(vtData.parray);
        }
    }
}
```



 

 



