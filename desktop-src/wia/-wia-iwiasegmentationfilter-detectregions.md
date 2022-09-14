---
description: Determines the sub-regions of an image laid out on the flatbed platen so that each of sub-region can be acquired into a separate image item.
ms.assetid: 899d61f0-2dd8-4a68-827e-89e85ebb5143
title: IWiaSegmentationFilter::DetectRegions method (Wia.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWiaSegmentationFilter.DetectRegions
api_type: 
- COM
api_location: 
- Wia.h
---

# IWiaSegmentationFilter::DetectRegions method

Determines the sub-regions of an image laid out on the flatbed platen so that each of sub-region can be acquired into a separate image item.

## Syntax


```C++
HRESULT DetectRegions(
  [in] LONG      lFlags,
  [in] IStream   *pInputStream,
  [in] IWiaItem2 *pWiaItem2
);
```



## Parameters

<dl> <dt>

*lFlags* \[in\]
</dt> <dd>

Type: **LONG**

Currently unused. Should be set to zero.

</dd> <dt>

*pInputStream* \[in\]
</dt> <dd>

Type: **[IStream](/windows/win32/api/objidl/nn-objidl-istream)\***

Specifies a pointer to the [IStream](/windows/win32/api/objidl/nn-objidl-istream) preview image.

</dd> <dt>

*pWiaItem2* \[in\]
</dt> <dd>

Type: **[**IWiaItem2**](-wia-iwiaitem2.md)\***

Specifies a pointer to the [**IWiaItem2**](-wia-iwiaitem2.md) item for which *pInputStream* was acquired. The segmentation filter creates child items for this item.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

This method determines the sub-regions of the image represented by pInputStream. For each sub-region that it detects, it creates a child item for the [**IWiaItem2**](-wia-iwiaitem2.md) item specified in the *pWiaItem2* parameter. For each child item, the segmentation filter must set values for the bounding rectangle of the area to scan, using the following [**Scanner WIA Item Property Constants**](-wia-wiaitempropscanneritem.md).

-   [**WIA\_IPS\_XPOS**](-wia-wiaitempropscanneritem.md)
-   [**WIA\_IPS\_YPOS**](-wia-wiaitempropscanneritem.md)
-   [**WIA\_IPS\_XEXTENT**](-wia-wiaitempropscanneritem.md)
-   [**WIA\_IPS\_YEXTENT**](-wia-wiaitempropscanneritem.md)

A more advanced filter may also require other [**Scanner WIA Item Property Constants**](-wia-wiaitempropscanneritem.md) such as **WIA\_IPS\_DESKEW\_X** and **WIA\_IPS\_DESKEW\_Y**, if the driver supports de-skewing.

If the application calls **IWiaSegmentationFilter::DetectRegions** more than once, the application must first delete the child items created by the last call to **IWiaSegmentationFilter::DetectRegions**.

If an application changes any properties into *pWiaItem2*, between acquiring the image into *pInputStream* and its call to **IWiaSegmentationFilter::DetectRegions**, the original properties (that is, the properties the item had when the stream was acquired) must be restored. This can be done by [**GetPropertyStream**](/windows/desktop/api/wia_xp/nf-wia_xp-iwiapropertystorage-getpropertystream) and [**SetPropertyStream**](/windows/desktop/api/wia_xp/nf-wia_xp-iwiapropertystorage-setpropertystream).

The application must reset the [IStream](/windows/win32/api/objidl/nn-objidl-istream) if its call passes the same stream into the segmentation filter more than once. The application must also reset the stream after the initial download and before calling **IWiaSegmentationFilter::DetectRegions**.

## Examples

The segmentation performs region detection on the stream (`pImageStream`) passed into DetectSubregions. See the [**GetExtension**](-wia-iwiaitem2-getextension.md) for CreateSegmentationFilter method used in this example.


```C++
HRESULT
DetectSubregions(
   IN IStream   *pImageStream,
   IN IWiaItem2 *pWiaItem2)
{
   HRESULT                 hr                  = S_OK;
   IWiaSegmentationFilter* pSegmentationFilter = NULL;

   if (!pWiaItem2 || !pImageStream)
   {
      hr = E_INVALIDARG;
   }

   if (SUCCEEDED(hr))
   {
      hr = CreateSegmentationFilter(pWiaItem2, &pSegmentationFilter);
   }

   if (SUCCEEDED(hr))
   {
      hr = pSegmentationFilter->DetectRegions(0,pImageStream, pWiaItem2); 
   }

   if (pSegmentationFilter)
   {
      pSegmentationFilter->Release();
      pSegmentationFilter = NULL;
   }

   return hr;
}
```



DownloadPreviewImage downloads image data from the scanner by calling the preview component's [**GetNewPreview**](-wia-iwiapreview-getnewpreview.md) method. It then calls DetectSubregions if the application user wants to invoke the segmentation filter, which creates a child item under pWiaItem2 for each region it detects. See **IWiaSegmentationFilter::DetectRegions** for the DetectSubregions method used in this example.

In this example, the application user sets `m_bUseSegmentationFilter` by clicking a check box. If the application supports this, it should first check that the driver has a segmentation filter by calling [**CheckExtension**](-wia-iwiaitem2-checkextension.md). See [**GetNewPreview**](-wia-iwiapreview-getnewpreview.md) for the CheckImgFilter method example that shows how this can be done.


```C++
HRESULT
DownloadPreviewImage(
   IN IWiaItem2 *pWiaFlatbedItem2)
{
   HRESULT hr              = S_OK;
   BOOL    bHasImgFilter   = FALSE;

   IWiaTransferCallback *pAppWiaTransferCallback = NULL;

   hr = CheckImgFilter(pWiaFlatbedItem2, &bHasImgFilter)

   if (SUCCEEDED(hr))
   {
      if (bHasImgFilter)
      {
         IWiaPreview *pWiaPreview = NULL;

         // In this example, the AppWiaTransferCallback class implements 
         // the IWiaTransferCallback interface.  
         // The constructor of AppWiaTransferCallback sets the reference count 
         // to 1.
         pAppWiaTransferCallback = new AppWiaTransferCallback();

         hr = pAppWiaTransferCallback ? S_OK : E_OUTOFMEMORY;

         if (SUCCEEDED(hr))
         {
            // Acquire image from scanner
            hr = m_pWiaPreview->GetNewPreview(pWiaFlatbedItem2,
                                              0,
                                              pAppWiaTransferCallback);    
         }

         //
         // Check the application UI for whether the user wants
         // to use the segmentation filter indicated by the value 
         // of m_bUseSegmentationFilter.
         //
         // m_FlatbedPreviewStream is the stream that
         // AppWiaTransferCallback::GetNextStream returned for the
         // flatbed item.
         // This stream is where the image data is stored after
         // the successful return of GetNewPreview.
         // The stream is passed into the segmentation filter
         // for region detection.
         if (SUCCEEDED(hr) && m_bUseSegmentationFilter)
         {
            DetectSubregions(m_FlatbedPreviewStream, pWiaFlatbedItem2);
         }

         if (pAppWiaTransferCallback)
         {
            // If the call to GetNewPreview was successful, the
            // preview component calls AddRef on the callback so
            // this call doesn't delete the object.

            pAppWiaTransferCallback->Release();
         }

      }
      else
      {
         // Do not create an instance of preview component if the driver 
         // does not come with an image-processing filter.
         // You can use a segmentation filter, however, if the driver
         // comes with one (omitted here).
      }
   }

   return hr;
}
```



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wia.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wia.idl</dt> </dl> |



 

 
