---
title: To Support Multiple Languages
description: To Support Multiple Languages
ms.assetid: 'b0061de4-d725-455f-9d9b-5bd0dbe8ff53'
keywords: ["Windows Media Format SDK,supporting multiple languages", "Windows Media Format SDK,multiple language support", "Windows Media Format SDK,language support", "Advanced Systems Format (ASF),supporting multiple languages", "ASF (Advanced Systems Format),supporting multiple languages", "Advanced Systems Format (ASF),multiple language support", "ASF (Advanced Systems Format),multiple language support", "Advanced Systems Format (ASF),language support", "ASF (Advanced Systems Format),language support"]
---

# To Support Multiple Languages

You can support multiple languages both in streams and in metadata. The core of multiple language support in the Windows Media Format SDK is the [**IWMLanguageList**](iwmlanguagelist.md) interface, which maintains a list of the languages supported. The language list gives each supported language an index, which is used in various objects in the SDK when dealing with the multiple languages.

The [**IWMLanguageList::AddLanguageByRFC1766String**](iwmlanguagelist-addlanguagebyrfc1766string.md) method adds a language to the list. You can identify the languages already in the list by obtaining the total number of languages with [**IWMLanguageList::GetLanguageCount**](iwmlanguagelist-getlanguagecount.md) and then looping through the languages calling [**IWMLanguageList::GetLanguageDetails**](iwmlanguagelist-getlanguagedetails.md) for each. The language index is zero based.

## To Configure Mutual Exclusion by Language

Configuring a simple mutual exclusion object by language is very simple. Each stream is now associated with a language. The language associated with a stream can be set using [**IWMStreamConfig3::SetLanguage**](iwmstreamconfig3-setlanguage.md). After all of the mutually exclusive streams are configured, simply create a mutual exclusion object as you would for any other type. Then call [**IWMMutualExclusion::SetType**](iwmmutualexclusion-settype.md) passing CLSID\_WMMUTEX\_Language for the type.

Streams that are mutually exclusive by language become more complicated when the exclusive streams are also mutually exclusive by bit rate. In this case you must use mutually exclusive records, by performing the following steps:

1.  Create a mutual exclusion object for the streams of differing bit rates in each language. For more information about creating a mutual exclusion object by bit rate, see [Using Multiple Bit Rate Mutual Exclusion](using-multiple-bit-rate-mutual-exclusion.md).
2.  Create a mutual exclusion object. Call [**IWMMutualExclusion::SetType**](iwmmutualexclusion-settype.md) and pass CLSID\_WMMUTEX\_Language to specify exclusivity by language.
3.  Obtain a pointer to the [**IWMMutualExclusion2**](iwmmutualexclusion2.md) interface of the mutual exclusion object created in step 2 by calling the **QueryInterface** method of [**IWMMutualExclusion**](iwmmutualexclusion.md).
4.  Call the [**IWMMutualExclusion2::AddRecord**](iwmmutualexclusion2-addrecord.md) method once for each language, to create stream records that will be mutually exclusive.
5.  For each record created in step 4, add the streams of the appropriate language with calls to [**IWMMutualExclusion2::AddStreamForRecord**](iwmmutualexclusion2-addstreamforrecord.md).

## To Read Files with Multiple Languages

The reader object provides methods to identify the available languages of streams in a file. You can retrieve the number of supported languages for an output by calling [**IWMReaderAdvanced4::GetLanguageCount**](iwmreaderadvanced4-getlanguagecount.md). You can then retrieve details about each language with calls to [**IWMReaderAdvanced4::GetLanguage**](iwmreaderadvanced4-getlanguage.md).

You can specify the language to play by passing the index of that language to the reader with a call to [**IWMReaderAdvanced2::SetOutputSetting**](iwmreaderadvanced2-setoutputsetting.md). This will select the specified language while maintaining automatic stream selection for any other mutual exclusion objects in the file.

## Related topics

<dl> <dt>

[**Advanced Topics**](advanced-topics.md)
</dt> <dt>

[**IWMLanguageList Interface**](iwmlanguagelist.md)
</dt> <dt>

[**IWMMutualExclusion Interface**](iwmmutualexclusion.md)
</dt> <dt>

[**IWMMutualExclusion2 Interface**](iwmmutualexclusion2.md)
</dt> <dt>

[**IWMReaderAdvanced2 Interface**](iwmreaderadvanced2.md)
</dt> <dt>

[**IWMReaderAdvanced4 Interface**](iwmreaderadvanced4.md)
</dt> <dt>

[**IWMStreamConfig3 Interface**](iwmstreamconfig3.md)
</dt> </dl>

 

 




