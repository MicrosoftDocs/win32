---
description: Implementing IWICBitmapCodecProgressNotification (Decoder)
ms.assetid: 686b0875-c7ec-45ee-bd3e-94bfd9e5dcda
title: Implementing IWICBitmapCodecProgressNotification (Decoder)
ms.topic: article
ms.date: 05/31/2018
---

# Implementing IWICBitmapCodecProgressNotification (Decoder)

## IWICBitmapCodecProgressNotification

When a codec is performing an I/O operation such as [**CopyPixels**](/windows/desktop/api/Wincodec/nf-wincodec-iwicbitmapsource-copypixels) on a large image, it may take several seconds or even minutes to complete. When end users are unable to interrupt a long-running operation, they may think the application has hung. Users will often close an application, or even restart their computers, in an attempt to regain control of their computer when an application becomes unresponsive.

This interface enables an application to specify a callback function that the codec can call at specified intervals to notify the caller of the progress of the current operation. The application can use this callback function to display an indication of progress in the user interface to notify the user of the status of the operation. If a user clicks the **Cancel** button on the **Progress** dialog box, the application returns **WINCODEC\_ERR\_ABORTED** from the callback function. When this happens, the codec must cancel the specified operation and propagate this **HRESULT** back to the caller of the method that was performing the operation.

This interface should be implemented on your container-level decoder class.


```C++
interface IWICBitmapCodecProgressNotification : public IUnknown
{
    HRESULT RegisterProgressNotification ( 
        PFNProgressNotification pfnProgressNotification,
        LPVOID pvData,
        DWORD dwProgressFlags );
}
```



-   [RegisterProgressNotification](#registerprogressnotification)
-   [PFNProgressNotification](#pfnprogressnotification)

### RegisterProgressNotification

[**RegisterProgressNotification**](/windows/desktop/api/Wincodec/nf-wincodec-iwicbitmapcodecprogressnotification-registerprogressnotification) is invoked by an application to register a callback function that the codec can call at specified intervals. The first parameter, *pfnProgressNotification*, is a pointer to the callback function that the codec should call at regular intervals.

The *pvData* parameter points to some object that the caller wants the codec to pass back to the callback function whenever the callback function is invoked. This object may be anything at all and has no particular significance to the codec.

The *dwProgressFlags* parameter specifies when the codec should call the callback function. An OR function can be performed with two enumerations for this parameter. The [**WICProgressOperation**](/windows/desktop/api/Wincodec/ne-wincodec-wicprogressoperation) enum specifies whether to call the callback function during decoding (**WICProgressOperationCopyPixels**), encoding (**WICProgerssOperationWritePixels**), or both (**WICProgressOperationAll**).


```C++
enum WICProgressOperation
{
   WICProgressOperationCopyPixels,
   WICProgerssOperationWritePixels,
   WICProgressOperationAll      
};
```



The codec should call the callback function at regular intervals throughout the operation, but the caller may specify certain requirements. The [**WICProgressNotification**](/windows/desktop/api/Wincodec/ne-wincodec-wicprogressnotification) enum indicates at which point in the operation to call the callback function. If the caller specifies **WICProgressNotificationBegin**, you must call it at the beginning of the operation (0.0). If the caller does not specify this, it is optional. Likewise, if the caller specifies **WICProgerssNotificationEnd**, you must call it when the operation is completed (1.0). If the caller specifies **WICProgressNotificationAll**, you must call it at the beginning and end, as well as at regular intervals throughout the operation. The caller may also specify **WICProgerssNotificationFrequent**, which indicates that they want to be called back at frequent intervals, perhaps after every couple of scan lines. (A caller will usually use this flag only for a very large image.) Otherwise, you should usually call back at intervals of approximately 10 percent increments of the total number of scan lines to be processed.


```C++
enum WICProgressNotification
{
   WICProgressNotificationBegin,
   WICProgerssNotificationEnd,
   WICProgerssNotificationFrequent,
   WICProgressNotificationAll
};
```



Only one callback function at a time can be registered for a specific decoder or encoder instance. If an application calls [**RegisterProgressNotification**](/windows/desktop/api/Wincodec/nf-wincodec-iwicbitmapcodecprogressnotification-registerprogressnotification) more than once, replace the previously registered callback function with the new one. To cancel a callback registration, a caller will set the *pfnProgressNotification* parameter to **NULL**.

### PFNProgressNotification

[**PFNProgressNotification**](/windows/desktop/api/Wincodec/nc-wincodec-pfnprogressnotification) is the callback function with the following signature.


```C++
typedef HRESULT (*PFNProgressNotification) ( 
   LPVOID pvData,
   ULONG uFrameNum,
   WICProgressOperation operation,
   double dblProgress );
```



When you invoke the callback function, use the *pvData* parameter to pass back the same *pvData* that the application specified when it registered the callback function.

The *uFrameNum* parameter should indicate the index of the frame that is being processed.

Set the operation parameter to **WICProgressOperationCopyPixels** when decoding and **WICProgressOperationWritePixels** when encoding.

The *dblProgress* parameter should be a number between 0.0 (the beginning of the operation) and 1.0 (the completion of the operation). The value should reflect the proportion of scan lines already processed relative to the total number of scan lines to be processed.

## Related topics

<dl> <dt>

**Reference**
</dt> <dt>

[**ProgressNotificationCallback**](/windows/desktop/api/Wincodec/nc-wincodec-pfnprogressnotification)
</dt> <dt>

[**IWICBitmapCodecProgressNotification**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapcodecprogressnotification)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Implementing IWICBitmapDecoder](-wic-imp-iwicbitmapdecoder.md)
</dt> <dt>

[Implementing IWICBitmapSource](-wic-imp-iwicbitmapsource.md)
</dt> <dt>

[How to Write a WIC-Enabled CODEC](-wic-howtowriteacodec.md)
</dt> <dt>

[Windows Imaging Component Overview](-wic-about-windows-imaging-codec.md)
</dt> </dl>

 

 



