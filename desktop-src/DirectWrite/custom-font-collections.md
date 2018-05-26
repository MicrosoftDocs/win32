---
title: Custom Font Collections (Windows 7/8)
description: DirectWrite provides access to the system font collection by using the IDWriteFactory GetSystemFontCollection method.
ms.assetid: ec892904-6778-4fbd-93b4-62d0db5b82ea
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Custom Font Collections (Windows 7/8)

[DirectWrite](direct-write-portal.md) provides access to the system font collection by using the [**IDWriteFactory::GetSystemFontCollection**](/windows/win32/dwrite/?branch=master) method. This is the font collection that is most frequently used. However some applications have to use fonts that are not installed on the system, such as from included font files or font files embedded in the application.

If the fonts that you want are not in the system font collection, you can create a custom font collection derived from [**IDWriteFontCollection**](/windows/win32/dwrite/?branch=master).

This overview consists of the following parts:

-   [Registering and unregistering a Font Collection Loader](#registering-and-unregistering-a-font-collection-loader)
-   [IDWriteFontCollectionLoader](#idwritefontcollectionloader)
-   [IDWriteFontFileEnumerator](#idwritefontfileenumerator)
-   [CreateCustomFontFileReference](#createcustomfontfilereference)
-   [IDWriteFontFileLoader](#idwritefontfileloader)
-   [IDWriteFontFileStream](#idwritefontfilestream)

## Registering and unregistering a Font Collection Loader

You register a font collection loader by using the [**IDWriteFactory::RegisterFontCollectionLoader**](/windows/win32/dwrite/?branch=master) method and passing it an [**IDWriteFontCollectionLoader**](/windows/win32/dwrite/?branch=master) interface implemented by the application as a singleton object. This object will load the fonts when the custom collection is requested. Both the system font collection and custom font collections are cached, so the fonts are only loaded one time.

The font collection loader must be unloaded eventually by using the [**IDWriteFactory::UnregisterFontCollectionLoader**](/windows/win32/dwrite/?branch=master).

> [!Note]  
> Registering the font collection loader adds to the reference count; do not call [**UnregisterFontCollectionLoader**](/windows/win32/dwrite/?branch=master) from within the destructor or the collection loader object will never be unregistered.

 

## IDWriteFontCollectionLoader

You create an [**IDWriteFontFileEnumerator**](/windows/win32/dwrite/?branch=master) object by using the [**IDWriteFactory::CreateCustomFontCollection**](/windows/win32/dwrite/?branch=master) and passing it an application-defined key. The key is a void pointer and the data type, format, and meaning are defined by the application and are opaque to the font system.

Whereas the key can be anything, [DirectWrite](direct-write-portal.md) requires that each key is both:

-   Unique to a single font collection within the scope of the loader.
-   Valid until the loader is unregistered using the factory.

When the [**CreateCustomFontCollection**](/windows/win32/dwrite/?branch=master) method is called, [DirectWrite](direct-write-portal.md) calls back to an [**IDWriteFontCollectionLoader**](/windows/win32/dwrite/?branch=master) interface implemented as a singleton object by the application. The [**IDWriteFontCollectionLoader::CreateEnumeratorFromKey**](/windows/win32/dwrite/?branch=master) callback method is used by DirectWrite to retrieve an [**IDWriteFontFileEnumerator**](/windows/win32/dwrite/?branch=master) object implemented by the application. The [**IDWriteFactory**](/windows/win32/dwrite/?branch=master) object that is being used to create the collection is passed to this method and should be used by the font file enumerator to create the [**IDWriteFontFile**](/windows/win32/dwrite/?branch=master) objects to be included in the collection.

The key passed to this method identifies the font collection and is the same key passed to [**CreateCustomFontCollection**](/windows/win32/dwrite/?branch=master).

## IDWriteFontFileEnumerator

The application-defined [**IDWriteFontFileEnumerator**](/windows/win32/dwrite/?branch=master) object that was created by the [**CreateEnumeratorFromKey**](/windows/win32/dwrite/?branch=master) method is used to enumerate the font files in a collection, creating an [**IDWriteFontFile**](/windows/win32/dwrite/?branch=master) object for each file. The [**IDWriteFontFileEnumerator::MoveNext**](/windows/win32/dwrite/?branch=master) method changes the position to the next font file. If there is a file at the position, it will set the *hasCurrentFile* to **TRUE**. Otherwise it will be set to **FALSE** and the method will return **S\_OK**.

> [!Note]  
> The font file enumerator must start positioned before the first element and advanced at the first call to [**MoveNext**](/windows/win32/dwrite/?branch=master).

 

An [**IDWriteFontFile**](/windows/win32/dwrite/?branch=master) object is output by the [**IDWriteFontFileEnumerator::GetCurrentFontFile**](/windows/win32/dwrite/?branch=master) method. If there is no font file at the current position, because [**MoveNext**](/windows/win32/dwrite/?branch=master) has not yet been called or hasCurrentFile was set to **FALSE**, then **GetCurrentFontFile** will return **E\_FAIL**.

## CreateCustomFontFileReference

The [**IDWriteFontFile**](/windows/win32/dwrite/?branch=master) object output by[**GetCurrentFontFile**](/windows/win32/dwrite/?branch=master) can be created by calling [**IDWriteFactory::CreateCustomFontFileReference**](/windows/win32/dwrite/?branch=master). The font file reference key identifies a specific font file reference and must be unique within the font file loader that will load the file.

## IDWriteFontFileLoader

The [**CreateCustomFontFileReference**](/windows/win32/dwrite/?branch=master) method takes an [**IDWriteFontFileLoader**](/windows/win32/dwrite/?branch=master) object implemented by the application that is used to load the font. The [**IDWriteFontFileLoader::CreateStreamFromKey**](/windows/win32/dwrite/?branch=master) callback method is passed the key and outputs an [**IDWriteFontFileStream**](/windows/win32/dwrite/?branch=master) object.

## IDWriteFontFileStream

The application-implemented [**IDWriteFontFileStream**](/windows/win32/dwrite/?branch=master) object provides the font file data for a font file reference from a custom font file loader. Together with the file size and last write time, it provides a method ([**ReadFileFragment**](/windows/win32/dwrite/?branch=master)) for retrieving file fragments that are to be compiled into an [**IDWriteFontFile**](/windows/win32/dwrite/?branch=master) object.

> [!Note]  
> [**ReadFileFragment**](/windows/win32/dwrite/?branch=master) implementations should return an error if the requested fragment is outside the file bounds.

 

An [**IDWriteFontFileStream**](/windows/win32/dwrite/?branch=master) can get the font file contents from anywhere, such as the local hard disk drive, or embedded resources.

 

 




