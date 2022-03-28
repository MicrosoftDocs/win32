---
description: As of Windows Vista, greater use is made of file-specific thumbnail images than in earlier versions of Windows.
title: Building Thumbnail Handlers
ms.topic: article
ms.date: 05/31/2018
ms.assetid: 218264a9-ed26-4049-a721-232943f6ec53
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# Building Thumbnail Handlers

As of Windows Vista, greater use is made of file-specific thumbnail images than in earlier versions of Windows. They are used in all views, in dialogs, and for any file type that provides them. Thumbnail display was also changed. A continuous spectrum of user-selectable sizes is available rather than the discrete sizes such as Icons and Thumbnails.

The [**IThumbnailProvider**](/windows/desktop/api/Thumbcache/nn-thumbcache-ithumbnailprovider) interface makes providing a thumbnail more straightforward than the older [**IExtractImage**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iextractimage) or [**IExtractImage2**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iextractimage2). Note, however, that existing code that uses **IExtractImage** or **IExtractImage2** is still valid and supported.

## The RecipeThumbnailProvider Sample

The [RecipeThumbnailProvider](samples-recipethumbnailprovider.md) sample dissected in this section is included in the Windows Software Development Kit (SDK). Its default install location is C:\\Program Files\\Microsoft SDKs\\Windows\\v6.0\\Samples\\WinUI\\Shell\\AppShellIntegration\\RecipeThumbnailProvider. However, the bulk of the code is included here as well.

The [RecipeThumbnailProvider](samples-recipethumbnailprovider.md) sample demonstrates the implementation of a thumbnail handler for a new file type registered with a .recipe extension. The sample illustrates the use of the different thumbnail handler APIs to register thumbnail extraction Component Object Model (COM) servers for custom file types. This topic walks you through the sample code, highlighting coding choices and guidelines.

A thumbnail handler must always implement [**IThumbnailProvider**](/windows/desktop/api/Thumbcache/nn-thumbcache-ithumbnailprovider) in concert with one of these interfaces:

- [**IInitializeWithStream**](/windows/desktop/api/Propsys/nn-propsys-iinitializewithstream)
- [**IInitializeWithItem**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-iinitializewithitem)
- [**IInitializeWithFile**](/windows/desktop/api/Propsys/nn-propsys-iinitializewithfile)

There are cases where initialization with streams is not possible. In scenarios where your thumbnail handler does not implement [**IInitializeWithStream**](/windows/desktop/api/Propsys/nn-propsys-iinitializewithstream), it must opt out of running in the isolated process where the system indexer places it by default when there is a change to the stream. To opt out of the process isolation feature, set the following registry value.

```
HKEY_CLASSES_ROOT
   CLSID
      {The CLSID of your thumbnail handler}
         DisableProcessIsolation = 1
```

If you implement [**IInitializeWithStream**](/windows/desktop/api/Propsys/nn-propsys-iinitializewithstream) and do a stream-based initialization, your handler is more secure and reliable. Typically, disabling process isolation is only intended for legacy handlers; avoid disabling this feature for any new code. **IInitializeWithStream** should be your first choice of initialization interface whenever possible.

Because the image file in the sample is not embedded in the .recipe file and is not a part of its file stream, [**IInitializeWithItem**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-iinitializewithitem) is used in the sample. The implementation of the [**IInitializeWithItem::Initialize**](/windows/win32/api/shobjidl_core/nf-shobjidl_core-iinitializewithitem-initialize) method simply passes its parameters to private class variables.

[**IThumbnailProvider**](/windows/desktop/api/Thumbcache/nn-thumbcache-ithumbnailprovider) has only one method—[**GetThumbnail**](/windows/desktop/api/Thumbcache/nf-thumbcache-ithumbnailprovider-getthumbnail)—that is called with the largest desired size of the image, in pixels. Although the parameter is named *cx*, its value is used as the maximum size of both the x and y dimensions of the image. If the retrieved thumbnail is not square, then the longer axis is limited by *cx* and the aspect ratio of the original image is preserved.

When it returns, [**GetThumbnail**](/windows/desktop/api/Thumbcache/nf-thumbcache-ithumbnailprovider-getthumbnail) provides a handle to the retrieved image. It also provides a value that indicates the color format of the image and whether it has valid alpha information.

The GetThumbnail implementation in the sample begins with a call to the private **\_GetBase64EncodedImageString** method.


