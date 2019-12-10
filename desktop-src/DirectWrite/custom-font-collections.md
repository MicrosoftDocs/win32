---
title: Custom Font Collections (Windows 7/8)
description: DirectWrite provides access to the system font collection by using the IDWriteFactory GetSystemFontCollection method.
ms.assetid: ec892904-6778-4fbd-93b4-62d0db5b82ea
ms.topic: article
ms.date: 05/31/2018
---

# Custom Font Collections (Windows 7/8)

[DirectWrite](direct-write-portal.md) provides access to the system font collection by using the [**IDWriteFactory::GetSystemFontCollection**](https://msdn.microsoft.com/library/Dd368208(v=VS.85).aspx) method. This is the font collection that is most frequently used. However some applications have to use fonts that are not installed on the system, such as from included font files or font files embedded in the application.

If the fonts that you want are not in the system font collection, you can create a custom font collection derived from [**IDWriteFontCollection**](https://msdn.microsoft.com/library/Dd368214(v=VS.85).aspx).

This overview consists of the following parts:

-   [Registering and unregistering a Font Collection Loader](#registering-and-unregistering-a-font-collection-loader)
-   [IDWriteFontCollectionLoader](#idwritefontcollectionloader)
-   [IDWriteFontFileEnumerator](#idwritefontfileenumerator)
-   [CreateCustomFontFileReference](#createcustomfontfilereference)
-   [IDWriteFontFileLoader](#idwritefontfileloader)
-   [IDWriteFontFileStream](#idwritefontfilestream)

## Registering and unregistering a Font Collection Loader

You register a font collection loader by using the [**IDWriteFactory::RegisterFontCollectionLoader**](https://msdn.microsoft.com/library/Dd368209(v=VS.85).aspx) method and passing it an [**IDWriteFontCollectionLoader**](https://msdn.microsoft.com/library/Dd368215(v=VS.85).aspx) interface implemented by the application as a singleton object. This object will load the fonts when the custom collection is requested. Both the system font collection and custom font collections are cached, so the fonts are only loaded one time.

The font collection loader must be unloaded eventually by using the [**IDWriteFactory::UnregisterFontCollectionLoader**](https://msdn.microsoft.com/library/Dd368211(v=VS.85).aspx).

> [!Note]  
> Registering the font collection loader adds to the reference count; do not call [**UnregisterFontCollectionLoader**](https://msdn.microsoft.com/library/Dd368211(v=VS.85).aspx) from within the destructor or the collection loader object will never be unregistered.

 

## IDWriteFontCollectionLoader

You create an [**IDWriteFontFileEnumerator**](https://msdn.microsoft.com/library/Dd371063(v=VS.85).aspx) object by using the [**IDWriteFactory::CreateCustomFontCollection**](https://msdn.microsoft.com/library/Dd368186(v=VS.85).aspx) and passing it an application-defined key. The key is a void pointer and the data type, format, and meaning are defined by the application and are opaque to the font system.

Whereas the key can be anything, [DirectWrite](direct-write-portal.md) requires that each key is both:

-   Unique to a single font collection within the scope of the loader.
-   Valid until the loader is unregistered using the factory.

When the [**CreateCustomFontCollection**](https://msdn.microsoft.com/library/Dd368186(v=VS.85).aspx) method is called, [DirectWrite](direct-write-portal.md) calls back to an [**IDWriteFontCollectionLoader**](https://msdn.microsoft.com/library/Dd368215(v=VS.85).aspx) interface implemented as a singleton object by the application. The [**IDWriteFontCollectionLoader::CreateEnumeratorFromKey**](https://msdn.microsoft.com/library/Dd368216(v=VS.85).aspx) callback method is used by DirectWrite to retrieve an [**IDWriteFontFileEnumerator**](https://msdn.microsoft.com/library/Dd371063(v=VS.85).aspx) object implemented by the application. The [**IDWriteFactory**](https://msdn.microsoft.com/library/Dd368183(v=VS.85).aspx) object that is being used to create the collection is passed to this method and should be used by the font file enumerator to create the [**IDWriteFontFile**](https://msdn.microsoft.com/library/Dd371060(v=VS.85).aspx) objects to be included in the collection.

The key passed to this method identifies the font collection and is the same key passed to [**CreateCustomFontCollection**](https://msdn.microsoft.com/library/Dd368186(v=VS.85).aspx).

## IDWriteFontFileEnumerator

The application-defined [**IDWriteFontFileEnumerator**](https://msdn.microsoft.com/library/Dd371063(v=VS.85).aspx) object that was created by the [**CreateEnumeratorFromKey**](https://msdn.microsoft.com/library/Dd368216(v=VS.85).aspx) method is used to enumerate the font files in a collection, creating an [**IDWriteFontFile**](https://msdn.microsoft.com/library/Dd371060(v=VS.85).aspx) object for each file. The [**IDWriteFontFileEnumerator::MoveNext**](https://msdn.microsoft.com/library/Dd371071(v=VS.85).aspx) method changes the position to the next font file. If there is a file at the position, it will set the *hasCurrentFile* to **TRUE**. Otherwise it will be set to **FALSE** and the method will return **S\_OK**.

> [!Note]  
> The font file enumerator must start positioned before the first element and advanced at the first call to [**MoveNext**](https://msdn.microsoft.com/library/Dd371071(v=VS.85).aspx).

 

An [**IDWriteFontFile**](https://msdn.microsoft.com/library/Dd371060(v=VS.85).aspx) object is output by the [**IDWriteFontFileEnumerator::GetCurrentFontFile**](https://msdn.microsoft.com/library/Dd371067(v=VS.85).aspx) method. If there is no font file at the current position, because [**MoveNext**](https://msdn.microsoft.com/library/Dd371071(v=VS.85).aspx) has not yet been called or hasCurrentFile was set to **FALSE**, then **GetCurrentFontFile** will return **E\_FAIL**.

## CreateCustomFontFileReference

The [**IDWriteFontFile**](https://msdn.microsoft.com/library/Dd371060(v=VS.85).aspx) object output by[**GetCurrentFontFile**](https://msdn.microsoft.com/library/Dd371067(v=VS.85).aspx) can be created by calling [**IDWriteFactory::CreateCustomFontFileReference**](https://msdn.microsoft.com/library/Dd368188(v=VS.85).aspx). The font file reference key identifies a specific font file reference and must be unique within the font file loader that will load the file.

## IDWriteFontFileLoader

The [**CreateCustomFontFileReference**](https://msdn.microsoft.com/library/Dd368188(v=VS.85).aspx) method takes an [**IDWriteFontFileLoader**](https://msdn.microsoft.com/library/Dd371075(v=VS.85).aspx) object implemented by the application that is used to load the font. The [**IDWriteFontFileLoader::CreateStreamFromKey**](https://msdn.microsoft.com/library/Dd371077(v=VS.85).aspx) callback method is passed the key and outputs an [**IDWriteFontFileStream**](https://msdn.microsoft.com/library/Dd371081(v=VS.85).aspx) object.

## IDWriteFontFileStream

The application-implemented [**IDWriteFontFileStream**](https://msdn.microsoft.com/library/Dd371081(v=VS.85).aspx) object provides the font file data for a font file reference from a custom font file loader. Together with the file size and last write time, it provides a method ([**ReadFileFragment**](https://msdn.microsoft.com/library/Dd371091(v=VS.85).aspx)) for retrieving file fragments that are to be compiled into an [**IDWriteFontFile**](https://msdn.microsoft.com/library/Dd371060(v=VS.85).aspx) object.

> [!Note]  
> [**ReadFileFragment**](https://msdn.microsoft.com/library/Dd371091(v=VS.85).aspx) implementations should return an error if the requested fragment is outside the file bounds.

 

An [**IDWriteFontFileStream**](https://msdn.microsoft.com/library/Dd371081(v=VS.85).aspx) can get the font file contents from anywhere, such as the local hard disk drive, or embedded resources.

 

 




