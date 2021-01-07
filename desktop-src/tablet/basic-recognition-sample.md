---
description: This application demonstrates how you can build a simple handwriting recognition application.This program creates an InkCollector object to ink-enable the window and a default recognizer context object.
ms.assetid: 6dc94293-cdf7-4b90-a5e8-559f376add26
title: Basic Recognition Sample
ms.topic: article
ms.date: 05/31/2018
---

# Basic Recognition Sample

This application demonstrates how you can build a simple *handwriting* recognition application.

This program creates an [**InkCollector**](inkcollector-class.md) object to *ink*-enable the window and a default *recognizer context* object. Upon receiving the "Recognize!" command, fired from the application's menu, the collected ink strokes are passed to the recognizer context. The best result string is presented in a message box.

## Creating the RecognizerContext Object

In the WndProc procedure for the application, when the WM\_CREATE message is received on startup, a new recognizer context that uses the default recognizer is created. This context is used for all recognition in the application.


```C++
case WM_CREATE:
{
    HRESULT hr;
    hr = CoCreateInstance(CLSID_InkRecognizerContext,
             NULL, CLSCTX_INPROC_SERVER, IID_IInkRecognizerContext,
             (void **) &g_pIInkRecoContext);
    if (FAILED(hr))
    {
        ::MessageBox(NULL, TEXT("There are no handwriting recognizers installed.\n"
            "You need to have at least one in order to run this sample.\nExiting."),
            gc_szAppName, MB_ICONERROR);
        return -1;
    }
  //...
```



## Recognizing the Strokes

The recognize command is received when the user clicks the Recognize! menu item. The code gets a pointer to the ink [**InkStrokes**](/previous-versions/windows/desktop/legacy/ms703293(v=vs.85)) (pIInkStrokes) off of the [**InkDisp**](inkdisp-class.md) object, and then passes the **InkStrokes** to the recognizer context using a call to putref\_Strokes.


```C++
 case WM_COMMAND:
  //...
  else if (wParam == ID_RECOGNIZE)
  {
      // change cursor to the system's Hourglass
      HCURSOR hCursor = ::SetCursor(::LoadCursor(NULL, IDC_WAIT));
      // Get a pointer to the ink stroke collection
      // This collection is a snapshot of the entire ink object
      IInkStrokes* pIInkStrokes = NULL;
      HRESULT hr = g_pIInkDisp->get_Strokes(&pIInkStrokes);
      if (SUCCEEDED(hr)) 
      {
          // Pass the stroke collection to the recognizer context
          hr = g_pIInkRecoContext->putref_Strokes(pIInkStrokes);
          if (SUCCEEDED(hr)) 
          {
```



The code then calls the [**Recognize**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognizercontext-recognize) method of the [**InkRecognizerContext**](inkrecognizercontext-class.md) object, passing in a pointer to an [**IInkRecognitionResult**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkrecognitionresult) object to hold the results.


```C++
              // Recognize
              IInkRecognitionResult* pIInkRecoResult = NULL;
              hr = g_pIInkRecoContext->Recognize(&pIInkRecoResult);
              if (SUCCEEDED(hr)) 
              {
```



Finally, the code uses the [**IInkRecognitionResult**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkrecognitionresult) object's [**TopString**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognitionresult-get_topstring) property retrieve the top recognition result into a string variable, releases the **IInkRecognitionResult** object, and displays the string in a message box.


```C++
                  // Get the best result of the recognition 
                  BSTR bstrBestResult = NULL;
                  hr = pIInkRecoResult->get_TopString(&bstrBestResult);
                  pIInkRecoResult->Release();
                  pIInkRecoResult = NULL;

                  // Show the result string
                  if (SUCCEEDED(hr) && bstrBestResult)
                  {
                      MessageBoxW(hwnd, bstrBestResult, 
                                  L"Recognition Results", MB_OK);
                      SysFreeString(bstrBestResult);
                  }  }
        
```



Be sure to reset the recognizer context between usages.


```
              // Reset the recognizer context
              g_pIInkRecoContext->putref_Strokes(NULL);
          }
          pIInkStrokes->Release();
      }
      // restore the cursor
      ::SetCursor(hCursor);
  }
```



 

 
