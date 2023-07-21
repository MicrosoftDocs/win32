---
title: Custom Font Sets
description: This topic describes various ways in which you can use custom fonts in your app.
ms.assetid: 50842838-d150-df9a-f1b7-67ce5ea2bc80
ms.topic: article
ms.date: 05/31/2018
---

# Custom Font Sets

This topic describes various ways in which you can use custom fonts in your app.

-   [Introduction ](#introduction)
-   [Summary of APIs](#summary-of-apis)
-   [Key concepts](#key-concepts)
-   [Fonts and font file formats](#fonts-and-font-file-formats)
-   [Font sets and font collections](#font-sets-and-font-collections)
-   [Common scenarios](#common-scenarios)
    -   [Creating a font set using arbitrary fonts in the local file system](#creating-a-font-set-using-arbitrary-fonts-in-the-local-file-system)
    -   [Creating a font set using known fonts in the local file system](#creating-a-font-set-using-known-fonts-in-the-local-file-system)
    -   [Creating a custom font set using known, remote fonts on the Web](#creating-a-custom-font-set-using-known-remote-fonts-on-the-web)
    -   [Creating a custom font set using font data loaded into memory](#creating-a-custom-font-set-using-font-data-loaded-into-memory)
-   [Advanced scenarios](#advanced-scenarios)
    -   [Combining font sets](#combining-font-sets)
    -   [Using local WOFF or WOFF2 font data ](#using-local-woff-or-woff2-font-data)
    -   [Using DirectWrite remote font mechanisms with custom low-level network implementation ](#using-directwrite-remote-font-mechanisms-with-custom-low-level-network-implementation)
    -   [Supporting scenarios on earlier Windows versions ](#supporting-scenarios-on-earlier-windows-versions)

## Introduction

Most of the time, apps use the fonts that are installed locally on the system. DirectWrite provides access to these fonts using the [**IDWriteFactory3::GetSystemFontSet**](/windows/win32/api/dwrite_3/nf-dwrite_3-idwritefactory3-getsystemfontset) or [**IDWriteFactory::GetSystemFontCollection**](/windows/win32/api/dwrite/nf-dwrite-idwritefactory-getsystemfontcollection) methods. In some cases, apps may also want to use fonts that are included as part of Windows 10 but that are not currently installed on the current system. Such fonts can be accessed from the Windows font service by using the **GetSystemFontSet** method, or by calling [**IDWriteFactory3::GetSystemFontCollection**](/windows/win32/api/dwrite_3/nf-dwrite_3-idwritefactory3-getsystemfontcollection) with includeDownloadableFonts set to TRUE. 

In some application scenarios, however, apps need to use fonts that are not installed in the system and are not provided by the Windows Font Service. The following are examples of such scenarios:

-   Fonts are embedded as resources within an app binary.
-   Font files are bundled within an app package and stored on disk under the app’s installation folder.
-   The app is a font-development tool that needs to load user-specified font files. 
-   Fonts are embedded in document files that can be viewed or edited in the app. 
-   The app uses fonts obtained from a public Web font service. 
-   The app uses font data streamed via a private network protocol. 

DirectWrite provides APIs for working with custom fonts in these and other similar scenarios. The custom font data might come from files in the local file system; from remote, cloud-based sources accessed using HTTP; or from arbitrary sources after having been loaded into a memory buffer. 

> [!Note]  
> While DirectWrite has provided APIs for working with custom fonts since Windows 7, newer APIs were added in Windows 10 and again in the Windows 10 Creators Update (preview build 15021 or later) that make it easier to implement several of the scenarios mentioned. This topic focuses on APIs available in Window 10. For applications that need to work on earlier Windows versions, see [Custom Font Collections (Windows 7/8)](custom-font-collections.md). 

 

## Summary of APIs

This topic focuses on functionality provided by the following APIs: 

-   [**IDWriteFontSet**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontset) interface
-   [**IDWriteFontSetBuilder**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontsetbuilder) interface
-   [**IDWriteFontSetBuilder1**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontsetbuilder1) interface 
-   [**IDWriteFontFaceReference**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontfacereference) interface
-   [**IDWriteFontFile**](/windows/win32/api/dwrite/nn-dwrite-idwritefontfile) interface
-   [**IDWriteFactory::CreateFontFileReference**](/windows/win32/api/dwrite/nf-dwrite-idwritefactory-createfontfilereference) method 
-   [**IDWriteFactory::CreateCustomFontFileReference**](/windows/win32/api/dwrite/nf-dwrite-idwritefactory-createcustomfontfilereference) method 
-   [**IDWriteFactory3::CreateFontFaceReference**](/windows/win32/api/dwrite_3/nf-dwrite_3-idwritefontresource-createfontfacereference) methods 
-   [**DWRITE\_FONT\_PROPERTY**](/windows/win32/api/dwrite_3/ns-dwrite_3-dwrite_font_property) structure 
-   [**DWRITE\_FONT\_PROPERTY\_ID**](/windows/win32/api/dwrite_3/ne-dwrite_3-dwrite_font_property_id) enumeration 
-   [**IDWriteFontFileLoader**](/windows/win32/api/dwrite/nn-dwrite-idwritefontfileloader) interface 
-   [**IDWriteFactory::RegisterFontFileLoader**](/windows/win32/api/dwrite/nf-dwrite-idwritefactory-registerfontfileloader) method 
-   [**IDWriteFactory::UnregisterFontFileLoader**](/windows/win32/api/dwrite/nf-dwrite-idwritefactory-unregisterfontfileloader) method 
-   [**IDWriteFactory5::CreateInMemoryFontFileLoader**](/windows/win32/api/dwrite_3/nf-dwrite_3-idwritefactory5-createinmemoryfontfileloader) method 
-   [**IDWriteInMemoryFontFileLoader**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwriteinmemoryfontfileloader) interface 
-   [**IDWriteFactory5::CreateHttpFontFileLoader**](/windows/win32/api/dwrite_3/nf-dwrite_3-idwritefactory5-createhttpfontfileloader) method 
-   [**IDWriteRemoteFontFileLoader**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwriteremotefontfileloader) interface 
-   [**IDWriteFontDownloadQueue**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontdownloadqueue) interface 
-   [**IDWriteFontDownloadListener**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontdownloadlistener) interface 
-   [**IDWriteFontFileStream**](/windows/win32/api/dwrite/nn-dwrite-idwritefontfilestream) interface 
-   [**IDWriteRemoteFontFileStream**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwriteremotefontfilestream) interface 
-   [**IDWriteAsyncResult**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwriteasyncresult) interface 
-   [**IDWriteFactory5::AnalyzeContainerType**](/windows/win32/api/dwrite_3/nf-dwrite_3-idwritefactory5-analyzecontainertype) method 
-   [**IDWriteFactory5::UnpackFontFile**](/windows/win32/api/dwrite_3/nf-dwrite_3-idwritefactory5-unpackfontfile) method 

 

## Key concepts

To understand the DirectWrite APIs for working with custom fonts, it can be helpful to understand the conceptual model that underlies these APIs. Key concepts will be described here. 

When DirectWrite does actual text layout or rendering, it needs to access actual font data. A font face object holds actual font data, which must exist in the local system. But for other operations, such as checking availability of a particular font, or presenting font choices to a user, all that is needed is a reference to a particular font, not the actual font data itself. In DirectWrite, a font face reference object holds just the information needed to locate and instantiate a font. Because the font face reference doesn’t hold actual data, DirectWrite can deal with font face references for which actual data is in a remote network location as well as when the actual data is local.

A font set is a set of font face references, along with certain basic, informational properties that can be used in referring to the font or in comparing it to other fonts, such as the family name, or a font-weight value. The actual data for the various fonts may be local, or it may all be remote, or some mixture.

A font set can be used to obtain a corresponding font collection object. See Font sets and font collections below for more details. 

The IDWriteFontSet interface provides methods that allow querying for property values such as family name or font-weight, or for font face references that match particular property values. After filtering down to a particular selection, an instance of the [**IDWriteFontFaceReference**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontfacereference) interface can be obtained, with methods for downloading (if the actual font data is currently remote), for obtaining the corresponding [**IDWriteFontFace3**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontface3) object that can be used for layout and rendering. 

The IDWriteFontFile interface underlies each font face or font face reference. This represents the location of a font file, and has two components: a font file loader, and a font file key. The font file loader ([**IDWriteFontFileLoader**](/windows/win32/api/dwrite/nn-dwrite-idwritefontfileloader)) is used to open a file if needed, and returns a stream with the data ([**IDWriteFontFileStream**](/windows/win32/api/dwrite/nn-dwrite-idwritefontfilestream)). Depending on the loader, the data may be located at a local file path, a remote URL, or in a memory buffer. The key is a loader-defined value that uniquely identifies the file within the loader context, allowing the loader to locate the data and create a stream for it. 

Custom fonts can easily be added to a custom font set, which in turn can be used for filtering or organizing font information for purposes such as creating a font-picker user interface. The font set can also be used to create a font collection for use in higher-level APIs like [**IDWriteTextFormat**](/windows/win32/api/dwrite/nn-dwrite-idwritetextformat) and [**IDWriteTextLayout**](/windows/win32/api/dwrite/nn-dwrite-idwritetextlayout). The [**IDWriteFontSetBuilder**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontsetbuilder) interface can be used to create a custom font set that includes several custom fonts. It can also be used to create a custom font set that mixes custom fonts and system-provided fonts; or that mixes fonts with different sources for the actual data — local storage, remote URLs, and memory. 

As mentioned, a font face reference may refer to font data at a remote source, but the data must be local in order to obtain a font face object that can be used for layout and rendering. Downloading of remote data is handled by a font download queue. Apps can use the [**IDWriteFontDownloadQueue**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontdownloadqueue) interface to enqueue requests to download remote fonts to initiate the download process, and to register an [**IDWriteFontDownloadListener**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontdownloadlistener) object to take action when the download process has completed. 

For most of the interfaces described here, DirectWrite provides system implementations. The one exception is the [**IDWriteFontDownloadListener**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontdownloadlistener) interface, which an app implements to take app-specific actions when remote fonts have been downloaded locally. Apps may have reason to provide their own custom implementations for certain other interfaces, though that would only be needed in specific, more advanced scenarios. For example, an app would need to provide a custom implementation of the [**IDWriteFontFileLoader**](/windows/win32/api/dwrite/nn-dwrite-idwritefontfileloader) interface to handle font files in local storage that use the WOFF2 container format. Additional details will be provided below. 

## Fonts and font file formats

Another key concept that is helpful to understand is the relationship between individual font faces and font files that contain them. The idea of an OpenType font file (.ttf or .otf) containing a single font is familiar. But the OpenType font format also allows for an OpenType Font Collection (.ttc or .otc), which is a single file that contains multiple fonts. OpenType Collection files are often used for large fonts that are closely related and have identical values for certain font data: by combining the fonts in a single file, the common data can be de-duplicated. For this reason, a font face or font face reference needs to refer not only to a font file (or equivalent data source), but it must also specify a font index within that file, for the general case in which the file may be a Collection file. 

For fonts used on the Web, font data is often packed into certain container formats, WOFF or WOFF2, which provide some compression of the font data and some level of protection against piracy and violation of font licenses. Functionally, a WOFF or WOFF2 file is equivalent to an OpenType font or Font Collection file, but the data is encoded in a different format that requires unpacking before it can be used. 

Certain DirectWrite APIs may deal with individual font faces, while other APIs can handle files that might include OpenType Collection files that contain multiple faces. Similarly, certain APIs deal only with raw, OpenType-format data, while other APIs can handle the packed, WOFF and WOFF2 container formats. These details are provided in the discussion below. 

## Font sets and font collections

Some applications may be implemented to work with fonts using the [**IDWriteFontCollection**](/windows/win32/api/dwrite/nn-dwrite-idwritefontcollection) interface. There is a direct correspondence between a font collection and a font set. Each can hold the same fonts, but they present them with a different organization. From any font collection, a corresponding font set can be obtained, and vice versa.

When working with a number of custom fonts, it is easiest to use a font set builder interface to create a custom font set, and then obtain a font collection after the font set is created. The process for creating a custom font set will be described in detail below. To obtain an [**IDWriteFontCollection1**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontcollection1) interface from a font set, the [**IDWriteFactory3::CreateFontCollectionFromFontSet**](/windows/win32/api/dwrite_3/nf-dwrite_3-idwritefactory3-createfontcollectionfromfontset) method is used.

If the app has a collection object and needs to obtain a corresponding font set, this can be done using the [**IDWriteFontCollection1::GetFontSet**](/windows/win32/api/dwrite_3/nf-dwrite_3-idwritefontcollection1-getfontset) method. 

## Common scenarios

This section describes some of the most common scenarios involving custom font sets:

-   Creating a custom font set using arbitrary fonts at paths in the local file system.
-   Creating a custom font set using known fonts (perhaps bundled with the app) that are stored in the local file system.
-   Creating a custom font set using known, remote fonts on the Web.
-   Creating a custom font set using font data loaded into memory.

Complete implementations for these scenarios are provided in the [DirectWrite Custom Font Sets sample](https://github.com/Microsoft/Windows-classic-samples/tree/master/Samples/DirectWriteCustomFontSets/). That sample also illustrates one more advanced scenario for handling font data packed in WOFF or WOFF2 container formats, which will be discussed below. 

### Creating a font set using arbitrary fonts in the local file system

When dealing with an arbitrary set of font files in local storage, the [**IDWriteFontSetBuilder1::AddFontFile**](/windows/win32/api/dwrite_3/nf-dwrite_3-idwritefontsetbuilder1-addfontfile) method is convenient since, in a single call, it can handle all of the font faces within an OpenType Font Collection file, as well as all instances for an OpenType variable font. This is available in the Windows 10 Creators Update (preview build 15021 or later), and is recommended whenever available. 

To use this method, use the following process.

<dl> 1. Start by creating the <a href="/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefactory5">IDWriteFactory5</a> interface: 


```C++
IDWriteFactory5* pDWriteFactory; 
HRESULT hr = DWriteCreateFactory( 
  DWRITE_FACTORY_TYPE_SHARED, 
  __uuidof(IDWriteFactory5), 
  reinterpret_cast<IUnknown**>(&pDWriteFactory) 
); 
```



   
2. Use the factory to obtain the <a href=""></a>[**IDWriteFontSetBuilder1**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontsetbuilder1) interface: 


```C++
IDWriteFontSetBuilder1* pFontSetBuilder; 
if (SUCCEEDED(hr)) 
{ 
  hr = pDWriteFactory->CreateFontSetBuilder(&pFontSetBuilder); 
}  
                
```



  
3. For each font file in the local file system, create an [**IDWriteFontFile**](/windows/win32/api/dwrite/nn-dwrite-idwritefontfile) that refers to it: 


```C++
IDWriteFontFile* pFontFile; 
if (SUCCEEDED(hr)) 
{ 
  hr = pDWriteFactory->CreateFontFileReference(pFilePath, /* lastWriteTime*/ nullptr, &pFontFile); 
} 
```



   
4. Add the [**IDWriteFontFile**](/windows/win32/api/dwrite/nn-dwrite-idwritefontfile) object to the font set builder using the [**AddFontFile**](/windows/win32/api/dwrite_3/nf-dwrite_3-idwritefontsetbuilder1-addfontfile) method: 


```C++
hr = pFontSetBuilder->AddFontFile(pFontFile); 
```

If the file path specified in the call to [**CreateFontFileReference**](/windows/win32/api/dwrite/nf-dwrite-idwritefactory-createfontfilereference) referred to something other than a supported OpenType file, then the call to [**AddFontFile**](/windows/win32/api/dwrite_3/nf-dwrite_3-idwritefontsetbuilder1-addfontfile) will return an error, DWRITE\_E\_FILEFORMAT.

5. After all of the files have been added to the font set builder, the custom font set can be created: 


```C++
IDWriteFontSet* pFontSet; 
hr = pFontSetBuilder->CreateFontSet(&pFontSet); 
```



   
</dl>

If the app needs to run on Windows 10 versions earlier than the Windows 10 Creators Update, then the AddFontFile method will not be available. Availability can be detected by creating an [**IDWriteFactory3**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefactory3) interface and then using QueryInterface to try to obtain an [**IDWriteFactory5**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefactory5) interface: if this succeeds, then the [**IDWriteFontSetBuilder1**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontsetbuilder1) interface and [**AddFontFile**](/windows/win32/api/dwrite_3/nf-dwrite_3-idwritefontsetbuilder1-addfontfile) method will also be available.

If the AddFontFile method is not available, then the [**IDWriteFontSetBuilder::AddFontFaceReference**](/windows/win32/api/dwrite_3/nf-dwrite_3-idwritefontsetbuilder-addfontfacereference(idwritefontfacereference)) method must be used to add individual font faces. To allow for OpenType Font Collection files that contain multiple faces, the [**IDWriteFontFile::Analyze**](/windows/win32/api/dwrite/nf-dwrite-idwritefontfile-analyze) method can be used to determine the number of faces contained within the file. The process is as follows.

<dl> 1. Start by creating the <a href="/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefactory3">IDWriteFactory3</a> interface: 


```C++
IDWriteFactory3* pDWriteFactory; 
HRESULT hr = DWriteCreateFactory( 
DWRITE_FACTORY_TYPE_SHARED, 
  __uuidof(IDWriteFactory5), 
  reinterpret_cast<IUnknown**>(&pDWriteFactory) 
); 
```



  
2. Use the factory to obtain the [**IDWriteFontSetBuilder**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontsetbuilder) interface: 


```C++
IDWriteFontSetBuilder* pFontSetBuilder; 
if (SUCCEEDED(hr)) 
{ 
  hr = pDWriteFactory->CreateFontSetBuilder(&pFontSetBuilder); 
} 
```



  
3. For each font file, create an [**IDWriteFontFile**](/windows/win32/api/dwrite/nn-dwrite-idwritefontfile), as above: 


```C++
IDWriteFontFile* pFontFile; 
if (SUCCEEDED(hr)) 
{ 
  hr = pDWriteFactory->CreateFontFileReference(pFilePath, /* lastWriteTime*/ nullptr, &pFontFile); 
} 
```



Instead of adding the file directly to the font set builder, we need to determine the number of faces and create individual [**IDWriteFontFaceReference**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontfacereference) objects.   
4. Use the [**Analyze**](/windows/win32/api/dwrite/nf-dwrite-idwritefontfile-analyze) method to get the number of faces in the file. 


```C++
BOOL isSupported; 
DWRITE_FONT_FILE_TYPE fileType; 
UINT32 numberOfFonts; 
hr = pFontFile->Analyze(&isSupported, &fileType, /* face type */ nullptr, &numberOfFonts); 
```



The [**Analyze**](/windows/win32/api/dwrite/nf-dwrite-idwritefontfile-analyze) method will also set values for the isSupported and fileType parameters. If the file is not a supported format, then isSupported will be FALSE, and appropriate action, such as ignoring the file, can be taken.   
5. Loop over the number of fonts set in the numberOfFonts parameter. Within the loop, create an [**IDWriteFontFaceReference**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontfacereference) for each file/index pair, and add that to the font set builder. 


```C++
for (uint32_t fontIndex = 0; fontIndex < numberOfFonts; fontIndex++) 
{ 
  IDWriteFontFaceReference* pFontFaceReference;
  hr = pDWriteFactory->CreateFontFaceReference(pFontFile, fontIndex, DWRITE_FONT_SIMULATIONS_NONE, &pFontFaceReference);

  if (SUCCEEDED(hr))
  {
    hr = pFontSetBuilder->AddFontFaceReference(pFontFaceReference);
  }
} 
```



  
6. After all the faces have been added to the font set builder, create the custom font set, as shown above.  
</dl>

An app can be designed so that it will use the preferred [**AddFontFile**](/windows/win32/api/dwrite_3/nf-dwrite_3-idwritefontsetbuilder1-addfontfile) method when running on the Windows 10 Creators Update, but fall back to use the [**AddFontFaceReference**](/windows/win32/api/dwrite_3/nf-dwrite_3-idwritefontsetbuilder-addfontfacereference(idwritefontfacereference)) method when running on earlier Windows 10 versions. Test for availability of the [**IDWriteFactory5**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefactory5) interface, as described above, and then branch accordingly. This approach is illustrated in the [DirectWrite Custom Font Sets sample](https://github.com/Microsoft/Windows-classic-samples/tree/master/Samples/DirectWriteCustomFontSets/). 

### Creating a font set using known fonts in the local file system

As mentioned above, each font face reference in a font set is associated with certain informational properties, such as family name and font weight. When custom fonts are added to a font set builder using the API calls listed above, these informational properties are obtained directly from the actual font data, which is read as the font is added. In some situations, however, if an app has another source of information about a font, it might wish to provide its own custom values for these properties. 

As an example of how this might be useful, suppose an app bundles some fonts that are used for presenting particular user-interface elements within the app. At times, such as with a new app version, the specific fonts that the app uses for these elements may need to change. If the app has encoded references to the specific fonts, then replacement of one font with another will require changing every one of those references. Instead, if the app uses custom properties to assign functional aliases based on the type of element or text being rendered, maps each alias to a specific font in one place and then uses the aliases in all the contexts where fonts are created and manipulated, then replacing one font with another requires only changing the one place where the alias is mapped to a specific font. 

Custom values for informational properties can be assigned when the [**IDWriteFontSetBuilder::AddFontFaceReference**](/windows/win32/api/dwrite_3/nf-dwrite_3-idwritefontsetbuilder-addfontfacereference(idwritefontfacereference)) method is called. The method for doing this is as follows; this can be used on any Windows 10 version. 

As shown above, start by obtaining the [**IDWriteFactory3**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefactory3) and [**IDWriteFontSet**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontset) interfaces. For each custom font face to be added, create an [**IDWriteFontFaceReference**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontfacereference), as shown above. Before this is added to the font set builder (within the loop in step 5, shown above), however, the app defines the custom property values to be used. 

A set of custom property values is defined using an array of [**DWRITE\_FONT\_PROPERTY**](/windows/win32/api/dwrite_3/ns-dwrite_3-dwrite_font_property) structures. Each of these identifies a particular property from the [**DWRITE\_FONT\_PROPERTY\_ID**](/windows/win32/api/dwrite_3/ne-dwrite_3-dwrite_font_property_id) enum, and the corresponding property value that is to be used.  

Note that all property values are assigned as strings. If these may later be displayed to users, then alternate values for a given property for different languages may be set, but this is not required. Also note that if any custom property values are set by the app, then only those values that are specified will be used within the Font set; DirectWrite will not derive any values directly from the font for informational properties used in a font set. 

The following example defines custom values for three informational properties: family name, full name, and font weight. 


```C++
DWRITE_FONT_PROPERTY props[] = 
{ 
  { DWRITE_FONT_PROPERTY_ID_FAMILY_NAME, L"My Icon Font", L"en-US" }, 
  { DWRITE_FONT_PROPERTY_ID_FULL_NAME, L"My Icon Font", L"en-US" }, 
  { DWRITE_FONT_PROPERTY_ID_WEIGHT, L"400", nullptr } 
}; 
               
            
```



After defining the desired array of property values for a font, make a call to AddFontFaceRefence, passing the property array as well as the font face reference. 


```C++
hr = pFontSetBuilder->AddFontFaceReference(pFontFaceReference, props, ARRAYSIZE(props)); 
```



 

Once all custom font faces have been added to the font set builder, along with their custom properties, create the custom font set, as shown above. 

### Creating a custom font set using known, remote fonts on the Web

Custom properties are important for working with remote fonts. Each font face reference must have some informational properties to characterize the font and distinguish it from other fonts. Since the font data for remote fonts is not local, DirectWrite cannot derive properties directly from the font data. Hence, properties must be provided explicitly when adding a remote font to the font set builder.

The sequence of API calls for adding remote fonts to a font set is similar to the sequence described for the previous scenario. Since the font data is remote, however, the operations involved for reading the actual font data will be different than when working with files in local storage. For this situation, a new lower-level interface, [**IDWriteRemoteFontFileLoader**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwriteremotefontfileloader), has been added in the Windows 10 Creators Update. 

To use the remote font file loader, it must first be registered with a DirectWrite factory. The loader will need to be held by the app for as long as the fonts associated with it are being used. Once the fonts are no longer in use, and at some point before the factory is destroyed, the loader must be unregistered. This can be done in the destructor for the class that owns the loader object. These steps will be shown below. 

The method for creating a custom font set using remote fonts is as follows; this requires the Windows 10 Creators Update.  

<dl> 1. Create an IDWriteFactory5 interface, as shown above.   
2. Create an <a href="/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontsetbuilder">IDWriteFontSetBuilder</a> interface, as shown above.   
3. Use the factory to obtain an <a href="/windows/win32/api/dwrite_3/nn-dwrite_3-idwriteremotefontfileloader">IDWriteRemoteFontFileLoader</a>. 


```C++
IDWriteRemoteFontFileLoader* pRemoteFontFileLoader; 
if (SUCCEEDED(hr)) 
{ 
    hr = pDWriteFactory->CreateHttpFontFileLoader( 
        /* referrerURL */ nullptr, 
        /* extraHeaders */ nullptr, 
        &pRemoteFontFileLoader 
    ); 
} 
```



This returns a system-provided implementation of the remote font file loader interface that is able to handle HTTP interactions for downloading font data on behalf of the app. A referrer URL or extra headers can be specified if required by the font service or services that are the source for the fonts.    

> [!IMPORTANT]
> Security note: When an attempt is made to fetch a remote font, the potential exists for an attacker to spoof the intended server that will be called. In that case, the target and referrer URLs and header details would be disclosed to the attacker. App developers are responsible for mitigating this risk. Use of the HTTPS protocol, rather than HTTP, is recommended. 

 

A single remote font file loader can be used for multiple fonts, though different loaders can be used if fonts are obtained from multiple services that have different requirements for referrer URL or extra headers.   
4. Register the remote font file loader with the factory. 


```C++
 if (SUCCEEDED(hr)) 
 { 
     hr = pDWriteFactory->RegisterFontFileLoader(pRemoteFontFileLoader); 
 } 
```



From this point, the steps for creating the custom font set are similar to those described for known, local font files, with two important exceptions. First, the [**IDWriteFontFile**](/windows/win32/api/dwrite/nn-dwrite-idwritefontfile) object is created using the remote font file loader interface rather than using the factory. Second, the Analyze method cannot be used since the font data is not local. Instead, the app must know whether the remote font file is an OpenType Font Collection file, and if so, then it must know which of the fonts within the collection it will use, and the index for each. Hence, the remaining steps are as follows.   
5. For each remote font file, use the remote font file loader interface to create an [**IDWriteFontFile**](/windows/win32/api/dwrite/nn-dwrite-idwritefontfile), specifying the URL required to access the font file. 


```C++
 IDWriteFontFile* pFontFile; 
 hr = pRemoteFontFileLoader->CreateFontFileReferenceFromUrl( 
     pDWriteFactory, 
     /* baseUrl */ L"https://github.com/", 
     /* fontFileUrl */ L"winjs/winjs/blob/master/src/fonts/Symbols.ttf?raw=true", 
     &pFontFile 
 ); 
```



Note that the complete URL can be specified in the fontFileUrl parameter, or it can be split into base and relative portions. If a base URL is specified, then the concatenation of the baseUrl and fontFileUrl values must provide the complete URL — DirectWrite will not supply any additional delimiter.  

> [!IMPORTANT]
> Security / performance note: When an attempt is made to fetch a remote font, there is no guarantee that Windows will receive a response from the server. In some cases, a server may respond with a file-not-found error for an invalid relative URL, but stop responding if it receives multiple invalid requests. If the server does not respond, Windows will eventually time out, though this may take several minutes if multiple fetches are initiated. You should do what you can to ensure that URLs will be valid when calls are made. 

 

Also note that the URL can point to a raw OpenType font file (.ttf, .otf, .ttc, .otc), but it can also point to fonts in a WOFF or WOFF2 container file. If a WOFF or WOFF2 file is referenced, then the DirectWrite implementation of the remote font file loader will automatically unpack the font data from the container file.   
6. For each font face index within the remote font file that is to be used, create an [**IDWriteFontFaceReference**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontfacereference). 


```C++
 IDWriteFontFaceReference* pFontFaceReference; 
 hr = pDWriteFactory->CreateFontFaceReference(pFontFile, /* faceIndex */ 0, DWRITE_FONT_SIMULATIONS_NONE, &pFontFaceReference);
```



  
7. Define custom properties for the font face, as shown above.   
8. Add the font face reference along with custom properties to the font set builder, as shown above.   
9. After all fonts have been added to the font set builder, create the font set, as shown above.   
10. At some point when the remote fonts will no longer be used, unregister the remote font file loader. 


```C++
hr = pDWriteFactory->UnregisterFontFileLoader(pRemoteFontFileLoader); 
```



  
</dl>

Once a custom font set with custom remote fonts is created, the font set contains references and informational properties for the remote fonts, but the actual data is still remote. DirectWrite support for remote fonts allows a font face reference to be maintained in the font set, and for a font to be selected for use in layout and rendering, but that the actual data is not downloaded until there is an actual need to use it, such as when text layout will be performed.  

An app can take an up-front approach by requesting that DirectWrite download the font data and then waiting for confirmation of a successful download before any processing with the font is begun. But a network download implies some latency of unpredictable duration, and success is also uncertain. For this reason, it will usually be better to take a different approach, allowing layout and rendering to be done initially using alternate or fallback fonts that are already local, while requesting download of the desired, remote font in parallel, and then updating the results once the desired font has been downloaded. 

To request that the entire font be downloaded before it gets used, the [**IDWriteFontFaceReference::EnqueueFontDownloadRequest**](/windows/win32/api/dwrite_3/nf-dwrite_3-idwritefontfacereference-enqueuefontdownloadrequest) method can be used. If the font is very large, only a portion of the data may be needed for processing particular strings. DirectWrite provides additional methods that can be used to request portions of the font data needed for particular content, [**EnqueueCharacterDownloadRequest**](/windows/win32/api/dwrite_3/nf-dwrite_3-idwritefontfacereference-enqueuecharacterdownloadrequest) and [**EnqueueGlyphDownloadRequest**](/windows/win32/api/dwrite_3/nf-dwrite_3-idwritefontfacereference-enqueueglyphdownloadrequest).  

Suppose the approach to be taken in the app is to allow processing to be done initially using local, alternate or fallback fonts. The IDWriteFontFallback::[**MapCharacters**](idwritefontfallback-mapcharacters.md) method can be used to identify local fallback fonts, and it will also automatically enqueue a request to download the preferred font. Also, if [**IDWriteTextLayout**](/windows/win32/api/dwrite/nn-dwrite-idwritetextlayout) is used and some or all of the text in the layout is formatted using a remote font reference, then DirectWrite will automatically use the **MapCharacters** method to get local fallback fonts and to enqueue a request to download the remote font data. 

DirectWrite maintains a font download queue for each factory, and the requests made using the methods mentioned above get added to that queue. The font download queue can be obtained using the [**IDWriteFactory3::GetFontDownloadQueue**](/windows/win32/api/dwrite_3/nf-dwrite_3-idwritefactory3-getfontdownloadqueue) method. 

If a download request is made but the font data is already local, this will result in a no-op: Nothing will be added to the download queue. An app can check whether the queue is empty or there are pending download requests by calling the [**IDWriteFontDownloadQueue::IsEmpty**](/windows/win32/api/dwrite_3/nf-dwrite_3-idwritefontdownloadqueue-isempty) method. 

After remote font requests have been added to the queue, the download process must be initiated. When remote fonts are used in [**IDWriteTextLayout**](/windows/win32/api/dwrite/nn-dwrite-idwritetextlayout), the download will be initiated automatically when the app calls **IDWriteTextLayout** methods that force layout or rendering operations, such as the GetLineMetrics or Draw methods. In other scenarios, the app must initiate the download directly by calling [**IDWriteFontDownloadQueue::BeginDownload**](/windows/win32/api/dwrite_3/nf-dwrite_3-idwritefontdownloadqueue-begindownload).  

When a download is completed, it will be up to the app to take appropriate actions — proceeding with pending operations, or repeating operations that were done initially with fallback fonts. (If DirectWrite’s text layout is being used, then [**IDWriteTextLayout3::InvalidateLayout**](idwritetextlayout3-invalidatelayout.md) can be used to clear the temporary results computed using fallback fonts.) In order for the app to be notified when the download process has completed and to take appropriate actions, the app must provide an implementation of the [**IDWriteFontDownloadListener**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontdownloadlistener) interface, and pass this into the BeginDownload call. 

> [!IMPORTANT]
> Security / performance note: When an attempt is made to fetch a remote font, there is no guarantee that Windows will receive a response from the server. If the server does not respond, Windows will eventually time out, though this may take several minutes if multiple remote fonts are being fetched but failing. The BeginDownload call will return immediately. Apps should not block UI while waiting for [**IDWriteFontDownloadListener::DownloadCompleted**](/windows/win32/api/dwrite_3/nf-dwrite_3-idwritefontdownloadlistener-downloadcompleted) to be called. 

 

Sample implementations of these interactions with DirectWrite’s font download queue and of the [**IDWriteFontDownloadListener**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontdownloadlistener) interface can be seen in the [DirectWrite Custom Font Sets sample](https://github.com/Microsoft/Windows-classic-samples/tree/master/Samples/DirectWriteCustomFontSets/), and also in the [DirectWrite Downloadable Fonts sample](https://github.com/Microsoft/Windows-universal-samples/tree/master/Samples/DWriteTextLayoutCloudFont). 

### Creating a custom font set using font data loaded into memory

Just as the low-level operations for reading data from a font file are different for files on a local disk versus remote files on the Web, the same is also true for font data loaded into a memory buffer. A new low-level interface for handling in-memory font data has been added in the Windows 10 Creators Update, [**IDWriteInMemoryFontFileLoader**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwriteinmemoryfontfileloader). 

As with a remote font file loader, an in-memory font file loader must first be registered with a DirectWrite factory. The loader will need to be held by the app for as long as the fonts associated with it are being used. Once the fonts are no longer in use, and at some point before the factory is destroyed, the loader must be unregistered. This can be done in the destructor for the class that owns the loader object. These steps will be shown below. 

If the app has separate information about the font faces represented by the data, it can add individual font face references to a font set builder with custom properties specified. Since the font data is in local memory, however, this is not required; DirectWrite will be able to read the data directly to derive the property values. 

DirectWrite assumes the font data is in raw, OpenType format, equivalent to an OpenType file (.ttf, .otf, .ttc, .otc), but in memory rather than on disk. The data cannot be in a WOFF or WOFF2 container format. The data can represent an OpenType Font Collection. If custom properties are not being used, then the [**IDWriteFontSetBuilder1::AddFontFile**](/windows/win32/api/dwrite_3/nf-dwrite_3-idwritefontsetbuilder1-addfontfile) method can be used to add all font faces in the data in a single call. 

An important consideration for the in-memory scenario is the lifetime of the data. If a pointer to the buffer is provided to DirectWrite without a clear indication that there is an owner, then DirectWrite will make a copy of the data into a new memory buffer that it will own. To avoid copying of data and additional memory allocation, the app can pass a data-owner object that implements IUnknown, and that owns the memory buffer containing the font data. By implementing this interface, DirectWrite can add to the ref count of the object, thereby ensuring the lifetime of the owned data. 

The method for creating a custom font set using in-memory font data is as follows; this requires the Windows 10 Creators Update. This will assume an app-implemented data-owner object, that implements IUnknown and also has methods that return a pointer to the memory buffer and the size of the buffer. 

<dl> 1. Create an IDWriteFactory5 interface, as shown above.  
2. Create an [**IDWriteFontSetBuilder1**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontsetbuilder1) interface, as shown above.  
3. Use the factory to obtain an IDWriteInMemoryFontFileLoader. 


```C++
 IDWriteInMemoryFontFileLoader* pInMemoryFontFileLoader; 
if (SUCCEEDED(hr)) 
{ 
    hr = pDWriteFactory->CreateInMemoryFontFileLoader(&pInMemoryFontFileLoader); 
}
```



This returns a system-provided implementation of the in-memory font file loader interface.   
4. Register the in-memory font file loader with the factory. 


```C++
if (SUCCEEDED(hr)) 
{ 
    hr = pDWriteFactory->RegisterFontFileLoader(pInMemoryFontFileLoader); 
}
```



   
5. For each in-memory font file, use the in-memory font file loader to create an [**IDWriteFontFile**](/windows/win32/api/dwrite/nn-dwrite-idwritefontfile). 


```C++
IDWriteFontFile* pFontFile; 
hr = pInMemoryFontFileLoader->CreateInMemoryFontFileReference( 
    pDWriteFactory, 
    pFontDataOwner->fontData /* returns void* */, 
    pFontDataOwner->fontDataSize /* returns UINT32 */, 
    pFontDataOwner /* ownerObject, owns the memory with font data and implements IUnknown */, 
    &pFontFile 
); 
```



   
6. Add the [**IDWriteFontFile**](/windows/win32/api/dwrite/nn-dwrite-idwritefontfile) object to the font set builder using the [**AddFontFile**](/windows/win32/api/dwrite_3/nf-dwrite_3-idwritefontsetbuilder1-addfontfile) method, as shown above.  If there is a need, the app can instead create individual [**IDWriteFontFaceReference**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontfacereference) objects based on the **IDWriteFontFile**, optionally define custom properties for each font face reference, and then add the font face reference with custom properties to the font set using the [**AddFontFaceReference**](/windows/win32/api/dwrite_3/nf-dwrite_3-idwritefontsetbuilder-addfontfacereference(idwritefontfacereference)) method, as shown above.   
7. After all fonts have been added to the font set builder, create the custom font set, as shown above.   
8. At some point when the in-memory fonts will no longer be used, unregister the in-memory font file loader. 


```C++
hr = pDWriteFactory->UnregisterFontFileLoader(pInMemoryFontFileLoader);
```



  
</dl>

 

## Advanced scenarios

Some apps may have special requirements that require more advanced processing than is described above. 

### Combining font sets

Some apps may need to create a font set that comprises some combination of items from other font sets. For example, an app may want to create a font set that combines all the fonts installed on the system with a selection of custom fonts, or that combines installed fonts matching certain criteria with other fonts. DirectWrite has APIs to support manipulation and combining of font sets. 

To combine two or more font sets, the [**IDWriteFontSetBuilder::AddFontSet**](/windows/win32/api/dwrite_3/nf-dwrite_3-idwritefontsetbuilder-addfontset) method adds all of the fonts in given font set to be added to a font set builder in a single call. If only certain fonts from an existing font set are wanted in the new font set, the [**IDWriteFontSet::GetMatchingFonts**](idwritefontset-getmatchingfonts-overload.md) method can be used to derive a new font set object that has been filtered to include only fonts matching specified properties. These methods provide an easy way to create a custom font set combining fonts from two or more existing font sets 

### Using local WOFF or WOFF2 font data

If an app has font files in the local file system or in a memory buffer, but they use the WOFF or WOFF2 container formats, DirectWrite (Windows 10 Creator Update or later) provides a method for unpacking the container format, [**IDWriteFactory5::UnpackFontFile**](/windows/win32/api/dwrite_3/nf-dwrite_3-idwritefactory5-unpackfontfile), which returns an [**IDWriteFontFileStream**](/windows/win32/api/dwrite/nn-dwrite-idwritefontfilestream). 

However, the app will need a way to get the [**IDWriteFontFileStream**](/windows/win32/api/dwrite/nn-dwrite-idwritefontfilestream) into a font file loader object. One way to do this is to create a custom [**IDWriteFontFileLoader**](/windows/win32/api/dwrite/nn-dwrite-idwritefontfileloader) implementation that wraps the stream. As with other font file loaders, this must be registered before use, and unregistered before the factory goes out of scope.  

If the custom loader will also be used with raw (not packed) font files, then the app would also need to provide a custom implementation of the [**IDWriteFontFileStream**](/windows/win32/api/dwrite/nn-dwrite-idwritefontfilestream) interface for handling those files. There are easier ways that use APIs discussed above for handling raw font files, however. The need for a custom stream implementation could be avoided by using separate code paths for packed font files versus raw font files. 

After a custom font file loader object is created, the packed font file data is added to the loader by app-specific means. The loader can handle multiple font files, each of which is identified using an app-defined key that is opaque to DirectWrite. After a packed font file has been added to the loader, the [**IDWriteFactory::CreateCustomFontFileReference**](/windows/win32/api/dwrite/nf-dwrite-idwritefactory-createcustomfontfilereference) method is used to obtain an [**IDWriteFontFile**](/windows/win32/api/dwrite/nn-dwrite-idwritefontfile) based on that loader for the font data identified by a given key.  

The actual unpacking of the font data can be done as fonts are added to the loader, but can also be handled in the [**IDWriteFontFileLoader::CreateStreamFromKey**](/windows/win32/api/dwrite/nf-dwrite-idwritefontfileloader-createstreamfromkey) method, which DirectWrite will call when it first needs to read the font data. 

After an IDWriteFontFile object has been created, remaining steps for adding the fonts to a custom font set will be as described above. 

An implementation using this approach is illustrated in the [DirectWrite Custom Font Sets sample](https://github.com/Microsoft/Windows-classic-samples/tree/master/Samples/DirectWriteCustomFontSets/). 

### Using DirectWrite remote font mechanisms with custom low-level network implementation

The DirectWrite mechanisms for handling remote fonts can be divided into higher-level mechanisms — having font sets that include font face references for remote fonts, checking locality of the font data, and managing the queue for font download requests — and the lower-level mechanisms that handle actual download. Some apps may want to utilize the higher-level remote font mechanisms, but also require custom network interactions, such as communicating with servers using protocols other than HTTP. 

For this situation, an app will need to create a custom implementation of the [**IDWriteRemoteFontFileLoader**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwriteremotefontfileloader) interface that interacts with other lower-level interfaces in the required ways. The app will also need to provide custom implementations of these lower-level interfaces: [**IDWriteRemoteFontFileStream**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwriteremotefontfilestream), and [**IDWriteAsyncResult**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwriteasyncresult). These three interfaces have callback methods that DirectWrite will call during download operations. 

When [**IDWriteFontDownloadQueue::BeginDownload**](/windows/win32/api/dwrite_3/nf-dwrite_3-idwritefontdownloadqueue-begindownload) is called, DirectWrite will make queries to the remote font file loader about locality of the data, and will request the remote stream. If data is not local, then it will call the stream’s BeginDownload method. The stream implementation should not block on that call, but should immediately return, passing back an [**IDWriteAsyncResult**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwriteasyncresult) object that provides the wait handle DirectWrite will use to wait on the asynchronous download operation. The custom stream implementation is responsible for handling the remote communication. When the completion event has occurred, then DirectWrite will call [**IDWriteAsyncResult::GetResult**](/windows/win32/api/dwrite_3/nf-dwrite_3-idwriteasyncresult-getresult) to determine the result of the operation. If the result is successful, then it’s expected that subsequent ReadFragment calls to the stream for the downloaded ranges will succeed. 

> [!IMPORTANT]
> Security / performance note: When an attempt is made to fetch a remote font, the potential exists in general for an attacker to spoof the intended server being called, or that the server may not respond. If you are implementing custom network interactions, you may have greater control over mitigations than when dealing with third-party servers. However, it is up to you to consider appropriate mitigations to avoid information disclosure or denial of service. Secure protocols such as HTTPS are recommended. Also, you should build in some timeout so that the event handle returned to DirectWrite does eventually get set. 

 

### Supporting scenarios on earlier Windows versions

The scenarios that have been described can be supported in DirectWrite on earlier versions of Windows, but would require much more custom implementation on the part of the app using the more limited APIs that were available prior to Windows 10. For more information, see [Custom Font Collections (Windows 7/8)](custom-font-collections.md).

 

 