---
description: Caches internally the unfiltered image returned from the driver.
ms.assetid: 09cb242d-d1d6-4130-8b49-0770940471d8
title: IWiaPreview::GetNewPreview method (Wia.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWiaPreview.GetNewPreview
api_type: 
- COM
api_location: 
- Wia.h
---

# IWiaPreview::GetNewPreview method

Caches internally the unfiltered image returned from the driver.

## Syntax


```C++
HRESULT GetNewPreview(
  [in] IWiaItem2            *pWiaItem2,
  [in] LONG                 lFlags,
  [in] IWiaTransferCallback *pWiaTransferCallback
);
```



## Parameters

<dl> <dt>

*pWiaItem2* \[in\]
</dt> <dd>

Type: **[**IWiaItem2**](-wia-iwiaitem2.md)\***

Specifies a pointer to the [**IWiaItem2**](-wia-iwiaitem2.md) item for the image.

</dd> <dt>

*lFlags* \[in\]
</dt> <dd>

Type: **LONG**

Currently unused. Should be set to zero.

</dd> <dt>

*pWiaTransferCallback* \[in\]
</dt> <dd>

Type: **[**IWiaTransferCallback**](-wia-iwiatransfercallback.md)\***

Specifies a pointer to the calling application's [**IWiaTransferCallback**](-wia-iwiatransfercallback.md) interface.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

An application must call **IWiaPreview::GetNewPreview** before it calls [**IWiaPreview::DetectRegions**](-wia-iwiapreview-detectregions.md).

**IWiaPreview::GetNewPreview** sets the [**WIA\_DPS\_PREVIEW**](-wia-wiaitempropscannerdevice.md) property (and resets it before it returns, unless it was set before). This lets the driver and hardware, as well as the image processing filter, know that the item is a preview scan.

Internally, the Windows Image Acquisition (WIA) 2.0 preview component creates an instance of the driver's image processing filter by calling [**GetExtension**](-wia-iwiaitem2-getextension.md) on *pWiaItem2*. The WIA 2.0 preview component does this when the application calls **IWiaPreview::GetNewPreview**. The WIA 2.0 preview component also initializes the filter in **IWiaPreview::GetNewPreview**. The same filter instance is used by the WIA 2.0 preview component during a call to [**IWiaPreview::UpdatePreview**](-wia-iwiapreview-updatepreview.md).

Before calling into the WIA 2.0 preview component, an application should call [**CheckExtension**](-wia-iwiaitem2-checkextension.md) to make sure that the driver comes with an image processing filter. It should call **CheckExtension** on the item that it would pass to **IWiaPreview::GetNewPreview**. It is useless to provide live previews without an image processing filter. If an application calls **IWiaPreview::GetNewPreview** for a driver without an image processing filter, the call will fail.

## Examples

CheckImgFilter checks if the driver has an image processing filter. Before calling into the preview component, an application should ensure that the driver has an image processing filter.


```C++
HRESULT
CheckImgFilter(
   IN  IWiaItem2 *pWiaItem2,
   OUT BOOL      *pbHasImgFilter)
{
   HRESULT     hr = S_OK;

   if (!pWiaItem2 || !pbHasImgFilter)
   {
      hr = E_INVALIDARG;
   }

   if (SUCCEEDED(hr))
   {
     *pbHasImgFilter = FALSE;
   }

   if (SUCCEEDED(hr))
   {
      BSTR    bstrFilterString = SysAllocString(WIA_IMAGEPROC_FILTER_STR);

      if (bstrFilterString)
      {
         hr = pWiaItem2->CheckExtension(0,
                                        bstrFilterString,
                                        IID_IWiaSegmentationFilter,
                                        pbHasImgFilter);

         SysFreeString(bstrFilterString);
         bstrFilterString = NULL;
      }
      else
      {
         hr = E_OUTOFMEMORY;
      }
   }

   return hr;

}
```



DownloadPreviewImage downloads image data from the scanner by calling the preview component's **IWiaPreview::GetNewPreview** method. It then calls DetectSubregions if the application user wants to invoke the segmentation filter, which creates a child item under pWiaItem2 for each region it detects. See [**DetectRegions**](-wia-iwiasegmentationfilter-detectregions.md) for the DetectSubregions method used in this example.

In this example, the application user sets `m_bUseSegmentationFilter` by clicking a check box. If the application supports this, it should first check that the driver has a segmentation filter by calling [**CheckExtension**](-wia-iwiaitem2-checkextension.md). See **IWiaPreview::GetNewPreview** for the CheckImgFilter method example that shows how this can be done.


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
         // The constructor of AppWiaTransferCallback sets the reference count to 1.
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
         // Do not create an instance of preview component if the driver does
         // not come with an image processing filter.
         // You can use segmentation filter, however, if the driver
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



 

 




