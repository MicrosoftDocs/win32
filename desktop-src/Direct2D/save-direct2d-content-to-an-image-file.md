---
title: How to save Direct2D content to an image file
description: This topic shows how to use IWICImageEncoder to save content in the form of an ID2D1Image to an encoded image file such as JPEG.
ms.assetid: F0D8BFC7-723A-4577-B2DF-4D656A18E2FC
ms.topic: article
ms.date: 05/31/2018
---

# How to save Direct2D content to an image file

This topic shows how to use [**IWICImageEncoder**](/windows/desktop/api/wincodec/nn-wincodec-iwicimageencoder) to save content in the form of an [**ID2D1Image**](/windows/win32/api/d2d1/nn-d2d1-id2d1image) to an encoded image file such as JPEG. If you are writing a Windows Store app, you can have the user select a destination file using [**Windows::Storage::Pickers::FileSavePicker**](/uwp/api/Windows.Storage.Pickers.FileSavePicker).

## What you need to know

### Technologies

-   [Direct2D](./direct2d-portal.md)
-   [Direct2D effects](effects-overview.md)
-   [**Windows::Storage::Pickers::FileSavePicker**](/uwp/api/Windows.Storage.Pickers.FileSavePicker)

### Prerequisites

-   You need an [**ID2D1DeviceContext**](/windows/win32/api/d2d1_1/nn-d2d1_1-id2d1devicecontext) object and an object containing [Direct2D](./direct2d-portal.md) content that implements [**ID2D1Image**](/windows/win32/api/d2d1/nn-d2d1-id2d1image) such as [**ID2D1Effect**](/windows/win32/api/d2d1_1/nn-d2d1_1-id2d1effect) or [**ID2D1Bitmap1**](/windows/win32/api/d2d1_1/nn-d2d1_1-id2d1bitmap1).

## Instructions

### Step 1: Get a destination file and stream

If you want to allow the user to select a destination file, you can use [**FileSavePicker**](/uwp/api/Windows.Storage.Pickers.FileSavePicker), open the returned file, and obtain an [**IStream**](/windows/desktop/api/objidl/nn-objidl-istream) to use with WIC.

Create a [**Windows::Storage::Pickers::FileSavePicker**](/uwp/api/Windows.Storage.Pickers.FileSavePicker) and set its parameters for image files. Call the [**PickSaveFileAsync**](/uwp/api/windows.storage.pickers.filesavepicker.picksavefileasync) method.


```C++
    Pickers::FileSavePicker^ savePicker = ref new Pickers::FileSavePicker();
    auto jpgExtensions = ref new Platform::Collections::Vector<Platform::String^>();
    pngExtensions->Append(".png");
    savePicker->FileTypeChoices->Insert("PNG file", pngExtensions);
    auto jpgExtensions = ref new Platform::Collections::Vector<Platform::String^>();
    jpgExtensions->Append(".jpg");
    savePicker->FileTypeChoices->Insert("JPEG file", jpgExtensions);
    savePicker->DefaultFileExtension = ".jpg";
    savePicker->SuggestedFileName = "SaveScreen";
    savePicker->SuggestedStartLocation = Pickers::PickerLocationId::PicturesLibrary;

    task<StorageFile^> fileTask(savePicker->PickSaveFileAsync());
```



Declare a completion handler to run after the file picker async operation returns. Use the [**GetResults**](/windows/desktop/WinRT/iasyncaction-getresults) method to retrieve the file and to get the file stream object.


```C++
    task<StorageFile^> fileTask(savePicker->PickSaveFileAsync());
    fileTask.then([=](StorageFile^ file) {
        if (file != nullptr)
        {
            // User selects a file.
            GUID wicFormat = GUID_ContainerFormatPng;
            if (file->FileType == ".jpg")
            {
                wicFormat = GUID_ContainerFormatJpeg;
            }
```



