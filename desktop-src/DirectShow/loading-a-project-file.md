---
description: Loading a Project File
ms.assetid: f8d142bd-e51d-4714-893b-8e3d02506891
title: Loading a Project File
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Loading a Project File

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

\[This API is not supported and may be altered or unavailable in the future.\]

To load a project file, you need two components: the XML parser and an empty timeline. The XML parser reads an XML project file and creates each object defined in the file. Then it inserts the objects into the timeline and sets any timeline attributes, such as the default frame rate. The following code example loads a file.


```C++
HRESULT         hr;
IAMTimeline     *pTL = NULL;
IXml2Dex        *pXML = NULL; 
hr = CoCreateInstance(CLSID_AMTimeline, NULL, CLSCTX_INPROC_SERVER, 
            IID_IAMTimeline, (void**)&pTL);
hr = CoCreateInstance(CLSID_Xml2Dex, NULL, CLSCTX_INPROC_SERVER, 
            IID_IXml2Dex, (void**)&pXML);
BSTR bstrFile = SysAllocStringLen(OLESTR("C:\\example.xtl"), 15);
hr = pXML->ReadXMLFile(pTL, bstrFile); 
SysFreeString(bstrFile);
pXML->Release();
```



The parser exposes the [**IXml2Dex**](ixml2dex.md) interface, which contains methods for loading and saving project files. The timeline exposes the [**IAMTimeline**](iamtimeline.md) interface, which contains methods for manipulating the timeline and creating new timeline objects. Call the **CoCreateInstance** function to create each component, as shown. Remember that by creating a new instance, you are incrementing the reference count on the interface. To avoid memory leaks, always release an interface when you are through with it. In this example, the pointer to **IXml2Dex** is not needed for anything more, so you can release the interface. The pointer to **IAMTimeline** is still needed for previewing the timeline.

The [**IXml2Dex::ReadXMLFile**](ixml2dex-readxmlfile.md) method reads the specified file and populates the timeline with the objects defined in the file. The file name is specified using a **BSTR** value. To shorten the example, the file name in the example is given as a literal string. Normally, you obtain it from an Open File dialog or something similar.

If the **ReadXML** method is successful, it returns a success code. Otherwise, it returns an error code such as VFW\_E\_INVALID\_FILE\_FORMAT. Always check the return value, in order to handle error conditions gracefully. Again for brevity, the example code does not check for errors.

## Related topics

<dl> <dt>

[Loading and Previewing a Project](loading-and-previewing-a-project.md)
</dt> </dl>

 

 



