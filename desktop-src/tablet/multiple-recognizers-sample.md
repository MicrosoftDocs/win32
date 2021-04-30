---
description: This sample demonstrates advanced features of the MicrosoftTablet PC Automation application programming interface (API) used for handwriting recognition.
ms.assetid: c9e6613c-5797-44c3-8ce1-92d4d1459ecf
title: Multiple Recognizers Sample
ms.topic: article
ms.date: 05/31/2018
---

# Multiple Recognizers Sample

This sample demonstrates advanced features of the MicrosoftTablet PC Automation application programming interface (API) used for *handwriting* recognition.

It includes the following:

-   Enumerating the installed recognizers
-   Creating a *recognizer context* with a specific language recognizer
-   Serializing recognition results with a stroke collection
-   Organizing stroke collections into a custom collection within the [**InkDisp**](inkdisp-class.md) object
-   Serializing *ink* objects to and retrieving them from an *ink serialized format (ISF)* file
-   Setting recognizer input guides
-   Using synchronous and asynchronous recognition

## Ink Headers

First, include the headers for Tablet PC Automation interfaces. These are installed with the Microsoft Windows XP Tablet PC Edition Software Development Kit (SDK).


```C++
#include <msinkaut.h>
#include <msinkaut_i.c>
```



The EventSinks.h file defines the IInkEventsImpl and IInkRecognitionEventsImpl interfaces.


```C++
#include "EventSinks.h"
```



## Enumerating the Installed Recognizers

The application's LoadMenu method populates the Create New Strokes menu with the available recognizers. An [**InkRecognizers**](/previous-versions/windows/desktop/legacy/ms702438(v=vs.85)) is created. If the [**Languages**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognizer-get_languages) property of an **InkRecognizers** object is not empty, then the recognizer is a *text recognizer*, and the value of its [**Name**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognizer-get_name) property is added to the menu.


```C++
// Create the enumerator for the installed recognizers
hr = m_spIInkRecognizers.CoCreateInstance(CLSID_InkRecognizers);
...
    // Filter out non-language recognizers by checking for
    // the languages supported by the recognizer - there is not
    // any if it is a gesture or object recognizer.
    CComVariant vLanguages;
    if (SUCCEEDED(spIInkRecognizer->get_Languages(&vLanguages)))
    {
        if ((VT_ARRAY == (VT_ARRAY & vLanguages.vt))           // it should be an array
            && (NULL != vLanguages.parray)
            && (0 < vLanguages.parray->rgsabound[0].cElements)) // with at least one element
        {
            // This is a language recognizer. Add its name to the menu.
            CComBSTR bstrName;
            if (SUCCEEDED(spIInkRecognizer->get_Name(&bstrName)))
                ...
        }
    }
```



## Creating an Ink Collector

The application's OnCreate method creates an [**InkCollector**](inkcollector-class.md) object, connects it to its event source, and enables ink collection.


```C++
// Create an ink collector object.
hr = m_spIInkCollector.CoCreateInstance(CLSID_InkCollector);

// Establish a connection to the collector's event source.
hr = IInkCollectorEventsImpl<CMultiRecoApp>::DispEventAdvise(m_spIInkCollector);

// Enable ink input in the m_wndInput window
hr = m_spIInkCollector->put_hWnd((long)m_wndInput.m_hWnd);
hr = m_spIInkCollector->put_Enabled(VARIANT_TRUE);
```



## Creating a Recognizer Context

The application's CreateRecoContext method creates and initializes a new recognizer context, and sets up the guides supported by the associated language. The [**IInkRecognizer**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkrecognizer) object's [**CreateRecognizerContext**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognizer-createrecognizercontext) method creates a [**IInkRecognizerContext2**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkrecognizercontext2) object for the language. If necessary, the old recognizer context is replaced. The context is connected to its event source. Finally, the [**Capabilities**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognizer-get_capabilities) property of the recognizer context is checked for which guides the recognizer context supports.


```C++
// Create a recognizer context
CComPtr<IInkRecognizerContext2> spNewContext;
if (FAILED(pIInkRecognizer2->CreateRecognizerContext(&spNewContext)))
    return false;

// Replace the current context with the new one
if (m_spIInkRecoContext != NULL)
{
    // Close the connection to the recognition events source
    IInkRecognitionEventsImpl<CMultiRecoApp>::DispEventUnadvise(m_spIInkRecoContext);
}
m_spIInkRecoContext.Attach(spNewContext.Detach());

// Establish a connection with the recognizer context's event source
if (FAILED(IInkRecognitionEventsImpl<CMultiRecoApp>::DispEventAdvise(m_spIInkRecoContext)))
    ...

// Set the guide if it's supported by the recognizer and has been created 
int cRows = 0, cColumns = 0;
InkRecognizerCapabilities dwCapabilities = IRC_DontCare;
if (SUCCEEDED(pIInkRecognizer->get_Capabilities(&dwCapabilities)))
    ...
```



## Collecting Strokes and Displaying Recognition Results

The application's OnStroke method updates the [**InkStrokes**](/previous-versions/windows/desktop/legacy/ms703293(v=vs.85)) of the ink collector, cancels existing asynchronous recognition requests, and creates a recognition request on the recognizer context.


