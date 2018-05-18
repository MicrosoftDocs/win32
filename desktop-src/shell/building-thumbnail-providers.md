---
Description: 'As of Windows Vista, greater use is made of file-specific thumbnail images than in earlier versions of Windows.'
title: Building Thumbnail Handlers
---

# Building Thumbnail Handlers

As of Windows Vista, greater use is made of file-specific thumbnail images than in earlier versions of Windows. They are used in all views, in dialogs, and for any file type that provides them. Thumbnail display was also changed. A continuous spectrum of user-selectable sizes is available rather than the discrete sizes such as Icons and Thumbnails.

The [**IThumbnailProvider**](ithumbnailprovider.md) interface makes providing a thumbnail more straightforward than the older [**IExtractImage**](iextractimage.md) or [**IExtractImage2**](iextractimage2.md). Note, however, that existing code that uses **IExtractImage** or **IExtractImage2** is still valid and supported.

## The RecipeThumbnailProvider Sample

The [RecipeThumbnailProvider](samples-recipethumbnailprovider.md) sample dissected in this section is included in the Windows Software Development Kit (SDK). Its default install location is C:\\Program Files\\Microsoft SDKs\\Windows\\v6.0\\Samples\\WinUI\\Shell\\AppShellIntegration\\RecipeThumbnailProvider. However, the bulk of the code is included here as well.

The [RecipeThumbnailProvider](samples-recipethumbnailprovider.md) sample demonstrates the implementation of a thumbnail handler for a new file type registered with a .recipe extension. The sample illustrates the use of the different thumbnail handler APIs to register thumbnail extraction Component Object Model (COM) servers for custom file types. This topic walks you through the sample code, highlighting coding choices and guidelines.

A thumbnail handler must always implement [**IThumbnailProvider**](ithumbnailprovider.md) in concert with one of these interfaces:

-   [**IInitializeWithStream**](iinitializewithstream.md)
-   [**IInitializeWithItem**](iinitializewithitem.md)
-   [**IInitializeWithFile**](iinitializewithfile.md)

There are cases where initialization with streams is not possible. In scenarios where your thumbnail handler does not implement [**IInitializeWithStream**](iinitializewithstream.md), it must opt out of running in the isolated process where the system indexer places it by default when there is a change to the stream. To opt out of the process isolation feature, set the following registry value.

```
HKEY_CLASSES_ROOT
   CLSID
      {The CLSID of your thumbnail handler}
         DisableProcessIsolation = 1
```

If you implement [**IInitializeWithStream**](iinitializewithstream.md) and do a stream-based initialization, your handler is more secure and reliable. Typically, disabling process isolation is only intended for legacy handlers; avoid disabling this feature for any new code. **IInitializeWithStream** should be your first choice of initialization interface whenever possible.

Because the image file in the sample is not embedded in the .recipe file and is not a part of its file stream, [**IInitializeWithItem**](iinitializewithitem.md) is used in the sample. The implementation of the [**IInitializeWithItem::Initialize**](iinitializewithitem-initialize.md) method simply passes its parameters to private class variables.

[**IThumbnailProvider**](ithumbnailprovider.md) has only one method—[**GetThumbnail**](ithumbnailprovider-getthumbnail.md)—that is called with the largest desired size of the image, in pixels. Although the parameter is named *cx*, its value is used as the maximum size of both the x and y dimensions of the image. If the retrieved thumbnail is not square, then the longer axis is limited by *cx* and the aspect ratio of the original image is preserved.

When it returns, [**GetThumbnail**](ithumbnailprovider-getthumbnail.md) provides a handle to the retrieved image. It also provides a value that indicates the color format of the image and whether it has valid alpha information.

The GetThumbnail implementation in the sample begins with a call to the private **\_GetBase64EncodedImageString** method.


```C++
IFACEMETHODIMP CRecipeThumbProvider::GetThumbnail(UINT cx, 
                                                  HBITMAP *phbmp, 
                                                  WTS_ALPHATYPE *pdwAlpha)
{
    PWSTR pszBase64EncodedImageString;
    HRESULT hr = _GetBase64EncodedImageString(cx, &amp;pszBase64EncodedImageString);
```



The .recipe file type is simply an XML file registered as a unique file name extension. It includes an element called **Picture** that provides the relative path and file name of the image to use as the thumbnail for this particular .recipe file. The **Picture** element consists of the **Source** attribute that specifies a base 64 encoded image, and an optional **Size** attribute.

**Size** has two values, Small and Large. This allows you to provide multiple **Picture** nodes with separate images. The image retrieved then depends on the maximum size value (*cx*) provided in the call to [**GetThumbnail**](ithumbnailprovider-getthumbnail.md). Because Windows never sizes the image any larger than its maximum size, different images can be provided for different resolutions. However, for simplicity, the sample omits the **Size** attribute and provides only one image for all situations.

The **\_GetBase64EncodedImageString** method, whose implementation is shown here, uses XML Document Object Model (DOM) APIs to retrieve the **Picture** node. From that node it extracts the image from the **Source** attribute data.