```C++
IFACEMETHODIMP CRecipeThumbProvider::GetThumbnail(UINT cx, 
                                                  HBITMAP *phbmp, 
                                                  WTS_ALPHATYPE *pdwAlpha)
{
    PWSTR pszBase64EncodedImageString;
    HRESULT hr = _GetBase64EncodedImageString(cx, &pszBase64EncodedImageString);
```



The .recipe file type is simply an XML file registered as a unique file name extension. It includes an element called **Picture** that provides the relative path and file name of the image to use as the thumbnail for this particular .recipe file. The **Picture** element consists of the **Source** attribute that specifies a base 64 encoded image, and an optional **Size** attribute.

**Size** has two values, Small and Large. This allows you to provide multiple **Picture** nodes with separate images. The image retrieved then depends on the maximum size value (*cx*) provided in the call to [**GetThumbnail**](/windows/desktop/api/Thumbcache/nf-thumbcache-ithumbnailprovider-getthumbnail). Because Windows never sizes the image any larger than its maximum size, different images can be provided for different resolutions. However, for simplicity, the sample omits the **Size** attribute and provides only one image for all situations.

The **\_GetBase64EncodedImageString** method, whose implementation is shown here, uses XML Document Object Model (DOM) APIs to retrieve the **Picture** node. From that node it extracts the image from the **Source** attribute data.


```C++
HRESULT CRecipeThumbProvider::_GetBase64EncodedImageString(UINT /* cx */, 
                                                           PWSTR *ppszResult)
{
    *ppszResult = NULL;

    IXMLDOMDocument *pXMLDoc;
    HRESULT hr = _LoadXMLDocument(&pXMLDoc);
    if (SUCCEEDED(hr))
    {
        BSTR bstrQuery = SysAllocString(L"Recipe/Attachments/Picture");
        hr = bstrQuery ? S_OK : E_OUTOFMEMORY;
        if (SUCCEEDED(hr))
        {
            IXMLDOMNode *pXMLNode;
            hr = pXMLDoc->selectSingleNode(bstrQuery, &pXMLNode);
            if (SUCCEEDED(hr))
            {
                IXMLDOMElement *pXMLElement;
                hr = pXMLNode->QueryInterface(&pXMLElement);
                if (SUCCEEDED(hr))
                {
                    BSTR bstrAttribute = SysAllocString(L"Source");
                    hr = bstrAttribute ? S_OK : E_OUTOFMEMORY;
                    if (SUCCEEDED(hr))
                    {
                        VARIANT varValue;
                        hr = pXMLElement->getAttribute(bstrAttribute, &varValue);
                        if (SUCCEEDED(hr))
                        {
                            if ((varValue.vt == VT_BSTR) && varValue.bstrVal && varValue.bstrVal[0])
                            {
                                hr = SHStrDupW(varValue.bstrVal, ppszResult);
                            }
                            else
                            {
                                hr = E_FAIL;
                            }
                            VariantClear(&varValue);
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



[**GetThumbnail**](/windows/desktop/api/Thumbcache/nf-thumbcache-ithumbnailprovider-getthumbnail) then passes the retrieved string to **\_GetStreamFromString**.


```C++
IFACEMETHODIMP CRecipeThumbProvider::GetThumbnail(UINT cx, 
                                                  HBITMAP *phbmp, 
                                                  WTS_ALPHATYPE *pdwAlpha)
{
    PWSTR pszBase64EncodedImageString;
    HRESULT hr = _GetBase64EncodedImageString(cx, &pszBase64EncodedImageString);
    if (SUCCEEDED(hr))
    {
        IStream *pImageStream;
        hr = _GetStreamFromString(pszBase64EncodedImageString, &pImageStream);
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
                                         &dwDecodedImageSize, 
                                         &dwSkipChars, 
                                         &dwActualFormat);
    if (fSuccess)
    {
        BYTE *pbDecodedImage = (BYTE*)LocalAlloc(LPTR, dwDecodedImageSize);
        if (pbDecodedImage)
        {
            fSuccess = CryptStringToBinaryW(pszImageName, 
                                            lstrlenW(pszImageName), 
                                            CRYPT_STRING_BASE64,
                                            pbDecodedImage, 
                                            &dwDecodedImageSize, 
                                            &dwSkipChars, 
                                            &dwActualFormat);
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
    HRESULT hr = _GetBase64EncodedImageString(cx, &pszBase64EncodedImageString);
    if (SUCCEEDED(hr))
    {
        IStream *pImageStream;
        hr = _GetStreamFromString(pszBase64EncodedImageString, &pImageStream);
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

[**IID\_PPV\_ARGS**](/windows/win32/api/combaseapi/nf-combaseapi-iid_ppv_args)
</dt> </dl>

 

 