Obtain an [**IRandomAccessStream**](/previous-versions//hh438400(v=vs.85)) by calling [**OpenAsync**](/uwp/api/windows.storage.storagefile.openasync) on the file and getting the result of the async operation.


```C++
    task<Streams::IRandomAccessStream^> createStreamTask(file->OpenAsync(FileAccessMode::ReadWrite));
    createStreamTask.then([=](Streams::IRandomAccessStream^ randomAccessStream) {
```



Finally, use the [**CreateStreamOverRandomAccessStream**](/windows/desktop/api/shcore/nf-shcore-createstreamoverrandomaccessstream) method to convert the file stream. Windows Runtime APIs represent streams with [**IRandomAccessStream**](/previous-versions//hh438400(v=vs.85)), while WIC consumes [**IStream**](/windows/desktop/api/objidl/nn-objidl-istream).


```C++
    ComPtr<IStream> stream;
    DX::ThrowIfFailed(
        CreateStreamOverRandomAccessStream(randomAccessStream, IID_PPV_ARGS(&stream))
        );
```



> [!Note]  
> To use the [**CreateStreamOverRandomAccessStream**](/windows/desktop/api/shcore/nf-shcore-createstreamoverrandomaccessstream) function, you should include **shcore.h** in your project.

 

### Step 2: Get the WIC bitmap and frame encoder

[IWICBitmapEncoder](/windows/desktop/wic/-wic-imp-iwicbitmapencoder) and [IWICBitmapFrameEncode](/windows/desktop/wic/-wic-imp-iwicbitmapframeencode) provide the functionality to save imaging data to an encoded file format.

Create and initialize the encoder objects.


```C++
    ComPtr<IWICBitmapEncoder> wicBitmapEncoder;
    DX::ThrowIfFailed(
        wicFactory2->CreateEncoder(
            wicFormat,
            nullptr,    // No preferred codec vendor.
            &wicBitmapEncoder
            )
        );

    DX::ThrowIfFailed(
        wicBitmapEncoder->Initialize(
            stream,
            WICBitmapEncoderNoCache
            )
        );

    ComPtr<IWICBitmapFrameEncode> wicFrameEncode;
    DX::ThrowIfFailed(
        wicBitmapEncoder->CreateNewFrame(
            &wicFrameEncode,
            nullptr     // No encoder options.
            )
        );

    DX::ThrowIfFailed(
        wicFrameEncode->Initialize(nullptr)
        );
```



### Step 3: Get an IWICImageEncoder

[**IWICImageEncoder**](/windows/desktop/api/wincodec/nn-wincodec-iwicimageencoder) is a new interface in Windows 8. It can be created from [**IWICImagingFactory2**](/windows/desktop/api/wincodec/nn-wincodec-iwicimagingfactory2), which extends **IWICImagingFactory** and is also new for Windows 8.


```C++
ComPtr<IWICImagingFactory2> m_wicFactory;

DX::ThrowIfFailed(
    CoCreateInstance(
        CLSID_WICImagingFactory,
        nullptr,
        CLSCTX_INPROC_SERVER,
        IID_PPV_ARGS(&m_wicFactory)
        )
    );
```



Call [**IWICImagingFactory2::CreateImageEncoder**](/windows/desktop/api/wincodec/nf-wincodec-iwicimagingfactory2-createimageencoder). The first parameter is an [**ID2D1Device**](/windows/win32/api/d2d1_1/nn-d2d1_1-id2d1device) and must be the device on which the image you want to encode was created – you cannot mix images from different resource domains within a single [**IWICImageEncoder**](/windows/desktop/api/wincodec/nn-wincodec-iwicimageencoder).


```C++
    ComPtr<IWICImageEncoder> imageEncoder;
    DX::ThrowIfFailed(
        wicFactory2->CreateImageEncoder(
            d2dDevice.Get(),
            &imageEncoder
            )
       );
```



### Step 4: Write the Direct2D content using IWICImageEncoder

[**IWICImageEncoder**](/windows/desktop/api/wincodec/nn-wincodec-iwicimageencoder) can write a [Direct2D](./direct2d-portal.md) image into an image frame, a frame thumbnail, or the container thumbnail. You can then use [IWICBitmapEncoder](/windows/desktop/wic/-wic-imp-iwicbitmapencoder) and [IWICBitmapFrameEncode](/windows/desktop/wic/-wic-imp-iwicbitmapframeencode) to encode the imaging data to a file as normal.

Write the [Direct2D](./direct2d-portal.md) image to the frame. In this snippet we write an [**ID2D1Bitmap**](/windows/win32/api/d2d1/nn-d2d1-id2d1bitmap) that contains rasterized Direct2D content. However, you can provide any interface that implements [**ID2D1Image**](/windows/win32/api/d2d1/nn-d2d1-id2d1image).


```C++
    DX::ThrowIfFailed(
        imageEncoder->WriteFrame(
            d2dBitmap.Get(),
            wicFrameEncode.Get(),
            nullptr     // Use default WICImageParameter options.
            )
        );
```



> [!Note]  
> The [**ID2D1Image**](/windows/win32/api/d2d1/nn-d2d1-id2d1image) parameter must have been created on the [**ID2D1Device**](/windows/win32/api/d2d1_1/nn-d2d1_1-id2d1device) that was passed into [**IWICImagingFactory2::CreateImageEncoder**](/windows/desktop/api/wincodec/nf-wincodec-iwicimagingfactory2-createimageencoder).

 

Commit the WIC and stream resources to finalize the operation.


```C++
    DX::ThrowIfFailed(
        wicFrameEncode->Commit()
        );

    DX::ThrowIfFailed(
        wicBitmapEncoder->Commit()
        );

    // Flush all memory buffers to the next-level storage object.
    DX::ThrowIfFailed(
        stream->Commit(STGC_DEFAULT)
        );
```



> [!Note]  
> Some implementations of [**IStream**](/windows/desktop/api/objidl/nn-objidl-istream) do not implement the [**Commit**](/windows/desktop/api/objidl/nf-objidl-istream-commit) method and return **E\_NOTIMPL**.

 

Now you have a file containing the [Direct2D](./direct2d-portal.md) image.

## Complete example

Here the full code for this example.

```cpp
ComPtr<IWICImagingFactory2> m_wicFactory;

DX::ThrowIfFailed(
    CoCreateInstance(
        CLSID_WICImagingFactory,
        nullptr,
        CLSCTX_INPROC_SERVER,
        IID_PPV_ARGS(&m_wicFactory)
        )
    );

void SaveAsImageFile::SaveBitmapToFile()
{
    // Prepare a file picker for customers to input image file name.
    Pickers::FileSavePicker^ savePicker = ref new Pickers::FileSavePicker();
    auto pngExtensions = ref new Platform::Collections::Vector<Platform::String^>();
    pngExtensions->Append(".png");
    savePicker->FileTypeChoices->Insert("PNG file", pngExtensions);
    auto jpgExtensions = ref new Platform::Collections::Vector<Platform::String^>();
    jpgExtensions->Append(".jpg");
    savePicker->FileTypeChoices->Insert("JPEG file", jpgExtensions);
    auto bmpExtensions = ref new Platform::Collections::Vector<Platform::String^>();
    bmpExtensions->Append(".bmp");
    savePicker->FileTypeChoices->Insert("BMP file", bmpExtensions);
    savePicker->DefaultFileExtension = ".png";
    savePicker->SuggestedFileName = "SaveScreen";
    savePicker->SuggestedStartLocation = Pickers::PickerLocationId::PicturesLibrary;

    task<StorageFile^> fileTask(savePicker->PickSaveFileAsync());
    fileTask.then([=](StorageFile^ file) {
        if (file != nullptr)
        {
            // User selects a file.
            m_imageFileName = file->Name;
            GUID wicFormat = GUID_ContainerFormatPng;
            if (file->FileType == ".bmp")
            {
                wicFormat = GUID_ContainerFormatBmp;
            }
            else if (file->FileType == ".jpg")
            {
                wicFormat = GUID_ContainerFormatJpeg;
            }

            // Retrieve a stream from the file.
            task<Streams::IRandomAccessStream^> createStreamTask(file->OpenAsync(FileAccessMode::ReadWrite));
            createStreamTask.then([=](Streams::IRandomAccessStream^ randomAccessStream) {
                // Convert the RandomAccessStream to an IStream.
                ComPtr<IStream> stream;
                DX::ThrowIfFailed(
                    CreateStreamOverRandomAccessStream(randomAccessStream, IID_PPV_ARGS(&stream))
                    );

                SaveBitmapToStream(m_d2dTargetBitmap, m_wicFactory, m_d2dContext, wicFormat, stream.Get());
            });
        }
    });
}

// Save render target bitmap to a stream using WIC.
void SaveAsImageFile::SaveBitmapToStream(
    _In_ ComPtr<ID2D1Bitmap1> d2dBitmap,
    _In_ ComPtr<IWICImagingFactory2> wicFactory2,
    _In_ ComPtr<ID2D1DeviceContext> d2dContext,
    _In_ REFGUID wicFormat,
    _In_ IStream* stream
    )
{
    // Create and initialize WIC Bitmap Encoder.
    ComPtr<IWICBitmapEncoder> wicBitmapEncoder;
    DX::ThrowIfFailed(
        wicFactory2->CreateEncoder(
            wicFormat,
            nullptr,    // No preferred codec vendor.
            &wicBitmapEncoder
            )
        );

    DX::ThrowIfFailed(
        wicBitmapEncoder->Initialize(
            stream,
            WICBitmapEncoderNoCache
            )
        );

    // Create and initialize WIC Frame Encoder.
    ComPtr<IWICBitmapFrameEncode> wicFrameEncode;
    DX::ThrowIfFailed(
        wicBitmapEncoder->CreateNewFrame(
            &wicFrameEncode,
            nullptr     // No encoder options.
            )
        );

    DX::ThrowIfFailed(
        wicFrameEncode->Initialize(nullptr)
        );

    // Retrieve D2D Device.
    ComPtr<ID2D1Device> d2dDevice;
    d2dContext->GetDevice(&d2dDevice);

    // Create IWICImageEncoder.
    ComPtr<IWICImageEncoder> imageEncoder;
    DX::ThrowIfFailed(
        wicFactory2->CreateImageEncoder(
            d2dDevice.Get(),
            &imageEncoder
            )
       );

    DX::ThrowIfFailed(
        imageEncoder->WriteFrame(
            d2dBitmap.Get(),
            wicFrameEncode.Get(),
            nullptr     // Use default WICImageParameter options.
            )
        );

    DX::ThrowIfFailed(
        wicFrameEncode->Commit()
        );

    DX::ThrowIfFailed(
        wicBitmapEncoder->Commit()
        );

    // Flush all memory buffers to the next-level storage object.
    DX::ThrowIfFailed(
        stream->Commit(STGC_DEFAULT)
        );
}

```



 

 