```C++
HRESULT CRecipeThumbProvider::_GetBase64EncodedImageString(UINT /* cx */, 
                                                           PWSTR *ppszResult)
{
    *ppszResult = NULL;

    IXMLDOMDocument *pXMLDoc;
    HRESULT hr = _LoadXMLDocument(&amp;pXMLDoc);
    if (SUCCEEDED(hr))
    {
        BSTR bstrQuery = SysAllocString(L"Recipe/Attachments/Picture");
        hr = bstrQuery ? S_OK : E_OUTOFMEMORY;
        if (SUCCEEDED(hr))
        {
            IXMLDOMNode *pXMLNode;
            hr = pXMLDoc->selectSingleNode(bstrQuery, &amp;pXMLNode);
            if (SUCCEEDED(hr))
            {
                IXMLDOMElement *pXMLElement;
                hr = pXMLNode->QueryInterface(&amp;pXMLElement);
                if (SUCCEEDED(hr))
                {
                    BSTR bstrAttribute = SysAllocString(L"Source");
                    hr = bstrAttribute ? S_OK : E_OUTOFMEMORY;
                    if (SUCCEEDED(hr))
                    {
                        VARIANT varValue;
                        hr = pXMLElement->getAttribute(bstrAttribute, &amp;varValue);
                        if (SUCCEEDED(hr))
                        {
                            if ((varValue.vt == VT_BSTR) &amp;&amp; varValue.bstrVal &amp;&amp; varValue.bstrVal[0])
                            {
                                hr = SHStrDupW(varValue.bstrVal, ppszResult);
                            }
                            else
                            {
                                hr = E_FAIL;
                            }
                            VariantClear(&amp;varValue);
                        }
                        SysFreeString(bstrAttribute);
                    }
                    pXMLElement->Release();
                }
                pXMLNode->Release();
            }
            SysFreeString(bstrQuery);
        }
        pXMLDoc->Release();
    }
    return hr;
}
```



[**GetThumbnail**](ithumbnailprovider-getthumbnail.md) then passes the retrieved string to **\_GetStreamFromString**.


```C++
IFACEMETHODIMP CRecipeThumbProvider::GetThumbnail(UINT cx, 
                                                  HBITMAP *phbmp, 
                                                  WTS_ALPHATYPE *pdwAlpha)
{
    PWSTR pszBase64EncodedImageString;
    HRESULT hr = _GetBase64EncodedImageString(cx, &amp;pszBase64EncodedImageString);
    if (SUCCEEDED(hr))
    {
        IStream *pImageStream;
        hr = _GetStreamFromString(pszBase64EncodedImageString, &amp;pImageStream);
```



The **\_GetStreamFromString** method, whose implementation is shown here, which converts the encoded image to a stream.


```C++
HRESULT CRecipeThumbProvider::_GetStreamFromString(PCWSTR pszImageName, 
                                                   IStream **ppImageStream)
{
    HRESULT hr = E_FAIL;

    DWORD dwDecodedImageSize = 0;
    DWORD dwSkipChars        = 0;
    DWORD dwActualFormat     = 0;

    // Base64-decode the string
    BOOL fSuccess = CryptStringToBinaryW(pszImageName, 
                                         NULL, 
                                         CRYPT_STRING_BASE64,
                                         NULL, 
                                         &amp;dwDecodedImageSize, 
                                         &amp;dwSkipChars, 
                                         &amp;dwActualFormat);
    if (fSuccess)
    {
        BYTE *pbDecodedImage = (BYTE*)LocalAlloc(LPTR, dwDecodedImageSize);
        if (pbDecodedImage)
        {
            fSuccess = CryptStringToBinaryW(pszImageName, 
                                            lstrlenW(pszImageName), 
                                            CRYPT_STRING_BASE64,
                                            pbDecodedImage, 
                                            &amp;dwDecodedImageSize, 
                                            &amp;dwSkipChars, 
                                            &amp;dwActualFormat);
            if (fSuccess)
            {
                *ppImageStream = SHCreateMemStream(pbDecodedImage, 
                                                   dwDecodedImageSize);
                if (*ppImageStream != NULL)
                {
                    hr = S_OK;
                }
            }
            LocalFree(pbDecodedImage);
        }
    }
    return hr;
}
```



**GetThumbnail** then uses Windows Imaging Component (WIC) APIs to extract a bitmap from the stream and get a handle to that bitmap. The alpha information is set, WIC is properly exited, and the method terminates successfully.


```C++
IFACEMETHODIMP CRecipeThumbProvider::GetThumbnail(UINT cx, 
                                                  HBITMAP *phbmp, 
                                                  WTS_ALPHATYPE *pdwAlpha)
{
    PWSTR pszBase64EncodedImageString;
    HRESULT hr = _GetBase64EncodedImageString(cx, &amp;pszBase64EncodedImageString);
    if (SUCCEEDED(hr))
    {
        IStream *pImageStream;
        hr = _GetStreamFromString(pszBase64EncodedImageString, &amp;pImageStream);
        if (SUCCEEDED(hr))
        {
            hr = WICCreate32BitsPerPixelHBITMAP(pImageStream, 
                                                cx, 
                                                phbmp, 
                                                pdwAlpha);;

            pImageStream->Release();
        }
        CoTaskMemFree(pszBase64EncodedImageString);
    }
    return hr;
}
```



## Related topics

<dl> <dt>

[Thumbnail Handlers](thumbnail-providers.md)
</dt> <dt>

[Thumbnail Handler Guidelines](thumbnail-provider-guidelines.md)
</dt> <dt>

[**IID\_PPV\_ARGS**](iid-ppv-args.md)
</dt> </dl>

 

 



