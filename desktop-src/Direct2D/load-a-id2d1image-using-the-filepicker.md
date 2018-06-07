---
title: How to load an image into Direct2D effects using the FilePicker
description: Shows how to use the Windows Storage Pickers FileOpenPicker to load an image into Direct2D effects.
ms.assetid: 42158EF0-2FC8-45F3-8C92-E12318D4724F
keywords:
- FileOpenPicker
- FilePicker
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# How to load an image into Direct2D effects using the FilePicker

Shows how to use the [**Windows::Storage::Pickers::FileOpenPicker**](https://msdn.microsoft.com/library/windows/apps/br207847) to load an image into [Direct2D effects](effects-overview.md). If you want to let the user select an image file from storage in a Windows Store app, we recommend that you use the [**FileOpenPicker**](https://msdn.microsoft.com/library/windows/apps/br207847).

## What you need to know

### Technologies

-   [Direct2D](https://msdn.microsoft.com/03b3b91c-9751-4f8d-af24-85067f06930b)
-   [Direct2D effects](effects-overview.md)
-   [**Windows::Storage::Pickers::FileOpenPicker**](https://msdn.microsoft.com/library/windows/apps/br207847)

### Prerequisites

-   You need an [**ID2D1DeviceContext**](/windows/desktop/api/D2d1_1/) object for creating effects.
-   You need an [**IWICImagingFactory**](https://msdn.microsoft.com/library/windows/desktop/ee690281) object for creating WIC objects.

## Instructions

### Step 1: Open the file picker

Create a [**FileOpenPicker**](https://msdn.microsoft.com/library/windows/apps/br207847) object and set the *ViewMode*, *SuggestedStartLocation*, and the *FileTypeFilter* for selecting images. Call the [**PickSingleFileAsync**](https://msdn.microsoft.com/library/windows/apps/jj635275) method.


```C++
    FileOpenPicker^ openPicker = ref new FileOpenPicker();
    openPicker->ViewMode = PickerViewMode::Thumbnail;
    openPicker->SuggestedStartLocation = PickerLocationId::PicturesLibrary;
    openPicker->FileTypeFilter->Append(".jpg");
    auto pickOperation = openPicker->PickSingleFileAsync();
```



After the [**PickSingleFileAsync**](https://msdn.microsoft.com/library/windows/apps/jj635275) completes, you get a file stream from the [**IAsyncOperation**](https://msdn.microsoft.com/library/windows/desktop/bb776309) interface it returns.

### Step 2: Get a file stream

Declare a completion handler to run after the file picker async operation returns. Use the [**GetResults**](https://msdn.microsoft.com/library/windows/desktop/br205815) method to retrieve the file and to get the file stream object.


```C++
    pickOperation->Completed = ref new AsyncOperationCompletedHandler<StorageFile^>(
          [=](IAsyncOperation<StorageFile^> ^operation, AsyncStatus status)
    {
        auto file = operation->GetResults();
        if (file) // If file == nullptr, the user did not select a file.
        {
                             auto openOperation = file->OpenAsync(FileAccessMode::Read);
                             openOperation->Completed = ref new
                                      AsyncOperationCompletedHandler<IRandomAccessStream^>(
                                      [=](IAsyncOperation<IRandomAccessStream^> ^operation, AsyncStatus status)
                             {
                                      auto fileStream = operation->GetResults();

                                      // Pass IRandomAccessStream^ into DirectXApp for decoding/processing.
                                      OpenFile(fileStream);
                             });
        }
    });
```



In the next step you convert the [**IRandomAccessStream**](https://msdn.microsoft.com/library/windows/desktop/hh438400) object to an [**IStream**](https://msdn.microsoft.com/library/windows/desktop/aa380034) that you can pass to [WIC](https://msdn.microsoft.com/library/windows/desktop/ee719655).

### Step 3: Convert the file stream

Use the [**CreateStreamOverRandomAccessStream**](https://msdn.microsoft.com/library/windows/desktop/hh846258) function to convert the file stream. Windows Runtime APIs represent streams with [**IRandomAccessStream**](https://msdn.microsoft.com/library/windows/desktop/hh438400), while [WIC](https://msdn.microsoft.com/library/windows/desktop/ee719655) consumes [**IStream**](https://msdn.microsoft.com/library/windows/desktop/aa380034).


```C++
    ComPtr<IStream> istream;
    DX::ThrowIfFailed(
        CreateStreamOverRandomAccessStream(
        reinterpret_cast<IUnknown*>(fileStream),
        IID_PPV_ARGS(&amp;istream)
        )
    );
```



> [!Note]  
> To use the [**CreateStreamOverRandomAccessStream**](https://msdn.microsoft.com/library/windows/desktop/hh846258) function, you should include *shcore.h* in your project.

 

### Step 4: Create a WIC decoder and get the frame

Create an [**IWICBitmapDecoder**](https://msdn.microsoft.com/library/windows/desktop/ee690086) object using the [**IWICImagingFactory::CreateDecoderFromStream**](https://msdn.microsoft.com/library/windows/desktop/ee690309) method.


```C++
    ComPtr<IWICBitmapDecoder> decoder;
    DX::ThrowIfFailed(
          m_wicFactory->CreateDecoderFromStream(
                    istream.Get(),
                    nullptr,
                    WICDecodeMetadataCacheOnDemand,
                    &amp;decoder
                    )
          );
```



Get the first frame of the image from the decoder using the [**IWICBitmapDecoder::GetFrame**](https://msdn.microsoft.com/library/windows/desktop/ee690099) method.


```C++
    ComPtr<IWICBitmapFrameDecode> frame;
    DX::ThrowIfFailed(
        decoder->GetFrame(0, &amp;frame)
        );
```



### Step 5: Create a WIC converter and initialize

Convert the image to the BGRA color format using [WIC](https://msdn.microsoft.com/library/windows/desktop/ee719655). [IWICBitmapFrameDecode](https://msdn.microsoft.com/library/windows/desktop/ee719894) will return the native pixel format of the image, like JPEGs are stored in GUID\_WICPixelFormat24bppBGR. However, as a performance optimization with Direct2D we recommend that you convert to WICPixelFormat32bppPBGRA.

1.  Create a [**IWICFormatConverter**](https://msdn.microsoft.com/library/windows/desktop/ee690274) object using the [**IWICImagingFactory::CreateFormatConverter**](https://msdn.microsoft.com/library/windows/desktop/ee690317) method.

    ```C++
        ComPtr<IWICFormatConverter> converter;
        DX::ThrowIfFailed(
            m_wicFactory->CreateFormatConverter(&amp;converter)
            ); 
     
    ```

    

2.  Initialize the format converter to use the WICPixelFormat32bppPBGRA and pass in the bitmap frame.

    ```C++
       DX::ThrowIfFailed(
            converter->Initialize(
                frame.Get(),
                GUID_WICPixelFormat32bppPBGRA,
                WICBitmapDitherTypeNone,
                nullptr,
                0.0f,
                WICBitmapPaletteTypeCustom  // premultiplied BGRA has no paletting, so this is ignored
                )
            );
    ```

    

The [**IWICFormatConverter**](https://msdn.microsoft.com/library/windows/desktop/ee690274) interface is derived from the [**IWICBitmapSource**](https://msdn.microsoft.com/library/windows/desktop/ee690171) interface, so you can pass the converter to the [bitmap source](bitmap-source.md) effect.

### Step 6: Create effect and pass in an IWICBitmapSource

Use the [**CreateEffect**](/windows/desktop/api/D2d1_1/) method to create a [bitmap source](bitmap-source.md) [**ID2D1Effect**](/windows/desktop/api/D2d1_1/) object using the [Direct2D](getting-started-with-direct2d.md) [**device context**](/windows/desktop/api/D2d1_1/).

Use the [**ID2D1Effect::SetValue**](/windows/desktop/api/D2d1_1/) method to set the *D2D1\_BITMAPSOURCE\_PROP\_WIC\_BITMAP\_SOURCE* property to the [WIC](https://msdn.microsoft.com/library/windows/desktop/ee719655) [**format converter**](https://msdn.microsoft.com/library/windows/desktop/ee690274).

> [!Note]  
> The [bitmap source](bitmap-source.md) effect doesn't take an input from the [**SetInput**](/windows/desktop/api/D2d1_1/) method like many [Direct2D effects](effects-overview.md). Instead, the [**IWICBitmapSource**](https://msdn.microsoft.com/library/windows/desktop/ee690171) object is specified as a property.

 


```C++
    ComPtr<ID2D1Effect> bitmapSourceEffect;

    DX::ThrowIfFailed(
        m_d2dContext->CreateEffect(CLSID_D2D1BitmapSource, &amp;bitmapSourceEffect)
        );

    DX::ThrowIfFailed(
        bitmapSourceEffect->SetValue(D2D1_BITMAPSOURCE_PROP_WIC_BITMAP_SOURCE, converter.Get())
        );

    // Insert code using the bitmap source in an effect graph.
```



Now that you have the [bitmap source](bitmap-source.md) effect, you can use it as input to any [**ID2D1Effect**](/windows/desktop/api/D2d1_1/) and create an effect graph.

## Complete example

Here is the full code for this example.


```C++
ComPtr<ID2D1Effect> bitmapSourceEffect;

void OpenFilePicker()
{
    FileOpenPicker^ openPicker = ref new FileOpenPicker();
    openPicker->ViewMode = PickerViewMode::Thumbnail;
    openPicker->SuggestedStartLocation = PickerLocationId::PicturesLibrary;
    openPicker->FileTypeFilter->Append(".jpg");
    auto pickOperation = openPicker->PickSingleFileAsync();
    
    pickOperation->Completed = ref new AsyncOperationCompletedHandler<StorageFile^>(
          [=](IAsyncOperation<StorageFile^> ^operation, AsyncStatus status)
    {
        auto file = operation->GetResults();
        if (file)
        {
                             auto openOperation = file->OpenAsync(FileAccessMode::Read);
                             openOperation->Completed = ref new
                                      AsyncOperationCompletedHandler<IRandomAccessStream^>(
                                      [=](IAsyncOperation<IRandomAccessStream^> ^operation, AsyncStatus status)
                             {
                                      auto fileStream = operation->GetResults();

                                      // Pass IRandomAccessStream^ into DirectXApp for decoding/processing.
                                      OpenFile(fileStream);
                             });
        }
    });
}

void OpenFile(Windows::Storage::Streams::IRandomAccessStream^ fileStream)
{
    ComPtr<IStream> istream;
    DX::ThrowIfFailed(
        CreateStreamOverRandomAccessStream(
            reinterpret_cast<IUnknown*>(fileStream),
            IID_PPV_ARGS(&amp;istream)
            )
        );

    ComPtr<IWICBitmapDecoder> decoder;
    DX::ThrowIfFailed(
          m_wicFactory->CreateDecoderFromStream(
                    istream.Get(),
                    nullptr,
                    WICDecodeMetadataCacheOnDemand,
                    &amp;decoder
                    )
          );

    ComPtr<IWICBitmapFrameDecode> frame;
    DX::ThrowIfFailed(
        decoder->GetFrame(0, &amp;frame)
        );

    ComPtr<IWICFormatConverter> converter;
    DX::ThrowIfFailed(
        m_wicFactory->CreateFormatConverter(&amp;converter)
        );

    DX::ThrowIfFailed(
        converter->Initialize(
            frame.Get(),
            GUID_WICPixelFormat32bppPBGRA,
            WICBitmapDitherTypeNone,
            nullptr,
            0.0f,
            WICBitmapPaletteTypeCustom  // premultiplied BGRA has no paletting, so this is ignored
            )
        );

       ComPtr<ID2D1Effect> bitmapSourceEffect;

    DX::ThrowIfFailed(
        m_d2dContext->CreateEffect(CLSID_D2D1BitmapSource, &amp;bitmapSourceEffect)
        );

    DX::ThrowIfFailed(
        bitmapSourceEffect->SetValue(D2D1_BITMAPSOURCE_PROP_WIC_BITMAP_SOURCE, converter.Get())
        );

    // Insert code using the bitmap source in an effect graph.
}
```



 

 




