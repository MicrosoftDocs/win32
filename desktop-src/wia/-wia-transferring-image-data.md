---
description: Use the methods of the IWiaDataTransfer interface to transfer data from a Windows Image Acquisition (WIA) 1.0 device to an application.
ms.assetid: 67fbf3d9-6965-4464-b04c-10989b2fd55d
title: Transferring Image Data in WIA 1.0
ms.topic: article
ms.date: 05/31/2018
---

# Transferring Image Data in WIA 1.0

> [!Note]  
> This tutorial is about transferring image data in applications that will run Windows XP or earlier. See [Transferring Image Data in WIA 2.0](-wia-transferring-image-data-in-wia2.md) for information about transferring image data in applications that will run on Windows Vista or later.

 

Use the methods of the [**IWiaDataTransfer**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiadatatransfer) interface to transfer data from a Windows Image Acquisition (WIA) 1.0 device to an application. This interface supports a shared memory window to transfer data from the device object to the application and eliminate unnecessary data copies during marshalling.

Applications must query an image item to obtain a pointer to its [**IWiaDataTransfer**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiadatatransfer) interface, as in the following code sample:


```
    // Get the IWiaDataTransfer interface
    //
    IWiaDataTransfer *pWiaDataTransfer = NULL;
    hr = pWiaItem->QueryInterface( IID_IWiaDataTransfer, (void**)&pWiaDataTransfer );
```



In the previous code, it is assumed that **pWiaItem** is a valid pointer to the [**IWiaItem**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiaitem) interface. The call to [IUnknown::QueryInterface](/windows/win32/api/unknwn/nf-unknwn-iunknown-queryinterface(q)) fills **pWiaDataTransfer** with a pointer to the [**IWiaDataTransfer**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiadatatransfer) interface of the item referred to by **pWiaItem**.

The application then sets the [STGMEDIUM](/windows/win32/api/objidl/ns-objidl-ustgmedium-r1) structure members. For information, see STGMEDIUM and [TYMED](/windows/win32/api/objidl/ne-objidl-tymed).


```
    // Set storage medium
    //
    STGMEDIUM StgMedium = {0};
    StgMedium.tymed = TYMED_FILE;
```



If you supply a filename, it should include the proper file extension; WIA 1.0 does not provide file extensions. If the **lpszFileName** member of **StgMedium** is **NULL**, WIA 1.0 generates a random file name and path for the transferred data. Move or copy this file before calling ReleaseStgMedium, because this function will delete the file.

The application then calls the [**IWiaDataTransfer::idtGetData**](/windows/desktop/api/wia_xp/nf-wia_xp-iwiadatatransfer-idtgetdata) method to run the data transfer:


```
    // Perform the transfer
    //
    hr = pWiaDataTransfer->idtGetData( &stgMedium, pWiaDataCallback );
```



In the call to [**IWiaDataTransfer::idtGetData**](/windows/desktop/api/wia_xp/nf-wia_xp-iwiadatatransfer-idtgetdata), the second parameter specifies a pointer to the [**IWiaDataCallback**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiadatacallback) interface. Applications must implement this interface to receive callbacks during data transfers. For information about implementing this interface, see [**IWiaDataCallback::BandedDataCallback**](/windows/desktop/api/wia_xp/nf-wia_xp-iwiadatacallback-bandeddatacallback).

The application then releases the pointers to the [**IWiaDataTransfer**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiadatatransfer) interface and frees any data allocated in the [STGMEDIUM](/windows/win32/api/objidl/ns-objidl-ustgmedium-r1) structure.

The application can also transfer the image using in-memory data transfers instead of file transfers. In this case, the application uses the idtGetBandedData method in place of the idtGetData method.

Here is the complete data transfer sample:


```
HRESULT TransferWiaItem( IWiaItem *pWiaItem )
{
    //
    // Validate arguments
    //
    if (NULL == pWiaItem)
    {
        return E_INVALIDARG;
    }

    //
    // Get the IWiaPropertyStorage interface so you can set required properties.
    //
    IWiaPropertyStorage *pWiaPropertyStorage = NULL;
    HRESULT hr = pWiaItem->QueryInterface( IID_IWiaPropertyStorage, (void**)&pWiaPropertyStorage );
    if (SUCCEEDED(hr))
    {
        //
        // Prepare PROPSPECs and PROPVARIANTs for setting the
        // media type and format
        //
        PROPSPEC PropSpec[2] = {0};
        PROPVARIANT PropVariant[2] = {0};
        const ULONG c_nPropCount = sizeof(PropVariant)/sizeof(PropVariant[0]);

        //
        // Use BMP as the output format
        //
        GUID guidOutputFormat = WiaImgFmt_BMP;

        //
        // Initialize the PROPSPECs
        //
        PropSpec[0].ulKind = PRSPEC_PROPID;
        PropSpec[0].propid = WIA_IPA_FORMAT;
        PropSpec[1].ulKind = PRSPEC_PROPID;
        PropSpec[1].propid = WIA_IPA_TYMED;

        //
        // Initialize the PROPVARIANTs
        //
        PropVariant[0].vt = VT_CLSID;
        PropVariant[0].puuid = &guidOutputFormat;
        PropVariant[1].vt = VT_I4;
        PropVariant[1].lVal = TYMED_FILE;

        //
        // Set the properties
        //
        hr = pWiaPropertyStorage->WriteMultiple( c_nPropCount, PropSpec, PropVariant, WIA_IPA_FIRST );
        if (SUCCEEDED(hr))
        {
            //
            // Get the IWiaDataTransfer interface
            //
            IWiaDataTransfer *pWiaDataTransfer = NULL;
            hr = pWiaItem->QueryInterface( IID_IWiaDataTransfer, (void**)&pWiaDataTransfer );
            if (SUCCEEDED(hr))
            {
                //
                // Create our callback class
                //
                CWiaDataCallback *pCallback = new CWiaDataCallback;
                if (pCallback)
                {
                    //
                    // Get the IWiaDataCallback interface from our callback class.
                    //
                    IWiaDataCallback *pWiaDataCallback = NULL;
                    hr = pCallback->QueryInterface( IID_IWiaDataCallback, (void**)&pWiaDataCallback );
                    if (SUCCEEDED(hr))
                    {
                        //
                        // Perform the transfer using default settings
                        //
                        STGMEDIUM stgMedium = {0};
                        StgMedium.tymed = TYMED_FILE;
                        hr = pWiaDataTransfer->idtGetData( &stgMedium, pWiaDataCallback );
                        if (S_OK == hr)
                        {
                            //
                            // Print the filename (note that this filename is always
                            // a WCHAR string, not TCHAR).
                            //
                            _tprintf( TEXT("Transferred filename: %ws\n"), stgMedium.lpszFileName );

                            //
                            // Release any memory associated with the stgmedium
                            // This will delete the file stgMedium.lpszFileName.
                            //
                            ReleaseStgMedium( &stgMedium );
                        }

                        //
                        // Release the callback interface
                        //
                        pWiaDataCallback->Release();
                        pWiaDataCallback = NULL;
                    }

                    //
                    // Release our callback.  It should now delete itself.
                    //
                    pCallback->Release();
                    pCallback = NULL;
                }

                //
                // Release the IWiaDataTransfer
                //
                pWiaDataTransfer->Release();
                pWiaDataTransfer = NULL;
            }
        }

        //
        // Release the IWiaPropertyStorage
        //
        pWiaPropertyStorage->Release();
        pWiaPropertyStorage = NULL;
    }

    return hr;
}
```



 

 