```C++
// Add the new stroke to the current collection
hr = m_spIInkStrokes->Add(pIInkStroke);

if (SUCCEEDED(hr))
{
    // Cancel the previous background recognition requests
    // which have not been processed yet
    m_spIInkRecoContext->StopBackgroundRecognition();

    // Ask the context to update the recognition results with newly added strokes
    // When the results are ready, the recognizer context returns them
    // through the corresponding event RecognitionWithAlternates
    CComVariant vCustomData;
    m_spIInkRecoContext->BackgroundRecognize(vCustomData);
}
```



The application's `OnRecognition` method sends the results of the recognition request to the output window's `UpdateString` method.


```C++
// Update the output window with the new results
m_wndResults.UpdateString(bstrRecognizedString);
```



## Deleting Strokes and Recognition Results

The application's OnClear method deletes all strokes and recognition results from the [**InkDisp**](inkdisp-class.md) object and clears the windows. The recognizer context's association with its [**InkStrokes**](/previous-versions/windows/desktop/legacy/ms703293(v=vs.85)) collection is removed.


```C++
// Detach the current stroke collection from the recognizer context and release it
if (m_spIInkRecoContext != NULL)
    m_spIInkRecoContext->putref_Strokes(NULL);

m_spIInkStrokes.Release();

// Clear the custom strokes collection
if (m_spIInkCustomStrokes != NULL)
    m_spIInkCustomStrokes->Clear();

// Delete all strokes from the Ink object
// Passing NULL as a stroke collection pointer means asking to delete all strokes
m_spIInkDisp->DeleteStrokes(NULL);

// Get a new stroke collection from the ink object
...
// Ask for an empty collection by passing an empty variant 
if (SUCCEEDED(m_spIInkDisp->CreateStrokes(v, &m_spIInkStrokes)))
{
    // Attach it to the recognizer context
    if (FAILED(m_spIInkRecoContext->putref_Strokes(m_spIInkStrokes)))
        ...
}
```



## Changing Recognizer Contexts

The application's OnNewStrokes method is called when the user selects a recognizer in the Create New Strokes menu. The current [**InkStrokes**](/previous-versions/windows/desktop/legacy/ms703293(v=vs.85)) is saved. If a different language recognizer was selected, a new recognizer context is created. Then, a new **InkStrokes** is attached to the new recognizer context.


```C++
// Save the current stroke collection if there is any
if (m_spIInkRecoContext != NULL)
{
    // Cancel the previous background recognition requests
    // which have not been processed yet
    m_spIInkRecoContext->StopBackgroundRecognition();
    
    // Let the context know that there'll be no more input 
    // for the attached stroke collection
    m_spIInkRecoContext->EndInkInput();

    // Add the stroke collection to the Ink object's CustomStrokes collection
    SaveStrokeCollection();
}
...
// If a different recognizer was selected, create a new recognizer context
// Else, reuse the same recognizer context
if (wID != m_nCmdRecognizer)
{
    // Get a pointer to the recognizer object from the recognizer collection  
    CComPtr<IInkRecognizer> spIInkRecognizer;
    if ((m_spIInkRecognizers == NULL)
        || FAILED(m_spIInkRecognizers->Item(wID - ID_RECOGNIZER_FIRST,
                                             &spIInkRecognizer))
        || (false == CreateRecoContext(spIInkRecognizer)))
    {
        // restore the cursor
        ::SetCursor(hCursor);
        return 0;
    }

    // Update the status bar
    m_bstrCurRecoName.Empty();
    spIInkRecognizer->get_Name(&m_bstrCurRecoName);
    UpdateStatusBar();

    // Store the selected recognizer's command id
    m_nCmdRecognizer = wID;
}
```



It then calls StartNewStrokeCollection, which creates an empty [**InkStrokes**](/previous-versions/windows/desktop/legacy/ms703293(v=vs.85)) and attaches it to the recognizer context.

## Saving the Strokes Collection for a Recognizer Context

The application's `SaveStrokeCollection` method checks for an existing recognizer context, and finalizes the recognition of the current strokes collection. Then the [**InkStrokes**](/previous-versions/windows/desktop/legacy/ms703293(v=vs.85)) collection is added to the [**CustomStrokes**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdisp-get_customstrokes) of the ink object.


```C++
if (m_spIInkRecoContext != NULL)
{
    if (SUCCEEDED(m_spIInkStrokes->get_Count(&lCount)) && 0 != lCount)
    {
        CComPtr<IInkRecognitionResult> spIInkRecoResult;
        InkRecognitionStatus RecognitionStatus;
        if (SUCCEEDED(m_spIInkRecoContext->Recognize(&RecognitionStatus, &spIInkRecoResult)))
        {
            if (SUCCEEDED(spIInkRecoResult->SetResultOnStrokes()))
            {
                CComBSTR bstr;
                spIInkRecoResult->get_TopString(&bstr);
                m_wndResults.UpdateString(bstr);
            }
            ...
        }
    }
    // Detach the stroke collection from the old recognizer context
    m_spIInkRecoContext->putref_Strokes(NULL);
}

// Now add it to the ink's custom strokes collection
// Each item (stroke collection) of the custom strokes must be identified
// by a unique string. Here we generate a GUID for this.
if ((0 != lCount) && (m_spIInkCustomStrokes != NULL))
{
    GUID guid;
    WCHAR szGuid[40]; // format: "{xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}"
    if (SUCCEEDED(::CoCreateGuid(&guid)) 
        && (::StringFromGUID2(guid, szGuid, countof(szGuid)) != 0))
    {
        CComBSTR bstrGuid(szGuid);
        if (FAILED(m_spIInkCustomStrokes->Add(bstrGuid, m_spIInkStrokes)))
            ...
```



 

 
