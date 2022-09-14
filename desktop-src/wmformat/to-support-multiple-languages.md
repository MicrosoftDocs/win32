---
title: To Support Multiple Languages
description: To Support Multiple Languages
ms.assetid: b0061de4-d725-455f-9d9b-5bd0dbe8ff53
keywords:
- Windows Media Format SDK,supporting multiple languages
- Windows Media Format SDK,multiple language support
- Windows Media Format SDK,language support
- Advanced Systems Format (ASF),supporting multiple languages
- ASF (Advanced Systems Format),supporting multiple languages
- Advanced Systems Format (ASF),multiple language support
- ASF (Advanced Systems Format),multiple language support
- Advanced Systems Format (ASF),language support
- ASF (Advanced Systems Format),language support
ms.topic: article
ms.date: 05/31/2018
---

# To Support Multiple Languages

You can support multiple languages both in streams and in metadata. The core of multiple language support in the Windows Media Format SDK is the [**IWMLanguageList**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmlanguagelist) interface, which maintains a list of the languages supported. The language list gives each supported language an index, which is used in various objects in the SDK when dealing with the multiple languages.

The [**IWMLanguageList::AddLanguageByRFC1766String**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmlanguagelist-addlanguagebyrfc1766string) method adds a language to the list. You can identify the languages already in the list by obtaining the total number of languages with [**IWMLanguageList::GetLanguageCount**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmlanguagelist-getlanguagecount) and then looping through the languages calling [**IWMLanguageList::GetLanguageDetails**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmlanguagelist-getlanguagedetails) for each. The language index is zero based.

## To Configure Mutual Exclusion by Language

Configuring a simple mutual exclusion object by language is very simple. Each stream is now associated with a language. The language associated with a stream can be set using [**IWMStreamConfig3::SetLanguage**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmstreamconfig3-setlanguage). After all of the mutually exclusive streams are configured, simply create a mutual exclusion object as you would for any other type. Then call [**IWMMutualExclusion::SetType**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmmutualexclusion-settype) passing CLSID\_WMMUTEX\_Language for the type.

Streams that are mutually exclusive by language become more complicated when the exclusive streams are also mutually exclusive by bit rate. In this case you must use mutually exclusive records, by performing the following steps:

1.  Create a mutual exclusion object for the streams of differing bit rates in each language. For more information about creating a mutual exclusion object by bit rate, see [Using Multiple Bit Rate Mutual Exclusion](using-multiple-bit-rate-mutual-exclusion.md).
2.  Create a mutual exclusion object. Call [**IWMMutualExclusion::SetType**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmmutualexclusion-settype) and pass CLSID\_WMMUTEX\_Language to specify exclusivity by language.
3.  Obtain a pointer to the [**IWMMutualExclusion2**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmmutualexclusion2) interface of the mutual exclusion object created in step 2 by calling the **QueryInterface** method of [**IWMMutualExclusion**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmmutualexclusion).
4.  Call the [**IWMMutualExclusion2::AddRecord**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmmutualexclusion2-addrecord) method once for each language, to create stream records that will be mutually exclusive.
5.  For each record created in step 4, add the streams of the appropriate language with calls to [**IWMMutualExclusion2::AddStreamForRecord**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmmutualexclusion2-addstreamforrecord).

## To Read Files with Multiple Languages

The reader object provides methods to identify the available languages of streams in a file. You can retrieve the number of supported languages for an output by calling [**IWMReaderAdvanced4::GetLanguageCount**](/previous-versions/windows/desktop/api/wmsdkidl/nf-wmsdkidl-iwmreaderadvanced4-getlanguagecount). You can then retrieve details about each language with calls to [**IWMReaderAdvanced4::GetLanguage**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreaderadvanced4-getlanguage).

You can specify the language to play by passing the index of that language to the reader with a call to [**IWMReaderAdvanced2::SetOutputSetting**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreaderadvanced2-setoutputsetting). This will select the specified language while maintaining automatic stream selection for any other mutual exclusion objects in the file.

## Related topics

<dl> <dt>

[**Advanced Topics**](advanced-topics.md)
</dt> <dt>

[**IWMLanguageList Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmlanguagelist)
</dt> <dt>

[**IWMMutualExclusion Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmmutualexclusion)
</dt> <dt>

[**IWMMutualExclusion2 Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmmutualexclusion2)
</dt> <dt>

[**IWMReaderAdvanced2 Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreaderadvanced2)
</dt> <dt>

[**IWMReaderAdvanced4 Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreaderadvanced4)
</dt> <dt>

[**IWMStreamConfig3 Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmstreamconfig3)
</dt> </dl>

 

 




